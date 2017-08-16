import Queue
import struct
from copy import copy
from gevent import Greenlet
from gevent.server import DatagramServer, _udp_socket
from gevent.socket import getaddrinfo
from operator import itemgetter
from socket import AF_INET, AF_INET6, SOCK_DGRAM, gaierror
from thread import start_new_thread
from urlparse import urlparse, urlunparse, ParseResult
from werkzeug.datastructures import MultiDict

from dtls import do_patch
from dtls.sslconnection import SSLConnection
from funcy import pluck

from coap import connection
from coap import constants
from coap import options
from coap.coapy.coapy import http2coap_codes
from coap.coapy.coapy.options import UnrecognizedOptionError
from futile.collections import get_iterable
from futile.logging import LoggerMixin
from openmtc_scl.transportdomain.util import (encode_error,
                                              serialize_generic_result)
from openmtc_server.transportdomain import (Request as GenericRequest,
                                            RequestMethod, ErrorResponse)
from .util import is_ipv4, is_ipv6


class DtlsServer(DatagramServer):
    """DtlsServer extends the Gevent DatagramServer with DTLS support"""

    def __init__(self, listener, handle=None, backlog=None, spawn='default',
                 **ssl_args):
        """Initializes the Server

        Calls init_socket()

        :param listener: Tuple (address, port) used by the server
        :param handle: function called when application data is recieved
        :param ssl_args: contains two keywords: "keyfile" and "certfile"
                         containing paths to respective files
        """
        DatagramServer.__init__(self, listener, handle=handle, spawn=spawn)
        self.backlog = backlog
        self.ssl_args = ssl_args

    def init_socket(self):
        """Initalizes listening socket and SSL Connection"""
        if not hasattr(self, 'socket'):
            self.socket = self.get_listener(self.address, self.backlog,
                                            self.family)
            self.address = self.socket.getsockname()

        self._handle = self.handle
        self._socket = self.socket

        self.scn = SSLConnection(
            self._socket,
            keyfile=self.ssl_args["keyfile"],
            certfile=self.ssl_args["certfile"],
            ca_certs=self.ssl_args["certfile"],
            server_side=True,
            do_handshake_on_connect=False
        )

    @classmethod
    def get_listener(cls, address, backlog=None, family=None):
        """Creates a datagram socket used to listen to incoming requests"""
        return _udp_socket(address, reuse_addr=cls.reuse_addr, family=family)

    def sendto(self, buff, remote):
        """Overwrites the DatagramServer sendto in order to send an encrypted
         reply

        :param buff: Byte buffer to be encrypted and sent
        :param remote: Unused parameter, since an SSL connection exists
        """
        self.conn.write(buff)

    def do_handshake(self, remote):
        """Performs the DTLS handshake before recieving data.

        Calls the message handler with tuple(data buffer, tuple(client IP,
        client Port))

        :param remote: tuple(client IP, client Port)
        """
        # TODO: Error handling: send something in case of SSL socket timeout
        # Accepting
        self.conn = self.scn.accept()[0]
        self.conn.get_socket(True).settimeout(5)

        # Handshake
        self.conn.do_handshake()

        # Reading the CoAP message
        message = self.conn.read()

        self._handle(message, remote)

    def do_read(self):
        """Overwrites the DatagramServer do_read in order to perform the DTLS
        handshake before receiving data.

        This function is triggered automatically by the DatagramServer when an
        I/O operation is detected.
        """
        peer_address = self.scn.listen()
        if peer_address:
            # FIXME: need to join these on stop()
            Greenlet.spawn(self.do_handshake, peer_address)


class CoapServer(LoggerMixin):
    block_size_exponent = 10

    """Server handling CoAP requests and generates RequestIndications."""
    DEFAULT_CONTENT_TYPE = "application/json"
    __cached_addresses = {}

    def __init__(self, request_handler, connector, address="0.0.0.0",
                 server_port=5682, ssl_args=None, *args, **kw):
        """Initializes the CoAP server.

        :param request_handler: Handler called with generated RequestIndications
        :param connector: Base uri used to reach this server (coap://IP:PORT or
                         coaps://IP:PORT)
        :param address: IP listening to
        :param server_port: Port listening to
        :param ssl_args: contains two keywords: "keyfile" and "certfile"
                         containing paths to respective files, None for regular
                         CoAP
        """
        self.server_port = server_port
        self.connector = connector
        self.request_handler = request_handler
        self.subs = {}
        self.address = address
        if address == "::":
            self.__addresses = self._get_addresses(AF_INET6) | \
                               self._get_addresses(AF_INET)
            self._resolve_host = self._resolve_host_ipv6
        elif address in ("", "0.0.0.0"):
            self.__addresses = self._get_addresses(AF_INET)
        else:
            self.__addresses = get_iterable(address)

        do_patch()

        self.logger.debug("Starting Coap Server on %s:%s" % (self.address,
                                                             self.server_port))

        if ssl_args:
            self.server = DtlsServer((address, self.server_port),
                                     self.handle_request, **ssl_args)
        else:
            self.server = DatagramServer((address, self.server_port),
                                         self.handle_request)

        self.block1_pending_payload = {}
        self.block2_pending_payload = {}
        self.actual_requests = []
        self.req_queue = Queue.Queue()
        start_new_thread(self.request_runner, ())

    def _add_headers(self, msg):
        """Reads the set of UriQuery options and extract additional headers in
        a dict.

        Used mainly for Store and Forward functionnalities, recognized headers
        are formated as: X-etsi-<headername>

        :param msg: CoAP message containing UriQuery options
        :return: Dictionnary containing headers
        """
        params = MultiDict()
        opts = msg.findOption(options.UriQuery)
        self.logger.debug("Message: %s", msg)
        self.logger.debug("List of UriQuery options: %s", opts)
        if not opts:
            return params
        for opt in opts:
            try:
                opt_split = opt.value.split("=")
                opt_name = opt_split[0]
                opt_value = opt_split[1]
                try:
                    opt_type = opt_name.split('-')[2]
                except:
                    opt_type = opt_name
                params.add(opt_type, opt_value)
            except:
                self.logger.debug("Unknown header : %s" % opt.value)
        return params

    # TODO: map to new scheme
    def _handle_observe(self, path, msg, rx_record, obs):
        """Handles the presence of the Observe Option.

        Creates or deletes a subscription to a resource depending on the Observe
        value.

        :param path: Resource path
        :param msg: CoAP message
        :param obs: Observe option Object
        """

        params = self._add_headers(msg)
        username = None

        accept = self._get_accept(msg)

        if obs.value == 0:
            sub_path = path + "/subscriptions"
            sub_payload = ('{"subscription": {"contact": "coap://%s:%s"}}' %
                           (self.remote, ))
            request = GenericRequest(RequestMethod.create, sub_path,
                                     sub_payload, self.DEFAULT_CONTENT_TYPE,
                                     id=rx_record.message.token,
                                     username=username, params=params,
                                     accept=accept, connector=self.connector)
            p = self.request_handler(request)

            def __handle_result(result):
                if not (self.remote in self.subs):
                    self.subs[self.remote] = {}
                self.subs[self.remote][path] = result.resourceURI

            p.then(__handle_result)

        else:
            request = GenericRequest(RequestMethod.delete,
                                     self.subs[self.remote][path],
                                     id=rx_record.message.token,
                                     username=username, params=params,
                                     accept=accept, connector=self.connector)
            self.request_handler(request)
            del self.subs[self.remote][path]
            if self.subs[self.remote] == {}:
                del self.subs[self.remote]

    def _generic_map_put(self, path, msg, rx_record):
        """Creates an generic update Request Object from a path and a CoAP
        message.

        :param path: Resource path
        :param msg: CoAP message
        :return: Request Object
        """
        params = self._add_headers(msg)
        username = None

        accept = self._get_accept(msg)

        return GenericRequest(RequestMethod.update, path, msg.payload,
                              msg.content_type, id=rx_record.message.token,
                              username=username, params=params, accept=accept,
                              connector=self.connector)

    def _generic_map_post(self, path, msg, rx_record):
        """Creates an generic create Request Object from a path and a CoAP
        message.

        :param path: Resource path
        :param msg: CoAP message
        :return: Request Object
        """
        method = RequestMethod.create
        # TODO: does this need to be done more generically?
        if msg.payload.startswith("m2m:operation="):
            _, _, rest = msg.payload.partition("=")
            if rest:
                method_value = rest[0]
                msg.payload = rest[1:]
                if int(method_value) == 5:
                    method = RequestMethod.notify

        params = self._add_headers(msg)
        username = None

        accept = self._get_accept(msg)

        return GenericRequest(method, path, msg.payload, msg.content_type,
                              id=rx_record.message.token, username=username,
                              params=params, accept=accept,
                              connector=self.connector)

    def _generic_map_get(self, path, msg, rx_record):
        """Creates an generic retrieve Request Object from a path and a CoAP
        message

        Checks for the Observe option and handles it if needed.

        :param path: Resource path
        :param msg: CoAP message
        :return: Request Object
        """
        obs = msg.findOption(options.Observe)
        if obs:
            return self._handle_observe(path, msg, rx_record, obs)

        params = self._add_headers(msg)
        username = None

        accept = self._get_accept(msg)

        return GenericRequest(RequestMethod.retrieve, path,
                              id=rx_record.message.token, username=username,
                              params=params, accept=accept,
                              connector=self.connector)

    def _generic_map_delete(self, path, msg, rx_record):
        """Creates an generic delete Request Object from a path and a CoAP
        message

        :param path: Resource path
        :param msg: CoAP message
        :return: Request Object
        """
        params = self._add_headers(msg)
        username = None

        accept = self._get_accept(msg)

        return GenericRequest(RequestMethod.delete, path,
                              id=rx_record.message.token, username=username,
                              params=params, accept=accept,
                              connector=self.connector)

    def _get_addresses(self, family):
        try:
            return self.__cached_addresses[family]
        except KeyError:
            from netifaces import interfaces, ifaddresses

            addresses = self.__cached_addresses[family] = set()

            for interface in interfaces():
                try:
                    ifdata = ifaddresses(interface)[family]
                    ifaddrs = map(lambda x: x.split("%")[0], pluck("addr",
                                                                   ifdata))
                    addresses.update(ifaddrs)
                except KeyError:
                    pass

            return addresses

    def _getaddrinfo(self, host, family):
        self.logger.debug("Resolving %s", host)
        try:
            info = getaddrinfo(host, 0, family, SOCK_DGRAM)
            return set(map(itemgetter(0), map(itemgetter(-1), info)))
        except gaierror as e:
            self.logger.error("Failed to resolve %s: %s", host, e)
            return set()

    def _resolve_host(self, host):
        if is_ipv4(host):
            return {host}
        return self._getaddrinfo(host, AF_INET)

    def _resolve_host_ipv6(self, host):
        self.logger.debug("Resolving: %s", host)
        if is_ipv6(host):
            return {host}
        # TODO: kca: optimize
        return self._getaddrinfo(host, AF_INET) | \
               self._getaddrinfo(host, AF_INET6)

    def _get_real_path(self, msg):
        """Returns the URI needed for further processing. This is either a
        relative path if the request is to be processed internally or a
        full URI if the request is retargeted

        :param msg: CoAP message
        :return: Uri string
        """
        path = msg.uri
        parsed = urlparse(path)

        # prefer the HOST header
        try:
            uri_host = msg.findOption(options.UriHost).value
            uri_port = msg.findOption(options.UriPort).value
            if ':' in uri_host:
                netloc = '[' + uri_host + ']:' + str(uri_port)
            else:
                netloc = uri_host + ':' + str(uri_port)
        except AttributeError:
            netloc = parsed.netloc
        if not netloc:
            # no absolute URI and no host header -> not retargeted
            return path

        if netloc[0] == "[":
            target_host, _, target_port = netloc[1:].partition(']')
            if target_port:
                target_port = target_port[1:]
        else:
            target_host, _, target_port = netloc.partition(":")

        if not target_port:
            target_port = "5684"

        if target_port == self.server_port and self._resolve_host(
                target_host) & self.__addresses:
            # port and host match -> not retargeted
            return urlunparse(ParseResult("", "", *parsed[2:]))

        # request is retargeted
        #
        # construct full URI if needed
        if not parsed.netloc:
            path = netloc + path
            if not parsed.scheme:
                path = "coap://" + path
        elif not parsed.scheme:
            path = "coap://" + path

        return path

    def handle_block1(self, block1, rx_record, remote, msg):
        """Handles the presence of the Block1 Option.

        Block1 informs the server that the payload of a client request is
        fragmented.
        This function aggregates the various fragments, and queries the client
        for the next fragment.

        :param block1: Block1 option Object
        :param rx_record: CoAP message transfer information
        :param remote: tuple(Client IP, Client PORT)
        :param msg: CoAP message
        :return: Completed payload or None if the payload is not complete
        """
        try:
            self.block1_pending_payload[remote] += msg.payload
        except (KeyError, TypeError):
            if block1.block_number != 0:
                # We discard fragments with block number > 0 if we haven't
                # received the first one yet
                return None
            self.block1_pending_payload[remote] = msg.payload

        if block1.more:
            msg = connection.Message(connection.Message.ACK,
                                     code=constants.CONTINUE)
            # block1.block_number += 1
            msg.addOption(block1)
            self.server.sendto(msg._pack(rx_record.transaction_id,
                                         rx_record.message.token), remote)
            return None
        payload = self.block1_pending_payload[remote]
        self.block1_pending_payload[remote] = None
        return payload

    def handle_block2(self, block2, remote, mesg):
        """Handles the presence of the Block2 Option.

        Block2 informs the server that the payload of a server response has to
        be fragmented.
        This function returns a specific fragment of a message, as requested by
        a client.

        :param block2: Block2 option Object
        :param remote: tuple(Client IP, Client PORT)
        :param mesg: CoAP message
        :return: CoAP message containing a the requested fragment
        """
        msg = copy(mesg)
        length = 2 ** block2.size_exponent
        start = length * block2.block_number
        end = start + length
        if end <= len(msg.payload):
            more = True
        else:
            more = False
            end = len(msg.payload)
            # This means the last block has to be requested before a new request
            # with block is created
            self.block2_pending_payload[remote] = None
        msg.payload = msg.payload[start:end]
        new_block2 = options.Block2(block_number=block2.block_number,
                                    more=more,
                                    size_exponent=block2.size_exponent)
        msg.replaceOption(new_block2)

        return msg

    def _get_accept(self, msg):
        """Retrives the Accept option value from a CoAP message.

        :param msg: CoAP message
        :return: String representation of Accept option
        """
        opt = msg.findOption(options.Accept)
        if opt:
            accept = opt.value_as_string
        else:
            accept = msg.content_type or None

        return accept

    def _generate_error(self, e):
        """Generates a CoAP RST message from the exception e.

        :param e: Exception
        :return: CoAP Message
        """
        code = constants.INTERNAL_SERVER_ERROR
        data = str(e)
        return connection.Message(connection.Message.RST, code=code,
                                  payload=data)

    def process(self, rx_record, remote):
        """Processes a CoAP message using its transfer information.

        Triggers the different options handlers if needed.
        Performs a mapping between RESTful methods and ETSI RequestIndications.

        :param rx_record: CoAP message transfer information
        :param remote: tuple(Client IP, Client PORT)
        """
        self.logger.debug("process: %s (%s)", rx_record, remote)
        msg = rx_record.message
        block1 = rx_record.message.findOption(options.Block1)
        if block1:
            block_payload = self.handle_block1(block1, rx_record, remote, msg)
            if not msg or not block_payload:
                return
            msg.payload = block_payload
        block2 = rx_record.message.findOption(options.Block2)
        try:
            self.block2_pending_payload[remote]
        except KeyError:
            self.block2_pending_payload[remote] = None
        finally:
            block2_pending_payload = self.block2_pending_payload[remote]

        if block2 and block2_pending_payload:
            msg = self.handle_block2(block2, remote, block2_pending_payload)
            return self.server.sendto(msg._pack(rx_record.transaction_id,
                                                rx_record.message.token),
                                      remote)

        generic_mappers = {
            constants.PUT: self._generic_map_put,
            constants.POST: self._generic_map_post,
            constants.GET: self._generic_map_get,
            constants.DELETE: self._generic_map_delete
        }
        path = self._get_real_path(msg)

        mapping_function = generic_mappers[msg.code]

        generic_req = mapping_function(path, msg, rx_record)

        def handle_generic_result(result):
            """Handles a successful response from the Request handler.

            Generates CoAP Response from a response after converting it to a
            generic Response Object.
            Triggers Block2 fragmentation if needed.

            :param result: response Object
            """
            # result = res
            self.logger.debug("handle_generic_result(%s)", vars(result))
            if result.statusCode == 202:
                response_msg = connection.Message(
                    connection.Message.ACK,
                    code=http2coap_codes[result.statusCode],
                    payload="Request Accepted"
                )
            else:
                pt = rx_record.message.code
                if pt == constants.GET:
                    accept = self._get_accept(rx_record.message)
                    content_type, data = serialize_generic_result(result,
                                                                  accept=accept)
                    if data is None:
                        response_msg = connection.Message(
                            connection.Message.ACK,
                            code=http2coap_codes[result.statusCode]
                        )
                    else:
                        response_msg = connection.Message(
                            connection.Message.ACK,
                            code=http2coap_codes[result.statusCode],
                            content_type=content_type,
                            payload=data
                        )
                elif pt == constants.POST:
                    accept = self._get_accept(rx_record.message)
                    content_type, data = serialize_generic_result(result,
                                                                  accept=accept)
                    if data is None:
                        response_msg = connection.Message(
                            connection.Message.ACK,
                            code=http2coap_codes[result.statusCode]
                        )
                    else:
                        response_msg = connection.Message(
                            connection.Message.ACK,
                            code=http2coap_codes[result.statusCode],
                            # Set location option
                            #  FIXME: needs to be handled somewhere else
                            # location=(generic_req.path + '/' +
                            #           generic_req.params.get('nm', "")),
                            location=result.location,
                            content_type=content_type,
                            payload=data
                        )
                elif pt == constants.PUT:
                    response_msg = connection.Message(
                        connection.Message.ACK,
                        code=http2coap_codes[result.statusCode]
                    )
                elif pt == constants.DELETE:
                    response_msg = connection.Message(
                        connection.Message.ACK,
                        code=http2coap_codes[result.statusCode]
                    )
                else:
                    raise NotImplementedError("Coap result mapping for %s", pt)
            self.logger.debug("Sending CoAP reply: %s", response_msg)

            block2 = rx_record.message.findOption(options.Block2)
            if block2:
                self.block2_pending_payload[remote] = response_msg
                response_msg = self.handle_block2(block2, remote, response_msg)

            elif (response_msg.payload and
                  len(response_msg.payload) >
                  2 ** self.block_size_exponent):
                nr_blocks, r = divmod(len(response_msg.payload),
                                      2 ** self.block_size_exponent)
                if r > 0:
                    nr_blocks += 1

                self.logger.debug("Message is too long, sending first "
                                  "fragment (of %s)", nr_blocks)
                block2 = options.Block2(block_number=0, more=True,
                                        size_exponent=self.block_size_exponent)
                self.block2_pending_payload[remote] = response_msg
                response_msg = self.handle_block2(block2, remote, response_msg)

            if block1:
                response_msg.addOption(block1)
            self.server.sendto(response_msg._pack(rx_record.transaction_id,
                                                  rx_record.message.token),
                               remote)
            self.actual_requests.remove((rx_record.transaction_id,
                                         rx_record.message.token))

        def handle_error(x):
            """Handles a failed response from the RequestIndication handler.

            Generates CoAP Response from ETSI ResponseConfirmation Object.

            :param x: ETSI ResponseConfirmation Object
            """
            self.logger.debug("handle_error(%s)", vars(result))
            try:
                code = constants.http2coap_codes[x.statusCode]
            except AttributeError:
                code = constants.INTERNAL_SERVER_ERROR
            except KeyError:
                self.logger.warning("Failed to map result code to coap: "
                                    "%s (%s)", x.statusCode, x)
                code = constants.INTERNAL_SERVER_ERROR

            accept = self._get_accept(rx_record.message)
            content_type, data = encode_error(x, accept=accept)

            msg = connection.Message(connection.Message.RST, code=code,
                                     payload=data, content_type=content_type)

            self.logger.debug("Sending CoAP error reply: %s", msg)
            self.server.sendto(msg._pack(rx_record.transaction_id,
                                         rx_record.message.token), remote)
            self.actual_requests.remove((rx_record.transaction_id,
                                         rx_record.message.token))

        try:
            result_promise = self.request_handler(generic_req)
            result = result_promise.get()
            if isinstance(result, ErrorResponse):
                return handle_error(result)
        except ErrorResponse as result:
            return handle_error(result)
        except Exception as exc:
            self.logger.exception("Caught exception while handling request")
            return handle_error(exc)

        return handle_generic_result(result)

    @staticmethod
    def get_id_and_token(packed):
        # rst: copy of the begin of the Connection.decode function before
        # the potential UnrecognizedOptionError
        vtoc = ord(packed[0])
        if 1 != 0x03 & (vtoc >> 6):
            raise Exception()
        # transaction_type = 0x03 & (vtoc >> 4)
        token_len = (vtoc & 0x0F)
        (_, transaction_id) = struct.unpack('!BH', packed[1:4])
        token = packed[4:4 + token_len]
        return transaction_id, token

    def handle_request(self, message, remote):
        req = self.get_id_and_token(message)
        if req in self.actual_requests:
            return

        self.actual_requests.append(req)
        self.req_queue.put((message, remote))

    def _handle_request(self, message, remote):
        """Entry points of requests, converts a buffer into CoAP message
        transfer information

        :param message: Buffer containing a CoAP message
        :param remote: tuple(Client IP, Client Port)
        """

        if message and remote:
            self.remote = remote
            # TODO(rst): put this later into constants, when coap lib is updated
            # TODO:      newer versions
            CONSTANTS_EMPTY = 0
            CONSTANTS_NOT_IMPLEMENTED = 161  # 5.01
            try:
                rx_record = connection.ReceptionRecord(None, message, remote)
                if (rx_record.message.code == CONSTANTS_EMPTY and
                            rx_record.message.transaction_type ==
                            connection.Message.RST):
                    return
            except UnrecognizedOptionError:
                code = CONSTANTS_NOT_IMPLEMENTED
                msg = connection.Message(connection.Message.RST, code=code)
                self.server.sendto(msg._pack(*self.get_id_and_token(message)),
                                   remote)
                raise UnrecognizedOptionError
            else:
                return self.process(rx_record, remote)
                # start_new_thread(self.process, (rx_record, remote))
                # self.req_queue.put((rx_record, remote))

    def request_runner(self):
        while True:
            message, remote = self.req_queue.get()
            self._handle_request(message, remote)
            # start_new_thread(self._handle_request, (message, remote))

    def start(self):
        """Starts the Server"""
        self.logger.debug("Coap Server launched")
        self.server.start()

    def stop(self):
        """Stops the Server gracefully"""
        self.server.stop()

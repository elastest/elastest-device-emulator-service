import socket as S
from Queue import Queue
from socket import inet_pton
from thread import start_new_thread
from threading import BoundedSemaphore
from urlparse import urlparse

from aplus import Promise
from futile.logging import LoggerMixin

import coapy.coapy as coapy
import coapy.coapy.connection as connection
import coapy.coapy.constants as constants
import coapy.coapy.link as link
import coapy.coapy.options as options

smaker_sockets = {}
suc = {}  # socket usage counter

args2ep_map = {}


class CoapClient(LoggerMixin):
    """CoAP Client with simple API using the coapy library"""

    def __init__(self, uri, client_port=constants.COAP_PORT, keyfile=None,
                 certfile=None, cacertfile=None, block_size_exponent=10, *args,
                 **kw):
        """Initializes the client.

        :param uri: URI referencing the server this clients is trying to reach.
                    Can contain SCHEME://IP:PORT
        :param client_port: Port used by the client when sending requests
        """
        self.lock = BoundedSemaphore()
        self.logger.debug("Creating CoapClient for %s", uri)
        # address_family = S.AF_INET,
        # socket_type = S.SOCK_DGRAM,
        # socket_proto = S.IPPROTO_UDP,
        # ssl_enabled = False, keyfile = None, certfile = None,
        # cacertfile = None, port = constants.COAP_PORT
        # self.socket_args = {}

        # self.socket_args["keyfile"] = keyfile
        # self.socket_args["certfile"] = certfile
        # self.socket_args["cacertfile"] = cacertfile
        # self.socket_args["port"] = client_port

        try:
            info = urlparse(uri)
            port = info.port and int(info.port) or constants.COAP_PORT
            # TODO: this will probably fail later under some IPv6 circumstances
            # TODO  since it strips [] from the hostname
            host = info.hostname
            self.scheme = info.scheme or "coap"
            if self.scheme == "coaps":
                ssl_enabled = True
            else:
                ssl_enabled = False

        except:
            raise Exception("CoapClient: Wrong URI format")
        if port < 0 or port > 65535:
            raise Exception("CoapClient: Wrong port number")
        if self.scheme != "coap" and self.scheme != "coaps":
            raise Exception("CoapClient: Scheme isn't coap or coaps")
        # self.remote is:
        # a pair (*host*, *port*) for IPv4
        # a tuple (*host*, *port*, *flowinfo*, *scopeid*) for IPv6
        # TODO: kca: deal with IPv6 hostnames

        ep_args = (keyfile, certfile, cacertfile, client_port, ssl_enabled)

        if ep_args in args2ep_map:
            self.ep = args2ep_map[ep_args]
            self.logger.debug("Reusing endpoint")
            try:
                inet_pton(S.AF_INET6, host)
            except:
                self.remote = (host, port)
            else:
                # TODO: values for flowinfo and scopeid probably need to be set
                # TODO  up
                self.remote = (host, port, 0, 0)
        else:
            try:
                inet_pton(S.AF_INET6, host)
            except:
                self.remote = (host, port)
                self.ep = connection.EndPoint(ssl_enabled=ssl_enabled,
                                              keyfile=keyfile,
                                              certfile=certfile,
                                              cacertfile=cacertfile,
                                              port=client_port)
            else:
                # TODO: values for flowinfo and scopeid probably need to be set
                # TODO  up
                self.remote = (host, port, 0, 0)
                self.ep = connection.EndPoint(address_family=S.AF_INET6,
                                              ssl_enabled=ssl_enabled,
                                              keyfile=keyfile,
                                              certfile=certfile,
                                              cacertfile=cacertfile,
                                              port=client_port)
            args2ep_map[ep_args] = self.ep

        self._incomplete_responses = {}

        self.block_size_exponent = block_size_exponent

        self.req_queue = Queue()

        self.logger.debug("starting request runner")
        start_new_thread(self.request_runner, ())

    def handle_block1(self, block1, msg):
        """Handles the presence of the Block1 Option.

        Block1 informs the server that the payload of a client request is
        fragmented.
        This function tries to send all fragments one after another, expecting
        acknowledgments for each.

        :param block1: Block1 option Object
        :param msg: CoAP message
        :return: Final response from the server
        """
        return self._handle_block1(block1, msg.payload, msg)

    def _handle_block1(self, block1, payload, msg):

        length = 2 ** block1.size_exponent
        start = length * block1.block_number
        end = start + length
        if end < len(payload):
            more = True
        else:
            more = False
            end = len(payload)
        msg.payload = payload[start:end]
        new_block1 = options.Block1(block_number=block1.block_number, more=more,
                                    size_exponent=block1.size_exponent)
        msg.replaceOption(new_block1)

        def handle_response(resp):
            block1 = resp.findOption(options.Block1)
            if block1:
                block1.block_number += 1
                if more:
                    return self._handle_block1(block1, payload, msg)
                else:
                    return resp
            else:
                if more:
                    self.logger.warn("It seems not all parts of the initial "
                                     "request were sent to endpoint.")

                return resp

        return self._send(msg).then(handle_response)

    def handle_block2(self, block2, resp, init_req, p):
        """Handles the presence of the Block2 Option.

        Block2 informs the client that the payload of a server response has to
        be fragmented.
        This function aggregates the fragmented parts and requests the following
        part if needed.

        :param block2: Block2 option Object
        :param resp: First response from the server containing the Block2 Option
        :param msg: First CoAP message
        :return: Complete response from the server
        """

        def request_next_block():
            block2.block_number += 1
            init_req.replaceOption(block2)
            return self._send(init_req)

        def handle_next_block(new_resp):
            new_block2 = new_resp.findOption(options.Block2)
            assert new_block2
            assert new_block2.block_number == block2.block_number
            self._incomplete_responses[init_req] += new_resp.payload

            if new_block2.more:
                request_next_block().then(handle_next_block, error_printer)
            else:

                # response is complete
                resp.payload = self._incomplete_responses[init_req]
                del (self._incomplete_responses[init_req])
                resp.deleteOption(options.Block2)
                self.lock.release()
                self.req_queue.task_done()
                p.fulfill(resp)

        def error_printer(error):
            print error
            # raise Exception(error)#
            p.reject(error)

        self._incomplete_responses[init_req] = resp.payload
        request_next_block().then(handle_next_block, error_printer)

    def request(self, method, path, data=None, token=None, observe=None,
                **args):
        """Sends a CoAP request over a specified method.

        A set of keywords are recognized by this function in order to set the
        different options: 'content_type', 'max_age', 'etag', 'uri_host',
        'uri_port', 'location', 'if_match', 'if_none_match', 'block1', 'block2,
        'accept', 'observe'

        :param method: RESTful method, "GET", "PUT", "POST" or "DELETE"
        :param path: Path of the resource, can include query parameters (?a=b)
        :param data: Request payload buffer
        :param args: Optional keywords
        :return: Response from server
        """
        query = None
        # TODO: kca: use urlparse or at least str.partition
        if path.find("?") != -1:
            split_path = path.split("?", 1)
            path = split_path[0]
            query = split_path[1]
        try:
            args = args["args"]
        except KeyError:
            pass

        try:
            transaction_type = args["transaction_type"]
        except KeyError:
            transaction_type = connection.Message.CON

        self.logger.debug("Sending %s on uri %s://%s:%s/%s with %s", method,
                          self.scheme, self.remote[0], self.remote[1], path,
                          args)
        if method == "GET":
            if query:
                msg = connection.Message(code=constants.GET, uri_path=path,
                                         uri_query=query, token=token,
                                         payload=data,
                                         kw=args,
                                         transaction_type=transaction_type)
            else:
                msg = connection.Message(code=constants.GET, uri_path=path,
                                         payload=data, token=token, kw=args,
                                         transaction_type=transaction_type)
        elif method == "POST":
            if query:
                msg = connection.Message(code=constants.POST, payload=data,
                                         uri_path=path, uri_query=query,
                                         token=token,
                                         observe=observe, kw=args,
                                         transaction_type=transaction_type)
            else:
                msg = connection.Message(code=constants.POST, payload=data,
                                         uri_path=path, token=token,
                                         observe=observe,
                                         kw=args,
                                         transaction_type=transaction_type)
        elif method == "PUT":
            if query:
                msg = connection.Message(code=constants.PUT, payload=data,
                                         uri_path=path, uri_query=query,
                                         kw=args,
                                         transaction_type=transaction_type)
            else:
                msg = connection.Message(code=constants.PUT, payload=data,
                                         uri_path=path, kw=args,
                                         transaction_type=transaction_type)
        elif method == "DELETE":
            if query:
                msg = connection.Message(code=constants.DELETE, uri_path=path,
                                         uri_query=query, kw=args,
                                         transaction_type=transaction_type)
            else:
                msg = connection.Message(code=constants.DELETE, uri_path=path,
                                         kw=args,
                                         transaction_type=transaction_type)
        elif method == "NOTIFY":
            if query:
                msg = connection.Message(
                    code=constants.POST, uri_path=path, uri_query=query,
                    kw=args, transaction_type=connection.Message.NON)
            else:
                msg = connection.Message(
                    code=constants.POST, uri_path=path, kw=args,
                    transaction_type=connection.Message.NON)
        else:
            raise ValueError("Unhandled method: %s" % (method,))

        p = Promise()

        # put the message with the corresponding promise into the request queue,
        # let request_runner handle the rest.
        self.req_queue.put((msg, p))

        return p

    def request_runner(self):
        """
        Sends requests from its queue.
        Waits for block-wise transfer to complete before sending a new request.
        """
        while True:
            try:
                # keep locked as long as block-wise transfer is not complete
                # (see handle_block2)
                self.lock.acquire()
                msg, p = self.req_queue.get()

                # self.logger.debug("lock acquired")
                # self.logger.debug("running; msg=%s, p=%s", msg, p)

                block1 = msg.findOption(options.Block1)

                if msg.payload is not None:
                    if (not block1 and
                            len(msg.payload) > 2 ** self.block_size_exponent):
                        nr_blocks, r = divmod(len(msg.payload),
                                              2 ** self.block_size_exponent)
                        if r > 0:
                            nr_blocks += 1

                        self.logger.debug("Message is too long, sending first "
                                          "fragment (of %s)",
                                          nr_blocks)
                        block1 = options.Block1(
                            block_number=0, more=True,
                            size_exponent=self.block_size_exponent)

                def handle_block2(resp):
                    self.logger.debug("handle_block2(%s)", resp)
                    block2 = resp.findOption(options.Block2)
                    if block2:
                        self.handle_block2(block2, resp, msg, p)
                    else:
                        # self.logger.debug("releasing lock")
                        self.lock.release()
                        self.req_queue.task_done()
                        p.fulfill(resp)

                def handle_error(e):
                    self.logger.debug("Unable to send request: %s for %s %s",
                                      constants.codes[e.code],
                                      constants.codes[msg.code], msg.uri)
                    # release lock on exception
                    self.lock.release()
                    self.req_queue.task_done()
                    # raise error again for promise chain
                    p.fulfill(e)

                if block1:
                    self.handle_block1(block1, msg).then(handle_block2,
                                                         handle_error)
                else:
                    self._send(msg).then(handle_block2, handle_error)

            except Exception as e:
                self.logger.error(e)
                try:
                    self.lock.release()
                except ValueError:
                    self.logger.debug("Releasing lock after exception failed. "
                                      "Lock was already released.")
                    pass

    def get(self, path, data=None, token=None, **args):
        """Sends a CoAP GET request.

        A set of keywords are recognized by this function in order to set the
        different options: 'content_type', 'max_age', 'etag', 'uri_host',
        'uri_port', 'location', 'if_match', 'if_none_match', 'block1', 'block2,
        'accept', 'observe'

        :param path: Path of the resource, can include query parameters (?a=b)
        :param data: Request payload buffer
        :param args: Optional keywords
        :return: Response from server
        """
        return self.request("GET", path, data, token=token, args=args)

    def post(self, path, data, token=None, observe=1, **args):
        """Sends a CoAP POST request.

        A set of keywords are recognized by this function in order to set the
        different options: 'content_type', 'max_age', 'etag', 'uri_host',
        'uri_port', 'location', 'if_match', 'if_none_match', 'block1', 'block2,
        'accept', 'observe'

        :param path: Path of the resource, can include query parameters (?a=b)
        :param data: Request payload buffer
        :param args: Optional keywords
        :return: Response from server
        """
        return self.request("POST", path, data, token=token, observe=observe,
                            args=args)

    def put(self, path, data, **args):
        """Sends a CoAP PUT request.

        A set of keywords are recognized by this function in order to set the
        different options: 'content_type', 'max_age', 'etag', 'uri_host',
        'uri_port', 'location', 'if_match', 'if_none_match', 'block1', 'block2,
        'accept', 'observe'

        :param path: Path of the resource, can include query parameters (?a=b)
        :param data: Request payload buffer
        :param args: Optional keywords
        :return: Response from server
        """
        return self.request("PUT", path, data, args=args)

    def delete(self, path, **args):
        """Sends a CoAP DELETE request.

        A set of keywords are recognized by this function in order to set the
        different options: 'content_type', 'max_age', 'etag', 'uri_host',
        'uri_port', 'location', 'if_match', 'if_none_match', 'block1', 'block2,
        'accept', 'observe'

        :param path: Path of the resource, can include query parameters (?a=b)
        :param args: Optional keywords
        :return: Response from server
        """
        return self.request("DELETE", path, None, args=args)

    def _send(self, msg):
        return self.ep.send(msg, self.remote)

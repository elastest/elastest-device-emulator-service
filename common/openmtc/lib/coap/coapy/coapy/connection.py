# Copyright (c) 2010 People Power Co.
# All rights reserved.
#
# This open source code was developed with funding from People Power Company
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# - Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# - Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the
#   distribution.
# - Neither the name of the People Power Corporation nor the names of
#   its contributors may be used to endorse or promote products derived
#   from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE
# PEOPLE POWER CO. OR ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE
#
import socket
from thread import start_new_thread
from threading import Timer

import constants
import options
from aplus import Promise
from futile import LoggerMixin

reload(socket)
# Avoid gevent socket patch
# import imp
# fp, pathname, description = imp.find_module('socket')
# try:
#    socket = imp.load_module('socket_', fp, pathname, description)
# finally:
#    if fp:
#        fp.close()
import struct
import time
import collections
from options import encstr
from random import randint, random
from select import select, POLLIN, POLLOUT, POLLNVAL, POLLERR, POLLHUP
from operator import attrgetter
from coap.coapy.coapy.options import ContentType
import ssl
from dtls.sslconnection import SSLConnection
import logging


class Message(object):
    """Represent the components of a CoAP message.

    - :attr:`.transaction_type`
    - :attr:`.code`
    - :attr:`.options`
    - :attr:`.payload`

    The transaction ID is not recorded in the message instance.
    Rather, it is recorded in a :class:`TransmissionRecord` or
    :class:`ReceptionRecord`.
    """
    logger = logging.getLogger(__name__)

    version = property(lambda _s: 1, None, None, "The CoAP protocol version.")

    CON = 0
    """The message transaction type indicating a confirmable message
    (one that requires an acknowledgement)."""

    NON = 1
    """The message transaction type indicating a non-confirmable
    message (one that does not evoke an acknowledgement)."""

    ACK = 2
    """The message transaction type indicating acknowledgement of a
    :attr:`confirmable<.CON>` message.  Note that such a message may
    also include a response payload that pertains to the acknowledged
    message."""

    RST = 3
    """The message transaction type indicating that a received
    :attr:`confirmable<.CON>` message could not be processed due to
    insufficient context."""

    _TransactionTypeMap = {CON: 'CON',
                           NON: 'NON',
                           ACK: 'ACK',
                           RST: 'RST'}

    OptionKeywords = {'content_type': options.ContentType,
                      'max_age': options.MaxAge,
                      # 'uri_scheme' : options.UriScheme,
                      'etag': options.Etag,
                      'uri_host': options.UriHost,
                      'uri_port': options.UriPort,
                      'location': options.Location,
                      'uri_path': options.UriPath,
                      'uri_query': options.UriQuery,
                      'observe': options.Observe,
                      'accept': options.Accept,
                      'if_match': options.IfMatch,
                      'if_none_match': options.IfNoneMatch,
                      'block1': options.Block1,
                      'block2': options.Block2}
    """A map from Python identifiers to :mod:`option classes<options>`.

    These identifiers can be provided as keyword parameters to the
    :meth:`Message.__init__` method; the corresponding option class will be
    invoked with the parameter value to create an option that is
    associated with the message."""

    def __init__(self, transaction_type=CON, code=0, payload='', token=None, **kw):
        """Create a Message instance.

        As a convenience, message options can be created from keyword
        parameters if the keywords are present in
        :attr:`.OptionKeywords`.

        :param transaction_type: One of :attr:`.CON`, :attr:`.NON`,
           :attr:`.ACK`, :attr:`.RST`.  The message transaction type
           cannot be modified after creation.

        :param code: The integral code identifying the method of a
           request message, or the disposition in a response message.

        :param payload: An optional payload for the message.  If not
           provided, the message will have no payload unless
           subsequently assigned.
        """

        if not (transaction_type in (self.CON, self.NON, self.ACK, self.RST)):
            raise ValueError()
        self.__transactionType = transaction_type
        self.__code = code
        self.__options = []
        self.__payload = payload
        self.token = token
        try:
            extra = kw.pop("kw")
        except KeyError:
            pass
        else:
            kw.update(extra)
        for (k, v) in kw.iteritems():
            kw_type = self.OptionKeywords.get(k)
            if kw_type is not None:
                if kw_type == options.UriQuery:
                    vsplit = v.split('&')
                    for optv in vsplit:
                        self.addOption(kw_type(optv))
                elif kw_type == options.UriPath:
                    vsplit = v.split('/')
                    for optv in vsplit:
                        self.addOption(kw_type(optv))
                elif kw_type in (options.Block1, options.Block2):
                    self.addOption(kw_type(**v))
                elif kw_type == options.ContentType:
                    if v is not None:
                        mimetype, _, _encoding = v.partition(";")
                        # TODO: deal with encodings other than UTF-8
                        self.addOption(kw_type(mimetype.strip()))
                else:
                    if v is None:
                        self.logger.debug("option '%s' is ignored, because its value is None", k)
                        continue
                    self.addOption(kw_type(v))

    @property
    def content_type(self):
        o = self.findOption(ContentType)
        if not o:
            o = ContentType()
        return o.value_as_string

    content_format = content_type

    def _get_options(self):
        """A tuple containing the :mod:`options <options>`
        associated with the message.

        The options are sorted in increasing value of option type.
        """
        # return tuple(sorted(self.__options.itervalues(), lambda _a,_b: cmp(_a.Type, _b.Type)))
        return tuple(sorted(self.__options,
                            lambda _a, _b: cmp(_a.Type, _b.Type)))
        # return self.__options

    options = property(_get_options)

    def addOption(self, opt):
        """Add a new option instance.

        If the option can appear multiple times, this method is
        intended to add the new value to the existing ones.

        """
        # self.__options[type(opt)] = opt
        self.__options.append(opt)
        return self

    def replaceOption(self, opt):
        """Add a new option instance.

        If the option is already present in message, its previous
        value is replaced by the new one.
        """
        # self.__options[type(opt)] = opt
        opttype = self._classForOption(opt)
        i = 0
        found = False
        for op in self.__options:
            if self._classForOption(op) is opttype:
                found = True
                self.__options.pop(i)
                break
            i = i + 1
        if found:
            self.__options.insert(i, opt)
        else:
            self.addOption(opt)

        return self

    def _classForOption(self, opt):
        if isinstance(opt, options._Base):
            opt = type(opt)
        elif isinstance(opt, int):
            opt = options.Registry.get(opt)
        if not issubclass(opt, options._Base):
            raise ValueError()
        return opt

    def deleteOption(self, opt):
        """Remove the option from the message.

        :param opt: An option, specified as an option instance, an
          option class, or the type code of an option.
        """
        # self.__options.pop(self._classForOption(opt))
        opttype = self._classForOption(opt)
        k = 0
        # TODO: kca: use filter. Caching?
        for op in self.__options:
            if self._classForOption(op) is opttype:
                self.__options.pop(k)
            k += 1

    def findOption(self, opt):
        """Locate the given option within the message.

        Returns ``None`` if no matching option can be found.

        :param opt: An option, specified as an option instance, an
          option class, or the type code of an option.
        """
        # return self.__options.get(self._classForOption(opt))
        opttype = self._classForOption(opt)
        k = 0
        reslist = []
        for op in self.__options:
            if self._classForOption(op) is opttype:
                reslist.append(op)
                k += 1
        if k == 0:
            return None
        if not reslist[0].is_repeatable():
            return reslist[0]

        return reslist

    def _get_transaction_type(self):
        """Return the transaction type (one of :attr:`.CON`,
        :attr:`.NON`, :attr:`.ACK`, :attr:`.RST`).

        :note: The transaction type is assigned when the message is
               created, and cannot be changed thereafter."""
        return self.__transactionType

    transaction_type = property(_get_transaction_type)

    def _get_code(self):
        """The integral request method code or response code of the message."""
        return self.__code

    def _set_code(self, code):
        self.__code = code

    code = property(_get_code, _set_code)

    def _get_payload(self):
        """The payload of the message as a :class:`str`.

        If this is not an empty string, there should be a
        corresponding :class:`options.ContentType` option
        present that defines its format (if the default value of
        ``text/plain`` is not appropriate)."""
        return self.__payload

    def _set_payload(self, payload):
        if not isinstance(payload, str):
            raise ValueError()
        self.__payload = payload

    payload = property(_get_payload, _set_payload)

    def build_uri(self, explicit=False):
        uri_scheme = None
        uri_host = self.findOption(options.UriHost)
        uri_port = self.findOption(options.UriPort)
        uri_path = self.findOption(options.UriPath)

        resp = []
        val = None
        # if uri_scheme is not None:
        #    val = uri_scheme
        # elif explicit:
        #    val = options.UriScheme.Default
        if val is not None:
            resp.append(val)
            resp.append(':')
        val = None
        # if uri_authority is not None:
        #    val = uri_authority.value
        # elif explicit:
        #    val = options.UriAuthority.Default
        if uri_host is not None:
            val = uri_host.value
            if val is not None:
                if not val.startswith('coap://') and not val.startswith('coaps://'):
                    resp.append('coap://')
                resp.append(val)

                val = None
                if uri_port is not None:
                    val = str(uri_port.value)
                if val is not None:
                    resp.extend((":", val))
                    # resp.append('/')

        val = [options.UriPath.Default]
        if uri_path is not None:
            val.extend(map(attrgetter("value"), uri_path))
        resp.append('/'.join(val))
        return ''.join(resp)

    uri = property(build_uri)

    def __str__(self):
        resp = [self._TransactionTypeMap[self.__transactionType]]
        if 0 != self.__code:
            resp.append('+')
            resp.append(constants.codes.get(self.__code, '%u' %
                                            (self.__code,)))
        uri = self.build_uri()
        if uri:
            resp.append(uri)
        resp.append('| Options: {')
        resp.append(', '.join(map(str, self.__options)))
        resp.append('}')
        resp.append('| Payload: {')
        resp.append(str(self.__payload))
        resp.append('}')

        return ' '.join(resp)

    def _pack(self, transaction_id, token=None):
        """Return the message as an octet sequence.

        :param transaction_id: The transaction ID to be encoded into the sequence
        :rtype: :class:`str`
        """

        data = []
        if self.token and not token:
            token = self.token
        if token:
            tokenlen = len(token)
        else:
            tokenlen = 4
        if self.__options is None:
            num_options = 0
            option_encoding = ''
        else:
            #    (num_options, option_encoding) = options.encode(self.__options.itervalues())
            (num_options, option_encoding) = options.encode(self.__options)
        assert isinstance(option_encoding, str)
        # was (num_options & 0x0F), removed in coap13
        data.append(chr((self.version << 6) + ((self.__transactionType & 0x03) << 4) + (tokenlen & 0x0F)))
        data.append(struct.pack('!BH', self.__code, transaction_id))
        if token:
            data.append(token)
        else:
            data.append(''.join(chr(randint(0, 255)) for _ in range(tokenlen)))  # urandom(tokenlen))
        if 0 < num_options:
            data.append(option_encoding)

        if self.__payload:
            # Payload maker
            data.append(chr(255))
            data.append(encstr(self.__payload))

        return b''.join(data)

    @classmethod
    def decode(cls, packed):
        """Create a Message instance from a payload.

        This method decodes the payload, and returns a pair (*xid*,
        *message*) where *xid* is the transaction ID extracted from
        the encoded message, and *message* is an instance of
        :class:`Message` initialized to the decoded components of the
        data.

        :param payload: A sequence of octets comprising a complete CoAP packet
        :rtype: (:class:`int`, :class:`Message`)
        """

        vtoc = ord(packed[0])
        if 1 != 0x03 & (vtoc >> 6):
            raise Exception()
        transaction_type = 0x03 & (vtoc >> 4)
        token_len = (vtoc & 0x0F)
        (code, transaction_id) = struct.unpack('!BH', packed[1:4])
        token = packed[4:4 + token_len]
        (option, packed) = options.decode(packed[(4 + token_len):])
        instance = cls(transaction_type=transaction_type, code=code,
                       payload=packed, token=token)
        for opt in option:
            instance.__options.append(opt)
        return (transaction_id, instance)


def is_multicast(address):
    """Return ``True`` iff address is a multicast address.

    This function is used to eliminate retransmissions for confirmable
    messages sent to multicast addresses.

    :param address: A socket address as supported by the Python socket
        functions: i.e. a pair (*host*, *port*) for IPv4 addresses and
        a tuple (*host*, *port*, *flowinfo*, *scopeid*) for IPv6.  The
        host may be either a host name or an IP address in the
        textual notation appropriate to the address family.
    """

    if isinstance(address, str):
        return False
    if not isinstance(address, tuple):
        raise ValueError()
    if 2 == len(address):
        family = socket.AF_INET
        (host, port) = address
    elif 4 == len(address):
        family = socket.AF_INET6
        (host, port, flowinfo, scopeid) = address
    else:
        raise ValueError()
    for (_, _, _, _, sockaddr) in socket.getaddrinfo(host, port, family):
        inaddr = socket.inet_pton(family, sockaddr[0])
        if socket.AF_INET == family:
            return 0xE0 == (0xF0 & ord(inaddr[0]))
        elif socket.AF_INET6 == family:
            return 0xFF == ord(inaddr[0])
    return False


class TransmissionRecord(object):
    """Material related to a transmitted CoAP message.

    - :attr:`.message`
    - :attr:`.remote`
    - :attr:`.transaction_id`
    - :attr:`.end_point`
    - :attr:`.packed`

    """

    __responseTimeout = None

    def __init__(self, end_point, message, remote):
        """
        :param end_point: The :class:`EndPoint` responsible for
          transmitting the message.

        :param message: An instance of :class:`Message` from which the
          transmission content will be calculated

        :param remote: A Python :mod:`socket` address identifying the
          destination of the transmission.
        """

        self.__endPoint = end_point
        self.__message = message
        self.__transactionId = transaction_id_giver._nextTransactionId()
        self.__remote = remote

        self.__packed = message._pack(self.__transactionId)

        self.__transmissionsLeft = 1
        if (Message.CON == message.transaction_type) and (not is_multicast(remote)):
            self.__transmissionsLeft = constants.MAX_RETRANSMIT
        self.__responseTimeout = constants.RESPONSE_TIMEOUT * (random() % 0.5 + 1)
        self.__nextEventTime = time.time()
        self.__allResponses = set()
        if Message.CON == message.transaction_type:
            self.__responseType = None
        else:
            self.__responseType = message.transaction_type

        self.create_time = time.time()

    __endPoint = None

    def _get_end_point(self):
        """The :class:`EndPoint` that transmitted the message."""
        return self.__endPoint

    end_point = property(_get_end_point)

    __message = None

    def _get_message(self):
        """A reference to the :class:`Message` from which the transmission derived.

        :note: The content of the message may have been changed by
           application code subsequent to its transmission."""
        return self.__message

    message = property(_get_message)

    __transactionId = None

    def _get_transaction_id(self):
        """The transmission ID encoded in the packed message."""
        return self.__transactionId

    transaction_id = property(_get_transaction_id)

    __remote = None

    def _get_remote(self):
        """The Python :mod:`socket` address to which the transmission was sent."""
        return self.__remote

    remote = property(_get_remote)

    __packed = None

    def _get_packed(self):
        """The octet sequence representing the message."""
        return self.__packed

    packed = property(_get_packed)

    __responseType = None

    def _get_response_type(self):
        """
        - :attr:`Message.NON` if the message does not require a response

        - :attr:`Message.ACK` if the message has been acknowledged.
          If the acknowledgement carried a response message, it is
          available in :attr:`.response`.

        - :attr:`Message.RST` if the message received could not
          process the message.

        - ``None`` if the message is confirmable and neither an
          :attr:`Message.ACK` nor :attr:`Message.RST` has been
          received.
        """
        return self.__responseType

    response_type = property(_get_response_type)

    __transmissionsLeft = None

    def _get_transmissions_left(self):
        """Return the number of (re-)transmissions yet to occur.

        A positive value requires that :attr:`next_event_time` not be
        ``None``."""
        return self.__transmissionsLeft

    transmissions_left = property(_get_transmissions_left)

    __transmissionTime = None

    def _get_transmission_time(self):
        """The :meth:`time.time` at which the message was first transmitted."""
        return self.__transmissionTime

    def _set_transmission_time(self, transmission_time):
        """Set the :attr:`.transmission_time`.

        :note: Only for use by an :class:`EndPoint`."""
        if self.__transmissionTime is None:
            self.__transmissionTime = transmission_time
        self._set_last_event_time(transmission_time)

    transmission_time = property(_get_transmission_time)

    __lastEventTime = None

    def _get_last_event_time(self):
        """The :meth:`time.time` at which the last event related to the transmission occured.

        Transmission events are:

        - transmission or retranmission of the message
        - receipt of a response to the message
        """
        return self.__lastEventTime

    def _set_last_event_time(self, let=None):
        if let is None:
            let = time.time()
        self.__lastEventTime = let
        return let

    last_event_time = property(_get_last_event_time)

    __nextEventTime = None

    def _get_next_event_time(self):
        """Get the :meth:`time.time` value at which the next event
        associated with this transmission is due.

        Predictable transmission events are:

        - the time at which the message should be retransmitted
        - the time by which a response to the message should be received

        Returns ``None`` if there are no events associated with the
        transmission.
        """
        return self.__nextEventTime

    def _clear_next_event_time(self):
        self.__nextEventTime = None

    next_event_time = property(_get_next_event_time)

    def _decrementTransmissions(self):
        """Record fact-of a (re-)transmission, updating the various counters.

        :note: To be invoked only by an :class:`EndPoint`.
        """
        let = self._set_last_event_time()
        if self.__transmissionTime is None:
            self.__transmissionTime = let
        self.__nextEventTime = let + self.__responseTimeout
        self.__transmissionsLeft -= 1
        self.__responseTimeout *= 2

    __responseRecord = None

    def _get_response(self):
        """The :class:`ReceptionRecord` for the first message that was
        interpreted as a response to this message."""
        return self.__responseRecord

    response = property(_get_response)

    __allResponses = None

    def _get_responses(self):
        """A set containing all :class:`ReceptionRecords` that pertain
        to this transmission."""
        return self.__allResponses

    responses = property(_get_responses)

    def _processResponse(self, rx_record):
        """Process a response to this transmission.

        Cancel any subsequent transmissions.  Add the response to
        :attr:`responses`.  If this is the first reponse, set
        :attr:`response` and record :attr:`response_type`.

        This counts as an event for the purposes of
        :attr:`last_event_time`.
        """
        self.__lastEventTime = time.time()
        self.__nextEventTime = None
        self.__transmissionsLeft = 0
        if self.__responseRecord is None:
            self.__responseRecord = rx_record
        if self.__responseType is None:
            self.__responseType = rx_record.message.transaction_type
        self.__allResponses.add(rx_record)

    def _is_unacknowledged(self):
        """Return ``True`` iff this was a confirmable transaction for
        which the last transmission response wait has elapsed without
        receipt of a response."""
        return (self.__nextEventTime is None) and (self.__responseType is None)

    is_unacknowledged = property(_is_unacknowledged)


class ReceptionRecord(object):
    """Material related to a received CoAP message.

    - :attr:`.message`
    - :attr:`.remote`
    - :attr:`.transaction_id`
    - :attr:`.pertains_to`
    - :attr:`.end_point`
    """

    def __init__(self, end_point, packed, remote):
        self.__endPoint = end_point

        (self.__transactionId, self.__message) = Message.decode(packed)
        self.__remote = remote
        if Message.CON == self.__message.transaction_type:
            self.__responseType = None
        else:
            self.__responseType = Message.NON

    __endPoint = None

    def _get_end_point(self):
        """The :class:`EndPoint` that received the message."""
        return self.__endPoint

    end_point = property(_get_end_point)

    __message = None

    def _get_message(self):
        """The :class:`Message` received."""
        return self.__message

    message = property(_get_message)

    __remote = None

    def _get_remote(self):
        """The :mod:`socket` address from which the message was received."""
        return self.__remote

    remote = property(_get_remote)

    __transactionId = None

    def _get_transaction_id(self):
        """The transaction ID of the received message."""
        return self.__transactionId

    transaction_id = property(_get_transaction_id)

    __pertainsTo = None

    def _get_pertains_to(self):
        """The :class:`TransmissionRecord` to which the received
        message was interpreted as a response.

        The value will be ``None`` if the :attr:`.message`
        :meth:`transaction type <Message.transaction_type>` is neither
        :attr:`Message.ACK` nor :attr:`Message.RST`, or if the
        receiving :class:`EndPoint` could not identify the relevant
        message (e.g., it had already been expired from the
        transmission cache).
        """
        return self.__pertainsTo

    def _set_pertains_to(self, pertains_to):
        """Set the :attr:`pertains_to` field and cross-reference to this record.

        :param pertains_to: A :class:`TransmissionRecord` for which
          this message appears to be a response.
        """
        self.__pertainsTo = pertains_to
        pertains_to._processResponse(self)

    pertains_to = property(_get_pertains_to)

    has_responded = property(lambda _s: _s.__responseType is not None)

    def _respond(self, response_msg):
        if self.has_responded:
            raise Exception()
        self.__responseType = response_msg.transaction_type
        self.__endPoint.socket.sendto(response_msg._pack(self.transaction_id),
                                      self.__remote)

    def ack(self, response_msg=None):
        if response_msg is None:
            response_msg = Message(Message.ACK)
        self._respond(response_msg)

    def reset(self):
        self._respond(Message(Message.RST))


class _SelectSelect(object):
    """ select.poll emulation by using select.select."""

    def __init__(self):
        super(_SelectSelect, self).__init__()
        self.rlist = set()
        self.wlist = set()
        self.xlist = set()

    def register(self, fd, events):
        try:
            fd = fd.fileno()
        except AttributeError:
            pass
        assert isinstance(fd, int)
        if events & POLLIN:
            self.rlist.add(fd)
            events &= ~POLLIN
        if events & POLLOUT:
            self.wlist.add(fd)
            events &= ~POLLOUT
        if events:
            self.xlist.add(fd)

    def poll(self, timeout):

        rlist, wlist, xlist = select(self.rlist, self.wlist, self.xlist,
                                     timeout)

        events_dict = collections.defaultdict(int)
        for fd in rlist:
            events_dict[fd] |= POLLIN
        for fd in wlist:
            events_dict[fd] |= POLLOUT
        for fd in xlist:
            events_dict[fd] |= (POLLERR | POLLHUP | POLLNVAL)
        return events_dict.items()


class EndPoint(object):
    MAX_TX_HISTORY_SEC = 10

    def __init__(self,
                 address_family=socket.AF_INET,
                 socket_type=socket.SOCK_DGRAM,
                 socket_proto=socket.IPPROTO_UDP,
                 ssl_enabled=False, keyfile=None, certfile=None, cacertfile=None, port=constants.COAP_PORT):
        self.__socket = socket.socket(address_family, socket_type,
                                      socket_proto)

        self.ssl = ssl_enabled
        self._sslobj = None
        if self.ssl:
            ssl_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            if not keyfile or not certfile:
                raise Exception("Missing keyfile or certfile")

            # https://github.com/rbit/pydtls/blob/master/dtls/sslconnection.py
            if not cacertfile:
                cacertfile = certfile

            self._sslobj = SSLConnection(
                ssl_sock,
                keyfile=keyfile,
                certfile=certfile,
                server_side=False,
                cert_reqs=ssl.CERT_REQUIRED,
                ssl_version=2,
                ca_certs=cacertfile,
                # ca_certs = "/opt/OpenMTC/openmtc-python/openmtc-gevent/certs/CA_and_certs/pydtls/ca/ca-cert.pem",
                do_handshake_on_connect=True,
                suppress_ragged_eofs=True,
                ciphers=None
            )
            self.processor = MiniProc(sslobj=self._sslobj)
        else:
            # self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.__socket.bind(('', port))
            # processor.add_socket(self.__socket, self._sslobj)
            self.processor = MiniProc(socket=self.__socket)

    def _get_socket(self):
        """Return a reference to the primary socket associated with the end-point.

        If this end-point is expected to receive REST requests, the
        socket should be bound to a known port so that clients can
        identify the server."""
        return self.__socket

    socket = property(_get_socket)

    def send(self, message, remote):
        """Transmit a message to the remote.

        The message should have a code of either :attr:`Message.CON`
        or :attr:`Message.NON`; acknowledgements and resets should be
        generated through the :class:`ReceptionRecord` methods.

        The :class:`TransmissionRecord` associated with the
        transmission is returned.
        """
        return self.processor.send(message, remote)


class TransactionIDGiver(object):
    """
    Small class that returns unique transaction IDs for transmission records
    """
    def __init__(self):
        self.__transactionId = randint(0, 65535)

    def _nextTransactionId(self):
        """Reserve and return a new transaction identifier."""
        transaction_id = self.__transactionId
        self.__transactionId = 0xFFFF & (1 + self.__transactionId)
        return transaction_id


transaction_id_giver = TransactionIDGiver()


class MiniProc(LoggerMixin):
    DEF_TIMEOUT = 5

    def __init__(self, socket=None, sslobj=None, timeout=DEF_TIMEOUT):
        """
        Creates a Mini Processor, that sends and receives on the given (ssl) socket.
        If ssl is used, socket can be None.

        :param socket: Socket you want to listen on / send from
        :type socket: socket
        :param sslobj: SSL connection
        :type sslobj: SSLConnection
        :param timeout: how long to wait for an answer (is also used for socket polling)
        :type timeout: int
        """

        if socket is None and sslobj is None:
            raise Exception("Socket and sslobj can't both be None")

        self.sslobj = sslobj

        if sslobj and socket is None:
            socket = sslobj.get_socket(True)

        self.socket = socket
        self.timeout = timeout

        self.unanswered = {}

        # start receiver thread
        self.do_receive = True
        start_new_thread(self._receive_runner, ())

        self.timings = {}
        self.timers = {}

    def _receive_runner(self):  # constantly polling socket
        inpoller = _SelectSelect()

        evt = POLLIN
        inpoller.register(self.socket.fileno(), evt)
        inpoll_t = time.time()

        while self.do_receive:
            for (sfd, evt) in inpoller.poll(self.timeout):
                self.logger.debug("inpoller for %s returned sfd:%s, evt:%s after %sms", id, sfd, evt,
                                  (time.time() - inpoll_t) * 1000)
                if evt & POLLIN:
                    try:
                        if self.sslobj:
                            (msg, remote) = (self.sslobj.read(8192), self.socket.getpeername())

                        else:
                            (msg, remote) = self.socket.recvfrom(8192)

                        rx_record = ReceptionRecord(self, msg, remote)
                        self.logger.debug("%s New message: (%s) %s", id, rx_record.transaction_id,
                                          rx_record.message)

                        if rx_record.message.transaction_type in (Message.ACK, Message.RST):
                            if rx_record.transaction_id in self.unanswered:
                                response = rx_record.message

                                # get promise of initial request
                                promise = self.unanswered[rx_record.transaction_id]

                                # cancel timer for request
                                timer = self.timers[promise]
                                timer.cancel()

                                # check how long it took
                                req_sent_time = self.timings[promise]
                                dtime = time.time() - req_sent_time

                                self.logger.info("%s request ACK'D after %ss", rx_record.transaction_id, dtime)

                                # fulfill promise in its own thread, delete everything corresponding to transaction
                                start_new_thread(promise.fulfill, (response,))
                                del (self.unanswered[rx_record.transaction_id])
                                del (self.timings[promise])
                                del (self.timers[promise])

                            else:
                                self.logger.error("Received message with wrong/unknown transaction ID: (%s) %s",
                                                  rx_record.transaction_id, rx_record.message)

                        else:
                            self.logger.warn("Can't handle transaction type %s", rx_record.message.transaction_type)
                    except Exception as e:
                        self.logger.warn("Unable to receive from socket (%s): %s", socket, e)

    def _send(self, tx_record):
        """
        Send TransmissionRecord (blocking and no return value)

        :param tx_record: TransmissionRecord that includes the message
        :type tx_record: TransmissionRecord
        """
        id = tx_record.transaction_id
        self.logger.debug("Sending transmission %s to %s on %s: %s", id, tx_record.remote, self.socket.getsockname(),
                          tx_record.message)
        self.logger.debug("%s socket fd is: %s", id, self.socket.fileno())

        outpoller = _SelectSelect()

        outpoller.register(self.socket.fileno(), POLLOUT)

        for (sfd, evt) in outpoller.poll(self.timeout):
            self.logger.debug("outpoller for %s returned sfd:%s, evt:%s", id, sfd, evt)

            if evt & POLLOUT:
                if self.sslobj:
                    self.sslobj.connect(tx_record.remote)

                    self.sslobj.write(tx_record.packed)
                    self.logger.info("%s request SENT (ssl)", id)

                else:
                    self.socket.sendto(tx_record.packed,
                                       tx_record.remote)
                    self.logger.info("%s request SENT", id)
            else:
                self.logger.warn("outpoller returned event different from POLLOUT! This should never happen...")

    def send(self, message, remote):
        """
        Send a message to a remote address.

        :param message: message to be sent
        :type message: Message
        :param remote: remote address (host, port)
        :type remote: tuple
        :return: promise for request
        :rtype: Promise
        """
        p = Promise()

        tx_record = TransmissionRecord(self, message, remote)
        self.unanswered[tx_record.transaction_id] = p
        self.timings[p] = time.time()

        def timeoutfunc():
            errormsg = Message(Message.CON, constants.GATEWAY_TIMEOUT, payload="No response")
            del (self.unanswered[tx_record.transaction_id])
            del (self.timings[p])
            del (self.timers[p])
            p.reject(errormsg)

        # automatically reject promise after given time
        timer = Timer(self.timeout, timeoutfunc)
        timer.start()
        self.timers[p] = timer

        start_new_thread(self._send, (tx_record,))

        return p

import json

from socketio.namespace import BaseNamespace

from aplus import Promise
from futile.logging import LoggerMixin
from openmtc_etsi.response import ErrorResponseConfirmation
from openmtc_etsi.serializer import JsonSerializer
from openmtc_scl.plugins.transport_gevent_socketio import namespace_data, util
from openmtc_scl.plugins.transport_gevent_socketio.lzstring import LZString

__author__ = 'ren-local'


class GlobalNamespace(BaseNamespace, LoggerMixin):
    """This is the main Namespace listening on the default path ('/')"""
    x = LZString()
    scheme = "sio"
    schemes = (scheme, )
    # disconnected = False
    compress = False
    serializer = JsonSerializer()

    def disconnect(self, silent=False):
        super(GlobalNamespace, self).disconnect(silent)
        # (ren) added this so I can send/emit from outside of this namespace
        namespace_data.global_namespaces.pop(self.socket.sessid, None)
        self.logger.debug("socket disconnected: %s", self.socket.sessid)
        # self.disconnected = True

    def initialize(self):
        super(GlobalNamespace, self).initialize()
        # self.disconnected = False
        # (ren) added this so I can send/emit from outside of this namespace
        self.logger.debug("Initialized GlobalNamespace, sessid: %s", self.socket.sessid)
        namespace_data.global_namespaces[self.socket.sessid] = self
        self.scheme = "sio%s" % (self.socket.sessid, )
        self.schemes = (self.scheme, )

        # compress has been set by SocketIOTransportPlugin during _start()
        self.compress = self.config.get("compress", False)

        # register_transport_client has been set by SocketIOTransportPlugin during _start()
        self.register_client(self.schemes, self.send_request_indication)

    def send_request_indication(self, request_indication):
        self.logger.debug("send_request_indication: %s", request_indication)
        p = Promise()

        def callback_handler(result):
            # if data is not a dict, it's probably compressed
            try:
                if isinstance(result, str):
                    result = json.loads(self.x.decompresFromBase64(result))
            except:
                pass

            self.logger.debug("got client response \'%s\' to request \'%s\'", result, request_indication)
            try:
                response = util.unmarshal_response(result)
                p.fulfill(response)
            except Exception as e:
                self.logger.warn("can't unmarshall response \'%s\', error: \'%s\'", result, e)
                p.fulfill(result)

        try:
            msg = util.marshal_request_indication(request_indication)
            msgjson = json.dumps(msg)
        except Exception as e:
            self.logger.warn("unable to marshal request indication '%s': %s", request_indication, e)
            msgjson = request_indication.payload
            msg = msgjson

        # msg = str(msg)

        if self.compress:
            self.logger.debug("encoding to base64\r\n: %s", msgjson)
            compressed = self.x.compressToBase64(msgjson)
            # only use compressed if size is actually smaller than uncompressed
            msglen = len(msgjson)
            compressedlen = len(compressed)
            if msglen > compressedlen:
                msg = compressed
            else:
                self.logger.debug("compressing request produced overhead. sending uncompressed (%s > %s)", msglen,
                                  compressedlen)

        self.emit("request", msg, callback=callback_handler)

        return p

    def on_request(self, data):
        """Handles 'request' events. Request needs method field!

        :param data: incoming request
        :return: (optional) returns a response
        """

        # if data is not a dict, it's probably compressed
        try:
            try:
                if isinstance(data, str):
                    data = json.loads(self.x.decompresFromBase64(data))
            except:
                pass

            self.logger.debug("(%s) Got request: %s", self.socket.sessid, data)

            request_indication = util.unmarshal_request_indication(data)

            # if subscription, and contact or aggregateURI are session id, prepend uri with "sio:///"
            if getattr(request_indication, "typename", None) == "subscription":
                if request_indication.resource.get("aggregateURI", None) == (self.socket.sessid or ""):
                    self.logger.debug("aggregateURI to self: updating aggregateURI")

                    orig = request_indication.resource["aggregateURI"]
                    updated = "%s:///" % (self.scheme, )
                    request_indication.resource["aggregateURI"] = updated

                    self.logger.debug("aggregateURI field updated: %s -> %s", orig, updated)

                if request_indication.resource.get("contact", None) == (self.socket.sessid or ""):
                    self.logger.debug("SessionID as contact detected: updating contact")

                    orig = request_indication.resource["contact"]
                    updated = "%s:///" % (self.scheme, )
                    request_indication.resource["contact"] = updated

                    self.logger.debug("contact field updated: %s -> %s", orig, updated)

                    # handle_request_indication has been set by SocketIOTransportPlugin during _start()
            try:
                p = self.handle_request_indication(request_indication)
            except Exception as e:
                return e

            try:
                success_result = p.get()
                response = util.marshal_response(success_result)
                responsejson = json.dumps(response)
                self.logger.debug("(%s) Got internal response to handle_request_indication: %s", self.socket.sessid,
                                  responsejson)

                if self.compress:
                    compressed = self.x.compressToBase64(responsejson)
                    self.logger.debug("compressed response: %s", compressed)
                    responselen = len(responsejson)
                    compressedlen = len(compressed)
                    if responselen > compressedlen:
                        response = compressed
                    else:
                        self.logger.debug("compressing request produced overhead. sending uncompressed (%s > %s)",
                                          responselen, compressedlen)

                return response
            except ErrorResponseConfirmation as error_response:
                # deal with error
                response = util.marshal_error_response(error_response, request_indication.method)
                responsejson = json.dumps(response)

                self.logger.debug("(%s) Got internal ERROR response to handle_request_indication: %s",
                                  self.socket.sessid,
                                  responsejson)
                if self.compress:
                    compressed = self.x.compressToBase64(responsejson)
                    self.logger.debug("compressed response: %s", compressed)
                    responselen = len(responsejson)
                    compressedlen = len(compressed)
                    if responselen > compressedlen:
                        response = compressed
                    else:
                        self.logger.debug("compressing request produced overhead. sending uncompressed (%s > %s)",
                                          responselen, compressedlen)
                return response
        except Exception as e:
            self.logger.error(e)
            return e

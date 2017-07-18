from urlparse import urlparse
from aplus import Promise

from socketio.server import SocketIOServer
from openmtc_scl.plugins.transport_gevent_socketio import util
from openmtc_scl.plugins.transport_gevent_socketio.application import Application
from socketio.namespace import BaseNamespace
from openmtc_scl.plugins.transport_gevent_socketio import namespace_data
from openmtc_server.Plugin import Plugin

__author__ = 'ren-local'


class SocketIOTransportPlugin(Plugin):
    """This plugin provides a Socket.IO server.
    The server is capable of handling incoming requests,
    and reacting to requests with a target uri using the protocol 'sio:///'."""

    default_host = "0.0.0.0"
    default_port = 8080
    transport_protocol = "sio"

    def _init(self):
        # self.api.register_transport_client(("sio", ), self.send_request_indication)
        #
        # self.api.register_client(("sio", ), self.send_request)

        self._initialized()

    def send_request_indication(self, request_indication):
        self.logger.debug("send_request_indication: %s", request_indication)
        p = Promise()

        path = urlparse(request_indication.path).path[1:]

        self.logger.debug("target sessid (path): %s", path)

        target = namespace_data.global_namespaces.get(path, None)

        def callback_handler(result):
            self.logger.debug("got client response \'%s\' to request \'%s\'", result, request_indication)
            try:
                response = util.unmarshal_response(result)
                p.fulfill(response)
            except Exception as e:
                self.logger.warn("can't unmarshall response \'%s\', error: \'%s\'", result, e)
                p.fulfill(result)

        target.emit("request", util.marshal_request_indication(request_indication), callback=callback_handler)

        return p

    def send_request(self, request):
        self.logger.debug("send_request: %s", request)
        # TODO (ren) implement send_request

    def _start(self):
        # add function to BaseNamespace it's callable from its context
        BaseNamespace.handle_request_indication = self.api.handle_request_indication
        BaseNamespace.register_client = self.api.register_client
        BaseNamespace.config = self.config
        kwargs = {}

        # fill kwargs with config values
        host = self.config.get("host", "0.0.0.0")
        port = int(self.config.get("port", 8080))
        kwargs["resource"] = self.config.get("resource", None)
        kwargs["transports"] = self.config.get("transports", None)
        kwargs["policyserver"] = self.config.get("policy_server", None)
        policy_listener = self.config.get("policy_listener", None)
        # policy_listener needs to be tuple
        if policy_listener:
            split_host = policy_listener.rsplit(":", 1)
            kwargs["policy_listener"] = (split_host[0], split_host[1])

        kwargs["heartbeat_interval"] = self.config.get("heartbeat_interval", None)
        kwargs["heartbeat_timeout"] = self.config.get("heartbeat_timeout", None)
        kwargs["close_timeout"] = self.config.get("close_timeout", None)
        kwargs["log_file"] = self.config.get("log_file", None)

        # remove all mappings with empty value
        kwargs = {k: v for k, v in kwargs.items() if v}

        self.logger.info("Starting SocketIO server on %s:%s with kwargs: %s", host, port, kwargs)

        self.server = SocketIOServer((host, port), Application(), **kwargs)
        self.logger.debug("starting to serve socketio")
        self.api.run_task(self._serve)
        self._started()

    def _serve(self):
        """Start server serving"""
        self.server.serve_forever()
        self.logger.debug("socketio done serving")

    def _stop(self):
        self.logger.debug("stopping socketio server")
        self.server.stop()
        self._stopped()
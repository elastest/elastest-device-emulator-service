from gevent.wsgi import WSGIServer
from socket import getservbyname

from openmtc_cse import OneM2MEndPoint
from openmtc_server.Plugin import Plugin
from openmtc_server.configuration import Configuration, SimpleOption
from openmtc_server.platform.gevent.ServerRack import GEventServerRack
from openmtc_onem2m.client.http import get_client
from .wsgi import OpenMTCWSGIApplication


class HTTPTransportPluginConfiguration(Configuration):
    __name__ = "HTTPTransportPluginConfiguration configuration"
    __options__ = {
        "port": SimpleOption(int, default=None)
    }


class HTTPTransportPlugin(Plugin):
    __configuration__ = HTTPTransportPluginConfiguration

    def _init(self):
        self._initialized()

    def _start_server_rack(self):
        servers = []

        interface = self.config.get("interface", "")

        key_file = self.config.get("key")
        cert_file = self.config.get("crt")

        is_https = key_file and cert_file

        scheme = "https" if is_https else "http"

        port = self.config.get("port", getservbyname(scheme))

        default_content_type = self.config.get("global", {}).get(
            "default_content_type", False)

        pretty = self.config.get("global", {}).get("pretty", False)

        application = OpenMTCWSGIApplication(
            self.api.handle_onem2m_request, server_address=interface,
            default_content_type=default_content_type, pretty=pretty)

        if is_https:
            servers.append(WSGIServer(
                (interface, port), application,
                environ={'SERVER_NAME': 'openmtc.local'},
                keyfile=key_file, certfile=cert_file))
        else:
            servers.append(WSGIServer(
                (interface, port), application,
                environ={'SERVER_NAME': 'openmtc.local'}))

        rack = self.__rack = GEventServerRack(servers)

        rack.start()

        return scheme, interface, port

    def _start(self):
        self.api.register_onem2m_client(("http", "https"), get_client)

        scheme, interface, port = self._start_server_rack()

        self.api.register_point_of_access(
            OneM2MEndPoint(scheme=scheme, server_address=interface, port=port))

        self._started()

    def _stop(self):
        self.__rack.stop()
        self._stopped()

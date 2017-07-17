from netifaces import ifaddresses, interfaces
from socket import AF_INET, AF_INET6
from socket import getnameinfo
from urlparse import urlparse, uses_relative, uses_netloc

from funcy import pluck

from aplus import Promise
from coap import CoapClient
from coap.coapy.coapy.constants import (CREATED, CONTENT, BAD_REQUEST,
                                        NOT_FOUND, METHOD_NOT_ALLOWED,
                                        UNSUPPORTED_CONTENT_FORMAT,
                                        INTERNAL_SERVER_ERROR, BAD_GATEWAY,
                                        GATEWAY_TIMEOUT, VALID, CHANGED)
from openmtc_etsi import exc as e_exc
from openmtc_onem2m import exc as o_exc
from openmtc_server.Plugin import Plugin
from openmtc_server.configuration import (Configuration, ListOption,
                                          SimpleOption, BooleanOption)
from openmtc_server.exc import ConfigurationError
from openmtc_server.platform.gevent.ServerRack import GEventServerRack
from openmtc_server.transportdomain import (RequestMethod, Response,
                                            ErrorResponse, Connector)
from .server import CoapServer

uses_relative.append('coap')
uses_netloc.append('coap')


class ConnectorConfiguration(Configuration):
    __name__ = "Connector configuration"
    __options__ = {"interface": SimpleOption(default=""),
                   "host": SimpleOption(default=None),
                   "port": SimpleOption(int),
                   "is_wan": BooleanOption(default=None)}


class CoAPTransportPluginGatewayConfiguration(Configuration):
    __name__ = "CoAPTransportPluginGatewayConfiguration configuration"
    __options__ = {
        "connectors": ListOption(ConnectorConfiguration,
                                 default=(
                                     ConnectorConfiguration(port=5000,
                                                            is_wan=False),
                                     ConnectorConfiguration(port=4000,
                                                            is_wan=True)))
    }


class CoAPTransportPluginBackendConfiguration(Configuration):
    __name__ = "CoAPTransportPluginBackendConfiguration configuration"
    __options__ = {
        "connectors": ListOption(ConnectorConfiguration,
                                 default=(
                                     ConnectorConfiguration(port=15000,
                                                            is_wan=False),
                                     ConnectorConfiguration(port=14000,
                                                            is_wan=True)))
    }

_coap2generic = {
    CREATED: o_exc.STATUS_CREATED.http_status_code,
    CONTENT: o_exc.STATUS_OK.http_status_code,
    BAD_REQUEST: o_exc.STATUS_BAD_REQUEST.http_status_code,
    NOT_FOUND: o_exc.STATUS_NOT_FOUND.http_status_code,
    METHOD_NOT_ALLOWED: o_exc.STATUS_OPERATION_NOT_ALLOWED.http_status_code,
    UNSUPPORTED_CONTENT_FORMAT: o_exc.STATUS_BAD_REQUEST.http_status_code,
    INTERNAL_SERVER_ERROR: o_exc.STATUS_INTERNAL_SERVER_ERROR.http_status_code,
    162: e_exc.STATUS_BAD_GATEWAY,
    BAD_GATEWAY: e_exc.STATUS_BAD_GATEWAY,
    GATEWAY_TIMEOUT: e_exc.STATUS_GATEWAY_TIMEOUT,
    VALID: e_exc.STATUS_NOT_MODIFIED,
    CHANGED: 204
}


class COAPTransportPlugin(Plugin):
    __gateway_configuration__ = CoAPTransportPluginGatewayConfiguration
    __backend_configuration__ = CoAPTransportPluginBackendConfiguration

    def __init__(self, api, config, *args, **kw):
        super(COAPTransportPlugin, self).__init__(api, config, *args, **kw)
        self.ERROR_RESPONSE_MAX = 320
        self._clients = {}

    def _init(self):
        self.api.register_client(("coap", "coaps"), self.send_request)
        self.serverport = self.config.get("server-port")
        self.clientport = self.config.get("client-port")
        self._initialized()

    __methodmap = {
        RequestMethod.create: "POST",
        RequestMethod.notify: "NOTIFY",
        RequestMethod.delete: "DELETE",
        RequestMethod.update: "PUT",
        RequestMethod.retrieve: "GET"
    }

    def _raise_error_message(self, response):
        try:
            status_code = _coap2generic[response.code]
        except KeyError:
            self.logger.warning("Failed to map coap response code: %s",
                                response.code)
            status_code = o_exc.STATUS_INTERNAL_SERVER_ERROR.http_status_code

        err = ErrorResponse(
            status_code=status_code,
            payload=response.payload or "<no further information available>",
            content_type=response.content_format
        )
        self.logger.debug("Raising error response: %s", vars(err))

        return err

    def _get_client(self, parsed_url):
        coaps = parsed_url.scheme[-1].lower() == "s"
        port = parsed_url.port  # or (coaps and 443 or 80)
        host = parsed_url.hostname
        # path = parsed_url.path
        key = (host, port, coaps)
        try:
            return self._clients[key]
        except KeyError:
            # TODO: make connection_timeout and concurrency configurable
            client = self._clients[key] = CoapClient(parsed_url.scheme +
                                                     "://" + parsed_url.netloc,
                                                     self.clientport)
            return client

    def send_request(self, request):
        p = Promise()
        full_path = request.path
        parsed = urlparse(full_path)

        client = self._get_client(parsed)
        method = self.__methodmap[request.method]
        payload = request.payload
        content_type = request.content_type
        # TODO(rst): simple hack for ETSI requests, they have no RI
        try:
            token = request.metadata['X-M2M-RI']
        except KeyError:
            token = None

        path = parsed.path
        param_str = []

        if request.params:
            for k, v in request.params.items():
                param_str.append(k + "=" + str(v))

        if request.originator:
            param_str.append('fr=' + request.originator)

        # TODO(rst): handle metadata somehow
        # see TS-0008 6.2.4 Query String:
        # da, dr, ec, fc, fr, gid, nm, oet, ort, ret, rqt, rst, rc, ret, rp
        # and ro (see core protocol specification [2]) shall be carried in
        # query string.

        if param_str:
            path += '?' + '&'.join(param_str)

        # FIXME: rst: it seems to be that token is ignored
        try:  # rst: has to be changed when TS-0008 is updated
            content_type = content_type.replace(
                'application/onem2m-resource+xml', 'application/xml')
            content_type = content_type.replace(
                'application/onem2m-resource+json', 'application/json')
        except AttributeError:
            pass

        def _handle_response(response):
            self.logger.debug("_handle_response(%s)", response)

            if response.code > 100:
                p.reject(self._raise_error_message(response))
            else:
                try:
                    status_code = _coap2generic[response.code]
                except KeyError:
                    self.logger.warning("Failed to map coap response code: "
                                        "%s", response.code)
                    status_code = (o_exc.STATUS_INTERNAL_SERVER_ERROR
                                   .http_status_code)

                payload = response.payload
                content_type = response.content_format
                try:
                    # TODO (ren): can there be more than 1 element in the list?
                    option = response.findOption(8)[0]
                    location = option.value
                except AttributeError:
                    location = None

                resp = Response(
                    status_code=status_code,
                    payload=payload,
                    content_type=content_type,
                    location=location
                )

                p.fulfill(resp)

        client.request(method, path, payload, token=token,
                       content_type=content_type).then(_handle_response)

        return p

    def _find_address(self, address, family):
        localhost = None

        for interface in interfaces():
            try:
                if_data = ifaddresses(interface)[family]
                addresses = pluck("addr", if_data)
            except KeyError:
                pass
            else:
                if addresses:
                    for a in addresses:
                        if a not in ("::1", "127.0.0.1"):
                            return a.rsplit("%", 1)[0]
                        if a:
                            localhost = a

        if localhost:
            return localhost

        raise Exception("Failed to guess host for interface '%s'", address)

    def _find_addresses(self, family):
        addresses = []

        for interface in interfaces():
            try:
                if_data = ifaddresses(interface)[family]
                addresses += pluck("addr", if_data)
            except KeyError:
                pass

        return [a.rsplit("%", 1)[0] for a in addresses]

    def _guess_alternatives(self, address):
        if address not in ("::", "", "0.0.0.0"):
            return None

        hosts = self._find_addresses(AF_INET)

        for a in hosts[:]:
            self.logger.debug("Finding hostname for %s", a)
            try:
                host = getnameinfo((a, 0), 0)[0]
            except Exception as e:
                self.logger.warn("Failed to lookup name for address %s: %s",
                                 address, e)
            else:
                if host != a:
                    hosts.append(host)

        if address == "::":
            hosts.append("[::]")
            ipv6addresses = self._find_addresses(AF_INET6)
            for address in ipv6addresses:
                hosts.append("[" + address.split("%")[0] + "]")
                self.logger.debug("Finding hostname for %s", address)
                try:
                    host = getnameinfo((address, 0), 0)[0]
                except Exception as e:
                    self.logger.warn("Failed to lookup name for address %s: %s",
                                     address, e)
                else:
                    if host != address:
                        hosts.append(host)
        else:
            hosts.append("0.0.0.0")

        return hosts

    def _guess_host(self, address):
        if address not in ("::", "", "0.0.0.0"):
            if ":" in address:
                return "[" + address + "]"
            return address

        family = address == "::" and AF_INET6 or AF_INET

        host = self._find_address(address, family)

        if family == AF_INET6:
            return "[" + host + "]"
        return host

    def _start(self):
        servers = []
        additional_hostnames = self.config["global"].get(
            "additional_hostnames") or []

        if not isinstance(additional_hostnames, list):
            raise ConfigurationError("additional_hostnames is not a list")

        for endpoint in self.config.get("connectors", []):
            interface = endpoint["interface"]
            port = endpoint["port"]
            host = endpoint["host"]
            keyfile = endpoint.get("key")
            certfile = endpoint.get("crt")
            is_wan = endpoint.get("is_wan")

            if not host:
                host = self._guess_host(interface)
                self.logger.debug("No host specified for connector on '%s'. "
                                  "Guessing %s", interface, host)
                connectors = self._guess_alternatives(interface)
            else:
                connectors = []

            is_coaps = keyfile and certfile

            if is_coaps:
                scheme = "coaps"
                ssl_args = {"keyfile": keyfile, "certfile": certfile}
            else:
                scheme = "coap"
                ssl_args = None

            base_uri = "%s://%s:%s" % (scheme, host, port)
            connectors = [base_uri] + ["%s://%s:%s" % (scheme, host, port)
                                       for host in connectors]

            for hostname in additional_hostnames:
                alternative = "%s://%s" % (scheme, hostname, )
                if urlparse(alternative).port in (None, ''):
                    alternative = "%s:%s" % (alternative, port)
                connectors.append(alternative)

            if endpoint.is_wan is None:
                # TODO: guess if an interface is a WAN interface
                raise NotImplementedError()
            connector = Connector(base_uri, connectors, is_wan)

            servers.append(CoapServer(self.api.handle_request,
                                      connector=connector, address=interface,
                                      server_port=port, ssl_args=ssl_args))

            self.api.register_connector(connector)

        rack = self.__rack = GEventServerRack(servers)

        rack.start()
        self._started()

    def _stop(self):
        self.logger.debug("Waiting for CoaP server to stop")
        self.__rack.stop()
        self._stopped()

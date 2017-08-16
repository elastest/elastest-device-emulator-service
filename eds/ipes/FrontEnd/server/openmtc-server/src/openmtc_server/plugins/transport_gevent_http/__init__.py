from gevent.pywsgi import Input
from gevent.wsgi import WSGIServer
from urlparse import urlparse
from netifaces import ifaddresses, interfaces
from socket import getnameinfo, gaierror, getservbyname, AF_INET, AF_INET6
from time import time
from socket import error as SocketError

from funcy import pluck
from geventhttpclient.client import HTTPClient

from openmtc_server.Plugin import Plugin
from .wsgi import OpenMTCWSGIApplication
from openmtc_server.platform.gevent.ServerRack import GEventServerRack
from aplus import Promise
from openmtc_server.exc import ConfigurationError
from openmtc_server.transportdomain import (Response, ErrorResponse,
                                            RequestMethod, Connector)
from futile.caching import LRUCache
from openmtc.exc import OpenMTCNetworkError, ConnectionFailed
from openmtc_server.configuration import (Configuration, ListOption,
                                          SimpleOption, BooleanOption)


class ConnectorConfiguration(Configuration):
    __name__ = "Connector configuration"
    __options__ = {"interface": SimpleOption(default=""),
                   "host": SimpleOption(default=None),
                   "port": SimpleOption(int),
                   "is_wan": BooleanOption(default=None)}


class HTTPTransportPluginGatewayConfiguration(Configuration):
    __name__ = "HTTPTransportPluginGatewayConfiguration configuration"
    __options__ = {
        "connectors": ListOption(ConnectorConfiguration,
                                 default=(
                                     ConnectorConfiguration(port=5000,
                                                            is_wan=False),
                                     ConnectorConfiguration(port=4000,
                                                            is_wan=True)))
    }


class HTTPTransportPluginBackendConfiguration(Configuration):
    __name__ = "HTTPTransportPluginBackendConfiguration configuration"
    __options__ = {
        "connectors": ListOption(ConnectorConfiguration,
                                 default=(
                                     ConnectorConfiguration(port=15000,
                                                            is_wan=False),
                                     ConnectorConfiguration(port=14000,
                                                            is_wan=True)))
    }


class HTTPTransportPlugin(Plugin):
    ERROR_RESPONSE_MAX = 320

    __gateway_configuration__ = HTTPTransportPluginGatewayConfiguration
    __backend_configuration__ = HTTPTransportPluginBackendConfiguration

    def _init(self):
        # TODO: make max_items configurable
        self._clients = LRUCache(threadsafe=False)
        self.api.register_client(("http", "https"), self.send_request)

        self._initialized()

    __methodmap = {
        RequestMethod.create: "POST",
        RequestMethod.delete: "DELETE",
        RequestMethod.update: "PUT",
        RequestMethod.retrieve: "GET"
    }

    def _get_error_message(self, response, content_type=None):
        try:
            data = response.read(self.ERROR_RESPONSE_MAX and
                                 self.ERROR_RESPONSE_MAX + 1 or
                                 None)
            if not data:
                data = "<no further information available>"
            elif (self.ERROR_RESPONSE_MAX and
                  len(data) > self.ERROR_RESPONSE_MAX):
                data = data[:self.ERROR_RESPONSE_MAX] + " (truncated)\n"
            data = data.encode("utf-8")
        except Exception as e:
            data = "<failed to read error response: %s>\n" % (e, )
        if not data.endswith("\n") and content_type is 'text/plain':
            data += "\n"
        return data

    def _get_client(self, parsed_url):
        https = parsed_url.scheme[-1].lower() == "s"
        port = parsed_url.port or (https and 443 or 80)
        host = parsed_url.hostname
        key = (host, port, https)
        try:
            return self._clients[key]
        except KeyError:
            # TODO: make connection_timeout and concurrency configurable
            client = self._clients[key] = HTTPClient(host, port,
                                                     connection_timeout=120.0,
                                                     concurrency=50,
                                                     ssl=https)
            return client

    def _handle_network_error(self, exc, p, method, parsed, path, t,
                              exc_class=OpenMTCNetworkError):
        error_str = str(exc)
        if error_str in ("", "''"):
            error_str = repr(exc)
        logpath = "%s://%s%s" % (parsed.scheme, parsed.netloc, path)
        error_msg = "Error during HTTP request: %s. " \
                    "Request was: %s %s (%.4fs)" % (error_str, method,
                                                    logpath, time() - t)
        p.reject(exc_class(error_msg))

    def send_request(self, request):
        with Promise() as p:
            # TODO: caching of clients and answers
            # TODO: set accept
            # TODO: set auth
            # TODO: other headers?
            # TODO: params
            fullpath = request.path
            parsed = urlparse(fullpath)

            client = self._get_client(parsed)
            method = self.__methodmap[request.method]
            payload = request.payload

            if payload:
                headers = {"Content-Type": request.content_type}
                # TODO: do we need to set Content-Length?
            else:
                headers = {}

            t = time()

            if request.originator:
                headers["From"] = request.originator

            if request.metadata:
                for k, v in request.metadata.items():
                    headers[k] = v

            path = parsed.path
            self.logger.debug("Request params: %s", request.params)
            if request.params:
                path += "?"
                param_str = [k + "=" + str(v) for
                             k, v in request.params.items()]
                path += "&".join(param_str)

            self.logger.debug("%s %s (%s)\n%r", method, path, headers,
                              request.payload)

            try:
                # FIXME: rst: geventhttpclient host header is not ipv6 safe
                # it is missing the brackets around the IP
                # our notification server is ignoring it but other servers could
                # handle this as an error and it is not correct wrt the standard
                headers['Host'] = parsed.netloc
                payload = request.payload

                # this was a try/catch block before, but broke the code
                # TODO: if openmtc can have streams here, too, those also have
                # TODO: to be dealt with
                if type(payload) is Input:
                    payload = payload.read()

                response = client.request(method, path, payload, headers)
            except (SocketError, gaierror) as exc:
                self._handle_network_error(exc, p, method, parsed, path, t,
                                           ConnectionFailed)
            except Exception as exc:
                self.logger.exception("Error in HTTP request")
                self._handle_network_error(exc, p, method, parsed, path, t)
            else:
                try:
                    status_code = response.get_code()
                    content_type = response.get("Content-Type")
                    self.logger.debug("%s %s result: %s (%.4fs)", method,
                                      fullpath, status_code, time() - t)
                    self.logger.debug("Response headers: %s", response.items())
                    if status_code >= 400:
                        data = self._get_error_message(response, content_type)
                        if content_type is 'text/plain':
                            msg = "Error during execution: %s - %s" \
                                  "Request was: %s %s." % (status_code, data,
                                                           method, request.path)
                            p.reject(ErrorResponse(status_code, msg,
                                                   "text/plain"))
                        else:
                            p.reject(ErrorResponse(
                                status_code, data, content_type,
                                metadata=dict(response.headers)))
                    elif status_code < 200 or status_code >= 300:
                        raise OpenMTCNetworkError(status_code)
                    else:
                        p.fulfill(Response(status_code, response.read() or None,
                                           content_type, location=response.get(
                                               "Location") or response.get(
                                               "Content-Location"),
                                           metadata=dict(response.headers)))
                finally:
                    response.release()

        return p

    def _find_address(self, address, family):
        localhost = None

        for interface in interfaces():
            try:
                ifdata = ifaddresses(interface)[family]
                addresses = pluck("addr", ifdata)
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
                ifdata = ifaddresses(interface)[family]
                addresses += pluck("addr", ifdata)
            except KeyError:
                pass

        return [a.rsplit("%", 1)[0] for a in addresses]

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
                    self.logger.warn("Failed to lookup address %s: %s",
                                     address, e)
                else:
                    if host != address:
                        hosts.append(host)
        else:
            hosts.append("0.0.0.0")

        return hosts

    def _start(self):
        servers = []
        additional_hostnames = self.config["global"].get(
            "additional_hostnames", [])

        if not isinstance(additional_hostnames, list):
            raise ConfigurationError("additional_hostnames is not a list")

        require_auth = self.config["global"].get("require_auth", True)
        for endpoint in self.config.get("connectors", []):
            interface = endpoint["interface"]
            port = endpoint["port"]
            host = endpoint["host"]
            keyfile = endpoint.get("key")
            certfile = endpoint.get("crt")

            if not host:
                host = self._guess_host(interface)
                self.logger.info("No host specified for connector on '%s'. "
                                 "Guessing %s", interface, host)
                connectors = self._guess_alternatives(interface)
            else:
                connectors = []

            is_https = keyfile and certfile

            scheme = "https" if is_https else "http"
            base_uri = "%s://%s:%s" % (scheme, host, port)
            connectors = ["%s://%s:%s" % (scheme, host, port)
                          for host in connectors]

            default_port = getservbyname(scheme)

            if port == default_port:
                connectors.append("%s://%s" % (scheme, host))

            for hostname in additional_hostnames:
                alternative = "%s://%s" % (scheme, hostname)
                parsed_alternative = urlparse(alternative)
                alternative_port = parsed_alternative.port
                if alternative_port in (None, ''):
                    alternative_port = port
                    alternative = "%s:%s" % (alternative, port)
                connectors.append(alternative)

                if alternative_port == default_port:
                    connectors.append("%s://%s" %
                                      (scheme,
                                       parsed_alternative.hostname))

            if endpoint.is_wan is None:
                # TODO: guess if an interface is a WAN interface
                raise NotImplementedError()
            connector = Connector(base_uri, connectors, endpoint.is_wan)

            application = OpenMTCWSGIApplication(self.api.handle_request,
                                                 connector=connector,
                                                 server_address=interface,
                                                 require_auth=require_auth)

            if is_https:
                servers.append(WSGIServer(
                    (interface, port), application,
                    environ={'SERVER_NAME': 'openmtc.local'},
                    keyfile=keyfile, certfile=certfile))
            else:
                servers.append(WSGIServer(
                    (interface, port), application,
                    environ={'SERVER_NAME': 'openmtc.local'}))

            self.api.register_connector(connector)

        rack = self.__rack = GEventServerRack(servers)

        rack.start()

        self._started()

    def _stop(self):
        self.__rack.stop()
        self._stopped()

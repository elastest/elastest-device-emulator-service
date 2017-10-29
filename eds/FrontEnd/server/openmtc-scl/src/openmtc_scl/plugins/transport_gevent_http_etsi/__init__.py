from _socket import getservbyname
from copy import copy
from gevent.wsgi import WSGIServer
from netifaces import ifaddresses, interfaces
from socket import AF_INET, AF_INET6
from socket import getnameinfo
from urlparse import ParseResult, urlparse, urlunparse

from funcy import pluck
from openmtc.client.http import XIXClient
from openmtc.response import ErrorResponseConfirmation
from openmtc_scl.platform.gevent.ServerRack import GEventServerRack

from aplus import Promise
from futile.net.http.client.RestClient import RestClient
from futile.net.http.exc import HTTPError
from openmtc.exc import SCLError, OpenMTCNetworkError, STATUS_BAD_GATEWAY
from openmtc_scl.transportdomain import Response, ErrorResponse
from openmtc_server.Plugin import Plugin
from openmtc_server.exc import ConfigurationError
from .wsgi import SCLWSGIApplication


class HTTPTransportPlugin(Plugin):
    def _init(self):
        etsi_version = self.config["global"]["etsi_version"]
        etsi_compatibility = self.config["global"]["etsi_compatibility"]

        self.etsi_version_v2 = etsi_version >= "2.0"
        self.etsi_compatibility_needed = etsi_compatibility < "2.0"

        self.api.register_client(("http", "https"), self.send_request)

        self._initialized()

    __methodmap = {
        "CREATE": "POST",
        "DELETE": "DELETE",
        "UPDATE": "PUT",
        "RETRIEVE": "GET"
    }

    def send_request(self, request):
        with Promise() as p:
            client = RestClient(uri=request.path,
                                content_type=request.content_type,
                                cache=False)

            method = self.__methodmap[request.method]
            try:
                with client.request(method, "", request.payload) as r:
                    p.fulfill(Response(r.status, r.read() or None,
                                       r.getheader("Content-Type")))
            except HTTPError as e:
                p.reject(ErrorResponse(e.status, e.message, "text/plain"))

        return p

    def send_request_indication(self, request_indication):
        # TODO: rewrite HTTP request handling totally

        with Promise() as p:
            fullpath = request_indication.path
            parsed = urlparse(fullpath)
            request_indication = copy(request_indication)
            request_indication.path = urlunparse(ParseResult("", "",
                                                             *parsed[2:]))
            try:
                client = XIXClient(parsed.scheme + "://" + parsed.netloc,
                                   scl_base=None,
                                   etsi_v1_compatibility=self.etsi_compatibility_needed,
                                   etsi_v2=self.etsi_version_v2)
                response = client.send_request_indication(request_indication)
            except OpenMTCNetworkError as e:
                response = ErrorResponseConfirmation(STATUS_BAD_GATEWAY,
                                                     request_indication.method,
                                                     str(e))
                p.reject(response)
            except SCLError as e:
                response = ErrorResponseConfirmation(e.statusCode,
                                                     request_indication.method,
                                                     str(e))
                p.reject(response)
            else:
                #response = self._convert_response(fullpath, request_indication, response)
                if request_indication.method == "retrieve" and hasattr(response.resource, "path"):
                    response.resource.path = fullpath
                p.fulfill(response)

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
        prefer_xml = bool(self.config["global"].get("prefer_xml"))
        additional_hostnames = self.config["global"].get("additional_hostnames") or []

        if not isinstance(additional_hostnames, list):
            raise ConfigurationError("additional_hostnames is not a list")

        pretty = self.config.get("pretty_print", "auto")

        if pretty and pretty is not True:
            try:
                pretty = pretty.lower()
            except AttributeError:
                pretty = True
            else:
                if pretty == "auto":
                    pretty = None
                else:
                    pretty = True

        require_auth = self.config["global"].get("require_auth", True)

        for endpoint in self.config.get("endpoints") or []:
            interface = endpoint.get("interface") or ""
            port = endpoint["port"]
            personality = endpoint["personality"]
            host = endpoint.get("host")
            keyfile = endpoint.get("key")
            certfile = endpoint.get("crt")

            if not host:
                host = self._guess_host(interface)
                self.logger.info("No host specified for %s endpoint on '%s'. Guessing %s", personality, interface, host)
                alternatives = self._guess_alternatives(interface)
            else:
                alternatives = []

            application = SCLWSGIApplication(self.api.handle_request_indication,
                                             base_uri=None,
                                             server_address=interface,
                                             reference_point=personality,
                                             prefer_xml=prefer_xml,
                                             require_auth=require_auth,
                                             etsi_version_v2=self.etsi_version_v2,
                                             etsi_compatibility=self.etsi_compatibility_needed
                                             )

            if keyfile and certfile:
                scheme = "https"
                base_uri = application.base_uri = "https://%s:%s" % (host,
                                                                     port)
                servers.append(WSGIServer((interface, port), application,
                                          keyfile=keyfile, certfile=certfile))
            else:
                scheme = "http"
                base_uri = application.base_uri = "http://%s:%s" % (host, port)
                servers.append(WSGIServer((interface, port), application))

            self.api.register_endpoint(personality, base_uri)

            alternatives = ["%s://%s:%s" % (scheme, host, port)
                            for host in alternatives]

            default_port = getservbyname(scheme)

            if port == default_port:
                alternatives.append("%s://%s" % (scheme, host))

            if additional_hostnames:
                for hostname in additional_hostnames:
                    alternative = "%s://%s" % (scheme, hostname)
                    parsed_alternative = urlparse(alternative)
                    alternative_port = parsed_alternative.port
                    if alternative_port in (None, ''):
                        alternative_port = port
                        alternative = "%s:%s" % (alternative, port)
                    alternatives.append(alternative)

                    if alternative_port == default_port:
                        alternatives.append("%s://%s" % (scheme, parsed_alternative.hostname))

            if alternatives:
                self.api.register_alternative_endpoints(personality,
                                                        alternatives)

        rack = self.__rack = GEventServerRack(servers)

        rack.start()

        self._started()

    def _stop(self):
        self.__rack.stop()
        self._stopped()

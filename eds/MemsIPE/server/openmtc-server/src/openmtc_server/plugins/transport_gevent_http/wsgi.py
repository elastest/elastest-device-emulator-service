from werkzeug.http import parse_accept_header
from futile.logging import LoggerMixin
from werkzeug.wrappers import Request, Response
from urlparse import urlparse, urlunparse, ParseResult
from futile.net.http.exc import HTTPError, HTTPError400, HTTPError401,\
    HTTPError404, HTTPError405
from socket import AF_INET, AF_INET6, getaddrinfo, SOCK_STREAM
from futile.collections import get_iterable
from operator import itemgetter
from funcy import pluck
from .util import is_ipv4, is_ipv6
from _socket import gaierror
from openmtc_etsi.exc import SCLNotAcceptable
from openmtc_server.transportdomain import Request as GenericRequest, \
    RequestMethod, Response as GenericResponse, ResponseCode, ErrorResponse
from collections import Mapping


class EnvironProxy(Mapping):
    def __init__(self, environ):
        self.environ = environ

    def __getitem__(self, key):
        return self.environ["HTTP_" + key.upper().replace("-", "_")]

    def __len__(self):
        return len(self.environ)

    def __iter__(self):
        for k in self.environ:
            if not k.startswith("HTTP_"):
                continue
            yield k[5:].lower().replace("_", "-")


class OpenMTCWSGIApplication(LoggerMixin):
    __cached_addresses = {}

    def __init__(self, request_handler, server_address, connector,
                 require_auth, *args, **kw):
        super(OpenMTCWSGIApplication, self).__init__(*args, **kw)

        self.request_handler = request_handler
        self.require_auth = require_auth
        self.__cache = set()
        self.connector = connector

        if server_address == "::":
            self.__addresses = self._get_addresses(AF_INET6) | \
                self._get_addresses(AF_INET)
            self._resolve_host = self._resolve_host_ipv6
        elif server_address in ("", "0.0.0.0"):
            self.__addresses = self._get_addresses(AF_INET)
        else:
            self.__addresses = get_iterable(server_address)

        self.__valid_hostnames = [c.hostname for c in connector.infos]

        self.logger.debug("All listening addresses: %s", self.__addresses)

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
            info = getaddrinfo(host, 0, family, SOCK_STREAM)
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

    def __call__(self, environ, start_response):
        # TODO(rst): handle vary header
        with Request(environ) as request:

            # path = environ["PATH_INFO"]
            try:
                response = (self._handle_OPTIONS(request)
                            if request.method == "OPTIONS"
                            else self._handle_http_request(request))
            except HTTPError as e:
                response = Response(
                    response=e.message,
                    status=e.status)
            except SCLNotAcceptable as e:
                response = Response(
                    response=e,
                    status=406)

            return response(environ, start_response)

    def _handle_OPTIONS(self, request):
        # TODO: use full list of supported encodings
        accept = parse_accept_header(request.environ.get('HTTP_ACCEPT', ''))
        if not ('*/*' in accept or not accept or
                'application/json' in accept or
                'application/xml' in accept):
            raise HTTPError400('Only application/json and '
                               'application/xml are supported.')
        if not ('application/json' in accept or
                'application/xml' in accept):
            raise HTTPError405('Only application/json and '
                               'application/xml are supported.')
        return Response(
            response="",
            status=204
        )

    def _get_real_path(self, request):
        """
        return the URI needed for further processing. This is either a
        relative path if the request is to be processed internally or a
        full URI if the request is retargeted
        """

        # TODO: kca: deal with more complex host headers
        environ = request.environ
        path = environ["PATH_INFO"]

        if path.startswith('/'):
            return path

        parsed = urlparse(path)

        host_header = environ.get("HTTP_HOST")

        self.logger.debug("Host header: %s", host_header)

        # prefer the HOST header
        netloc = host_header or parsed.netloc
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
            target_port = parsed.scheme.lower() == "https" and "443" or "5000"

        target = (target_host, target_port)

        if target in self.__cache:
            return urlunparse(ParseResult("", "", *parsed[2:]))

        if (target_port == environ["SERVER_PORT"] and
                (self._resolve_host(target_host) & self.__addresses or
                    target_host in self.__valid_hostnames)):
            # port and host match -> not retargeted
            self.__cache.add(target)
            return urlunparse(ParseResult("", "", *parsed[2:]))

        # request is retargeted
        #
        # construct full URI if needed
        if not parsed.netloc:
            path = netloc + path
            if not parsed.scheme:
                path = request.environ['wsgi.url_scheme'] + "://" + path
        elif not parsed.scheme:
            path = "http://" + path
        print(path)

        return path

    def _handle_http_request(self, request):
        path = self._get_real_path(request)

        self.logger.debug("Real path: %s", path)

        # raise Exception(path)

        # TS 102.921 V1.1.1 C.2.3 next-to-last paragraph:
        # The requestingEntity primitive attribute shall be the uri-decoded
        # user-part of the HTTP basic authentication header. If no basic
        # authentication header is included in the request, the request is
        # rejected with 402 statusCode.

        # TS 102.921 V2.1.1 C.2.3 next-to-last paragraph:
        # The requestingEntity primitive attribute shall be included as a
        # HTTP From header. If no From header is included in the request,
        # the request is rejected with 402 statusCode.

        environ = request.environ
        env_get = environ.get

        originator = env_get("HTTP_FROM")

        auth = request.authorization
        if auth:
            username = auth.username
            password = auth.password
        else:
            username = password = None

        # TODO: Move higher up?
        if not username and not originator and self.require_auth:
            raise HTTPError401()

        viastr = env_get("HTTP_VIA")
        via = None
        if viastr:
            try:
                via = map(str.strip, viastr.split(","))
                via = [v.split(" ", 1)[-1] for v in via]
            except Exception as e:
                self.logger.warn("Failed to parse Via header %s: %s",
                                 viastr, e)
        else:
            via = None

        method = request.method

        if method == "GET":
            method = RequestMethod.retrieve
            payload = content_type = None
        elif method == "DELETE":
            method = RequestMethod.delete
            payload = content_type = None
        else:
            if method == "POST":
                method = RequestMethod.create
            elif method == "PUT":
                method = RequestMethod.update
            else:
                raise HTTPError405()

            payload = request.input_stream
            content_type = request.content_type

            if not content_type:
                raise HTTPError400("Content-Type header missing")

        request = GenericRequest(method, path, payload=payload,
                                 content_type=content_type,
                                 via=via,
                                 username=username,
                                 password=password,
                                 params=request.args,
                                 originator=originator,
                                 user_agent=env_get("HTTP_USER_AGENT"),
                                 accept=env_get("HTTP_ACCEPT"),
                                 metadata=EnvironProxy(environ),
                                 connector=self.connector)

        # TODO: REQUEST HEADERS!!!
#            request_indication = self.add_request_headers(req_ind, request)

        try:
            result_promise = self.request_handler(request)
            result = result_promise.get()
        except ErrorResponse as result:
            self.logger.info(result)
        except Exception as exc:
            self.logger.exception("Caught exception while handling request")
            result = GenericResponse(ResponseCode.internal_error, repr(exc),
                                     "text/plain")

        return self._map_generic_response(result)

    def _map_generic_response(self, response):
        data = response.payload or ""
        location = response.location
        content_location = response.content_location

        headers = []
        if location:
            headers.append(("Location", location))
        if content_location:
            headers.append(("Content-Location", content_location))

        for k, v in response.metadata.items():
            headers.append((k, v))

        return Response(
            status=response.status_code,
            response=data,
            content_type=response.content_type if data else None,
            headers=headers
        )

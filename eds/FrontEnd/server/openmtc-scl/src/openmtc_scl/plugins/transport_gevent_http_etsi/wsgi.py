from werkzeug.http import parse_accept_header
from futile.logging import LoggerMixin
from werkzeug.wrappers import Request, Response
from openmtc.scl import RetrieveRequestIndication, CreateRequestIndication, \
    DeleteRequestIndication, UpdateRequestIndication
from urlparse import urlparse, urlunparse, ParseResult
from futile.net.http.exc import HTTPError, HTTPError400, HTTPError401,\
    HTTPError404, HTTPError405
from socket import AF_INET, AF_INET6, getaddrinfo, SOCK_STREAM
from futile.collections import get_iterable
from operator import itemgetter
from funcy import pluck
from .util import is_ipv4, is_ipv6
from _socket import gaierror
from urllib2 import unquote
from openmtc_scl import log_error
from openmtc_scl.transportdomain.util import encode_result, encode_error
from openmtc_scl.transportdomain import Endpoint, Response as GenericResponse
from openmtc.exc import SCLNotAcceptable


class SCLWSGIApplication(LoggerMixin):
    __cached_addresses = {}

    def __init__(self, request_handler, server_address, base_uri,
                 reference_point, require_auth, etsi_version_v2,
                 etsi_compatibility,
                 uri_base="/m2m", pretty_print=None, prefer_xml=False,
                 *args, **kw):
        self.request_handler = request_handler
        self.uri_base = uri_base
        self.reference_point = reference_point
        self.require_auth = require_auth
        self.etsi_version_v2 = etsi_version_v2
        self.etsi_compatibility_needed = etsi_compatibility
        self.base_uri = base_uri
        self.prefer_xml = prefer_xml
        self.__cache = set()
        self.pretty_print = pretty_print

        if server_address == "::":
            self.__addresses = self._get_addresses(AF_INET6) | \
                               self._get_addresses(AF_INET)
            self._resolve_host = self._resolve_host_ipv6
        elif server_address in ("", "0.0.0.0"):
            self.__addresses = self._get_addresses(AF_INET)
        else:
            self.__addresses = get_iterable(server_address)

        self.logger.debug("All listening addresses: %s", self.__addresses)

    @property
    def base_uri(self):
        return self.__base_uri

    @base_uri.setter
    def base_uri(self, base_uri):
        self.__base_uri = base_uri
        self.endpoint = Endpoint(self.reference_point, base_uri)

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
            #if e.errno != -2:
            #    raise
            return set()

    def _resolve_host(self, host):
        if is_ipv4(host):
            return set([host])
        return self._getaddrinfo(host, AF_INET)

    def _resolve_host_ipv6(self, host):
        self.logger.debug("Resolving: %s", host)
        if is_ipv6(host):
            return set([host])
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

        #TODO: kca: deal with more complex host headers
        environ = request.environ
        path = environ["PATH_INFO"]
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

        if target_port == environ["SERVER_PORT"] and \
                self._resolve_host(target_host) & self.__addresses:
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

        return path

    def _handle_http_request(self, request):
        """
        try:
            path = urlparse(path).path
        except:
            raise HTTPError400("Invalid URI: %s" % (path, ))
        """

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

        if self.etsi_version_v2:
            requesting_entity = request.environ.get('HTTP_FROM')
        else:
            requesting_entity = None
        if self.etsi_compatibility_needed and not requesting_entity:
            try:
                requesting_entity = unquote(request.authorization
                                            .username).decode('utf-8')
            except AttributeError:
                requesting_entity = None

        self.logger.debug("Requesting entity: %s", requesting_entity)

        if not requesting_entity and self.require_auth:
            raise HTTPError401()

        try:
            mapping_function = getattr(self, "_map_" + request.method)
        except AttributeError:
            raise HTTPError405()

        try:
            req_ind = mapping_function(path, request)
            request_indication = self.add_request_headers(req_ind, request)

            request_indication.requestingEntity = requesting_entity or None

            try:
                viastr = request.environ["HTTP_VIA"]
            except KeyError:
                pass
            else:
                try:
                    via = map(str.strip, viastr.split(","))
                    request_indication.via = [v.split(" ", 1)[-1] for v in via]
                except Exception as e:
                    self.logger.warn("Failed to parse Via header %s: %s",
                                     viastr, e)

            result_promise = self.request_handler(request_indication,
                                                  self.endpoint)
            result = result_promise.get()
        except Exception as e:
            if log_error(e):
                self.logger.exception("Caught Exception in request handling")
            else:
                self.logger.error("Caught Exception in request handling: %s",
                                  repr(e))
            try:
                statuscode = e.statusCode
            except AttributeError:
                statuscode = 500
            accept, pretty = self._get_accept_and_pretty(request)
            content_type, data = encode_error(e, accept=accept, pretty=pretty)
            return Response(
                response=data,
                status=statuscode,
                content_type=content_type)

        if result.statusCode == 202:
            # result is a SuccessResponseConfirmation
            return Response(status=202)

        if isinstance(result, GenericResponse):
            return self._map_generic_response(result)

        result_mapper = getattr(self, "_map_" + request.method + "_result")

        return result_mapper(request, result)

    def add_request_headers(self, request_indication, request):
        headers = request.environ
        for n in ("correlationID", "rcat", "trpdt", "contactURI"):
            try:
                header = headers["HTTP_X_ETSI_" + n.upper()]
                setattr(request_indication, n, header)
            except KeyError:
                pass

        return request_indication

    def _map_generic_response(self, response):
        data = response.payload or ""
        return Response(
            status=response.status_code,
            response=data,
            content_type=response.content_type if data else None,
        )

    def _map_GET(self, path, request):
        args = request.args

        if path.endswith(("/contentInstances", "/discovery")):
            filter_criteria = {k: v for k, v in args.items()
                               if k not in ("ifNoneMatch", "searchString",
                                            "contentType", "searchPrefix",
                                            "maxSize")}

            if_none_match = args.getlist("ifNoneMatch")
            if if_none_match:
                filter_criteria["ifNoneMatch"] = if_none_match

            search_string = args.getlist("searchString")
            if search_string:
                filter_criteria["searchString"] = search_string

            content_type = args.getlist("contentType")
            if content_type:
                filter_criteria["contentType"] = content_type

            search_prefix = args.get("searchPrefix")
            max_size = args.get("maxSize")

            # obtain some filter-criteria from HTTP headers, where appropriate
            # TODO: kca: not sure if this is actually standard compliant, but it
            #seems like common sense. Check if its in the standard, if not, allow
            #to turn it off via config
            environ = request.environ
            for n in ("if_None_Match", "if_Unmodified_Since", "if_Modified_Since"):
                try:
                    header = environ["HTTP_" + n.upper()]
                except KeyError:
                    pass
                else:
                    filter_criteria.setdefault(n.replace("_", ""), header)

            request_indication = RetrieveRequestIndication(
                path,
                filterCriteria=filter_criteria,
                searchPrefix=search_prefix,
                maxSize=max_size
            )
        else:
            request_indication = RetrieveRequestIndication(path)
        return request_indication

    def _get_accept_and_pretty(self, request):
        environ = request.environ
        pretty = self.pretty_print
        if pretty is None:
            try:
                ua = environ["HTTP_USER_AGENT"]
            except KeyError:
                pass
            else:
                ua = ua.lower()
                pretty = "mozilla" in ua or "opera" in ua

        accept = environ.get("HTTP_ACCEPT") or None
        if accept in (None, "*/*"):
            accept = environ.get("CONTENT_TYPE") or None
        return accept, pretty

    def _map_GET_result(self, request, result):
        accept, pretty = self._get_accept_and_pretty(request)
        content_type, data = encode_result(result, accept=accept,
                                           pretty=pretty,
                                           prefer_xml=self.prefer_xml)

        if data is None:
            return Response(status=204)

        return Response(
            response=data,
            content_type=content_type,
        )

    def _map_POST(self, path, request):
        content_type = request.content_type
        if not content_type:
            raise HTTPError400("Content-Type header missing")
        request_indication = CreateRequestIndication(
            path=path,
            resource=request.input_stream,
            content_type=request.content_type
        )
        return request_indication

    def _map_PUT(self, path, request):
        content_type = request.content_type
        if not content_type:
            raise HTTPError400("Content-Type header missing")
        request_indication = UpdateRequestIndication(
            path=path,
            resource=request.input_stream,
            content_type=content_type
        )
        return request_indication

    def _map_PUT_result(self, request, result):
        return Response(
            response="",
            status=204
        )

    def _map_POST_result(self, request, result):
        if result.primitiveType == "notify":
            return Response(
                response="",
                status=204
            )

        accept, pretty = self._get_accept_and_pretty(request)
        content_type, data = encode_result(result, accept, pretty)
        resourceURI = result.resourceURI
        # TODO: full URI for Location header?

        return Response(
            response=data,
            status=201,
            content_type=content_type,
            headers=(
                ("Location", resourceURI),
                ("Content-Location", resourceURI)
            )
        )

    def _map_DELETE(self, path, request):
        request_indication = DeleteRequestIndication(
            path=path
        )
        return request_indication

    def _map_DELETE_result(self, request, result):
        return Response("", status=204)

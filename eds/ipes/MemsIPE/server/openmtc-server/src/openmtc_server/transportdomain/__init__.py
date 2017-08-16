from urlparse import urlparse, urlsplit
from aplus import Promise, RejectedPromise
from futile.collections import get_iterable
from futile import uc
from collections import defaultdict, namedtuple
from openmtc_etsi.response import SuccessResponseConfirmation
from openmtc_server import Component
from enum import IntEnum
from openmtc.exc import OpenMTCError
from openmtc_server.Event import BasicEvent
from threading import _start_new_thread

from openmtc_onem2m.transport import RequestMethod


class Request(namedtuple("RequestBase", ("method", "path", "payload",
                                         "content_type", "via",
                                         "username", "password",
                                         "id", "params",
                                         "originator", "user_agent",
                                         "accept", "metadata",
                                         "connector"))):
    __slots__ = ()

    def __new__(cls, method, path, payload=None, content_type=None, via=None,
                username=None, password=None, id=None, params=None,
                originator=None, user_agent=None, accept=None, metadata=None,
                connector=None):
        if method not in RequestMethod:
            raise ValueError("Invalid method: %s" % (method,))

        return super(Request, cls).__new__(cls, method=method, path=path,
                                           payload=payload,
                                           content_type=content_type, via=via,
                                           username=username, password=password,
                                           id=id, params=params,
                                           originator=originator,
                                           user_agent=user_agent, accept=accept,
                                           metadata=metadata or {},
                                           connector=connector)


class ResponseCode(IntEnum):
    ok = 200
    created = 201
    accepted = 202
    no_content = 204
    bad_request = 400
    unauthorized = 401
    forbidden = 403
    not_found = 404
    method_not_allowed = 405
    not_acceptable = 406
    request_timeout = 408
    conflict = 409
    unsupported_media_type = 415
    internal_error = 500
    not_implemented = 501
    bad_gateway = 502
    service_unavailable = 503
    gateway_timeout = 504

    error_min = 400


class Response(object):
    def __init__(self, status_code, payload=None, content_type=None, id=None,
                 location=None, content_location=None, metadata=None,
                 *args, **kw):
        super(Response, self).__init__(*args, **kw)

        status_code = int(status_code)
        self.status_code = status_code
        self.payload = payload
        self.content_type = content_type
        self.id = id
        self.metadata = metadata or {}
        self.location = location
        self.content_location = content_location

    @property
    def is_error(self):
        return self.status_code >= ResponseCode.error_min

    @property
    def statusCode(self):
        return self.status_code


class ErrorResponse(Response, Exception):
    def __init__(self, status_code=ResponseCode.internal_error,
                 payload=None, content_type=None, *args, **kw):
        if payload:
            content_type = content_type or "text/plain"

        super(ErrorResponse, self).__init__(status_code=status_code,
                                            payload=payload,
                                            content_type=content_type,
                                            *args, **kw)


class ConnectorInfo(namedtuple("ConnectorInfoBase",
                               ("scheme", "hostname", "port"))):
    def __new__(cls, scheme, hostname, port):
        assert scheme and hostname

        port = int(port) if port is not None else None
        scheme = str(scheme)
        hostname = uc(hostname)
        return super(ConnectorInfo, cls).__new__(cls, scheme, hostname, port)


class ConnectorSpec(namedtuple("ConnectorSpecBase",
                               ("scheme", "hostname", "port", "is_wan"))):
    def __new__(cls, scheme, hostname, port, is_wan):
        is_wan = bool(is_wan) if is_wan is not None else None
        port = int(port) if port is not None else None
        scheme = str(scheme) if scheme is not None else None
        hostname = uc(hostname) if hostname is not None else None
        return super(ConnectorSpec, cls).__new__(cls, scheme, hostname,
                                                  port, is_wan)

    def matches(self, info):
        return self.scheme in (None, info.scheme) and \
               self.hostname in (None, info.hostname) and \
               self.port in (None, info.port) and \
               self.is_wan in (None, info.is_wan)

    def matches_connector(self, connector):
        return any(map(self.matches, connector.specs))


class Connector(namedtuple("ConnectorBase", ("base_uri", "names", "is_wan",
                                             "infos", "specs", "routes"))):
    def __new__(cls, base_uri, names, is_wan=True):
        names = tuple(map(uc, set([base_uri] + names)))
        parsed_names = map(urlparse, map(unicode.lower, names))
        infos = tuple([ConnectorInfo(p.scheme, p.hostname, p.port)
                       for p in parsed_names])
        specs = tuple([ConnectorSpec(p.scheme, p.hostname, p.port, is_wan)
                       for p in parsed_names])
        return super(Connector, cls).__new__(cls, base_uri, names, is_wan,
                                             infos, specs, {})

    def register_route(self, route, handler):
        route = route.strip("/")

        if not route or "/" in route:
            raise OpenMTCError("Invalid route: %s" % (route,))

        routes = self.routes
        if route in routes:
            raise OpenMTCError("Route '%s' is already registered on %s.",
                               route, self.base_uri)

        routes[route] = handler


def _get_connector_info(uri):
    parsed = urlparse(uri)
    return ConnectorInfo(parsed.scheme, parsed.hostname, parsed.port)


class ConnectorEvent(BasicEvent):
    def register_handler(self, handler, filter=None, **kw):
        self._add_handler_data((filter, handler))

    def _fired(self, connector):
        for filter, handler in self._handlers:
            if not filter or filter.matches_connector(connector):
                self._execute_handler(handler, connector)


class EndpointEvent(BasicEvent):
    def register_handler(self, handler, scheme=None, type=None, **kw):
        self._add_handler_data((scheme, type, handler))

    def _fired(self, endpoint):
        for scheme, type, handler in self._handlers:
            if (scheme in (None, endpoint.scheme) and
                    type in (None, endpoint.reference_point)):
                self._execute_handler(handler, endpoint)


class TransportDomain(Component):
    def __init__(self, config, *args, **kw):
        """
        Create and initialize the transport domain.
        """

        super(TransportDomain, self).__init__(*args, **kw)
        self._api = None

        self.config = config

        self.disable_retargeting = (config["global"]
                                    ["disable_retargeting"])

        self.__generic_clients = {}
        self.connectors = {}
        self.retargeting_handlers = defaultdict(list)

    def initialize(self, api):
        self._api = api

    def start(self):
        pass

    def stop(self):
        pass

    def _fire_connectors_event(self, connectors, handler):
        if connectors and handler:
            try:
                handler(connectors)
            except Exception:
                self.logger.exception("Connector handler %s failed for %s",
                                      handler, connectors)

    def register_retargeting_handler(self, uri, handler):
        parsed = urlparse(uri)
        path = parsed.path
        parsed = ConnectorInfo(parsed.scheme, parsed.hostname, parsed.port)

        handlers = self.retargeting_handlers[parsed]

        for route, _ in handlers:
            if path == route or path.startswith(route + "/"):
                raise OpenMTCError("A retargeting handler is already "
                                   "registered for %s" % (uri,))

        handlers.append((path, handler))

    # TODO: remove handler from signature
    def unregister_retargeting_handler(self, uri, handler):
        parsed = urlparse(uri)
        path = parsed.path
        parsed = ConnectorInfo(parsed.scheme, parsed.hostname, parsed.port)

        handlers = self.retargeting_handlers[parsed]

        # TODO: clean empty entries
        try:
            handlers.remove((path, handler))
        except ValueError:
            self.logger.warn("Unable to unregister retargeting handler "
                             "for '%s': couldn't find handler in handlers", uri)

    def handle_request(self, request):
        # TODO: optimize
        parsed = urlparse(request.path.lower())
        path = parsed.path

        # TODO: optimize
        scheme = parsed.scheme

        if scheme:
            info = ConnectorInfo(scheme, parsed.hostname, parsed.port)
            try:
                connector = self.connectors[info]
            except KeyError:
                if not self.disable_retargeting:
                    try:
                        handlers = self.retargeting_handlers[info]
                    except KeyError:
                        pass
                    else:
                        path_startswith = path.startswith
                        for route, handler in handlers:
                            if path == route or path_startswith(route + "/"):
                                self.logger.debug("Re-targeting: %s",
                                                  request.path)
                                return handler(request)

                    self.logger.error("Refusing to retarget to %s",
                                      request.path)
                    raise ErrorResponse(ResponseCode.forbidden,
                                        "Refusing to re-target to %s" %
                                        (request.path,))
                else:
                    connector = None

        else:
            connector = request.connector

        try:
            handler = connector.routes[path.split("/", 2)[1]]
        except KeyError:
            try:
                handler = connector.routes['default']
            except KeyError:
                return RejectedPromise(ErrorResponse(
                    ResponseCode.not_found, "No route found for %s" % (path,)))

        return handler(request)

    def get_client(self, scheme):
        try:
            return self.__generic_clients[scheme]
        except KeyError:
            if not scheme:
                raise OpenMTCError("No scheme given")
            raise OpenMTCError("Unknown protocol: %s" % (scheme,))

    # def send_request(self, request):
    #     parsed = urlsplit(request.path)
    #
    #     client = self.get_client(parsed.scheme)
    #     return client(request)

    def send_request(self, request):
        parsed = urlsplit(request.path)
        try:
            params = request.params or {}
        except AttributeError:
            params = {}

        try:
            contactURI = params["contactURI"]
        except KeyError:
            contactURI = None

        for k, v in params.iteritems():
            try:
                params[k] = v.isoformat().replace('+', '%2B')
            except AttributeError:
                pass

        # 1. try to send immediately
        # 2. if it works, return result
        # 3. if it fails, do store and forward using correlationId

        client = self.get_client(parsed.scheme)

        if 'correlationID' in params:
            correlationID = params["correlationID"]

            def _forward(request, contactURI):
                response = client(request)

                def _handle_response(resp):
                    return self._send_saf_notify(resp, contactURI)

                def _handle_error(resp):
                    # initiate store & forward
                    # set timer
                    try:
                        contactURI = params["contactURI"]
                    except KeyError:
                        self.logger.warn("Trying Store & Forward without "
                                         "contactURI! No notify will be sent!")

                    def timerfunc():
                        self.logger.info(
                            "trpdt for correlationID %s reached. Trying to "
                            "forward again and sending notify.",
                            correlationID)

                        def _handle_result(result):
                            self.logger.info("Store & forward for %s succeeded."
                                             " Sending notify...",
                                             correlationID)
                            return self._send_saf_notify(result, contactURI)

                        def _handle_error(result):
                            self.logger.warn("Store & forward for %s failed. "
                                             "Sending notify...", correlationID)
                            return self._send_saf_notify(result, contactURI)

                        # self.send_request(request).then(_handle_result,
                        #                                 _handle_error)
                        return client(request).then(_handle_result,
                                                    _handle_error)

                    # TODO: check if that even works
                    try:
                        time = int(request.params["trpdt"])
                    except Exception as e:
                        self.logger.warn("Trying Store & Forward without trpdt "
                                         "value! Using default value")
                        time = 1

                    self._api.set_timer(time, timerfunc)

                if isinstance(response, Promise):
                    return response.then(_handle_response, _handle_error)
                elif isinstance(response, ErrorResponse):
                    return _handle_error(response)
                else:
                    return _handle_response(response)

            _start_new_thread(_forward, (request, contactURI))

            return SuccessResponseConfirmation(202)

        else:
            return client(request)

    def _send_saf_notify(self, response, path):
        try:
            notify = Request(RequestMethod.notify, path,
                             payload=response.payload,
                             content_type=response.content_type)
            self.logger.debug("Sending store & forward notify to '%s': %s",
                              path, notify)
            return self.send_request(notify)
        except Exception as e:
            self.logger.error("Unable to send store & forward notify to "
                              "'%s': %s", path, e)

    def register_client(self, schemes, client):
        """Register a generic client for the given schemes"""
        schemes = set(map(str.lower, get_iterable(schemes)))

        for scheme in schemes:
            self.__generic_clients[scheme] = client

    def is_local_path(self, path):
        # try:
        if path[0] == "/":
            return True
        # FIXME
        parsed = urlparse(path)
        parsed = ConnectorInfo(parsed.scheme, parsed.hostname, parsed.port)

        # except (TypeError, IndexError):2
        #    raise ValueError("Not a valid path: %s" % (path, ))

        return parsed in self.connectors

    def register_connector(self, connector):
        infos = connector.infos
        connectors = self.connectors
        for info in infos:
            if info in connectors:
                raise OpenMTCError("Connector already registered: %s", info)

        for info in infos:
            connectors[info] = connector

        self._api.events.connector_created.fire(connector)

    def get_connectors(self, spec=None, created_handler=None,
                       deleted_handler=None):
        if created_handler:
            self._api.events.connector_created.register_handler(created_handler)

        if deleted_handler:
            self._api.events.connector_deleted.register_handler(deleted_handler)

        connectors = set(self.connectors.values())
        if spec:
            connectors = filter(spec.matches_connector, connectors)

        return connectors

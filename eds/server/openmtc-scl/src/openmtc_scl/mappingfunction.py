from urllib2 import unquote
from openmtc.exc import OpenMTCNetworkError
from openmtc_etsi.model import FilterCriteria

from openmtc_server.transportdomain import (RequestMethod, ErrorResponse,
                                            Response, Request, ResponseCode)
from openmtc_etsi.scl import (
    CreateRequestIndication, RetrieveRequestIndication, DeleteRequestIndication,
    UpdateRequestIndication, NotifyRequestIndication)
from openmtc_etsi.response import (
    CreateResponseConfirmation, NotifyResponseConfirmation,
    DeleteResponseConfirmation, UpdateResponseConfirmation,
    RetrieveResponseConfirmation, ErrorResponseConfirmation)
from openmtc_etsi.exc import (SCLError, STATUS_ACCEPTED, SCLNotAcceptable,
                              OpenMTCError)
from openmtc_scl.transportdomain.util import (encode_result, encode_error,
                                              encode_request_indication_payload)
from futile.logging import get_logger
from openmtc_etsi.client.util import decode_result
import openmtc_scl.api as api
from openmtc_scl import ETSIEndpoint
from openmtc.model import ListAttribute
from openmtc_server.util import log_error

_logger = get_logger(__name__)


etsi_version_2 = api.config["etsi"]["etsi_version"] >= "2.0"

if etsi_version_2:
    etsi_compat = api.config["etsi"]["etsi_compatibility"] < "2.0"
    if etsi_compat:
        def get_requesting_entity(request):
            req_entity = request.originator
            _logger.debug("Originator: %s  - Username: %s", req_entity,
                          request.username)
            if not req_entity:
                req_entity = request.username
                if req_entity:
                    req_entity = unquote(req_entity)
            return req_entity
    else:
        def get_requesting_entity(request):
            _logger.debug("originator: %s", request.originator)
            return request.originator
else:
    etsi_compat = api.config["etsi"]["etsi_compatibility"] >= "2.0"
    if etsi_compat:
        def get_requesting_entity(request):
            req_entity = request.username
            _logger.debug("Username: %s  - Originator: %s", req_entity,
                          request.originator)
            if req_entity:
                return unquote(req_entity)
            return request.originator
    else:
        def get_requesting_entity(request):
            req_entity = request.username
            _logger.debug("Username: %s", req_entity)
            if req_entity:
                return unquote(req_entity)


def map_request_to_request_indication(request):
    path = request.path
    method = request.method
    if method == RequestMethod.create:
        req_ind = CreateRequestIndication(path=path, resource=request.payload,
                                          content_type=request.content_type)
    elif method == RequestMethod.retrieve:
        req_ind = RetrieveRequestIndication(path)
        if path.endswith(("/contentInstances", "/discovery")):
            args = request.params
            filter_criteria = {k: v for k, v in args.items() if
                               k not in ("ifNoneMatch", "searchString",
                                         "contentType", "searchPrefix",
                                         "maxSize")}
            filter_criteria = FilterCriteria(**filter_criteria)
            if_none_match = args.getlist("ifNoneMatch")
            if if_none_match:
                filter_criteria.ifNoneMatch = if_none_match
            search_string = args.getlist("searchString")
            if search_string:
                filter_criteria.searchString = search_string
            content_type = args.getlist("contentType")
            if content_type:
                filter_criteria.contentType = content_type
            req_ind.filterCriteria = filter_criteria
            if path.endswith("/discovery"):
                req_ind.searchPrefix = args.get("searchPrefix")
                req_ind.maxSize = args.get("maxSize")
            # obtain some filter-criteria from HTTP headers, where appropriate
            # TODO: kca: not sure if this is actually standard compliant, but it
            # seems like common sense. Check if its in the standard, if not,
            # allow to turn it off via config
            # TODO: use generic format
            environ = request.metadata
            for n in ("if_None_Match", "if_Unmodified_Since",
                      "if_Modified_Since"):
                try:
                    header = environ["HTTP_" + n.upper()]
                except KeyError:
                    pass
                else:
                    filter_criteria.setdefault(n.replace("_", ""), header)

    elif method == RequestMethod.update:
        req_ind = UpdateRequestIndication(path=path,
                                          resource=request.payload,
                                          content_type=request.content_type)
    elif method == RequestMethod.delete:
        req_ind = DeleteRequestIndication(path)
    elif method == RequestMethod.notify:
        req_ind = NotifyRequestIndication(path=path,
                                          resource=request.payload,
                                          content_type=request.content_type)
    else:
        raise ErrorResponse(ResponseCode.method_not_allowed)
# TODO: set correlationID, rcat, trpdt
    req_ind.requestingEntity = get_requesting_entity(request)
    via = request.via
    if via:
        req_ind.via = request.via
    return req_ind


def get_etsi_request_mapper(handle_request_indication, reference_point):
    def etsi_request_mapper(request):
        # TODO: unify so that thjs is not needed
        req_ind = map_request_to_request_indication(request)

        endpoint = ETSIEndpoint(reference_point, request.connector.base_uri)

        try:
            return handle_request_indication(req_ind, endpoint) \
                .then(lambda response: map_response_confirmation_to_response(
                    request, response),
                lambda response: map_error_response_confirmation_to_response(
                    request, response))
        except SCLError as exc:
            raise ErrorResponse(status_code=exc.StatusCode,
                                payload=str(exc))
        except Exception as exc:
            raise ErrorResponse(payload=repr(exc))
    return etsi_request_mapper


def map_response_confirmation_to_response(request, response):
    try:
        primitiveType = response.primitiveType
    except AttributeError:
        if isinstance(response, Response):
            return response
        raise

    config = api.config
    status_code = response.statusCode

    if status_code == STATUS_ACCEPTED:
        return Response(ResponseCode.accepted)

    pretty = config["global"].get("pretty_print")
    if pretty is None:
        user_agent = request.user_agent
        pretty = user_agent and ("opera" in user_agent or
                                 "mozilla" in user_agent)

    location = None
    if primitiveType in ("create", "retrieve"):
        try:
            content_type, data = encode_result(response, accept=request.accept,
                                               pretty=pretty)
        except SCLNotAcceptable as exc:
            status_code = exc.statusCode
            data = str(exc)
            content_type = "text/plain"
        else:
            if primitiveType == "create":
                location = response.resourceURI
    else:
        data = content_type = None

    if data is None:
        return Response(ResponseCode.no_content)

    return Response(
        status_code=status_code,
        payload=data,
        content_type=content_type,
        location=location
    )


def map_error_response_confirmation_to_response(request, response):
    if log_error(response):
        _logger.exception("Caught Exception in request handling")
    else:
        _logger.debug("Caught Exception in request handling: %s",
                      repr(response))

    if isinstance(response, ErrorResponse):
        return response

    try:
        statuscode = response.statusCode
    except AttributeError:
        statuscode = ResponseCode.internal_error

    config = api.config
    pretty = config["global"].get("pretty_print")
    if pretty is None:
        user_agent = request.user_agent
        pretty = user_agent and ("opera" in user_agent or
                                 "mozilla" in user_agent)

    content_type, data = encode_error(response, accept=request.accept,
                                      pretty=pretty)

    return ErrorResponse(
        payload=data,
        status_code=statuscode,
        content_type=content_type)


def map_request_indication_to_request(request_indication):
    try:
        request_indication.content_type
    except AttributeError:
        content_type = data = None
    else:
        content_type, data = encode_request_indication_payload(
            request_indication)

    method = method_map[request_indication.method]

    if method == RequestMethod.retrieve:
        # params
        try:
            params = {k: v for k, v in
                      request_indication.filterCriteria.values.items() if
                      v is not None}
        except AttributeError:
            params = {}
        if request_indication.searchPrefix:
            params['searchPrefix'] = request_indication.searchPrefix
        if request_indication.maxSize:
            params['maxSize'] = request_indication.maxSize
    else:
        params = {}

    # TODO: Via handling
    return Request(method=method,
                   path=request_indication.path,
                   originator=request_indication.requestingEntity,
                   content_type=content_type,
                   payload=data,
                   params=params)


def map_response_to_response_confirmation(method, path, response):

    try:
        content_type = response.content_type
    except AttributeError:
        content_type = None

    if method in ("create", "retrieve", "update"):
        try:
            payload = response.payload
        except AttributeError:
            payload = None
            pass
        d, ct = decode_result(path, payload, content_type)
    else:
        d, ct = None, None

    if method == "create":
        # try to detect fields when response from retargeted create response
        # returned. i.e. expirationTime
        fields = [a.name for a in d.attributes if
                  (getattr(d, a.name) is not None) and
                  not (a.default and getattr(d, a.name) == a.default) and
                  not (isinstance(a, ListAttribute) and not getattr(d, a.name))]
        return CreateResponseConfirmation(resourceURI=response.location,
                                          resource=d, content_type=ct,
                                          fields=fields)
    if method == "notify":
        return NotifyResponseConfirmation()
    if method == "retrieve":
        return RetrieveResponseConfirmation(resource=d, content_type=ct)
    if method == "update":
        return UpdateResponseConfirmation(resource=d, content_type=ct)
    if method == "delete":
        return DeleteResponseConfirmation()
    raise OpenMTCError("Unhandled method: %s", method)


def map_error_response_to_error_response_confirmation(request_indication,
                                                      request, response):
    if log_error(response):
        _logger.exception("Caught Exception in request handling")
    else:
        _logger.debug("Caught Exception in request handling: %s",
                      repr(response))

    if isinstance(response, OpenMTCNetworkError):
        return response

    if isinstance(response, ErrorResponseConfirmation):
        return response

    try:
        status_code = response.statusCode
    except AttributeError:
        status_code = ResponseCode.internal_error

    config = api.config
    pretty = config["global"].get("pretty_print")
    if pretty is None:
        user_agent = request.user_agent
        pretty = user_agent and ("opera" in user_agent or
                                 "mozilla" in user_agent)

    content_type, data = encode_error(response, accept=request.accept,
                                      pretty=pretty)

    return ErrorResponseConfirmation(status_code, request_indication.method,
                                     data)


method_map = {
    "create": RequestMethod.create,
    "retrieve": RequestMethod.retrieve,
    "notify": RequestMethod.create,
    "update": RequestMethod.update,
    "delete": RequestMethod.delete,
    "execute": RequestMethod.update
}


def get_request_method(request_indication_method):
    try:
        return method_map[request_indication_method]
    except KeyError:
        raise ValueError("Invalid request indication method: %s",
                         request_indication_method)

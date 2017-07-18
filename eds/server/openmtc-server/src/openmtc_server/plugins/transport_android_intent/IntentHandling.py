from openmtc.response import ErrorResponseConfirmation
from openmtc.scl import RetrieveRequestIndication, CreateRequestIndication, \
    UpdateRequestIndication, \
    DeleteRequestIndication
from openmtc_scl.serializer import JsonSerializer

from IntentError import IntentError
from futile.logging import LoggerMixin
from openmtc_scl.transportdomain import Endpoint
from openmtc_server.exc import ConfigurationError
from .client import IntentClient


class IntentRequest():
    content_type = ""
    content = ""
    method = None
    replyAction = None
    issuer = ""
    intentRequestId = ""
    searchStrings = None
    context = None
    requestCategory = None
    tolerantDelay = None
    contactURI = None

    def __init__(self, issuer, request_dict, context, logger):

        self.logger = logger
        self.issuer = issuer
        self.context = context

        self.logger.info("request dict is " + str(request_dict))

        if "method" in request_dict:
            # if request_dict.has_key("method"):
            self.method = request_dict[
                "method"]  # create, update, retrieve, update

        else:
            raise IntentError("Extra field method is not present")
            return

        try:
            self.method = request_dict[
                "method"]  # create, update, retrieve, update
            self.logger.info("method: %s", self.method)
        except KeyError:
            raise ConfigurationError("Extra field method is not present")

        if request_dict.has_key("path"):
            self.path = request_dict.get(
                "path")  # http://something, e.g. "http://some.host:1234/m2m/applications"
            self.logger.info("path: " + str(self.path))
        else:
            raise IntentError("Extra field path is not present")
            return

        if request_dict.has_key("content_type"):
            self.content_type = request_dict.get(
                "content_type")  # application/json
        else:
            self.logger.info(
                "Extra field content_type not provided, default value application/json used")
            self.content_type = "application/json"
        self.logger.info("content_type: " + str(self.content_type))

        if request_dict.has_key("requestId"):
            self.intentRequestId = request_dict.get("requestId")
            self.logger.info("requestId is " + self.intentRequestId)
        else:
            self.logger.info("Extra field requestId is not present")

        if request_dict.has_key("replyAction"):
            self.replyAction = request_dict.get("replyAction")
            self.logger.info("replyAction: " + str(self.replyAction))
        else:
            raise IntentError("Extra field replyAction is not present")
            return
        if request_dict.has_key("searchStrings"):
            self.searchStrings = request_dict.get("searchStrings")
            self.logger.info("searchStrings: " + str(self.searchStrings))
        else:
            self.logger.info("no searchStrings present")

        if request_dict.has_key("requestCategory"):
            self.requestCategory = request_dict.get("requestCategory")
            self.logger.info("requestCategory: " + str(self.requestCategory))
        else:
            self.logger.info("no requestCategory present, assuming default 7")
            self.requestCategory = 7

        if request_dict.has_key("tolerantDelay"):
            self.tolerantDelay = request_dict.get("tolerantDelay")
            self.logger.info("tolerantDelay: " + str(self.tolerantDelay))
        else:
            self.logger.info("no tolerantDelay present, assuming default 30s")
            self.tolerantDelay = 30

        if request_dict.has_key("contactURI"):
            self.contactURI = request_dict.get("contactURI")
            self.logger.info("contactURI: " + str(self.contactURI))
        else:
            self.logger.info("no contactURI present")

        if request_dict.has_key("content"):
            self.content = request_dict.get("content")
            self.logger.info("content: " + str(self.content))
        else:
            self.logger.info("Extra field content was not provided")

        if len(self.content) is 0:
            self.logger.info("content is empty")


class IntentHandler(LoggerMixin):
    serializer = JsonSerializer()

    def __init__(self, logger, config):
        self.logger = logger
        self.config = config
        self.endpoint = Endpoint(base_uri="intent://",
                                 reference_point="dIa")

    def intent_extras_to_dict(self, intent_request):

        extras = intent_request.getExtras()
        if extras is None:
            return None

        request_dict = {}
        keySet = extras.keySet()
        iterator = keySet.iterator()

        while iterator.hasNext():
            key = iterator.next()
            elem = extras.get(key)
            request_dict[key] = elem

        return request_dict

    def parseRequest(self, issuer, request_dict, context=None):

        parsedRequest = IntentRequest(issuer, request_dict, context,
                                      self.logger)
        return parsedRequest

    def handleParsedRequest(self, parsedRequest, request_handler, queue):

        self.logger.info(
            "handle parsed request: parsed req is " + str(parsedRequest))
        self.logger.info("request handler is " + str(
            request_handler) + " and queue is " + str(queue))
        if request_handler is not None:
            try:
                mapping_function = getattr(self, "_map_" + parsedRequest.method)
            except AttributeError:
                return IntentError()

            request_indication = mapping_function(parsedRequest.path,
                                                  parsedRequest)
            self.logger.info("request indication is " + str(request_indication))

            result_promise = request_handler(request_indication,
                                             endpoint=self.endpoint)
            result_mapper = getattr(self,
                                    "_map_" + parsedRequest.method + "_result")
            try:
                result = result_promise.get()
                self.logger.info("result is : " + str(result))
                return result_mapper(parsedRequest, result,
                                     parsedRequest.context)
            except Exception as e:
                result = ErrorResponseConfirmation(500,
                                                   request_indication.method,
                                                   repr(e))
                self.logger.info("result is : " + str(result))
                self.handle_result(parsedRequest, result, parsedRequest.context)
                return {'request': request_indication, 'result': result}
                # return result_mapper(parsedRequest, result, parsedRequest.context)
        elif queue is not None:
            self.logger.info("adding a request to the queue ")
            queue.put(parsedRequest)

    def executeQueuedRequests(self, queue, request_handler):

        #        parsed_request = queue.get(block=True, timeout=None)
        #        result = self.handleParsedRequest(parsed_request, request_handler, None)
        #        self.handle_result(parsed_request, result, parsed_request.context)
        while True:
            try:
                parsed_request = queue.get(block=True, timeout=1)
                result = self.handleParsedRequest(parsed_request,
                                                  request_handler, None)
                self.handle_result(parsed_request, result,
                                   parsed_request.context)
            except:
                continue

    def get_optional_params(self, request):
        correlationID = None
        rcat = None
        trpdt = None
        contactURI = None
        if self.config.has_key("enable_store_and_forward"):
            if self.config["enable_store_and_forward"]["correlation_id"]:
                correlationID = request.intentRequestId
            if self.config["enable_store_and_forward"]["rcat"]:
                rcat = request.requestCategory
            if self.config["enable_store_and_forward"]["trpdt"]:
                trpdt = request.tolerantDelay
            if self.config["enable_store_and_forward"]["contact_uri"]:
                contactURI = request.contactURI
        return (correlationID, rcat, trpdt, contactURI)

    def handle_result(self, request, result, context=None):
        self.logger.info(
            "request is " + str(request) + " and the result " + str(result))

        self.logger.info("handling result")
        if context is not None:
            self.logger.info("context is not none")
            self.logger.info("replyAction: " + str(request.replyAction))
            self.logger.info("issuer: " + str(request.issuer))
            client = IntentClient(str(request.issuer), str(request.replyAction),
                                  self.logger, None)
            self.logger.info("created intent client ")

            if isinstance(result, ErrorResponseConfirmation):
                self.logger.info("error while processing request")
                client.send_IntentError(context, request, result)
            else:
                self.logger.info("sending ok result " + str(result))
                client.send_IntentResponse(context, request, result)
        else:
            self.logger.info("context is none")

    def _map_retrieve(self, path, request):
        filter_criteria = None
        if request.searchStrings is not None:
            self.logger.info(
                "using searchStrings [" + request.searchStrings + "] in retrieve")
            filter_criteria = {}
            filter_criteria["searchStrings"] = request.searchStrings
        optional_params = self.get_optional_params(request)
        return RetrieveRequestIndication(path,
                                         filterCriteria=filter_criteria,
                                         correlationID=optional_params[0],
                                         rcat=optional_params[1],
                                         trpdt=optional_params[2],
                                         contactURI=optional_params[3])

    def _map_retrieve_result(self, request, result, context=None):

        self.handle_result(request, result, context)

        return {"request": request,
                "response": result
                }

    def _map_create(self, path, request):
        self.logger.info("content_type is " + request.content_type)
        if request.content_type and request.content_type != "application/json":
            self.logger.error("application type is not application/json");
            # send error 400 Unhandled content type

        self.logger.info("resource is " + str(request.content))
        optional_params = self.get_optional_params(request)

        return CreateRequestIndication(
            path=path,
            resource=request.content,
            content_type=request.content_type,
            correlationID=optional_params[0],
            rcat=optional_params[1],
            trpdt=optional_params[2],
            contactURI=optional_params[3])

    def _map_create_result(self, request, result, context=None):
        # TODO: kca: I'm assuming here that result always is STATUS_CREATED, is that the case?
        # (not counting EXECUTE, which is just not handled yet)

        self.logger.info("sent Post request")
        self.logger.info("sent Post request, result is " + str(result))
        if hasattr(result, "resourceURI"):
            self.logger.info("result resource URI is " + result.resourceURI)
        # TODO:kca: Which Content-Type to set here?

        self.handle_result(request, result, context)
        result = {"request": request,
                  "response": result
                  }
        return result

    def _map_delete(self, path, request):
        optional_params = self.get_optional_params(request)
        return DeleteRequestIndication(path,
                                       correlationID=optional_params[0],
                                       rcat=optional_params[1],
                                       trpdt=optional_params[2],
                                       contactURI=optional_params[3])

    def _map_delete_result(self, request, result, context=None):
        self.logger.info("sent Delete request")
        self.handle_result(request, result, context)
        result = {"request": request,
                  "response": result
                  }
        return result

    def _map_update(self, path, request):
        self.logger.info("content_type is " + request.content_type)
        self.logger.info("resource is " + str(request.content))
        return UpdateRequestIndication(path=path,
                                       resource=request.content,
                                       content_type=request.content_type,
                                       correlationID=optional_params[0],
                                       rcat=optional_params[1],
                                       trpdt=optional_params[2],
                                       contactURI=optional_params[3])

    def _map_update_result(self, request, result, context=None):
        self.handle_result(request, result, context)
        result = {"request": request,
                  "response": result
                  }
        return result

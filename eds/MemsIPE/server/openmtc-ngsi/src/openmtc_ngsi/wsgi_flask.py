from flask import Flask, request, Response, abort

from openmtc_ngsi.resources_ngsi9 import (NGSI9ContextEntityResource,
                                          NGSI9SubscriptionResource,
                                          NGSI9SubscriptionsResource)
import logging
from openmtc_ngsi.ngsi import NGSI_9, NGSI_10
from openmtc_ngsi.xml import InvalidRequest, NGSIXMLParser, NGSIXMLWriter
import openmtc_ngsi.requests as requests
from json import loads
from base64 import b64decode
from openmtc_ngsi.resources_base import api
from openmtc_ngsi.resources_ngsi10 import (NGSI10ContextEntityResource,
                                           NGSI10SubscriptionsResource,
                                           NGSI10SubscriptionResource)
from openmtc_ngsi.ngsi_json import NGSIJSONReader, NGSIJSONWriter

# logger = get_logger(__name__)
logging.basicConfig()
logger = logging.getLogger('ngsi')
logger.setLevel(10)
app = Flask("OpenMTC-NGSI")
api.init_app(app)

xml_parser = NGSIXMLParser()
xml_response_serializer = NGSIXMLWriter()

json_parser = NGSIJSONReader()
json_response_serializer = NGSIJSONWriter()

ngsi9 = NGSI_9()
ngsi10 = NGSI_10()


def reset():
    global ngsi9, ngsi10
    ngsi9 = NGSI_9()
    ngsi10 = NGSI_10()


data = {}

_after_notify_hook = None


def ngsi_rest_method(prefix):
    def decorator(f):
        request_type = getattr(requests, f.__name__[0].upper() +
                               f.__name__[1:] + "Request")
        route = "/" + prefix + "/" + f.__name__
        route2 = "/" + prefix.lower() + "/" + f.__name__

        def rest_method():
            request_type, f = data[request.path]
            if not request.content_type:
                logger.warning("No content type set, assuming XML input")
                inputtype = "xml"
            elif request.content_type in ("application/xml", "text/xml"):
                inputtype = "xml"
            elif request.content_type in ("application/json", "text/json"):
                inputtype = "json"
            else:
                return Response("Unacceptable content-type: %s.\
                                Expected one of application/xml, text/xml, "
                                "application/json, text/json." %
                                (request.content_type,), status=400)

            if inputtype == "xml":
                parser = xml_parser
                response_serializer = xml_response_serializer
            else:
                parser = json_parser
                response_serializer = json_response_serializer

            try:
                ngsi_request = parser.parse_request(request.data, request_type)
            except InvalidRequest as e:
                return Response(str(e), status=400)

            response = f(ngsi_request)

            response = response_serializer.serialize(response)
            logger.debug(response)
            return response

        app.add_url_rule(route, f.__name__, rest_method, methods=["POST"])
        app.add_url_rule(route2, f.__name__, rest_method, methods=["POST"])

        data[route] = (request_type, f)
        return rest_method

    return decorator


@ngsi_rest_method("NGSI9")
def registerContext(ngsi_request):
    return ngsi9.registerContext(ngsi_request)


@ngsi_rest_method("NGSI9")
def discoverContextAvailability(ngsi_request):
    return ngsi9.discoverContextAvailability(ngsi_request)


@ngsi_rest_method("NGSI9")
def subscribeContextAvailability(ngsi_request):
    return ngsi9.subscribeContextAvailability(ngsi_request)


@ngsi_rest_method("NGSI9")
def unsubscribeContextAvailability(ngsi_request):
    return ngsi9.unsubscribeContextAvailability(ngsi_request)


@ngsi_rest_method("NGSI9")
def updateContextAvailabilitySubscription(ngsi_request):
    return ngsi9.updateContextAvailabilitySubscription(ngsi_request)


@ngsi_rest_method("NGSI10")
def updateContext(ngsi_request):
    return ngsi10.updateContext(ngsi_request)


@ngsi_rest_method("NGSI10")
def queryContext(ngsi_request):
    return ngsi10.queryContext(ngsi_request)


@ngsi_rest_method("NGSI10")
def subscribeContext(ngsi_request):
    return ngsi10.subscribeContext(ngsi_request)


@ngsi_rest_method("NGSI10")
def updateContextSubscription(ngsi_request):
    return ngsi10.updateContextSubscription(ngsi_request)


@ngsi_rest_method("NGSI10")
def unsubscribeContext(ngsi_request):
    return ngsi10.unsubscribeContext(ngsi_request)


@app.route("/event", methods=["POST"])
def handle_event():
    """Handles event notifications sent by the event service.

    Registers a new context that is forwarded to the SCL automatically.
    """
    """Retrieve information from notify request"""
    data = request.json
    event = data["contextResponses"][0]["contextElement"]

    """Creation of Registration request (App + Containers)"""
    entityid = requests.EntityId(id=event["id"], type=event["type"],
                                 isPattern=False)
    contextregatt = []
    for attribute in event["attributes"]:
        contextregatt.append(
            requests.ContextRegistrationAttribute(name=attribute["name"],
                                                  type=attribute["type"],
                                                  isDomain=False, metadata=[])
        )
    contextreg = requests.ContextRegistration(
        entityIdList=[entityid], contextRegistrationAttributeList=contextregatt,
        registrationMetaData=None, providingApplication=None)
    reg = requests.RegisterContextRequest(contextRegistrationList=[contextreg])

    """Send registration request"""
    ngsi9.registerContext(reg)

    """Creation of update request (fills up contentInstances)"""
    contextattr = []
    for attribute in event["attributes"]:
        contextattr.append(
            requests.ContextAttribute(name=attribute["name"],
                                      type=attribute["type"],
                                      contextValue=attribute["value"],
                                      metadata=[])
        )
    contextel = requests.ContextElement(entityId=entityid,
                                        attributeDomainName=None,
                                        contextAttributeList=contextattr,
                                        domainMetadata=[])
    update = requests.UpdateContextRequest(contextElementList=[contextel],
                                           updateAction='UPDATE')

    """Send update request"""
    ngsi10.updateContext(update)

    return ""


@app.route("/_notify/<num>", methods=["POST"])
def notify(num):
    try:
        data = request.json
        decoded = b64decode(data["notify"]["representation"]["$t"])
        try:
            data = loads(decoded)
        except ValueError:
            data = loads(b64decode(decoded))
        if len(data) != 1:
            abort(400)
        logger.debug('Got notification %s' % data)
        type, object = data.items()[0]
    except (KeyError, TypeError, ValueError):
        logger.exception("Failed to get notification data")
        abort(400)

    # logger.debug(data)
    try:
        handler = globals()["ngsi" + num]
    except KeyError:
        abort(404)

    r = handler.handle_notification(type, object)

    _anh = _after_notify_hook
    if r and _anh:
        try:
            _anh(num, data)
        except:
            logger.exception("Error in notification hook.")

    return ""


api.add_resource(
    NGSI9ContextEntityResource,
    '/NGSI9/contextEntities',
    '/NGSI9/contextEntities/<string:entity_id>',
    '/NGSI9/contextEntities/<string:entity_id>/attributes',
    '/NGSI9/contextEntities/<string:entity_id>/attributes/<string:attribute>',
    '/NGSI9/contextTypes/<string:entity_type>',
    '/NGSI9/contextTypes/<string:entity_type>/attributes',
    '/NGSI9/contextTypes/<string:entity_type>/attributes/<string:attribute>',
)

api.add_resource(
    NGSI9SubscriptionsResource,
    "/NGSI9/contextAvailabilitySubscriptions"
)

api.add_resource(
    NGSI9SubscriptionResource,
    "/NGSI9/contextAvailabilitySubscriptions/<string:subscription_id>"
)

api.add_resource(
    NGSI10ContextEntityResource,
    '/NGSI10/contextEntities',
    '/NGSI10/contextEntities/<string:entity_id>',
    '/NGSI10/contextEntities/<string:entity_id>/attributes',
    '/NGSI10/contextEntities/<string:entity_id>/attributes/<string:attribute>',
    '/NGSI10/contextTypes/<string:entity_type>',
    '/NGSI10/contextTypes/<string:entity_type>/attributes',
    '/NGSI10/contextTypes/<string:entity_type>/attributes/<string:attribute>',
)

api.add_resource(
    NGSI10SubscriptionsResource,
    "/NGSI10/contextAvailabilitySubscriptions"
)

api.add_resource(
    NGSI10SubscriptionResource,
    "/NGSI10/contextAvailabilitySubscriptions/<string:subscription_id>"
)

_server = None


def main():
    global _server
    from futile.net.http.server.wsgi import ThreadingWSGIServer
    _server = ThreadingWSGIServer(("0.0.0.0", 5050), app)
    _server.serve_forever(1)
    # app.run(debug = True, port = 5050)


if __name__ == "__main__":
    main()

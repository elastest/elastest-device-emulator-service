from base64 import b64encode
from collections import OrderedDict
import json
from futile.logging import get_logger
from openmtc_etsi.response import CreateResponseConfirmation, RetrieveResponseConfirmation, UpdateResponseConfirmation, \
    NotifyResponseConfirmation, ErrorResponseConfirmation, SuccessResponseConfirmation
from openmtc_etsi.response import DeleteResponseConfirmation
from openmtc_etsi.scl import CreateRequestIndication, RetrieveRequestIndication, UpdateRequestIndication, \
    NotifyRequestIndication
from openmtc_etsi.scl import DeleteRequestIndication
from json import loads
from openmtc_etsi.serializer import JsonSerializer

"""THIS IS A DIRECT COPY OF openmtc_scl/platform/openxsp/util.py"""

logger = get_logger(__name__)

serializer = JsonSerializer()

_response_map = {
    "create": CreateResponseConfirmation,
    "delete": DeleteResponseConfirmation,
    "retrieve": RetrieveResponseConfirmation,
    "update": UpdateResponseConfirmation,
    "notify": NotifyResponseConfirmation
}

_request_map = {
    "create": CreateRequestIndication,
    "delete": DeleteRequestIndication,
    "retrieve": RetrieveRequestIndication,
    "update": UpdateRequestIndication,
    "notify": NotifyRequestIndication
}


def marshal_request_indication(request_indication):
    """
    message = {
        "path": request_indication.path,
        "method": request_indication.method
    }
    """
    message = request_indication.__dict__


    method = message["method"] = request_indication.method.value
    message["path"] = request_indication.path

    # message = dict(message)

    def encode_representation(representation):
        # TODO: this is an excerpt from Serializer.encode_values
        # prvide a better serializer interface so that no code duplication is needed
        payload = representation["$t"]
        if not representation.get("contentType"):
            if isinstance(payload, ErrorResponseConfirmation):
                payload = serializer.encode_error(payload, False, "utf-8")
            else:
                payload = serializer.encode(payload, False, "utf-8")
            representation["contentType"] = "application/json"
        representation["$t"] = b64encode(payload)

    try:
        resource = request_indication.resource
        ct = message["content_type"] = request_indication.content_type
        if not ct:
            message["typename"] = request_indication.typename
            if method == "notify":
                if request_indication.typename == 'notifyCollection':
                    notifies = resource["notify"]
                    for notify in notifies:
                        encode_representation(notify["representation"])
                else:
                    encode_representation(resource["representation"])

        encoded = serializer.encode(resource)
        logger.debug("encoded: %s", encoded)
        message["resource"] = json.loads(encoded)
    except AttributeError:
        pass

    logger.debug("Marshalled request indication: %s", message)

    return message


def unmarshal_request_indication(message):
    logger.debug("Unmarshalling request indication: %s", message)
    method = message.pop("method")

    try:
        res = _request_map[method]
    except KeyError:
        raise NotImplementedError(method)
    if message.get("content_type"):
        message["typename"] = None
    return res(**message)


def marshal_response(response):
    message = response.__dict__

    logger.debug("Marshalling result values: %s", message)

    try:
        resource = message["resource"]
    except KeyError:
        pass
    else:
        encoded = serializer.encode(resource)
        message["resource"] = json.loads(encoded)

    message["primitiveType"] = response.primitiveType

    logger.debug("marshalled result: %s", message)
    return message


def marshal_error_response(response, method):
    try:
        code = response.statusCode
    except Exception as e:
        logger.error("Failed to marshal response %r: %s" % (response, e))
        code = 500
    else:
        try:
            errorInfo = response.errorInfo
        except:
            errorInfo = str(response)

    return {
        "primitiveType": method,
        "statusCode": code,
        "errorInfo": errorInfo
    }


def unmarshal_response(message):
    try:
        statusCode = message["statusCode"]

        if statusCode >= 400:
            raise ErrorResponseConfirmation(**message)
        elif statusCode == 202:
            return SuccessResponseConfirmation(**message)
        else:
            primitive_type = message["primitiveType"]
            cls = _response_map[primitive_type]
            message.pop("statusCode")

            # fix by ren. doesn't look like it would break anything
            message.pop("primitiveType")

            try:
                resource = message["resource"]
            except KeyError:
                pass
            else:
                if not message.get("content_type") and message["resource"]:
                    message["resource"] = \
                        serializer.parse_representation(resource)

        return cls(**message)
    except:
        raise


def unmarshal_error_response(message):
    try:
        return ErrorResponseConfirmation(**message["message"])
    except:
        raise

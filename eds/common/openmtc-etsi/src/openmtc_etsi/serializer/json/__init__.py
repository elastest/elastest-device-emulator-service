from openmtc.model import Resource, Entity
from openmtc_etsi.serializer import Serializer
from openmtc_etsi.response import get_status_message, get_status_message_safe,\
    ErrorResponseConfirmation
from futile.logging import DEBUG, get_logger
from futile import uc
from json import JSONEncoder
from openmtc_etsi.serializer.json.exc import JSONError
from base64 import b64encode

logger = get_logger(__name__)

try:
    from ujson import load, loads
    logger.debug("using ujson for decoding JSON")
except ImportError:
    try:
        from yajl import load, loads
        logger.debug("using yajl for decoding JSON")
    except ImportError:
        try:
            # simplejson is faster on decoding, tiny bit slower on encoding
            from simplejson import load, loads
            logger.debug("using simplejson for decoding JSON")
        except ImportError:
            logger.debug("using builtin json for decoding JSON")
            from json import load, loads


del logger


def _default(x):
    if isinstance(x, Resource):
        return {
            "id": x.name,
            "$t": x.path
        }

    if isinstance(x, Entity):
        return x.values

    try:
        isoformat = x.isoformat
    except AttributeError:
        raise TypeError("%s (%s)" % (x, type(x)))

    return isoformat()

_simple_encoder = JSONEncoder(check_circular=False, separators=(',', ':'),
                              default=_default)

dumps = _simple_encoder.encode


def iter_dumps(o):
    return _simple_encoder.iterencode(o, True)


class JsonSerializer(Serializer):
    encoder = JSONEncoder(default=_default, indent=2, separators=(',', ':'),
                          check_circular=False)

    def __init__(self, type_factory=None, *args, **kw):
        # TODO: remove type_factory stuff
        if type_factory is None:
            from openmtc_etsi.model import get_etsi_type as type_factory
        self.get_resource_type = type_factory

    def encode(self, resource, pretty=False, encoding="utf-8", fields=None):
        representation = self.get_representation(resource, fields=fields)

        try:
            membersContentResponses = resource.membersContentResponses
        except AttributeError:
            pass
        else:
            l = []
            representation["membersContent"]["membersContentResponses"] = {"status": l}
            for r in membersContentResponses:
                v = {
                    "statusCode": r.status,
                    "id": r.id,
                    "lastModifiedTime": r.lastModifiedTime
                }

                try:
                    error_info = r.errorInfo
                except AttributeError:
                    try:
                        v["resourceURI"] = r.resourceURI
                    except AttributeError:
                        pass

                    try:
                        resource = r.resource
                    except AttributeError:
                        pass
                    else:
                        v["content"] = {
                            "contentType": "application/json",
                            "$t": b64encode(self.encode(resource, pretty))
                        }
                else:
                    v["content"] = {
                        "contentType": "text/plain",
                        "$t": b64encode(error_info)
                    }

                l.append(v)

        self.logger.debug("Encoding representation: %s", representation)
        if not pretty:
            return dumps(representation)
        return self.encoder.encode(representation)

    def iterencode(self, resource, pretty=False):
        representation = self.get_representation(resource)
        self.logger.debug("Encoding representation: %s", representation)
        if not pretty:
            return iter_dumps(representation)
        return self.encoder.iterencode(representation, True)

    def encode_error(self, error, pretty=False, encoding="utf-8"):
        try:
            statuscode = error.statusCode
        except AttributeError:
            status = "STATUS_INTERNAL_SERVER_ERROR"
        else:
            _, status = get_status_message_safe(statuscode)

        representation = {
            "errorInfo": {
                "statusCode": status,
                "additionalInfo": error.payload if hasattr(error, "payload") else uc(error)
            }
        }
        if not pretty:
            return dumps(representation)
        return self.encoder.encode(representation)

    def encode_values(self, typename, values, filter_none=False, pretty=False,
                      encoding="utf-8"):
        if filter_none:
            values = {k: v for k, v in values.items() if v is not None}
        try:
            status_code = values["statusCode"]
        except KeyError:
            pass
        except TypeError as e:  # HACK retargeted update?
            if isinstance(values, str):
                self.logger.debug("error encoding values: %s",e)
                return values
            else:
                raise
        else:
            # notify
            if not isinstance(status_code, basestring):
                if not filter_none:
                    values = values.copy()
                values["statusCode"] = get_status_message(status_code)
            representation = values["representation"].copy()
            payload = representation["$t"]
            if not representation.get("contentType"):
                if isinstance(payload, ErrorResponseConfirmation):
                    payload = self.encode_error(payload, pretty, encoding)
                else:
                    payload = self.encode(payload, pretty, encoding)
                representation["contentType"] = "application/json"
            representation["$t"] = b64encode(payload)
            values["representation"] = representation
        if not pretty:
            return dumps({typename: values})
        return self.encoder.encode({typename: values})

    if Serializer.get_class_logger().isEnabledFor(DEBUG):
        def decode(self, s):
            try:
                s = s.read()
            except AttributeError:
                pass
            return self.decode_string(s)
    else:
        def decode(self, s):
            entity = self.load(s)
            return self.decode_values(entity)
    decode_resource_values = decode

    def decode_string(self, s):
        self.logger.debug("Reading JSON input: %s", s)
        entity = self.load_string(s)
        return self.decode_values(entity)

    def load_string(self, s):
        self.logger.debug("Reading JSON input: %s", s)
        try:
            return loads(s)
        except ValueError as e:
            raise JSONError("Invalid JSON input: " + str(e))

    def load_pa_content(self, s):
        try:
            s = s.read()
        except AttributeError:
            pass
        self.logger.debug("Reading JSON input (PA): %s", s)
        return loads(s)

    if Serializer.get_class_logger().isEnabledFor(DEBUG):
        def load(self, s):
            try:
                s = s.read()
            except AttributeError:
                pass
            return self.load_string(s)
    else:
        def load(self, s):
            if not hasattr(s, "read"):
                return self.load_string(s)
            if not hasattr(s, "seek"):
                return self.load_string(s.read())

            try:
                return load(s)
            except ValueError as e:
                s.seek(0)
                raise JSONError("Invalid JSON input: " + str(e))



from openmtc_etsi.serializer import Serializer
from base64 import b64encode
from openmtc_etsi.response import get_status_message_safe, get_status_message,\
    ErrorResponseConfirmation
from futile.logging import DEBUG
from futile import uc
from openmtc_etsi.exc import SCLSyntaxError


class DictSerializer(Serializer):
    def __init__(self, type_factory=None, *args, **kw):
        super(DictSerializer, self).__init__(*args, **kw)
        if type_factory is None:
            from openmtc.model.etsi import get_etsi_type as type_factory
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
                        # TODO_ is this the right content type?
                        "contentType": "text/plain",
                        "$t": b64encode(error_info)
                    }

                l.append(v)

        self.logger.debug("Encoding representation: %s", representation)
        if not pretty:
            return self.dumps(representation)
        return self.pretty_dumps(representation)

    def iterencode(self, resource, pretty=False):
        representation = self.get_representation(resource)
        self.logger.debug("Encoding representation: %s", representation)
        if not pretty:
            return self.iter_dumps(representation)
        return self.pretty_iter_dumps(representation, True)

    def iter_dumps(self, o):
        return (self.dumps(o), )

    def pretty_iter_dumps(self, o):
        return (self.pretty_dumps(o), )

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
                "additionalInfo": uc(error)
            }
        }
        if not pretty:
            return self.dumps(representation)
        return self.pretty_dumps(representation)

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
                self.logger.debug("error encoding values: %s", e)
                return values
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
                    payload = self.encode_error(payload, pretty, "utf-8")
                else:
                    payload = self.encode(payload, pretty, "utf-8")
                representation["contentType"] = "application/json"
            representation["$t"] = b64encode(payload)
            values["representation"] = representation
        if not pretty:
            return self.dumps({typename: values})
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
        entity = self.load_string(s)
        return self.decode_values(entity)

    def load_string(self, s):
        try:
            return self.loads(s)
        except Exception as e:
            raise SCLSyntaxError("Invalid input: " + str(e))

    def load_pa_content(self, s):
        try:
            s = s.read()
        except AttributeError:
            pass
        return self.loads(s)

    def read_load(self, s):
        try:
            s = s.read()
        except AttributeError:
            pass
        return self.load_string(s)

    if Serializer.get_class_logger().isEnabledFor(DEBUG):
        load = read_load
    else:
        def load(self, s):
            if not hasattr(s, "read"):
                return self.load_string(s)
            if not hasattr(s, "seek"):
                return self.load_string(s.read())

            try:
                return self.load_file(s)
            except ValueError as e:
                s.seek(0)
                raise SCLSyntaxError("Invalid input: " + str(e))

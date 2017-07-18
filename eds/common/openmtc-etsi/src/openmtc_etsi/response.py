import openmtc_etsi.exc
import futile.logging
from openmtc_etsi.exc import OpenMTCError, STATUS_OK, STATUS_CREATED,\
    STATUS_INTERNAL_SERVER_ERROR


_logger = futile.logging.get_logger(__name__)

_messages = {}

for k, v in vars(openmtc_etsi.exc).items():
    if k.startswith("STATUS_"):
        _messages[v] = k

del k, v

_messages[404] = "STATUS_NOT_FOUND"


def get_status_message(status_code):
    try:
        return _messages[int(status_code)]
    except (ValueError, TypeError, KeyError):
        raise ValueError("Invalid status code: %s" % (status_code, ))


def get_status_message_safe(status_code):
    try:
        return status_code, get_status_message(status_code)
    except ValueError:
        _logger.exception("Failed to get status message for statuscode %r",
                          status_code)
        return STATUS_INTERNAL_SERVER_ERROR, "STATUS_INTERNAL_SERVER_ERROR"


class ResponseConfirmation(object):
    def __init__(self, statusCode, *args, **kw):
        if statusCode not in _messages:
            raise ValueError("Invalid status code: %s" % (statusCode, ))

        super(ResponseConfirmation, self).__init__(*args, **kw)

        self.statusCode = statusCode

    @property
    def status(self):
        return _messages[self.statusCode]

    def __str__(self):
        return "%s: %s" % (type(self).__name__, self.status)

# class Notify(ResponseConfirmation):
#     def __init__(self, statusCode, representation, subscription, *args, **kw):
#         super(Notify, self).__init__(statusCode=statusCode, *args, **kw)
#
#         self.representation = representation
#         self.subscriptionReference = subscription


class SuccessResponseConfirmation(ResponseConfirmation):
    def __init__(self, statusCode, *args, **kw):
        super(SuccessResponseConfirmation, self).__init__(
            statusCode=statusCode, *args, **kw)

        if statusCode >= 400:
            raise ValueError("Invalid success code: %s" % (statusCode, ))


class RetrieveResponseConfirmation(SuccessResponseConfirmation):
    primitiveType = "retrieve"

    def __init__(self, resource, content_type=None, *args, **kw):
        super(RetrieveResponseConfirmation, self).__init__(
            statusCode=STATUS_OK, *args, **kw)

        # TODO: kca: the name of this attr should correspond to the resource
        # TODO: type name
        self.resource = resource
        self.content_type = content_type


class UpdateResponseConfirmation(SuccessResponseConfirmation):
    primitiveType = "update"

    def __init__(self, resource=None, content_type=None, *args, **kw):
        super(UpdateResponseConfirmation, self).__init__(
            statusCode=STATUS_OK, *args, **kw)

        self.resource = resource
        self.content_type = content_type


class CreateResponseConfirmation(SuccessResponseConfirmation):
    primitiveType = "create"

    def __init__(self, resourceURI=None, resource=None, fields=(),
                 content_type=None, *args, **kw):
        super(CreateResponseConfirmation, self).__init__(
            statusCode=STATUS_CREATED, *args, **kw)

        if resource is None and not resourceURI:
            raise ValueError("Either resource or resourceURI must be specified")

        self.resource = resource
        self.fields = fields
        self.content_type = content_type

        self.resourceURI = (resourceURI if
                            resourceURI is not None else
                            resource.path)


class DeleteResponseConfirmation(SuccessResponseConfirmation):
    primitiveType = "delete"

    def __init__(self, *args, **kw):
        super(DeleteResponseConfirmation, self).__init__(
            statusCode=STATUS_OK, *args, **kw)


class NotifyResponseConfirmation(SuccessResponseConfirmation):
    primitiveType = "notify"

    def __init__(self, *args, **kw):
        super(NotifyResponseConfirmation, self).__init__(
            statusCode=STATUS_OK, *args, **kw)


class ErrorResponseConfirmation(ResponseConfirmation, OpenMTCError):
    def __init__(self, statusCode, primitiveType, errorInfo, *args, **kw):
        super(ErrorResponseConfirmation, self).__init__(
            statusCode=statusCode, *args, **kw)

        if statusCode < 400:
            raise ValueError("Invalid error code: %s" % (statusCode, ))

        self.errorInfo = errorInfo
        self.primitiveType = primitiveType

    def __str__(self):
        return "%s: %s" % (self.status, self.errorInfo)

    def __repr__(self):
        return "{}({}, {}, {})".format(type(self).__name__, self.status,
                                       self.primitiveType, self.errorInfo)

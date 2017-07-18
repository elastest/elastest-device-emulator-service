"""
Created on 26.05.2013

@author: kca
"""
from openmtc.exc import OpenMTCError

STATUS_OK = 200
STATUS_CREATED = 201
STATUS_ACCEPTED = 202
STATUS_NOT_MODIFIED = 304
STATUS_BAD_REQUEST = 400
STATUS_PERMISSION_DENIED = 401
STATUS_FORBIDDEN = 403
STATUS_NOT_FOUND = 404
STATUS_METHOD_NOT_ALLOWED = 405
STATUS_NOT_ACCEPTABLE = 406
STATUS_REQUEST_TIMEOUT = 408
STATUS_CONFLICT = 409
STATUS_UNSUPPORTED_MEDIA_TYPE = 415
STATUS_INTERNAL_SERVER_ERROR = 500
STATUS_NOT_IMPLEMENTED = 501
STATUS_BAD_GATEWAY = 502
STATUS_SERVICE_UNAVAILABLE = 503
STATUS_GATEWAY_TIMEOUT = 504
STATUS_DELETED = 410
STATUS_EXPIRED = 404


class SCLError(OpenMTCError):
    statusCode = STATUS_INTERNAL_SERVER_ERROR


class SCLNotFound(SCLError):
    statusCode = STATUS_NOT_FOUND


class SCLMethodNotAllowed(SCLError):
    statusCode = STATUS_METHOD_NOT_ALLOWED


class SCLNotImplemented(SCLError):
    statusCode = STATUS_NOT_IMPLEMENTED


ResourceNotFound = SCLNotFound


class SCLConflict(SCLError):
    statusCode = STATUS_CONFLICT


Conflict = SCLConflict


class SCLBadRequest(SCLError):
    statusCode = STATUS_BAD_REQUEST


class SCLSyntaxError(SCLBadRequest):
    statusCode = STATUS_BAD_REQUEST


class SCLValueError(SCLSyntaxError, ValueError):
    pass

SclValueError = SCLValueError


class SCLTypeError(SCLSyntaxError, TypeError):
    pass

SclTypeError = SCLTypeError


class SCLMissingValue(SCLSyntaxError):
    pass


class SCLNotAcceptable(SCLError):
    statusCode = STATUS_NOT_ACCEPTABLE


class SCLPermissionDenied(SCLError):
    statusCode = STATUS_PERMISSION_DENIED


class SCLForbidden(SCLError):
    statusCode = STATUS_FORBIDDEN


class SCLBadGateway(SCLError):
    statusCode = STATUS_BAD_GATEWAY


_error_map = {
    STATUS_INTERNAL_SERVER_ERROR: SCLError
}


def get_error_class(status_code):
    return _error_map.get(int(status_code), SCLError)

for c in SCLError.__subclasses__():
    try:
        code = vars(c)["statusCode"]
    except KeyError:
        continue
    _error_map[code] = c

del c, code

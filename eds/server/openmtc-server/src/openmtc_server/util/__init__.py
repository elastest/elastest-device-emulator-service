from urllib import quote
from mimeparse import parse_mime_type
import aplus
from futile.logging import get_logger
from openmtc.exc import OpenMTCNetworkError
from openmtc_etsi.exc import SCLError
from openmtc_etsi.response import ErrorResponseConfirmation
from openmtc_onem2m.exc import CSEError
from openmtc_onem2m.transport import OneM2MErrorResponse
from openmtc_server.transportdomain import ErrorResponse

logger = get_logger(__name__)


def log_error(error):
    try:
        return error.status_code == 500
    except AttributeError:
        try:
            return error.statusCode == 500
        except AttributeError:
            return not isinstance(error, (OpenMTCNetworkError, CSEError,
                                          ErrorResponse, OneM2MErrorResponse,
                                          SCLError, ErrorResponseConfirmation))


aplus.log_error = log_error


def get_regex_path_component():
    # see http://tools.ietf.org/html/rfc3986#section-3.3
    # path-abempty  = *( "/" segment )
    # segment       = *pchar
    # pchar         = unreserved / pct-encoded / sub-delims / ":" / "@"
    # pct-encoded = "%" HEXDIG HEXDIG
    # unreserved  = ALPHA / DIGIT / "-" / "." / "_" / "~"
    # sub-delims  = "!" / "$" / "&" / """ / "(" / ")" / "*" / "+" / "," / ";" /
    #               "="

    unreserved = r"[\w\.\-~]"
    pct_encoded = "%[A-Fa-f0-9][A-Fa-f0-9]"
    sub_delims = r"[!$&'()\*\+,;=]"

    pchar = "(?:" + unreserved + "|" + pct_encoded + "|" + sub_delims + "|:|@)"
    segment = pchar + "+"

    return segment


def uri_safe(s):
    return quote(s.replace("/", "_"))


def is_text_content(mimetype):
    try:
        maintype, subtype, _ = parse_mime_type(mimetype)

        maintype = maintype.lower()

        if maintype == "text":
            return True

        if maintype == "application":
            return subtype.rpartition("+")[-1].lower() in ("xml", "json")
    except Exception as e:
        logger.warn("Failed to parse mimetype '%s': %s", mimetype, e)

    return False


def join_url(base, path):
    if not base.endswith("/"):
        if not path.startswith("/"):
            base += "/"
    elif path.startswith("/"):
        path = path[1:]
    return base + path

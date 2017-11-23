from openmtc_etsi.exc import SCLValueError, SCLBadRequest
from openmtc.model.exc import ModelTypeError
from futile.logging import get_logger
from openmtc_etsi.serializer import get_serializer


_logger = get_logger(__name__)


def decode_result(path, rawdata, content_type):
    # TODO: rst rawdata can not be handled in the program, i.e. GSCL register
    # if content_type not in ("application/xml", "application/json"):
    #     return RetrieveResponseConfirmation(rawdata,
    #                                         content_type=content_type)
    if not rawdata:
        return None, None

    try:
        serializer = get_serializer(content_type)
    except SCLBadRequest:
        # TODO: kca: here we assume that this means a partial retrieve on the
        # content of a contentInstance. need a better check for that
        return rawdata, content_type
    try:
        data = serializer.load(rawdata)
        """:type : dict """
    except SCLValueError:
        # TODO: kca: here we assume that this means a partial retrieve on the
        # content of a contentInstance. need a better check for that
        # TODO: kca: theoretically this case should be handled by
        # the check above, but XML serializer is very picky
        return rawdata, content_type

    try:
        data = serializer.parse_representation(data)
        """:type : Resource"""
    except ModelTypeError:
        # TODO: kca: here we assume that ModelTypeError means we did a partial
        # retrieve. need a better check for that
        pass
    else:
        # data is a resource
        data.path = path
    return data, None

from datetime import datetime
from werkzeug.http import parse_accept_header

import openmtc_scl.api
from futile.logging import get_logger
from openmtc_etsi.exc import SCLNotAcceptable
from openmtc_etsi.serializer import get_supported_content_types, get_serializer
from openmtc_server.transportdomain.util import OpenMTCAccept

logger = get_logger(__name__)


def encode_error(error, accept=None, pretty=False):
    # TODO: optimize
    if accept:
        parsed_accept_header = parse_accept_header(accept, OpenMTCAccept)
        """:type : Accept"""
        supported = get_supported_content_types()
        accepted_type = parsed_accept_header.best_match(supported)
        if not accepted_type:
            raise SCLNotAcceptable("%s is not supported. "
                                   "Supported content types are: %s" %
                                   (accept,
                                    ', '.join(get_supported_content_types())))
    else:
        # even if no accept header was found, default-encode to json
        # TODO: use config["default_content_type"]
        accepted_type = "application/json"

    serializer = get_serializer(accepted_type)

    data = serializer.encode_error(error, pretty=pretty)
    return accepted_type, data


def encode_request_indication_payload(request_indication,
                                      target_content_type=None):
    # TODO: pretty handling

    logger.debug("Encoding request indication: %s", request_indication)

    data = request_indication.resource

    if data is None:
        return None, None

    content_type = request_indication.content_type
    if content_type:
        return content_type, data

    target_content_type = target_content_type or openmtc_scl.api.config[
        "etsi"]["default_content_type"]

    serializer = get_serializer(target_content_type)

    data = serializer.encode_values(request_indication.typename,
                                    data, filter_none=True)

    return target_content_type + "; charset=utf-8", data


def encode_result(result, accept=None, pretty=False, prefer_xml=False):
    data = result.resource

    logger.debug("Encoding result: %s (%s) - %s", result, data, accept)

    if data is None:
        return None, None

    try:
        content_type = result.content_type
    except AttributeError:
        content_type = None

    try:
        fields = result.fields if not result.content_type else None
    except AttributeError:
        fields = None

    if content_type:
        # TODO: still honor accept header here
        return content_type, data

    # TODO: optimize
    if accept:
        parsed_accept_header = parse_accept_header(accept, OpenMTCAccept)
        """:type : Accept"""
        supported = get_supported_content_types()
        accepted_type = parsed_accept_header.best_match(supported)
        if not accepted_type:
            raise SCLNotAcceptable("%s is not supported. "
                                   "Supported content types are: %s" %
                                   (accept, ', '.join(supported)))
    elif prefer_xml:
        # TODO: use config["default_content_type"]
        accepted_type = "application/xml"
    else:
        accepted_type = "application/json"

    serializer = get_serializer(accepted_type)

    data = serializer.encode(data, pretty=pretty, fields=fields)

    return accepted_type + "; charset=utf-8", data

serialize_result = encode_result


def serialize_generic_result(result, accept=None, pretty=False,
                             prefer_xml=False):
    try:
        data = result.payload
    except:
        data = None

    if data is None:
        return None, None

    try:
        content_type = result.content_type
        fields = None
    except AttributeError:
        content_type = None
        fields = result.fields

    if content_type:
        # TODO: still honor accept header here
        return content_type, data

    # TODO: optimize
    if accept:
        parsed_accept_header = parse_accept_header(accept, OpenMTCAccept)
        """:type : Accept"""
        supported = get_supported_content_types()
        accepted_type = parsed_accept_header.best_match(supported)
        if not accepted_type:
            raise SCLNotAcceptable("%s is not supported. "
                                   "Supported content types are: %s" %
                                   (accept,
                                    ', '.join(get_supported_content_types())))
    elif prefer_xml:
        # TODO: use config["default_content_type"]
        accepted_type = "application/xml"
    else:
        accepted_type = "application/json"

    serializer = get_serializer(accepted_type)

    data = serializer.encode(data, pretty=pretty, fields=fields)

    return accepted_type + "; charset=utf-8", data
"""
def iterencode_result(result, accept=None, pretty=False):
    data = result.resource

    if data is None:
        return None, None

    try:
        content_type = result.content_type
        fields = None
    except AttributeError:
        content_type = None
        fields = result.fields

    if accept is not None:
        parsed_accept_header = parse_accept_header(accept,Accept)
        # :type : Accept
        accepted_type = parsed_accept_header.best_match(["application/json", "application/xml", ])
    if content_type is None:
        if data is None:
            return None, None
        # content_type = "application/json; charset=utf-8"
        data = serializer.iterencode(data, pretty=pretty, fields=fields)
    else:
        return content_type, data
    return accepted_type+"; charset=utf-8", data
"""


def match_now_cron(cron):
    return match_time_cron(datetime.now(), cron)


def match_time_cron(time, cron):
    cron_parts = cron.split(' ')

    if len(cron_parts) < 5:
        return False

    minute, hour, day, month, weekday = cron_parts

    to_check = {
        'minute': minute,
        'hour': hour,
        'day': day,
        'month': month,
        'weekday': weekday
    }

    ranges = {
        'minute': '0-59',
        'hour': '0-23',
        'day': '1-31',
        'month': '1-12',
        'weekday': '0-6'
    }

    for c in to_check.keys():
        val = to_check[c]
        values = []

        # For patters like 0-23/2
        if val.find('/') >= 0:
            # Get the range and step
            _range, steps = val.split('/')
            steps = int(steps)

            # Now get the start and stop
            if _range == '*':
                _range = ranges[c]

            start, stop = map(int, _range.split('-'))

            for i in range(start, stop, steps):
                values.append(i)

        # For patters like : 2 or 2,5,8 or 2-23
        else:
            k = val.split(',')

            for v in k:
                if v.find('-') >= 0:
                    start, stop = map(int, v.split('-'))

                    for i in range(start, stop):
                        values.append(i)
                elif v == '*':
                    values.append('*')
                else:
                    values.append(int(v))

        if c is 'weekday':
            if time.weekday() not in values and val != '*':
                return False
        else:
            if getattr(time, c) not in values and val != '*':
                return False

    return True

from datetime import datetime as _datetime
from iso8601.iso8601 import parse_date as _parse_date
from iso8601.iso8601 import ParseError as _ParseError
from futile.collections import is_iterable as _is_iterable


def _datetime_parameter(value):
    if _is_iterable(value):
        raise ValueError("parameter specified more than once")
    if isinstance(value, _datetime):
        return value

    try:
        return _parse_date(value)
    except _ParseError as e:
        raise ValueError("'%s' is not a valid datetime value: %s" %
                         (value, e))
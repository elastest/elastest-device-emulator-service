from datetime import datetime as _datetime
from iso8601.iso8601 import parse_date as _parse_date
from iso8601.iso8601 import ParseError as _ParseError
from futile.collections import get_iterable as _get_iterable
from futile import identity as _identity
from futile.collections import is_iterable as _is_iterable


def _datetime_parameter(value):
    if _is_iterable(value):
        raise ValueError("parameter specified more than once")
    if isinstance(value, _datetime):
        return value

    try:
        return _parse_date(value)
    except _ParseError as e:
        try:
            # java.SQL.timestamp !
            return _parse_date(str(value).replace(' ','T'))
        except Exception as e:
            raise ValueError("'%s' is not a valid datetime value: %s" %
                             (value, e))

# DateTime[0..1]
ifModifiedSince = ifUnmodifiedSince = createdAfter = createdBefore = \
    _datetime_parameter

# TODO(rst): is get_iterable enough?
# String[0..unbounded]
ifNoneMatch = searchString = _get_iterable

# TODO(rst): anyURI maybe more strict
# AnyURI
attributeAccessor = _identity

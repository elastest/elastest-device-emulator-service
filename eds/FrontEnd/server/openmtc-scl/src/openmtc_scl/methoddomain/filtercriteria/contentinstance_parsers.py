from openmtc_scl.methoddomain.filtercriteria.parsers import attributeAccessor, \
    createdAfter, createdBefore, ifModifiedSince, ifNoneMatch, \
    ifUnmodifiedSince, searchString
from futile.collections import get_iterable as _get_iterable
from futile import identity as _identity
from futile.collections import is_iterable as _is_iterable


def _int_parameter(value):
    if _is_iterable(value):
        raise ValueError("parameter specified more than once")
    try:
        return int(value)
    except (ValueError, TypeError) as e:
        raise ValueError(e)


# Long[0..1]
sizeFrom = sizeUntil = _int_parameter

# String[0..unbounded]
contentType = _get_iterable

# todo check for boolean
# Boolean[0..1]
metaDataOnly = _identity

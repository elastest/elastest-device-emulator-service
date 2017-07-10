from openmtc_scl.methoddomain.filtercriteria import filters, parsers
from openmtc_scl.methoddomain.filtercriteria import contentinstance_filters
from openmtc_scl.methoddomain.filtercriteria import contentinstance_parsers
from openmtc_etsi.model import ContentInstance, FilterCriteria
from futile.logging import get_logger
from openmtc_etsi.exc import SCLSyntaxError, SCLValueError


_logger = get_logger(__name__)


def filter_criteria_match(resource, filter_criteria,
                          fail_on_missing=False):
    _filters = filters
    if isinstance(resource, ContentInstance):
        _filters = contentinstance_filters

    try:
        filter_criteria = filter_criteria.items()
    except AttributeError:
        pass

    return _filter_criteria_match(resource, filter_criteria,
                                  _filters, fail_on_missing)


def _filter_criteria_match(resource, filter_criteria,
                           filters, fail_on_missing=False):
    # _logger.debug("Matching criteria %s against %s", filter_criteria, resource)

    for criteria, value in filter_criteria:
        try:
            filter_function = getattr(filters, criteria)
        except AttributeError:
            _logger.warn("No filter '%s' available for resource of type %s",
                         criteria, type(resource).__name__)
            if fail_on_missing:
                return False
        else:
            if not filter_function(resource, value):
                #_logger.debug("filterCriteria did not match due to %s", filter_function.__name__)
                return False

    #_logger.debug("filterCriteria matched")
    return True


def filter_resources(resources, filter_criteria,
                     fail_on_missing=False, max_results=-1):
    """
        @type filter_criteria: dict
    """

    if not resources or not filter_criteria:
        return resources

    _logger.debug("Filtering %s resources: %s", len(resources),
                  filter_criteria)

    _filters = filters
    if isinstance(resources[0], ContentInstance):
        _filters = contentinstance_filters

    if isinstance(resources, dict):
        resources = resources.values()

    try:
        filter_criteria = filter_criteria.items()
    except AttributeError:
        pass

    # _logger.debug("Filtering resources %s %s %s", len(resources), type(resources), type(resources[0]))
    if max_results >= 0:
        if max_results == 0:
            return []

        done = 0
        result = []
        for r in resources:
            if _filter_criteria_match(r, filter_criteria,
                                      _filters, fail_on_missing):
                result.append(r)
                done += 1
                if done >= max_results:
                    break
    else:
        result = [r for r in resources
                  if _filter_criteria_match(r, filter_criteria,
                                            _filters, fail_on_missing)]

    _logger.debug("Filtered length: %s", len(result))
    return result


def _handle_missing(name, resource_type, fail_on_missing):
    if fail_on_missing:
        raise SCLSyntaxError(
            "Unknown filterCriteria for resource_type '%s': %s" % (
            resource_type.__name__, name, ))
    _logger.warn("Unknown filterCriteria for resource_type '%s': %s",
                 resource_type.__name__, name)


def parse_filter_criteria(filter_criteria, resource_type,
                          fail_on_missing=False):
    # TODO: don't use dicts anymore, only proper objects
    if isinstance(filter_criteria, FilterCriteria):
        filter_criteria = {k: v
                           for k, v in filter_criteria.values.items()
                           if v is not None}
    elif not isinstance(filter_criteria, dict):
        raise SCLValueError("Not a valid filterCriteria object: %s" %
                            (filter_criteria, ))

    result = {}

    _parsers = parsers

    if issubclass(resource_type, ContentInstance):
        _parsers = contentinstance_parsers

    for k, v in filter_criteria.items():
        if k.startswith("_"):
            _handle_missing(k, resource_type, fail_on_missing)
        elif v is not None:
            try:
                parser = getattr(_parsers, k)
            except AttributeError:
                _handle_missing(k, resource_type, fail_on_missing)
            else:
                try:
                    result[k] = parser(v)
                except Exception as e:
                    raise SCLSyntaxError(
                        "Illegal value for filterCriteria '%s': %s" % (k, e))
    return result


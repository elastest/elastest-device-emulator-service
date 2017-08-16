from abc import ABCMeta
from operator import attrgetter
from re import compile

from futile.logging import get_logger
from openmtc_etsi.exc import SCLNotFound, SCLBadRequest
from openmtc_etsi.model import (SclBase, ContentInstances,
                                ContentInstance, Application,
                                MembersContent, Subcontainers,
                                Parameters, MgmtObj)
from openmtc_server.util import get_regex_path_component
from openmtc_server.util.regexer import (capturing_group as c_group,
                                         not_capturing_group as nc_group,
                                         zero_plus_elem as star,
                                         zero_or_one_elem as q_mark,
                                         slash, alternative as alt)

_methods = ("retrieve", "update", "delete")

URI_BASE = "/m2m"

PATH_COMPONENT = get_regex_path_component()

MGMT_OBJ_FLEX_ATTRS = ["Enabled", "opEnable", "opDisable", "Property",
                       "Attached"]

routes = []

rd = {}


class Route(object):
    __metaclass__ = ABCMeta
    __slots__ = ("regex", "resource_types", "children", "sub_resources",
                 "attributes", "regexstr")

    def __init__(self, route, resource_types, *args, **kw):

        super(Route, self).__init__(*args, **kw)
        self.regexstr = "^" + route + "$"
        self.regex = compile(self.regexstr)
        self.resource_types = tuple(resource_types)

        collections = reduce(list.__add__,
                             map(attrgetter("collections"), resource_types))
        subresources = reduce(list.__add__,
                              map(attrgetter("subresources"), resource_types))
        attributes = reduce(list.__add__,
                            map(attrgetter("attributes"), resource_types))

        self.children = tuple(map(attrgetter("content_type"), collections) +
                              map(attrgetter("type"), subresources))

        self.attributes = [a.name for a in attributes]

    def match(self, path, method):
        result = self.regex.match(path)

        if result is not None:
            parent_types = None
            aPoc_path = None
            resource_types = self.resource_types

            try:
                partial_accessor = result.group(2)
            except IndexError:
                partial_accessor = None

            try:
                # group 3 must be the apocpath
                aPoc_path = result.group(3)
            # partial addressing
            except IndexError:
                aPoc_path = None

                # check for sub collection or child creation
            if method == 'create' and MembersContent not in resource_types:
                parent_types = resource_types

                if partial_accessor is not None:
                    raise SCLBadRequest(
                        "Cannot use partial addressing on create")
                elif resource_types[0] == ContentInstances:
                    resource_types = (ContentInstance, )
                else:
                    resource_types = self.children

            return resource_types, parent_types, result.group(
                1), partial_accessor, aPoc_path

    def __str__(self):
        return "%s -> %s (%s)" % (self.regexstr, self.resource_types,
                                  self.children)


_logger = get_logger(__name__)


# TODO: kca: more descriptive error messages
def match_route(path, method):
    _logger.debug("Matching route for %s at %s", method, path)

    for route in routes:
        result = route.match(path, method)
        if result is not None:
            _logger.debug("Route matched: %s", result)
            return result

    _logger.debug("No route found for %s.", path)
    raise SCLNotFound(path)


def build_routes(resources, pre, match_string):
    if not resources:
        return

    attribute_names = set(map(attrgetter("name"),
                              reduce(list.__add__,
                                     map(attrgetter("attributes"),
                                         resources))))
    member_names = set(map(attrgetter("name"),
                           reduce(list.__add__,
                                  map(attrgetter("__members__"), resources))))
    subresources = reduce(list.__add__,
                          map(attrgetter("subresources"), resources))

    if Subcontainers in resources:
        not_matching = nc_group(alt(member_names), negated=True)
        match_string = (star(nc_group(match_string + "/" + not_matching +
                                      PATH_COMPONENT + "/")) + match_string)

    if Parameters in resources:
        match_string = star(nc_group(match_string + "/")) + match_string

    # TODO(rst): find a better solution for this
    if MgmtObj in resources:
        attribute_names = set(list(attribute_names) + MGMT_OBJ_FLEX_ATTRS)

    base_group = c_group(URI_BASE + pre + match_string)

    partial_group = c_group(nc_group(alt(attribute_names)) +
                            star(nc_group(slash(PATH_COMPONENT))))

    if Application in resources:
        subresource_names = map(attrgetter("name"), subresources)

        apoc_group = c_group(nc_group(alt(subresource_names),
                                      negated=True) + PATH_COMPONENT +
                             star(nc_group(slash(PATH_COMPONENT))))

        attribute_additions = q_mark(nc_group(alt([
            slash(partial_group), slash(apoc_group)])))
    elif MembersContent in resources:
        member_group = c_group(PATH_COMPONENT +
                               star(nc_group(slash(PATH_COMPONENT))))
        attribute_additions = q_mark(nc_group(slash(member_group)))
    elif attribute_names:
        attribute_additions = q_mark(nc_group(slash(partial_group)))
    else:
        attribute_additions = ""

    regex_string = base_group + attribute_additions + q_mark(slash(""))

    routes.append(Route(regex_string, resources))

    assert regex_string not in rd

    rd[regex_string] = (routes[-1], resources)

    # sub resources
    for sub_res_name, sub_res_type in set(
            map(attrgetter("name", "type"), subresources)):
        if sub_res_name == 'subcontainers' and 'subcontainers' in pre:
            continue
        build_routes((sub_res_type, ), pre + match_string + "/", sub_res_name)

    if Parameters in resources:
        return

    # collections
    not_matching = nc_group(alt(member_names), negated=True)
    collections = reduce(list.__add__,
                         map(attrgetter("collections"), resources), [])
    build_routes(set(map(attrgetter("content_type"), collections)),
                 pre + match_string + "/", not_matching + PATH_COMPONENT)


build_routes((SclBase, ), "", "")
routes = tuple(routes)
del rd

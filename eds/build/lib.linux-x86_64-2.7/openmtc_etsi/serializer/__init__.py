from base64 import b64encode
from collections import Mapping

from futile.collections import OrderedDict
from futile.logging import LoggerMixin, get_logger
from openmtc_etsi.exc import SCLValueError, SCLBadRequest, OpenMTCError,\
    SCLNotAcceptable
from openmtc_etsi.model import get_etsi_type, ContentInstance
from werkzeug import parse_accept_header, Accept


class Serializer(LoggerMixin):
    compat = False

    def get_values(self, resource):
        return resource.get_values_representation()

    def get_representation(self, resource, internal=False, fields=None):
        self.logger.debug("Getting representation for %s", resource)
        try:
            representation = resource.get_values_representation(fields=fields,
                                                                internal=internal)
        except AttributeError:
            return resource

        path = resource.path
        if internal:
            representation["path"] = resource.path
        elif fields is None:
            for sr in resource.subresources:
                # TODO: Move this out of serializer
                # (and into rendering part of TD probably)
                representation[sr.name + "Reference"] = path + "/" + sr.name

        if fields is None:
            for collection_member in resource.collections:
                collection = getattr(resource, collection_member.name)

                cr = representation[collection_member.name] = {}
                if collection_member.name == "contentInstanceCollection":
                    cl = cr["contentInstance"] = [r.get_values_representation()
                                                  for r in collection]
                    if self.compat:
                        map(self._fix_contentinstance_representation, cl)
                else:
                    cr["namedReference"] = [{"$t": r.path, "id": r.name}
                                            for r in collection]

            try:
                latest = resource.latest
                oldest = resource.oldest
            except AttributeError:
                pass
            else:
                if latest is not None:
                    representation["latest"] = {"id": latest.name,
                                                "$t": latest.path}
                    representation["oldest"] = {"id": oldest.name,
                                                "$t": oldest.path}

        if self.compat and isinstance(resource, ContentInstance):
            self._fix_contentinstance_representation(representation)

        return {
            resource.typename: representation
        }

    def _fix_contentinstance_representation(self, r):
        """alters a ContentInstance representation to provide v1 <-> v2
        compatibility"""

        try:
            content = r["content"]
        except KeyError:
            return

        try:
            content["$t"] = content["binaryContent"]
            return
        except KeyError:
            pass

        try:
            content["$t"] = b64encode(content["textContent"])
        except KeyError:
            self.logger.warn("No content found in contentinstance"
                             "representation: %s", r)

    def parse_representation(self, representation):
        if not isinstance(representation, Mapping) or len(representation) != 1:
            raise ValueError("Not a valid resource representation: %s (%s)" %
                             (representation, type(representation)))

        typename, values = representation.items()[0]

        cls = get_etsi_type(typename)

        for c in cls.subresources:
            values.pop(c.name + "Reference", None)

        self.logger.debug("Parsing representation %s %s", typename, values)
        for c in cls.collections:
            try:
                collection = values[c.name]
            except KeyError:
                continue

            self.logger.debug("Parsing collection: %s", collection)

            if c.name == "contentInstanceCollection":

                content_instances = OrderedDict()
                for ci_values in collection["contentInstance"]:
                    ci = ContentInstance(ci_values["href"], **ci_values)
                    content_instances[ci_values["href"]] = ci
                values[c.name] = content_instances.values()

                if content_instances:
                    try:
                        latest = content_instances[values["latest"]["$t"]]
                        oldest = content_instances[values["oldest"]["$t"]]
                        values["latest"] = latest
                        values["oldest"] = oldest
                    except KeyError:
                        self.logger.warn("Could not find latest/oldest CIs.")
                        # hack: happened in chile; reasons unknown;
                        values["latest"] = values["latest"]["$t"]
                        values["oldest"] = values["oldest"]["$t"]
            else:
                ct = c.content_type
                values[c.name] = [ct(path=r["$t"])
                                  for r in collection["namedReference"]]

        self.logger.debug("Creating object of type %s with %s", cls, values)
        return cls(**values)

    def decode_values(self, entity):
        try:
            items = entity.items()
            if len(items) != 1:
                raise SCLValueError("Not a valid entity: %s" % (entity, ))
            return items[0]
        except (AttributeError, TypeError):
            raise SCLValueError("Not a valid entity: %s" % (entity, ))

from .xml import XMLSerializer
from .json import JsonSerializer

_factories = {"application/xml": XMLSerializer,
              "application/json": JsonSerializer,
              "text/plain": JsonSerializer}
_serializers = {}


def create_serializer(content_type):
    try:
        factory = _factories[content_type]
    except KeyError:
        raise SCLBadRequest("Unsupported content type: %s. Try one of %s" %
                            (content_type, ', '.join(_factories.keys())))
    return factory()


def get_supported_content_types():
    return _factories.keys()


def get_decoder(content_type):
    # TODO: Check if this is faster than split
    content_type, _, _ = content_type.partition(";")

    content_type = content_type.strip().lower()

    try:
        return _serializers[content_type]
    except KeyError:
        serializer = create_serializer(content_type)
        _serializers[content_type] = serializer
        return serializer
get_serializer = get_decoder


def get_encoder(accept):
    # TODO: optimize
    if accept:
        parsed_accept_header = parse_accept_header(accept, Accept)
        """:type : Accept"""
        supported = get_supported_content_types()
        accepted_type = parsed_accept_header.best_match(supported)
        if not accepted_type:
            raise SCLNotAcceptable("%s is not supported. "
                                   "Supported content types are: %s" %
                                   (accept,
                                    ', '.join(get_supported_content_types())))
    else:
        # TODO: use config["default_content_type"]
        accepted_type = "application/json"

    # TODO: optimize
    return get_serializer(accepted_type)


def register_serializer(content_type, factory):
    set_value = _factories.setdefault(content_type, factory)

    if set_value is not factory:
        raise OpenMTCError("Content type is already registered: %s" %
                           (content_type, ))

import impl
import pkgutil

logger = get_logger(__name__)

for _importer, modname, ispkg in pkgutil.iter_modules(impl.__path__):
    modname = impl.__name__ + "." + modname
    logger.debug("Found serializer module %s (is a package: %s)" %
                 (modname, ispkg))
    try:
        __import__(modname)
    except:
        logger.error("Failed to import serializer %s", modname)
        raise
    del _importer
    del modname
    del ispkg

del impl
del pkgutil
del logger


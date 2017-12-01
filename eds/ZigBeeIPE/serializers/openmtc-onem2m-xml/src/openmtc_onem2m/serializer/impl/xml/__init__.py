from base64 import b64decode, b64encode
from datetime import datetime
from enum import Enum

import pyxb.binding.basis
from futile.etree.ElementTree import QName
from openmtc_onem2m.serializer.impl.xml.binding import (childResourceRef,
                                                        listOfURIs)
from pyxb.binding.basis import STD_list, complexTypeDefinition
from pyxb.binding.content import _PluralBinding
from pyxb.exceptions_ import UnrecognizedDOMRootNodeError,\
    NonElementValidationError, SimpleFacetValueError, \
    UnrecognizedAttributeError, UnrecognizedContentError,\
    IncompleteElementContentError, SimpleTypeValueError
from pyxb.namespace import ExpandedName
from pyxb.utils.domutils import BindingDOMSupport

import binding_v1_3_0 as binding
import openmtc_onem2m.model as model
from futile import uc
from futile.etree import ElementTree as ET, tostring
from openmtc.model import ListAttribute, AnyURI, Entity, EntityAttribute, \
    StringListAttribute
from openmtc_onem2m.exc import CSESyntaxError, CSEValueError, CSEMissingValue
from openmtc_onem2m.model import get_onem2m_type, EncodingType,\
    NotificationEvent, OneM2MEntity, CSEBase, OneM2MResource
from openmtc_onem2m.serializer import register_onem2m_serializer
from openmtc_onem2m.serializer.base import OneM2MSerializer

XMLNS = "http://www.onem2m.org/xml/protocols"
# namespace_prefix = "onem2m"
namespace_prefix = "m2m"
namespace_url = "{" + XMLNS + "}"
namespace_url_len = len(namespace_url)
ET.register_namespace(namespace_prefix, XMLNS)


class OneM2MXMLSerializer(OneM2MSerializer):
    def __init__(self, type_factory=None, *args, **kw):
        if type_factory is None:
            from openmtc_onem2m.model import get_onem2m_type as type_factory
        self.get_resource_type = type_factory

    def _convert_notification_event(self, event):
        representation = event.representation
        if isinstance(representation, OneM2MEntity):
            event.representation = self.encode_resource(representation)
        return self._convert_value(event, NotificationEvent)

    def _convert_value(self, value, need_type, mapped_type=None):
        self.logger.debug("_convert_value: %s %s %s", value, need_type, mapped_type)
        if need_type is not None:
            if mapped_type is None:
                mapped_type = self._get_mapper_class(need_type.get_typename())

            values = {}
            for k, v in value.values.items():
                a = getattr(need_type, k)
                if isinstance(a, ListAttribute):
                    act = a.content_type
                    if act is AnyURI:
                        self.logger.debug("wrapping AnyURIList %s", v)
                        l = listOfURIs(reference=v)
                    else:
                        if issubclass(act, Entity):
                            mt = self._get_mapper_class(act.get_typename())
                            l = [self._convert_value(x, act, mt)
                                 for x in v]
                        elif k[-1] != "s":
                            l = v
                        else:
                            self.logger.debug("wrapping %s", v)
                            wrappercls = self._get_wrapper_class(k)
                            l = wrappercls()
                            n = str(wrappercls._ElementMap.keys()[0])
                            setattr(l, n, v)
                    values[k] = l
                elif isinstance(a, StringListAttribute):
                    act = a.content_type
                    if act is AnyURI:
                        self.logger.debug("wrapping AnyURIList %s", v)
                        l = listOfURIs(reference=v)
                    else:
                        l = [str(i) for i in v.split()]
                    values[k] = l
                elif isinstance(a, EntityAttribute):
                    if v:
                        if (a.name == "representation" and
                                a.type is OneM2MResource):
                            continue
                        values[k] = self._convert_value(v, a.type)
                else:
                    self.logger.debug("No specific handling for %s - %s with %s", k,
                                      a, getattr(a, "content_type", "<n/a/>"))
                    values[k] = v
            self.logger.debug("Creating mapper of type %s with %s",
                              mapped_type, values)
            value = mapped_type(**values)
        else:
            try:
                value = value.isoformat()
            except AttributeError:
                pass

        return value

    __enum_values = {
        "cseType": {
            "IN": 1,
            "MN": 2,
            "AEN": 3
        }
    }

    __resource_types = {
        model.AccessControlPolicy: 1,
        model.AE: 2,
        model.Container: 3,
        model.ContentInstance: 4,
        model.CSEBase: 5,
        model.Node: 15,
        model.RemoteCSE: 18,
        model.Subscription: 23
    }

    __resource_types_reversed = {v: k for k, v in __resource_types.items()}

    __resource_types[model.AEAnnc] = 2
    __resource_types[model.ContainerAnnc] = 3
    __resource_types[model.ContentInstanceAnnc] = 4

    __binding_class_map = {
        v.typeDefinition(): get_onem2m_type(k)
        for k, v in binding.__dict__.items()
        if isinstance(v, pyxb.binding.basis.element)
    }

    __wrappers = {
        "accessControlPolicyIDs": binding.acpType,
        "pointOfAccess": binding.poaList,
        "privileges": binding.setOfAcrs,
        "selfPrivileges": binding.setOfAcrs
    }

    __mappers = {
                 "AE": binding.AE,
                 "AEAnnc": binding.AEAnnc,
                 "CSEBase": binding.CSEBase,
                 "privilege": binding.accessControlRule,
                 "selfPrivilege": binding.accessControlRule,
    }

    def _get_wrapper_class(self, name):
        #valclsname = name[0].upper() + name[1:]
        valclsname = name
        try:
            return self.__wrappers[valclsname]
        except KeyError:
            return getattr(binding, valclsname)

    def _get_mapper_class(self, name):
        try:
            return self.__mappers[name]
        except KeyError:
            return getattr(binding, name[0].lower() + name[1:])

    def encode_resource(self, resource, response, pretty=False,
                        encoding="utf-8", fields=None):
        # representation = self.get_representation(resource, fields=fields)

        try:
            id_attribute = resource.id_attribute
        except AttributeError:
            xml = tostring(self._build_elementtree(resource),
                           pretty_print=pretty,
                           encoding=encoding)
            return '<?xml version="1.0" encoding="utf-8"?>' + xml

        representation = {}

        if False:
            pass
        else:
            for attr in resource.attributes:
                a_name = attr.name
                if (fields is None or a_name == id_attribute or
                        a_name in fields) and attr.accesstype is not None:
                    val = getattr(resource, "_" + a_name, None)
                    if val is None:
                        continue
                    if isinstance(attr, ListAttribute):
                        if a_name == "childResource":
                            children = [
                                childResourceRef(child.path, name=child.name,
                                                 type=self.__resource_types[
                                                     type(child)])
                                for child in resource.childResource]
                            representation["childResource"] = children
                        elif attr.content_type is AnyURI:
                            representation[a_name] = l = listOfURIs()
                            l.reference = val
                        else:
                            wrappercls = self._get_wrapper_class(a_name)

                            if issubclass(attr.content_type, Entity):
                                valcls = self._get_mapper_class(a_name[:-1])
                                vals = [self._convert_value(v,
                                                            attr.content_type,
                                                            valcls)
                                        for v in val]
                            else:
                                vals = val
                            wrapper = wrappercls()
                            if issubclass(wrappercls, STD_list):
                                wrapper[:] = vals
                            else:
                                setattr(wrapper, wrappercls._ElementMap.keys()[0].localName(), vals)
                            representation[a_name] = wrapper
                    elif isinstance(attr, StringListAttribute):
                        if attr.content_type is AnyURI:
                            representation[a_name] = l = listOfURIs()
                            l.reference = val
                        elif val:
                            representation[a_name] = ' '.join(map(str, val))
                    elif isinstance(attr, EntityAttribute):
                        if issubclass(attr.type, Entity):
                            valcls = self._get_mapper_class(attr.type.typename)
                            val = self._convert_value(val, attr.type,
                                                      valcls)
                        representation[a_name] = val
                    else:
                        if not isinstance(val, Enum):
                            try:
                                enum_values = self.__enum_values[a_name]
                            except KeyError:
                                try:
                                    val = val.strftime('%Y%m%dT%H%M%S')
                                except AttributeError:
                                    pass
                            else:
                                val = enum_values[val]

                        if a_name in ("name", "content"):
                            a_name += "_"
                        representation[a_name] = val

            content_encoding = representation.get("encoding")
            if content_encoding is not None and content_encoding != EncodingType.opaque:
                representation["content_"] = b64decode(representation["content_"])

            cls = self._get_mapper_class(type(resource).__name__)

            self.logger.debug("Creating instance of %s with %s", cls, representation)

            instance = cls()
            #representation.setdefault("expirationTime", '1970-01-01T00:00:00+00:00')

            for k, v in representation.iteritems():
                if k == 'latest' and isinstance(v, model.ContentInstance):
                    v = v.path
                setattr(instance, k.replace("-", "_"), v)

            if (type(resource) not in (model.Discovery, model.Notification) and
                    response):
                instance.resourceType = resource.resourceType
                #try:
                #    instance.resourceType = self.__resource_types[type(resource)]
                #except KeyError:
                #    pass
                instance.resourceID = resource.path
                instance.parentID = resource.parent_path or "/onem2m"

                if type(resource) == CSEBase:
                    instance.expirationTime = datetime(1970, 1, 1)
                instance.stateTag = 0

        bds = BindingDOMSupport()
        bds.declareNamespace(binding.Namespace, namespace_prefix)

        xml = instance.toDOM(
            element_name=namespace_prefix + ":" + resource.typename,
            bds=bds).toxml(encoding=encoding)
        self.logger.debug("XML representation of %s: %s", resource, xml)
        return xml

    def _build_elementtree(self, representation, id_attribute=[]):
        resource_name, representation_values = representation.items()[0]
        self.logger.debug("building elementtree from: resource_name: %s and representation_value: %s",resource_name, representation_values)

        tagname = QName(XMLNS, resource_name)
        e = ET.Element(tagname)

        if isinstance(representation_values, dict):
            for k, v in representation_values.iteritems():
                if k in id_attribute:
                    e.set(namespace_url+k, v)
                elif isinstance(v,list):
                    for i in v:
                        s = self._build_elementtree({k: i}, id_attribute=id_attribute)
                        e.append(s)
                elif isinstance(v,dict):   #check if instance is a dict: for example searchStrings :{ 'searchString': [] }
                    s = self._build_elementtree({k: v}, id_attribute=id_attribute)         #create a subelement
                    e.append(s)                                 #append the result
                elif k == "$t":
                    self.logger.debug("hve: %s", v)
                    e.text = v
                else:
                    s = ET.SubElement(e, namespace_url+k)
                    s.text = str(v)
        elif isinstance(representation_values, list):
            for i in representation_values:                     #we have a list
                if isinstance(i, str):
                    e.text = str(i)
                else:
                    s = self._build_elementtree({resource_name:i}, id_attribute=id_attribute)
                    e.append(s)
        elif isinstance(representation_values, (basestring, int, float)):
            e.text = uc(representation_values)
        elif isinstance(representation_values, datetime):
            e.text = representation_values.strftime('%Y%m%dT%H%M%S')
        else:
            self.logger.debug("building elementtree: Unknown representation value, %s", type(representation_values))
        return e

    def decode_resource_values(self, s):
        try:
            s = s.read()
        except AttributeError:
            pass

        instance = self._parse_doc(s)
        d = self._convert_instance(instance)
        self.logger.debug("Converted values: %s", d)

        encoding_type = d.get("encoding")
        if encoding_type is not None:
            if encoding_type == EncodingType.opaque:
                d["encoding"] = EncodingType.base64String
            d["content"] = b64encode(d["content"])

        try:
            resource_type = self.__binding_class_map[type(instance)]
        except KeyError:
            raise CSESyntaxError("Not a valid OneM2M type: %s", type(instance))

        return resource_type, d

    def _convert_entity(self, entity):
        if isinstance(entity, complexTypeDefinition):
            return self._convert_instance(entity)
        return entity

    def _convert_instance(self, instance):
        values = {}

        for elem in instance._ElementMap.values() + instance._AttributeMap.values():
            val = elem.value(instance)
            if val is not None:
                if isinstance(val, complexTypeDefinition):
                    val = self._convert_instance(val)
                elif isinstance(val, _PluralBinding):
                    val = map(self._convert_entity, val)
                values[elem.name().localName()] = val

        # Hack for M2MPoc
        try:
            contact_info = values["contactInfo"]
        except KeyError:
            pass
        else:
            if contact_info not in (None, ""):
                try:
                    contact_info = contact_info["contactURI"]
                except KeyError:
                    contact_info = contact_info.get("other")
            values["contactInfo"] = contact_info

        return values

    def _parse_doc(self, s):
        self.logger.debug("Reading XML input: %s", s)
        try:
            return binding.CreateFromDocument(s)
        except UnrecognizedDOMRootNodeError:
            raise CSESyntaxError("Unrecognized document root node.")
        except UnrecognizedContentError as e:
            try:
                nameinfo = e[2]._Name()
            except AttributeError:
                nameinfo = ExpandedName(e[2])
            location = "%s:%s" % (e[3].lineNumber, e[3].columnNumber)
            raise CSESyntaxError("Unrecognized element: %s at %s" %
                                 (nameinfo, location))
        except UnrecognizedAttributeError as e:
            raise CSESyntaxError("Unrecognized attribute: {%s}%s" %
                                 (e[1].uriTuple()))
        except SimpleFacetValueError as e:
            raise CSEValueError("Illegal value for %s: %s" %
                                (e[0]._ExpandedName, e[1]))
        except (NonElementValidationError, SimpleTypeValueError) as e:
            raise CSEValueError(e)
        except IncompleteElementContentError as exc:
            cfg = exc[1]
            msg = 'Incomplete content, expect %s' % (' or '.join(map(str, cfg.acceptableSymbols())))
            raise CSEMissingValue(msg)
        except Exception as e:
            self.logger.exception("Parse error")
            raise CSESyntaxError("Failed to parse XML: %r" % (e, ))

register_onem2m_serializer("application/xml", OneM2MXMLSerializer)
register_onem2m_serializer("application/vnd.onem2m-res+xml",
                           OneM2MXMLSerializer)
register_onem2m_serializer("application/vnd.onem2m-ntfy+xml",
                           OneM2MXMLSerializer)
register_onem2m_serializer("application/vnd.onem2m-attrs+xml",
                           OneM2MXMLSerializer)
"""
import logging
logger = logging.getLogger("pyxb.binding.content")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
i = binding.CSEBase()

i.resourceID = "/onem2m"
i.parentID = "/"
i.resourceType = binding.resourceType(1)
i.accessControlPolicyIDs = binding.acpType()
setattr(i, "CSE-ID", "huhu")

i.expirationTime = '1970-01-01T00:00:00+00:00'
i.creationTime = '1970-01-01T00:00:00+00:00'
i.lastModifiedTime = '1970-01-01T00:00:00+00:00'
i.resourceType = 1
i.resourceID = "/onem2m"
i.parentID = "/"
i.stateTag = 0
i.cseType = 1
i.CSE_ID = "huhu"

x = i.toDOM()
"""

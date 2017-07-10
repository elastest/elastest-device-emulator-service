from base64 import b64encode, b64decode
from datetime import datetime

from futile.etree.ElementTree import QName
from pyxb.binding.basis import complexTypeDefinition
from pyxb.binding.content import _PluralBinding
from pyxb.exceptions_ import UnrecognizedAttributeError, \
    UnrecognizedContentError, SimpleFacetValueError,\
    UnrecognizedDOMRootNodeError, NonElementValidationError,\
    IncompleteElementContentError, SimpleTypeValueError
from pyxb.namespace import ExpandedName
from pyxb.utils.domutils import BindingDOMSupport

import binding
from futile import uc
from futile.etree import ElementTree as ET, tostring
from futile.logging import DEBUG
from openmtc.model import EntityAttribute
from openmtc_etsi.exc import SCLValueError, SCLSyntaxError, SCLMissingValue
from openmtc_etsi.model import ListAttribute, Entity, \
    AnyURI, ContentInstance, MembersContent, Notify
from openmtc_etsi.response import get_status_message_safe, \
    ErrorResponseConfirmation
from openmtc_etsi.serializer import Serializer
from openmtc_etsi.serializer.xml.binding import AnyURIList, NamedReferenceCollection,\
    ReferenceToNamedResource, PermissionListType, PermissionType,\
    PermissionFlagListType, permissionHolders, PermissionHolderType, CTD_ANON,\
    ContentInstanceCollection, SearchStrings, ContentTypes, \
    ContentInstancesFilterCriteriaType

XMLNS = "http://uri.etsi.org/m2m"
namespace_prefix = "tns"
namespace_url = "{" + XMLNS + "}"
ET.register_namespace(namespace_prefix, XMLNS)


class XMLSerializer(Serializer):
    def __init__(self, type_factory=None, *args, **kw):
        if type_factory is None:
            from openmtc_etsi.model import get_etsi_type as type_factory
        self.get_resource_type = type_factory

    def _convert_value(self, value, need_type, mapped_type=None):
        if need_type is not None:
            if mapped_type is None:
                mapped_type = self._get_mapper_class(need_type.get_typename())

            print "_convert_value:", need_type, "->", mapped_type, "from", value, " - ", value.values
            values = {}
            for k, v in value.values.items():
                a = getattr(need_type, k)
                if isinstance(a, ListAttribute):
                    if a.content_type is AnyURI:
                        if isinstance(v, (tuple, list)):
                            l = AnyURIList()
                            l.reference = v
                        else:
                            l = AnyURIList()
                            l.reference = v["reference"]
                    else:
                        if issubclass(a.content_type, Entity) or k[-1] != "s":
                            l = v
                        else:
                            print k, v, a.content_type
                            wrappercls = self._get_wrapper_class(k)
                            wrapper = wrappercls()

                            if type(v) is list:
                                setattr(wrapper, k, v)
                            else:
                                l = v.values()[0]
                                setattr(wrapper, v.keys()[0], l)
                            l = wrapper
                    values[k] = l
                elif isinstance(a, EntityAttribute) and \
                        issubclass(a.type, Entity):
                    values[k] = self._convert_value(v, a.type)
                elif k == "all" and mapped_type is PermissionHolderType:
                    values[k] = CTD_ANON()
                else:
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

    __wrappers = {
        "Permissions": PermissionListType,
        "SelfPermissions": PermissionListType,
        "PermissionFlags": PermissionFlagListType,
        "HolderRefs": binding.HolderRefListType,
        "Domains": binding.DomainListType
    }

    __mappers = {
        "Permission": PermissionType,
        "SelfPermission": PermissionType,
        "PermissionHolder": PermissionHolderType,
        "FilterCriteria": ContentInstancesFilterCriteriaType,
        "M2mPoc": binding.M2MPoc,
        "M2mPocs": binding.M2MPocs
    }

    def _get_wrapper_class(self, name):
        valclsname = name[0].upper() + name[1:]
        try:
            return self.__wrappers[valclsname]
        except KeyError:
            return getattr(binding, valclsname)

    def _get_mapper_class(self, name):
        valclsname = name[0].upper() + name[1:]
        try:
            return self.__mappers[valclsname]
        except KeyError:
            return getattr(binding, valclsname)

    def _encode_contentinstance(self, r, fields=None):
        instance = binding.ContentInstance()
        instance.href = r.href
        instance.id = r.id
        if fields is None or "searchStrings" in fields:
            instance.searchStrings = SearchStrings(searchString=r.searchStrings)
        if fields is None or "creationTime" in fields:
            instance.creationTime = r.creationTime
        if fields is None or "contentTypes" in fields:
            instance.contentTypes = ContentTypes(contentType=r.contentTypes)
        if fields is None or "lastModifiedTime" in fields:
            instance.lastModifiedTime = r.lastModifiedTime
        if fields is None or "content" in fields:
            content_elem = binding.Content(contentType=r.content.contentType)
            content = r.content
            if content.binaryContent:
                content_elem.binaryContent = b64decode(content.binaryContent)
            else:
                content_elem.textContent = content.textContent
            instance.content_ = content_elem
        if fields is None or "contentSize" in fields:
            instance.contentSize = r.contentSize
        return instance

    def _encode_memberscontent(self, resource, pretty, encoding):
        cls = binding.membersContentResponses.typeDefinition()
        instance = cls()
        statuscls = instance._ElementMap.values()[0].elementBinding().typeDefinition()
        stati = []
        for response in resource.membersContentResponses:
            status = statuscls()
            status.id = response.id
            status.lastModifiedTime = response.lastModifiedTime
            status.statusCode = response.status
            try:
                status.resourceURI = response.resourceURI
            except AttributeError:
                # Weirdly enough and contrary to what is stated in table 11.35 in TS102.921, resourceURI is not optional as per XSD
                status.resourceURI = response.id

            try:
                body = response.errorInfo
            except AttributeError:
                try:
                    body = response.resource
                except AttributeError:
                    pass
                else:
                    status.resultBody = b64encode(self.encode(body, pretty,
                                                              encoding=encoding))
            else:
                status.resultBody = b64encode(body)

            stati.append(status)
        instance.status = stati
        return instance

    def _encode_notify(self, resource, pretty, encoding):
        instance = binding.Notify(
            statusCode=resource.statusCode,
            subscriptionReference=resource.subscriptionReference,
            requestingEntity=resource.requestingEntity,
            contact=resource.contact
        )

        if resource.timeoutReason:
            instance.timeoutReason = resource.timeoutReason
        else:
            content_type = resource.representation.get("contentType")
            if content_type:
                payload = resource.representation["$t"]
            else:
                content_type = "application/xml"
                payload = resource.representation["$t"]
                if isinstance(payload, ErrorResponseConfirmation):
                    payload = self.encode_error(payload, pretty, encoding)
                else:
                    payload = self.encode(payload, pretty, encoding)

            instance.representation = binding.base64Binary(
                payload,
                contentType=content_type
            )
        return instance

    def encode(self, resource, pretty=False, encoding="utf-8", fields=None,
               attributes_only=False):
        # representation = self.get_representation(resource, fields=fields)

        try:
            id_attribute = resource.id_attribute
        except AttributeError:
            xml = tostring(self._build_elementtree(resource),
                           pretty_print=pretty,
                           encoding=encoding)
            return '<?xml version="1.0" encoding="utf-8"?>' + xml

        representation = {}

        if isinstance(resource, ContentInstance):
            instance = self._encode_contentinstance(resource, fields)
        elif isinstance(resource, MembersContent):
            instance = self._encode_memberscontent(resource, pretty, encoding)
        elif isinstance(resource, Notify):
            instance = self._encode_notify(resource, pretty, encoding)
        else:
            for attr in resource.attributes:
                a_name = attr.name
                if (fields is None or a_name == id_attribute or a_name in fields) \
                        and attr.accesstype is not None:
                    val = getattr(resource, "_" + a_name, None)
                    if val is None:
                        continue
                    if isinstance(attr, ListAttribute):
                        if attr.content_type is AnyURI:
                            representation[a_name] = l = AnyURIList()
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
                            setattr(wrapper, wrappercls._ElementMap.keys()[0].localName(), vals)
                            representation[a_name] = wrapper
                    elif isinstance(attr, EntityAttribute):
                        valcls = self._get_mapper_class(
                            attr.type.get_typename()
                        )
                        val = self._convert_value(val, attr.type,
                                                  valcls)
                        representation[a_name] = val
                    else:
                        try:
                            val = val.isoformat()
                        except AttributeError:
                            pass
                        representation[a_name] = val

            if fields is None and not attributes_only:
                path = resource.path
                for sr in resource.subresources:
                    representation[sr.name + "Reference"] = path + "/" + sr.name

                for collection_member in resource.collections:
                    collection = getattr(resource, collection_member.name)

                    if collection_member.name == "contentInstanceCollection":
                        cr = ContentInstanceCollection()
                        instances = map(self._encode_contentinstance, collection)
                        """
                        for r in collection:
                            ci = binding.ContentInstance()
                            ci.searchStrings = SearchStrings(searchString=r.searchStrings)
                            ci.creationTime = r.creationTime
                            ci.href = r.href
                            ci.contentTypes = ContentTypes(contentType=r.contentTypes)
                            ci.lastModifiedTime = r.lastModifiedTime
                            ci.content_ = binding.Content(r.content["$t"],
                                                          contentType=r.content["contentType"])
                            ci.id = r.id
                            ci.contentSize = r.contentSize
                            instances.append(ci)
                        """
                        cr.contentInstance = instances
                    else:
                        cr = NamedReferenceCollection()
                        references = []
                        for item in collection:
                            r = ReferenceToNamedResource(item.path)
                            r.id = item.name
                            references.append(r)
                        cr.namedReference = references
                    representation[collection_member.name] = cr

                try:
                    latest = resource.latest
                    oldest = resource.oldest
                except AttributeError:
                    pass
                else:
                    if latest is not None:
                        representation["latest"] = ReferenceToNamedResource(latest.path, id=latest.name)
                        representation["oldest"] = ReferenceToNamedResource(oldest.path, id=oldest.name)

            cls = self._get_mapper_class(type(resource).__name__)

            self.logger.debug("Creating instance of %s with %s", cls, representation)

            instance = cls()

            for k, v in representation.iteritems():
                setattr(instance, k, v)

            try:
                flex_values = resource.flex_values
            except AttributeError:
                pass
            else:
                # FIXME: find out how to set these
                for k, v in flex_values.items():
                    self.logger.debug("Set flex: %s - %s", k, v)

        bds = BindingDOMSupport()
        bds.declareNamespace(binding.Namespace, namespace_prefix)

        return instance.toDOM(element_name=namespace_prefix + ":" + resource.typename, bds=bds) \
            .toxml(encoding=encoding)

    def encode_error(self, error, pretty=False, encoding="utf-8"):
        try:
            statuscode = error.statusCode
        except AttributeError:
            status = "STATUS_INTERNAL_SERVER_ERROR"
        else:
            _, status = get_status_message_safe(statuscode)

        return binding.ErrorInfo(
            statusCode=status, additionalInfo=uc(error)
        ).toDOM(element_name="ns1:errorInfo").toxml(encoding=encoding)

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
                    #if k == "searchStrings":
                    #    v = {'searchString': ["XML serializer test searchstring", "this is just a test"]}
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
                if isinstance(i,str):
                    e.text = str(i)
                else:
                    s = self._build_elementtree({resource_name:i}, id_attribute=id_attribute)
                    e.append(s)
        elif isinstance(representation_values, (basestring, int, float)):
            e.text = uc(representation_values)
        elif isinstance(representation_values, datetime):
            e.text = representation_values.isoformat()
        else:
            self.logger.debug("building elementtree: Unknown representation value, %s", type(representation_values))
        return e

    def iterencode(self, resource, pretty=False):
        return [self.encode(resource, pretty), ]

    def encode_values(self, typename, values, filter_none=False, pretty=False,
                      encoding="utf-8"):
        if isinstance(values, str): # HACK retargeted update?
            return values

        # UGH, but works
        resource = self.parse_representation({typename: values})
        return self.encode(resource, pretty, encoding, attributes_only=True)

    """
    def encode_values(self, typename, values, filter_none=False):
        self.logger.debug("hve_encode_values")

        if filter_none:
            values = {k: v for k, v in values.items() if v is not None}
        try:
            status_code = values["statusCode"]
        except KeyError:
            pass
        except TypeError as e:  # HACK retargeted update?
            if isinstance(values, str):
                self.logger.debug("error encoding values: %s", e)
                return values
            else:
                raise
        else:
            if not filter_none:
                values = values.copy()
            values["statusCode"] = get_status_message(status_code)
        # return self._build_elementtree({typename: values})
        return ET.tostring(self._build_elementtree({typename: values}))
    """

    if Serializer.get_class_logger().isEnabledFor(DEBUG):
        def decode(self, s):
            try:
                s = s.read()
            except AttributeError:
                pass
            return self.decode_string(s)
    else:
        def decode(self, s):
            entity = self.load(s)
            return self.decode_values(entity)
    decode_resource_values = decode

    def decode_string(self, s):
        self.logger.debug("Reading XML input: %s", s)
        entity = self.load_string(s)
        return self.decode_values(entity)

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
                    if elem.name().localName() == "representation":
                        val = {"contentType": val.contentType, "$t": b64encode(val.value())}
                    else:
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
            raise SCLSyntaxError("Unrecognized document root node.")
        except UnrecognizedContentError as e:
            try:
                nameinfo = e[2]._Name()
            except AttributeError:
                nameinfo = ExpandedName(e[2])
            location = "%s:%s" % (e[3].lineNumber, e[3].columnNumber)
            raise SCLSyntaxError("Unrecognized element: %s at %s" %
                                 (nameinfo, location))
        except UnrecognizedAttributeError as e:
            raise SCLSyntaxError("Unrecognized attribute: {%s}%s" %
                                 (e[1].uriTuple()))
        except SimpleFacetValueError as e:
            raise SCLValueError("Illegal value for %s: %s" %
                                (e[0]._ExpandedName, e[1]))
        except (NonElementValidationError, SimpleTypeValueError) as e:
            raise SCLValueError(e)
        except IncompleteElementContentError as exc:
            cfg = exc[1]
            msg = 'Incomplete content, expect %s' % (' or '.join(map(str, cfg.acceptableSymbols())))
            raise SCLMissingValue(msg)
        except Exception as e:
            self.logger.exception("Parse error")
            raise SCLSyntaxError("Failed to parse XML: %r" % (e, ))

    def load_string(self, s):
        instance = self._parse_doc(s)
        d = self._convert_instance(instance)
        self.logger.debug("Converted values: %s", d)

        typename = type(instance).__name__

        if typename == "M2MPoc":
            typename = "m2mPoc"
        elif typename == "M2MPocs":
            typename = "m2mPocs"
        else:
            typename = typename[0].lower() + typename[1:]

            if typename == "contentInstance":
                try:
                    binary_content = d["content"]["binaryContent"]
                except KeyError:
                    pass
                else:
                    d["content"]["binaryContent"] = b64encode(binary_content)

        return {
            typename: d
        }

    def load(self, s):
        try:
            s = s.read()
        except AttributeError:
            pass
        return self.load_string(s)

    def load_pa_content(self, s):
        try:
            s = s.read()
        except AttributeError:
            pass

        # TODO: can we just use load_string here?
        instance = self._parse_doc(s)
        d = self._convert_entity(instance)
        self.logger.debug("Converted values: %s", d)

        typename = type(instance).__name__
        typename = typename[0].lower() + typename[1:]

        return {
            typename: d
        }

    """
    if Serializer.get_class_logger().isEnabledFor(DEBUG):
        def load(self, s):
            try:
                s = s.read()
            except AttributeError:
                pass
            return self.load_string(s)
    else:
        def load(self, s):
            if not hasattr(s, "read"):
                return self.load_string(s)
            if not hasattr(s, "seek"):
                return self.load_string(s.read())

            try:
                # FIXME: does this work? s is not a string or sequence, but a buffer
                return etree_to_dict(ET.parse(s).getroot())
            except (ValueError, XMLSyntaxError) as e:
                s.seek(0)
                raise SCLValueError("Invalid XML input: " + str(e))
    """

# ./_xmlmime.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:fea1cf329f0f855e4df4fec1b9d504f220530c48
# Generated 2014-09-01 15:23:39.635106 by PyXB version 1.2.3
# Namespace http://www.w3.org/2005/05/xmlmime [xmlns:xmlmime]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier(
    'urn:uuid:2f2a852e-31db-11e4-8b7f-3c970e5f194d')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/05/xmlmime',
                                           create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])


def CreateFromDocument(xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace,
                                           location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance


def CreateFromDOM(node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        u'http://www.w3.org/2005/05/xmlmime.xsd', 24, 4)
    _Documentation = None


STD_ANON._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(3L))
STD_ANON._InitializeFacetMap(STD_ANON._CF_minLength)

# Complex type {http://www.w3.org/2005/05/xmlmime}base64Binary with content type SIMPLE
class base64Binary(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2005/05/xmlmime}base64Binary with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.base64Binary
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'base64Binary')
    _XSDLocation = pyxb.utils.utility.Location(
        u'http://www.w3.org/2005/05/xmlmime.xsd', 33, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.base64Binary

    # Attribute {http://www.w3.org/2005/05/xmlmime}contentType uses Python identifier contentType
    __contentType = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'contentType'), 'contentType',
        '__httpwww_w3_org200505xmlmime_base64Binary_httpwww_w3_org200505xmlmimecontentType',
        STD_ANON)
    __contentType._DeclarationLocation = pyxb.utils.utility.Location(
        u'http://www.w3.org/2005/05/xmlmime.xsd', 23, 2)
    __contentType._UseLocation = pyxb.utils.utility.Location(
        u'http://www.w3.org/2005/05/xmlmime.xsd', 36, 12)

    contentType = property(__contentType.value, __contentType.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __contentType.name(): __contentType
    })


Namespace.addCategoryObject('typeBinding', u'base64Binary', base64Binary)


# Complex type {http://www.w3.org/2005/05/xmlmime}hexBinary with content type SIMPLE
class hexBinary(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2005/05/xmlmime}hexBinary with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.hexBinary
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hexBinary')
    _XSDLocation = pyxb.utils.utility.Location(
        u'http://www.w3.org/2005/05/xmlmime.xsd', 41, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.hexBinary

    # Attribute {http://www.w3.org/2005/05/xmlmime}contentType uses Python identifier contentType
    __contentType = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'contentType'), 'contentType',
        '__httpwww_w3_org200505xmlmime_hexBinary_httpwww_w3_org200505xmlmimecontentType',
        STD_ANON)
    __contentType._DeclarationLocation = pyxb.utils.utility.Location(
        u'http://www.w3.org/2005/05/xmlmime.xsd', 23, 2)
    __contentType._UseLocation = pyxb.utils.utility.Location(
        u'http://www.w3.org/2005/05/xmlmime.xsd', 44, 12)

    contentType = property(__contentType.value, __contentType.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __contentType.name(): __contentType
    })


Namespace.addCategoryObject('typeBinding', u'hexBinary', hexBinary)


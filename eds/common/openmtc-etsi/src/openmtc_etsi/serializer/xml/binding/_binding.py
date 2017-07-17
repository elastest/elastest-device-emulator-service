# ./binding.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e335df22d147f2d1c4eacc090a44cf921201a604
# Generated 2014-09-01 15:23:39.635580 by PyXB version 1.2.3
# Namespace http://uri.etsi.org/m2m

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import pyxb.utils.utility
import pyxb.utils.domutils

import pyio


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
from openmtc_etsi.serializer.xml.binding import \
    _xmlmime as _ImportedBinding__xmlmime

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://uri.etsi.org/m2m',
                                           create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_xmlmime = _ImportedBinding__xmlmime.Namespace
_Namespace_xmlmime.configureCategories(['typeBinding', 'elementBinding'])


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
    saxer.parse(pyio.BytesIO(xmld))
    instance = handler.rootObject()
    return instance


def CreateFromDOM(node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://uri.etsi.org/m2m}PermissionFlagType
class PermissionFlagType(pyxb.binding.datatypes.string,
                         pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'PermissionFlagType')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        85, 4)
    _Documentation = None


PermissionFlagType._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=PermissionFlagType, enum_prefix=None)
PermissionFlagType.READ = PermissionFlagType._CF_enumeration.addEnumeration(
    unicode_value=u'READ', tag=u'READ')
PermissionFlagType.WRITE = PermissionFlagType._CF_enumeration.addEnumeration(
    unicode_value=u'WRITE', tag=u'WRITE')
PermissionFlagType.DISCOVER = PermissionFlagType._CF_enumeration.addEnumeration(
    unicode_value=u'DISCOVER', tag=u'DISCOVER')
PermissionFlagType.DELETE = PermissionFlagType._CF_enumeration.addEnumeration(
    unicode_value=u'DELETE', tag=u'DELETE')
PermissionFlagType.CREATE = PermissionFlagType._CF_enumeration.addEnumeration(
    unicode_value=u'CREATE', tag=u'CREATE')
PermissionFlagType._InitializeFacetMap(PermissionFlagType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PermissionFlagType',
                            PermissionFlagType)

# Atomic simple type: {http://uri.etsi.org/m2m}ReferencePoint
class ReferencePoint(pyxb.binding.datatypes.string,
                     pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ReferencePoint')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
        39, 4)
    _Documentation = None


ReferencePoint._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=ReferencePoint, enum_prefix=None)
ReferencePoint.MIA_REFERENCE_POINT = ReferencePoint._CF_enumeration.addEnumeration(
    unicode_value=u'MIA_REFERENCE_POINT', tag=u'MIA_REFERENCE_POINT')
ReferencePoint.MID_REFERENCE_POINT = ReferencePoint._CF_enumeration.addEnumeration(
    unicode_value=u'MID_REFERENCE_POINT', tag=u'MID_REFERENCE_POINT')
ReferencePoint.DIA_REFERENCE_POINT = ReferencePoint._CF_enumeration.addEnumeration(
    unicode_value=u'DIA_REFERENCE_POINT', tag=u'DIA_REFERENCE_POINT')
ReferencePoint._InitializeFacetMap(ReferencePoint._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ReferencePoint', ReferencePoint)

# Atomic simple type: {http://uri.etsi.org/m2m}OnlineStatus
class OnlineStatus(pyxb.binding.datatypes.string,
                   pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'OnlineStatus')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 128,
        4)
    _Documentation = None


OnlineStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=OnlineStatus, enum_prefix=None)
OnlineStatus.ONLINE = OnlineStatus._CF_enumeration.addEnumeration(
    unicode_value=u'ONLINE', tag=u'ONLINE')
OnlineStatus.OFFLINE = OnlineStatus._CF_enumeration.addEnumeration(
    unicode_value=u'OFFLINE', tag=u'OFFLINE')
OnlineStatus.NOT_REACHABLE = OnlineStatus._CF_enumeration.addEnumeration(
    unicode_value=u'NOT_REACHABLE', tag=u'NOT_REACHABLE')
OnlineStatus._InitializeFacetMap(OnlineStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'OnlineStatus', OnlineStatus)

# Atomic simple type: {http://uri.etsi.org/m2m}ChannelType
class ChannelType(pyxb.binding.datatypes.string,
                  pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ChannelType')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 140,
        4)
    _Documentation = None


ChannelType._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=ChannelType, enum_prefix=None)
ChannelType.LONG_POLLING = ChannelType._CF_enumeration.addEnumeration(
    unicode_value=u'LONG_POLLING', tag=u'LONG_POLLING')
ChannelType._InitializeFacetMap(ChannelType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ChannelType', ChannelType)

# Atomic simple type: {http://uri.etsi.org/m2m}RcatType
class RcatType(pyxb.binding.datatypes.string,
               pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RcatType')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 164,
        4)
    _Documentation = None


RcatType._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=RcatType, enum_prefix=None)
RcatType.RCAT_0 = RcatType._CF_enumeration.addEnumeration(
    unicode_value=u'RCAT_0', tag=u'RCAT_0')
RcatType.RCAT_1 = RcatType._CF_enumeration.addEnumeration(
    unicode_value=u'RCAT_1', tag=u'RCAT_1')
RcatType.RCAT_2 = RcatType._CF_enumeration.addEnumeration(
    unicode_value=u'RCAT_2', tag=u'RCAT_2')
RcatType.RCAT_3 = RcatType._CF_enumeration.addEnumeration(
    unicode_value=u'RCAT_3', tag=u'RCAT_3')
RcatType.RCAT_4 = RcatType._CF_enumeration.addEnumeration(
    unicode_value=u'RCAT_4', tag=u'RCAT_4')
RcatType.RCAT_5 = RcatType._CF_enumeration.addEnumeration(
    unicode_value=u'RCAT_5', tag=u'RCAT_5')
RcatType.RCAT_6 = RcatType._CF_enumeration.addEnumeration(
    unicode_value=u'RCAT_6', tag=u'RCAT_6')
RcatType.RCAT_7 = RcatType._CF_enumeration.addEnumeration(
    unicode_value=u'RCAT_7', tag=u'RCAT_7')
RcatType._InitializeFacetMap(RcatType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'RcatType', RcatType)

# Atomic simple type: {http://uri.etsi.org/m2m}StatusCode
class StatusCode(pyxb.binding.datatypes.string,
                 pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'StatusCode')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 187,
        4)
    _Documentation = None


StatusCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=StatusCode, enum_prefix=None)
StatusCode.STATUS_OK = StatusCode._CF_enumeration.addEnumeration(
    unicode_value=u'STATUS_OK', tag=u'STATUS_OK')
StatusCode.STATUS_ACCEPTED = StatusCode._CF_enumeration.addEnumeration(
    unicode_value=u'STATUS_ACCEPTED', tag=u'STATUS_ACCEPTED')
StatusCode.STATUS_BAD_REQUEST = StatusCode._CF_enumeration.addEnumeration(
    unicode_value=u'STATUS_BAD_REQUEST', tag=u'STATUS_BAD_REQUEST')
StatusCode.STATUS_PERMISSION_DENIED = StatusCode._CF_enumeration.addEnumeration(
    unicode_value=u'STATUS_PERMISSION_DENIED', tag=u'STATUS_PERMISSION_DENIED')
StatusCode.STATUS_FORBIDDEN = StatusCode._CF_enumeration.addEnumeration(
    unicode_value=u'STATUS_FORBIDDEN', tag=u'STATUS_FORBIDDEN')
StatusCode.STATUS_NOT_FOUND = StatusCode._CF_enumeration.addEnumeration(
    unicode_value=u'STATUS_NOT_FOUND', tag=u'STATUS_NOT_FOUND')
StatusCode.STATUS_METHOD_NOT_ALLOWED = StatusCode._CF_enumeration.addEnumeration(
    unicode_value=u'STATUS_METHOD_NOT_ALLOWED',
    tag=u'STATUS_METHOD_NOT_ALLOWED')
StatusCode.STATUS_NOT_ACCEPTABLE = StatusCode._CF_enumeration.addEnumeration(
    unicode_value=u'STATUS_NOT_ACCEPTABLE', tag=u'STATUS_NOT_ACCEPTABLE')
StatusCode.STATUS_REQUEST_TIMEOUT = StatusCode._CF_enumeration.addEnumeration(
    unicode_value=u'STATUS_REQUEST_TIMEOUT', tag=u'STATUS_REQUEST_TIMEOUT')
StatusCode.STATUS_CONFLICT = StatusCode._CF_enumeration.addEnumeration(
    unicode_value=u'STATUS_CONFLICT', tag=u'STATUS_CONFLICT')
StatusCode.STATUS_UNSUPPORTED_MEDIA_TYPE = StatusCode._CF_enumeration.addEnumeration(
    unicode_value=u'STATUS_UNSUPPORTED_MEDIA_TYPE',
    tag=u'STATUS_UNSUPPORTED_MEDIA_TYPE')
StatusCode.STATUS_INTERNAL_SERVER_ERROR = StatusCode._CF_enumeration.addEnumeration(
    unicode_value=u'STATUS_INTERNAL_SERVER_ERROR',
    tag=u'STATUS_INTERNAL_SERVER_ERROR')
StatusCode.STATUS_NOT_IMPLEMENTED = StatusCode._CF_enumeration.addEnumeration(
    unicode_value=u'STATUS_NOT_IMPLEMENTED', tag=u'STATUS_NOT_IMPLEMENTED')
StatusCode.STATUS_BAD_GATEWAY = StatusCode._CF_enumeration.addEnumeration(
    unicode_value=u'STATUS_BAD_GATEWAY', tag=u'STATUS_BAD_GATEWAY')
StatusCode.STATUS_SERVICE_UNAVAILABLE = StatusCode._CF_enumeration.addEnumeration(
    unicode_value=u'STATUS_SERVICE_UNAVAILABLE',
    tag=u'STATUS_SERVICE_UNAVAILABLE')
StatusCode.STATUS_GATEWAY_TIMEOUT = StatusCode._CF_enumeration.addEnumeration(
    unicode_value=u'STATUS_GATEWAY_TIMEOUT', tag=u'STATUS_GATEWAY_TIMEOUT')
StatusCode.STATUS_DELETED = StatusCode._CF_enumeration.addEnumeration(
    unicode_value=u'STATUS_DELETED', tag=u'STATUS_DELETED')
StatusCode.STATUS_EXPIRED = StatusCode._CF_enumeration.addEnumeration(
    unicode_value=u'STATUS_EXPIRED', tag=u'STATUS_EXPIRED')
StatusCode._InitializeFacetMap(StatusCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'StatusCode', StatusCode)

# Atomic simple type: {http://uri.etsi.org/m2m}APocHandling
class APocHandling(pyxb.binding.datatypes.string,
                   pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'APocHandling')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 212,
        4)
    _Documentation = None


APocHandling._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=APocHandling, enum_prefix=None)
APocHandling.SHALLOW = APocHandling._CF_enumeration.addEnumeration(
    unicode_value=u'SHALLOW', tag=u'SHALLOW')
APocHandling.DEEP = APocHandling._CF_enumeration.addEnumeration(
    unicode_value=u'DEEP', tag=u'DEEP')
APocHandling._InitializeFacetMap(APocHandling._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'APocHandling', APocHandling)

# Atomic simple type: [anonymous]
class STD_ANON(pyxb.binding.datatypes.short):
    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 28,
        16)
    _Documentation = None


STD_ANON._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(
    value_datatype=STD_ANON, value=pyxb.binding.datatypes.short(100))
STD_ANON._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(
    value_datatype=STD_ANON, value=pyxb.binding.datatypes.short(0))
STD_ANON._InitializeFacetMap(STD_ANON._CF_maxInclusive,
                             STD_ANON._CF_minInclusive)

# Atomic simple type: {http://uri.etsi.org/m2m}MemorySize
class MemorySize(pyxb.binding.datatypes.NMTOKEN):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MemorySize')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 39,
        4)
    _Documentation = None


MemorySize._CF_pattern = pyxb.binding.facets.CF_pattern()
MemorySize._CF_pattern.addPattern(pattern=u'[0-9]{1,15}[BKMGT]')
MemorySize._InitializeFacetMap(MemorySize._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'MemorySize', MemorySize)

# Atomic simple type: {http://uri.etsi.org/m2m}FinalStatus
class FinalStatus(pyxb.binding.datatypes.string,
                  pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'FinalStatus')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 46,
        4)
    _Documentation = None


FinalStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=FinalStatus, enum_prefix=None)
FinalStatus.SUCCESS = FinalStatus._CF_enumeration.addEnumeration(
    unicode_value=u'SUCCESS', tag=u'SUCCESS')
FinalStatus.FAILURE = FinalStatus._CF_enumeration.addEnumeration(
    unicode_value=u'FAILURE', tag=u'FAILURE')
FinalStatus._InitializeFacetMap(FinalStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'FinalStatus', FinalStatus)

# Atomic simple type: {http://uri.etsi.org/m2m}swVersion
class swVersion(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'swVersion')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 59,
        4)
    _Documentation = None


swVersion._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(32L))
swVersion._InitializeFacetMap(swVersion._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'swVersion', swVersion)

# Atomic simple type: [anonymous]
class STD_ANON_(pyxb.binding.datatypes.hexBinary):
    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        7, 8)
    _Documentation = None


STD_ANON_._CF_length = pyxb.binding.facets.CF_length(
    value=pyxb.binding.datatypes.nonNegativeInteger(16L))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_2(pyxb.binding.datatypes.hexBinary):
    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        21, 8)
    _Documentation = None


STD_ANON_2._CF_length = pyxb.binding.facets.CF_length(
    value=pyxb.binding.datatypes.nonNegativeInteger(40L))
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_3(pyxb.binding.datatypes.hexBinary):
    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        33, 8)
    _Documentation = None


STD_ANON_3._CF_length = pyxb.binding.facets.CF_length(
    value=pyxb.binding.datatypes.nonNegativeInteger(2L))
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_length)

# Atomic simple type: [anonymous]
class STD_ANON_4(pyxb.binding.datatypes.hexBinary):
    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        41, 8)
    _Documentation = None


STD_ANON_4._CF_length = pyxb.binding.facets.CF_length(
    value=pyxb.binding.datatypes.nonNegativeInteger(9L))
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_length)

# Atomic simple type: {http://uri.etsi.org/m2m}AreaNwkStatus
class AreaNwkStatus(pyxb.binding.datatypes.string,
                    pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AreaNwkStatus')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
        29, 4)
    _Documentation = None


AreaNwkStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=AreaNwkStatus, enum_prefix=None)
AreaNwkStatus.ASLEEP = AreaNwkStatus._CF_enumeration.addEnumeration(
    unicode_value=u'ASLEEP', tag=u'ASLEEP')
AreaNwkStatus.AWAKE = AreaNwkStatus._CF_enumeration.addEnumeration(
    unicode_value=u'AWAKE', tag=u'AWAKE')
AreaNwkStatus._InitializeFacetMap(AreaNwkStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'AreaNwkStatus', AreaNwkStatus)

# Atomic simple type: {http://uri.etsi.org/m2m}AreaNwkType
class AreaNwkType(pyxb.binding.datatypes.string,
                  pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AreaNwkType')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInstance.xsd',
        25, 4)
    _Documentation = None


AreaNwkType._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=AreaNwkType, enum_prefix=None)
AreaNwkType.n6LOWPAN = AreaNwkType._CF_enumeration.addEnumeration(
    unicode_value=u'6LOWPAN', tag=u'n6LOWPAN')
AreaNwkType.n6LOWPAN_BLUETOOTH = AreaNwkType._CF_enumeration.addEnumeration(
    unicode_value=u'6LOWPAN-BLUETOOTH', tag=u'n6LOWPAN_BLUETOOTH')
AreaNwkType.n6LOWPAN_WIFI = AreaNwkType._CF_enumeration.addEnumeration(
    unicode_value=u'6LOWPAN-WIFI', tag=u'n6LOWPAN_WIFI')
AreaNwkType.n6LOWPAN_PLC = AreaNwkType._CF_enumeration.addEnumeration(
    unicode_value=u'6LOWPAN-PLC', tag=u'n6LOWPAN_PLC')
AreaNwkType.IPV4_WPAN = AreaNwkType._CF_enumeration.addEnumeration(
    unicode_value=u'IPV4-WPAN', tag=u'IPV4_WPAN')
AreaNwkType.IPV4_BLUETOOTH = AreaNwkType._CF_enumeration.addEnumeration(
    unicode_value=u'IPV4-BLUETOOTH', tag=u'IPV4_BLUETOOTH')
AreaNwkType.IPV4_WIFI = AreaNwkType._CF_enumeration.addEnumeration(
    unicode_value=u'IPV4-WIFI', tag=u'IPV4_WIFI')
AreaNwkType.IPV4_PLC = AreaNwkType._CF_enumeration.addEnumeration(
    unicode_value=u'IPV4-PLC', tag=u'IPV4_PLC')
AreaNwkType.ZIGBEE = AreaNwkType._CF_enumeration.addEnumeration(
    unicode_value=u'ZIGBEE', tag=u'ZIGBEE')
AreaNwkType._InitializeFacetMap(AreaNwkType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'AreaNwkType', AreaNwkType)

# Atomic simple type: {http://uri.etsi.org/m2m}BatteryLevel
class BatteryLevel(pyxb.binding.datatypes.long):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BatteryLevel')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiBatteryInstance.xsd',
        28, 4)
    _Documentation = None


BatteryLevel._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(
    value_datatype=BatteryLevel, value=pyxb.binding.datatypes.long(100L))
BatteryLevel._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(
    value_datatype=BatteryLevel, value=pyxb.binding.datatypes.long(0L))
BatteryLevel._InitializeFacetMap(BatteryLevel._CF_maxInclusive,
                                 BatteryLevel._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'BatteryLevel', BatteryLevel)

# Atomic simple type: {http://uri.etsi.org/m2m}BatteryStatus
class BatteryStatus(pyxb.binding.datatypes.string,
                    pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BatteryStatus')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiBatteryInstance.xsd',
        43, 4)
    _Documentation = None


BatteryStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=BatteryStatus, enum_prefix=None)
BatteryStatus.NORMAL = BatteryStatus._CF_enumeration.addEnumeration(
    unicode_value=u'NORMAL', tag=u'NORMAL')
BatteryStatus.CHARGING = BatteryStatus._CF_enumeration.addEnumeration(
    unicode_value=u'CHARGING', tag=u'CHARGING')
BatteryStatus.CHARGE_COMPLETE = BatteryStatus._CF_enumeration.addEnumeration(
    unicode_value=u'CHARGE_COMPLETE', tag=u'CHARGE_COMPLETE')
BatteryStatus.DAMAGED = BatteryStatus._CF_enumeration.addEnumeration(
    unicode_value=u'DAMAGED', tag=u'DAMAGED')
BatteryStatus.LOW_BATTERY = BatteryStatus._CF_enumeration.addEnumeration(
    unicode_value=u'LOW_BATTERY', tag=u'LOW_BATTERY')
BatteryStatus.NOT_INSTALLED = BatteryStatus._CF_enumeration.addEnumeration(
    unicode_value=u'NOT_INSTALLED', tag=u'NOT_INSTALLED')
BatteryStatus.UNKNOWN = BatteryStatus._CF_enumeration.addEnumeration(
    unicode_value=u'UNKNOWN', tag=u'UNKNOWN')
BatteryStatus._InitializeFacetMap(BatteryStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'BatteryStatus', BatteryStatus)

# Atomic simple type: {http://uri.etsi.org/m2m}TFboolean
class TFboolean(pyxb.binding.datatypes.boolean):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TFboolean')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityInstance.xsd',
        34, 4)
    _Documentation = None


TFboolean._CF_pattern = pyxb.binding.facets.CF_pattern()
TFboolean._CF_pattern.addPattern(pattern=u'true/false')
TFboolean._InitializeFacetMap(TFboolean._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'TFboolean', TFboolean)

# Atomic simple type: {http://uri.etsi.org/m2m}fwName
class fwName(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fwName')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareInstance.xsd',
        25, 4)
    _Documentation = None


fwName._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(256L))
fwName._InitializeFacetMap(fwName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'fwName', fwName)

# Atomic simple type: {http://uri.etsi.org/m2m}fwURL
class fwURL(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fwURL')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareInstance.xsd',
        33, 4)
    _Documentation = None


fwURL._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(256L))
fwURL._InitializeFacetMap(fwURL._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'fwURL', fwURL)

# Atomic simple type: {http://uri.etsi.org/m2m}logTypId
class logTypId(pyxb.binding.datatypes.string,
               pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'logTypId')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerformanceLog.xsd',
        24, 4)
    _Documentation = None


logTypId._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=logTypId, enum_prefix=None)
logTypId.systLog = logTypId._CF_enumeration.addEnumeration(
    unicode_value=u'systLog', tag=u'systLog')
logTypId.appLog = logTypId._CF_enumeration.addEnumeration(
    unicode_value=u'appLog', tag=u'appLog')
logTypId._InitializeFacetMap(logTypId._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'logTypId', logTypId)

# Atomic simple type: {http://uri.etsi.org/m2m}RebootLevel
class RebootLevel(pyxb.binding.datatypes.string,
                  pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RebootLevel')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd', 32,
        4)
    _Documentation = None


RebootLevel._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=RebootLevel, enum_prefix=None)
RebootLevel.RESTART_OS = RebootLevel._CF_enumeration.addEnumeration(
    unicode_value=u'RESTART_OS', tag=u'RESTART_OS')
RebootLevel.RESTART_ALL_APPLS = RebootLevel._CF_enumeration.addEnumeration(
    unicode_value=u'RESTART_ALL_APPLS', tag=u'RESTART_ALL_APPLS')
RebootLevel.RESTART_ONE_APPL = RebootLevel._CF_enumeration.addEnumeration(
    unicode_value=u'RESTART_ONE_APPL', tag=u'RESTART_ONE_APPL')
RebootLevel._InitializeFacetMap(RebootLevel._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'RebootLevel', RebootLevel)

# Atomic simple type: {http://uri.etsi.org/m2m}RebootTiming
class RebootTiming(pyxb.binding.datatypes.string,
                   pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RebootTiming')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd', 50,
        4)
    _Documentation = None


RebootTiming._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=RebootTiming, enum_prefix=None)
RebootTiming.IMMEDIATE = RebootTiming._CF_enumeration.addEnumeration(
    unicode_value=u'IMMEDIATE', tag=u'IMMEDIATE')
RebootTiming.ASAP = RebootTiming._CF_enumeration.addEnumeration(
    unicode_value=u'ASAP', tag=u'ASAP')
RebootTiming._InitializeFacetMap(RebootTiming._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'RebootTiming', RebootTiming)

# Atomic simple type: {http://uri.etsi.org/m2m}swName
class swName(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'swName')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareInstance.xsd',
        25, 4)
    _Documentation = None


swName._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(64L))
swName._InitializeFacetMap(swName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'swName', swName)

# Atomic simple type: {http://uri.etsi.org/m2m}swURL
class swURL(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'swURL')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareInstance.xsd',
        34, 4)
    _Documentation = None


swURL._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1024L))
swURL._InitializeFacetMap(swURL._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'swURL', swURL)

# Atomic simple type: {http://uri.etsi.org/m2m}trapEventIndex
class trapEventIndex(pyxb.binding.datatypes.integer):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'trapEventIndex')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
        53, 4)
    _Documentation = None


trapEventIndex._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(
    value_datatype=trapEventIndex, value=pyxb.binding.datatypes.integer(100L))
trapEventIndex._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(
    value_datatype=trapEventIndex, value=pyxb.binding.datatypes.integer(0L))
trapEventIndex._InitializeFacetMap(trapEventIndex._CF_maxInclusive,
                                   trapEventIndex._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'trapEventIndex', trapEventIndex)

# Atomic simple type: {http://uri.etsi.org/m2m}ExecStatus
class ExecStatus(pyxb.binding.datatypes.string,
                 pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExecStatus')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
        32, 4)
    _Documentation = None


ExecStatus._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=ExecStatus, enum_prefix=None)
ExecStatus.INITIATED = ExecStatus._CF_enumeration.addEnumeration(
    unicode_value=u'INITIATED', tag=u'INITIATED')
ExecStatus.STARTED = ExecStatus._CF_enumeration.addEnumeration(
    unicode_value=u'STARTED', tag=u'STARTED')
ExecStatus.FINISHED = ExecStatus._CF_enumeration.addEnumeration(
    unicode_value=u'FINISHED', tag=u'FINISHED')
ExecStatus.CANCELLING = ExecStatus._CF_enumeration.addEnumeration(
    unicode_value=u'CANCELLING', tag=u'CANCELLING')
ExecStatus._InitializeFacetMap(ExecStatus._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ExecStatus', ExecStatus)

# Atomic simple type: {http://uri.etsi.org/m2m}MemberType
class MemberType(pyxb.binding.datatypes.string,
                 pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MemberType')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 47, 4)
    _Documentation = None


MemberType._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=MemberType, enum_prefix=None)
MemberType.APPLICATION = MemberType._CF_enumeration.addEnumeration(
    unicode_value=u'APPLICATION', tag=u'APPLICATION')
MemberType.CONTAINER = MemberType._CF_enumeration.addEnumeration(
    unicode_value=u'CONTAINER', tag=u'CONTAINER')
MemberType.ACCESS_RIGHT = MemberType._CF_enumeration.addEnumeration(
    unicode_value=u'ACCESS_RIGHT', tag=u'ACCESS_RIGHT')
MemberType.SCL_BASE = MemberType._CF_enumeration.addEnumeration(
    unicode_value=u'SCL_BASE', tag=u'SCL_BASE')
MemberType.SCL = MemberType._CF_enumeration.addEnumeration(unicode_value=u'SCL',
                                                           tag=u'SCL')
MemberType.LOCATION_CONTAINER = MemberType._CF_enumeration.addEnumeration(
    unicode_value=u'LOCATION_CONTAINER', tag=u'LOCATION_CONTAINER')
MemberType.MGMT_OBJ = MemberType._CF_enumeration.addEnumeration(
    unicode_value=u'MGMT_OBJ', tag=u'MGMT_OBJ')
MemberType.MGMT_CMD = MemberType._CF_enumeration.addEnumeration(
    unicode_value=u'MGMT_CMD', tag=u'MGMT_CMD')
MemberType.ATTACHED_DEVICE = MemberType._CF_enumeration.addEnumeration(
    unicode_value=u'ATTACHED_DEVICE', tag=u'ATTACHED_DEVICE')
MemberType.MIXED = MemberType._CF_enumeration.addEnumeration(
    unicode_value=u'MIXED', tag=u'MIXED')
MemberType._InitializeFacetMap(MemberType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MemberType', MemberType)

# Atomic simple type: {http://uri.etsi.org/m2m}ConsistencyStrategy
class ConsistencyStrategy(pyxb.binding.datatypes.string,
                          pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'ConsistencyStrategy')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 62, 4)
    _Documentation = None


ConsistencyStrategy._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=ConsistencyStrategy, enum_prefix=None)
ConsistencyStrategy.ABANDON_GROUP = ConsistencyStrategy._CF_enumeration.addEnumeration(
    unicode_value=u'ABANDON_GROUP', tag=u'ABANDON_GROUP')
ConsistencyStrategy.ABANDON_MEMBER = ConsistencyStrategy._CF_enumeration.addEnumeration(
    unicode_value=u'ABANDON_MEMBER', tag=u'ABANDON_MEMBER')
ConsistencyStrategy.MODIFY_TYPE = ConsistencyStrategy._CF_enumeration.addEnumeration(
    unicode_value=u'MODIFY_TYPE', tag=u'MODIFY_TYPE')
ConsistencyStrategy._InitializeFacetMap(ConsistencyStrategy._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ConsistencyStrategy',
                            ConsistencyStrategy)

# Atomic simple type: {http://uri.etsi.org/m2m}LocationContainerType
class LocationContainerType(pyxb.binding.datatypes.string,
                            pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'LocationContainerType')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/locationContainer.xsd',
        23, 4)
    _Documentation = None


LocationContainerType._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=LocationContainerType, enum_prefix=None)
LocationContainerType.LOCATION_SERVER_BASED = LocationContainerType._CF_enumeration.addEnumeration(
    unicode_value=u'LOCATION_SERVER_BASED', tag=u'LOCATION_SERVER_BASED')
LocationContainerType.APPLICATION_GENERATED = LocationContainerType._CF_enumeration.addEnumeration(
    unicode_value=u'APPLICATION_GENERATED', tag=u'APPLICATION_GENERATED')
LocationContainerType._InitializeFacetMap(LocationContainerType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'LocationContainerType',
                            LocationContainerType)

# Atomic simple type: {http://uri.etsi.org/m2m}CmdType
class CmdType(pyxb.binding.datatypes.string,
              pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CmdType')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd', 35, 4)
    _Documentation = None


CmdType._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=CmdType, enum_prefix=None)
CmdType.RESET = CmdType._CF_enumeration.addEnumeration(unicode_value=u'RESET',
                                                       tag=u'RESET')
CmdType.REBOOT = CmdType._CF_enumeration.addEnumeration(unicode_value=u'REBOOT',
                                                        tag=u'REBOOT')
CmdType.UPLOAD = CmdType._CF_enumeration.addEnumeration(unicode_value=u'UPLOAD',
                                                        tag=u'UPLOAD')
CmdType.DOWNLOAD = CmdType._CF_enumeration.addEnumeration(
    unicode_value=u'DOWNLOAD', tag=u'DOWNLOAD')
CmdType.SCHEDULEDOWNLOAD = CmdType._CF_enumeration.addEnumeration(
    unicode_value=u'SCHEDULEDOWNLOAD', tag=u'SCHEDULEDOWNLOAD')
CmdType.SCHEDULEINFORM = CmdType._CF_enumeration.addEnumeration(
    unicode_value=u'SCHEDULEINFORM', tag=u'SCHEDULEINFORM')
CmdType.CHANGEDUSTATE = CmdType._CF_enumeration.addEnumeration(
    unicode_value=u'CHANGEDUSTATE', tag=u'CHANGEDUSTATE')
CmdType._InitializeFacetMap(CmdType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'CmdType', CmdType)

# Atomic simple type: {http://uri.etsi.org/m2m}MethodType
class MethodType(pyxb.binding.datatypes.string,
                 pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MethodType')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
        39, 4)
    _Documentation = None


MethodType._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=MethodType, enum_prefix=None)
MethodType.CREATE = MethodType._CF_enumeration.addEnumeration(
    unicode_value=u'CREATE', tag=u'CREATE')
MethodType.RETRIEVE = MethodType._CF_enumeration.addEnumeration(
    unicode_value=u'RETRIEVE', tag=u'RETRIEVE')
MethodType.UPDATE = MethodType._CF_enumeration.addEnumeration(
    unicode_value=u'UPDATE', tag=u'UPDATE')
MethodType.DELETE = MethodType._CF_enumeration.addEnumeration(
    unicode_value=u'DELETE', tag=u'DELETE')
MethodType.EXECUTE = MethodType._CF_enumeration.addEnumeration(
    unicode_value=u'EXECUTE', tag=u'EXECUTE')
MethodType.NOTIFY = MethodType._CF_enumeration.addEnumeration(
    unicode_value=u'NOTIFY', tag=u'NOTIFY')
MethodType._InitializeFacetMap(MethodType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MethodType', MethodType)

# Atomic simple type: {http://uri.etsi.org/m2m}MgmtProtocolType
class MgmtProtocolType(pyxb.binding.datatypes.string,
                       pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MgmtProtocolType')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 55, 4)
    _Documentation = None


MgmtProtocolType._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=MgmtProtocolType, enum_prefix=None)
MgmtProtocolType.OMA_DM = MgmtProtocolType._CF_enumeration.addEnumeration(
    unicode_value=u'OMA_DM', tag=u'OMA_DM')
MgmtProtocolType.BBF_TR069 = MgmtProtocolType._CF_enumeration.addEnumeration(
    unicode_value=u'BBF_TR069', tag=u'BBF_TR069')
MgmtProtocolType.OMADM = MgmtProtocolType._CF_enumeration.addEnumeration(
    unicode_value=u'OMA DM', tag=u'OMADM')
MgmtProtocolType.BBF_TR_069 = MgmtProtocolType._CF_enumeration.addEnumeration(
    unicode_value=u'BBF TR 069', tag=u'BBF_TR_069')
MgmtProtocolType.LWM2M = MgmtProtocolType._CF_enumeration.addEnumeration(
    unicode_value=u'LWM2M', tag=u'LWM2M')
MgmtProtocolType._InitializeFacetMap(MgmtProtocolType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'MgmtProtocolType',
                            MgmtProtocolType)

# Atomic simple type: {http://uri.etsi.org/m2m}SclType
class SclType(pyxb.binding.datatypes.string,
              pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SclType')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 61, 4)
    _Documentation = None


SclType._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=SclType, enum_prefix=None)
SclType.NSCL = SclType._CF_enumeration.addEnumeration(unicode_value=u'NSCL',
                                                      tag=u'NSCL')
SclType.GSCL = SclType._CF_enumeration.addEnumeration(unicode_value=u'GSCL',
                                                      tag=u'GSCL')
SclType.DSCL = SclType._CF_enumeration.addEnumeration(unicode_value=u'DSCL',
                                                      tag=u'DSCL')
SclType._InitializeFacetMap(SclType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'SclType', SclType)

# Atomic simple type: {http://uri.etsi.org/m2m}SubscriptionType
class SubscriptionType(pyxb.binding.datatypes.string,
                       pyxb.binding.basis.enumeration_mixin):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SubscriptionType')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
        44, 4)
    _Documentation = None


SubscriptionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=SubscriptionType, enum_prefix=None)
SubscriptionType.ASYNCHRONOUS = SubscriptionType._CF_enumeration.addEnumeration(
    unicode_value=u'ASYNCHRONOUS', tag=u'ASYNCHRONOUS')
SubscriptionType.SYNCHRONOUS = SubscriptionType._CF_enumeration.addEnumeration(
    unicode_value=u'SYNCHRONOUS', tag=u'SYNCHRONOUS')
SubscriptionType._InitializeFacetMap(SubscriptionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'SubscriptionType',
                            SubscriptionType)

# Complex type {http://uri.etsi.org/m2m}AccessRight with content type ELEMENT_ONLY
class AccessRight(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}AccessRight with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AccessRight')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}permissions uses Python identifier permissions
    __permissions = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'permissions'), 'permissions',
        '__httpuri_etsi_orgm2m_AccessRight_httpuri_etsi_orgm2mpermissions',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
            25, 4), )

    permissions = property(__permissions.value, __permissions.set, None, None)


    # Element {http://uri.etsi.org/m2m}selfPermissions uses Python identifier selfPermissions
    __selfPermissions = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'selfPermissions'),
        'selfPermissions',
        '__httpuri_etsi_orgm2m_AccessRight_httpuri_etsi_orgm2mselfPermissions',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
            26, 4), )

    selfPermissions = property(__selfPermissions.value, __selfPermissions.set,
                               None, None)


    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_AccessRight_httpuri_etsi_orgm2mcreationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_AccessRight_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}expirationTime uses Python identifier expirationTime
    __expirationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
        'expirationTime',
        '__httpuri_etsi_orgm2m_AccessRight_httpuri_etsi_orgm2mexpirationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            16, 4), )

    expirationTime = property(__expirationTime.value, __expirationTime.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}searchStrings uses Python identifier searchStrings
    __searchStrings = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings'),
        'searchStrings',
        '__httpuri_etsi_orgm2m_AccessRight_httpuri_etsi_orgm2msearchStrings',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            18, 4), )

    searchStrings = property(__searchStrings.value, __searchStrings.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}announceTo uses Python identifier announceTo
    __announceTo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'announceTo'), 'announceTo',
        '__httpuri_etsi_orgm2m_AccessRight_httpuri_etsi_orgm2mannounceTo',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            58, 4), )

    announceTo = property(__announceTo.value, __announceTo.set, None, None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_AccessRight_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)


    # Attribute {http://uri.etsi.org/m2m}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_AccessRight_httpuri_etsi_orgm2mid',
        pyxb.binding.datatypes.NMTOKEN)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 8, 4)
    __id._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        22, 8)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __permissions.name(): __permissions,
        __selfPermissions.name(): __selfPermissions,
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __expirationTime.name(): __expirationTime,
        __searchStrings.name(): __searchStrings,
        __announceTo.name(): __announceTo,
        __subscriptionsReference.name(): __subscriptionsReference
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'AccessRight', AccessRight)


# Complex type {http://uri.etsi.org/m2m}PermissionListType with content type ELEMENT_ONLY
class PermissionListType(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}PermissionListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'PermissionListType')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        28, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}permission uses Python identifier permission
    __permission = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'permission'), 'permission',
        '__httpuri_etsi_orgm2m_PermissionListType_httpuri_etsi_orgm2mpermission',
        True, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
            34, 4), )

    permission = property(__permission.value, __permission.set, None, None)

    _ElementMap.update({
        __permission.name(): __permission
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'PermissionListType',
                            PermissionListType)


# Complex type {http://uri.etsi.org/m2m}PermissionType with content type ELEMENT_ONLY
class PermissionType(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}PermissionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PermissionType')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        36, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}permissionFlags uses Python identifier permissionFlags
    __permissionFlags = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'permissionFlags'),
        'permissionFlags',
        '__httpuri_etsi_orgm2m_PermissionType_httpuri_etsi_orgm2mpermissionFlags',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
            44, 4), )

    permissionFlags = property(__permissionFlags.value, __permissionFlags.set,
                               None, None)


    # Element {http://uri.etsi.org/m2m}permissionHolders uses Python identifier permissionHolders
    __permissionHolders = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'permissionHolders'),
        'permissionHolders',
        '__httpuri_etsi_orgm2m_PermissionType_httpuri_etsi_orgm2mpermissionHolders',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
            46, 4), )

    permissionHolders = property(__permissionHolders.value,
                                 __permissionHolders.set, None, None)


    # Attribute {http://uri.etsi.org/m2m}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_PermissionType_httpuri_etsi_orgm2mid',
        pyxb.binding.datatypes.NMTOKEN)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 8, 4)
    __id._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        41, 8)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __permissionFlags.name(): __permissionFlags,
        __permissionHolders.name(): __permissionHolders
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'PermissionType', PermissionType)


# Complex type {http://uri.etsi.org/m2m}PermissionHolderType with content type ELEMENT_ONLY
class PermissionHolderType(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}PermissionHolderType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'PermissionHolderType')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        48, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}holderRefs uses Python identifier holderRefs
    __holderRefs = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'holderRefs'), 'holderRefs',
        '__httpuri_etsi_orgm2m_PermissionHolderType_httpuri_etsi_orgm2mholderRefs',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
            58, 4), )

    holderRefs = property(__holderRefs.value, __holderRefs.set, None, None)


    # Element {http://uri.etsi.org/m2m}domains uses Python identifier domains
    __domains = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'domains'), 'domains',
        '__httpuri_etsi_orgm2m_PermissionHolderType_httpuri_etsi_orgm2mdomains',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
            59, 4), )

    domains = property(__domains.value, __domains.set, None, None)


    # Element {http://uri.etsi.org/m2m}all uses Python identifier all
    __all = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'all'), 'all',
        '__httpuri_etsi_orgm2m_PermissionHolderType_httpuri_etsi_orgm2mall',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
            75, 4), )

    all = property(__all.value, __all.set, None, None)


    # Element {http://uri.etsi.org/m2m}applicationIDs uses Python identifier applicationIDs
    __applicationIDs = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'applicationIDs'),
        'applicationIDs',
        '__httpuri_etsi_orgm2m_PermissionHolderType_httpuri_etsi_orgm2mapplicationIDs',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
            103, 4), )

    applicationIDs = property(__applicationIDs.value, __applicationIDs.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}sclIDs uses Python identifier sclIDs
    __sclIDs = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'sclIDs'), 'sclIDs',
        '__httpuri_etsi_orgm2m_PermissionHolderType_httpuri_etsi_orgm2msclIDs',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
            114, 4), )

    sclIDs = property(__sclIDs.value, __sclIDs.set, None, None)

    _ElementMap.update({
        __holderRefs.name(): __holderRefs,
        __domains.name(): __domains,
        __all.name(): __all,
        __applicationIDs.name(): __applicationIDs,
        __sclIDs.name(): __sclIDs
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'PermissionHolderType',
                            PermissionHolderType)


# Complex type {http://uri.etsi.org/m2m}HolderRefListType with content type ELEMENT_ONLY
class HolderRefListType(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}HolderRefListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'HolderRefListType')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        61, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}holderRef uses Python identifier holderRef
    __holderRef = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'holderRef'), 'holderRef',
        '__httpuri_etsi_orgm2m_HolderRefListType_httpuri_etsi_orgm2mholderRef',
        True, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
            73, 4), )

    holderRef = property(__holderRef.value, __holderRef.set, None, None)

    _ElementMap.update({
        __holderRef.name(): __holderRef
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'HolderRefListType',
                            HolderRefListType)


# Complex type {http://uri.etsi.org/m2m}DomainListType with content type ELEMENT_ONLY
class DomainListType(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}DomainListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DomainListType')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        67, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}domain uses Python identifier domain
    __domain = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'domain'), 'domain',
        '__httpuri_etsi_orgm2m_DomainListType_httpuri_etsi_orgm2mdomain', True,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
            83, 4), )

    domain = property(__domain.value, __domain.set, None, None)

    _ElementMap.update({
        __domain.name(): __domain
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'DomainListType', DomainListType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        76, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


# Complex type {http://uri.etsi.org/m2m}PermissionFlagListType with content type ELEMENT_ONLY
class PermissionFlagListType(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}PermissionFlagListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'PermissionFlagListType')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        97, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}flag uses Python identifier flag
    __flag = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'flag'), 'flag',
        '__httpuri_etsi_orgm2m_PermissionFlagListType_httpuri_etsi_orgm2mflag',
        True, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
            95, 4), )

    flag = property(__flag.value, __flag.set, None, None)

    _ElementMap.update({
        __flag.name(): __flag
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'PermissionFlagListType',
                            PermissionFlagListType)


# Complex type {http://uri.etsi.org/m2m}ApplicationIDs with content type ELEMENT_ONLY
class ApplicationIDs(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ApplicationIDs with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ApplicationIDs')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        105, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}applicationID uses Python identifier applicationID
    __applicationID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'applicationID'),
        'applicationID',
        '__httpuri_etsi_orgm2m_ApplicationIDs_httpuri_etsi_orgm2mapplicationID',
        True, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
            112, 4), )

    applicationID = property(__applicationID.value, __applicationID.set, None,
                             None)

    _ElementMap.update({
        __applicationID.name(): __applicationID
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'ApplicationIDs', ApplicationIDs)


# Complex type {http://uri.etsi.org/m2m}SclIDs with content type ELEMENT_ONLY
class SclIDs(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}SclIDs with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SclIDs')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        116, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}sclID uses Python identifier sclID
    __sclID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'sclID'), 'sclID',
        '__httpuri_etsi_orgm2m_SclIDs_httpuri_etsi_orgm2msclID', True,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
            122, 4), )

    sclID = property(__sclID.value, __sclID.set, None, None)

    _ElementMap.update({
        __sclID.name(): __sclID
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'SclIDs', SclIDs)


# Complex type {http://uri.etsi.org/m2m}AccessRightAnnc with content type ELEMENT_ONLY
class AccessRightAnnc(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}AccessRightAnnc with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AccessRightAnnc')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRightAnnc.xsd',
        10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_AccessRightAnnc_httpuri_etsi_orgm2maccessRightID',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}expirationTime uses Python identifier expirationTime
    __expirationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
        'expirationTime',
        '__httpuri_etsi_orgm2m_AccessRightAnnc_httpuri_etsi_orgm2mexpirationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            16, 4), )

    expirationTime = property(__expirationTime.value, __expirationTime.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}searchStrings uses Python identifier searchStrings
    __searchStrings = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings'),
        'searchStrings',
        '__httpuri_etsi_orgm2m_AccessRightAnnc_httpuri_etsi_orgm2msearchStrings',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            18, 4), )

    searchStrings = property(__searchStrings.value, __searchStrings.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}announceTo uses Python identifier announceTo
    __announceTo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'announceTo'), 'announceTo',
        '__httpuri_etsi_orgm2m_AccessRightAnnc_httpuri_etsi_orgm2mannounceTo',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            58, 4), )

    announceTo = property(__announceTo.value, __announceTo.set, None, None)


    # Element {http://uri.etsi.org/m2m}link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'link'), 'link',
        '__httpuri_etsi_orgm2m_AccessRightAnnc_httpuri_etsi_orgm2mlink', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            74, 4), )

    link = property(__link.value, __link.set, None, None)


    # Attribute {http://uri.etsi.org/m2m}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_AccessRightAnnc_httpuri_etsi_orgm2mid',
        pyxb.binding.datatypes.NMTOKEN)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 8, 4)
    __id._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRightAnnc.xsd',
        18, 8)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __expirationTime.name(): __expirationTime,
        __searchStrings.name(): __searchStrings,
        __announceTo.name(): __announceTo,
        __link.name(): __link
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'AccessRightAnnc', AccessRightAnnc)


# Complex type {http://uri.etsi.org/m2m}AccessRights with content type ELEMENT_ONLY
class AccessRights(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}AccessRights with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AccessRights')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRights.xsd',
        10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightCollection uses Python identifier accessRightCollection
    __accessRightCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightCollection'),
        'accessRightCollection',
        '__httpuri_etsi_orgm2m_AccessRights_httpuri_etsi_orgm2maccessRightCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRights.xsd',
            22, 4), )

    accessRightCollection = property(__accessRightCollection.value,
                                     __accessRightCollection.set, None, None)


    # Element {http://uri.etsi.org/m2m}accessRightAnncCollection uses Python identifier accessRightAnncCollection
    __accessRightAnncCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightAnncCollection'),
        'accessRightAnncCollection',
        '__httpuri_etsi_orgm2m_AccessRights_httpuri_etsi_orgm2maccessRightAnncCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRights.xsd',
            23, 4), )

    accessRightAnncCollection = property(__accessRightAnncCollection.value,
                                         __accessRightAnncCollection.set, None,
                                         None)


    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_AccessRights_httpuri_etsi_orgm2maccessRightID',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_AccessRights_httpuri_etsi_orgm2mcreationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_AccessRights_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_AccessRights_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)

    _ElementMap.update({
        __accessRightCollection.name(): __accessRightCollection,
        __accessRightAnncCollection.name(): __accessRightAnncCollection,
        __accessRightID.name(): __accessRightID,
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __subscriptionsReference.name(): __subscriptionsReference
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'AccessRights', AccessRights)


# Complex type {http://uri.etsi.org/m2m}Application with content type ELEMENT_ONLY
class Application(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}Application with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Application')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
        10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}referencePoint uses Python identifier referencePoint
    __referencePoint = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'referencePoint'),
        'referencePoint',
        '__httpuri_etsi_orgm2m_Application_httpuri_etsi_orgm2mreferencePoint',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
            32, 4), )

    referencePoint = property(__referencePoint.value, __referencePoint.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}aPoC uses Python identifier aPoC
    __aPoC = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'aPoC'), 'aPoC',
        '__httpuri_etsi_orgm2m_Application_httpuri_etsi_orgm2maPoC', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
            33, 4), )

    aPoC = property(__aPoC.value, __aPoC.set, None, None)


    # Element {http://uri.etsi.org/m2m}aPoCPaths uses Python identifier aPoCPaths
    __aPoCPaths = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'aPoCPaths'), 'aPoCPaths',
        '__httpuri_etsi_orgm2m_Application_httpuri_etsi_orgm2maPoCPaths', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
            34, 4), )

    aPoCPaths = property(__aPoCPaths.value, __aPoCPaths.set, None, None)


    # Element {http://uri.etsi.org/m2m}locRequestor uses Python identifier locRequestor
    __locRequestor = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'locRequestor'), 'locRequestor',
        '__httpuri_etsi_orgm2m_Application_httpuri_etsi_orgm2mlocRequestor',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
            36, 4), )

    locRequestor = property(__locRequestor.value, __locRequestor.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_Application_httpuri_etsi_orgm2maccessRightID',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_Application_httpuri_etsi_orgm2mcreationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_Application_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}expirationTime uses Python identifier expirationTime
    __expirationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
        'expirationTime',
        '__httpuri_etsi_orgm2m_Application_httpuri_etsi_orgm2mexpirationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            16, 4), )

    expirationTime = property(__expirationTime.value, __expirationTime.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}searchStrings uses Python identifier searchStrings
    __searchStrings = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings'),
        'searchStrings',
        '__httpuri_etsi_orgm2m_Application_httpuri_etsi_orgm2msearchStrings',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            18, 4), )

    searchStrings = property(__searchStrings.value, __searchStrings.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}announceTo uses Python identifier announceTo
    __announceTo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'announceTo'), 'announceTo',
        '__httpuri_etsi_orgm2m_Application_httpuri_etsi_orgm2mannounceTo',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            58, 4), )

    announceTo = property(__announceTo.value, __announceTo.set, None, None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_Application_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}groupsReference uses Python identifier groupsReference
    __groupsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'groupsReference'),
        'groupsReference',
        '__httpuri_etsi_orgm2m_Application_httpuri_etsi_orgm2mgroupsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            77, 4), )

    groupsReference = property(__groupsReference.value, __groupsReference.set,
                               None, None)


    # Element {http://uri.etsi.org/m2m}containersReference uses Python identifier containersReference
    __containersReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'containersReference'),
        'containersReference',
        '__httpuri_etsi_orgm2m_Application_httpuri_etsi_orgm2mcontainersReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            79, 4), )

    containersReference = property(__containersReference.value,
                                   __containersReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}accessRightsReference uses Python identifier accessRightsReference
    __accessRightsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightsReference'),
        'accessRightsReference',
        '__httpuri_etsi_orgm2m_Application_httpuri_etsi_orgm2maccessRightsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            81, 4), )

    accessRightsReference = property(__accessRightsReference.value,
                                     __accessRightsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}notificationChannelsReference uses Python identifier notificationChannelsReference
    __notificationChannelsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace,
                                    u'notificationChannelsReference'),
        'notificationChannelsReference',
        '__httpuri_etsi_orgm2m_Application_httpuri_etsi_orgm2mnotificationChannelsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            82, 4), )

    notificationChannelsReference = property(
        __notificationChannelsReference.value,
        __notificationChannelsReference.set, None, None)


    # Attribute appId uses Python identifier appId
    __appId = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, u'appId'), 'appId',
        '__httpuri_etsi_orgm2m_Application_appId',
        pyxb.binding.datatypes.anyURI)
    __appId._DeclarationLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
        29, 8)
    __appId._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
        29, 8)

    appId = property(__appId.value, __appId.set, None, None)

    _ElementMap.update({
        __referencePoint.name(): __referencePoint,
        __aPoC.name(): __aPoC,
        __aPoCPaths.name(): __aPoCPaths,
        __locRequestor.name(): __locRequestor,
        __accessRightID.name(): __accessRightID,
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __expirationTime.name(): __expirationTime,
        __searchStrings.name(): __searchStrings,
        __announceTo.name(): __announceTo,
        __subscriptionsReference.name(): __subscriptionsReference,
        __groupsReference.name(): __groupsReference,
        __containersReference.name(): __containersReference,
        __accessRightsReference.name(): __accessRightsReference,
        __notificationChannelsReference.name(): __notificationChannelsReference
    })
    _AttributeMap.update({
        __appId.name(): __appId
    })


Namespace.addCategoryObject('typeBinding', u'Application', Application)


# Complex type {http://uri.etsi.org/m2m}APoCPaths with content type ELEMENT_ONLY
class APoCPaths(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}APoCPaths with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'APoCPaths')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
        46, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}aPoCPath uses Python identifier aPoCPath
    __aPoCPath = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'aPoCPath'), 'aPoCPath',
        '__httpuri_etsi_orgm2m_APoCPaths_httpuri_etsi_orgm2maPoCPath', True,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
            52, 4), )

    aPoCPath = property(__aPoCPath.value, __aPoCPath.set, None, None)

    _ElementMap.update({
        __aPoCPath.name(): __aPoCPath
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'APoCPaths', APoCPaths)


# Complex type {http://uri.etsi.org/m2m}APoCPath with content type ELEMENT_ONLY
class APoCPath(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}APoCPath with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'APoCPath')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
        54, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}path uses Python identifier path
    __path = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'path'), 'path',
        '__httpuri_etsi_orgm2m_APoCPath_httpuri_etsi_orgm2mpath', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
            62, 4), )

    path = property(__path.value, __path.set, None, None)


    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_APoCPath_httpuri_etsi_orgm2maccessRightID',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}searchStrings uses Python identifier searchStrings
    __searchStrings = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings'),
        'searchStrings',
        '__httpuri_etsi_orgm2m_APoCPath_httpuri_etsi_orgm2msearchStrings',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            18, 4), )

    searchStrings = property(__searchStrings.value, __searchStrings.set, None,
                             None)

    _ElementMap.update({
        __path.name(): __path,
        __accessRightID.name(): __accessRightID,
        __searchStrings.name(): __searchStrings
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'APoCPath', APoCPath)


# Complex type {http://uri.etsi.org/m2m}ApplicationAnnc with content type ELEMENT_ONLY
class ApplicationAnnc(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ApplicationAnnc with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ApplicationAnnc')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applicationAnnc.xsd',
        10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_ApplicationAnnc_httpuri_etsi_orgm2maccessRightID',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}expirationTime uses Python identifier expirationTime
    __expirationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
        'expirationTime',
        '__httpuri_etsi_orgm2m_ApplicationAnnc_httpuri_etsi_orgm2mexpirationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            16, 4), )

    expirationTime = property(__expirationTime.value, __expirationTime.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}searchStrings uses Python identifier searchStrings
    __searchStrings = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings'),
        'searchStrings',
        '__httpuri_etsi_orgm2m_ApplicationAnnc_httpuri_etsi_orgm2msearchStrings',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            18, 4), )

    searchStrings = property(__searchStrings.value, __searchStrings.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}announceTo uses Python identifier announceTo
    __announceTo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'announceTo'), 'announceTo',
        '__httpuri_etsi_orgm2m_ApplicationAnnc_httpuri_etsi_orgm2mannounceTo',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            58, 4), )

    announceTo = property(__announceTo.value, __announceTo.set, None, None)


    # Element {http://uri.etsi.org/m2m}link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'link'), 'link',
        '__httpuri_etsi_orgm2m_ApplicationAnnc_httpuri_etsi_orgm2mlink', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            74, 4), )

    link = property(__link.value, __link.set, None, None)


    # Element {http://uri.etsi.org/m2m}groupsReference uses Python identifier groupsReference
    __groupsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'groupsReference'),
        'groupsReference',
        '__httpuri_etsi_orgm2m_ApplicationAnnc_httpuri_etsi_orgm2mgroupsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            77, 4), )

    groupsReference = property(__groupsReference.value, __groupsReference.set,
                               None, None)


    # Element {http://uri.etsi.org/m2m}containersReference uses Python identifier containersReference
    __containersReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'containersReference'),
        'containersReference',
        '__httpuri_etsi_orgm2m_ApplicationAnnc_httpuri_etsi_orgm2mcontainersReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            79, 4), )

    containersReference = property(__containersReference.value,
                                   __containersReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}accessRightsReference uses Python identifier accessRightsReference
    __accessRightsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightsReference'),
        'accessRightsReference',
        '__httpuri_etsi_orgm2m_ApplicationAnnc_httpuri_etsi_orgm2maccessRightsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            81, 4), )

    accessRightsReference = property(__accessRightsReference.value,
                                     __accessRightsReference.set, None, None)


    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_ApplicationAnnc_id',
        pyxb.binding.datatypes.anyURI)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applicationAnnc.xsd',
        22, 8)
    __id._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applicationAnnc.xsd',
        22, 8)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __expirationTime.name(): __expirationTime,
        __searchStrings.name(): __searchStrings,
        __announceTo.name(): __announceTo,
        __link.name(): __link,
        __groupsReference.name(): __groupsReference,
        __containersReference.name(): __containersReference,
        __accessRightsReference.name(): __accessRightsReference
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'ApplicationAnnc', ApplicationAnnc)


# Complex type {http://uri.etsi.org/m2m}Applications with content type ELEMENT_ONLY
class Applications(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}Applications with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Applications')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
        10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}applicationCollection uses Python identifier applicationCollection
    __applicationCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'applicationCollection'),
        'applicationCollection',
        '__httpuri_etsi_orgm2m_Applications_httpuri_etsi_orgm2mapplicationCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
            23, 4), )

    applicationCollection = property(__applicationCollection.value,
                                     __applicationCollection.set, None, None)


    # Element {http://uri.etsi.org/m2m}applicationAnncCollection uses Python identifier applicationAnncCollection
    __applicationAnncCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'applicationAnncCollection'),
        'applicationAnncCollection',
        '__httpuri_etsi_orgm2m_Applications_httpuri_etsi_orgm2mapplicationAnncCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
            24, 4), )

    applicationAnncCollection = property(__applicationAnncCollection.value,
                                         __applicationAnncCollection.set, None,
                                         None)


    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_Applications_httpuri_etsi_orgm2maccessRightID',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_Applications_httpuri_etsi_orgm2mcreationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_Applications_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_Applications_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}mgmtObjsReference uses Python identifier mgmtObjsReference
    __mgmtObjsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'mgmtObjsReference'),
        'mgmtObjsReference',
        '__httpuri_etsi_orgm2m_Applications_httpuri_etsi_orgm2mmgmtObjsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            84, 4), )

    mgmtObjsReference = property(__mgmtObjsReference.value,
                                 __mgmtObjsReference.set, None, None)

    _ElementMap.update({
        __applicationCollection.name(): __applicationCollection,
        __applicationAnncCollection.name(): __applicationAnncCollection,
        __accessRightID.name(): __accessRightID,
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __subscriptionsReference.name(): __subscriptionsReference,
        __mgmtObjsReference.name(): __mgmtObjsReference
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'Applications', Applications)


# Complex type {http://uri.etsi.org/m2m}AttachedDevice with content type ELEMENT_ONLY
class AttachedDevice(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}AttachedDevice with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AttachedDevice')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevice.xsd',
        10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_AttachedDevice_httpuri_etsi_orgm2maccessRightID',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_AttachedDevice_httpuri_etsi_orgm2mcreationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_AttachedDevice_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_AttachedDevice_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}mgmtObjsReference uses Python identifier mgmtObjsReference
    __mgmtObjsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'mgmtObjsReference'),
        'mgmtObjsReference',
        '__httpuri_etsi_orgm2m_AttachedDevice_httpuri_etsi_orgm2mmgmtObjsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            84, 4), )

    mgmtObjsReference = property(__mgmtObjsReference.value,
                                 __mgmtObjsReference.set, None, None)


    # Attribute {http://uri.etsi.org/m2m}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_AttachedDevice_httpuri_etsi_orgm2mid',
        pyxb.binding.datatypes.NMTOKEN)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 8, 4)
    __id._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevice.xsd',
        21, 8)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __subscriptionsReference.name(): __subscriptionsReference,
        __mgmtObjsReference.name(): __mgmtObjsReference
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'AttachedDevice', AttachedDevice)


# Complex type {http://uri.etsi.org/m2m}AttachedDevices with content type ELEMENT_ONLY
class AttachedDevices(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}AttachedDevices with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AttachedDevices')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevices.xsd',
        10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}attachedDeviceCollection uses Python identifier attachedDeviceCollection
    __attachedDeviceCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'attachedDeviceCollection'),
        'attachedDeviceCollection',
        '__httpuri_etsi_orgm2m_AttachedDevices_httpuri_etsi_orgm2mattachedDeviceCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevices.xsd',
            23, 4), )

    attachedDeviceCollection = property(__attachedDeviceCollection.value,
                                        __attachedDeviceCollection.set, None,
                                        None)


    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_AttachedDevices_httpuri_etsi_orgm2maccessRightID',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_AttachedDevices_httpuri_etsi_orgm2mcreationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_AttachedDevices_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_AttachedDevices_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}mgmtObjsReference uses Python identifier mgmtObjsReference
    __mgmtObjsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'mgmtObjsReference'),
        'mgmtObjsReference',
        '__httpuri_etsi_orgm2m_AttachedDevices_httpuri_etsi_orgm2mmgmtObjsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            84, 4), )

    mgmtObjsReference = property(__mgmtObjsReference.value,
                                 __mgmtObjsReference.set, None, None)

    _ElementMap.update({
        __attachedDeviceCollection.name(): __attachedDeviceCollection,
        __accessRightID.name(): __accessRightID,
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __subscriptionsReference.name(): __subscriptionsReference,
        __mgmtObjsReference.name(): __mgmtObjsReference
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'AttachedDevices', AttachedDevices)


# Complex type {http://uri.etsi.org/m2m}BootstrapParamSet with content type ELEMENT_ONLY
class BootstrapParamSet(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}BootstrapParamSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BootstrapParamSet')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/bootstrapParamSet.xsd',
        11, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}sclIdList uses Python identifier sclIdList
    __sclIdList = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'sclIdList'), 'sclIdList',
        '__httpuri_etsi_orgm2m_BootstrapParamSet_httpuri_etsi_orgm2msclIdList',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/bootstrapParamSet.xsd',
            23, 4), )

    sclIdList = property(__sclIdList.value, __sclIdList.set, None, None)


    # Element {http://uri.etsi.org/m2m}sclId uses Python identifier sclId
    __sclId = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'sclId'), 'sclId',
        '__httpuri_etsi_orgm2m_BootstrapParamSet_httpuri_etsi_orgm2msclId',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            220, 4), )

    sclId = property(__sclId.value, __sclId.set, None, None)


    # Element {http://uri.etsi.org/m2m}securityM2MNodeId uses Python identifier securityM2MNodeId
    __securityM2MNodeId = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'securityM2MNodeId'),
        'securityM2MNodeId',
        '__httpuri_etsi_orgm2m_BootstrapParamSet_httpuri_etsi_orgm2msecurityM2MNodeId',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
            6, 4), )

    securityM2MNodeId = property(__securityM2MNodeId.value,
                                 __securityM2MNodeId.set, None, None)


    # Element {http://uri.etsi.org/m2m}securityKmrIndex uses Python identifier securityKmrIndex
    __securityKmrIndex = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'securityKmrIndex'),
        'securityKmrIndex',
        '__httpuri_etsi_orgm2m_BootstrapParamSet_httpuri_etsi_orgm2msecurityKmrIndex',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
            14, 4), )

    securityKmrIndex = property(__securityKmrIndex.value,
                                __securityKmrIndex.set, None, None)


    # Element {http://uri.etsi.org/m2m}securityLifetime uses Python identifier securityLifetime
    __securityLifetime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'securityLifetime'),
        'securityLifetime',
        '__httpuri_etsi_orgm2m_BootstrapParamSet_httpuri_etsi_orgm2msecurityLifetime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
            16, 4), )

    securityLifetime = property(__securityLifetime.value,
                                __securityLifetime.set, None, None)


    # Element {http://uri.etsi.org/m2m}securityMasFqdn uses Python identifier securityMasFqdn
    __securityMasFqdn = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'securityMasFqdn'),
        'securityMasFqdn',
        '__httpuri_etsi_orgm2m_BootstrapParamSet_httpuri_etsi_orgm2msecurityMasFqdn',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
            18, 4), )

    securityMasFqdn = property(__securityMasFqdn.value, __securityMasFqdn.set,
                               None, None)


    # Element {http://uri.etsi.org/m2m}securityEncryptedM2MKey uses Python identifier securityEncryptedM2MKey
    __securityEncryptedM2MKey = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'securityEncryptedM2MKey'),
        'securityEncryptedM2MKey',
        '__httpuri_etsi_orgm2m_BootstrapParamSet_httpuri_etsi_orgm2msecurityEncryptedM2MKey',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
            20, 4), )

    securityEncryptedM2MKey = property(__securityEncryptedM2MKey.value,
                                       __securityEncryptedM2MKey.set, None,
                                       None)

    _ElementMap.update({
        __sclIdList.name(): __sclIdList,
        __sclId.name(): __sclId,
        __securityM2MNodeId.name(): __securityM2MNodeId,
        __securityKmrIndex.name(): __securityKmrIndex,
        __securityLifetime.name(): __securityLifetime,
        __securityMasFqdn.name(): __securityMasFqdn,
        __securityEncryptedM2MKey.name(): __securityEncryptedM2MKey
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'BootstrapParamSet',
                            BootstrapParamSet)


# Complex type {http://uri.etsi.org/m2m}SearchStrings with content type ELEMENT_ONLY
class SearchStrings(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}SearchStrings with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SearchStrings')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 20, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}searchString uses Python identifier searchString
    __searchString = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'searchString'), 'searchString',
        '__httpuri_etsi_orgm2m_SearchStrings_httpuri_etsi_orgm2msearchString',
        True, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            28, 4), )

    searchString = property(__searchString.value, __searchString.set, None,
                            None)

    _ElementMap.update({
        __searchString.name(): __searchString
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'SearchStrings', SearchStrings)


# Complex type {http://uri.etsi.org/m2m}FilterCriteriaType with content type ELEMENT_ONLY
class FilterCriteriaType(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}FilterCriteriaType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'FilterCriteriaType')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 32, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element ifModifiedSince uses Python identifier ifModifiedSince
    __ifModifiedSince = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'ifModifiedSince'),
        'ifModifiedSince',
        '__httpuri_etsi_orgm2m_FilterCriteriaType_ifModifiedSince', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            34, 12), )

    ifModifiedSince = property(__ifModifiedSince.value, __ifModifiedSince.set,
                               None, None)


    # Element ifUnmodifiedSince uses Python identifier ifUnmodifiedSince
    __ifUnmodifiedSince = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'ifUnmodifiedSince'),
        'ifUnmodifiedSince',
        '__httpuri_etsi_orgm2m_FilterCriteriaType_ifUnmodifiedSince', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            36, 12), )

    ifUnmodifiedSince = property(__ifUnmodifiedSince.value,
                                 __ifUnmodifiedSince.set, None, None)


    # Element ifNoneMatch uses Python identifier ifNoneMatch
    __ifNoneMatch = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'ifNoneMatch'), 'ifNoneMatch',
        '__httpuri_etsi_orgm2m_FilterCriteriaType_ifNoneMatch', True,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            38, 12), )

    ifNoneMatch = property(__ifNoneMatch.value, __ifNoneMatch.set, None, None)


    # Element attributeAccessor uses Python identifier attributeAccessor
    __attributeAccessor = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'attributeAccessor'),
        'attributeAccessor',
        '__httpuri_etsi_orgm2m_FilterCriteriaType_attributeAccessor', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            40, 12), )

    attributeAccessor = property(__attributeAccessor.value,
                                 __attributeAccessor.set, None, None)


    # Element searchString uses Python identifier searchString
    __searchString = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'searchString'), 'searchString',
        '__httpuri_etsi_orgm2m_FilterCriteriaType_searchString', True,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            41, 12), )

    searchString = property(__searchString.value, __searchString.set, None,
                            None)


    # Element createdAfter uses Python identifier createdAfter
    __createdAfter = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'createdAfter'), 'createdAfter',
        '__httpuri_etsi_orgm2m_FilterCriteriaType_createdAfter', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            43, 12), )

    createdAfter = property(__createdAfter.value, __createdAfter.set, None,
                            None)


    # Element createdBefore uses Python identifier createdBefore
    __createdBefore = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'createdBefore'), 'createdBefore',
        '__httpuri_etsi_orgm2m_FilterCriteriaType_createdBefore', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            45, 12), )

    createdBefore = property(__createdBefore.value, __createdBefore.set, None,
                             None)

    _ElementMap.update({
        __ifModifiedSince.name(): __ifModifiedSince,
        __ifUnmodifiedSince.name(): __ifUnmodifiedSince,
        __ifNoneMatch.name(): __ifNoneMatch,
        __attributeAccessor.name(): __attributeAccessor,
        __searchString.name(): __searchString,
        __createdAfter.name(): __createdAfter,
        __createdBefore.name(): __createdBefore
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'FilterCriteriaType',
                            FilterCriteriaType)


# Complex type {http://uri.etsi.org/m2m}AnyURIList with content type ELEMENT_ONLY
class AnyURIList(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}AnyURIList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AnyURIList')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 51, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element reference uses Python identifier reference
    __reference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'reference'), 'reference',
        '__httpuri_etsi_orgm2m_AnyURIList_reference', True,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            53, 12), )

    reference = property(__reference.value, __reference.set, None, None)

    _ElementMap.update({
        __reference.name(): __reference
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'AnyURIList', AnyURIList)


# Complex type {http://uri.etsi.org/m2m}AnnounceTo with content type ELEMENT_ONLY
class AnnounceTo(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}AnnounceTo with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AnnounceTo')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 60, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}activated uses Python identifier activated
    __activated = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'activated'), 'activated',
        '__httpuri_etsi_orgm2m_AnnounceTo_httpuri_etsi_orgm2mactivated', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            68, 4), )

    activated = property(__activated.value, __activated.set, None, None)


    # Element {http://uri.etsi.org/m2m}sclList uses Python identifier sclList
    __sclList = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'sclList'), 'sclList',
        '__httpuri_etsi_orgm2m_AnnounceTo_httpuri_etsi_orgm2msclList', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            69, 4), )

    sclList = property(__sclList.value, __sclList.set, None, None)


    # Element {http://uri.etsi.org/m2m}global uses Python identifier global_
    __global = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'global'), 'global_',
        '__httpuri_etsi_orgm2m_AnnounceTo_httpuri_etsi_orgm2mglobal', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            70, 4), )

    global_ = property(__global.value, __global.set, None, None)

    _ElementMap.update({
        __activated.name(): __activated,
        __sclList.name(): __sclList,
        __global.name(): __global
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'AnnounceTo', AnnounceTo)


# Complex type {http://uri.etsi.org/m2m}NamedReferenceCollection with content type ELEMENT_ONLY
class NamedReferenceCollection(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}NamedReferenceCollection with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'NamedReferenceCollection')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 89, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}namedReference uses Python identifier namedReference
    __namedReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'namedReference'),
        'namedReference',
        '__httpuri_etsi_orgm2m_NamedReferenceCollection_httpuri_etsi_orgm2mnamedReference',
        True, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            104, 4), )

    namedReference = property(__namedReference.value, __namedReference.set,
                              None, None)

    _ElementMap.update({
        __namedReference.name(): __namedReference
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'NamedReferenceCollection',
                            NamedReferenceCollection)


# Complex type {http://uri.etsi.org/m2m}ReferenceToNamedResource with content type SIMPLE
class ReferenceToNamedResource(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ReferenceToNamedResource with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'ReferenceToNamedResource')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 96, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyURI

    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_ReferenceToNamedResource_id',
        pyxb.binding.datatypes.anySimpleType)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 99,
        16)
    __id._UseLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 99,
        16)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'ReferenceToNamedResource',
                            ReferenceToNamedResource)


# Complex type {http://uri.etsi.org/m2m}Schedule with content type ELEMENT_ONLY
class Schedule(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}Schedule with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Schedule')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 108,
        4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}scheduleString uses Python identifier scheduleString
    __scheduleString = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'scheduleString'),
        'scheduleString',
        '__httpuri_etsi_orgm2m_Schedule_httpuri_etsi_orgm2mscheduleString',
        True, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            115, 4), )

    scheduleString = property(__scheduleString.value, __scheduleString.set,
                              None, None)

    _ElementMap.update({
        __scheduleString.name(): __scheduleString
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'Schedule', Schedule)


# Complex type {http://uri.etsi.org/m2m}ScheduleString with content type SIMPLE
class ScheduleString(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ScheduleString with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ScheduleString')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 117,
        4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string

    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_ScheduleString_id',
        pyxb.binding.datatypes.anySimpleType, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 120,
        16)
    __id._UseLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 120,
        16)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'ScheduleString', ScheduleString)


# Complex type {http://uri.etsi.org/m2m}ChannelData with content type EMPTY
class ChannelData(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ChannelData with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ChannelData')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 148,
        4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'ChannelData', ChannelData)


# Complex type {http://uri.etsi.org/m2m}TrpdtType with content type ELEMENT_ONLY
class TrpdtType(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}TrpdtType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TrpdtType')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 177,
        4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element tolerableDelay uses Python identifier tolerableDelay
    __tolerableDelay = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'tolerableDelay'), 'tolerableDelay',
        '__httpuri_etsi_orgm2m_TrpdtType_tolerableDelay', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            179, 12), )

    tolerableDelay = property(__tolerableDelay.value, __tolerableDelay.set,
                              None, None)


    # Element tolerableTime uses Python identifier tolerableTime
    __tolerableTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'tolerableTime'), 'tolerableTime',
        '__httpuri_etsi_orgm2m_TrpdtType_tolerableTime', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            181, 12), )

    tolerableTime = property(__tolerableTime.value, __tolerableTime.set, None,
                             None)

    _ElementMap.update({
        __tolerableDelay.name(): __tolerableDelay,
        __tolerableTime.name(): __tolerableTime
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'TrpdtType', TrpdtType)


# Complex type {http://uri.etsi.org/m2m}ActionStatus with content type ELEMENT_ONLY
class ActionStatus(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ActionStatus with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ActionStatus')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 24,
        4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element action uses Python identifier action
    __action = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'action'), 'action',
        '__httpuri_etsi_orgm2m_ActionStatus_action', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
            26, 12), )

    action = property(__action.value, __action.set, None, None)


    # Element progress uses Python identifier progress
    __progress = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'progress'), 'progress',
        '__httpuri_etsi_orgm2m_ActionStatus_progress', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
            27, 12), )

    progress = property(__progress.value, __progress.set, None, None)


    # Element finalStatus uses Python identifier finalStatus
    __finalStatus = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'finalStatus'), 'finalStatus',
        '__httpuri_etsi_orgm2m_ActionStatus_finalStatus', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
            35, 12), )

    finalStatus = property(__finalStatus.value, __finalStatus.set, None, None)

    _ElementMap.update({
        __action.name(): __action,
        __progress.name(): __progress,
        __finalStatus.name(): __finalStatus
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'ActionStatus', ActionStatus)


# Complex type {http://uri.etsi.org/m2m}AreaNwkTypeInfoSet with content type ELEMENT_ONLY
class AreaNwkTypeInfoSet(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}AreaNwkTypeInfoSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'AreaNwkTypeInfoSet')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 65,
        4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}areaNwkTypeItem uses Python identifier areaNwkTypeItem
    __areaNwkTypeItem = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'areaNwkTypeItem'),
        'areaNwkTypeItem',
        '__httpuri_etsi_orgm2m_AreaNwkTypeInfoSet_httpuri_etsi_orgm2mareaNwkTypeItem',
        True, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
            72, 4), )

    areaNwkTypeItem = property(__areaNwkTypeItem.value, __areaNwkTypeItem.set,
                               None, None)

    _ElementMap.update({
        __areaNwkTypeItem.name(): __areaNwkTypeItem
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'AreaNwkTypeInfoSet',
                            AreaNwkTypeInfoSet)


# Complex type {http://uri.etsi.org/m2m}NameValuePairItem with content type ELEMENT_ONLY
class NameValuePairItem(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}NameValuePairItem with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NameValuePairItem')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 74,
        4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'name'), 'name',
        '__httpuri_etsi_orgm2m_NameValuePairItem_httpuri_etsi_orgm2mname',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
            81, 4), )

    name = property(__name.value, __name.set, None, None)


    # Element {http://uri.etsi.org/m2m}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'value'), 'value_',
        '__httpuri_etsi_orgm2m_NameValuePairItem_httpuri_etsi_orgm2mvalue',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
            83, 4), )

    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        __name.name(): __name,
        __value.name(): __value
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'NameValuePairItem',
                            NameValuePairItem)


# Complex type {http://uri.etsi.org/m2m}CommunicationChannel with content type ELEMENT_ONLY
class CommunicationChannel(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}CommunicationChannel with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'CommunicationChannel')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannel.xsd',
        10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_CommunicationChannel_httpuri_etsi_orgm2mcreationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_CommunicationChannel_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}contactURI uses Python identifier contactURI
    __contactURI = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'contactURI'), 'contactURI',
        '__httpuri_etsi_orgm2m_CommunicationChannel_httpuri_etsi_orgm2mcontactURI',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            136, 4), )

    contactURI = property(__contactURI.value, __contactURI.set, None, None)


    # Element {http://uri.etsi.org/m2m}channelType uses Python identifier channelType
    __channelType = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'channelType'), 'channelType',
        '__httpuri_etsi_orgm2m_CommunicationChannel_httpuri_etsi_orgm2mchannelType',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            138, 4), )

    channelType = property(__channelType.value, __channelType.set, None, None)


    # Element {http://uri.etsi.org/m2m}channelData uses Python identifier channelData
    __channelData = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'channelData'), 'channelData',
        '__httpuri_etsi_orgm2m_CommunicationChannel_httpuri_etsi_orgm2mchannelData',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            146, 4), )

    channelData = property(__channelData.value, __channelData.set, None, None)


    # Attribute {http://uri.etsi.org/m2m}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_CommunicationChannel_httpuri_etsi_orgm2mid',
        pyxb.binding.datatypes.NMTOKEN)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 8, 4)
    __id._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannel.xsd',
        19, 8)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __contactURI.name(): __contactURI,
        __channelType.name(): __channelType,
        __channelData.name(): __channelData
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'CommunicationChannel',
                            CommunicationChannel)


# Complex type {http://uri.etsi.org/m2m}CommunicationChannels with content type ELEMENT_ONLY
class CommunicationChannels(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}CommunicationChannels with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'CommunicationChannels')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannels.xsd',
        10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_CommunicationChannels_httpuri_etsi_orgm2mcreationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_CommunicationChannels_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}communicationChannelCollection uses Python identifier communicationChannelCollection
    __communicationChannelCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace,
                                    u'communicationChannelCollection'),
        'communicationChannelCollection',
        '__httpuri_etsi_orgm2m_CommunicationChannels_httpuri_etsi_orgm2mcommunicationChannelCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannels.xsd',
            19, 4), )

    communicationChannelCollection = property(
        __communicationChannelCollection.value,
        __communicationChannelCollection.set, None, None)

    _ElementMap.update({
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __communicationChannelCollection.name(): __communicationChannelCollection
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'CommunicationChannels',
                            CommunicationChannels)


# Complex type {http://uri.etsi.org/m2m}ConnectionParamSet with content type ELEMENT_ONLY
class ConnectionParamSet(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ConnectionParamSet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'ConnectionParamSet')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/connectionParamSet.xsd',
        11, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}sclId uses Python identifier sclId
    __sclId = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'sclId'), 'sclId',
        '__httpuri_etsi_orgm2m_ConnectionParamSet_httpuri_etsi_orgm2msclId',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            220, 4), )

    sclId = property(__sclId.value, __sclId.set, None, None)


    # Element {http://uri.etsi.org/m2m}securityLifetime uses Python identifier securityLifetime
    __securityLifetime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'securityLifetime'),
        'securityLifetime',
        '__httpuri_etsi_orgm2m_ConnectionParamSet_httpuri_etsi_orgm2msecurityLifetime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
            16, 4), )

    securityLifetime = property(__securityLifetime.value,
                                __securityLifetime.set, None, None)


    # Element {http://uri.etsi.org/m2m}securityEncryptedM2MKey uses Python identifier securityEncryptedM2MKey
    __securityEncryptedM2MKey = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'securityEncryptedM2MKey'),
        'securityEncryptedM2MKey',
        '__httpuri_etsi_orgm2m_ConnectionParamSet_httpuri_etsi_orgm2msecurityEncryptedM2MKey',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
            20, 4), )

    securityEncryptedM2MKey = property(__securityEncryptedM2MKey.value,
                                       __securityEncryptedM2MKey.set, None,
                                       None)


    # Element {http://uri.etsi.org/m2m}securityKmcIndex uses Python identifier securityKmcIndex
    __securityKmcIndex = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'securityKmcIndex'),
        'securityKmcIndex',
        '__httpuri_etsi_orgm2m_ConnectionParamSet_httpuri_etsi_orgm2msecurityKmcIndex',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
            30, 4), )

    securityKmcIndex = property(__securityKmcIndex.value,
                                __securityKmcIndex.set, None, None)


    # Element {http://uri.etsi.org/m2m}securitymIdFlags uses Python identifier securitymIdFlags
    __securitymIdFlags = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'securitymIdFlags'),
        'securitymIdFlags',
        '__httpuri_etsi_orgm2m_ConnectionParamSet_httpuri_etsi_orgm2msecuritymIdFlags',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
            32, 4), )

    securitymIdFlags = property(__securitymIdFlags.value,
                                __securitymIdFlags.set, None, None)


    # Element {http://uri.etsi.org/m2m}securityConnectionId uses Python identifier securityConnectionId
    __securityConnectionId = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'securityConnectionId'),
        'securityConnectionId',
        '__httpuri_etsi_orgm2m_ConnectionParamSet_httpuri_etsi_orgm2msecurityConnectionId',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
            48, 4), )

    securityConnectionId = property(__securityConnectionId.value,
                                    __securityConnectionId.set, None, None)

    _ElementMap.update({
        __sclId.name(): __sclId,
        __securityLifetime.name(): __securityLifetime,
        __securityEncryptedM2MKey.name(): __securityEncryptedM2MKey,
        __securityKmcIndex.name(): __securityKmcIndex,
        __securitymIdFlags.name(): __securitymIdFlags,
        __securityConnectionId.name(): __securityConnectionId
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'ConnectionParamSet',
                            ConnectionParamSet)


# Complex type {http://uri.etsi.org/m2m}Container with content type ELEMENT_ONLY
class Container(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}Container with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Container')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd', 10,
        4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_Container_httpuri_etsi_orgm2maccessRightID',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_Container_httpuri_etsi_orgm2mcreationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_Container_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}expirationTime uses Python identifier expirationTime
    __expirationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
        'expirationTime',
        '__httpuri_etsi_orgm2m_Container_httpuri_etsi_orgm2mexpirationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            16, 4), )

    expirationTime = property(__expirationTime.value, __expirationTime.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}searchStrings uses Python identifier searchStrings
    __searchStrings = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings'),
        'searchStrings',
        '__httpuri_etsi_orgm2m_Container_httpuri_etsi_orgm2msearchStrings',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            18, 4), )

    searchStrings = property(__searchStrings.value, __searchStrings.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}announceTo uses Python identifier announceTo
    __announceTo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'announceTo'), 'announceTo',
        '__httpuri_etsi_orgm2m_Container_httpuri_etsi_orgm2mannounceTo', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            58, 4), )

    announceTo = property(__announceTo.value, __announceTo.set, None, None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_Container_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}contentInstancesReference uses Python identifier contentInstancesReference
    __contentInstancesReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'contentInstancesReference'),
        'contentInstancesReference',
        '__httpuri_etsi_orgm2m_Container_httpuri_etsi_orgm2mcontentInstancesReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            86, 4), )

    contentInstancesReference = property(__contentInstancesReference.value,
                                         __contentInstancesReference.set, None,
                                         None)


    # Element {http://uri.etsi.org/m2m}subcontainersReference uses Python identifier subcontainersReference
    __subcontainersReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subcontainersReference'),
        'subcontainersReference',
        '__httpuri_etsi_orgm2m_Container_httpuri_etsi_orgm2msubcontainersReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            87, 4), )

    subcontainersReference = property(__subcontainersReference.value,
                                      __subcontainersReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}maxNrOfInstances uses Python identifier maxNrOfInstances
    __maxNrOfInstances = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'maxNrOfInstances'),
        'maxNrOfInstances',
        '__httpuri_etsi_orgm2m_Container_httpuri_etsi_orgm2mmaxNrOfInstances',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
            30, 4), )

    maxNrOfInstances = property(__maxNrOfInstances.value,
                                __maxNrOfInstances.set, None, None)


    # Element {http://uri.etsi.org/m2m}maxByteSize uses Python identifier maxByteSize
    __maxByteSize = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'maxByteSize'), 'maxByteSize',
        '__httpuri_etsi_orgm2m_Container_httpuri_etsi_orgm2mmaxByteSize', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
            31, 4), )

    maxByteSize = property(__maxByteSize.value, __maxByteSize.set, None, None)


    # Element {http://uri.etsi.org/m2m}maxInstanceAge uses Python identifier maxInstanceAge
    __maxInstanceAge = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'maxInstanceAge'),
        'maxInstanceAge',
        '__httpuri_etsi_orgm2m_Container_httpuri_etsi_orgm2mmaxInstanceAge',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
            32, 4), )

    maxInstanceAge = property(__maxInstanceAge.value, __maxInstanceAge.set,
                              None, None)


    # Attribute {http://uri.etsi.org/m2m}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_Container_httpuri_etsi_orgm2mid',
        pyxb.binding.datatypes.NMTOKEN)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 8, 4)
    __id._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd', 27,
        8)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __expirationTime.name(): __expirationTime,
        __searchStrings.name(): __searchStrings,
        __announceTo.name(): __announceTo,
        __subscriptionsReference.name(): __subscriptionsReference,
        __contentInstancesReference.name(): __contentInstancesReference,
        __subcontainersReference.name(): __subcontainersReference,
        __maxNrOfInstances.name(): __maxNrOfInstances,
        __maxByteSize.name(): __maxByteSize,
        __maxInstanceAge.name(): __maxInstanceAge
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'Container', Container)


# Complex type {http://uri.etsi.org/m2m}ContainerAnnc with content type ELEMENT_ONLY
class ContainerAnnc(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ContainerAnnc with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ContainerAnnc')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containerAnnc.xsd',
        10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_ContainerAnnc_httpuri_etsi_orgm2maccessRightID',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}expirationTime uses Python identifier expirationTime
    __expirationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
        'expirationTime',
        '__httpuri_etsi_orgm2m_ContainerAnnc_httpuri_etsi_orgm2mexpirationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            16, 4), )

    expirationTime = property(__expirationTime.value, __expirationTime.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}searchStrings uses Python identifier searchStrings
    __searchStrings = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings'),
        'searchStrings',
        '__httpuri_etsi_orgm2m_ContainerAnnc_httpuri_etsi_orgm2msearchStrings',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            18, 4), )

    searchStrings = property(__searchStrings.value, __searchStrings.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}announceTo uses Python identifier announceTo
    __announceTo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'announceTo'), 'announceTo',
        '__httpuri_etsi_orgm2m_ContainerAnnc_httpuri_etsi_orgm2mannounceTo',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            58, 4), )

    announceTo = property(__announceTo.value, __announceTo.set, None, None)


    # Element {http://uri.etsi.org/m2m}link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'link'), 'link',
        '__httpuri_etsi_orgm2m_ContainerAnnc_httpuri_etsi_orgm2mlink', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            74, 4), )

    link = property(__link.value, __link.set, None, None)


    # Attribute {http://uri.etsi.org/m2m}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_ContainerAnnc_httpuri_etsi_orgm2mid',
        pyxb.binding.datatypes.NMTOKEN)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 8, 4)
    __id._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containerAnnc.xsd',
        18, 8)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __expirationTime.name(): __expirationTime,
        __searchStrings.name(): __searchStrings,
        __announceTo.name(): __announceTo,
        __link.name(): __link
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'ContainerAnnc', ContainerAnnc)


# Complex type {http://uri.etsi.org/m2m}Containers with content type ELEMENT_ONLY
class Containers(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}Containers with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Containers')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd', 10,
        4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_Containers_httpuri_etsi_orgm2maccessRightID',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_Containers_httpuri_etsi_orgm2mcreationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_Containers_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_Containers_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}containerCollection uses Python identifier containerCollection
    __containerCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'containerCollection'),
        'containerCollection',
        '__httpuri_etsi_orgm2m_Containers_httpuri_etsi_orgm2mcontainerCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd',
            24, 4), )

    containerCollection = property(__containerCollection.value,
                                   __containerCollection.set, None, None)


    # Element {http://uri.etsi.org/m2m}containerAnncCollection uses Python identifier containerAnncCollection
    __containerAnncCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'containerAnncCollection'),
        'containerAnncCollection',
        '__httpuri_etsi_orgm2m_Containers_httpuri_etsi_orgm2mcontainerAnncCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd',
            25, 4), )

    containerAnncCollection = property(__containerAnncCollection.value,
                                       __containerAnncCollection.set, None,
                                       None)


    # Element {http://uri.etsi.org/m2m}locationContainerCollection uses Python identifier locationContainerCollection
    __locationContainerCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'locationContainerCollection'),
        'locationContainerCollection',
        '__httpuri_etsi_orgm2m_Containers_httpuri_etsi_orgm2mlocationContainerCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd',
            27, 4), )

    locationContainerCollection = property(__locationContainerCollection.value,
                                           __locationContainerCollection.set,
                                           None, None)


    # Element {http://uri.etsi.org/m2m}locationContainerAnncCollection uses Python identifier locationContainerAnncCollection
    __locationContainerAnncCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace,
                                    u'locationContainerAnncCollection'),
        'locationContainerAnncCollection',
        '__httpuri_etsi_orgm2m_Containers_httpuri_etsi_orgm2mlocationContainerAnncCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd',
            29, 4), )

    locationContainerAnncCollection = property(
        __locationContainerAnncCollection.value,
        __locationContainerAnncCollection.set, None, None)

    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __subscriptionsReference.name(): __subscriptionsReference,
        __containerCollection.name(): __containerCollection,
        __containerAnncCollection.name(): __containerAnncCollection,
        __locationContainerCollection.name(): __locationContainerCollection,
        __locationContainerAnncCollection.name(): __locationContainerAnncCollection
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'Containers', Containers)


# Complex type {http://uri.etsi.org/m2m}ContentInstance with content type ELEMENT_ONLY
class ContentInstance(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ContentInstance with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ContentInstance')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
        14, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_ContentInstance_httpuri_etsi_orgm2mcreationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_ContentInstance_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}searchStrings uses Python identifier searchStrings
    __searchStrings = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings'),
        'searchStrings',
        '__httpuri_etsi_orgm2m_ContentInstance_httpuri_etsi_orgm2msearchStrings',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            18, 4), )

    searchStrings = property(__searchStrings.value, __searchStrings.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}delayTolerance uses Python identifier delayTolerance
    __delayTolerance = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'delayTolerance'),
        'delayTolerance',
        '__httpuri_etsi_orgm2m_ContentInstance_httpuri_etsi_orgm2mdelayTolerance',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            72, 4), )

    delayTolerance = property(__delayTolerance.value, __delayTolerance.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}content uses Python identifier content_
    __content = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'content'), 'content_',
        '__httpuri_etsi_orgm2m_ContentInstance_httpuri_etsi_orgm2mcontent',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
            28, 4), )

    content_ = property(__content.value, __content.set, None, None)


    # Element {http://uri.etsi.org/m2m}contentSize uses Python identifier contentSize
    __contentSize = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'contentSize'), 'contentSize',
        '__httpuri_etsi_orgm2m_ContentInstance_httpuri_etsi_orgm2mcontentSize',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
            40, 4), )

    contentSize = property(__contentSize.value, __contentSize.set, None, None)


    # Element {http://uri.etsi.org/m2m}contentTypes uses Python identifier contentTypes
    __contentTypes = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'contentTypes'), 'contentTypes',
        '__httpuri_etsi_orgm2m_ContentInstance_httpuri_etsi_orgm2mcontentTypes',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
            41, 4), )

    contentTypes = property(__contentTypes.value, __contentTypes.set, None,
                            None)


    # Attribute {http://uri.etsi.org/m2m}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_ContentInstance_httpuri_etsi_orgm2mid',
        pyxb.binding.datatypes.NMTOKEN)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 8, 4)
    __id._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
        24, 8)

    id = property(__id.value, __id.set, None, None)


    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'href'), 'href',
        '__httpuri_etsi_orgm2m_ContentInstance_href',
        pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
        25, 8)
    __href._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
        25, 8)

    href = property(__href.value, __href.set, None, None)

    _ElementMap.update({
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __searchStrings.name(): __searchStrings,
        __delayTolerance.name(): __delayTolerance,
        __content.name(): __content,
        __contentSize.name(): __contentSize,
        __contentTypes.name(): __contentTypes
    })
    _AttributeMap.update({
        __id.name(): __id,
        __href.name(): __href
    })


Namespace.addCategoryObject('typeBinding', u'ContentInstance', ContentInstance)


# Complex type {http://uri.etsi.org/m2m}ContentTypes with content type ELEMENT_ONLY
class ContentTypes(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ContentTypes with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ContentTypes')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
        43, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}contentType uses Python identifier contentType
    __contentType = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'contentType'), 'contentType',
        '__httpuri_etsi_orgm2m_ContentTypes_httpuri_etsi_orgm2mcontentType',
        True, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            106, 4), )

    contentType = property(__contentType.value, __contentType.set, None, None)

    _ElementMap.update({
        __contentType.name(): __contentType
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'ContentTypes', ContentTypes)


# Complex type {http://uri.etsi.org/m2m}ContentInstances with content type ELEMENT_ONLY
class ContentInstances(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ContentInstances with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ContentInstances')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
        11, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_ContentInstances_httpuri_etsi_orgm2mcreationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_ContentInstances_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_ContentInstances_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}currentNrOfInstances uses Python identifier currentNrOfInstances
    __currentNrOfInstances = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'currentNrOfInstances'),
        'currentNrOfInstances',
        '__httpuri_etsi_orgm2m_ContentInstances_httpuri_etsi_orgm2mcurrentNrOfInstances',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
            25, 4), )

    currentNrOfInstances = property(__currentNrOfInstances.value,
                                    __currentNrOfInstances.set, None, None)


    # Element {http://uri.etsi.org/m2m}currentByteSize uses Python identifier currentByteSize
    __currentByteSize = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'currentByteSize'),
        'currentByteSize',
        '__httpuri_etsi_orgm2m_ContentInstances_httpuri_etsi_orgm2mcurrentByteSize',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
            26, 4), )

    currentByteSize = property(__currentByteSize.value, __currentByteSize.set,
                               None, None)


    # Element {http://uri.etsi.org/m2m}latest uses Python identifier latest
    __latest = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'latest'), 'latest',
        '__httpuri_etsi_orgm2m_ContentInstances_httpuri_etsi_orgm2mlatest',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
            28, 4), )

    latest = property(__latest.value, __latest.set, None, None)


    # Element {http://uri.etsi.org/m2m}oldest uses Python identifier oldest
    __oldest = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'oldest'), 'oldest',
        '__httpuri_etsi_orgm2m_ContentInstances_httpuri_etsi_orgm2moldest',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
            29, 4), )

    oldest = property(__oldest.value, __oldest.set, None, None)


    # Element {http://uri.etsi.org/m2m}contentInstanceCollection uses Python identifier contentInstanceCollection
    __contentInstanceCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'contentInstanceCollection'),
        'contentInstanceCollection',
        '__httpuri_etsi_orgm2m_ContentInstances_httpuri_etsi_orgm2mcontentInstanceCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
            31, 4), )

    contentInstanceCollection = property(__contentInstanceCollection.value,
                                         __contentInstanceCollection.set, None,
                                         None)

    _ElementMap.update({
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __subscriptionsReference.name(): __subscriptionsReference,
        __currentNrOfInstances.name(): __currentNrOfInstances,
        __currentByteSize.name(): __currentByteSize,
        __latest.name(): __latest,
        __oldest.name(): __oldest,
        __contentInstanceCollection.name(): __contentInstanceCollection
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'ContentInstances',
                            ContentInstances)


# Complex type {http://uri.etsi.org/m2m}ContentInstanceCollection with content type ELEMENT_ONLY
class ContentInstanceCollection(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ContentInstanceCollection with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'ContentInstanceCollection')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
        34, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}contentInstance uses Python identifier contentInstance
    __contentInstance = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'contentInstance'),
        'contentInstance',
        '__httpuri_etsi_orgm2m_ContentInstanceCollection_httpuri_etsi_orgm2mcontentInstance',
        True, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
            12, 4), )

    contentInstance = property(__contentInstance.value, __contentInstance.set,
                               None, None)

    _ElementMap.update({
        __contentInstance.name(): __contentInstance
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'ContentInstanceCollection',
                            ContentInstanceCollection)


# Complex type {http://uri.etsi.org/m2m}Discovery with content type ELEMENT_ONLY
class Discovery(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}Discovery with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Discovery')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/discovery.xsd', 8,
        4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}matchSize uses Python identifier matchSize
    __matchSize = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'matchSize'), 'matchSize',
        '__httpuri_etsi_orgm2m_Discovery_httpuri_etsi_orgm2mmatchSize', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/discovery.xsd',
            15, 4), )

    matchSize = property(__matchSize.value, __matchSize.set, None, None)


    # Element {http://uri.etsi.org/m2m}truncated uses Python identifier truncated
    __truncated = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'truncated'), 'truncated',
        '__httpuri_etsi_orgm2m_Discovery_httpuri_etsi_orgm2mtruncated', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/discovery.xsd',
            16, 4), )

    truncated = property(__truncated.value, __truncated.set, None, None)


    # Element {http://uri.etsi.org/m2m}discoveryURI uses Python identifier discoveryURI
    __discoveryURI = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'discoveryURI'), 'discoveryURI',
        '__httpuri_etsi_orgm2m_Discovery_httpuri_etsi_orgm2mdiscoveryURI',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/discovery.xsd',
            17, 4), )

    discoveryURI = property(__discoveryURI.value, __discoveryURI.set, None,
                            None)

    _ElementMap.update({
        __matchSize.name(): __matchSize,
        __truncated.name(): __truncated,
        __discoveryURI.name(): __discoveryURI
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'Discovery', Discovery)


# Complex type {http://uri.etsi.org/m2m}ErrorInfo with content type ELEMENT_ONLY
class ErrorInfo(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ErrorInfo with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ErrorInfo')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/errorInfo.xsd', 10,
        4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}statusCode uses Python identifier statusCode
    __statusCode = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'statusCode'), 'statusCode',
        '__httpuri_etsi_orgm2m_ErrorInfo_httpuri_etsi_orgm2mstatusCode', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            186, 4), )

    statusCode = property(__statusCode.value, __statusCode.set, None, None)


    # Element {http://uri.etsi.org/m2m}additionalInfo uses Python identifier additionalInfo
    __additionalInfo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'additionalInfo'),
        'additionalInfo',
        '__httpuri_etsi_orgm2m_ErrorInfo_httpuri_etsi_orgm2madditionalInfo',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/errorInfo.xsd',
            17, 4), )

    additionalInfo = property(__additionalInfo.value, __additionalInfo.set,
                              None, None)

    _ElementMap.update({
        __statusCode.name(): __statusCode,
        __additionalInfo.name(): __additionalInfo
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'ErrorInfo', ErrorInfo)


# Complex type {http://uri.etsi.org/m2m}LogDataFile with content type ELEMENT_ONLY
class LogDataFile(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}LogDataFile with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LogDataFile')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerformanceLog.xsd',
        33, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'LogDataFile', LogDataFile)


# Complex type {http://uri.etsi.org/m2m}RankedAnList with content type ELEMENT_ONLY
class RankedAnList(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}RankedAnList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RankedAnList')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
        30, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessNetwork uses Python identifier accessNetwork
    __accessNetwork = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessNetwork'),
        'accessNetwork',
        '__httpuri_etsi_orgm2m_RankedAnList_httpuri_etsi_orgm2maccessNetwork',
        True, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
            37, 4), )

    accessNetwork = property(__accessNetwork.value, __accessNetwork.set, None,
                             None)


    # Attribute {http://uri.etsi.org/m2m}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_RankedAnList_httpuri_etsi_orgm2mid',
        pyxb.binding.datatypes.NMTOKEN, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 8, 4)
    __id._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
        35, 8)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __accessNetwork.name(): __accessNetwork
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'RankedAnList', RankedAnList)


# Complex type {http://uri.etsi.org/m2m}OccuredEvents with content type ELEMENT_ONLY
class OccuredEvents(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}OccuredEvents with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'OccuredEvents')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
        33, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element currentIndex uses Python identifier currentIndex
    __currentIndex = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'currentIndex'), 'currentIndex',
        '__httpuri_etsi_orgm2m_OccuredEvents_currentIndex', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
            35, 12), )

    currentIndex = property(__currentIndex.value, __currentIndex.set, None,
                            u'Indicates the rank of the last occured event\n                        in the table of timeStamps.\n                    ')


    # Element trapEventTimeStamp uses Python identifier trapEventTimeStamp
    __trapEventTimeStamp = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'trapEventTimeStamp'),
        'trapEventTimeStamp',
        '__httpuri_etsi_orgm2m_OccuredEvents_trapEventTimeStamp', True,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
            42, 12), )

    trapEventTimeStamp = property(__trapEventTimeStamp.value,
                                  __trapEventTimeStamp.set, None,
                                  u'It is a circular buffer of timeStamps of the\n                        last occured events. The number of logged events is\n                        limited to 100.\n                    ')

    _ElementMap.update({
        __currentIndex.name(): __currentIndex,
        __trapEventTimeStamp.name(): __trapEventTimeStamp
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'OccuredEvents', OccuredEvents)


# Complex type {http://uri.etsi.org/m2m}ExecInstance with content type ELEMENT_ONLY
class ExecInstance(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ExecInstance with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExecInstance')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
        10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_ExecInstance_httpuri_etsi_orgm2maccessRightID',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_ExecInstance_httpuri_etsi_orgm2mcreationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_ExecInstance_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}expirationTime uses Python identifier expirationTime
    __expirationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
        'expirationTime',
        '__httpuri_etsi_orgm2m_ExecInstance_httpuri_etsi_orgm2mexpirationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            16, 4), )

    expirationTime = property(__expirationTime.value, __expirationTime.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_ExecInstance_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}execStatus uses Python identifier execStatus
    __execStatus = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'execStatus'), 'execStatus',
        '__httpuri_etsi_orgm2m_ExecInstance_httpuri_etsi_orgm2mexecStatus',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
            29, 4), )

    execStatus = property(__execStatus.value, __execStatus.set, None, None)


    # Element {http://uri.etsi.org/m2m}execDisable uses Python identifier execDisable
    __execDisable = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'execDisable'), 'execDisable',
        '__httpuri_etsi_orgm2m_ExecInstance_httpuri_etsi_orgm2mexecDisable',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
            30, 4), )

    execDisable = property(__execDisable.value, __execDisable.set, None, None)


    # Element {http://uri.etsi.org/m2m}execResult uses Python identifier execResult
    __execResult = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'execResult'), 'execResult',
        '__httpuri_etsi_orgm2m_ExecInstance_httpuri_etsi_orgm2mexecResult',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
            42, 4), )

    execResult = property(__execResult.value, __execResult.set, None, None)


    # Attribute {http://uri.etsi.org/m2m}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_ExecInstance_httpuri_etsi_orgm2mid',
        pyxb.binding.datatypes.NMTOKEN)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 8, 4)
    __id._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
        26, 8)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __expirationTime.name(): __expirationTime,
        __subscriptionsReference.name(): __subscriptionsReference,
        __execStatus.name(): __execStatus,
        __execDisable.name(): __execDisable,
        __execResult.name(): __execResult
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'ExecInstance', ExecInstance)


# Complex type {http://uri.etsi.org/m2m}ExecResultList with content type ELEMENT_ONLY
class ExecResultList(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ExecResultList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExecResultList')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
        43, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element execResultItem uses Python identifier execResultItem
    __execResultItem = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'execResultItem'), 'execResultItem',
        '__httpuri_etsi_orgm2m_ExecResultList_execResultItem', True,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
            45, 12), )

    execResultItem = property(__execResultItem.value, __execResultItem.set,
                              None, None)

    _ElementMap.update({
        __execResultItem.name(): __execResultItem
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'ExecResultList', ExecResultList)


# Complex type {http://uri.etsi.org/m2m}ExecResultItem with content type ELEMENT_ONLY
class ExecResultItem(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ExecResultItem with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExecResultItem')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
        50, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'name'), 'name',
        '__httpuri_etsi_orgm2m_ExecResultItem_name', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
            52, 12), )

    name = property(__name.value, __name.set, None, None)


    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'value'), 'value_',
        '__httpuri_etsi_orgm2m_ExecResultItem_value', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
            53, 12), )

    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        __name.name(): __name,
        __value.name(): __value
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'ExecResultItem', ExecResultItem)


# Complex type {http://uri.etsi.org/m2m}ExecInstances with content type ELEMENT_ONLY
class ExecInstances(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ExecInstances with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExecInstances')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstances.xsd',
        11, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_ExecInstances_httpuri_etsi_orgm2mcreationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_ExecInstances_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_ExecInstances_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}execInstanceCollection uses Python identifier execInstanceCollection
    __execInstanceCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'execInstanceCollection'),
        'execInstanceCollection',
        '__httpuri_etsi_orgm2m_ExecInstances_httpuri_etsi_orgm2mexecInstanceCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstances.xsd',
            24, 4), )

    execInstanceCollection = property(__execInstanceCollection.value,
                                      __execInstanceCollection.set, None, None)


    # Attribute {http://uri.etsi.org/m2m}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_ExecInstances_httpuri_etsi_orgm2mid',
        pyxb.binding.datatypes.NMTOKEN)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 8, 4)
    __id._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstances.xsd',
        21, 8)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __subscriptionsReference.name(): __subscriptionsReference,
        __execInstanceCollection.name(): __execInstanceCollection
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'ExecInstances', ExecInstances)


# Complex type {http://uri.etsi.org/m2m}Group with content type ELEMENT_ONLY
class Group(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}Group with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Group')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 16, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_Group_httpuri_etsi_orgm2maccessRightID', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_Group_httpuri_etsi_orgm2mcreationTime', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_Group_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}expirationTime uses Python identifier expirationTime
    __expirationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
        'expirationTime',
        '__httpuri_etsi_orgm2m_Group_httpuri_etsi_orgm2mexpirationTime', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            16, 4), )

    expirationTime = property(__expirationTime.value, __expirationTime.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}searchStrings uses Python identifier searchStrings
    __searchStrings = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings'),
        'searchStrings',
        '__httpuri_etsi_orgm2m_Group_httpuri_etsi_orgm2msearchStrings', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            18, 4), )

    searchStrings = property(__searchStrings.value, __searchStrings.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}announceTo uses Python identifier announceTo
    __announceTo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'announceTo'), 'announceTo',
        '__httpuri_etsi_orgm2m_Group_httpuri_etsi_orgm2mannounceTo', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            58, 4), )

    announceTo = property(__announceTo.value, __announceTo.set, None, None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_Group_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}membersContentAccessRightID uses Python identifier membersContentAccessRightID
    __membersContentAccessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'membersContentAccessRightID'),
        'membersContentAccessRightID',
        '__httpuri_etsi_orgm2m_Group_httpuri_etsi_orgm2mmembersContentAccessRightID',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 14,
            4), )

    membersContentAccessRightID = property(__membersContentAccessRightID.value,
                                           __membersContentAccessRightID.set,
                                           None, None)


    # Element {http://uri.etsi.org/m2m}memberType uses Python identifier memberType
    __memberType = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'memberType'), 'memberType',
        '__httpuri_etsi_orgm2m_Group_httpuri_etsi_orgm2mmemberType', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 38,
            4), )

    memberType = property(__memberType.value, __memberType.set, None, None)


    # Element {http://uri.etsi.org/m2m}currentNrOfMembers uses Python identifier currentNrOfMembers
    __currentNrOfMembers = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'currentNrOfMembers'),
        'currentNrOfMembers',
        '__httpuri_etsi_orgm2m_Group_httpuri_etsi_orgm2mcurrentNrOfMembers',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 39,
            4), )

    currentNrOfMembers = property(__currentNrOfMembers.value,
                                  __currentNrOfMembers.set, None, None)


    # Element {http://uri.etsi.org/m2m}maxNrOfMembers uses Python identifier maxNrOfMembers
    __maxNrOfMembers = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'maxNrOfMembers'),
        'maxNrOfMembers',
        '__httpuri_etsi_orgm2m_Group_httpuri_etsi_orgm2mmaxNrOfMembers', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 40,
            4), )

    maxNrOfMembers = property(__maxNrOfMembers.value, __maxNrOfMembers.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}members uses Python identifier members
    __members = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'members'), 'members',
        '__httpuri_etsi_orgm2m_Group_httpuri_etsi_orgm2mmembers', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 41,
            4), )

    members = property(__members.value, __members.set, None, None)


    # Element {http://uri.etsi.org/m2m}memberTypeValidated uses Python identifier memberTypeValidated
    __memberTypeValidated = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'memberTypeValidated'),
        'memberTypeValidated',
        '__httpuri_etsi_orgm2m_Group_httpuri_etsi_orgm2mmemberTypeValidated',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 42,
            4), )

    memberTypeValidated = property(__memberTypeValidated.value,
                                   __memberTypeValidated.set, None, None)


    # Element {http://uri.etsi.org/m2m}consistencyStrategy uses Python identifier consistencyStrategy
    __consistencyStrategy = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'consistencyStrategy'),
        'consistencyStrategy',
        '__httpuri_etsi_orgm2m_Group_httpuri_etsi_orgm2mconsistencyStrategy',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 43,
            4), )

    consistencyStrategy = property(__consistencyStrategy.value,
                                   __consistencyStrategy.set, None, None)


    # Element {http://uri.etsi.org/m2m}membersContentReference uses Python identifier membersContentReference
    __membersContentReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'membersContentReference'),
        'membersContentReference',
        '__httpuri_etsi_orgm2m_Group_httpuri_etsi_orgm2mmembersContentReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 45,
            4), )

    membersContentReference = property(__membersContentReference.value,
                                       __membersContentReference.set, None,
                                       None)


    # Attribute {http://uri.etsi.org/m2m}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_Group_httpuri_etsi_orgm2mid',
        pyxb.binding.datatypes.NMTOKEN)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 8, 4)
    __id._UseLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 35, 8)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __expirationTime.name(): __expirationTime,
        __searchStrings.name(): __searchStrings,
        __announceTo.name(): __announceTo,
        __subscriptionsReference.name(): __subscriptionsReference,
        __membersContentAccessRightID.name(): __membersContentAccessRightID,
        __memberType.name(): __memberType,
        __currentNrOfMembers.name(): __currentNrOfMembers,
        __maxNrOfMembers.name(): __maxNrOfMembers,
        __members.name(): __members,
        __memberTypeValidated.name(): __memberTypeValidated,
        __consistencyStrategy.name(): __consistencyStrategy,
        __membersContentReference.name(): __membersContentReference
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'Group', Group)


# Complex type {http://uri.etsi.org/m2m}GroupAnnc with content type ELEMENT_ONLY
class GroupAnnc(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}GroupAnnc with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'GroupAnnc')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groupAnnc.xsd', 10,
        4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_GroupAnnc_httpuri_etsi_orgm2maccessRightID',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}expirationTime uses Python identifier expirationTime
    __expirationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
        'expirationTime',
        '__httpuri_etsi_orgm2m_GroupAnnc_httpuri_etsi_orgm2mexpirationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            16, 4), )

    expirationTime = property(__expirationTime.value, __expirationTime.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}searchStrings uses Python identifier searchStrings
    __searchStrings = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings'),
        'searchStrings',
        '__httpuri_etsi_orgm2m_GroupAnnc_httpuri_etsi_orgm2msearchStrings',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            18, 4), )

    searchStrings = property(__searchStrings.value, __searchStrings.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}announceTo uses Python identifier announceTo
    __announceTo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'announceTo'), 'announceTo',
        '__httpuri_etsi_orgm2m_GroupAnnc_httpuri_etsi_orgm2mannounceTo', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            58, 4), )

    announceTo = property(__announceTo.value, __announceTo.set, None, None)


    # Element {http://uri.etsi.org/m2m}link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'link'), 'link',
        '__httpuri_etsi_orgm2m_GroupAnnc_httpuri_etsi_orgm2mlink', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            74, 4), )

    link = property(__link.value, __link.set, None, None)


    # Attribute {http://uri.etsi.org/m2m}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_GroupAnnc_httpuri_etsi_orgm2mid',
        pyxb.binding.datatypes.NMTOKEN)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 8, 4)
    __id._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groupAnnc.xsd', 18,
        8)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __expirationTime.name(): __expirationTime,
        __searchStrings.name(): __searchStrings,
        __announceTo.name(): __announceTo,
        __link.name(): __link
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'GroupAnnc', GroupAnnc)


# Complex type {http://uri.etsi.org/m2m}Groups with content type ELEMENT_ONLY
class Groups(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}Groups with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Groups')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groups.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_Groups_httpuri_etsi_orgm2maccessRightID', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_Groups_httpuri_etsi_orgm2mcreationTime', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_Groups_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_Groups_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}groupCollection uses Python identifier groupCollection
    __groupCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'groupCollection'),
        'groupCollection',
        '__httpuri_etsi_orgm2m_Groups_httpuri_etsi_orgm2mgroupCollection',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groups.xsd',
            22, 4), )

    groupCollection = property(__groupCollection.value, __groupCollection.set,
                               None, None)


    # Element {http://uri.etsi.org/m2m}groupAnncCollection uses Python identifier groupAnncCollection
    __groupAnncCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'groupAnncCollection'),
        'groupAnncCollection',
        '__httpuri_etsi_orgm2m_Groups_httpuri_etsi_orgm2mgroupAnncCollection',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groups.xsd',
            23, 4), )

    groupAnncCollection = property(__groupAnncCollection.value,
                                   __groupAnncCollection.set, None, None)

    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __subscriptionsReference.name(): __subscriptionsReference,
        __groupCollection.name(): __groupCollection,
        __groupAnncCollection.name(): __groupAnncCollection
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'Groups', Groups)


# Complex type {http://uri.etsi.org/m2m}LocationContainerAnnc with content type ELEMENT_ONLY
class LocationContainerAnnc(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}LocationContainerAnnc with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'LocationContainerAnnc')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/locationContainerAnnc.xsd',
        10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_LocationContainerAnnc_httpuri_etsi_orgm2maccessRightID',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}expirationTime uses Python identifier expirationTime
    __expirationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
        'expirationTime',
        '__httpuri_etsi_orgm2m_LocationContainerAnnc_httpuri_etsi_orgm2mexpirationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            16, 4), )

    expirationTime = property(__expirationTime.value, __expirationTime.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}searchStrings uses Python identifier searchStrings
    __searchStrings = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings'),
        'searchStrings',
        '__httpuri_etsi_orgm2m_LocationContainerAnnc_httpuri_etsi_orgm2msearchStrings',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            18, 4), )

    searchStrings = property(__searchStrings.value, __searchStrings.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}announceTo uses Python identifier announceTo
    __announceTo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'announceTo'), 'announceTo',
        '__httpuri_etsi_orgm2m_LocationContainerAnnc_httpuri_etsi_orgm2mannounceTo',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            58, 4), )

    announceTo = property(__announceTo.value, __announceTo.set, None, None)


    # Element {http://uri.etsi.org/m2m}link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'link'), 'link',
        '__httpuri_etsi_orgm2m_LocationContainerAnnc_httpuri_etsi_orgm2mlink',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            74, 4), )

    link = property(__link.value, __link.set, None, None)


    # Attribute {http://uri.etsi.org/m2m}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_LocationContainerAnnc_httpuri_etsi_orgm2mid',
        pyxb.binding.datatypes.NMTOKEN)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 8, 4)
    __id._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/locationContainerAnnc.xsd',
        18, 8)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __expirationTime.name(): __expirationTime,
        __searchStrings.name(): __searchStrings,
        __announceTo.name(): __announceTo,
        __link.name(): __link
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'LocationContainerAnnc',
                            LocationContainerAnnc)


# Complex type {http://uri.etsi.org/m2m}M2MPoc with content type ELEMENT_ONLY
class M2MPoc(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}M2MPoc with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'M2MPoc')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_M2MPoc_httpuri_etsi_orgm2mcreationTime', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_M2MPoc_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}expirationTime uses Python identifier expirationTime
    __expirationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
        'expirationTime',
        '__httpuri_etsi_orgm2m_M2MPoc_httpuri_etsi_orgm2mexpirationTime', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            16, 4), )

    expirationTime = property(__expirationTime.value, __expirationTime.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}onlineStatus uses Python identifier onlineStatus
    __onlineStatus = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'onlineStatus'), 'onlineStatus',
        '__httpuri_etsi_orgm2m_M2MPoc_httpuri_etsi_orgm2monlineStatus', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            126, 4), )

    onlineStatus = property(__onlineStatus.value, __onlineStatus.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}contactInfo uses Python identifier contactInfo
    __contactInfo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'contactInfo'), 'contactInfo',
        '__httpuri_etsi_orgm2m_M2MPoc_httpuri_etsi_orgm2mcontactInfo', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd', 23,
            4), )

    contactInfo = property(__contactInfo.value, __contactInfo.set, None, None)


    # Attribute {http://uri.etsi.org/m2m}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_M2MPoc_httpuri_etsi_orgm2mid',
        pyxb.binding.datatypes.NMTOKEN)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 8, 4)
    __id._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd', 20, 8)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __expirationTime.name(): __expirationTime,
        __onlineStatus.name(): __onlineStatus,
        __contactInfo.name(): __contactInfo
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'M2MPoc', M2MPoc)


# Complex type {http://uri.etsi.org/m2m}ContactInfo with content type ELEMENT_ONLY
class ContactInfo(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ContactInfo with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ContactInfo')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd', 24, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}contactURI uses Python identifier contactURI
    __contactURI = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'contactURI'), 'contactURI',
        '__httpuri_etsi_orgm2m_ContactInfo_httpuri_etsi_orgm2mcontactURI',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            136, 4), )

    contactURI = property(__contactURI.value, __contactURI.set, None, None)


    # Element {http://uri.etsi.org/m2m}other uses Python identifier other
    __other = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'other'), 'other',
        '__httpuri_etsi_orgm2m_ContactInfo_httpuri_etsi_orgm2mother', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd', 32,
            4), )

    other = property(__other.value, __other.set, None, None)

    _ElementMap.update({
        __contactURI.name(): __contactURI,
        __other.name(): __other
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'ContactInfo', ContactInfo)


# Complex type {http://uri.etsi.org/m2m}M2MPocs with content type ELEMENT_ONLY
class M2MPocs(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}M2MPocs with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'M2MPocs')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPocs.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_M2MPocs_httpuri_etsi_orgm2mcreationTime', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_M2MPocs_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}m2mPocCollection uses Python identifier m2mPocCollection
    __m2mPocCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'm2mPocCollection'),
        'm2mPocCollection',
        '__httpuri_etsi_orgm2m_M2MPocs_httpuri_etsi_orgm2mm2mPocCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPocs.xsd',
            19, 4), )

    m2mPocCollection = property(__m2mPocCollection.value,
                                __m2mPocCollection.set, None, None)

    _ElementMap.update({
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __m2mPocCollection.name(): __m2mPocCollection
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'M2MPocs', M2MPocs)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MembersContent')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
        13, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'status'), 'status',
        '__httpuri_etsi_orgm2m_CTD_ANON__status', True,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
            15, 16), )

    status = property(__status.value, __status.set, None, None)

    _ElementMap.update({
        __status.name(): __status
    })
    _AttributeMap.update({

    })


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
        16, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element statusCode uses Python identifier statusCode
    __statusCode = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'statusCode'), 'statusCode',
        '__httpuri_etsi_orgm2m_CTD_ANON_2_statusCode', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
            18, 28), )

    statusCode = property(__statusCode.value, __statusCode.set, None, None)


    # Element eTag uses Python identifier eTag
    __eTag = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'eTag'), 'eTag',
        '__httpuri_etsi_orgm2m_CTD_ANON_2_eTag', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
            19, 28), )

    eTag = property(__eTag.value, __eTag.set, None, None)


    # Element resourceURI uses Python identifier resourceURI
    __resourceURI = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'resourceURI'), 'resourceURI',
        '__httpuri_etsi_orgm2m_CTD_ANON_2_resourceURI', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
            20, 28), )

    resourceURI = property(__resourceURI.value, __resourceURI.set, None, None)


    # Element lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'lastModifiedTime'),
        'lastModifiedTime', '__httpuri_etsi_orgm2m_CTD_ANON_2_lastModifiedTime',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
            21, 28), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element resultBody uses Python identifier resultBody
    __resultBody = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'resultBody'), 'resultBody',
        '__httpuri_etsi_orgm2m_CTD_ANON_2_resultBody', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
            23, 28), )

    resultBody = property(__resultBody.value, __resultBody.set, None, None)


    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_CTD_ANON_2_id', pyxb.binding.datatypes.anyURI)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
        27, 24)
    __id._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
        27, 24)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __statusCode.name(): __statusCode,
        __eTag.name(): __eTag,
        __resourceURI.name(): __resourceURI,
        __lastModifiedTime.name(): __lastModifiedTime,
        __resultBody.name(): __resultBody
    })
    _AttributeMap.update({
        __id.name(): __id
    })


# Complex type {http://uri.etsi.org/m2m}MgmtCmd with content type ELEMENT_ONLY
class MgmtCmd(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}MgmtCmd with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MgmtCmd')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_MgmtCmd_httpuri_etsi_orgm2maccessRightID', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_MgmtCmd_httpuri_etsi_orgm2mcreationTime', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_MgmtCmd_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}expirationTime uses Python identifier expirationTime
    __expirationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
        'expirationTime',
        '__httpuri_etsi_orgm2m_MgmtCmd_httpuri_etsi_orgm2mexpirationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            16, 4), )

    expirationTime = property(__expirationTime.value, __expirationTime.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}searchStrings uses Python identifier searchStrings
    __searchStrings = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings'),
        'searchStrings',
        '__httpuri_etsi_orgm2m_MgmtCmd_httpuri_etsi_orgm2msearchStrings', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            18, 4), )

    searchStrings = property(__searchStrings.value, __searchStrings.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_MgmtCmd_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'description'), 'description',
        '__httpuri_etsi_orgm2m_MgmtCmd_httpuri_etsi_orgm2mdescription', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
            12, 4), )

    description = property(__description.value, __description.set, None, None)


    # Element {http://uri.etsi.org/m2m}cmdType uses Python identifier cmdType
    __cmdType = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'cmdType'), 'cmdType',
        '__httpuri_etsi_orgm2m_MgmtCmd_httpuri_etsi_orgm2mcmdType', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
            34, 4), )

    cmdType = property(__cmdType.value, __cmdType.set, None, None)


    # Element {http://uri.etsi.org/m2m}execEnable uses Python identifier execEnable
    __execEnable = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'execEnable'), 'execEnable',
        '__httpuri_etsi_orgm2m_MgmtCmd_httpuri_etsi_orgm2mexecEnable', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
            47, 4), )

    execEnable = property(__execEnable.value, __execEnable.set, None, None)


    # Element {http://uri.etsi.org/m2m}execReqArgs uses Python identifier execReqArgs
    __execReqArgs = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'execReqArgs'), 'execReqArgs',
        '__httpuri_etsi_orgm2m_MgmtCmd_httpuri_etsi_orgm2mexecReqArgs', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
            49, 4), )

    execReqArgs = property(__execReqArgs.value, __execReqArgs.set, None, None)


    # Element {http://uri.etsi.org/m2m}execInstancesReference uses Python identifier execInstancesReference
    __execInstancesReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'execInstancesReference'),
        'execInstancesReference',
        '__httpuri_etsi_orgm2m_MgmtCmd_httpuri_etsi_orgm2mexecInstancesReference',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
            64, 4), )

    execInstancesReference = property(__execInstancesReference.value,
                                      __execInstancesReference.set, None, None)


    # Attribute {http://uri.etsi.org/m2m}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_MgmtCmd_httpuri_etsi_orgm2mid',
        pyxb.binding.datatypes.NMTOKEN)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 8, 4)
    __id._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd', 30, 8)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __expirationTime.name(): __expirationTime,
        __searchStrings.name(): __searchStrings,
        __subscriptionsReference.name(): __subscriptionsReference,
        __description.name(): __description,
        __cmdType.name(): __cmdType,
        __execEnable.name(): __execEnable,
        __execReqArgs.name(): __execReqArgs,
        __execInstancesReference.name(): __execInstancesReference
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'MgmtCmd', MgmtCmd)


# Complex type {http://uri.etsi.org/m2m}ExecReqArgsList with content type ELEMENT_ONLY
class ExecReqArgsList(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ExecReqArgsList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExecReqArgsList')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd', 50, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element execReqArg uses Python identifier execReqArg
    __execReqArg = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'execReqArg'), 'execReqArg',
        '__httpuri_etsi_orgm2m_ExecReqArgsList_execReqArg', True,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
            52, 12), )

    execReqArg = property(__execReqArg.value, __execReqArg.set, None, None)

    _ElementMap.update({
        __execReqArg.name(): __execReqArg
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'ExecReqArgsList', ExecReqArgsList)


# Complex type {http://uri.etsi.org/m2m}ExecReqArg with content type ELEMENT_ONLY
class ExecReqArg(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ExecReqArg with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ExecReqArg')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd', 57, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'name'), 'name',
        '__httpuri_etsi_orgm2m_ExecReqArg_name', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
            59, 12), )

    name = property(__name.value, __name.set, None, None)


    # Element value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'value'), 'value_',
        '__httpuri_etsi_orgm2m_ExecReqArg_value', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
            60, 12), )

    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        __name.name(): __name,
        __value.name(): __value
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'ExecReqArg', ExecReqArg)


# Complex type {http://uri.etsi.org/m2m}MgmtObj with content type ELEMENT_ONLY
class MgmtObj(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}MgmtObj with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MgmtObj')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd', 9, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_MgmtObj_httpuri_etsi_orgm2maccessRightID', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_MgmtObj_httpuri_etsi_orgm2mcreationTime', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_MgmtObj_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}expirationTime uses Python identifier expirationTime
    __expirationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
        'expirationTime',
        '__httpuri_etsi_orgm2m_MgmtObj_httpuri_etsi_orgm2mexpirationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            16, 4), )

    expirationTime = property(__expirationTime.value, __expirationTime.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}searchStrings uses Python identifier searchStrings
    __searchStrings = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings'),
        'searchStrings',
        '__httpuri_etsi_orgm2m_MgmtObj_httpuri_etsi_orgm2msearchStrings', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            18, 4), )

    searchStrings = property(__searchStrings.value, __searchStrings.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_MgmtObj_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}contentType uses Python identifier contentType
    __contentType = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'contentType'), 'contentType',
        '__httpuri_etsi_orgm2m_MgmtObj_httpuri_etsi_orgm2mcontentType', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            106, 4), )

    contentType = property(__contentType.value, __contentType.set, None, None)


    # Element {http://uri.etsi.org/m2m}moID uses Python identifier moID
    __moID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'moID'), 'moID',
        '__httpuri_etsi_orgm2m_MgmtObj_httpuri_etsi_orgm2mmoID', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
            8, 4), )

    moID = property(__moID.value, __moID.set, None, None)


    # Element {http://uri.etsi.org/m2m}originalMO uses Python identifier originalMO
    __originalMO = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO'), 'originalMO',
        '__httpuri_etsi_orgm2m_MgmtObj_httpuri_etsi_orgm2moriginalMO', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
            10, 4), )

    originalMO = property(__originalMO.value, __originalMO.set, None, None)


    # Element {http://uri.etsi.org/m2m}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'description'), 'description',
        '__httpuri_etsi_orgm2m_MgmtObj_httpuri_etsi_orgm2mdescription', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
            12, 4), )

    description = property(__description.value, __description.set, None, None)


    # Element {http://uri.etsi.org/m2m}parametersCollection uses Python identifier parametersCollection
    __parametersCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection'),
        'parametersCollection',
        '__httpuri_etsi_orgm2m_MgmtObj_httpuri_etsi_orgm2mparametersCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
            14, 4), )

    parametersCollection = property(__parametersCollection.value,
                                    __parametersCollection.set, None, None)


    # Attribute {http://uri.etsi.org/m2m}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_MgmtObj_httpuri_etsi_orgm2mid',
        pyxb.binding.datatypes.NMTOKEN, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 8, 4)
    __id._UseLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd', 29,
        8)

    id = property(__id.value, __id.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __expirationTime.name(): __expirationTime,
        __searchStrings.name(): __searchStrings,
        __subscriptionsReference.name(): __subscriptionsReference,
        __contentType.name(): __contentType,
        __moID.name(): __moID,
        __originalMO.name(): __originalMO,
        __description.name(): __description,
        __parametersCollection.name(): __parametersCollection
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'MgmtObj', MgmtObj)


# Complex type {http://uri.etsi.org/m2m}MgmtObjs with content type ELEMENT_ONLY
class MgmtObjs(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}MgmtObjs with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MgmtObjs')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObjs.xsd', 8, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_MgmtObjs_httpuri_etsi_orgm2maccessRightID',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_MgmtObjs_httpuri_etsi_orgm2mcreationTime', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_MgmtObjs_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_MgmtObjs_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}mgmtObjCollection uses Python identifier mgmtObjCollection
    __mgmtObjCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'mgmtObjCollection'),
        'mgmtObjCollection',
        '__httpuri_etsi_orgm2m_MgmtObjs_httpuri_etsi_orgm2mmgmtObjCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObjs.xsd',
            21, 4), )

    mgmtObjCollection = property(__mgmtObjCollection.value,
                                 __mgmtObjCollection.set, None, None)


    # Element {http://uri.etsi.org/m2m}mgmtCmdCollection uses Python identifier mgmtCmdCollection
    __mgmtCmdCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'mgmtCmdCollection'),
        'mgmtCmdCollection',
        '__httpuri_etsi_orgm2m_MgmtObjs_httpuri_etsi_orgm2mmgmtCmdCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObjs.xsd',
            22, 4), )

    mgmtCmdCollection = property(__mgmtCmdCollection.value,
                                 __mgmtCmdCollection.set, None, None)

    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __subscriptionsReference.name(): __subscriptionsReference,
        __mgmtObjCollection.name(): __mgmtObjCollection,
        __mgmtCmdCollection.name(): __mgmtCmdCollection
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'MgmtObjs', MgmtObjs)


# Complex type {http://uri.etsi.org/m2m}NotificationChannel with content type ELEMENT_ONLY
class NotificationChannel(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}NotificationChannel with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'NotificationChannel')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannel.xsd',
        10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_NotificationChannel_httpuri_etsi_orgm2mcreationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_NotificationChannel_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}contactURI uses Python identifier contactURI
    __contactURI = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'contactURI'), 'contactURI',
        '__httpuri_etsi_orgm2m_NotificationChannel_httpuri_etsi_orgm2mcontactURI',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            136, 4), )

    contactURI = property(__contactURI.value, __contactURI.set, None, None)


    # Element {http://uri.etsi.org/m2m}channelType uses Python identifier channelType
    __channelType = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'channelType'), 'channelType',
        '__httpuri_etsi_orgm2m_NotificationChannel_httpuri_etsi_orgm2mchannelType',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            138, 4), )

    channelType = property(__channelType.value, __channelType.set, None, None)


    # Element {http://uri.etsi.org/m2m}channelData uses Python identifier channelData
    __channelData = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'channelData'), 'channelData',
        '__httpuri_etsi_orgm2m_NotificationChannel_httpuri_etsi_orgm2mchannelData',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            146, 4), )

    channelData = property(__channelData.value, __channelData.set, None, None)


    # Attribute {http://uri.etsi.org/m2m}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_NotificationChannel_httpuri_etsi_orgm2mid',
        pyxb.binding.datatypes.NMTOKEN)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 8, 4)
    __id._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannel.xsd',
        19, 8)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __contactURI.name(): __contactURI,
        __channelType.name(): __channelType,
        __channelData.name(): __channelData
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'NotificationChannel',
                            NotificationChannel)


# Complex type {http://uri.etsi.org/m2m}NotificationChannels with content type ELEMENT_ONLY
class NotificationChannels(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}NotificationChannels with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'NotificationChannels')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannels.xsd',
        10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_NotificationChannels_httpuri_etsi_orgm2mcreationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_NotificationChannels_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}notificationChannelCollection uses Python identifier notificationChannelCollection
    __notificationChannelCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace,
                                    u'notificationChannelCollection'),
        'notificationChannelCollection',
        '__httpuri_etsi_orgm2m_NotificationChannels_httpuri_etsi_orgm2mnotificationChannelCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannels.xsd',
            19, 4), )

    notificationChannelCollection = property(
        __notificationChannelCollection.value,
        __notificationChannelCollection.set, None, None)

    _ElementMap.update({
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __notificationChannelCollection.name(): __notificationChannelCollection
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'NotificationChannels',
                            NotificationChannels)


# Complex type {http://uri.etsi.org/m2m}Notify with content type ELEMENT_ONLY
class Notify(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}Notify with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Notify')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}statusCode uses Python identifier statusCode
    __statusCode = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'statusCode'), 'statusCode',
        '__httpuri_etsi_orgm2m_Notify_httpuri_etsi_orgm2mstatusCode', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            186, 4), )

    statusCode = property(__statusCode.value, __statusCode.set, None, None)


    # Element representation uses Python identifier representation
    __representation = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'representation'), 'representation',
        '__httpuri_etsi_orgm2m_Notify_representation', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd', 14,
            16), )

    representation = property(__representation.value, __representation.set,
                              None, None)


    # Element timeoutReason uses Python identifier timeoutReason
    __timeoutReason = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'timeoutReason'), 'timeoutReason',
        '__httpuri_etsi_orgm2m_Notify_timeoutReason', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd', 16,
            16), )

    timeoutReason = property(__timeoutReason.value, __timeoutReason.set, None,
                             None)


    # Element subscriptionReference uses Python identifier subscriptionReference
    __subscriptionReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'subscriptionReference'),
        'subscriptionReference',
        '__httpuri_etsi_orgm2m_Notify_subscriptionReference', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd', 18,
            12), )

    subscriptionReference = property(__subscriptionReference.value,
                                     __subscriptionReference.set, None, None)


    # Element requestingEntity uses Python identifier requestingEntity
    __requestingEntity = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'requestingEntity'),
        'requestingEntity', '__httpuri_etsi_orgm2m_Notify_requestingEntity',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd', 19,
            12), )

    requestingEntity = property(__requestingEntity.value,
                                __requestingEntity.set, None, None)


    # Element contact uses Python identifier contact
    __contact = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'contact'), 'contact',
        '__httpuri_etsi_orgm2m_Notify_contact', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd', 20,
            12), )

    contact = property(__contact.value, __contact.set, None, None)

    _ElementMap.update({
        __statusCode.name(): __statusCode,
        __representation.name(): __representation,
        __timeoutReason.name(): __timeoutReason,
        __subscriptionReference.name(): __subscriptionReference,
        __requestingEntity.name(): __requestingEntity,
        __contact.name(): __contact
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'Notify', Notify)


# Complex type {http://uri.etsi.org/m2m}NotifyCollection with content type ELEMENT_ONLY
class NotifyCollection(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}NotifyCollection with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NotifyCollection')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notifyCollection.xsd',
        14, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}notify uses Python identifier notify
    __notify = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'notify'), 'notify',
        '__httpuri_etsi_orgm2m_NotifyCollection_httpuri_etsi_orgm2mnotify',
        True, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd', 9,
            4), )

    notify = property(__notify.value, __notify.set, None, None)

    _ElementMap.update({
        __notify.name(): __notify
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'NotifyCollection',
                            NotifyCollection)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notifyCollectionResponse.xsd',
        13, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'status'), 'status',
        '__httpuri_etsi_orgm2m_CTD_ANON_3_status', True,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notifyCollectionResponse.xsd',
            15, 16), )

    status = property(__status.value, __status.set, None, None)

    _ElementMap.update({
        __status.name(): __status
    })
    _AttributeMap.update({

    })


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4(pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notifyCollectionResponse.xsd',
        16, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element targetId uses Python identifier targetId
    __targetId = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'targetId'), 'targetId',
        '__httpuri_etsi_orgm2m_CTD_ANON_4_targetId', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notifyCollectionResponse.xsd',
            18, 28), )

    targetId = property(__targetId.value, __targetId.set, None, None)


    # Element primitiveType uses Python identifier primitiveType
    __primitiveType = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'primitiveType'), 'primitiveType',
        '__httpuri_etsi_orgm2m_CTD_ANON_4_primitiveType', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notifyCollectionResponse.xsd',
            19, 28), )

    primitiveType = property(__primitiveType.value, __primitiveType.set, None,
                             None)


    # Element statusCode uses Python identifier statusCode
    __statusCode = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'statusCode'), 'statusCode',
        '__httpuri_etsi_orgm2m_CTD_ANON_4_statusCode', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notifyCollectionResponse.xsd',
            20, 28), )

    statusCode = property(__statusCode.value, __statusCode.set, None, None)

    _ElementMap.update({
        __targetId.name(): __targetId,
        __primitiveType.name(): __primitiveType,
        __statusCode.name(): __statusCode
    })
    _AttributeMap.update({

    })


# Complex type {http://uri.etsi.org/m2m}Parameters with content type ELEMENT_ONLY
class Parameters(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}Parameters with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Parameters')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd', 9,
        4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_Parameters_httpuri_etsi_orgm2maccessRightID',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_Parameters_httpuri_etsi_orgm2mcreationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_Parameters_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_Parameters_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}originalMO uses Python identifier originalMO
    __originalMO = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO'), 'originalMO',
        '__httpuri_etsi_orgm2m_Parameters_httpuri_etsi_orgm2moriginalMO', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
            10, 4), )

    originalMO = property(__originalMO.value, __originalMO.set, None, None)


    # Element {http://uri.etsi.org/m2m}parametersCollection uses Python identifier parametersCollection
    __parametersCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection'),
        'parametersCollection',
        '__httpuri_etsi_orgm2m_Parameters_httpuri_etsi_orgm2mparametersCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
            14, 4), )

    parametersCollection = property(__parametersCollection.value,
                                    __parametersCollection.set, None, None)


    # Attribute {http://uri.etsi.org/m2m}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_Parameters_httpuri_etsi_orgm2mid',
        pyxb.binding.datatypes.NMTOKEN, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 8, 4)
    __id._UseLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
        22, 8)

    id = property(__id.value, __id.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __subscriptionsReference.name(): __subscriptionsReference,
        __originalMO.name(): __originalMO,
        __parametersCollection.name(): __parametersCollection
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'Parameters', Parameters)


# Complex type {http://uri.etsi.org/m2m}RequestNotify with content type ELEMENT_ONLY
class RequestNotify(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}RequestNotify with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RequestNotify')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
        12, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element requestingEntity uses Python identifier requestingEntity
    __requestingEntity = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'requestingEntity'),
        'requestingEntity',
        '__httpuri_etsi_orgm2m_RequestNotify_requestingEntity', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            14, 12), )

    requestingEntity = property(__requestingEntity.value,
                                __requestingEntity.set, None, None)


    # Element targetID uses Python identifier targetID
    __targetID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'targetID'), 'targetID',
        '__httpuri_etsi_orgm2m_RequestNotify_targetID', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            15, 12), )

    targetID = property(__targetID.value, __targetID.set, None, None)


    # Element method uses Python identifier method
    __method = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'method'), 'method',
        '__httpuri_etsi_orgm2m_RequestNotify_method', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            16, 12), )

    method = property(__method.value, __method.set, None, None)


    # Element filterCriteria uses Python identifier filterCriteria
    __filterCriteria = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'filterCriteria'), 'filterCriteria',
        '__httpuri_etsi_orgm2m_RequestNotify_filterCriteria', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            17, 12), )

    filterCriteria = property(__filterCriteria.value, __filterCriteria.set,
                              None, None)


    # Element maxSize uses Python identifier maxSize
    __maxSize = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'maxSize'), 'maxSize',
        '__httpuri_etsi_orgm2m_RequestNotify_maxSize', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            19, 12), )

    maxSize = property(__maxSize.value, __maxSize.set, None, None)


    # Element searchPrefix uses Python identifier searchPrefix
    __searchPrefix = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'searchPrefix'), 'searchPrefix',
        '__httpuri_etsi_orgm2m_RequestNotify_searchPrefix', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            20, 12), )

    searchPrefix = property(__searchPrefix.value, __searchPrefix.set, None,
                            None)


    # Element groupRequestIdentifier uses Python identifier groupRequestIdentifier
    __groupRequestIdentifier = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'groupRequestIdentifier'),
        'groupRequestIdentifier',
        '__httpuri_etsi_orgm2m_RequestNotify_groupRequestIdentifier', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            21, 12), )

    groupRequestIdentifier = property(__groupRequestIdentifier.value,
                                      __groupRequestIdentifier.set, None, None)


    # Element TRPDT uses Python identifier TRPDT
    __TRPDT = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'TRPDT'), 'TRPDT',
        '__httpuri_etsi_orgm2m_RequestNotify_TRPDT', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            23, 12), )

    TRPDT = property(__TRPDT.value, __TRPDT.set, None, None)


    # Element RCAT uses Python identifier RCAT
    __RCAT = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'RCAT'), 'RCAT',
        '__httpuri_etsi_orgm2m_RequestNotify_RCAT', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            24, 12), )

    RCAT = property(__RCAT.value, __RCAT.set, None, None)


    # Element contentTypeHeader uses Python identifier contentTypeHeader
    __contentTypeHeader = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'contentTypeHeader'),
        'contentTypeHeader',
        '__httpuri_etsi_orgm2m_RequestNotify_contentTypeHeader', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            25, 12), )

    contentTypeHeader = property(__contentTypeHeader.value,
                                 __contentTypeHeader.set, None, None)


    # Element acceptHeader uses Python identifier acceptHeader
    __acceptHeader = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'acceptHeader'), 'acceptHeader',
        '__httpuri_etsi_orgm2m_RequestNotify_acceptHeader', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            26, 12), )

    acceptHeader = property(__acceptHeader.value, __acceptHeader.set, None,
                            None)


    # Element ifModifiedSinceHeader uses Python identifier ifModifiedSinceHeader
    __ifModifiedSinceHeader = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'ifModifiedSinceHeader'),
        'ifModifiedSinceHeader',
        '__httpuri_etsi_orgm2m_RequestNotify_ifModifiedSinceHeader', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            27, 12), )

    ifModifiedSinceHeader = property(__ifModifiedSinceHeader.value,
                                     __ifModifiedSinceHeader.set, None, None)


    # Element ifUnmodifiedSinceHeader uses Python identifier ifUnmodifiedSinceHeader
    __ifUnmodifiedSinceHeader = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'ifUnmodifiedSinceHeader'),
        'ifUnmodifiedSinceHeader',
        '__httpuri_etsi_orgm2m_RequestNotify_ifUnmodifiedSinceHeader', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            28, 12), )

    ifUnmodifiedSinceHeader = property(__ifUnmodifiedSinceHeader.value,
                                       __ifUnmodifiedSinceHeader.set, None,
                                       None)


    # Element ifMatchHeader uses Python identifier ifMatchHeader
    __ifMatchHeader = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'ifMatchHeader'), 'ifMatchHeader',
        '__httpuri_etsi_orgm2m_RequestNotify_ifMatchHeader', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            30, 12), )

    ifMatchHeader = property(__ifMatchHeader.value, __ifMatchHeader.set, None,
                             None)


    # Element ifNoneMatchHeader uses Python identifier ifNoneMatchHeader
    __ifNoneMatchHeader = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'ifNoneMatchHeader'),
        'ifNoneMatchHeader',
        '__httpuri_etsi_orgm2m_RequestNotify_ifNoneMatchHeader', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            31, 12), )

    ifNoneMatchHeader = property(__ifNoneMatchHeader.value,
                                 __ifNoneMatchHeader.set, None, None)


    # Element xEtsiContactUriHeader uses Python identifier xEtsiContactUriHeader
    __xEtsiContactUriHeader = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'xEtsiContactUriHeader'),
        'xEtsiContactUriHeader',
        '__httpuri_etsi_orgm2m_RequestNotify_xEtsiContactUriHeader', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            32, 12), )

    xEtsiContactUriHeader = property(__xEtsiContactUriHeader.value,
                                     __xEtsiContactUriHeader.set, None, None)


    # Element xEtsiCorrelationIDHeader uses Python identifier xEtsiCorrelationIDHeader
    __xEtsiCorrelationIDHeader = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'xEtsiCorrelationIDHeader'),
        'xEtsiCorrelationIDHeader',
        '__httpuri_etsi_orgm2m_RequestNotify_xEtsiCorrelationIDHeader', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            33, 12), )

    xEtsiCorrelationIDHeader = property(__xEtsiCorrelationIDHeader.value,
                                        __xEtsiCorrelationIDHeader.set, None,
                                        None)


    # Element representation uses Python identifier representation
    __representation = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'representation'), 'representation',
        '__httpuri_etsi_orgm2m_RequestNotify_representation', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            34, 12), )

    representation = property(__representation.value, __representation.set,
                              None, None)

    _ElementMap.update({
        __requestingEntity.name(): __requestingEntity,
        __targetID.name(): __targetID,
        __method.name(): __method,
        __filterCriteria.name(): __filterCriteria,
        __maxSize.name(): __maxSize,
        __searchPrefix.name(): __searchPrefix,
        __groupRequestIdentifier.name(): __groupRequestIdentifier,
        __TRPDT.name(): __TRPDT,
        __RCAT.name(): __RCAT,
        __contentTypeHeader.name(): __contentTypeHeader,
        __acceptHeader.name(): __acceptHeader,
        __ifModifiedSinceHeader.name(): __ifModifiedSinceHeader,
        __ifUnmodifiedSinceHeader.name(): __ifUnmodifiedSinceHeader,
        __ifMatchHeader.name(): __ifMatchHeader,
        __ifNoneMatchHeader.name(): __ifNoneMatchHeader,
        __xEtsiContactUriHeader.name(): __xEtsiContactUriHeader,
        __xEtsiCorrelationIDHeader.name(): __xEtsiCorrelationIDHeader,
        __representation.name(): __representation
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'RequestNotify', RequestNotify)


# Complex type {http://uri.etsi.org/m2m}ResponseNotify with content type ELEMENT_ONLY
class ResponseNotify(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}ResponseNotify with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ResponseNotify')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/responseNotify.xsd',
        13, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}statusCode uses Python identifier statusCode
    __statusCode = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'statusCode'), 'statusCode',
        '__httpuri_etsi_orgm2m_ResponseNotify_httpuri_etsi_orgm2mstatusCode',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            186, 4), )

    statusCode = property(__statusCode.value, __statusCode.set, None, None)


    # Element representation uses Python identifier representation
    __representation = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'representation'), 'representation',
        '__httpuri_etsi_orgm2m_ResponseNotify_representation', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/responseNotify.xsd',
            16, 12), )

    representation = property(__representation.value, __representation.set,
                              None, None)


    # Element locationHeader uses Python identifier locationHeader
    __locationHeader = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'locationHeader'), 'locationHeader',
        '__httpuri_etsi_orgm2m_ResponseNotify_locationHeader', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/responseNotify.xsd',
            18, 12), )

    locationHeader = property(__locationHeader.value, __locationHeader.set,
                              None, None)


    # Element etagHeader uses Python identifier etagHeader
    __etagHeader = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'etagHeader'), 'etagHeader',
        '__httpuri_etsi_orgm2m_ResponseNotify_etagHeader', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/responseNotify.xsd',
            19, 12), )

    etagHeader = property(__etagHeader.value, __etagHeader.set, None, None)


    # Element lastModifiedHeader uses Python identifier lastModifiedHeader
    __lastModifiedHeader = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'lastModifiedHeader'),
        'lastModifiedHeader',
        '__httpuri_etsi_orgm2m_ResponseNotify_lastModifiedHeader', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/responseNotify.xsd',
            20, 12), )

    lastModifiedHeader = property(__lastModifiedHeader.value,
                                  __lastModifiedHeader.set, None, None)

    _ElementMap.update({
        __statusCode.name(): __statusCode,
        __representation.name(): __representation,
        __locationHeader.name(): __locationHeader,
        __etagHeader.name(): __etagHeader,
        __lastModifiedHeader.name(): __lastModifiedHeader
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'ResponseNotify', ResponseNotify)


# Complex type {http://uri.etsi.org/m2m}Scl with content type ELEMENT_ONLY
class Scl(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}Scl with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Scl')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 7, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2maccessRightID', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mcreationTime', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mlastModifiedTime', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}expirationTime uses Python identifier expirationTime
    __expirationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
        'expirationTime',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mexpirationTime', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            16, 4), )

    expirationTime = property(__expirationTime.value, __expirationTime.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}searchStrings uses Python identifier searchStrings
    __searchStrings = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings'),
        'searchStrings',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2msearchStrings', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            18, 4), )

    searchStrings = property(__searchStrings.value, __searchStrings.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}announceTo uses Python identifier announceTo
    __announceTo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'announceTo'), 'announceTo',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mannounceTo', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            58, 4), )

    announceTo = property(__announceTo.value, __announceTo.set, None, None)


    # Element {http://uri.etsi.org/m2m}link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'link'), 'link',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mlink', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            74, 4), )

    link = property(__link.value, __link.set, None, None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}groupsReference uses Python identifier groupsReference
    __groupsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'groupsReference'),
        'groupsReference',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mgroupsReference', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            77, 4), )

    groupsReference = property(__groupsReference.value, __groupsReference.set,
                               None, None)


    # Element {http://uri.etsi.org/m2m}applicationsReference uses Python identifier applicationsReference
    __applicationsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'applicationsReference'),
        'applicationsReference',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mapplicationsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            78, 4), )

    applicationsReference = property(__applicationsReference.value,
                                     __applicationsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}containersReference uses Python identifier containersReference
    __containersReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'containersReference'),
        'containersReference',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mcontainersReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            79, 4), )

    containersReference = property(__containersReference.value,
                                   __containersReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}accessRightsReference uses Python identifier accessRightsReference
    __accessRightsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightsReference'),
        'accessRightsReference',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2maccessRightsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            81, 4), )

    accessRightsReference = property(__accessRightsReference.value,
                                     __accessRightsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}notificationChannelsReference uses Python identifier notificationChannelsReference
    __notificationChannelsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace,
                                    u'notificationChannelsReference'),
        'notificationChannelsReference',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mnotificationChannelsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            82, 4), )

    notificationChannelsReference = property(
        __notificationChannelsReference.value,
        __notificationChannelsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}communicationChannelsReference uses Python identifier communicationChannelsReference
    __communicationChannelsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace,
                                    u'communicationChannelsReference'),
        'communicationChannelsReference',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mcommunicationChannelsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            83, 4), )

    communicationChannelsReference = property(
        __communicationChannelsReference.value,
        __communicationChannelsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}mgmtObjsReference uses Python identifier mgmtObjsReference
    __mgmtObjsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'mgmtObjsReference'),
        'mgmtObjsReference',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mmgmtObjsReference', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            84, 4), )

    mgmtObjsReference = property(__mgmtObjsReference.value,
                                 __mgmtObjsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}onlineStatus uses Python identifier onlineStatus
    __onlineStatus = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'onlineStatus'), 'onlineStatus',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2monlineStatus', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            126, 4), )

    onlineStatus = property(__onlineStatus.value, __onlineStatus.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}aPocHandling uses Python identifier aPocHandling
    __aPocHandling = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'aPocHandling'), 'aPocHandling',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2maPocHandling', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            210, 4), )

    aPocHandling = property(__aPocHandling.value, __aPocHandling.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}pocs uses Python identifier pocs
    __pocs = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'pocs'), 'pocs',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mpocs', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 42,
            4), )

    pocs = property(__pocs.value, __pocs.set, None, None)


    # Element {http://uri.etsi.org/m2m}serverCapability uses Python identifier serverCapability
    __serverCapability = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'serverCapability'),
        'serverCapability',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mserverCapability', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 43,
            4), )

    serverCapability = property(__serverCapability.value,
                                __serverCapability.set, None, None)


    # Element {http://uri.etsi.org/m2m}schedule uses Python identifier schedule
    __schedule = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'schedule'), 'schedule',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mschedule', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 44,
            4), )

    schedule = property(__schedule.value, __schedule.set, None, None)


    # Element {http://uri.etsi.org/m2m}remTriggerAddr uses Python identifier remTriggerAddr
    __remTriggerAddr = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'remTriggerAddr'),
        'remTriggerAddr',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mremTriggerAddr', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 45,
            4), )

    remTriggerAddr = property(__remTriggerAddr.value, __remTriggerAddr.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}locTargetDevice uses Python identifier locTargetDevice
    __locTargetDevice = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'locTargetDevice'),
        'locTargetDevice',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mlocTargetDevice', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 46,
            4), )

    locTargetDevice = property(__locTargetDevice.value, __locTargetDevice.set,
                               None, None)


    # Element {http://uri.etsi.org/m2m}mgmtProtocolType uses Python identifier mgmtProtocolType
    __mgmtProtocolType = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'mgmtProtocolType'),
        'mgmtProtocolType',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mmgmtProtocolType', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 47,
            4), )

    mgmtProtocolType = property(__mgmtProtocolType.value,
                                __mgmtProtocolType.set, None, None)


    # Element {http://uri.etsi.org/m2m}sclType uses Python identifier sclType
    __sclType = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'sclType'), 'sclType',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2msclType', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 48,
            4), )

    sclType = property(__sclType.value, __sclType.set, None, None)


    # Element {http://uri.etsi.org/m2m}publicDomain uses Python identifier publicDomain
    __publicDomain = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'publicDomain'), 'publicDomain',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mpublicDomain', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 49,
            4), )

    publicDomain = property(__publicDomain.value, __publicDomain.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}integrityValResults uses Python identifier integrityValResults
    __integrityValResults = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'integrityValResults'),
        'integrityValResults',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mintegrityValResults',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 50,
            4), )

    integrityValResults = property(__integrityValResults.value,
                                   __integrityValResults.set, None, None)


    # Element {http://uri.etsi.org/m2m}m2mPocsReference uses Python identifier m2mPocsReference
    __m2mPocsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'm2mPocsReference'),
        'm2mPocsReference',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mm2mPocsReference', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 51,
            4), )

    m2mPocsReference = property(__m2mPocsReference.value,
                                __m2mPocsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}attachedDevicesReference uses Python identifier attachedDevicesReference
    __attachedDevicesReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'attachedDevicesReference'),
        'attachedDevicesReference',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2mattachedDevicesReference',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 52,
            4), )

    attachedDevicesReference = property(__attachedDevicesReference.value,
                                        __attachedDevicesReference.set, None,
                                        None)


    # Element {http://uri.etsi.org/m2m}sclAnncsReference uses Python identifier sclAnncsReference
    __sclAnncsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'sclAnncsReference'),
        'sclAnncsReference',
        '__httpuri_etsi_orgm2m_Scl_httpuri_etsi_orgm2msclAnncsReference', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 53,
            4), )

    sclAnncsReference = property(__sclAnncsReference.value,
                                 __sclAnncsReference.set, None, None)


    # Attribute sclId uses Python identifier sclId
    __sclId = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, u'sclId'), 'sclId',
        '__httpuri_etsi_orgm2m_Scl_sclId', pyxb.binding.datatypes.anyURI)
    __sclId._DeclarationLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 40, 8)
    __sclId._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 40, 8)

    sclId = property(__sclId.value, __sclId.set, None, None)

    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __expirationTime.name(): __expirationTime,
        __searchStrings.name(): __searchStrings,
        __announceTo.name(): __announceTo,
        __link.name(): __link,
        __subscriptionsReference.name(): __subscriptionsReference,
        __groupsReference.name(): __groupsReference,
        __applicationsReference.name(): __applicationsReference,
        __containersReference.name(): __containersReference,
        __accessRightsReference.name(): __accessRightsReference,
        __notificationChannelsReference.name(): __notificationChannelsReference,
        __communicationChannelsReference.name(): __communicationChannelsReference,
        __mgmtObjsReference.name(): __mgmtObjsReference,
        __onlineStatus.name(): __onlineStatus,
        __aPocHandling.name(): __aPocHandling,
        __pocs.name(): __pocs,
        __serverCapability.name(): __serverCapability,
        __schedule.name(): __schedule,
        __remTriggerAddr.name(): __remTriggerAddr,
        __locTargetDevice.name(): __locTargetDevice,
        __mgmtProtocolType.name(): __mgmtProtocolType,
        __sclType.name(): __sclType,
        __publicDomain.name(): __publicDomain,
        __integrityValResults.name(): __integrityValResults,
        __m2mPocsReference.name(): __m2mPocsReference,
        __attachedDevicesReference.name(): __attachedDevicesReference,
        __sclAnncsReference.name(): __sclAnncsReference
    })
    _AttributeMap.update({
        __sclId.name(): __sclId
    })


Namespace.addCategoryObject('typeBinding', u'Scl', Scl)


# Complex type {http://uri.etsi.org/m2m}IntegrityValResults with content type ELEMENT_ONLY
class IntegrityValResults(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}IntegrityValResults with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'IntegrityValResults')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 68, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element ivalResults uses Python identifier ivalResults
    __ivalResults = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'ivalResults'), 'ivalResults',
        '__httpuri_etsi_orgm2m_IntegrityValResults_ivalResults', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 70,
            12), )

    ivalResults = property(__ivalResults.value, __ivalResults.set, None, None)


    # Element signedIvalResult uses Python identifier signedIvalResult
    __signedIvalResult = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'signedIvalResult'),
        'signedIvalResult',
        '__httpuri_etsi_orgm2m_IntegrityValResults_signedIvalResult', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 71,
            12), )

    signedIvalResult = property(__signedIvalResult.value,
                                __signedIvalResult.set, None, None)


    # Element secureTimeStamp uses Python identifier secureTimeStamp
    __secureTimeStamp = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'secureTimeStamp'),
        'secureTimeStamp',
        '__httpuri_etsi_orgm2m_IntegrityValResults_secureTimeStamp', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 72,
            12), )

    secureTimeStamp = property(__secureTimeStamp.value, __secureTimeStamp.set,
                               None, None)

    _ElementMap.update({
        __ivalResults.name(): __ivalResults,
        __signedIvalResult.name(): __signedIvalResult,
        __secureTimeStamp.name(): __secureTimeStamp
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'IntegrityValResults',
                            IntegrityValResults)


# Complex type {http://uri.etsi.org/m2m}SclAnnc with content type ELEMENT_ONLY
class SclAnnc(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}SclAnnc with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SclAnnc')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnnc.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_SclAnnc_httpuri_etsi_orgm2maccessRightID', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}expirationTime uses Python identifier expirationTime
    __expirationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
        'expirationTime',
        '__httpuri_etsi_orgm2m_SclAnnc_httpuri_etsi_orgm2mexpirationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            16, 4), )

    expirationTime = property(__expirationTime.value, __expirationTime.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}searchStrings uses Python identifier searchStrings
    __searchStrings = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings'),
        'searchStrings',
        '__httpuri_etsi_orgm2m_SclAnnc_httpuri_etsi_orgm2msearchStrings', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            18, 4), )

    searchStrings = property(__searchStrings.value, __searchStrings.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'link'), 'link',
        '__httpuri_etsi_orgm2m_SclAnnc_httpuri_etsi_orgm2mlink', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            74, 4), )

    link = property(__link.value, __link.set, None, None)


    # Element {http://uri.etsi.org/m2m}groupsReference uses Python identifier groupsReference
    __groupsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'groupsReference'),
        'groupsReference',
        '__httpuri_etsi_orgm2m_SclAnnc_httpuri_etsi_orgm2mgroupsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            77, 4), )

    groupsReference = property(__groupsReference.value, __groupsReference.set,
                               None, None)


    # Element {http://uri.etsi.org/m2m}applicationsReference uses Python identifier applicationsReference
    __applicationsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'applicationsReference'),
        'applicationsReference',
        '__httpuri_etsi_orgm2m_SclAnnc_httpuri_etsi_orgm2mapplicationsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            78, 4), )

    applicationsReference = property(__applicationsReference.value,
                                     __applicationsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}containersReference uses Python identifier containersReference
    __containersReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'containersReference'),
        'containersReference',
        '__httpuri_etsi_orgm2m_SclAnnc_httpuri_etsi_orgm2mcontainersReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            79, 4), )

    containersReference = property(__containersReference.value,
                                   __containersReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}accessRightsReference uses Python identifier accessRightsReference
    __accessRightsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightsReference'),
        'accessRightsReference',
        '__httpuri_etsi_orgm2m_SclAnnc_httpuri_etsi_orgm2maccessRightsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            81, 4), )

    accessRightsReference = property(__accessRightsReference.value,
                                     __accessRightsReference.set, None, None)


    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_SclAnnc_id', pyxb.binding.datatypes.anyURI)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnnc.xsd', 22, 8)
    __id._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnnc.xsd', 22, 8)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __expirationTime.name(): __expirationTime,
        __searchStrings.name(): __searchStrings,
        __link.name(): __link,
        __groupsReference.name(): __groupsReference,
        __applicationsReference.name(): __applicationsReference,
        __containersReference.name(): __containersReference,
        __accessRightsReference.name(): __accessRightsReference
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'SclAnnc', SclAnnc)


# Complex type {http://uri.etsi.org/m2m}SclAnncs with content type ELEMENT_ONLY
class SclAnncs(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}SclAnncs with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SclAnncs')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnncs.xsd', 10,
        4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_SclAnncs_httpuri_etsi_orgm2maccessRightID',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_SclAnncs_httpuri_etsi_orgm2mcreationTime', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_SclAnncs_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_SclAnncs_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}sclAnncCollection uses Python identifier sclAnncCollection
    __sclAnncCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'sclAnncCollection'),
        'sclAnncCollection',
        '__httpuri_etsi_orgm2m_SclAnncs_httpuri_etsi_orgm2msclAnncCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnncs.xsd',
            22, 4), )

    sclAnncCollection = property(__sclAnncCollection.value,
                                 __sclAnncCollection.set, None, None)

    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __subscriptionsReference.name(): __subscriptionsReference,
        __sclAnncCollection.name(): __sclAnncCollection
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'SclAnncs', SclAnncs)


# Complex type {http://uri.etsi.org/m2m}SclBase with content type ELEMENT_ONLY
class SclBase(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}SclBase with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SclBase')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_SclBase_httpuri_etsi_orgm2maccessRightID', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_SclBase_httpuri_etsi_orgm2mcreationTime', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_SclBase_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}searchStrings uses Python identifier searchStrings
    __searchStrings = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings'),
        'searchStrings',
        '__httpuri_etsi_orgm2m_SclBase_httpuri_etsi_orgm2msearchStrings', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            18, 4), )

    searchStrings = property(__searchStrings.value, __searchStrings.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_SclBase_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}groupsReference uses Python identifier groupsReference
    __groupsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'groupsReference'),
        'groupsReference',
        '__httpuri_etsi_orgm2m_SclBase_httpuri_etsi_orgm2mgroupsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            77, 4), )

    groupsReference = property(__groupsReference.value, __groupsReference.set,
                               None, None)


    # Element {http://uri.etsi.org/m2m}applicationsReference uses Python identifier applicationsReference
    __applicationsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'applicationsReference'),
        'applicationsReference',
        '__httpuri_etsi_orgm2m_SclBase_httpuri_etsi_orgm2mapplicationsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            78, 4), )

    applicationsReference = property(__applicationsReference.value,
                                     __applicationsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}containersReference uses Python identifier containersReference
    __containersReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'containersReference'),
        'containersReference',
        '__httpuri_etsi_orgm2m_SclBase_httpuri_etsi_orgm2mcontainersReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            79, 4), )

    containersReference = property(__containersReference.value,
                                   __containersReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}accessRightsReference uses Python identifier accessRightsReference
    __accessRightsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightsReference'),
        'accessRightsReference',
        '__httpuri_etsi_orgm2m_SclBase_httpuri_etsi_orgm2maccessRightsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            81, 4), )

    accessRightsReference = property(__accessRightsReference.value,
                                     __accessRightsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}aPocHandling uses Python identifier aPocHandling
    __aPocHandling = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'aPocHandling'), 'aPocHandling',
        '__httpuri_etsi_orgm2m_SclBase_httpuri_etsi_orgm2maPocHandling', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            210, 4), )

    aPocHandling = property(__aPocHandling.value, __aPocHandling.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}sclsReference uses Python identifier sclsReference
    __sclsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'sclsReference'),
        'sclsReference',
        '__httpuri_etsi_orgm2m_SclBase_httpuri_etsi_orgm2msclsReference', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
            28, 4), )

    sclsReference = property(__sclsReference.value, __sclsReference.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}discoveryReference uses Python identifier discoveryReference
    __discoveryReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'discoveryReference'),
        'discoveryReference',
        '__httpuri_etsi_orgm2m_SclBase_httpuri_etsi_orgm2mdiscoveryReference',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
            29, 4), )

    discoveryReference = property(__discoveryReference.value,
                                  __discoveryReference.set, None, None)

    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __searchStrings.name(): __searchStrings,
        __subscriptionsReference.name(): __subscriptionsReference,
        __groupsReference.name(): __groupsReference,
        __applicationsReference.name(): __applicationsReference,
        __containersReference.name(): __containersReference,
        __accessRightsReference.name(): __accessRightsReference,
        __aPocHandling.name(): __aPocHandling,
        __sclsReference.name(): __sclsReference,
        __discoveryReference.name(): __discoveryReference
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'SclBase', SclBase)


# Complex type {http://uri.etsi.org/m2m}Scls with content type ELEMENT_ONLY
class Scls(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}Scls with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Scls')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scls.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_Scls_httpuri_etsi_orgm2maccessRightID', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_Scls_httpuri_etsi_orgm2mcreationTime', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_Scls_httpuri_etsi_orgm2mlastModifiedTime', False,
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_Scls_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}mgmtObjsReference uses Python identifier mgmtObjsReference
    __mgmtObjsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'mgmtObjsReference'),
        'mgmtObjsReference',
        '__httpuri_etsi_orgm2m_Scls_httpuri_etsi_orgm2mmgmtObjsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            84, 4), )

    mgmtObjsReference = property(__mgmtObjsReference.value,
                                 __mgmtObjsReference.set, None, None)


    # Element {http://uri.etsi.org/m2m}sclCollection uses Python identifier sclCollection
    __sclCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'sclCollection'),
        'sclCollection',
        '__httpuri_etsi_orgm2m_Scls_httpuri_etsi_orgm2msclCollection', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scls.xsd', 23,
            4), )

    sclCollection = property(__sclCollection.value, __sclCollection.set, None,
                             None)

    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __subscriptionsReference.name(): __subscriptionsReference,
        __mgmtObjsReference.name(): __mgmtObjsReference,
        __sclCollection.name(): __sclCollection
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'Scls', Scls)


# Complex type {http://uri.etsi.org/m2m}Subcontainers with content type ELEMENT_ONLY
class Subcontainers(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}Subcontainers with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Subcontainers')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subcontainers.xsd',
        10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}accessRightID uses Python identifier accessRightID
    __accessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
        'accessRightID',
        '__httpuri_etsi_orgm2m_Subcontainers_httpuri_etsi_orgm2maccessRightID',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            10, 4), )

    accessRightID = property(__accessRightID.value, __accessRightID.set, None,
                             None)

    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_Subcontainers_httpuri_etsi_orgm2mcreationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_Subcontainers_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}subscriptionsReference uses Python identifier subscriptionsReference
    __subscriptionsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
        'subscriptionsReference',
        '__httpuri_etsi_orgm2m_Subcontainers_httpuri_etsi_orgm2msubscriptionsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            76, 4), )


    # Element {http://uri.etsi.org/m2m}containerCollection uses Python identifier containerCollection
    __containerCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'containerCollection'),
        'containerCollection',
        '__httpuri_etsi_orgm2m_Subcontainers_httpuri_etsi_orgm2mcontainerCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subcontainers.xsd',
            21, 4), )

    containerCollection = property(__containerCollection.value,
                                   __containerCollection.set, None, None)

    subscriptionsReference = property(__subscriptionsReference.value,
                                      __subscriptionsReference.set, None, None)

    _ElementMap.update({
        __accessRightID.name(): __accessRightID,
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __subscriptionsReference.name(): __subscriptionsReference,
        __containerCollection.name(): __containerCollection
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'Subcontainers', Subcontainers)


# Complex type {http://uri.etsi.org/m2m}Subscription with content type ELEMENT_ONLY
class Subscription(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}Subscription with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Subscription')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
        10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}creationTime uses Python identifier creationTime
    __creationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime'), 'creationTime',
        '__httpuri_etsi_orgm2m_Subscription_httpuri_etsi_orgm2mcreationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            12, 4), )

    creationTime = property(__creationTime.value, __creationTime.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}lastModifiedTime uses Python identifier lastModifiedTime
    __lastModifiedTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
        'lastModifiedTime',
        '__httpuri_etsi_orgm2m_Subscription_httpuri_etsi_orgm2mlastModifiedTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            14, 4), )

    lastModifiedTime = property(__lastModifiedTime.value,
                                __lastModifiedTime.set, None, None)


    # Element {http://uri.etsi.org/m2m}expirationTime uses Python identifier expirationTime
    __expirationTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
        'expirationTime',
        '__httpuri_etsi_orgm2m_Subscription_httpuri_etsi_orgm2mexpirationTime',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            16, 4), )

    expirationTime = property(__expirationTime.value, __expirationTime.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}filterCriteria uses Python identifier filterCriteria
    __filterCriteria = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'filterCriteria'),
        'filterCriteria',
        '__httpuri_etsi_orgm2m_Subscription_httpuri_etsi_orgm2mfilterCriteria',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            30, 4), )

    filterCriteria = property(__filterCriteria.value, __filterCriteria.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}delayTolerance uses Python identifier delayTolerance
    __delayTolerance = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'delayTolerance'),
        'delayTolerance',
        '__httpuri_etsi_orgm2m_Subscription_httpuri_etsi_orgm2mdelayTolerance',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            72, 4), )

    delayTolerance = property(__delayTolerance.value, __delayTolerance.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}minimalTimeBetweenNotifications uses Python identifier minimalTimeBetweenNotifications
    __minimalTimeBetweenNotifications = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace,
                                    u'minimalTimeBetweenNotifications'),
        'minimalTimeBetweenNotifications',
        '__httpuri_etsi_orgm2m_Subscription_httpuri_etsi_orgm2mminimalTimeBetweenNotifications',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
            30, 4), )

    minimalTimeBetweenNotifications = property(
        __minimalTimeBetweenNotifications.value,
        __minimalTimeBetweenNotifications.set, None,
        u'\n                In milliseconds.\n            ')


    # Element {http://uri.etsi.org/m2m}subscriptionType uses Python identifier subscriptionType
    __subscriptionType = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionType'),
        'subscriptionType',
        '__httpuri_etsi_orgm2m_Subscription_httpuri_etsi_orgm2msubscriptionType',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
            37, 4), )

    subscriptionType = property(__subscriptionType.value,
                                __subscriptionType.set, None, None)


    # Element {http://uri.etsi.org/m2m}contact uses Python identifier contact
    __contact = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'contact'), 'contact',
        '__httpuri_etsi_orgm2m_Subscription_httpuri_etsi_orgm2mcontact', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
            38, 4), )

    contact = property(__contact.value, __contact.set, None, None)


    # Element {http://uri.etsi.org/m2m}aggregateURI uses Python identifier aggregateURI
    __aggregateURI = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'aggregateURI'), 'aggregateURI',
        '__httpuri_etsi_orgm2m_Subscription_httpuri_etsi_orgm2maggregateURI',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
            39, 4), )

    aggregateURI = property(__aggregateURI.value, __aggregateURI.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}timeoutReason uses Python identifier timeoutReason
    __timeoutReason = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'timeoutReason'),
        'timeoutReason',
        '__httpuri_etsi_orgm2m_Subscription_httpuri_etsi_orgm2mtimeoutReason',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
            40, 4), )

    timeoutReason = property(__timeoutReason.value, __timeoutReason.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}noRepresentation uses Python identifier noRepresentation
    __noRepresentation = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'noRepresentation'),
        'noRepresentation',
        '__httpuri_etsi_orgm2m_Subscription_httpuri_etsi_orgm2mnoRepresentation',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
            41, 4), )

    noRepresentation = property(__noRepresentation.value,
                                __noRepresentation.set, None, None)


    # Element {http://uri.etsi.org/m2m}subscriberId uses Python identifier subscriberId
    __subscriberId = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriberId'), 'subscriberId',
        '__httpuri_etsi_orgm2m_Subscription_httpuri_etsi_orgm2msubscriberId',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
            42, 4), )

    subscriberId = property(__subscriberId.value, __subscriberId.set, None,
                            None)


    # Attribute {http://uri.etsi.org/m2m}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(Namespace, u'id'), 'id',
        '__httpuri_etsi_orgm2m_Subscription_httpuri_etsi_orgm2mid',
        pyxb.binding.datatypes.NMTOKEN)
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 8, 4)
    __id._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
        28, 8)

    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __creationTime.name(): __creationTime,
        __lastModifiedTime.name(): __lastModifiedTime,
        __expirationTime.name(): __expirationTime,
        __filterCriteria.name(): __filterCriteria,
        __delayTolerance.name(): __delayTolerance,
        __minimalTimeBetweenNotifications.name(): __minimalTimeBetweenNotifications,
        __subscriptionType.name(): __subscriptionType,
        __contact.name(): __contact,
        __aggregateURI.name(): __aggregateURI,
        __timeoutReason.name(): __timeoutReason,
        __noRepresentation.name(): __noRepresentation,
        __subscriberId.name(): __subscriberId
    })
    _AttributeMap.update({
        __id.name(): __id
    })


Namespace.addCategoryObject('typeBinding', u'Subscription', Subscription)


# Complex type {http://uri.etsi.org/m2m}Subscriptions with content type ELEMENT_ONLY
class Subscriptions(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}Subscriptions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Subscriptions')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscriptions.xsd',
        10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}subscriptionCollection uses Python identifier subscriptionCollection
    __subscriptionCollection = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionCollection'),
        'subscriptionCollection',
        '__httpuri_etsi_orgm2m_Subscriptions_httpuri_etsi_orgm2msubscriptionCollection',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscriptions.xsd',
            17, 4), )

    subscriptionCollection = property(__subscriptionCollection.value,
                                      __subscriptionCollection.set, None, None)

    _ElementMap.update({
        __subscriptionCollection.name(): __subscriptionCollection
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'Subscriptions', Subscriptions)


# Complex type {http://uri.etsi.org/m2m}LongPollingChannelData with content type ELEMENT_ONLY
class LongPollingChannelData(ChannelData):
    """Complex type {http://uri.etsi.org/m2m}LongPollingChannelData with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'LongPollingChannelData')
    _XSDLocation = pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 152,
        4)
    _ElementMap = ChannelData._ElementMap.copy()
    _AttributeMap = ChannelData._AttributeMap.copy()
    # Base type is ChannelData

    # Element {http://uri.etsi.org/m2m}longPollingURI uses Python identifier longPollingURI
    __longPollingURI = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'longPollingURI'),
        'longPollingURI',
        '__httpuri_etsi_orgm2m_LongPollingChannelData_httpuri_etsi_orgm2mlongPollingURI',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            162, 4), )

    longPollingURI = property(__longPollingURI.value, __longPollingURI.set,
                              None, None)

    _ElementMap.update({
        __longPollingURI.name(): __longPollingURI
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'LongPollingChannelData',
                            LongPollingChannelData)


# Complex type {http://uri.etsi.org/m2m}Content with content type ELEMENT_ONLY
class Content(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uri.etsi.org/m2m}Content with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Content')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
        29, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://uri.etsi.org/m2m}textContent uses Python identifier textContent
    __textContent = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'textContent'), 'textContent',
        '__httpuri_etsi_orgm2m_Content_httpuri_etsi_orgm2mtextContent', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
            37, 4), )

    textContent = property(__textContent.value, __textContent.set, None, None)


    # Element {http://uri.etsi.org/m2m}binaryContent uses Python identifier binaryContent
    __binaryContent = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'binaryContent'),
        'binaryContent',
        '__httpuri_etsi_orgm2m_Content_httpuri_etsi_orgm2mbinaryContent', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
            38, 4), )

    binaryContent = property(__binaryContent.value, __binaryContent.set, None,
                             None)


    # Attribute {http://www.w3.org/2005/05/xmlmime}contentType uses Python identifier contentType
    __contentType = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(_Namespace_xmlmime, u'contentType'),
        'contentType',
        '__httpuri_etsi_orgm2m_Content_httpwww_w3_org200505xmlmimecontentType',
        _ImportedBinding__xmlmime.STD_ANON)
    __contentType._DeclarationLocation = pyxb.utils.utility.Location(
        u'http://www.w3.org/2005/05/xmlmime.xsd', 23, 2)
    __contentType._UseLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
        34, 8)

    contentType = property(__contentType.value, __contentType.set, None, None)

    _ElementMap.update({
        __textContent.name(): __textContent,
        __binaryContent.name(): __binaryContent
    })
    _AttributeMap.update({
        __contentType.name(): __contentType
    })


Namespace.addCategoryObject('typeBinding', u'Content', Content)


# Complex type {http://uri.etsi.org/m2m}ContentInstancesFilterCriteriaType with content type ELEMENT_ONLY
class ContentInstancesFilterCriteriaType(FilterCriteriaType):
    """Complex type {http://uri.etsi.org/m2m}ContentInstancesFilterCriteriaType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'ContentInstancesFilterCriteriaType')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
        41, 4)
    _ElementMap = FilterCriteriaType._ElementMap.copy()
    _AttributeMap = FilterCriteriaType._AttributeMap.copy()
    # Base type is FilterCriteriaType

    # Element ifModifiedSince (ifModifiedSince) inherited from {http://uri.etsi.org/m2m}FilterCriteriaType

    # Element ifUnmodifiedSince (ifUnmodifiedSince) inherited from {http://uri.etsi.org/m2m}FilterCriteriaType

    # Element ifNoneMatch (ifNoneMatch) inherited from {http://uri.etsi.org/m2m}FilterCriteriaType

    # Element attributeAccessor (attributeAccessor) inherited from {http://uri.etsi.org/m2m}FilterCriteriaType

    # Element searchString (searchString) inherited from {http://uri.etsi.org/m2m}FilterCriteriaType

    # Element createdAfter (createdAfter) inherited from {http://uri.etsi.org/m2m}FilterCriteriaType

    # Element createdBefore (createdBefore) inherited from {http://uri.etsi.org/m2m}FilterCriteriaType

    # Element sizeFrom uses Python identifier sizeFrom
    __sizeFrom = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'sizeFrom'), 'sizeFrom',
        '__httpuri_etsi_orgm2m_ContentInstancesFilterCriteriaType_sizeFrom',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
            45, 20), )

    sizeFrom = property(__sizeFrom.value, __sizeFrom.set, None, None)


    # Element sizeUntil uses Python identifier sizeUntil
    __sizeUntil = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'sizeUntil'), 'sizeUntil',
        '__httpuri_etsi_orgm2m_ContentInstancesFilterCriteriaType_sizeUntil',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
            47, 20), )

    sizeUntil = property(__sizeUntil.value, __sizeUntil.set, None, None)


    # Element contentType uses Python identifier contentType
    __contentType = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'contentType'), 'contentType',
        '__httpuri_etsi_orgm2m_ContentInstancesFilterCriteriaType_contentType',
        True, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
            49, 20), )

    contentType = property(__contentType.value, __contentType.set, None, None)


    # Element metaDataOnly uses Python identifier metaDataOnly
    __metaDataOnly = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, u'metaDataOnly'), 'metaDataOnly',
        '__httpuri_etsi_orgm2m_ContentInstancesFilterCriteriaType_metaDataOnly',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
            51, 20), )

    metaDataOnly = property(__metaDataOnly.value, __metaDataOnly.set, None,
                            None)

    _ElementMap.update({
        __sizeFrom.name(): __sizeFrom,
        __sizeUntil.name(): __sizeUntil,
        __contentType.name(): __contentType,
        __metaDataOnly.name(): __metaDataOnly
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding',
                            u'ContentInstancesFilterCriteriaType',
                            ContentInstancesFilterCriteriaType)


# Complex type {http://uri.etsi.org/m2m}EtsiAreaNwkDeviceInfo with content type ELEMENT_ONLY
class EtsiAreaNwkDeviceInfo(MgmtObj):
    """Complex type {http://uri.etsi.org/m2m}EtsiAreaNwkDeviceInfo with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'EtsiAreaNwkDeviceInfo')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfo.xsd',
        9, 4)
    _ElementMap = MgmtObj._ElementMap.copy()
    _AttributeMap = MgmtObj._AttributeMap.copy()
    # Base type is MgmtObj

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element expirationTime ({http://uri.etsi.org/m2m}expirationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element searchStrings ({http://uri.etsi.org/m2m}searchStrings) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element contentType ({http://uri.etsi.org/m2m}contentType) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element moID ({http://uri.etsi.org/m2m}moID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element description ({http://uri.etsi.org/m2m}description) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Attribute id inherited from {http://uri.etsi.org/m2m}MgmtObj
    _HasWildcardElement = True
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'EtsiAreaNwkDeviceInfo',
                            EtsiAreaNwkDeviceInfo)


# Complex type {http://uri.etsi.org/m2m}AreaNwkDeviceInfoInstance with content type ELEMENT_ONLY
class AreaNwkDeviceInfoInstance(Parameters):
    """Complex type {http://uri.etsi.org/m2m}AreaNwkDeviceInfoInstance with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'AreaNwkDeviceInfoInstance')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
        10, 4)
    _ElementMap = Parameters._ElementMap.copy()
    _AttributeMap = Parameters._AttributeMap.copy()
    # Base type is Parameters

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element {http://uri.etsi.org/m2m}groupsReference uses Python identifier groupsReference
    __groupsReference = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'groupsReference'),
        'groupsReference',
        '__httpuri_etsi_orgm2m_AreaNwkDeviceInfoInstance_httpuri_etsi_orgm2mgroupsReference',
        False, pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            77, 4), )

    groupsReference = property(__groupsReference.value, __groupsReference.set,
                               None, None)


    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element {http://uri.etsi.org/m2m}areaNwkID uses Python identifier areaNwkID
    __areaNwkID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'areaNwkID'), 'areaNwkID',
        '__httpuri_etsi_orgm2m_AreaNwkDeviceInfoInstance_httpuri_etsi_orgm2mareaNwkID',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
            27, 4), )

    areaNwkID = property(__areaNwkID.value, __areaNwkID.set, None, None)


    # Element {http://uri.etsi.org/m2m}status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'status'), 'status',
        '__httpuri_etsi_orgm2m_AreaNwkDeviceInfoInstance_httpuri_etsi_orgm2mstatus',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
            28, 4), )

    status = property(__status.value, __status.set, None, None)


    # Element {http://uri.etsi.org/m2m}sleepInterval uses Python identifier sleepInterval
    __sleepInterval = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'sleepInterval'),
        'sleepInterval',
        '__httpuri_etsi_orgm2m_AreaNwkDeviceInfoInstance_httpuri_etsi_orgm2msleepInterval',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
            35, 4), )

    sleepInterval = property(__sleepInterval.value, __sleepInterval.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}sleepDuration uses Python identifier sleepDuration
    __sleepDuration = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'sleepDuration'),
        'sleepDuration',
        '__httpuri_etsi_orgm2m_AreaNwkDeviceInfoInstance_httpuri_etsi_orgm2msleepDuration',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
            36, 4), )

    sleepDuration = property(__sleepDuration.value, __sleepDuration.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}areaNwkTypeInfoOfDevice uses Python identifier areaNwkTypeInfoOfDevice
    __areaNwkTypeInfoOfDevice = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'areaNwkTypeInfoOfDevice'),
        'areaNwkTypeInfoOfDevice',
        '__httpuri_etsi_orgm2m_AreaNwkDeviceInfoInstance_httpuri_etsi_orgm2mareaNwkTypeInfoOfDevice',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
            37, 4), )

    areaNwkTypeInfoOfDevice = property(__areaNwkTypeInfoOfDevice.value,
                                       __areaNwkTypeInfoOfDevice.set, None,
                                       None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}Parameters
    _HasWildcardElement = True
    _ElementMap.update({
        __groupsReference.name(): __groupsReference,
        __areaNwkID.name(): __areaNwkID,
        __status.name(): __status,
        __sleepInterval.name(): __sleepInterval,
        __sleepDuration.name(): __sleepDuration,
        __areaNwkTypeInfoOfDevice.name(): __areaNwkTypeInfoOfDevice
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'AreaNwkDeviceInfoInstance',
                            AreaNwkDeviceInfoInstance)


# Complex type {http://uri.etsi.org/m2m}EtsiAreaNwkInfo with content type ELEMENT_ONLY
class EtsiAreaNwkInfo(MgmtObj):
    """Complex type {http://uri.etsi.org/m2m}EtsiAreaNwkInfo with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EtsiAreaNwkInfo')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInfo.xsd',
        9, 4)
    _ElementMap = MgmtObj._ElementMap.copy()
    _AttributeMap = MgmtObj._AttributeMap.copy()
    # Base type is MgmtObj

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element expirationTime ({http://uri.etsi.org/m2m}expirationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element searchStrings ({http://uri.etsi.org/m2m}searchStrings) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element contentType ({http://uri.etsi.org/m2m}contentType) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element moID ({http://uri.etsi.org/m2m}moID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element description ({http://uri.etsi.org/m2m}description) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element {http://uri.etsi.org/m2m}numOfAreaNwks uses Python identifier numOfAreaNwks
    __numOfAreaNwks = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'numOfAreaNwks'),
        'numOfAreaNwks',
        '__httpuri_etsi_orgm2m_EtsiAreaNwkInfo_httpuri_etsi_orgm2mnumOfAreaNwks',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInfo.xsd',
            20, 4), )

    numOfAreaNwks = property(__numOfAreaNwks.value, __numOfAreaNwks.set, None,
                             None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}MgmtObj
    _HasWildcardElement = True
    _ElementMap.update({
        __numOfAreaNwks.name(): __numOfAreaNwks
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'EtsiAreaNwkInfo', EtsiAreaNwkInfo)


# Complex type {http://uri.etsi.org/m2m}AreaNwkInstance with content type ELEMENT_ONLY
class AreaNwkInstance(Parameters):
    """Complex type {http://uri.etsi.org/m2m}AreaNwkInstance with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AreaNwkInstance')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInstance.xsd',
        10, 4)
    _ElementMap = Parameters._ElementMap.copy()
    _AttributeMap = Parameters._AttributeMap.copy()
    # Base type is Parameters

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element {http://uri.etsi.org/m2m}areaNwkType uses Python identifier areaNwkType
    __areaNwkType = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'areaNwkType'), 'areaNwkType',
        '__httpuri_etsi_orgm2m_AreaNwkInstance_httpuri_etsi_orgm2mareaNwkType',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInstance.xsd',
            24, 4), )

    areaNwkType = property(__areaNwkType.value, __areaNwkType.set, None, None)


    # Element {http://uri.etsi.org/m2m}listOfDevices uses Python identifier listOfDevices
    __listOfDevices = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'listOfDevices'),
        'listOfDevices',
        '__httpuri_etsi_orgm2m_AreaNwkInstance_httpuri_etsi_orgm2mlistOfDevices',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInstance.xsd',
            39, 4), )

    listOfDevices = property(__listOfDevices.value, __listOfDevices.set, None,
                             None)


    # Element {http://uri.etsi.org/m2m}addressType uses Python identifier addressType
    __addressType = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'addressType'), 'addressType',
        '__httpuri_etsi_orgm2m_AreaNwkInstance_httpuri_etsi_orgm2maddressType',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInstance.xsd',
            40, 4), )

    addressType = property(__addressType.value, __addressType.set, None, None)


    # Element {http://uri.etsi.org/m2m}areaNwkTypeInfo uses Python identifier areaNwkTypeInfo
    __areaNwkTypeInfo = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'areaNwkTypeInfo'),
        'areaNwkTypeInfo',
        '__httpuri_etsi_orgm2m_AreaNwkInstance_httpuri_etsi_orgm2mareaNwkTypeInfo',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInstance.xsd',
            41, 4), )

    areaNwkTypeInfo = property(__areaNwkTypeInfo.value, __areaNwkTypeInfo.set,
                               None, None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}Parameters
    _HasWildcardElement = True
    _ElementMap.update({
        __areaNwkType.name(): __areaNwkType,
        __listOfDevices.name(): __listOfDevices,
        __addressType.name(): __addressType,
        __areaNwkTypeInfo.name(): __areaNwkTypeInfo
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'AreaNwkInstance', AreaNwkInstance)


# Complex type {http://uri.etsi.org/m2m}EtsiBattery with content type ELEMENT_ONLY
class EtsiBattery(MgmtObj):
    """Complex type {http://uri.etsi.org/m2m}EtsiBattery with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EtsiBattery')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiBattery.xsd', 9,
        4)
    _ElementMap = MgmtObj._ElementMap.copy()
    _AttributeMap = MgmtObj._AttributeMap.copy()
    # Base type is MgmtObj

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element expirationTime ({http://uri.etsi.org/m2m}expirationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element searchStrings ({http://uri.etsi.org/m2m}searchStrings) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element contentType ({http://uri.etsi.org/m2m}contentType) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element moID ({http://uri.etsi.org/m2m}moID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element description ({http://uri.etsi.org/m2m}description) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element {http://uri.etsi.org/m2m}standbyTime uses Python identifier standbyTime
    __standbyTime = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'standbyTime'), 'standbyTime',
        '__httpuri_etsi_orgm2m_EtsiBattery_httpuri_etsi_orgm2mstandbyTime',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiBattery.xsd',
            20, 4), )

    standbyTime = property(__standbyTime.value, __standbyTime.set, None,
                           u'\n                Contains the estimated time of operation. It is based on the\n                charge of all the batteries and it is expressed in minutes.\n            ')


    # Attribute id inherited from {http://uri.etsi.org/m2m}MgmtObj
    _HasWildcardElement = True
    _ElementMap.update({
        __standbyTime.name(): __standbyTime
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'EtsiBattery', EtsiBattery)


# Complex type {http://uri.etsi.org/m2m}BatteryInstance with content type ELEMENT_ONLY
class BatteryInstance(Parameters):
    """Complex type {http://uri.etsi.org/m2m}BatteryInstance with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BatteryInstance')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiBatteryInstance.xsd',
        9, 4)
    _ElementMap = Parameters._ElementMap.copy()
    _AttributeMap = Parameters._AttributeMap.copy()
    # Base type is Parameters

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element {http://uri.etsi.org/m2m}battLevel uses Python identifier battLevel
    __battLevel = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'battLevel'), 'battLevel',
        '__httpuri_etsi_orgm2m_BatteryInstance_httpuri_etsi_orgm2mbattLevel',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiBatteryInstance.xsd',
            20, 4), )

    battLevel = property(__battLevel.value, __battLevel.set, None,
                         u'\n                Contains the current battery level expressed in percentage.\n            ')


    # Element {http://uri.etsi.org/m2m}battStatus uses Python identifier battStatus
    __battStatus = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'battStatus'), 'battStatus',
        '__httpuri_etsi_orgm2m_BatteryInstance_httpuri_etsi_orgm2mbattStatus',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiBatteryInstance.xsd',
            35, 4), )

    battStatus = property(__battStatus.value, __battStatus.set, None,
                          u'\n                Indicates the status of the battery.\n            ')


    # Attribute id inherited from {http://uri.etsi.org/m2m}Parameters
    _HasWildcardElement = True
    _ElementMap.update({
        __battLevel.name(): __battLevel,
        __battStatus.name(): __battStatus
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'BatteryInstance', BatteryInstance)


# Complex type {http://uri.etsi.org/m2m}CapabilityAction  with content type ELEMENT_ONLY
class CapabilityAction(Parameters):
    """Complex type {http://uri.etsi.org/m2m}CapabilityAction  with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CapabilityAction ')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityAction.xsd',
        10, 4)
    _ElementMap = Parameters._ElementMap.copy()
    _AttributeMap = Parameters._AttributeMap.copy()
    # Base type is Parameters

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element {http://uri.etsi.org/m2m}devCapEnable uses Python identifier devCapEnable
    __devCapEnable = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'devCapEnable'), 'devCapEnable',
        '__httpuri_etsi_orgm2m_CapabilityAction_httpuri_etsi_orgm2mdevCapEnable',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityAction.xsd',
            22, 4), )

    devCapEnable = property(__devCapEnable.value, __devCapEnable.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}devCapDisable uses Python identifier devCapDisable
    __devCapDisable = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'devCapDisable'),
        'devCapDisable',
        '__httpuri_etsi_orgm2m_CapabilityAction_httpuri_etsi_orgm2mdevCapDisable',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityAction.xsd',
            23, 4), )

    devCapDisable = property(__devCapDisable.value, __devCapDisable.set, None,
                             None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}Parameters
    _HasWildcardElement = True
    _ElementMap.update({
        __devCapEnable.name(): __devCapEnable,
        __devCapDisable.name(): __devCapDisable
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'CapabilityAction ',
                            CapabilityAction)


# Complex type {http://uri.etsi.org/m2m}CapabilityInstance with content type ELEMENT_ONLY
class CapabilityInstance(Parameters):
    """Complex type {http://uri.etsi.org/m2m}CapabilityInstance with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'CapabilityInstance')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityInstance.xsd',
        10, 4)
    _ElementMap = Parameters._ElementMap.copy()
    _AttributeMap = Parameters._AttributeMap.copy()
    # Base type is Parameters

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element {http://uri.etsi.org/m2m}capabilityName uses Python identifier capabilityName
    __capabilityName = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'capabilityName'),
        'capabilityName',
        '__httpuri_etsi_orgm2m_CapabilityInstance_httpuri_etsi_orgm2mcapabilityName',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityInstance.xsd',
            23, 4), )

    capabilityName = property(__capabilityName.value, __capabilityName.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}attached uses Python identifier attached
    __attached = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'attached'), 'attached',
        '__httpuri_etsi_orgm2m_CapabilityInstance_httpuri_etsi_orgm2mattached',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityInstance.xsd',
            25, 4), )

    attached = property(__attached.value, __attached.set, None,
                        u'\n                When the Device Capability is removable, it indicates whether\n                the device is attached or not to the device.\n            ')


    # Element {http://uri.etsi.org/m2m}capabilityActionStatus uses Python identifier capabilityActionStatus
    __capabilityActionStatus = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'capabilityActionStatus'),
        'capabilityActionStatus',
        '__httpuri_etsi_orgm2m_CapabilityInstance_httpuri_etsi_orgm2mcapabilityActionStatus',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityInstance.xsd',
            40, 4), )

    capabilityActionStatus = property(__capabilityActionStatus.value,
                                      __capabilityActionStatus.set, None, None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}Parameters
    _HasWildcardElement = True
    _ElementMap.update({
        __capabilityName.name(): __capabilityName,
        __attached.name(): __attached,
        __capabilityActionStatus.name(): __capabilityActionStatus
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'CapabilityInstance',
                            CapabilityInstance)


# Complex type {http://uri.etsi.org/m2m}EtsiDeviceCapability with content type ELEMENT_ONLY
class EtsiDeviceCapability(MgmtObj):
    """Complex type {http://uri.etsi.org/m2m}EtsiDeviceCapability with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'EtsiDeviceCapability')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceCapability.xsd',
        9, 4)
    _ElementMap = MgmtObj._ElementMap.copy()
    _AttributeMap = MgmtObj._AttributeMap.copy()
    # Base type is MgmtObj

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element expirationTime ({http://uri.etsi.org/m2m}expirationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element searchStrings ({http://uri.etsi.org/m2m}searchStrings) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element contentType ({http://uri.etsi.org/m2m}contentType) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element moID ({http://uri.etsi.org/m2m}moID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element description ({http://uri.etsi.org/m2m}description) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Attribute id inherited from {http://uri.etsi.org/m2m}MgmtObj
    _HasWildcardElement = True
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'EtsiDeviceCapability',
                            EtsiDeviceCapability)


# Complex type {http://uri.etsi.org/m2m}EtsiDeviceInfo with content type ELEMENT_ONLY
class EtsiDeviceInfo(MgmtObj):
    """Complex type {http://uri.etsi.org/m2m}EtsiDeviceInfo with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EtsiDeviceInfo')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
        9, 4)
    _ElementMap = MgmtObj._ElementMap.copy()
    _AttributeMap = MgmtObj._AttributeMap.copy()
    # Base type is MgmtObj

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element expirationTime ({http://uri.etsi.org/m2m}expirationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element searchStrings ({http://uri.etsi.org/m2m}searchStrings) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element contentType ({http://uri.etsi.org/m2m}contentType) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element moID ({http://uri.etsi.org/m2m}moID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element description ({http://uri.etsi.org/m2m}description) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element {http://uri.etsi.org/m2m}firmwareVersion uses Python identifier firmwareVersion
    __firmwareVersion = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'firmwareVersion'),
        'firmwareVersion',
        '__httpuri_etsi_orgm2m_EtsiDeviceInfo_httpuri_etsi_orgm2mfirmwareVersion',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
            55, 4), )

    firmwareVersion = property(__firmwareVersion.value, __firmwareVersion.set,
                               None, None)


    # Element {http://uri.etsi.org/m2m}softwareVersion uses Python identifier softwareVersion
    __softwareVersion = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'softwareVersion'),
        'softwareVersion',
        '__httpuri_etsi_orgm2m_EtsiDeviceInfo_httpuri_etsi_orgm2msoftwareVersion',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
            57, 4), )

    softwareVersion = property(__softwareVersion.value, __softwareVersion.set,
                               None, None)


    # Element {http://uri.etsi.org/m2m}deviceLabel uses Python identifier deviceLabel
    __deviceLabel = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'deviceLabel'), 'deviceLabel',
        '__httpuri_etsi_orgm2m_EtsiDeviceInfo_httpuri_etsi_orgm2mdeviceLabel',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
            27, 4), )

    deviceLabel = property(__deviceLabel.value, __deviceLabel.set, None, None)


    # Element {http://uri.etsi.org/m2m}manufacturer uses Python identifier manufacturer
    __manufacturer = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'manufacturer'), 'manufacturer',
        '__httpuri_etsi_orgm2m_EtsiDeviceInfo_httpuri_etsi_orgm2mmanufacturer',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
            29, 4), )

    manufacturer = property(__manufacturer.value, __manufacturer.set, None,
                            u'\n                Manufacturer identifier.\n            ')


    # Element {http://uri.etsi.org/m2m}model uses Python identifier model
    __model = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'model'), 'model',
        '__httpuri_etsi_orgm2m_EtsiDeviceInfo_httpuri_etsi_orgm2mmodel', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
            37, 4), )

    model = property(__model.value, __model.set, None,
                     u'\n                Manufacturer specified string.\n            ')


    # Element {http://uri.etsi.org/m2m}deviceType uses Python identifier deviceType
    __deviceType = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'deviceType'), 'deviceType',
        '__httpuri_etsi_orgm2m_EtsiDeviceInfo_httpuri_etsi_orgm2mdeviceType',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
            45, 4), )

    deviceType = property(__deviceType.value, __deviceType.set, None,
                          u'\n                For example, PDA, meter, sensor, ... .\n            ')


    # Element {http://uri.etsi.org/m2m}hardwareVersion uses Python identifier hardwareVersion
    __hardwareVersion = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'hardwareVersion'),
        'hardwareVersion',
        '__httpuri_etsi_orgm2m_EtsiDeviceInfo_httpuri_etsi_orgm2mhardwareVersion',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
            54, 4), )

    hardwareVersion = property(__hardwareVersion.value, __hardwareVersion.set,
                               None, None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}MgmtObj
    _HasWildcardElement = True
    _ElementMap.update({
        __firmwareVersion.name(): __firmwareVersion,
        __softwareVersion.name(): __softwareVersion,
        __deviceLabel.name(): __deviceLabel,
        __manufacturer.name(): __manufacturer,
        __model.name(): __model,
        __deviceType.name(): __deviceType,
        __hardwareVersion.name(): __hardwareVersion
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'EtsiDeviceInfo', EtsiDeviceInfo)


# Complex type {http://uri.etsi.org/m2m}EtsiFirmware with content type ELEMENT_ONLY
class EtsiFirmware(MgmtObj):
    """Complex type {http://uri.etsi.org/m2m}EtsiFirmware with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EtsiFirmware')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmware.xsd',
        9, 4)
    _ElementMap = MgmtObj._ElementMap.copy()
    _AttributeMap = MgmtObj._AttributeMap.copy()
    # Base type is MgmtObj

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element expirationTime ({http://uri.etsi.org/m2m}expirationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element searchStrings ({http://uri.etsi.org/m2m}searchStrings) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element contentType ({http://uri.etsi.org/m2m}contentType) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element moID ({http://uri.etsi.org/m2m}moID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element description ({http://uri.etsi.org/m2m}description) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Attribute id inherited from {http://uri.etsi.org/m2m}MgmtObj
    _HasWildcardElement = True
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'EtsiFirmware', EtsiFirmware)


# Complex type {http://uri.etsi.org/m2m}FirmwareAction with content type ELEMENT_ONLY
class FirmwareAction(Parameters):
    """Complex type {http://uri.etsi.org/m2m}FirmwareAction with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'FirmwareAction')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareAction.xsd',
        9, 4)
    _ElementMap = Parameters._ElementMap.copy()
    _AttributeMap = Parameters._AttributeMap.copy()
    # Base type is Parameters

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element {http://uri.etsi.org/m2m}fwDownload uses Python identifier fwDownload
    __fwDownload = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'fwDownload'), 'fwDownload',
        '__httpuri_etsi_orgm2m_FirmwareAction_httpuri_etsi_orgm2mfwDownload',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareAction.xsd',
            22, 4), )

    fwDownload = property(__fwDownload.value, __fwDownload.set, None, None)


    # Element {http://uri.etsi.org/m2m}fwUpdate uses Python identifier fwUpdate
    __fwUpdate = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'fwUpdate'), 'fwUpdate',
        '__httpuri_etsi_orgm2m_FirmwareAction_httpuri_etsi_orgm2mfwUpdate',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareAction.xsd',
            23, 4), )

    fwUpdate = property(__fwUpdate.value, __fwUpdate.set, None, None)


    # Element {http://uri.etsi.org/m2m}fwDownloadAndUpdate uses Python identifier fwDownloadAndUpdate
    __fwDownloadAndUpdate = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'fwDownloadAndUpdate'),
        'fwDownloadAndUpdate',
        '__httpuri_etsi_orgm2m_FirmwareAction_httpuri_etsi_orgm2mfwDownloadAndUpdate',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareAction.xsd',
            24, 4), )

    fwDownloadAndUpdate = property(__fwDownloadAndUpdate.value,
                                   __fwDownloadAndUpdate.set, None, None)


    # Element {http://uri.etsi.org/m2m}fwRemove uses Python identifier fwRemove
    __fwRemove = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'fwRemove'), 'fwRemove',
        '__httpuri_etsi_orgm2m_FirmwareAction_httpuri_etsi_orgm2mfwRemove',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareAction.xsd',
            25, 4), )

    fwRemove = property(__fwRemove.value, __fwRemove.set, None, None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}Parameters
    _HasWildcardElement = True
    _ElementMap.update({
        __fwDownload.name(): __fwDownload,
        __fwUpdate.name(): __fwUpdate,
        __fwDownloadAndUpdate.name(): __fwDownloadAndUpdate,
        __fwRemove.name(): __fwRemove
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'FirmwareAction', FirmwareAction)


# Complex type {http://uri.etsi.org/m2m}FwInstance with content type ELEMENT_ONLY
class FwInstance(Parameters):
    """Complex type {http://uri.etsi.org/m2m}FwInstance with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'FwInstance')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareInstance.xsd',
        9, 4)
    _ElementMap = Parameters._ElementMap.copy()
    _AttributeMap = Parameters._AttributeMap.copy()
    # Base type is Parameters

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element {http://uri.etsi.org/m2m}firmwareVersion uses Python identifier firmwareVersion
    __firmwareVersion = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'firmwareVersion'),
        'firmwareVersion',
        '__httpuri_etsi_orgm2m_FwInstance_httpuri_etsi_orgm2mfirmwareVersion',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
            55, 4), )

    firmwareVersion = property(__firmwareVersion.value, __firmwareVersion.set,
                               None, None)


    # Element {http://uri.etsi.org/m2m}firmwareName uses Python identifier firmwareName
    __firmwareName = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'firmwareName'), 'firmwareName',
        '__httpuri_etsi_orgm2m_FwInstance_httpuri_etsi_orgm2mfirmwareName',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareInstance.xsd',
            23, 4), )

    firmwareName = property(__firmwareName.value, __firmwareName.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}firmwareURL uses Python identifier firmwareURL
    __firmwareURL = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'firmwareURL'), 'firmwareURL',
        '__httpuri_etsi_orgm2m_FwInstance_httpuri_etsi_orgm2mfirmwareURL',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareInstance.xsd',
            31, 4), )

    firmwareURL = property(__firmwareURL.value, __firmwareURL.set, None, None)


    # Element {http://uri.etsi.org/m2m}fwActionStatus uses Python identifier fwActionStatus
    __fwActionStatus = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'fwActionStatus'),
        'fwActionStatus',
        '__httpuri_etsi_orgm2m_FwInstance_httpuri_etsi_orgm2mfwActionStatus',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareInstance.xsd',
            39, 4), )

    fwActionStatus = property(__fwActionStatus.value, __fwActionStatus.set,
                              None, None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}Parameters
    _HasWildcardElement = True
    _ElementMap.update({
        __firmwareVersion.name(): __firmwareVersion,
        __firmwareName.name(): __firmwareName,
        __firmwareURL.name(): __firmwareURL,
        __fwActionStatus.name(): __fwActionStatus
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'FwInstance', FwInstance)


# Complex type {http://uri.etsi.org/m2m}M2mSpPolicy with content type ELEMENT_ONLY
class M2mSpPolicy(Parameters):
    """Complex type {http://uri.etsi.org/m2m}M2mSpPolicy with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'M2mSpPolicy')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiM2mSpPolicy.xsd',
        11, 4)
    _ElementMap = Parameters._ElementMap.copy()
    _AttributeMap = Parameters._AttributeMap.copy()
    # Base type is Parameters

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element {http://uri.etsi.org/m2m}defaultRcatValue uses Python identifier defaultRcatValue
    __defaultRcatValue = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'defaultRcatValue'),
        'defaultRcatValue',
        '__httpuri_etsi_orgm2m_M2mSpPolicy_httpuri_etsi_orgm2mdefaultRcatValue',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiM2mSpPolicy.xsd',
            21, 4), )

    defaultRcatValue = property(__defaultRcatValue.value,
                                __defaultRcatValue.set, None, None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}Parameters
    _HasWildcardElement = True
    _ElementMap.update({
        __defaultRcatValue.name(): __defaultRcatValue
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'M2mSpPolicy', M2mSpPolicy)


# Complex type {http://uri.etsi.org/m2m}EtsiMemory with content type ELEMENT_ONLY
class EtsiMemory(MgmtObj):
    """Complex type {http://uri.etsi.org/m2m}EtsiMemory with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EtsiMemory')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiMemory.xsd', 9,
        4)
    _ElementMap = MgmtObj._ElementMap.copy()
    _AttributeMap = MgmtObj._AttributeMap.copy()
    # Base type is MgmtObj

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element expirationTime ({http://uri.etsi.org/m2m}expirationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element searchStrings ({http://uri.etsi.org/m2m}searchStrings) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element contentType ({http://uri.etsi.org/m2m}contentType) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element moID ({http://uri.etsi.org/m2m}moID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element description ({http://uri.etsi.org/m2m}description) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element {http://uri.etsi.org/m2m}ramAvailable uses Python identifier ramAvailable
    __ramAvailable = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'ramAvailable'), 'ramAvailable',
        '__httpuri_etsi_orgm2m_EtsiMemory_httpuri_etsi_orgm2mramAvailable',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiMemory.xsd',
            21, 4), )

    ramAvailable = property(__ramAvailable.value, __ramAvailable.set, None,
                            u'\n                Expressed in kilobytes.\n            ')


    # Element {http://uri.etsi.org/m2m}ramTotal uses Python identifier ramTotal
    __ramTotal = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'ramTotal'), 'ramTotal',
        '__httpuri_etsi_orgm2m_EtsiMemory_httpuri_etsi_orgm2mramTotal', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiMemory.xsd',
            29, 4), )

    ramTotal = property(__ramTotal.value, __ramTotal.set, None,
                        u'\n                Expressed in kilobytes.\n            ')


    # Attribute id inherited from {http://uri.etsi.org/m2m}MgmtObj
    _HasWildcardElement = True
    _ElementMap.update({
        __ramAvailable.name(): __ramAvailable,
        __ramTotal.name(): __ramTotal
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'EtsiMemory', EtsiMemory)


# Complex type {http://uri.etsi.org/m2m}PerfLogAction with content type ELEMENT_ONLY
class PerfLogAction(Parameters):
    """Complex type {http://uri.etsi.org/m2m}PerfLogAction with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PerfLogAction')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerfLogAction.xsd',
        9, 4)
    _ElementMap = Parameters._ElementMap.copy()
    _AttributeMap = Parameters._AttributeMap.copy()
    # Base type is Parameters

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element {http://uri.etsi.org/m2m}perfLogStart uses Python identifier perfLogStart
    __perfLogStart = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'perfLogStart'), 'perfLogStart',
        '__httpuri_etsi_orgm2m_PerfLogAction_httpuri_etsi_orgm2mperfLogStart',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerfLogAction.xsd',
            21, 4), )

    perfLogStart = property(__perfLogStart.value, __perfLogStart.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}perfLogStop uses Python identifier perfLogStop
    __perfLogStop = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'perfLogStop'), 'perfLogStop',
        '__httpuri_etsi_orgm2m_PerfLogAction_httpuri_etsi_orgm2mperfLogStop',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerfLogAction.xsd',
            22, 4), )

    perfLogStop = property(__perfLogStop.value, __perfLogStop.set, None, None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}Parameters
    _HasWildcardElement = True
    _ElementMap.update({
        __perfLogStart.name(): __perfLogStart,
        __perfLogStop.name(): __perfLogStop
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'PerfLogAction', PerfLogAction)


# Complex type {http://uri.etsi.org/m2m}EtsiPerformanceLog with content type ELEMENT_ONLY
class EtsiPerformanceLog(MgmtObj):
    """Complex type {http://uri.etsi.org/m2m}EtsiPerformanceLog with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace,
                                                u'EtsiPerformanceLog')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerformanceLog.xsd',
        9, 4)
    _ElementMap = MgmtObj._ElementMap.copy()
    _AttributeMap = MgmtObj._AttributeMap.copy()
    # Base type is MgmtObj

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element expirationTime ({http://uri.etsi.org/m2m}expirationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element searchStrings ({http://uri.etsi.org/m2m}searchStrings) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element contentType ({http://uri.etsi.org/m2m}contentType) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element moID ({http://uri.etsi.org/m2m}moID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element description ({http://uri.etsi.org/m2m}description) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element {http://uri.etsi.org/m2m}logTypeId uses Python identifier logTypeId
    __logTypeId = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'logTypeId'), 'logTypeId',
        '__httpuri_etsi_orgm2m_EtsiPerformanceLog_httpuri_etsi_orgm2mlogTypeId',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerformanceLog.xsd',
            22, 4), )

    logTypeId = property(__logTypeId.value, __logTypeId.set, None, None)


    # Element {http://uri.etsi.org/m2m}logData uses Python identifier logData
    __logData = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'logData'), 'logData',
        '__httpuri_etsi_orgm2m_EtsiPerformanceLog_httpuri_etsi_orgm2mlogData',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerformanceLog.xsd',
            31, 4), )

    logData = property(__logData.value, __logData.set, None, None)


    # Element {http://uri.etsi.org/m2m}perfoLogActionStatus uses Python identifier perfoLogActionStatus
    __perfoLogActionStatus = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'perfoLogActionStatus'),
        'perfoLogActionStatus',
        '__httpuri_etsi_orgm2m_EtsiPerformanceLog_httpuri_etsi_orgm2mperfoLogActionStatus',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerformanceLog.xsd',
            39, 4), )

    perfoLogActionStatus = property(__perfoLogActionStatus.value,
                                    __perfoLogActionStatus.set, None, None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}MgmtObj
    _HasWildcardElement = True
    _ElementMap.update({
        __logTypeId.name(): __logTypeId,
        __logData.name(): __logData,
        __perfoLogActionStatus.name(): __perfoLogActionStatus
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'EtsiPerformanceLog',
                            EtsiPerformanceLog)


# Complex type {http://uri.etsi.org/m2m}RcatParamList with content type ELEMENT_ONLY
class RcatParamList(Parameters):
    """Complex type {http://uri.etsi.org/m2m}RcatParamList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RcatParamList')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
        9, 4)
    _ElementMap = Parameters._ElementMap.copy()
    _AttributeMap = Parameters._AttributeMap.copy()
    # Base type is Parameters

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element {http://uri.etsi.org/m2m}rcatValue uses Python identifier rcatValue
    __rcatValue = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'rcatValue'), 'rcatValue',
        '__httpuri_etsi_orgm2m_RcatParamList_httpuri_etsi_orgm2mrcatValue',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
            53, 4), )

    rcatValue = property(__rcatValue.value, __rcatValue.set, None, None)


    # Element {http://uri.etsi.org/m2m}defaultTrpdtValue uses Python identifier defaultTrpdtValue
    __defaultTrpdtValue = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'defaultTrpdtValue'),
        'defaultTrpdtValue',
        '__httpuri_etsi_orgm2m_RcatParamList_httpuri_etsi_orgm2mdefaultTrpdtValue',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
            25, 4), )

    defaultTrpdtValue = property(__defaultTrpdtValue.value,
                                 __defaultTrpdtValue.set, None, None)


    # Element {http://uri.etsi.org/m2m}maxPendReqs uses Python identifier maxPendReqs
    __maxPendReqs = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'maxPendReqs'), 'maxPendReqs',
        '__httpuri_etsi_orgm2m_RcatParamList_httpuri_etsi_orgm2mmaxPendReqs',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
            26, 4), )

    maxPendReqs = property(__maxPendReqs.value, __maxPendReqs.set, None, None)


    # Element {http://uri.etsi.org/m2m}maxPendData uses Python identifier maxPendData
    __maxPendData = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'maxPendData'), 'maxPendData',
        '__httpuri_etsi_orgm2m_RcatParamList_httpuri_etsi_orgm2mmaxPendData',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
            27, 4), )

    maxPendData = property(__maxPendData.value, __maxPendData.set, None, None)


    # Element {http://uri.etsi.org/m2m}rankedAnList uses Python identifier rankedAnList
    __rankedAnList = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'rankedAnList'), 'rankedAnList',
        '__httpuri_etsi_orgm2m_RcatParamList_httpuri_etsi_orgm2mrankedAnList',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
            28, 4), )

    rankedAnList = property(__rankedAnList.value, __rankedAnList.set, None,
                            None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}Parameters
    _HasWildcardElement = True
    _ElementMap.update({
        __rcatValue.name(): __rcatValue,
        __defaultTrpdtValue.name(): __defaultTrpdtValue,
        __maxPendReqs.name(): __maxPendReqs,
        __maxPendData.name(): __maxPendData,
        __rankedAnList.name(): __rankedAnList
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'RcatParamList', RcatParamList)


# Complex type {http://uri.etsi.org/m2m}EtsiReboot with content type ELEMENT_ONLY
class EtsiReboot(MgmtObj):
    """Complex type {http://uri.etsi.org/m2m}EtsiReboot with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EtsiReboot')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd', 9,
        4)
    _ElementMap = MgmtObj._ElementMap.copy()
    _AttributeMap = MgmtObj._AttributeMap.copy()
    # Base type is MgmtObj

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element expirationTime ({http://uri.etsi.org/m2m}expirationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element searchStrings ({http://uri.etsi.org/m2m}searchStrings) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element contentType ({http://uri.etsi.org/m2m}contentType) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element moID ({http://uri.etsi.org/m2m}moID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element description ({http://uri.etsi.org/m2m}description) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element {http://uri.etsi.org/m2m}rebootLevel uses Python identifier rebootLevel
    __rebootLevel = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'rebootLevel'), 'rebootLevel',
        '__httpuri_etsi_orgm2m_EtsiReboot_httpuri_etsi_orgm2mrebootLevel',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd',
            23, 4), )

    rebootLevel = property(__rebootLevel.value, __rebootLevel.set, None,
                           u'\n                Indicates the level at which the reboot operation has to be\n                performed.\n            ')


    # Element {http://uri.etsi.org/m2m}applicationRef uses Python identifier applicationRef
    __applicationRef = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'applicationRef'),
        'applicationRef',
        '__httpuri_etsi_orgm2m_EtsiReboot_httpuri_etsi_orgm2mapplicationRef',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd',
            40, 4), )

    applicationRef = property(__applicationRef.value, __applicationRef.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}rebootTiming uses Python identifier rebootTiming
    __rebootTiming = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'rebootTiming'), 'rebootTiming',
        '__httpuri_etsi_orgm2m_EtsiReboot_httpuri_etsi_orgm2mrebootTiming',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd',
            42, 4), )

    rebootTiming = property(__rebootTiming.value, __rebootTiming.set, None,
                            u'\n                Indicates the timing of the requested reboot.\n            ')


    # Element {http://uri.etsi.org/m2m}rebootActionStatus uses Python identifier rebootActionStatus
    __rebootActionStatus = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'rebootActionStatus'),
        'rebootActionStatus',
        '__httpuri_etsi_orgm2m_EtsiReboot_httpuri_etsi_orgm2mrebootActionStatus',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd',
            57, 4), )

    rebootActionStatus = property(__rebootActionStatus.value,
                                  __rebootActionStatus.set, None, None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}MgmtObj
    _HasWildcardElement = True
    _ElementMap.update({
        __rebootLevel.name(): __rebootLevel,
        __applicationRef.name(): __applicationRef,
        __rebootTiming.name(): __rebootTiming,
        __rebootActionStatus.name(): __rebootActionStatus
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'EtsiReboot', EtsiReboot)


# Complex type {http://uri.etsi.org/m2m}RebootAction with content type ELEMENT_ONLY
class RebootAction(Parameters):
    """Complex type {http://uri.etsi.org/m2m}RebootAction with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RebootAction')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRebootAction.xsd',
        10, 4)
    _ElementMap = Parameters._ElementMap.copy()
    _AttributeMap = Parameters._AttributeMap.copy()
    # Base type is Parameters

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element {http://uri.etsi.org/m2m}reboot uses Python identifier reboot
    __reboot = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'reboot'), 'reboot',
        '__httpuri_etsi_orgm2m_RebootAction_httpuri_etsi_orgm2mreboot', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRebootAction.xsd',
            22, 4), )

    reboot = property(__reboot.value, __reboot.set, None, None)


    # Element {http://uri.etsi.org/m2m}factoryReset uses Python identifier factoryReset
    __factoryReset = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'factoryReset'), 'factoryReset',
        '__httpuri_etsi_orgm2m_RebootAction_httpuri_etsi_orgm2mfactoryReset',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRebootAction.xsd',
            24, 4), )

    factoryReset = property(__factoryReset.value, __factoryReset.set, None,
                            None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}Parameters
    _HasWildcardElement = True
    _ElementMap.update({
        __reboot.name(): __reboot,
        __factoryReset.name(): __factoryReset
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'RebootAction', RebootAction)


# Complex type {http://uri.etsi.org/m2m}SafPolicySet with content type ELEMENT_ONLY
class SafPolicySet(Parameters):
    """Complex type {http://uri.etsi.org/m2m}SafPolicySet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SafPolicySet')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSafPolicySet.xsd',
        11, 4)
    _ElementMap = Parameters._ElementMap.copy()
    _AttributeMap = Parameters._AttributeMap.copy()
    # Base type is Parameters

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element {http://uri.etsi.org/m2m}policyScope uses Python identifier policyScope
    __policyScope = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'policyScope'), 'policyScope',
        '__httpuri_etsi_orgm2m_SafPolicySet_httpuri_etsi_orgm2mpolicyScope',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSafPolicySet.xsd',
            22, 4), )

    policyScope = property(__policyScope.value, __policyScope.set, None, None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}Parameters
    _HasWildcardElement = True
    _ElementMap.update({
        __policyScope.name(): __policyScope
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'SafPolicySet', SafPolicySet)


# Complex type {http://uri.etsi.org/m2m}EtsiSclMo with content type ELEMENT_ONLY
class EtsiSclMo(MgmtObj):
    """Complex type {http://uri.etsi.org/m2m}EtsiSclMo with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EtsiSclMo')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd', 10,
        4)
    _ElementMap = MgmtObj._ElementMap.copy()
    _AttributeMap = MgmtObj._AttributeMap.copy()
    # Base type is MgmtObj

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element expirationTime ({http://uri.etsi.org/m2m}expirationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element searchStrings ({http://uri.etsi.org/m2m}searchStrings) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element contentType ({http://uri.etsi.org/m2m}contentType) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element moID ({http://uri.etsi.org/m2m}moID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element description ({http://uri.etsi.org/m2m}description) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element {http://uri.etsi.org/m2m}regTargetNsclList uses Python identifier regTargetNsclList
    __regTargetNsclList = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'regTargetNsclList'),
        'regTargetNsclList',
        '__httpuri_etsi_orgm2m_EtsiSclMo_httpuri_etsi_orgm2mregTargetNsclList',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
            28, 4), )

    regTargetNsclList = property(__regTargetNsclList.value,
                                 __regTargetNsclList.set, None, None)


    # Element {http://uri.etsi.org/m2m}regExpirationDuration uses Python identifier regExpirationDuration
    __regExpirationDuration = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'regExpirationDuration'),
        'regExpirationDuration',
        '__httpuri_etsi_orgm2m_EtsiSclMo_httpuri_etsi_orgm2mregExpirationDuration',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
            29, 4), )

    regExpirationDuration = property(__regExpirationDuration.value,
                                     __regExpirationDuration.set, None, None)


    # Element {http://uri.etsi.org/m2m}regAccessRightID uses Python identifier regAccessRightID
    __regAccessRightID = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'regAccessRightID'),
        'regAccessRightID',
        '__httpuri_etsi_orgm2m_EtsiSclMo_httpuri_etsi_orgm2mregAccessRightID',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
            30, 4), )

    regAccessRightID = property(__regAccessRightID.value,
                                __regAccessRightID.set, None, None)


    # Element {http://uri.etsi.org/m2m}regSearchStrings uses Python identifier regSearchStrings
    __regSearchStrings = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'regSearchStrings'),
        'regSearchStrings',
        '__httpuri_etsi_orgm2m_EtsiSclMo_httpuri_etsi_orgm2mregSearchStrings',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
            31, 4), )

    regSearchStrings = property(__regSearchStrings.value,
                                __regSearchStrings.set, None, None)


    # Element {http://uri.etsi.org/m2m}announcedToSclList uses Python identifier announcedToSclList
    __announcedToSclList = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'announcedToSclList'),
        'announcedToSclList',
        '__httpuri_etsi_orgm2m_EtsiSclMo_httpuri_etsi_orgm2mannouncedToSclList',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
            32, 4), )

    announcedToSclList = property(__announcedToSclList.value,
                                  __announcedToSclList.set, None, None)


    # Element {http://uri.etsi.org/m2m}maxNumberOfDiscovRecords uses Python identifier maxNumberOfDiscovRecords
    __maxNumberOfDiscovRecords = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'maxNumberOfDiscovRecords'),
        'maxNumberOfDiscovRecords',
        '__httpuri_etsi_orgm2m_EtsiSclMo_httpuri_etsi_orgm2mmaxNumberOfDiscovRecords',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
            33, 4), )

    maxNumberOfDiscovRecords = property(__maxNumberOfDiscovRecords.value,
                                        __maxNumberOfDiscovRecords.set, None,
                                        None)


    # Element {http://uri.etsi.org/m2m}maxSizeOfDiscovAnswer uses Python identifier maxSizeOfDiscovAnswer
    __maxSizeOfDiscovAnswer = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'maxSizeOfDiscovAnswer'),
        'maxSizeOfDiscovAnswer',
        '__httpuri_etsi_orgm2m_EtsiSclMo_httpuri_etsi_orgm2mmaxSizeOfDiscovAnswer',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
            34, 4), )

    maxSizeOfDiscovAnswer = property(__maxSizeOfDiscovAnswer.value,
                                     __maxSizeOfDiscovAnswer.set, None, None)


    # Element {http://uri.etsi.org/m2m}sclActionStatus uses Python identifier sclActionStatus
    __sclActionStatus = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'sclActionStatus'),
        'sclActionStatus',
        '__httpuri_etsi_orgm2m_EtsiSclMo_httpuri_etsi_orgm2msclActionStatus',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
            35, 4), )

    sclActionStatus = property(__sclActionStatus.value, __sclActionStatus.set,
                               None, None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}MgmtObj
    _HasWildcardElement = True
    _ElementMap.update({
        __regTargetNsclList.name(): __regTargetNsclList,
        __regExpirationDuration.name(): __regExpirationDuration,
        __regAccessRightID.name(): __regAccessRightID,
        __regSearchStrings.name(): __regSearchStrings,
        __announcedToSclList.name(): __announcedToSclList,
        __maxNumberOfDiscovRecords.name(): __maxNumberOfDiscovRecords,
        __maxSizeOfDiscovAnswer.name(): __maxSizeOfDiscovAnswer,
        __sclActionStatus.name(): __sclActionStatus
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'EtsiSclMo', EtsiSclMo)


# Complex type {http://uri.etsi.org/m2m}SclMoAction with content type ELEMENT_ONLY
class SclMoAction(Parameters):
    """Complex type {http://uri.etsi.org/m2m}SclMoAction with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SclMoAction')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMoAction.xsd',
        9, 4)
    _ElementMap = Parameters._ElementMap.copy()
    _AttributeMap = Parameters._AttributeMap.copy()
    # Base type is Parameters

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element {http://uri.etsi.org/m2m}reRegistration uses Python identifier reRegistration
    __reRegistration = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'reRegistration'),
        'reRegistration',
        '__httpuri_etsi_orgm2m_SclMoAction_httpuri_etsi_orgm2mreRegistration',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMoAction.xsd',
            21, 4), )

    reRegistration = property(__reRegistration.value, __reRegistration.set,
                              None, None)


    # Element {http://uri.etsi.org/m2m}deRegistration uses Python identifier deRegistration
    __deRegistration = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'deRegistration'),
        'deRegistration',
        '__httpuri_etsi_orgm2m_SclMoAction_httpuri_etsi_orgm2mdeRegistration',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMoAction.xsd',
            22, 4), )

    deRegistration = property(__deRegistration.value, __deRegistration.set,
                              None, None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}Parameters
    _HasWildcardElement = True
    _ElementMap.update({
        __reRegistration.name(): __reRegistration,
        __deRegistration.name(): __deRegistration
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'SclMoAction', SclMoAction)


# Complex type {http://uri.etsi.org/m2m}EtsiSoftware with content type ELEMENT_ONLY
class EtsiSoftware(MgmtObj):
    """Complex type {http://uri.etsi.org/m2m}EtsiSoftware with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EtsiSoftware')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftware.xsd',
        9, 4)
    _ElementMap = MgmtObj._ElementMap.copy()
    _AttributeMap = MgmtObj._AttributeMap.copy()
    # Base type is MgmtObj

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element expirationTime ({http://uri.etsi.org/m2m}expirationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element searchStrings ({http://uri.etsi.org/m2m}searchStrings) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element contentType ({http://uri.etsi.org/m2m}contentType) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element moID ({http://uri.etsi.org/m2m}moID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element description ({http://uri.etsi.org/m2m}description) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Attribute id inherited from {http://uri.etsi.org/m2m}MgmtObj
    _HasWildcardElement = True
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'EtsiSoftware', EtsiSoftware)


# Complex type {http://uri.etsi.org/m2m}SoftwareAction with content type ELEMENT_ONLY
class SoftwareAction(Parameters):
    """Complex type {http://uri.etsi.org/m2m}SoftwareAction with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SoftwareAction')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
        10, 4)
    _ElementMap = Parameters._ElementMap.copy()
    _AttributeMap = Parameters._AttributeMap.copy()
    # Base type is Parameters

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element {http://uri.etsi.org/m2m}swDownload uses Python identifier swDownload
    __swDownload = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'swDownload'), 'swDownload',
        '__httpuri_etsi_orgm2m_SoftwareAction_httpuri_etsi_orgm2mswDownload',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
            26, 4), )

    swDownload = property(__swDownload.value, __swDownload.set, None, None)


    # Element {http://uri.etsi.org/m2m}swDownloadAndInstall uses Python identifier swDownloadAndInstall
    __swDownloadAndInstall = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'swDownloadAndInstall'),
        'swDownloadAndInstall',
        '__httpuri_etsi_orgm2m_SoftwareAction_httpuri_etsi_orgm2mswDownloadAndInstall',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
            27, 4), )

    swDownloadAndInstall = property(__swDownloadAndInstall.value,
                                    __swDownloadAndInstall.set, None, None)


    # Element {http://uri.etsi.org/m2m}swInstall uses Python identifier swInstall
    __swInstall = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'swInstall'), 'swInstall',
        '__httpuri_etsi_orgm2m_SoftwareAction_httpuri_etsi_orgm2mswInstall',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
            28, 4), )

    swInstall = property(__swInstall.value, __swInstall.set, None, None)


    # Element {http://uri.etsi.org/m2m}swRemove uses Python identifier swRemove
    __swRemove = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'swRemove'), 'swRemove',
        '__httpuri_etsi_orgm2m_SoftwareAction_httpuri_etsi_orgm2mswRemove',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
            29, 4), )

    swRemove = property(__swRemove.value, __swRemove.set, None, None)


    # Element {http://uri.etsi.org/m2m}swActivate uses Python identifier swActivate
    __swActivate = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'swActivate'), 'swActivate',
        '__httpuri_etsi_orgm2m_SoftwareAction_httpuri_etsi_orgm2mswActivate',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
            30, 4), )

    swActivate = property(__swActivate.value, __swActivate.set, None, None)


    # Element {http://uri.etsi.org/m2m}swDeactivate uses Python identifier swDeactivate
    __swDeactivate = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'swDeactivate'), 'swDeactivate',
        '__httpuri_etsi_orgm2m_SoftwareAction_httpuri_etsi_orgm2mswDeactivate',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
            31, 4), )

    swDeactivate = property(__swDeactivate.value, __swDeactivate.set, None,
                            None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}Parameters
    _HasWildcardElement = True
    _ElementMap.update({
        __swDownload.name(): __swDownload,
        __swDownloadAndInstall.name(): __swDownloadAndInstall,
        __swInstall.name(): __swInstall,
        __swRemove.name(): __swRemove,
        __swActivate.name(): __swActivate,
        __swDeactivate.name(): __swDeactivate
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'SoftwareAction', SoftwareAction)


# Complex type {http://uri.etsi.org/m2m}SwInstance with content type ELEMENT_ONLY
class SwInstance(Parameters):
    """Complex type {http://uri.etsi.org/m2m}SwInstance with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SwInstance')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareInstance.xsd',
        9, 4)
    _ElementMap = Parameters._ElementMap.copy()
    _AttributeMap = Parameters._AttributeMap.copy()
    # Base type is Parameters

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element {http://uri.etsi.org/m2m}softwareVersion uses Python identifier softwareVersion
    __softwareVersion = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'softwareVersion'),
        'softwareVersion',
        '__httpuri_etsi_orgm2m_SwInstance_httpuri_etsi_orgm2msoftwareVersion',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
            57, 4), )

    softwareVersion = property(__softwareVersion.value, __softwareVersion.set,
                               None, None)


    # Element {http://uri.etsi.org/m2m}softwareName uses Python identifier softwareName
    __softwareName = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'softwareName'), 'softwareName',
        '__httpuri_etsi_orgm2m_SwInstance_httpuri_etsi_orgm2msoftwareName',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareInstance.xsd',
            23, 4), )

    softwareName = property(__softwareName.value, __softwareName.set, None,
                            None)


    # Element {http://uri.etsi.org/m2m}softwareURL uses Python identifier softwareURL
    __softwareURL = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'softwareURL'), 'softwareURL',
        '__httpuri_etsi_orgm2m_SwInstance_httpuri_etsi_orgm2msoftwareURL',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareInstance.xsd',
            32, 4), )

    softwareURL = property(__softwareURL.value, __softwareURL.set, None, None)


    # Element {http://uri.etsi.org/m2m}swActionStatus uses Python identifier swActionStatus
    __swActionStatus = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'swActionStatus'),
        'swActionStatus',
        '__httpuri_etsi_orgm2m_SwInstance_httpuri_etsi_orgm2mswActionStatus',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareInstance.xsd',
            40, 4), )

    swActionStatus = property(__swActionStatus.value, __swActionStatus.set,
                              None, None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}Parameters
    _HasWildcardElement = True
    _ElementMap.update({
        __softwareVersion.name(): __softwareVersion,
        __softwareName.name(): __softwareName,
        __softwareURL.name(): __softwareURL,
        __swActionStatus.name(): __swActionStatus
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'SwInstance', SwInstance)


# Complex type {http://uri.etsi.org/m2m}EtsiTrapEvent with content type ELEMENT_ONLY
class EtsiTrapEvent(MgmtObj):
    """Complex type {http://uri.etsi.org/m2m}EtsiTrapEvent with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EtsiTrapEvent')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapEvent.xsd',
        9, 4)
    _ElementMap = MgmtObj._ElementMap.copy()
    _AttributeMap = MgmtObj._AttributeMap.copy()
    # Base type is MgmtObj

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element expirationTime ({http://uri.etsi.org/m2m}expirationTime) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element searchStrings ({http://uri.etsi.org/m2m}searchStrings) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element contentType ({http://uri.etsi.org/m2m}contentType) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element moID ({http://uri.etsi.org/m2m}moID) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element description ({http://uri.etsi.org/m2m}description) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}MgmtObj

    # Attribute id inherited from {http://uri.etsi.org/m2m}MgmtObj
    _HasWildcardElement = True
    _ElementMap.update({

    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'EtsiTrapEvent', EtsiTrapEvent)


# Complex type {http://uri.etsi.org/m2m}TrapEventAction with content type ELEMENT_ONLY
class TrapEventAction(Parameters):
    """Complex type {http://uri.etsi.org/m2m}TrapEventAction with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TrapEventAction')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapEventAction.xsd',
        9, 4)
    _ElementMap = Parameters._ElementMap.copy()
    _AttributeMap = Parameters._AttributeMap.copy()
    # Base type is Parameters

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element {http://uri.etsi.org/m2m}trapEventEnable uses Python identifier trapEventEnable
    __trapEventEnable = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'trapEventEnable'),
        'trapEventEnable',
        '__httpuri_etsi_orgm2m_TrapEventAction_httpuri_etsi_orgm2mtrapEventEnable',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapEventAction.xsd',
            21, 4), )

    trapEventEnable = property(__trapEventEnable.value, __trapEventEnable.set,
                               None, None)


    # Element {http://uri.etsi.org/m2m}trapEventDisable uses Python identifier trapEventDisable
    __trapEventDisable = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'trapEventDisable'),
        'trapEventDisable',
        '__httpuri_etsi_orgm2m_TrapEventAction_httpuri_etsi_orgm2mtrapEventDisable',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapEventAction.xsd',
            23, 4), )

    trapEventDisable = property(__trapEventDisable.value,
                                __trapEventDisable.set, None, None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}Parameters
    _HasWildcardElement = True
    _ElementMap.update({
        __trapEventEnable.name(): __trapEventEnable,
        __trapEventDisable.name(): __trapEventDisable
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'TrapEventAction', TrapEventAction)


# Complex type {http://uri.etsi.org/m2m}TrapInstance  with content type ELEMENT_ONLY
class TrapInstance(Parameters):
    """Complex type {http://uri.etsi.org/m2m}TrapInstance  with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TrapInstance ')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
        9, 4)
    _ElementMap = Parameters._ElementMap.copy()
    _AttributeMap = Parameters._AttributeMap.copy()
    # Base type is Parameters

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element originalMO ({http://uri.etsi.org/m2m}originalMO) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element parametersCollection ({http://uri.etsi.org/m2m}parametersCollection) inherited from {http://uri.etsi.org/m2m}Parameters

    # Element {http://uri.etsi.org/m2m}trapId uses Python identifier trapId
    __trapId = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'trapId'), 'trapId',
        '__httpuri_etsi_orgm2m_TrapInstance_httpuri_etsi_orgm2mtrapId', False,
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
            23, 4), )

    trapId = property(__trapId.value, __trapId.set, None, None)


    # Element {http://uri.etsi.org/m2m}eventOccured uses Python identifier eventOccured
    __eventOccured = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'eventOccured'), 'eventOccured',
        '__httpuri_etsi_orgm2m_TrapInstance_httpuri_etsi_orgm2meventOccured',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
            25, 4), )

    eventOccured = property(__eventOccured.value, __eventOccured.set, None,
                            u'\n                This element indicates the last occurences of the event.\n            ')


    # Element {http://uri.etsi.org/m2m}trapActionStatus uses Python identifier trapActionStatus
    __trapActionStatus = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'trapActionStatus'),
        'trapActionStatus',
        '__httpuri_etsi_orgm2m_TrapInstance_httpuri_etsi_orgm2mtrapActionStatus',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
            60, 4), )

    trapActionStatus = property(__trapActionStatus.value,
                                __trapActionStatus.set, None, None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}Parameters
    _HasWildcardElement = True
    _ElementMap.update({
        __trapId.name(): __trapId,
        __eventOccured.name(): __eventOccured,
        __trapActionStatus.name(): __trapActionStatus
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'TrapInstance ', TrapInstance)


# Complex type {http://uri.etsi.org/m2m}LocationContainer with content type ELEMENT_ONLY
class LocationContainer(Container):
    """Complex type {http://uri.etsi.org/m2m}LocationContainer with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LocationContainer')
    _XSDLocation = pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/locationContainer.xsd',
        10, 4)
    _ElementMap = Container._ElementMap.copy()
    _AttributeMap = Container._AttributeMap.copy()
    # Base type is Container

    # Element accessRightID ({http://uri.etsi.org/m2m}accessRightID) inherited from {http://uri.etsi.org/m2m}Container

    # Element creationTime ({http://uri.etsi.org/m2m}creationTime) inherited from {http://uri.etsi.org/m2m}Container

    # Element lastModifiedTime ({http://uri.etsi.org/m2m}lastModifiedTime) inherited from {http://uri.etsi.org/m2m}Container

    # Element expirationTime ({http://uri.etsi.org/m2m}expirationTime) inherited from {http://uri.etsi.org/m2m}Container

    # Element searchStrings ({http://uri.etsi.org/m2m}searchStrings) inherited from {http://uri.etsi.org/m2m}Container

    # Element announceTo ({http://uri.etsi.org/m2m}announceTo) inherited from {http://uri.etsi.org/m2m}Container

    # Element subscriptionsReference ({http://uri.etsi.org/m2m}subscriptionsReference) inherited from {http://uri.etsi.org/m2m}Container

    # Element contentInstancesReference ({http://uri.etsi.org/m2m}contentInstancesReference) inherited from {http://uri.etsi.org/m2m}Container

    # Element subcontainersReference ({http://uri.etsi.org/m2m}subcontainersReference) inherited from {http://uri.etsi.org/m2m}Container

    # Element maxNrOfInstances ({http://uri.etsi.org/m2m}maxNrOfInstances) inherited from {http://uri.etsi.org/m2m}Container

    # Element maxByteSize ({http://uri.etsi.org/m2m}maxByteSize) inherited from {http://uri.etsi.org/m2m}Container

    # Element maxInstanceAge ({http://uri.etsi.org/m2m}maxInstanceAge) inherited from {http://uri.etsi.org/m2m}Container

    # Element {http://uri.etsi.org/m2m}locationContainerType uses Python identifier locationContainerType
    __locationContainerType = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, u'locationContainerType'),
        'locationContainerType',
        '__httpuri_etsi_orgm2m_LocationContainer_httpuri_etsi_orgm2mlocationContainerType',
        False, pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/locationContainer.xsd',
            20, 4), )

    locationContainerType = property(__locationContainerType.value,
                                     __locationContainerType.set, None, None)


    # Attribute id inherited from {http://uri.etsi.org/m2m}Container
    _ElementMap.update({
        __locationContainerType.name(): __locationContainerType
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', u'LocationContainer',
                            LocationContainer)


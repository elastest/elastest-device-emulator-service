from enum import IntEnum
from openmtc.model import Entity, Attribute, UnicodeAttribute, ListAttribute, \
    DatetimeAttribute, AnyURI, SubresourceMember, \
    CollectionMember, FlexibleAttributesMixin, Resource, EntityAttribute,\
    StrEnum
from openmtc.model.exc import ModelTypeError
from futile import issubclass

LATEST_VERSION = "2.1.1"


class SCLType(StrEnum):
    gscl = "GSCL"
    nscl = "NSCL"
    dscl = "DSCL"

    @property
    def is_nscl(self):
        return self == SCLType.nscl

    def __str__(self):
        return self.value


class LongPollingChannelData(Entity):
    longPollingURI = UnicodeAttribute(mandatory=True)


class APocPath(Entity):
    """See TS 102.921 table 11.13"""
    path = UnicodeAttribute(mandatory=True)
    accessRightID = UnicodeAttribute(mandatory=False)  # todo
    searchStrings = ListAttribute(mandatory=False)


class PermissionHolder(Entity):
    """See TS 102.921 table 11.18"""
    holderRefs = ListAttribute(mandatory=False)
    applicationIDs = ListAttribute(mandatory=False)
    sclIDs = ListAttribute(mandatory=False)
    all = Attribute(bool, mandatory=False, default=None)
    domains = ListAttribute(mandatory=False)


class Permission(Entity):
    """See TS 102.921 table 11.16"""
    id = Attribute(str, id_attribute=True, mandatory=True)
    permissionFlags = ListAttribute(mandatory=True)
    permissionHolders = EntityAttribute(mandatory=True,
                                        type=PermissionHolder)

# Hack for XSD compatibility
PermissionType = Permission


class FilterCriteria(Entity):
    """See TS 102.921 table 11.23"""
    ifModifiedSince = DatetimeAttribute(mandatory=False)
    ifUnmodifiedSince = DatetimeAttribute(mandatory=False)
    ifNoneMatch = ListAttribute(mandatory=False, default=None)
    attributeAccessor = Attribute(str, mandatory=False)
    searchString = ListAttribute(mandatory=False, default=None)
    createdAfter = DatetimeAttribute(mandatory=False)
    createdBefore = DatetimeAttribute(mandatory=False)

    sizeFrom = Attribute(int, mandatory=False)
    sizeUntil = Attribute(int, mandatory=False)
    contentType = ListAttribute(mandatory=False, default=None)
    metaDataOnly = Attribute(bool, mandatory=False)


# Hack for XSD compatibility
FilterCriteriaType = FilterCriteria


class Content(Entity):
    binaryContent = Attribute(str)
    textContent = UnicodeAttribute()
    contentType = Attribute(str, mandatory=True)


class AnnounceTo(Entity):
    """See TS 102.921 table 11.28"""
    activated = Attribute(bool, mandatory=False, default=True)
    sclList = ListAttribute(mandatory=False, content_type=AnyURI)


class Notify(Entity):
    """See TS 102.921 table 10.305"""

    statusCode = Attribute(mandatory=True)
    representation = EntityAttribute(dict)
    timeoutReason = UnicodeAttribute()
    subscriptionReference = UnicodeAttribute(mandatory=True)
    contact = UnicodeAttribute()
    requestingEntity = UnicodeAttribute()


class ETSIResource(Resource):
    __model_name__ = "etsi"
    __model_version__ = "2.1.1"

    def get_attribute_values(self, filter=False):
        vals = {}
        for attr in self.attributes:
            a_name = attr.name
            val = getattr(self, a_name)
            if val is None and filter:
                continue
            if isinstance(attr, ListAttribute):
                # TODO: return simple values. No representation
                if attr.content_type is AnyURI:
                    vals[a_name] = {"reference": val}
                else:
                    vals[a_name] = {a_name[:-1]: val}
            else:
                vals[a_name] = val
        return vals
    attribute_values = property(get_attribute_values)


class DefaultResource(ETSIResource):
    lastModifiedTime = DatetimeAttribute(mandatory=False,
                                         accesstype=Attribute.RO)
    creationTime = DatetimeAttribute(mandatory=False,
                                     accesstype=Attribute.RO)


class ExpiringResource(DefaultResource):
    expirationTime = DatetimeAttribute(mandatory=False)


class CollectionResource(ETSIResource):
    pass


class Subscription(ExpiringResource):
    """See TS 102.921 10.25.1."""
    # expirationTime
    minimalTimeBetweenNotifications = UnicodeAttribute(mandatory=False)  # todo
    delayTolerance = UnicodeAttribute(mandatory=False)  # todo
    # creationTime
    # lastModifiedTime
    filterCriteria = EntityAttribute(mandatory=False, accesstype=Attribute.WO,
                                     type=FilterCriteria, default=None)
    subscriptionType = UnicodeAttribute(mandatory=False,
                                        accesstype=Attribute.WO)  # todo
    contact = Attribute(str, mandatory=True, accesstype=Attribute.WO)
    id = UnicodeAttribute(mandatory=False, id_attribute=True)
    aggregateURI = Attribute(str, version="2.0")
    timeoutReason = UnicodeAttribute(version="2.0")
    noRepresentation = Attribute(bool, version="2.0")
    subscriberId = Attribute(str, version="2.0", accesstype=None)

    def __repr__(self):
        return "openmtc.Subscription(%r, %r)" % (self.id, self.contact)


class Subscriptions(CollectionResource):
    """See TS 102.921 10.24.1."""
    subscriptionCollection = CollectionMember(Subscription)


class SubscribableResource(ETSIResource):
    subscriptions = SubresourceMember(Subscriptions)


class SubscribableCollection(CollectionResource,
                             SubscribableResource, DefaultResource):
    pass


class ContentInstance(DefaultResource):
    """See TS 102.921 10.19.1."""
    id = UnicodeAttribute(mandatory=False, id_attribute=True)
    href = UnicodeAttribute(mandatory=False, path_attribute=True)
    contentTypes = ListAttribute()
    contentSize = Attribute(int)
    # creationTime
    # lastModifiedTime
    delayTolerance = UnicodeAttribute(mandatory=False)  # todo
    content = EntityAttribute(Content)
    searchStrings = ListAttribute(version="2.0")


class ContentInstances(SubscribableCollection):
    """See TS 102.921 10.18.1."""
    contentInstanceCollection = CollectionMember(ContentInstance)
    latest = Attribute(ContentInstance, mandatory=False)
    oldest = Attribute(ContentInstance, mandatory=False)
    currentNrOfInstances = Attribute(int, default=0, accesstype=Attribute.RO)
    currentByteSize = Attribute(int, default=0, accesstype=Attribute.RO)


class AnnounceableResource(ETSIResource):
    announceTo = EntityAttribute(mandatory=False, default=None,
                                 type=AnnounceTo)


class Container(ExpiringResource, SubscribableResource, AnnounceableResource):
    """See TS 102.921 10.14.1."""
    contentInstances = SubresourceMember(ContentInstances)
    id = UnicodeAttribute(id_attribute=True)
    accessRightID = UnicodeAttribute(mandatory=False)  # todo
    searchStrings = ListAttribute(mandatory=False)
    maxNrOfInstances = Attribute(int, default=-1)
    maxByteSize = Attribute(int, default=-1)
    maxInstanceAge = UnicodeAttribute(mandatory=False)  # todo


class Subcontainers(SubscribableCollection):
    """See TS 102.921 10.40.1"""
    containerCollection = CollectionMember(Container)


Container.subcontainers = SubresourceMember(Subcontainers)
Container.subcontainers._init("subcontainers")
Container.__members__.append(Container.subcontainers)
Container.subresources.append(Container.subcontainers)


class AnnouncementResource(ExpiringResource):
    id = UnicodeAttribute(id_attribute=True)
    accessRightID = UnicodeAttribute(mandatory=False)  # todo
    searchStrings = ListAttribute(mandatory=True)
    # TODO(rst): workaround -> change back to RW later
    link = UnicodeAttribute(mandatory=True, accesstype=Attribute.RW,
                            update_mandatory=False)
    announceTo = EntityAttribute(mandatory=False, type=AnnounceTo,
                                 default=None)


class ContainerAnnc(AnnouncementResource):
    """See TS 102.921 10.15.1."""
    pass


class LocationContainer(ExpiringResource, SubscribableResource,
                        AnnounceableResource):
    """See TS 102.921 10.16.1."""
    contentInstances = SubresourceMember(ContentInstances)
    id = UnicodeAttribute(id_attribute=True)
    accessRightID = UnicodeAttribute(mandatory=False)  # todo
    searchStrings = ListAttribute(mandatory=False)
    # announceTo
    maxNrOfInstances = Attribute(int)
    maxByteSize = Attribute(int)
    maxInstanceAge = UnicodeAttribute(mandatory=False)  # todo
    locationContainerType = UnicodeAttribute(mandatory=True,
                                             accesstype=Attribute.WO)


class LocationContainerAnnc(AnnouncementResource):
    """See TS 102.921 10.17.1."""
    pass


class Containers(SubscribableCollection):
    """See TS 102.921 10.13.1."""
    containerCollection = CollectionMember(Container)
    containerAnncCollection = CollectionMember(ContainerAnnc)
    locationContainerCollection = CollectionMember(LocationContainer)
    locationContainerAnncCollection = CollectionMember(LocationContainerAnnc)
    accessRightID = UnicodeAttribute(mandatory=False)  # todo


class AccessRight(ExpiringResource, SubscribableResource,
                  AnnounceableResource):
    """See TS 102.921 10.11.1."""
    searchStrings = ListAttribute(mandatory=False)
    permissions = ListAttribute(mandatory=False, content_type=Permission)
    selfPermissions = ListAttribute(mandatory=True, content_type=Permission)
    id = UnicodeAttribute(mandatory=False, id_attribute=True)


class AccessRightAnnc(AnnouncementResource):
    """See TS 102.921 10.12.1."""
    pass


class AccessRights(SubscribableCollection):
    """See TS 102.921 10.10.1."""
    accessRightCollection = CollectionMember(AccessRight)
    accessRightAnncCollection = CollectionMember(AccessRightAnnc)  # todo
    accessRightID = UnicodeAttribute(mandatory=False)  # todo


class MembersContent(ETSIResource):
    """See TS 102.921 10.23.1."""
    virtual = True

    membersContentResponses = ListAttribute(accesstype=Attribute.RO)


class NotifyCollection(ETSIResource):
    """See TS 102.921 10.25.6."""
    virtual = True

    notifyCollection = ListAttribute(accesstype=Attribute.RO)


class Group(SubscribableResource, ExpiringResource, AnnounceableResource):
    """See TS 102.921 10.21.1."""
    id = UnicodeAttribute(id_attribute=True)
    accessRightID = UnicodeAttribute(mandatory=False)
    searchStrings = ListAttribute(mandatory=False)
    members = ListAttribute(mandatory=False, content_type=AnyURI)
    membersContent = SubresourceMember(MembersContent)
    memberType = UnicodeAttribute(mandatory=True, accesstype=Attribute.WO)
    currentNrOfMembers = Attribute(int, default=0, accesstype=Attribute.RO)
    maxNrOfMembers = Attribute(int)
    membersContentAccessRightID = UnicodeAttribute(mandatory=False)
    memberTypeValidated = Attribute(bool, accesstype=Attribute.RO)
    consistencyStrategy = UnicodeAttribute(mandatory=False)


class GroupAnnc(AnnouncementResource):
    """See TS 102.921 10.22.1."""
    pass


class Groups(SubscribableCollection):
    """See TS 102.921 10.20.1."""
    accessRightID = UnicodeAttribute(mandatory=False)
    groupCollection = CollectionMember(Group)
    groupAnncCollection = CollectionMember(GroupAnnc)


# TODO: kca: non-creatable resource ExecInstance
class ExecInstance(ExpiringResource, SubscribableResource):
    """See TS 102.921 10.33.1."""
    id = UnicodeAttribute(id_attribute=True)
    accessRightID = UnicodeAttribute(mandatory=False)
    execStatus = UnicodeAttribute(mandatory=False)
    execResult = UnicodeAttribute(mandatory=False)
    execDisable = UnicodeAttribute(mandatory=False)


class ExecInstances(SubscribableCollection):
    """See TS 102.921 10.32.1."""
    execinstanceCollection = CollectionMember(ExecInstance)


class Parameters(FlexibleAttributesMixin, SubscribableCollection):
    """See TS 102.921 10.30.1."""
    id = UnicodeAttribute(id_attribute=True)
    accessRightID = UnicodeAttribute(mandatory=False)  # todo
    originalMO = UnicodeAttribute(mandatory=False, accesstype=Attribute.WO)

    #TODO: kca: Deal with the <moAttribute> thing: (missing checks for mandatory ones)
    #For the <parameters> resource instances using generic or external data model, there could be zero or
    #multiple <moAttribute> attributes that are optional in createReq, updateReq and response. For ETSI specific
    #<parameters> resource instances, the multiplicity and optionality of the <moAttribute> attribute is described
    #in annex E. A mandatory <moAttribute> shall be provided in the createReq unless a default value has been
    #defined for its absence, otherwise the receiver shall reject the createReq.


class MgmtObj(FlexibleAttributesMixin, ExpiringResource, SubscribableResource):
    """See TS 102.921 10.29.1."""
    id = UnicodeAttribute(id_attribute=True)
    moID = UnicodeAttribute(mandatory=True, accesstype=Attribute.WO)
    accessRightID = UnicodeAttribute(mandatory=False)  # todo
    searchStrings = ListAttribute(mandatory=False)
    description = UnicodeAttribute(mandatory=False)  # todo
    originalMO = UnicodeAttribute(mandatory=False, accesstype=Attribute.WO)
    parametersCollection = CollectionMember(Parameters)

    #TODO: kca: Deal with the <moAttribute> thing: (missing checks for mandatory ones)
    #For the <mgmtObj> resource instances using generic or external data model, there could be zero or
    #multiple <moAttribute> attributes that are optional in createReq, updateReq and response. For ETSI
    #specific <mgmtObj> resource instances, the multiplicity and optionality of the <moAttribute> attribute is
    #described in annex E. A mandatory <moAttribute> will be provided in the createReq unless a default
    #value has been defined for its absence, otherwise the receiver will reject the createReq.


class MgmtCmd(ExpiringResource, SubscribableResource):
    """See TS 102.921 10.31.1."""
    id = UnicodeAttribute(id_attribute=True)
    accessRightID = UnicodeAttribute(mandatory=False)  # todo
    searchStrings = ListAttribute(mandatory=False)
    description = UnicodeAttribute(mandatory=False)  # todo
    originalMO = UnicodeAttribute(mandatory=False, accesstype=Attribute.WO)
    cmdType = UnicodeAttribute(mandatory=True, update_mandatory=False)
    execEnable = UnicodeAttribute(mandatory=True, accesstype=Attribute.WO)
    execReqArgs = UnicodeAttribute(mandatory=False)
    execInstances = SubresourceMember(ExecInstances)


#TODO: kca: make sure this only shows up on certain reference points
class MgmtObjs(SubscribableCollection):
    """See TS 102.921 10.28.1."""
    mgmtObjCollection = CollectionMember(MgmtObj)
    mgmtCmdCollection = CollectionMember(MgmtCmd)


class ApplicationAnnc(AnnouncementResource):
    """See TS 102.921 10.9.1."""
    containers = SubresourceMember(Containers)
    groups = SubresourceMember(Groups)
    accessRights = SubresourceMember(AccessRights)

    @property
    def name(self):
        return self.id


class AttachedDevice(SubscribableResource, DefaultResource):
    """See TS 102.921 10.35.1."""
    id = UnicodeAttribute(id_attribute=True)
    accessRightID = UnicodeAttribute(mandatory=False)
    mgmtObjs = SubresourceMember(MgmtObjs)


class AttachedDevices(SubscribableCollection):
    """See TS 102.921 10.34.1."""
    attachedDeviceCollection = CollectionMember(AttachedDevice)
    accessRightID = UnicodeAttribute(mandatory=False)


class NotificationChannel(DefaultResource):
    """See TS 102.921 10.37.1."""
    id = UnicodeAttribute(mandatory=False, id_attribute=True)
    channelType = UnicodeAttribute(mandatory=True, accesstype=Attribute.WO)
    contactURI = UnicodeAttribute(accesstype=Attribute.RO)
    channelData = EntityAttribute(accesstype=Attribute.RO,
                                  type=LongPollingChannelData)


class NotificationChannels(CollectionResource, DefaultResource):
    """See TS 102.921 10.38.1."""
    notificationChannelCollection = CollectionMember(NotificationChannel)


class Application(ExpiringResource, SubscribableResource,
                  AnnounceableResource):
    """See TS 102.921 10.8.1."""
    containers = SubresourceMember(Containers)
    groups = SubresourceMember(Groups)
    accessRights = SubresourceMember(AccessRights)
    notificationChannels = SubresourceMember(NotificationChannels)
    appId = UnicodeAttribute(mandatory=False, id_attribute=True,
                             id_immutable=True)
    accessRightID = UnicodeAttribute(mandatory=False)
    searchStrings = ListAttribute(mandatory=False)
    aPoC = UnicodeAttribute(mandatory=False)
    aPoCPaths = ListAttribute(mandatory=False, content_type=APocPath)
    locrequester = UnicodeAttribute(mandatory=False)  # todo
    referencePoint = UnicodeAttribute(accesstype=Attribute.RO, version="2.0")


class Applications(SubscribableCollection):
    """See TS 102.921 10.7.1."""
    applicationCollection = CollectionMember(Application)
    applicationAnncCollection = CollectionMember(ApplicationAnnc)
    mgmtObjs = SubresourceMember(MgmtObjs)
    accessRightID = UnicodeAttribute(mandatory=False)

    def __repr__(self):
        return "openmtc.Applications( %s, %s )" % (
            self.applicationAnncCollection, self.applicationCollection)


class M2mPoc(ExpiringResource):
    """See TS 102.921 10.27.1"""
    id = UnicodeAttribute(id_attribute=True)
    onlineStatus = UnicodeAttribute(mandatory=False)
    contactInfo = UnicodeAttribute(mandatory=True) # TODO: this should be a complex attribute


class M2mPocs(CollectionResource, DefaultResource):
    """See TS 102.921 10.26.1"""
    m2mPocCollection = CollectionMember(M2mPoc)


class CommunicationChannel(DefaultResource):
    """See TS 102.921 10.42.1."""
    id = UnicodeAttribute(mandatory=False, id_attribute=True)
    channelType = UnicodeAttribute(mandatory=True, accesstype=Attribute.WO)
    contactURI = UnicodeAttribute(accesstype=Attribute.RO)
    channelData = EntityAttribute(accesstype=Attribute.RO,
                                  type=LongPollingChannelData)


class CommunicationChannels(CollectionResource, DefaultResource):
    """See TS 102.921 10.41.1."""
    communicationChannelCollection = CollectionMember(CommunicationChannel)


class SclAnnc(AnnouncementResource):
    """See TS 102.921 10.6a.1."""


class SclAnncs(SubscribableCollection):
    """See TS 102.921 10.5a.1."""
    accessRightID = UnicodeAttribute(mandatory=False)  # todo
    sclAnncCollection = CollectionMember(SclAnnc)


class Scl(ExpiringResource, SubscribableResource, AnnounceableResource):
    """See TS 102.921 10.6.1."""
    containers = SubresourceMember(Containers)
    groups = SubresourceMember(Groups)
    applications = SubresourceMember(Applications)
    accessRights = SubresourceMember(AccessRights)
    mgmtObjs = SubresourceMember(MgmtObjs)
    notificationChannels = SubresourceMember(NotificationChannels)
    communicationChannels = SubresourceMember(CommunicationChannels)
    sclAnncs = SubresourceMember(SclAnncs)
    m2mPocs = SubresourceMember(M2mPocs)
    attachedDevices = SubresourceMember(AttachedDevices)
    sclId = UnicodeAttribute(id_attribute=True, mandatory=True)
    pocs = ListAttribute(content_type=AnyURI)
    remTriggerAddr = UnicodeAttribute(mandatory=False)
    onlineStatus = UnicodeAttribute(mandatory=False, accesstype=Attribute.RO)
    serverCapability = Attribute(bool, mandatory=False,
                                 accesstype=Attribute.RO)
    link = UnicodeAttribute(mandatory=True, accesstype=Attribute.WO)
    schedule = UnicodeAttribute(mandatory=False)
    accessRightID = UnicodeAttribute(mandatory=False)
    searchStrings = ListAttribute()
    locTargetDevice = UnicodeAttribute(mandatory=False)
    mgmtProtocolType = UnicodeAttribute(mandatory=True, update_mandatory=True)
    integrityValResults = UnicodeAttribute(mandatory=False)
    aPocHandling = UnicodeAttribute(mandatory=False, accesstype=Attribute.RO)
    sclType = Attribute(SCLType, mandatory=True, accesstype=Attribute.WO,
                        version="2.0")
    publicDomain = UnicodeAttribute(mandatory=False, accesstype=Attribute.RO,
                                    version="2.0")


class Scls(SubscribableCollection):
    """See TS 102.921 10.5.1."""
    sclCollection = CollectionMember(Scl)
    mgmtObjs = SubresourceMember(MgmtObjs)
    accessRightID = UnicodeAttribute(mandatory=False)


class Discovery(ETSIResource):
    virtual = True

    discoveryURI = ListAttribute(content_type=AnyURI)
    matchSize = Attribute(int, default=0)
    truncated = Attribute(bool, default=False)


class SclBase(DefaultResource, SubscribableResource):
    """See TS 102.921 10.4.1."""

    scls = SubresourceMember(Scls)
    applications = SubresourceMember(Applications)
    containers = SubresourceMember(Containers)
    groups = SubresourceMember(Groups)
    accessRights = SubresourceMember(AccessRights)
    discovery = SubresourceMember(Discovery)  # todo
    accessRightID = UnicodeAttribute()
    searchStrings = ListAttribute()
    aPocHandling = UnicodeAttribute()


class sclMoAction(DefaultResource):
    """See TS 102.690 B.2.1.1."""
    pass


class RcatType(IntEnum):
    RCAT_0 = 0
    RCAT_1 = 1
    RCAT_2 = 2
    RCAT_3 = 3
    RCAT_4 = 4
    RCAT_5 = 5
    RCAT_6 = 6
    RCAT_7 = 7


class RcatList(DefaultResource):
    rcatTypes = ListAttribute(RcatType)


class AbsTimeSpan(DefaultResource):
    startTime = DatetimeAttribute()
    endTime = DatetimeAttribute()


class ScheduleString(DefaultResource):
    id = Attribute(str)


class Schedule(DefaultResource):
    scheduleStrings = ListAttribute(ScheduleString)


class SchedItem(DefaultResource):
    absTimeSpan = ListAttribute(AbsTimeSpan)
    schedule = ListAttribute(Schedule)


class RcatSchedule(DefaultResource):
    rcatValue = ListAttribute(RcatType)
    schedItem = ListAttribute(SchedItem)


class RcatSchedList(DefaultResource):
    rcatSchedule = ListAttribute(RcatSchedule)


class BlockItem(DefaultResource):
    failedAttempts = ListAttribute(long)
    blockDuration = Attribute(long)


class BlockList(DefaultResource):
    blockItems = ListAttribute(BlockItem)


class anpPolicy(SubscribableResource):
    """See TS 102.690 B.2.1.3."""
    # For each Network
    anName = UnicodeAttribute(id_attribute=True)
    # RCAT vs time
    rcatSchedList = EntityAttribute(RcatSchedList)
    # Failed attempts vs block duration (optionnal)
    blockPeriods = EntityAttribute(BlockList)

    def __eq__(self, o):
        if self.anName is not None:
            try:
                return self.anName == o.anName
            except AttributeError:
                return False
        return super(anpPolicy, self).__eq__(o)


class rcatParamList(DefaultResource):
    """See TS 102.690 B.2.1.5."""
    # For each RCAT (0-7)
    rcatValue = Attribute(int, default=0)
    maxPendReq = Attribute(int, default=-1)
    maxPendData = Attribute(int, default=-1)
    anSelList = ListAttribute()


class m2mSpPolicy(DefaultResource, SubscribableResource):
    # For each Policy
    """See TS 102.690 B.2.1.4."""
    defaultRcatValue = Attribute(int, default=0)
    rcatParamListCollection = CollectionMember(rcatParamList)


class safPolicySet(ExpiringResource, SubscribableResource):
    """See TS 102.690 B.2.1.2."""
    # For each Policy
    anpPolicyCollection = CollectionMember(anpPolicy)
    m2mSpPolicy = SubresourceMember(m2mSpPolicy)
    # Either "default" or list of app IDs where this policy applies
    policyScope = ListAttribute()


def get_etsi_type(typename):
    try:
        return globals()[typename[0].upper() + typename[1:]]
    except KeyError:
        raise ModelTypeError("Not a valid type: %s" % (typename, ))


_all_types = None


def get_etsi_types():
    global _all_types
    if _all_types is None:
        _all_types = [x for x in globals().values()
                      if issubclass(x, ETSIResource) and not x.__subclasses__()]
    return _all_types

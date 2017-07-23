import pyxb
import pyxb.binding
import pyxb.utils
import pyxb.utils.utility

from _binding import *


holderRef = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'holderRef'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        73, 4))
Namespace.addCategoryObject('elementBinding', holderRef.name().localName(),
                            holderRef)

domain = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'domain'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        83, 4))
Namespace.addCategoryObject('elementBinding', domain.name().localName(), domain)

applicationID = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'applicationID'),
    pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        112, 4))
Namespace.addCategoryObject('elementBinding', applicationID.name().localName(),
                            applicationID)

sclID = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclID'),
    pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        122, 4))
Namespace.addCategoryObject('elementBinding', sclID.name().localName(), sclID)

aPoC = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'aPoC'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
        33, 4))
Namespace.addCategoryObject('elementBinding', aPoC.name().localName(), aPoC)

locRequestor = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'locRequestor'),
    pyxb.binding.datatypes.anyType, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
        36, 4))
Namespace.addCategoryObject('elementBinding', locRequestor.name().localName(),
                            locRequestor)

path = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'path'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
        62, 4))
Namespace.addCategoryObject('elementBinding', path.name().localName(), path)

accessRightID = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4))
Namespace.addCategoryObject('elementBinding', accessRightID.name().localName(),
                            accessRightID)

creationTime = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4))
Namespace.addCategoryObject('elementBinding', creationTime.name().localName(),
                            creationTime)

lastModifiedTime = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4))
Namespace.addCategoryObject('elementBinding',
                            lastModifiedTime.name().localName(),
                            lastModifiedTime)

expirationTime = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
    pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 16,
        4))
Namespace.addCategoryObject('elementBinding', expirationTime.name().localName(),
                            expirationTime)

searchString = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'searchString'),
    pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 28,
        4))
Namespace.addCategoryObject('elementBinding', searchString.name().localName(),
                            searchString)

activated = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'activated'),
    pyxb.binding.datatypes.boolean, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 68,
        4))
Namespace.addCategoryObject('elementBinding', activated.name().localName(),
                            activated)

global_ = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'global'),
    pyxb.binding.datatypes.boolean, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 70,
        4))
Namespace.addCategoryObject('elementBinding', global_.name().localName(),
                            global_)

delayTolerance = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'delayTolerance'),
    pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 72,
        4))
Namespace.addCategoryObject('elementBinding', delayTolerance.name().localName(),
                            delayTolerance)

link = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'link'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 74,
        4))
Namespace.addCategoryObject('elementBinding', link.name().localName(), link)

subscriptionsReference = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4))
Namespace.addCategoryObject('elementBinding',
                            subscriptionsReference.name().localName(),
                            subscriptionsReference)

groupsReference = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'groupsReference'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 77,
        4))
Namespace.addCategoryObject('elementBinding',
                            groupsReference.name().localName(), groupsReference)

applicationsReference = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'applicationsReference'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 78,
        4))
Namespace.addCategoryObject('elementBinding',
                            applicationsReference.name().localName(),
                            applicationsReference)

containersReference = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'containersReference'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 79,
        4))
Namespace.addCategoryObject('elementBinding',
                            containersReference.name().localName(),
                            containersReference)

accessRightsReference = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightsReference'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 81,
        4))
Namespace.addCategoryObject('elementBinding',
                            accessRightsReference.name().localName(),
                            accessRightsReference)

notificationChannelsReference = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'notificationChannelsReference'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 82,
        4))
Namespace.addCategoryObject('elementBinding',
                            notificationChannelsReference.name().localName(),
                            notificationChannelsReference)

communicationChannelsReference = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'communicationChannelsReference'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 83,
        4))
Namespace.addCategoryObject('elementBinding',
                            communicationChannelsReference.name().localName(),
                            communicationChannelsReference)

mgmtObjsReference = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'mgmtObjsReference'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 84,
        4))
Namespace.addCategoryObject('elementBinding',
                            mgmtObjsReference.name().localName(),
                            mgmtObjsReference)

contentInstancesReference = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contentInstancesReference'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 86,
        4))
Namespace.addCategoryObject('elementBinding',
                            contentInstancesReference.name().localName(),
                            contentInstancesReference)

subcontainersReference = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subcontainersReference'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 87,
        4))
Namespace.addCategoryObject('elementBinding',
                            subcontainersReference.name().localName(),
                            subcontainersReference)

contentType = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contentType'),
    pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 106,
        4))
Namespace.addCategoryObject('elementBinding', contentType.name().localName(),
                            contentType)

contactURI = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contactURI'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 136,
        4))
Namespace.addCategoryObject('elementBinding', contactURI.name().localName(),
                            contactURI)

longPollingURI = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'longPollingURI'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 162,
        4))
Namespace.addCategoryObject('elementBinding', longPollingURI.name().localName(),
                            longPollingURI)

appId = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'appId'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 219,
        4))
Namespace.addCategoryObject('elementBinding', appId.name().localName(), appId)

sclId = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclId'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 220,
        4))
Namespace.addCategoryObject('elementBinding', sclId.name().localName(), sclId)

moID = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'moID'),
    pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 8,
        4))
Namespace.addCategoryObject('elementBinding', moID.name().localName(), moID)

originalMO = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'originalMO'),
    pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 10,
        4))
Namespace.addCategoryObject('elementBinding', originalMO.name().localName(),
                            originalMO)

description = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'description'),
    pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 12,
        4))
Namespace.addCategoryObject('elementBinding', description.name().localName(),
                            description)

moAttribute = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'moAttribute'),
    pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1),
    documentation=u'To be substituted by specific MO resource attributes,\n                e.g. ramTotal\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 16,
        4))
Namespace.addCategoryObject('elementBinding', moAttribute.name().localName(),
                            moAttribute)

firmwareVersion = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'firmwareVersion'),
    pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 55,
        4))
Namespace.addCategoryObject('elementBinding',
                            firmwareVersion.name().localName(), firmwareVersion)

name = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'name'),
    pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 81,
        4))
Namespace.addCategoryObject('elementBinding', name.name().localName(), name)

value = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'value'),
    pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 83,
        4))
Namespace.addCategoryObject('elementBinding', value.name().localName(), value)

securityKmrIndex = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'securityKmrIndex'),
    pyxb.binding.datatypes.unsignedInt, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        14, 4))
Namespace.addCategoryObject('elementBinding',
                            securityKmrIndex.name().localName(),
                            securityKmrIndex)

securityLifetime = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'securityLifetime'),
    pyxb.binding.datatypes.dateTime, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        16, 4))
Namespace.addCategoryObject('elementBinding',
                            securityLifetime.name().localName(),
                            securityLifetime)

securityMasFqdn = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'securityMasFqdn'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        18, 4))
Namespace.addCategoryObject('elementBinding',
                            securityMasFqdn.name().localName(), securityMasFqdn)

securitySclId = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'securitySclId'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        28, 4))
Namespace.addCategoryObject('elementBinding', securitySclId.name().localName(),
                            securitySclId)

securityKmcIndex = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'securityKmcIndex'),
    pyxb.binding.datatypes.unsignedInt, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        30, 4))
Namespace.addCategoryObject('elementBinding',
                            securityKmcIndex.name().localName(),
                            securityKmcIndex)

securityConnectionId = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'securityConnectionId'),
    pyxb.binding.datatypes.unsignedLong, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        48, 4))
Namespace.addCategoryObject('elementBinding',
                            securityConnectionId.name().localName(),
                            securityConnectionId)

maxNrOfInstances = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'maxNrOfInstances'),
    pyxb.binding.datatypes.long, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd', 30,
        4))
Namespace.addCategoryObject('elementBinding',
                            maxNrOfInstances.name().localName(),
                            maxNrOfInstances)

maxByteSize = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'maxByteSize'),
    pyxb.binding.datatypes.long, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd', 31,
        4))
Namespace.addCategoryObject('elementBinding', maxByteSize.name().localName(),
                            maxByteSize)

maxInstanceAge = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'maxInstanceAge'),
    pyxb.binding.datatypes.duration, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd', 32,
        4))
Namespace.addCategoryObject('elementBinding', maxInstanceAge.name().localName(),
                            maxInstanceAge)

textContent = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'textContent'),
    pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
        37, 4))
Namespace.addCategoryObject('elementBinding', textContent.name().localName(),
                            textContent)

binaryContent = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'binaryContent'),
    pyxb.binding.datatypes.base64Binary, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
        38, 4))
Namespace.addCategoryObject('elementBinding', binaryContent.name().localName(),
                            binaryContent)

contentSize = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contentSize'),
    pyxb.binding.datatypes.long, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
        40, 4))
Namespace.addCategoryObject('elementBinding', contentSize.name().localName(),
                            contentSize)

currentNrOfInstances = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'currentNrOfInstances'),
    pyxb.binding.datatypes.long, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
        25, 4))
Namespace.addCategoryObject('elementBinding',
                            currentNrOfInstances.name().localName(),
                            currentNrOfInstances)

currentByteSize = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'currentByteSize'),
    pyxb.binding.datatypes.long, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
        26, 4))
Namespace.addCategoryObject('elementBinding',
                            currentByteSize.name().localName(), currentByteSize)

matchSize = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'matchSize'),
    pyxb.binding.datatypes.long, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/discovery.xsd', 15,
        4))
Namespace.addCategoryObject('elementBinding', matchSize.name().localName(),
                            matchSize)

truncated = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'truncated'),
    pyxb.binding.datatypes.boolean, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/discovery.xsd', 16,
        4))
Namespace.addCategoryObject('elementBinding', truncated.name().localName(),
                            truncated)

additionalInfo = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'additionalInfo'),
    pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/errorInfo.xsd', 17,
        4))
Namespace.addCategoryObject('elementBinding', additionalInfo.name().localName(),
                            additionalInfo)

areaNwkID = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'areaNwkID'),
    pyxb.binding.datatypes.long, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
        27, 4))
Namespace.addCategoryObject('elementBinding', areaNwkID.name().localName(),
                            areaNwkID)

sleepInterval = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sleepInterval'),
    pyxb.binding.datatypes.long, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
        35, 4))
Namespace.addCategoryObject('elementBinding', sleepInterval.name().localName(),
                            sleepInterval)

sleepDuration = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sleepDuration'),
    pyxb.binding.datatypes.long, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
        36, 4))
Namespace.addCategoryObject('elementBinding', sleepDuration.name().localName(),
                            sleepDuration)

numOfAreaNwks = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'numOfAreaNwks'),
    pyxb.binding.datatypes.long, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInfo.xsd',
        20, 4))
Namespace.addCategoryObject('elementBinding', numOfAreaNwks.name().localName(),
                            numOfAreaNwks)

addressType = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'addressType'),
    pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInstance.xsd',
        40, 4))
Namespace.addCategoryObject('elementBinding', addressType.name().localName(),
                            addressType)

standbyTime = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'standbyTime'),
    pyxb.binding.datatypes.long,
    documentation=u'\n                Contains the estimated time of operation. It is based on the\n                charge of all the batteries and it is expressed in minutes.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiBattery.xsd',
        20, 4))
Namespace.addCategoryObject('elementBinding', standbyTime.name().localName(),
                            standbyTime)

devCapEnable = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'devCapEnable'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityAction.xsd',
        22, 4))
Namespace.addCategoryObject('elementBinding', devCapEnable.name().localName(),
                            devCapEnable)

devCapDisable = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'devCapDisable'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityAction.xsd',
        23, 4))
Namespace.addCategoryObject('elementBinding', devCapDisable.name().localName(),
                            devCapDisable)

capabilityName = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'capabilityName'),
    pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityInstance.xsd',
        23, 4))
Namespace.addCategoryObject('elementBinding', capabilityName.name().localName(),
                            capabilityName)

deviceLabel = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'deviceLabel'),
    pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
        27, 4))
Namespace.addCategoryObject('elementBinding', deviceLabel.name().localName(),
                            deviceLabel)

manufacturer = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'manufacturer'),
    pyxb.binding.datatypes.string,
    documentation=u'\n                Manufacturer identifier.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
        29, 4))
Namespace.addCategoryObject('elementBinding', manufacturer.name().localName(),
                            manufacturer)

model = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'model'),
    pyxb.binding.datatypes.string,
    documentation=u'\n                Manufacturer specified string.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
        37, 4))
Namespace.addCategoryObject('elementBinding', model.name().localName(), model)

deviceType = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'deviceType'),
    pyxb.binding.datatypes.string,
    documentation=u'\n                For example, PDA, meter, sensor, ... .\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
        45, 4))
Namespace.addCategoryObject('elementBinding', deviceType.name().localName(),
                            deviceType)

hardwareVersion = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'hardwareVersion'),
    pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
        54, 4))
Namespace.addCategoryObject('elementBinding',
                            hardwareVersion.name().localName(), hardwareVersion)

fwDownload = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'fwDownload'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareAction.xsd',
        22, 4))
Namespace.addCategoryObject('elementBinding', fwDownload.name().localName(),
                            fwDownload)

fwUpdate = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'fwUpdate'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareAction.xsd',
        23, 4))
Namespace.addCategoryObject('elementBinding', fwUpdate.name().localName(),
                            fwUpdate)

fwDownloadAndUpdate = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'fwDownloadAndUpdate'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareAction.xsd',
        24, 4))
Namespace.addCategoryObject('elementBinding',
                            fwDownloadAndUpdate.name().localName(),
                            fwDownloadAndUpdate)

fwRemove = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'fwRemove'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareAction.xsd',
        25, 4))
Namespace.addCategoryObject('elementBinding', fwRemove.name().localName(),
                            fwRemove)

ramAvailable = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'ramAvailable'),
    pyxb.binding.datatypes.long,
    documentation=u'\n                Expressed in kilobytes.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiMemory.xsd', 21,
        4))
Namespace.addCategoryObject('elementBinding', ramAvailable.name().localName(),
                            ramAvailable)

ramTotal = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'ramTotal'),
    pyxb.binding.datatypes.long,
    documentation=u'\n                Expressed in kilobytes.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiMemory.xsd', 29,
        4))
Namespace.addCategoryObject('elementBinding', ramTotal.name().localName(),
                            ramTotal)

perfLogStart = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'perfLogStart'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerfLogAction.xsd',
        21, 4))
Namespace.addCategoryObject('elementBinding', perfLogStart.name().localName(),
                            perfLogStart)

perfLogStop = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'perfLogStop'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerfLogAction.xsd',
        22, 4))
Namespace.addCategoryObject('elementBinding', perfLogStop.name().localName(),
                            perfLogStop)

maxPendReqs = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'maxPendReqs'),
    pyxb.binding.datatypes.long, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
        26, 4))
Namespace.addCategoryObject('elementBinding', maxPendReqs.name().localName(),
                            maxPendReqs)

accessNetwork = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessNetwork'),
    pyxb.binding.datatypes.token, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
        37, 4))
Namespace.addCategoryObject('elementBinding', accessNetwork.name().localName(),
                            accessNetwork)

applicationRef = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'applicationRef'),
    pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd', 40,
        4))
Namespace.addCategoryObject('elementBinding', applicationRef.name().localName(),
                            applicationRef)

reboot = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'reboot'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRebootAction.xsd',
        22, 4))
Namespace.addCategoryObject('elementBinding', reboot.name().localName(), reboot)

factoryReset = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'factoryReset'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRebootAction.xsd',
        24, 4))
Namespace.addCategoryObject('elementBinding', factoryReset.name().localName(),
                            factoryReset)

regExpirationDuration = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'regExpirationDuration'),
    pyxb.binding.datatypes.duration, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd', 29,
        4))
Namespace.addCategoryObject('elementBinding',
                            regExpirationDuration.name().localName(),
                            regExpirationDuration)

regAccessRightID = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'regAccessRightID'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd', 30,
        4))
Namespace.addCategoryObject('elementBinding',
                            regAccessRightID.name().localName(),
                            regAccessRightID)

maxNumberOfDiscovRecords = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'maxNumberOfDiscovRecords'),
    pyxb.binding.datatypes.long, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd', 33,
        4))
Namespace.addCategoryObject('elementBinding',
                            maxNumberOfDiscovRecords.name().localName(),
                            maxNumberOfDiscovRecords)

maxSizeOfDiscovAnswer = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'maxSizeOfDiscovAnswer'),
    pyxb.binding.datatypes.long, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd', 34,
        4))
Namespace.addCategoryObject('elementBinding',
                            maxSizeOfDiscovAnswer.name().localName(),
                            maxSizeOfDiscovAnswer)

reRegistration = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'reRegistration'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMoAction.xsd',
        21, 4))
Namespace.addCategoryObject('elementBinding', reRegistration.name().localName(),
                            reRegistration)

deRegistration = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'deRegistration'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMoAction.xsd',
        22, 4))
Namespace.addCategoryObject('elementBinding', deRegistration.name().localName(),
                            deRegistration)

swDownload = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'swDownload'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
        26, 4))
Namespace.addCategoryObject('elementBinding', swDownload.name().localName(),
                            swDownload)

swDownloadAndInstall = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'swDownloadAndInstall'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
        27, 4))
Namespace.addCategoryObject('elementBinding',
                            swDownloadAndInstall.name().localName(),
                            swDownloadAndInstall)

swInstall = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'swInstall'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
        28, 4))
Namespace.addCategoryObject('elementBinding', swInstall.name().localName(),
                            swInstall)

swRemove = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'swRemove'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
        29, 4))
Namespace.addCategoryObject('elementBinding', swRemove.name().localName(),
                            swRemove)

swActivate = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'swActivate'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
        30, 4))
Namespace.addCategoryObject('elementBinding', swActivate.name().localName(),
                            swActivate)

swDeactivate = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'swDeactivate'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
        31, 4))
Namespace.addCategoryObject('elementBinding', swDeactivate.name().localName(),
                            swDeactivate)

trapEventEnable = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'trapEventEnable'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapEventAction.xsd',
        21, 4))
Namespace.addCategoryObject('elementBinding',
                            trapEventEnable.name().localName(), trapEventEnable)

trapEventDisable = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'trapEventDisable'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapEventAction.xsd',
        23, 4))
Namespace.addCategoryObject('elementBinding',
                            trapEventDisable.name().localName(),
                            trapEventDisable)

trapId = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'trapId'),
    pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
        23, 4))
Namespace.addCategoryObject('elementBinding', trapId.name().localName(), trapId)

execDisable = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'execDisable'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
        30, 4))
Namespace.addCategoryObject('elementBinding', execDisable.name().localName(),
                            execDisable)

membersContentAccessRightID = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'membersContentAccessRightID'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 14, 4))
Namespace.addCategoryObject('elementBinding',
                            membersContentAccessRightID.name().localName(),
                            membersContentAccessRightID)

currentNrOfMembers = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'currentNrOfMembers'),
    pyxb.binding.datatypes.long, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 39, 4))
Namespace.addCategoryObject('elementBinding',
                            currentNrOfMembers.name().localName(),
                            currentNrOfMembers)

maxNrOfMembers = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'maxNrOfMembers'),
    pyxb.binding.datatypes.long, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 40, 4))
Namespace.addCategoryObject('elementBinding', maxNrOfMembers.name().localName(),
                            maxNrOfMembers)

memberTypeValidated = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'memberTypeValidated'),
    pyxb.binding.datatypes.boolean, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 42, 4))
Namespace.addCategoryObject('elementBinding',
                            memberTypeValidated.name().localName(),
                            memberTypeValidated)

membersContentReference = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'membersContentReference'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 45, 4))
Namespace.addCategoryObject('elementBinding',
                            membersContentReference.name().localName(),
                            membersContentReference)

other = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'other'),
    pyxb.binding.datatypes.anyType, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd', 32, 4))
Namespace.addCategoryObject('elementBinding', other.name().localName(), other)

execEnable = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'execEnable'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd', 47,
        4))
Namespace.addCategoryObject('elementBinding', execEnable.name().localName(),
                            execEnable)

execInstancesReference = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'execInstancesReference'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd', 64,
        4))
Namespace.addCategoryObject('elementBinding',
                            execInstancesReference.name().localName(),
                            execInstancesReference)

serverCapability = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'serverCapability'),
    pyxb.binding.datatypes.boolean, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 43, 4))
Namespace.addCategoryObject('elementBinding',
                            serverCapability.name().localName(),
                            serverCapability)

remTriggerAddr = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'remTriggerAddr'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 45, 4))
Namespace.addCategoryObject('elementBinding', remTriggerAddr.name().localName(),
                            remTriggerAddr)

locTargetDevice = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'locTargetDevice'),
    pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 46, 4))
Namespace.addCategoryObject('elementBinding',
                            locTargetDevice.name().localName(), locTargetDevice)

publicDomain = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'publicDomain'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 49, 4))
Namespace.addCategoryObject('elementBinding', publicDomain.name().localName(),
                            publicDomain)

m2mPocsReference = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'm2mPocsReference'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 51, 4))
Namespace.addCategoryObject('elementBinding',
                            m2mPocsReference.name().localName(),
                            m2mPocsReference)

attachedDevicesReference = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'attachedDevicesReference'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 52, 4))
Namespace.addCategoryObject('elementBinding',
                            attachedDevicesReference.name().localName(),
                            attachedDevicesReference)

sclAnncsReference = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclAnncsReference'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 53, 4))
Namespace.addCategoryObject('elementBinding',
                            sclAnncsReference.name().localName(),
                            sclAnncsReference)

sclsReference = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclsReference'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd', 28,
        4))
Namespace.addCategoryObject('elementBinding', sclsReference.name().localName(),
                            sclsReference)

discoveryReference = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'discoveryReference'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd', 29,
        4))
Namespace.addCategoryObject('elementBinding',
                            discoveryReference.name().localName(),
                            discoveryReference)

minimalTimeBetweenNotifications = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'minimalTimeBetweenNotifications'),
    pyxb.binding.datatypes.long,
    documentation=u'\n                In milliseconds.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
        30, 4))
Namespace.addCategoryObject('elementBinding',
                            minimalTimeBetweenNotifications.name().localName(),
                            minimalTimeBetweenNotifications)

contact = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contact'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
        38, 4))
Namespace.addCategoryObject('elementBinding', contact.name().localName(),
                            contact)

aggregateURI = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'aggregateURI'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
        39, 4))
Namespace.addCategoryObject('elementBinding', aggregateURI.name().localName(),
                            aggregateURI)

timeoutReason = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'timeoutReason'),
    pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
        40, 4))
Namespace.addCategoryObject('elementBinding', timeoutReason.name().localName(),
                            timeoutReason)

noRepresentation = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'noRepresentation'),
    pyxb.binding.datatypes.boolean, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
        41, 4))
Namespace.addCategoryObject('elementBinding',
                            noRepresentation.name().localName(),
                            noRepresentation)

subscriberId = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriberId'),
    pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
        42, 4))
Namespace.addCategoryObject('elementBinding', subscriberId.name().localName(),
                            subscriberId)

accessRight = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRight'), AccessRight,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd', 8,
        4))
Namespace.addCategoryObject('elementBinding', accessRight.name().localName(),
                            accessRight)

permissions = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'permissions'), PermissionListType,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        25, 4))
Namespace.addCategoryObject('elementBinding', permissions.name().localName(),
                            permissions)

selfPermissions = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'selfPermissions'),
    PermissionListType, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        26, 4))
Namespace.addCategoryObject('elementBinding',
                            selfPermissions.name().localName(), selfPermissions)

permission = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'permission'), PermissionType,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        34, 4))
Namespace.addCategoryObject('elementBinding', permission.name().localName(),
                            permission)

permissionFlags = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'permissionFlags'),
    PermissionFlagListType, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        44, 4))
Namespace.addCategoryObject('elementBinding',
                            permissionFlags.name().localName(), permissionFlags)

permissionHolders = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'permissionHolders'),
    PermissionHolderType, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        46, 4))
Namespace.addCategoryObject('elementBinding',
                            permissionHolders.name().localName(),
                            permissionHolders)

holderRefs = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'holderRefs'), HolderRefListType,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        58, 4))
Namespace.addCategoryObject('elementBinding', holderRefs.name().localName(),
                            holderRefs)

domains = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'domains'), DomainListType,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        59, 4))
Namespace.addCategoryObject('elementBinding', domains.name().localName(),
                            domains)

all = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'all'),
                                 CTD_ANON, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        75, 4))
Namespace.addCategoryObject('elementBinding', all.name().localName(), all)

flag = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'flag'), PermissionFlagType,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        95, 4))
Namespace.addCategoryObject('elementBinding', flag.name().localName(), flag)

applicationIDs = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'applicationIDs'), ApplicationIDs,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        103, 4))
Namespace.addCategoryObject('elementBinding', applicationIDs.name().localName(),
                            applicationIDs)

sclIDs = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclIDs'), SclIDs,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        114, 4))
Namespace.addCategoryObject('elementBinding', sclIDs.name().localName(), sclIDs)

accessRightAnnc = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightAnnc'), AccessRightAnnc,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRightAnnc.xsd',
        8, 4))
Namespace.addCategoryObject('elementBinding',
                            accessRightAnnc.name().localName(), accessRightAnnc)

accessRights = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRights'), AccessRights,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRights.xsd',
        8, 4))
Namespace.addCategoryObject('elementBinding', accessRights.name().localName(),
                            accessRights)

accessRightCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRights.xsd',
        22, 4))
Namespace.addCategoryObject('elementBinding',
                            accessRightCollection.name().localName(),
                            accessRightCollection)

accessRightAnncCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightAnncCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRights.xsd',
        23, 4))
Namespace.addCategoryObject('elementBinding',
                            accessRightAnncCollection.name().localName(),
                            accessRightAnncCollection)

application = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'application'), Application,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd', 8,
        4))
Namespace.addCategoryObject('elementBinding', application.name().localName(),
                            application)

referencePoint = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'referencePoint'), ReferencePoint,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
        32, 4))
Namespace.addCategoryObject('elementBinding', referencePoint.name().localName(),
                            referencePoint)

aPoCPaths = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'aPoCPaths'), APoCPaths,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
        34, 4))
Namespace.addCategoryObject('elementBinding', aPoCPaths.name().localName(),
                            aPoCPaths)

aPoCPath = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'aPoCPath'), APoCPath,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
        52, 4))
Namespace.addCategoryObject('elementBinding', aPoCPath.name().localName(),
                            aPoCPath)

applicationAnnc = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'applicationAnnc'), ApplicationAnnc,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applicationAnnc.xsd',
        8, 4))
Namespace.addCategoryObject('elementBinding',
                            applicationAnnc.name().localName(), applicationAnnc)

applications = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'applications'), Applications,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
        8, 4))
Namespace.addCategoryObject('elementBinding', applications.name().localName(),
                            applications)

applicationCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'applicationCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
        23, 4))
Namespace.addCategoryObject('elementBinding',
                            applicationCollection.name().localName(),
                            applicationCollection)

applicationAnncCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'applicationAnncCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
        24, 4))
Namespace.addCategoryObject('elementBinding',
                            applicationAnncCollection.name().localName(),
                            applicationAnncCollection)

attachedDevice = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'attachedDevice'), AttachedDevice,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevice.xsd',
        8, 4))
Namespace.addCategoryObject('elementBinding', attachedDevice.name().localName(),
                            attachedDevice)

attachedDevices = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'attachedDevices'), AttachedDevices,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevices.xsd',
        8, 4))
Namespace.addCategoryObject('elementBinding',
                            attachedDevices.name().localName(), attachedDevices)

attachedDeviceCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'attachedDeviceCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevices.xsd',
        23, 4))
Namespace.addCategoryObject('elementBinding',
                            attachedDeviceCollection.name().localName(),
                            attachedDeviceCollection)

bootstrapParamSet = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'bootstrapParamSet'),
    BootstrapParamSet, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/bootstrapParamSet.xsd',
        9, 4))
Namespace.addCategoryObject('elementBinding',
                            bootstrapParamSet.name().localName(),
                            bootstrapParamSet)

sclIdList = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclIdList'), AnyURIList,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/bootstrapParamSet.xsd',
        23, 4))
Namespace.addCategoryObject('elementBinding', sclIdList.name().localName(),
                            sclIdList)

searchStrings = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'searchStrings'), SearchStrings,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 18,
        4))
Namespace.addCategoryObject('elementBinding', searchStrings.name().localName(),
                            searchStrings)

filterCriteria = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'filterCriteria'),
    FilterCriteriaType, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 30,
        4))
Namespace.addCategoryObject('elementBinding', filterCriteria.name().localName(),
                            filterCriteria)

announceTo = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'announceTo'), AnnounceTo,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 58,
        4))
Namespace.addCategoryObject('elementBinding', announceTo.name().localName(),
                            announceTo)

sclList = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclList'), AnyURIList,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 69,
        4))
Namespace.addCategoryObject('elementBinding', sclList.name().localName(),
                            sclList)

namedReference = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'namedReference'),
    ReferenceToNamedResource, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 104,
        4))
Namespace.addCategoryObject('elementBinding', namedReference.name().localName(),
                            namedReference)

scheduleString = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'scheduleString'), ScheduleString,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 115,
        4))
Namespace.addCategoryObject('elementBinding', scheduleString.name().localName(),
                            scheduleString)

onlineStatus = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'onlineStatus'), OnlineStatus,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 126,
        4))
Namespace.addCategoryObject('elementBinding', onlineStatus.name().localName(),
                            onlineStatus)

channelType = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'channelType'), ChannelType,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 138,
        4))
Namespace.addCategoryObject('elementBinding', channelType.name().localName(),
                            channelType)

channelData = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'channelData'), ChannelData,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 146,
        4))
Namespace.addCategoryObject('elementBinding', channelData.name().localName(),
                            channelData)

statusCode = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'statusCode'), StatusCode,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 186,
        4))
Namespace.addCategoryObject('elementBinding', statusCode.name().localName(),
                            statusCode)

aPocHandling = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'aPocHandling'), APocHandling,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 210,
        4))
Namespace.addCategoryObject('elementBinding', aPocHandling.name().localName(),
                            aPocHandling)

parametersCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'parametersCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 14,
        4))
Namespace.addCategoryObject('elementBinding',
                            parametersCollection.name().localName(),
                            parametersCollection)

rcatValue = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'rcatValue'), RcatType,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 53,
        4))
Namespace.addCategoryObject('elementBinding', rcatValue.name().localName(),
                            rcatValue)

softwareVersion = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'softwareVersion'), swVersion,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 57,
        4))
Namespace.addCategoryObject('elementBinding',
                            softwareVersion.name().localName(), softwareVersion)

areaNwkTypeItem = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'areaNwkTypeItem'),
    NameValuePairItem, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 72,
        4))
Namespace.addCategoryObject('elementBinding',
                            areaNwkTypeItem.name().localName(), areaNwkTypeItem)

securityM2MNodeId = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'securityM2MNodeId'), STD_ANON_,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        6, 4))
Namespace.addCategoryObject('elementBinding',
                            securityM2MNodeId.name().localName(),
                            securityM2MNodeId)

securityEncryptedM2MKey = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'securityEncryptedM2MKey'),
    STD_ANON_2, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        20, 4))
Namespace.addCategoryObject('elementBinding',
                            securityEncryptedM2MKey.name().localName(),
                            securityEncryptedM2MKey)

securitymIdFlags = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'securitymIdFlags'), STD_ANON_3,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        32, 4))
Namespace.addCategoryObject('elementBinding',
                            securitymIdFlags.name().localName(),
                            securitymIdFlags)

securityXmlAlgorithmsFlags = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'securityXmlAlgorithmsFlags'),
    STD_ANON_4, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        40, 4))
Namespace.addCategoryObject('elementBinding',
                            securityXmlAlgorithmsFlags.name().localName(),
                            securityXmlAlgorithmsFlags)

communicationChannel = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'communicationChannel'),
    CommunicationChannel, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannel.xsd',
        8, 4))
Namespace.addCategoryObject('elementBinding',
                            communicationChannel.name().localName(),
                            communicationChannel)

communicationChannels = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'communicationChannels'),
    CommunicationChannels, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannels.xsd',
        8, 4))
Namespace.addCategoryObject('elementBinding',
                            communicationChannels.name().localName(),
                            communicationChannels)

communicationChannelCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'communicationChannelCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannels.xsd',
        19, 4))
Namespace.addCategoryObject('elementBinding',
                            communicationChannelCollection.name().localName(),
                            communicationChannelCollection)

connectionParamSet = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'connectionParamSet'),
    ConnectionParamSet, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/connectionParamSet.xsd',
        9, 4))
Namespace.addCategoryObject('elementBinding',
                            connectionParamSet.name().localName(),
                            connectionParamSet)

container = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'container'), Container,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd', 8,
        4))
Namespace.addCategoryObject('elementBinding', container.name().localName(),
                            container)

containerAnnc = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'containerAnnc'), ContainerAnnc,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containerAnnc.xsd',
        8, 4))
Namespace.addCategoryObject('elementBinding', containerAnnc.name().localName(),
                            containerAnnc)

containers = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'containers'), Containers,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd', 8,
        4))
Namespace.addCategoryObject('elementBinding', containers.name().localName(),
                            containers)

containerCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'containerCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd', 24,
        4))
Namespace.addCategoryObject('elementBinding',
                            containerCollection.name().localName(),
                            containerCollection)

containerAnncCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'containerAnncCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd', 25,
        4))
Namespace.addCategoryObject('elementBinding',
                            containerAnncCollection.name().localName(),
                            containerAnncCollection)

locationContainerCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'locationContainerCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd', 27,
        4))
Namespace.addCategoryObject('elementBinding',
                            locationContainerCollection.name().localName(),
                            locationContainerCollection)

locationContainerAnncCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'locationContainerAnncCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd', 29,
        4))
Namespace.addCategoryObject('elementBinding',
                            locationContainerAnncCollection.name().localName(),
                            locationContainerAnncCollection)

contentInstance = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contentInstance'), ContentInstance,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
        12, 4))
Namespace.addCategoryObject('elementBinding',
                            contentInstance.name().localName(), contentInstance)

contentTypes = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contentTypes'), ContentTypes,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
        41, 4))
Namespace.addCategoryObject('elementBinding', contentTypes.name().localName(),
                            contentTypes)

contentInstances = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contentInstances'),
    ContentInstances, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
        9, 4))
Namespace.addCategoryObject('elementBinding',
                            contentInstances.name().localName(),
                            contentInstances)

latest = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'latest'), ReferenceToNamedResource,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
        28, 4))
Namespace.addCategoryObject('elementBinding', latest.name().localName(), latest)

oldest = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'oldest'), ReferenceToNamedResource,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
        29, 4))
Namespace.addCategoryObject('elementBinding', oldest.name().localName(), oldest)

contentInstanceCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contentInstanceCollection'),
    ContentInstanceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
        31, 4))
Namespace.addCategoryObject('elementBinding',
                            contentInstanceCollection.name().localName(),
                            contentInstanceCollection)

discovery = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'discovery'), Discovery,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/discovery.xsd', 7,
        4))
Namespace.addCategoryObject('elementBinding', discovery.name().localName(),
                            discovery)

discoveryURI = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'discoveryURI'), AnyURIList,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/discovery.xsd', 17,
        4))
Namespace.addCategoryObject('elementBinding', discoveryURI.name().localName(),
                            discoveryURI)

errorInfo = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'errorInfo'), ErrorInfo,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/errorInfo.xsd', 8,
        4))
Namespace.addCategoryObject('elementBinding', errorInfo.name().localName(),
                            errorInfo)

status = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'status'), AreaNwkStatus,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
        28, 4))
Namespace.addCategoryObject('elementBinding', status.name().localName(), status)

areaNwkTypeInfoOfDevice = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'areaNwkTypeInfoOfDevice'),
    AreaNwkTypeInfoSet, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
        37, 4))
Namespace.addCategoryObject('elementBinding',
                            areaNwkTypeInfoOfDevice.name().localName(),
                            areaNwkTypeInfoOfDevice)

areaNwkType = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'areaNwkType'), AreaNwkType,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInstance.xsd',
        24, 4))
Namespace.addCategoryObject('elementBinding', areaNwkType.name().localName(),
                            areaNwkType)

listOfDevices = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'listOfDevices'), Group,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInstance.xsd',
        39, 4))
Namespace.addCategoryObject('elementBinding', listOfDevices.name().localName(),
                            listOfDevices)

areaNwkTypeInfo = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'areaNwkTypeInfo'),
    AreaNwkTypeInfoSet, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInstance.xsd',
        41, 4))
Namespace.addCategoryObject('elementBinding',
                            areaNwkTypeInfo.name().localName(), areaNwkTypeInfo)

battLevel = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'battLevel'), BatteryLevel,
    documentation=u'\n                Contains the current battery level expressed in percentage.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiBatteryInstance.xsd',
        20, 4))
Namespace.addCategoryObject('elementBinding', battLevel.name().localName(),
                            battLevel)

battStatus = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'battStatus'), BatteryStatus,
    documentation=u'\n                Indicates the status of the battery.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiBatteryInstance.xsd',
        35, 4))
Namespace.addCategoryObject('elementBinding', battStatus.name().localName(),
                            battStatus)

attached = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'attached'), TFboolean,
    documentation=u'\n                When the Device Capability is removable, it indicates whether\n                the device is attached or not to the device.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityInstance.xsd',
        25, 4))
Namespace.addCategoryObject('elementBinding', attached.name().localName(),
                            attached)

capabilityActionStatus = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'capabilityActionStatus'),
    ActionStatus, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityInstance.xsd',
        40, 4))
Namespace.addCategoryObject('elementBinding',
                            capabilityActionStatus.name().localName(),
                            capabilityActionStatus)

firmwareName = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'firmwareName'), fwName,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareInstance.xsd',
        23, 4))
Namespace.addCategoryObject('elementBinding', firmwareName.name().localName(),
                            firmwareName)

firmwareURL = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'firmwareURL'), fwURL,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareInstance.xsd',
        31, 4))
Namespace.addCategoryObject('elementBinding', firmwareURL.name().localName(),
                            firmwareURL)

fwActionStatus = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'fwActionStatus'), ActionStatus,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareInstance.xsd',
        39, 4))
Namespace.addCategoryObject('elementBinding', fwActionStatus.name().localName(),
                            fwActionStatus)

defaultRcatValue = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'defaultRcatValue'), RcatType,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiM2mSpPolicy.xsd',
        21, 4))
Namespace.addCategoryObject('elementBinding',
                            defaultRcatValue.name().localName(),
                            defaultRcatValue)

logTypeId = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'logTypeId'), logTypId,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerformanceLog.xsd',
        22, 4))
Namespace.addCategoryObject('elementBinding', logTypeId.name().localName(),
                            logTypeId)

logData = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'logData'), LogDataFile,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerformanceLog.xsd',
        31, 4))
Namespace.addCategoryObject('elementBinding', logData.name().localName(),
                            logData)

perfoLogActionStatus = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'perfoLogActionStatus'),
    ActionStatus, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerformanceLog.xsd',
        39, 4))
Namespace.addCategoryObject('elementBinding',
                            perfoLogActionStatus.name().localName(),
                            perfoLogActionStatus)

defaultTrpdtValue = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'defaultTrpdtValue'), TrpdtType,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
        25, 4))
Namespace.addCategoryObject('elementBinding',
                            defaultTrpdtValue.name().localName(),
                            defaultTrpdtValue)

maxPendData = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'maxPendData'), MemorySize,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
        27, 4))
Namespace.addCategoryObject('elementBinding', maxPendData.name().localName(),
                            maxPendData)

rankedAnList = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'rankedAnList'), RankedAnList,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
        28, 4))
Namespace.addCategoryObject('elementBinding', rankedAnList.name().localName(),
                            rankedAnList)

rebootLevel = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'rebootLevel'), RebootLevel,
    documentation=u'\n                Indicates the level at which the reboot operation has to be\n                performed.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd', 23,
        4))
Namespace.addCategoryObject('elementBinding', rebootLevel.name().localName(),
                            rebootLevel)

rebootTiming = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'rebootTiming'), RebootTiming,
    documentation=u'\n                Indicates the timing of the requested reboot.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd', 42,
        4))
Namespace.addCategoryObject('elementBinding', rebootTiming.name().localName(),
                            rebootTiming)

rebootActionStatus = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'rebootActionStatus'), ActionStatus,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd', 57,
        4))
Namespace.addCategoryObject('elementBinding',
                            rebootActionStatus.name().localName(),
                            rebootActionStatus)

policyScope = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'policyScope'), AnyURIList,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSafPolicySet.xsd',
        22, 4))
Namespace.addCategoryObject('elementBinding', policyScope.name().localName(),
                            policyScope)

regTargetNsclList = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'regTargetNsclList'), AnyURIList,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd', 28,
        4))
Namespace.addCategoryObject('elementBinding',
                            regTargetNsclList.name().localName(),
                            regTargetNsclList)

regSearchStrings = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'regSearchStrings'), SearchStrings,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd', 31,
        4))
Namespace.addCategoryObject('elementBinding',
                            regSearchStrings.name().localName(),
                            regSearchStrings)

announcedToSclList = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'announcedToSclList'), AnyURIList,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd', 32,
        4))
Namespace.addCategoryObject('elementBinding',
                            announcedToSclList.name().localName(),
                            announcedToSclList)

sclActionStatus = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclActionStatus'), ActionStatus,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd', 35,
        4))
Namespace.addCategoryObject('elementBinding',
                            sclActionStatus.name().localName(), sclActionStatus)

softwareName = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'softwareName'), swName,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareInstance.xsd',
        23, 4))
Namespace.addCategoryObject('elementBinding', softwareName.name().localName(),
                            softwareName)

softwareURL = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'softwareURL'), swURL,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareInstance.xsd',
        32, 4))
Namespace.addCategoryObject('elementBinding', softwareURL.name().localName(),
                            softwareURL)

swActionStatus = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'swActionStatus'), ActionStatus,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareInstance.xsd',
        40, 4))
Namespace.addCategoryObject('elementBinding', swActionStatus.name().localName(),
                            swActionStatus)

eventOccured = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'eventOccured'), OccuredEvents,
    documentation=u'\n                This element indicates the last occurences of the event.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
        25, 4))
Namespace.addCategoryObject('elementBinding', eventOccured.name().localName(),
                            eventOccured)

trapActionStatus = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'trapActionStatus'), ActionStatus,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
        60, 4))
Namespace.addCategoryObject('elementBinding',
                            trapActionStatus.name().localName(),
                            trapActionStatus)

execInstance = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'execInstance'), ExecInstance,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
        8, 4))
Namespace.addCategoryObject('elementBinding', execInstance.name().localName(),
                            execInstance)

execStatus = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'execStatus'), ExecStatus,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
        29, 4))
Namespace.addCategoryObject('elementBinding', execStatus.name().localName(),
                            execStatus)

execResult = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'execResult'), ExecResultList,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
        42, 4))
Namespace.addCategoryObject('elementBinding', execResult.name().localName(),
                            execResult)

execInstances = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'execInstances'), ExecInstances,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstances.xsd',
        10, 4))
Namespace.addCategoryObject('elementBinding', execInstances.name().localName(),
                            execInstances)

execInstanceCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'execInstanceCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstances.xsd',
        24, 4))
Namespace.addCategoryObject('elementBinding',
                            execInstanceCollection.name().localName(),
                            execInstanceCollection)

group = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'group'), Group,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 12, 4))
Namespace.addCategoryObject('elementBinding', group.name().localName(), group)

memberType = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'memberType'), MemberType,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 38, 4))
Namespace.addCategoryObject('elementBinding', memberType.name().localName(),
                            memberType)

members = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'members'), AnyURIList,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 41, 4))
Namespace.addCategoryObject('elementBinding', members.name().localName(),
                            members)

consistencyStrategy = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'consistencyStrategy'),
    ConsistencyStrategy, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 43, 4))
Namespace.addCategoryObject('elementBinding',
                            consistencyStrategy.name().localName(),
                            consistencyStrategy)

groupAnnc = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'groupAnnc'), GroupAnnc,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groupAnnc.xsd', 8,
        4))
Namespace.addCategoryObject('elementBinding', groupAnnc.name().localName(),
                            groupAnnc)

groups = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'groups'), Groups,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groups.xsd', 8, 4))
Namespace.addCategoryObject('elementBinding', groups.name().localName(), groups)

groupCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'groupCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groups.xsd', 22,
        4))
Namespace.addCategoryObject('elementBinding',
                            groupCollection.name().localName(), groupCollection)

groupAnncCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'groupAnncCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groups.xsd', 23,
        4))
Namespace.addCategoryObject('elementBinding',
                            groupAnncCollection.name().localName(),
                            groupAnncCollection)

locationContainerType = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'locationContainerType'),
    LocationContainerType, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/locationContainer.xsd',
        20, 4))
Namespace.addCategoryObject('elementBinding',
                            locationContainerType.name().localName(),
                            locationContainerType)

locationContainerAnnc = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'locationContainerAnnc'),
    LocationContainerAnnc, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/locationContainerAnnc.xsd',
        8, 4))
Namespace.addCategoryObject('elementBinding',
                            locationContainerAnnc.name().localName(),
                            locationContainerAnnc)

m2mPoc = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'm2mPoc'), M2MPoc,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd', 8, 4))
Namespace.addCategoryObject('elementBinding', m2mPoc.name().localName(), m2mPoc)

contactInfo = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contactInfo'), ContactInfo,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd', 23, 4))
Namespace.addCategoryObject('elementBinding', contactInfo.name().localName(),
                            contactInfo)

m2mPocs = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'm2mPocs'), M2MPocs,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPocs.xsd', 8, 4))
Namespace.addCategoryObject('elementBinding', m2mPocs.name().localName(),
                            m2mPocs)

m2mPocCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'm2mPocCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPocs.xsd', 19,
        4))
Namespace.addCategoryObject('elementBinding',
                            m2mPocCollection.name().localName(),
                            m2mPocCollection)

membersContentResponses = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'membersContentResponses'),
    CTD_ANON_, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
        12, 4))
Namespace.addCategoryObject('elementBinding',
                            membersContentResponses.name().localName(),
                            membersContentResponses)

mgmtCmd = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'mgmtCmd'), MgmtCmd,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd', 8, 4))
Namespace.addCategoryObject('elementBinding', mgmtCmd.name().localName(),
                            mgmtCmd)

cmdType = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'cmdType'), CmdType,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd', 34,
        4))
Namespace.addCategoryObject('elementBinding', cmdType.name().localName(),
                            cmdType)

execReqArgs = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'execReqArgs'), ExecReqArgsList,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd', 49,
        4))
Namespace.addCategoryObject('elementBinding', execReqArgs.name().localName(),
                            execReqArgs)

mgmtObjs = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'mgmtObjs'), MgmtObjs,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObjs.xsd', 7,
        4))
Namespace.addCategoryObject('elementBinding', mgmtObjs.name().localName(),
                            mgmtObjs)

mgmtObjCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'mgmtObjCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObjs.xsd', 21,
        4))
Namespace.addCategoryObject('elementBinding',
                            mgmtObjCollection.name().localName(),
                            mgmtObjCollection)

mgmtCmdCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'mgmtCmdCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObjs.xsd', 22,
        4))
Namespace.addCategoryObject('elementBinding',
                            mgmtCmdCollection.name().localName(),
                            mgmtCmdCollection)

notificationChannel = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'notificationChannel'),
    NotificationChannel, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannel.xsd',
        8, 4))
Namespace.addCategoryObject('elementBinding',
                            notificationChannel.name().localName(),
                            notificationChannel)

notificationChannels = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'notificationChannels'),
    NotificationChannels, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannels.xsd',
        8, 4))
Namespace.addCategoryObject('elementBinding',
                            notificationChannels.name().localName(),
                            notificationChannels)

notificationChannelCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'notificationChannelCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannels.xsd',
        19, 4))
Namespace.addCategoryObject('elementBinding',
                            notificationChannelCollection.name().localName(),
                            notificationChannelCollection)

notify = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'notify'), Notify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd', 9, 4))
Namespace.addCategoryObject('elementBinding', notify.name().localName(), notify)

notifyCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'notifyCollection'),
    NotifyCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notifyCollection.xsd',
        12, 4))
Namespace.addCategoryObject('elementBinding',
                            notifyCollection.name().localName(),
                            notifyCollection)

notifyCollectionResponse = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'notifyCollectionResponse'),
    CTD_ANON_3, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notifyCollectionResponse.xsd',
        12, 4))
Namespace.addCategoryObject('elementBinding',
                            notifyCollectionResponse.name().localName(),
                            notifyCollectionResponse)

requestNotify = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'requestNotify'), RequestNotify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
        11, 4))
Namespace.addCategoryObject('elementBinding', requestNotify.name().localName(),
                            requestNotify)

responseNotify = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'responseNotify'), ResponseNotify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/responseNotify.xsd',
        11, 4))
Namespace.addCategoryObject('elementBinding', responseNotify.name().localName(),
                            responseNotify)

scl = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'scl'),
                                 Scl, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 6, 4))
Namespace.addCategoryObject('elementBinding', scl.name().localName(), scl)

pocs = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'pocs'), AnyURIList,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 42, 4))
Namespace.addCategoryObject('elementBinding', pocs.name().localName(), pocs)

schedule = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'schedule'), Schedule,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 44, 4))
Namespace.addCategoryObject('elementBinding', schedule.name().localName(),
                            schedule)

mgmtProtocolType = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'mgmtProtocolType'),
    MgmtProtocolType, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 47, 4))
Namespace.addCategoryObject('elementBinding',
                            mgmtProtocolType.name().localName(),
                            mgmtProtocolType)

sclType = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclType'), SclType,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 48, 4))
Namespace.addCategoryObject('elementBinding', sclType.name().localName(),
                            sclType)

integrityValResults = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'integrityValResults'),
    IntegrityValResults, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 50, 4))
Namespace.addCategoryObject('elementBinding',
                            integrityValResults.name().localName(),
                            integrityValResults)

sclAnnc = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclAnnc'), SclAnnc,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnnc.xsd', 8, 4))
Namespace.addCategoryObject('elementBinding', sclAnnc.name().localName(),
                            sclAnnc)

sclAnncs = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclAnncs'), SclAnncs,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnncs.xsd', 8,
        4))
Namespace.addCategoryObject('elementBinding', sclAnncs.name().localName(),
                            sclAnncs)

sclAnncCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclAnncCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnncs.xsd', 22,
        4))
Namespace.addCategoryObject('elementBinding',
                            sclAnncCollection.name().localName(),
                            sclAnncCollection)

sclBase = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclBase'), SclBase,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd', 8, 4))
Namespace.addCategoryObject('elementBinding', sclBase.name().localName(),
                            sclBase)

scls = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'scls'), Scls,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scls.xsd', 8, 4))
Namespace.addCategoryObject('elementBinding', scls.name().localName(), scls)

sclCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scls.xsd', 23, 4))
Namespace.addCategoryObject('elementBinding', sclCollection.name().localName(),
                            sclCollection)

subcontainers = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subcontainers'), Subcontainers,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subcontainers.xsd',
        8, 4))
Namespace.addCategoryObject('elementBinding', subcontainers.name().localName(),
                            subcontainers)

subscription = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscription'), Subscription,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
        9, 4))
Namespace.addCategoryObject('elementBinding', subscription.name().localName(),
                            subscription)

subscriptionType = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionType'),
    SubscriptionType, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
        37, 4))
Namespace.addCategoryObject('elementBinding',
                            subscriptionType.name().localName(),
                            subscriptionType)

subscriptions = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptions'), Subscriptions,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscriptions.xsd',
        8, 4))
Namespace.addCategoryObject('elementBinding', subscriptions.name().localName(),
                            subscriptions)

subscriptionCollection = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionCollection'),
    NamedReferenceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscriptions.xsd',
        17, 4))
Namespace.addCategoryObject('elementBinding',
                            subscriptionCollection.name().localName(),
                            subscriptionCollection)

content = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'content'), Content,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
        28, 4))
Namespace.addCategoryObject('elementBinding', content.name().localName(),
                            content)

m2mSpPolicy = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'm2mSpPolicy'), M2mSpPolicy,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiM2mSpPolicy.xsd',
        8, 4))
Namespace.addCategoryObject('elementBinding', m2mSpPolicy.name().localName(),
                            m2mSpPolicy)

safPolicySet = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'safPolicySet'), SafPolicySet,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSafPolicySet.xsd',
        8, 4))
Namespace.addCategoryObject('elementBinding', safPolicySet.name().localName(),
                            safPolicySet)

locationContainer = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'locationContainer'),
    LocationContainer, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/locationContainer.xsd',
        8, 4))
Namespace.addCategoryObject('elementBinding',
                            locationContainer.name().localName(),
                            locationContainer)

AccessRight._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'permissions'), PermissionListType,
    scope=AccessRight, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        25, 4)))

AccessRight._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'selfPermissions'),
    PermissionListType, scope=AccessRight, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        26, 4)))

AccessRight._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=AccessRight,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

AccessRight._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=AccessRight,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

AccessRight._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
    pyxb.binding.datatypes.dateTime, scope=AccessRight,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 16,
        4)))

AccessRight._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'searchStrings'), SearchStrings,
    scope=AccessRight, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 18,
        4)))

AccessRight._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'announceTo'), AnnounceTo,
    scope=AccessRight, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 58,
        4)))

AccessRight._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=AccessRight,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))


def _BuildAutomaton():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                    15, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                    16, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                    17, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                    20, 12))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AccessRight._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AccessRight._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AccessRight._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AccessRight._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AccessRight._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'announceTo')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AccessRight._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'permissions')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AccessRight._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'selfPermissions')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                                 18, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(AccessRight._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                                 20, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
    ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True)]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


AccessRight._Automaton = _BuildAutomaton()

PermissionListType._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'permission'), PermissionType,
    scope=PermissionListType, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        34, 4)))


def _BuildAutomaton_():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                    30, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PermissionListType._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'permission')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                                 30, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


PermissionListType._Automaton = _BuildAutomaton_()

PermissionType._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'permissionFlags'),
    PermissionFlagListType, scope=PermissionType,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        44, 4)))

PermissionType._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'permissionHolders'),
    PermissionHolderType, scope=PermissionType,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        46, 4)))


def _BuildAutomaton_2():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PermissionType._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'permissionFlags')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                                 38, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PermissionType._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'permissionHolders')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                                 39, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


PermissionType._Automaton = _BuildAutomaton_2()





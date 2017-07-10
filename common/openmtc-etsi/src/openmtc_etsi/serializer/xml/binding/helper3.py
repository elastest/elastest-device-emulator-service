import pyxb
import pyxb.binding
import pyxb.utils
import pyxb.utils.utility

from _binding import *


Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=Scl,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=Scl,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=Scl,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
    pyxb.binding.datatypes.dateTime, scope=Scl,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 16,
        4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'searchStrings'), SearchStrings,
    scope=Scl, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 18,
        4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'announceTo'), AnnounceTo,
    scope=Scl, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 58,
        4)))

Scl._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'link'),
                               pyxb.binding.datatypes.anyURI, scope=Scl,
                               location=pyxb.utils.utility.Location(
                                   u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                   74, 4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=Scl,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'groupsReference'),
    pyxb.binding.datatypes.anyURI, scope=Scl,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 77,
        4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'applicationsReference'),
    pyxb.binding.datatypes.anyURI, scope=Scl,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 78,
        4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'containersReference'),
    pyxb.binding.datatypes.anyURI, scope=Scl,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 79,
        4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightsReference'),
    pyxb.binding.datatypes.anyURI, scope=Scl,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 81,
        4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'notificationChannelsReference'),
    pyxb.binding.datatypes.anyURI, scope=Scl,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 82,
        4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'communicationChannelsReference'),
    pyxb.binding.datatypes.anyURI, scope=Scl,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 83,
        4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'mgmtObjsReference'),
    pyxb.binding.datatypes.anyURI, scope=Scl,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 84,
        4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'onlineStatus'), OnlineStatus,
    scope=Scl, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 126,
        4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'aPocHandling'), APocHandling,
    scope=Scl, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 210,
        4)))

Scl._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pocs'),
                               AnyURIList, scope=Scl,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                   42, 4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'serverCapability'),
    pyxb.binding.datatypes.boolean, scope=Scl,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 43, 4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'schedule'), Schedule, scope=Scl,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 44, 4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'remTriggerAddr'),
    pyxb.binding.datatypes.anyURI, scope=Scl,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 45, 4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'locTargetDevice'),
    pyxb.binding.datatypes.string, scope=Scl,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 46, 4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'mgmtProtocolType'),
    MgmtProtocolType, scope=Scl, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 47, 4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclType'), SclType, scope=Scl,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 48, 4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'publicDomain'),
    pyxb.binding.datatypes.anyURI, scope=Scl,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 49, 4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'integrityValResults'),
    IntegrityValResults, scope=Scl, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 50, 4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'm2mPocsReference'),
    pyxb.binding.datatypes.anyURI, scope=Scl,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 51, 4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'attachedDevicesReference'),
    pyxb.binding.datatypes.anyURI, scope=Scl,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 52, 4)))

Scl._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclAnncsReference'),
    pyxb.binding.datatypes.anyURI, scope=Scl,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 53, 4)))


def _BuildAutomaton_71():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_71
    del _BuildAutomaton_71
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                    9, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                    10, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                    11, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                    12, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                    13, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                    14, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                    15, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                    16, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                    17, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                    18, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                     19, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                     20, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                     21, 12))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                     22, 12))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                     23, 12))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                     24, 12))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                     25, 12))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                     26, 12))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                     28, 12))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                     29, 12))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                     30, 12))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                     31, 12))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                     32, 12))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                     33, 12))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                     34, 12))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                     35, 12))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                     36, 12))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                     37, 12))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                     38, 12))
    counters.add(cc_28)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        Scl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pocs')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 9,
            12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Scl._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'remTriggerAddr')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 10, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        Scl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'onlineStatus')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 11,
            12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Scl._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'serverCapability')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 12, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(
        Scl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'link')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 13,
            12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(
        Scl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'schedule')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 14,
            12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Scl._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 15, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Scl._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 16, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Scl._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 17, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(
        Scl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 18,
            12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Scl._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 19, 12))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Scl._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'locTargetDevice')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 20, 12))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(Scl._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'mgmtProtocolType')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 21, 12))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(Scl._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'integrityValResults')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 22, 12))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(
        Scl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'aPocHandling')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 23,
            12))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(
        Scl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sclType')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 24,
            12))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(
        Scl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'announceTo')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 25,
            12))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(
        Scl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'publicDomain')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 26,
            12))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(Scl._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'containersReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 28, 12))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(Scl._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'groupsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 29, 12))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(Scl._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'applicationsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 30, 12))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(Scl._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 31, 12))
    st_21 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(Scl._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 32, 12))
    st_22 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(Scl._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'mgmtObjsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 33, 12))
    st_23 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(Scl._UseForTag(
        pyxb.namespace.ExpandedName(Namespace,
                                    u'notificationChannelsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 34, 12))
    st_24 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(Scl._UseForTag(
        pyxb.namespace.ExpandedName(Namespace,
                                    u'communicationChannelsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 35, 12))
    st_25 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_26, False))
    symbol = pyxb.binding.content.ElementUse(Scl._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'm2mPocsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 36, 12))
    st_26 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_27, False))
    symbol = pyxb.binding.content.ElementUse(Scl._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'attachedDevicesReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 37, 12))
    st_27 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_28, False))
    symbol = pyxb.binding.content.ElementUse(Scl._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'sclAnncsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 38, 12))
    st_28 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_28)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_28, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_28, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_28, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_9, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_10, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_11, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_12, False)]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False)]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False)]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False)]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False)]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_15, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False)]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False)]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_16, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, False)]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_17, True)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False)]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_17, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_17, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_17, False)]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_18, True)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, False)]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_18, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_18, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_18, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_18, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_18, False)]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_19, True)]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, False)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_19, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_19, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_19, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_19, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_19, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_19, False)]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_20, True)]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_20, False)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_20, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_20, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_20, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_20, False)]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_21, True)]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_21, False)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_21, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_21, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_21, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_21, False)]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_22, True)]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_22, False)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_22, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_22, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_22, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_22, False)]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_23, True)]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_23, False)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_23, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_23, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_23, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_23, False)]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_24, True)]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_24, False)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_24, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_24, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_24, False)]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_25, True)]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_25, False)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_25, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_25, False)]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_26, True)]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_26, False)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_26, False)]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_27, True)]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_27, False)]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_28, True)]))
    st_28._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Scl._Automaton = _BuildAutomaton_71()

IntegrityValResults._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'ivalResults'),
    pyxb.binding.datatypes.long, scope=IntegrityValResults,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 70, 12)))

IntegrityValResults._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'signedIvalResult'),
    pyxb.binding.datatypes.long, scope=IntegrityValResults,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 71, 12)))

IntegrityValResults._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'secureTimeStamp'),
    pyxb.binding.datatypes.dateTime, scope=IntegrityValResults,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd', 72, 12)))


def _BuildAutomaton_72():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_72
    del _BuildAutomaton_72
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(IntegrityValResults._UseForTag(
        pyxb.namespace.ExpandedName(None, u'ivalResults')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 70, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(IntegrityValResults._UseForTag(
        pyxb.namespace.ExpandedName(None, u'signedIvalResult')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 71, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(IntegrityValResults._UseForTag(
        pyxb.namespace.ExpandedName(None, u'secureTimeStamp')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scl.xsd',
                                                 72, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


IntegrityValResults._Automaton = _BuildAutomaton_72()

SclAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=SclAnnc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

SclAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
    pyxb.binding.datatypes.dateTime, scope=SclAnnc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 16,
        4)))

SclAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'searchStrings'), SearchStrings,
    scope=SclAnnc, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 18,
        4)))

SclAnnc._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'link'),
                               pyxb.binding.datatypes.anyURI, scope=SclAnnc,
                               location=pyxb.utils.utility.Location(
                                   u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                   74, 4)))

SclAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'groupsReference'),
    pyxb.binding.datatypes.anyURI, scope=SclAnnc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 77,
        4)))

SclAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'applicationsReference'),
    pyxb.binding.datatypes.anyURI, scope=SclAnnc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 78,
        4)))

SclAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'containersReference'),
    pyxb.binding.datatypes.anyURI, scope=SclAnnc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 79,
        4)))

SclAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightsReference'),
    pyxb.binding.datatypes.anyURI, scope=SclAnnc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 81,
        4)))


def _BuildAutomaton_73():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_73
    del _BuildAutomaton_73
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnnc.xsd',
                                    13, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnnc.xsd',
                                    14, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnnc.xsd',
                                    15, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnnc.xsd',
                                    17, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnnc.xsd',
                                    18, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnnc.xsd',
                                    19, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnnc.xsd',
                                    20, 12))
    counters.add(cc_6)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        SclAnnc._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'link')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnnc.xsd',
            12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SclAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnnc.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SclAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnnc.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SclAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnnc.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SclAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'applicationsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnnc.xsd',
                                                 17, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SclAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'containersReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnnc.xsd',
                                                 18, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SclAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'groupsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnnc.xsd',
                                                 19, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(SclAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnnc.xsd',
                                                 20, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True)]))
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True)]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


SclAnnc._Automaton = _BuildAutomaton_73()

SclAnncs._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=SclAnncs,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

SclAnncs._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=SclAnncs,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

SclAnncs._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=SclAnncs,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

SclAnncs._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=SclAnncs,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))

SclAnncs._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclAnncCollection'),
    NamedReferenceCollection, scope=SclAnncs,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnncs.xsd', 22,
        4)))


def _BuildAutomaton_74():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_74
    del _BuildAutomaton_74
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnncs.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnncs.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnncs.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnncs.xsd',
                                    16, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnncs.xsd',
                                    17, 12))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SclAnncs._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnncs.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SclAnncs._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnncs.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SclAnncs._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnncs.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SclAnncs._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'sclAnncCollection')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnncs.xsd',
                                                 16, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SclAnncs._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclAnncs.xsd',
                                                 17, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


SclAnncs._Automaton = _BuildAutomaton_74()

SclBase._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=SclBase,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

SclBase._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=SclBase,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

SclBase._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=SclBase,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

SclBase._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'searchStrings'), SearchStrings,
    scope=SclBase, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 18,
        4)))

SclBase._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=SclBase,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))

SclBase._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'groupsReference'),
    pyxb.binding.datatypes.anyURI, scope=SclBase,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 77,
        4)))

SclBase._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'applicationsReference'),
    pyxb.binding.datatypes.anyURI, scope=SclBase,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 78,
        4)))

SclBase._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'containersReference'),
    pyxb.binding.datatypes.anyURI, scope=SclBase,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 79,
        4)))

SclBase._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightsReference'),
    pyxb.binding.datatypes.anyURI, scope=SclBase,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 81,
        4)))

SclBase._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'aPocHandling'), APocHandling,
    scope=SclBase, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 210,
        4)))

SclBase._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclsReference'),
    pyxb.binding.datatypes.anyURI, scope=SclBase,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd', 28,
        4)))

SclBase._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'discoveryReference'),
    pyxb.binding.datatypes.anyURI, scope=SclBase,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd', 29,
        4)))


def _BuildAutomaton_75():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_75
    del _BuildAutomaton_75
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                    15, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                    16, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                    18, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                    19, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                    20, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                    21, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                    22, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                     23, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                     24, 12))
    counters.add(cc_11)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SclBase._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SclBase._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SclBase._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SclBase._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SclBase._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'aPocHandling')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SclBase._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'sclsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                                 18, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(SclBase._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'applicationsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                                 19, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(SclBase._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'containersReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                                 20, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(SclBase._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'groupsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                                 21, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(SclBase._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                                 22, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(SclBase._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                                 23, 12))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(SclBase._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'discoveryReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/sclBase.xsd',
                                                 24, 12))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_11, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True)]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


SclBase._Automaton = _BuildAutomaton_75()

Scls._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=Scls,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

Scls._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=Scls,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

Scls._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=Scls,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

Scls._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=Scls,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))

Scls._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'mgmtObjsReference'),
    pyxb.binding.datatypes.anyURI, scope=Scls,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 84,
        4)))

Scls._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclCollection'),
    NamedReferenceCollection, scope=Scls, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scls.xsd', 23, 4)))


def _BuildAutomaton_76():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_76
    del _BuildAutomaton_76
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scls.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scls.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scls.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scls.xsd',
                                    16, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scls.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scls.xsd',
                                    18, 12))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Scls._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scls.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Scls._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scls.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Scls._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scls.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Scls._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'sclCollection')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scls.xsd',
                                                 16, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Scls._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scls.xsd',
                                                 17, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Scls._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'mgmtObjsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/scls.xsd',
                                                 18, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Scls._Automaton = _BuildAutomaton_76()

Subcontainers._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=Subcontainers,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

Subcontainers._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=Subcontainers,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

Subcontainers._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=Subcontainers,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

Subcontainers._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=Subcontainers,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))

Subcontainers._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'containerCollection'),
    NamedReferenceCollection, scope=Subcontainers,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subcontainers.xsd',
        21, 4)))


def _BuildAutomaton_76b():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_76b
    del _BuildAutomaton_76b
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subcontainers.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subcontainers.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subcontainers.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subcontainers.xsd',
                                    16, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subcontainers.xsd',
                                    17, 12))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Subcontainers._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subcontainers.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Subcontainers._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subcontainers.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Subcontainers._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subcontainers.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Subcontainers._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'containerCollection')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subcontainers.xsd',
                                                 16, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Subcontainers._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subcontainers.xsd',
                                                 17, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Subcontainers._Automaton = _BuildAutomaton_76b()

Subscription._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=Subscription,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

Subscription._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=Subscription,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

Subscription._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
    pyxb.binding.datatypes.dateTime, scope=Subscription,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 16,
        4)))

Subscription._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'filterCriteria'),
    FilterCriteriaType, scope=Subscription,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 30,
        4)))

Subscription._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'delayTolerance'),
    pyxb.binding.datatypes.dateTime, scope=Subscription,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 72,
        4)))

Subscription._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'minimalTimeBetweenNotifications'),
    pyxb.binding.datatypes.long, scope=Subscription,
    documentation=u'\n                In milliseconds.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
        30, 4)))

Subscription._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionType'),
    SubscriptionType, scope=Subscription, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
        37, 4)))

Subscription._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contact'),
    pyxb.binding.datatypes.anyURI, scope=Subscription,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
        38, 4)))

Subscription._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'aggregateURI'),
    pyxb.binding.datatypes.anyURI, scope=Subscription,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
        39, 4)))

Subscription._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'timeoutReason'),
    pyxb.binding.datatypes.string, scope=Subscription,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
        40, 4)))

Subscription._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'noRepresentation'),
    pyxb.binding.datatypes.boolean, scope=Subscription,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
        41, 4)))

Subscription._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriberId'),
    pyxb.binding.datatypes.anyURI, scope=Subscription,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
        42, 4)))


def _BuildAutomaton_77():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_77
    del _BuildAutomaton_77
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                    17, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                    18, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                    19, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                    20, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                    21, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                    22, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                    23, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                    24, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                     25, 12))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Subscription._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Subscription._UseForTag(
        pyxb.namespace.ExpandedName(Namespace,
                                    u'minimalTimeBetweenNotifications')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                                 14, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Subscription._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'delayTolerance')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                                 15, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Subscription._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                                 17, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Subscription._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                                 18, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Subscription._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'filterCriteria')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                                 19, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Subscription._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionType')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                                 20, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Subscription._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contact')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                                 21, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Subscription._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'aggregateURI')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                                 22, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Subscription._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'timeoutReason')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                                 23, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Subscription._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'noRepresentation')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                                 24, 12))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Subscription._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriberId')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscription.xsd',
                                                 25, 12))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True)]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Subscription._Automaton = _BuildAutomaton_77()

Subscriptions._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionCollection'),
    NamedReferenceCollection, scope=Subscriptions,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscriptions.xsd',
        17, 4)))


def _BuildAutomaton_78():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_78
    del _BuildAutomaton_78
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscriptions.xsd',
                                    13, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Subscriptions._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionCollection')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/subscriptions.xsd',
                                                 13, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Subscriptions._Automaton = _BuildAutomaton_78()

LongPollingChannelData._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'longPollingURI'),
    pyxb.binding.datatypes.anyURI, scope=LongPollingChannelData,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 162,
        4)))


def _BuildAutomaton_79():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_79
    del _BuildAutomaton_79
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LongPollingChannelData._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'longPollingURI')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                                 156, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


LongPollingChannelData._Automaton = _BuildAutomaton_79()

Content._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'textContent'),
    pyxb.binding.datatypes.string, scope=Content,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
        37, 4)))

Content._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'binaryContent'),
    pyxb.binding.datatypes.base64Binary, scope=Content,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
        38, 4)))


def _BuildAutomaton_80():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_80
    del _BuildAutomaton_80
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Content._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'binaryContent')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
                                                 31, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Content._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'textContent')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
                                                 32, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Content._Automaton = _BuildAutomaton_80()

ContentInstancesFilterCriteriaType._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'sizeFrom'),
                               pyxb.binding.datatypes.long,
                               scope=ContentInstancesFilterCriteriaType,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                   45, 20)))

ContentInstancesFilterCriteriaType._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'sizeUntil'),
                               pyxb.binding.datatypes.long,
                               scope=ContentInstancesFilterCriteriaType,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                   47, 20)))

ContentInstancesFilterCriteriaType._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'contentType'),
    pyxb.binding.datatypes.string, scope=ContentInstancesFilterCriteriaType,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
        49, 20)))

ContentInstancesFilterCriteriaType._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'metaDataOnly'),
    pyxb.binding.datatypes.boolean, scope=ContentInstancesFilterCriteriaType,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
        51, 20)))


def _BuildAutomaton_81():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_81
    del _BuildAutomaton_81
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                    34, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                    36, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                    38, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                    41, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1L,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                    43, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                    45, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                    45, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                    47, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                    49, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1L,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                    51, 20))
    counters.add(cc_9)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        ContentInstancesFilterCriteriaType._UseForTag(
            pyxb.namespace.ExpandedName(None, u'ifModifiedSince')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            34, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        ContentInstancesFilterCriteriaType._UseForTag(
            pyxb.namespace.ExpandedName(None, u'ifUnmodifiedSince')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            36, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        ContentInstancesFilterCriteriaType._UseForTag(
            pyxb.namespace.ExpandedName(None, u'ifNoneMatch')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            38, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        ContentInstancesFilterCriteriaType._UseForTag(
            pyxb.namespace.ExpandedName(None, u'attributeAccessor')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            40, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        ContentInstancesFilterCriteriaType._UseForTag(
            pyxb.namespace.ExpandedName(None, u'searchString')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            41, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(
        ContentInstancesFilterCriteriaType._UseForTag(
            pyxb.namespace.ExpandedName(None, u'createdAfter')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            43, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(
        ContentInstancesFilterCriteriaType._UseForTag(
            pyxb.namespace.ExpandedName(None, u'createdBefore')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            45, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(
        ContentInstancesFilterCriteriaType._UseForTag(
            pyxb.namespace.ExpandedName(None, u'sizeFrom')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
            45, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(
        ContentInstancesFilterCriteriaType._UseForTag(
            pyxb.namespace.ExpandedName(None, u'sizeUntil')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
            47, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(
        ContentInstancesFilterCriteriaType._UseForTag(
            pyxb.namespace.ExpandedName(None, u'contentType')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
            49, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(
        ContentInstancesFilterCriteriaType._UseForTag(
            pyxb.namespace.ExpandedName(None, u'metaDataOnly')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
            51, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
    ]))
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    transitions.append(fac.Transition(st_8, [
    ]))
    transitions.append(fac.Transition(st_9, [
    ]))
    transitions.append(fac.Transition(st_10, [
    ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True)]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


ContentInstancesFilterCriteriaType._Automaton = _BuildAutomaton_81()


def _BuildAutomaton_82():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_82
    del _BuildAutomaton_82
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    15, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    16, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    17, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    18, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    19, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    20, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    23, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None,
                                 metadata=pyxb.utils.utility.Location(
                                     u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                     25, 12))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'moID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 18, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contentType')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 19, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'description')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 20, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 22, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 23, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                  25, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
    ]))
    transitions.append(fac.Transition(st_11, [
    ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True)]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


EtsiAreaNwkDeviceInfo._Automaton = _BuildAutomaton_82()

AreaNwkDeviceInfoInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'groupsReference'),
    pyxb.binding.datatypes.anyURI, scope=AreaNwkDeviceInfoInstance,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 77,
        4)))

AreaNwkDeviceInfoInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'areaNwkID'),
    pyxb.binding.datatypes.long, scope=AreaNwkDeviceInfoInstance,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
        27, 4)))

AreaNwkDeviceInfoInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'status'), AreaNwkStatus,
    scope=AreaNwkDeviceInfoInstance, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
        28, 4)))

AreaNwkDeviceInfoInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sleepInterval'),
    pyxb.binding.datatypes.long, scope=AreaNwkDeviceInfoInstance,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
        35, 4)))

AreaNwkDeviceInfoInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sleepDuration'),
    pyxb.binding.datatypes.long, scope=AreaNwkDeviceInfoInstance,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
        36, 4)))

AreaNwkDeviceInfoInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'areaNwkTypeInfoOfDevice'),
    AreaNwkTypeInfoSet, scope=AreaNwkDeviceInfoInstance,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
        37, 4)))


def _BuildAutomaton_83():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_83
    del _BuildAutomaton_83
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    11, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    12, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    13, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    14, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    19, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
                                    21, 20))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        AreaNwkDeviceInfoInstance._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
            11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        AreaNwkDeviceInfoInstance._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
            12, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        AreaNwkDeviceInfoInstance._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
            13, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        AreaNwkDeviceInfoInstance._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
            14, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        AreaNwkDeviceInfoInstance._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
            16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        AreaNwkDeviceInfoInstance._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
            17, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                  19, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        AreaNwkDeviceInfoInstance._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, u'areaNwkID')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
            14, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        AreaNwkDeviceInfoInstance._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, u'sleepInterval')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
            15, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        AreaNwkDeviceInfoInstance._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, u'sleepDuration')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
            16, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        AreaNwkDeviceInfoInstance._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, u'status')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
            17, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        AreaNwkDeviceInfoInstance._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, u'areaNwkTypeInfoOfDevice')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
            18, 20))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(
        AreaNwkDeviceInfoInstance._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, u'groupsReference')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkDeviceInfoInstance.xsd',
            21, 20))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_12)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
    ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
    ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
    ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
    ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
    ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, True)]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


AreaNwkDeviceInfoInstance._Automaton = _BuildAutomaton_83()

EtsiAreaNwkInfo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'numOfAreaNwks'),
    pyxb.binding.datatypes.long, scope=EtsiAreaNwkInfo,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInfo.xsd',
        20, 4)))


def _BuildAutomaton_84():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_84
    del _BuildAutomaton_84
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    15, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    16, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    17, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    18, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    19, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    20, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    23, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None,
                                 metadata=pyxb.utils.utility.Location(
                                     u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                     25, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInfo.xsd',
                                     13, 20))
    counters.add(cc_11)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'moID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 18, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contentType')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 19, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'description')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 20, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 22, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 23, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                  25, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(EtsiAreaNwkInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'numOfAreaNwks')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInfo.xsd',
                                                 13, 20))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_12)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
    ]))
    transitions.append(fac.Transition(st_11, [
    ]))
    transitions.append(fac.Transition(st_12, [
    ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True)]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


EtsiAreaNwkInfo._Automaton = _BuildAutomaton_84()

AreaNwkInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'areaNwkType'), AreaNwkType,
    scope=AreaNwkInstance, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInstance.xsd',
        24, 4)))

AreaNwkInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'listOfDevices'), Group,
    scope=AreaNwkInstance, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInstance.xsd',
        39, 4)))

AreaNwkInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'addressType'),
    pyxb.binding.datatypes.string, scope=AreaNwkInstance,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInstance.xsd',
        40, 4)))

AreaNwkInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'areaNwkTypeInfo'),
    AreaNwkTypeInfoSet, scope=AreaNwkInstance,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInstance.xsd',
        41, 4)))


def _BuildAutomaton_85():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_85
    del _BuildAutomaton_85
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    11, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    12, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    13, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    14, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    19, 12))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AreaNwkInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AreaNwkInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 12, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AreaNwkInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 13, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AreaNwkInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 14, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AreaNwkInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AreaNwkInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                  19, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AreaNwkInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'areaNwkType')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInstance.xsd',
                                                 14, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AreaNwkInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'addressType')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInstance.xsd',
                                                 15, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AreaNwkInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'areaNwkTypeInfo')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInstance.xsd',
                                                 16, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AreaNwkInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'listOfDevices')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiAreaNwkInstance.xsd',
                                                 17, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
    ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
    ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
    ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


AreaNwkInstance._Automaton = _BuildAutomaton_85()

EtsiBattery._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'standbyTime'),
    pyxb.binding.datatypes.long, scope=EtsiBattery,
    documentation=u'\n                Contains the estimated time of operation. It is based on the\n                charge of all the batteries and it is expressed in minutes.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiBattery.xsd',
        20, 4)))


def _BuildAutomaton_86():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_86
    del _BuildAutomaton_86
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    15, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    16, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    17, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    18, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    19, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    20, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    23, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None,
                                 metadata=pyxb.utils.utility.Location(
                                     u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                     25, 12))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiBattery._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiBattery._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiBattery._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiBattery._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiBattery._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        EtsiBattery._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moID')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
            17, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiBattery._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 18, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiBattery._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contentType')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 19, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiBattery._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'description')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 20, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiBattery._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 22, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiBattery._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 23, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                  25, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EtsiBattery._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'standbyTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiBattery.xsd',
                                                 13, 20))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_12)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
    ]))
    transitions.append(fac.Transition(st_11, [
    ]))
    transitions.append(fac.Transition(st_12, [
    ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


EtsiBattery._Automaton = _BuildAutomaton_86()

BatteryInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'battLevel'), BatteryLevel,
    scope=BatteryInstance,
    documentation=u'\n                Contains the current battery level expressed in percentage.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiBatteryInstance.xsd',
        20, 4)))

BatteryInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'battStatus'), BatteryStatus,
    scope=BatteryInstance,
    documentation=u'\n                Indicates the status of the battery.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiBatteryInstance.xsd',
        35, 4)))


def _BuildAutomaton_87():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_87
    del _BuildAutomaton_87
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    11, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    12, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    13, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    14, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    19, 12))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BatteryInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BatteryInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 12, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BatteryInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 13, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BatteryInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 14, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BatteryInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BatteryInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                  19, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BatteryInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'battLevel')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiBatteryInstance.xsd',
                                                 13, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BatteryInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'battStatus')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiBatteryInstance.xsd',
                                                 14, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
    ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


BatteryInstance._Automaton = _BuildAutomaton_87()

CapabilityAction._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'devCapEnable'),
    pyxb.binding.datatypes.anyURI, scope=CapabilityAction,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityAction.xsd',
        22, 4)))

CapabilityAction._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'devCapDisable'),
    pyxb.binding.datatypes.anyURI, scope=CapabilityAction,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityAction.xsd',
        23, 4)))


def _BuildAutomaton_88():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_88
    del _BuildAutomaton_88
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    11, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    12, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    13, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    14, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    19, 12))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CapabilityAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CapabilityAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 12, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CapabilityAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 13, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CapabilityAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 14, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CapabilityAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CapabilityAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                  19, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CapabilityAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'devCapEnable')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityAction.xsd',
                                                 14, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CapabilityAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'devCapDisable')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityAction.xsd',
                                                 15, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
    ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CapabilityAction._Automaton = _BuildAutomaton_88()

CapabilityInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'capabilityName'),
    pyxb.binding.datatypes.string, scope=CapabilityInstance,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityInstance.xsd',
        23, 4)))

CapabilityInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'attached'), TFboolean,
    scope=CapabilityInstance,
    documentation=u'\n                When the Device Capability is removable, it indicates whether\n                the device is attached or not to the device.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityInstance.xsd',
        25, 4)))

CapabilityInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'capabilityActionStatus'),
    ActionStatus, scope=CapabilityInstance,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityInstance.xsd',
        40, 4)))


def _BuildAutomaton_89():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_89
    del _BuildAutomaton_89
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    11, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    12, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    13, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    14, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    19, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityInstance.xsd',
                                    14, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityInstance.xsd',
                                    15, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityInstance.xsd',
                                    16, 20))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CapabilityInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CapabilityInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 12, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CapabilityInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 13, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CapabilityInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 14, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CapabilityInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CapabilityInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                  19, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CapabilityInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'capabilityName')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityInstance.xsd',
                                                 14, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CapabilityInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'attached')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityInstance.xsd',
                                                 15, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CapabilityInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'capabilityActionStatus')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiCapabilityInstance.xsd',
                                                 16, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    transitions.append(fac.Transition(st_8, [
    ]))
    transitions.append(fac.Transition(st_9, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True)]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CapabilityInstance._Automaton = _BuildAutomaton_89()


def _BuildAutomaton_90():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_90
    del _BuildAutomaton_90
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    15, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    16, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    17, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    18, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    19, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    20, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    23, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None,
                                 metadata=pyxb.utils.utility.Location(
                                     u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                     25, 12))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceCapability._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceCapability._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceCapability._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceCapability._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceCapability._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceCapability._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'moID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceCapability._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 18, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceCapability._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contentType')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 19, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceCapability._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'description')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 20, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceCapability._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 22, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceCapability._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 23, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                  25, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
    ]))
    transitions.append(fac.Transition(st_11, [
    ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True)]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


EtsiDeviceCapability._Automaton = _BuildAutomaton_90()

EtsiDeviceInfo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'firmwareVersion'),
    pyxb.binding.datatypes.string, scope=EtsiDeviceInfo,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 55,
        4)))

EtsiDeviceInfo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'softwareVersion'), swVersion,
    scope=EtsiDeviceInfo, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 57,
        4)))

EtsiDeviceInfo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'deviceLabel'),
    pyxb.binding.datatypes.string, scope=EtsiDeviceInfo,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
        27, 4)))

EtsiDeviceInfo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'manufacturer'),
    pyxb.binding.datatypes.string, scope=EtsiDeviceInfo,
    documentation=u'\n                Manufacturer identifier.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
        29, 4)))

EtsiDeviceInfo._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'model'),
                               pyxb.binding.datatypes.string,
                               scope=EtsiDeviceInfo,
                               documentation=u'\n                Manufacturer specified string.\n            ',
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
                                   37, 4)))

EtsiDeviceInfo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'deviceType'),
    pyxb.binding.datatypes.string, scope=EtsiDeviceInfo,
    documentation=u'\n                For example, PDA, meter, sensor, ... .\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
        45, 4)))

EtsiDeviceInfo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'hardwareVersion'),
    pyxb.binding.datatypes.string, scope=EtsiDeviceInfo,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
        54, 4)))


def _BuildAutomaton_91():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_91
    del _BuildAutomaton_91
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    15, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    16, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    17, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    18, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    19, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    20, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    23, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None,
                                 metadata=pyxb.utils.utility.Location(
                                     u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                     25, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
                                     13, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
                                     14, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
                                     15, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
                                     16, 20))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
                                     17, 20))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
                                     18, 20))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
                                     19, 20))
    counters.add(cc_17)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'moID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 18, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contentType')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 19, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'description')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 20, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 22, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 23, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                  25, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'deviceLabel')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
                                                 13, 20))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'manufacturer')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
                                                 14, 20))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'model')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
                                                 15, 20))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'deviceType')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
                                                 16, 20))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'firmwareVersion')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
                                                 17, 20))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'softwareVersion')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
                                                 18, 20))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(EtsiDeviceInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'hardwareVersion')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiDeviceInfo.xsd',
                                                 19, 20))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_18)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
    ]))
    transitions.append(fac.Transition(st_11, [
    ]))
    transitions.append(fac.Transition(st_12, [
    ]))
    transitions.append(fac.Transition(st_13, [
    ]))
    transitions.append(fac.Transition(st_14, [
    ]))
    transitions.append(fac.Transition(st_15, [
    ]))
    transitions.append(fac.Transition(st_16, [
    ]))
    transitions.append(fac.Transition(st_17, [
    ]))
    transitions.append(fac.Transition(st_18, [
    ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False)]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False)]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False)]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False)]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False)]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False)]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, True)]))
    st_18._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


EtsiDeviceInfo._Automaton = _BuildAutomaton_91()


def _BuildAutomaton_92():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_92
    del _BuildAutomaton_92
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    15, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    16, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    17, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    18, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    19, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    20, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    23, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None,
                                 metadata=pyxb.utils.utility.Location(
                                     u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                     25, 12))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiFirmware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiFirmware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiFirmware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiFirmware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiFirmware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiFirmware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'moID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiFirmware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 18, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiFirmware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contentType')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 19, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiFirmware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'description')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 20, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EtsiFirmware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 22, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(EtsiFirmware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 23, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                  25, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
    ]))
    transitions.append(fac.Transition(st_11, [
    ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True)]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


EtsiFirmware._Automaton = _BuildAutomaton_92()

FirmwareAction._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'fwDownload'),
    pyxb.binding.datatypes.anyURI, scope=FirmwareAction,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareAction.xsd',
        22, 4)))

FirmwareAction._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'fwUpdate'),
    pyxb.binding.datatypes.anyURI, scope=FirmwareAction,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareAction.xsd',
        23, 4)))

FirmwareAction._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'fwDownloadAndUpdate'),
    pyxb.binding.datatypes.anyURI, scope=FirmwareAction,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareAction.xsd',
        24, 4)))

FirmwareAction._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'fwRemove'),
    pyxb.binding.datatypes.anyURI, scope=FirmwareAction,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareAction.xsd',
        25, 4)))


def _BuildAutomaton_93():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_93
    del _BuildAutomaton_93
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    11, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    12, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    13, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    14, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    19, 12))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FirmwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FirmwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 12, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FirmwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 13, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FirmwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 14, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FirmwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FirmwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                  19, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FirmwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'fwDownload')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareAction.xsd',
                                                 13, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FirmwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'fwUpdate')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareAction.xsd',
                                                 14, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FirmwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'fwDownloadAndUpdate')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareAction.xsd',
                                                 15, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FirmwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'fwRemove')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareAction.xsd',
                                                 16, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
    ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
    ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
    ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


FirmwareAction._Automaton = _BuildAutomaton_93()

FwInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'firmwareVersion'),
    pyxb.binding.datatypes.string, scope=FwInstance,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 55,
        4)))

FwInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'firmwareName'), fwName,
    scope=FwInstance, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareInstance.xsd',
        23, 4)))

FwInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'firmwareURL'), fwURL,
    scope=FwInstance, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareInstance.xsd',
        31, 4)))

FwInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'fwActionStatus'), ActionStatus,
    scope=FwInstance, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareInstance.xsd',
        39, 4)))


def _BuildAutomaton_94():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_94
    del _BuildAutomaton_94
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    11, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    12, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    13, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    14, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    19, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareInstance.xsd',
                                    16, 20))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FwInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FwInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 12, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FwInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 13, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FwInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 14, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FwInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FwInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                  19, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FwInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'firmwareName')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareInstance.xsd',
                                                 13, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FwInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'firmwareVersion')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareInstance.xsd',
                                                 14, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FwInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'firmwareURL')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareInstance.xsd',
                                                 15, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(FwInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'fwActionStatus')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiFirmwareInstance.xsd',
                                                 16, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
    ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
    ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
    ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, True)]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


FwInstance._Automaton = _BuildAutomaton_94()

M2mSpPolicy._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'defaultRcatValue'), RcatType,
    scope=M2mSpPolicy, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiM2mSpPolicy.xsd',
        21, 4)))


def _BuildAutomaton_95():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_95
    del _BuildAutomaton_95
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    11, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    12, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    13, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    14, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    19, 12))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(M2mSpPolicy._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(M2mSpPolicy._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 12, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(M2mSpPolicy._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 13, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(M2mSpPolicy._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 14, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(M2mSpPolicy._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(M2mSpPolicy._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                  19, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(M2mSpPolicy._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'defaultRcatValue')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiM2mSpPolicy.xsd',
                                                 15, 20))
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


M2mSpPolicy._Automaton = _BuildAutomaton_95()

EtsiMemory._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'ramAvailable'),
    pyxb.binding.datatypes.long, scope=EtsiMemory,
    documentation=u'\n                Expressed in kilobytes.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiMemory.xsd', 21,
        4)))

EtsiMemory._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'ramTotal'),
    pyxb.binding.datatypes.long, scope=EtsiMemory,
    documentation=u'\n                Expressed in kilobytes.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiMemory.xsd', 29,
        4)))


def _BuildAutomaton_96():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_96
    del _BuildAutomaton_96
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    15, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    16, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    17, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    18, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    19, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    20, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    23, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None,
                                 metadata=pyxb.utils.utility.Location(
                                     u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                     25, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiMemory.xsd',
                                     13, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiMemory.xsd',
                                     14, 20))
    counters.add(cc_12)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiMemory._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiMemory._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiMemory._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiMemory._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiMemory._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        EtsiMemory._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moID')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
            17, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiMemory._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 18, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiMemory._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contentType')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 19, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiMemory._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'description')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 20, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EtsiMemory._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 22, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(EtsiMemory._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 23, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                  25, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(EtsiMemory._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'ramAvailable')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiMemory.xsd',
                                                 13, 20))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(EtsiMemory._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'ramTotal')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiMemory.xsd',
                                                 14, 20))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_13)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
    ]))
    transitions.append(fac.Transition(st_11, [
    ]))
    transitions.append(fac.Transition(st_12, [
    ]))
    transitions.append(fac.Transition(st_13, [
    ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False)]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True)]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


EtsiMemory._Automaton = _BuildAutomaton_96()

PerfLogAction._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'perfLogStart'),
    pyxb.binding.datatypes.anyURI, scope=PerfLogAction,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerfLogAction.xsd',
        21, 4)))

PerfLogAction._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'perfLogStop'),
    pyxb.binding.datatypes.anyURI, scope=PerfLogAction,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerfLogAction.xsd',
        22, 4)))


def _BuildAutomaton_97():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_97
    del _BuildAutomaton_97
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    11, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    12, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    13, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    14, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    19, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerfLogAction.xsd',
                                    13, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerfLogAction.xsd',
                                    14, 20))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PerfLogAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PerfLogAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 12, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PerfLogAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 13, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PerfLogAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 14, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PerfLogAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(PerfLogAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                  19, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(PerfLogAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'perfLogStart')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerfLogAction.xsd',
                                                 13, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(PerfLogAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'perfLogStop')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerfLogAction.xsd',
                                                 14, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    transitions.append(fac.Transition(st_8, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True)]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


PerfLogAction._Automaton = _BuildAutomaton_97()

EtsiPerformanceLog._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'logTypeId'), logTypId,
    scope=EtsiPerformanceLog, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerformanceLog.xsd',
        22, 4)))

EtsiPerformanceLog._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'logData'), LogDataFile,
    scope=EtsiPerformanceLog, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerformanceLog.xsd',
        31, 4)))

EtsiPerformanceLog._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'perfoLogActionStatus'),
    ActionStatus, scope=EtsiPerformanceLog,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerformanceLog.xsd',
        39, 4)))


def _BuildAutomaton_98():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_98
    del _BuildAutomaton_98
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    15, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    16, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    17, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    18, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    19, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    20, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    23, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None,
                                 metadata=pyxb.utils.utility.Location(
                                     u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                     25, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerformanceLog.xsd',
                                     13, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerformanceLog.xsd',
                                     14, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerformanceLog.xsd',
                                     15, 20))
    counters.add(cc_13)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiPerformanceLog._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiPerformanceLog._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiPerformanceLog._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiPerformanceLog._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiPerformanceLog._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiPerformanceLog._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'moID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiPerformanceLog._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 18, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiPerformanceLog._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contentType')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 19, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiPerformanceLog._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'description')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 20, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EtsiPerformanceLog._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 22, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(EtsiPerformanceLog._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 23, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                  25, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(EtsiPerformanceLog._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'logTypeId')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerformanceLog.xsd',
                                                 13, 20))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(EtsiPerformanceLog._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'logData')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerformanceLog.xsd',
                                                 14, 20))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(EtsiPerformanceLog._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'perfoLogActionStatus')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerformanceLog.xsd',
                                                 15, 20))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_14)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
    ]))
    transitions.append(fac.Transition(st_11, [
    ]))
    transitions.append(fac.Transition(st_12, [
    ]))
    transitions.append(fac.Transition(st_13, [
    ]))
    transitions.append(fac.Transition(st_14, [
    ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False)]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False)]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True)]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


EtsiPerformanceLog._Automaton = _BuildAutomaton_98()

RcatParamList._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'rcatValue'), RcatType,
    scope=RcatParamList, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 53,
        4)))

RcatParamList._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'defaultTrpdtValue'), TrpdtType,
    scope=RcatParamList, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
        25, 4)))

RcatParamList._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'maxPendReqs'),
    pyxb.binding.datatypes.long, scope=RcatParamList,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
        26, 4)))

RcatParamList._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'maxPendData'), MemorySize,
    scope=RcatParamList, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
        27, 4)))

RcatParamList._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'rankedAnList'), RankedAnList,
    scope=RcatParamList, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
        28, 4)))


def _BuildAutomaton_99():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_99
    del _BuildAutomaton_99
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    11, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    12, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    13, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    14, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    19, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
                                    16, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
                                    17, 20))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RcatParamList._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RcatParamList._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 12, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RcatParamList._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 13, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RcatParamList._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 14, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RcatParamList._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RcatParamList._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                  19, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RcatParamList._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'rcatValue')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
                                                 13, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RcatParamList._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'defaultTrpdtValue')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
                                                 14, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RcatParamList._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'maxPendReqs')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
                                                 16, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RcatParamList._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'maxPendData')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
                                                 17, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RcatParamList._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'rankedAnList')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
                                                 18, 20))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
    ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
    ]))
    transitions.append(fac.Transition(st_10, [
    ]))
    transitions.append(fac.Transition(st_11, [
    ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


RcatParamList._Automaton = _BuildAutomaton_99()

EtsiReboot._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'rebootLevel'), RebootLevel,
    scope=EtsiReboot,
    documentation=u'\n                Indicates the level at which the reboot operation has to be\n                performed.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd', 23,
        4)))

EtsiReboot._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'applicationRef'),
    pyxb.binding.datatypes.string, scope=EtsiReboot,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd', 40,
        4)))

EtsiReboot._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'rebootTiming'), RebootTiming,
    scope=EtsiReboot,
    documentation=u'\n                Indicates the timing of the requested reboot.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd', 42,
        4)))

EtsiReboot._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'rebootActionStatus'), ActionStatus,
    scope=EtsiReboot, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd', 57,
        4)))


def _BuildAutomaton_100():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_100
    del _BuildAutomaton_100
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    15, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    16, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    17, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    18, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    19, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    20, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    23, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None,
                                 metadata=pyxb.utils.utility.Location(
                                     u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                     25, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd',
                                     13, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd',
                                     14, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd',
                                     15, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd',
                                     16, 20))
    counters.add(cc_14)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiReboot._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiReboot._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiReboot._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiReboot._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiReboot._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        EtsiReboot._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moID')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
            17, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiReboot._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 18, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiReboot._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contentType')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 19, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiReboot._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'description')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 20, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EtsiReboot._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 22, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(EtsiReboot._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 23, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                  25, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(EtsiReboot._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'rebootLevel')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd',
                                                 13, 20))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(EtsiReboot._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'rebootTiming')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd',
                                                 14, 20))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(EtsiReboot._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'applicationRef')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd',
                                                 15, 20))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(EtsiReboot._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'rebootActionStatus')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiReboot.xsd',
                                                 16, 20))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_15)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
    ]))
    transitions.append(fac.Transition(st_11, [
    ]))
    transitions.append(fac.Transition(st_12, [
    ]))
    transitions.append(fac.Transition(st_13, [
    ]))
    transitions.append(fac.Transition(st_14, [
    ]))
    transitions.append(fac.Transition(st_15, [
    ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False)]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False)]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False)]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True)]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


EtsiReboot._Automaton = _BuildAutomaton_100()

RebootAction._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'reboot'),
    pyxb.binding.datatypes.anyURI, scope=RebootAction,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRebootAction.xsd',
        22, 4)))

RebootAction._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'factoryReset'),
    pyxb.binding.datatypes.anyURI, scope=RebootAction,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRebootAction.xsd',
        24, 4)))


def _BuildAutomaton_101():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_101
    del _BuildAutomaton_101
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    11, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    12, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    13, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    14, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    19, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRebootAction.xsd',
                                    14, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRebootAction.xsd',
                                    15, 20))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RebootAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RebootAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 12, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RebootAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 13, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RebootAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 14, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RebootAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RebootAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                  19, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(RebootAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'reboot')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRebootAction.xsd',
                                                 14, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(RebootAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'factoryReset')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRebootAction.xsd',
                                                 15, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    transitions.append(fac.Transition(st_8, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True)]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


RebootAction._Automaton = _BuildAutomaton_101()

SafPolicySet._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'policyScope'), AnyURIList,
    scope=SafPolicySet, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSafPolicySet.xsd',
        22, 4)))


def _BuildAutomaton_102():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_102
    del _BuildAutomaton_102
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    11, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    12, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    13, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    14, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    19, 12))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SafPolicySet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SafPolicySet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 12, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SafPolicySet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 13, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SafPolicySet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 14, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SafPolicySet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SafPolicySet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                  19, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SafPolicySet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'policyScope')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSafPolicySet.xsd',
                                                 16, 20))
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


SafPolicySet._Automaton = _BuildAutomaton_102()

EtsiSclMo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'regTargetNsclList'), AnyURIList,
    scope=EtsiSclMo, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd', 28,
        4)))

EtsiSclMo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'regExpirationDuration'),
    pyxb.binding.datatypes.duration, scope=EtsiSclMo,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd', 29,
        4)))

EtsiSclMo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'regAccessRightID'),
    pyxb.binding.datatypes.anyURI, scope=EtsiSclMo,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd', 30,
        4)))

EtsiSclMo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'regSearchStrings'), SearchStrings,
    scope=EtsiSclMo, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd', 31,
        4)))

EtsiSclMo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'announcedToSclList'), AnyURIList,
    scope=EtsiSclMo, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd', 32,
        4)))

EtsiSclMo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'maxNumberOfDiscovRecords'),
    pyxb.binding.datatypes.long, scope=EtsiSclMo,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd', 33,
        4)))

EtsiSclMo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'maxSizeOfDiscovAnswer'),
    pyxb.binding.datatypes.long, scope=EtsiSclMo,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd', 34,
        4)))

EtsiSclMo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclActionStatus'), ActionStatus,
    scope=EtsiSclMo, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd', 35,
        4)))


def _BuildAutomaton_103():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_103
    del _BuildAutomaton_103
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    15, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    16, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    17, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    18, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    19, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    20, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    23, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None,
                                 metadata=pyxb.utils.utility.Location(
                                     u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                     25, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
                                     14, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
                                     15, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
                                     16, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
                                     17, 20))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
                                     18, 20))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
                                     19, 20))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
                                     20, 20))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
                                     21, 20))
    counters.add(cc_18)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiSclMo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiSclMo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiSclMo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiSclMo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiSclMo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        EtsiSclMo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moID')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
            17, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiSclMo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 18, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiSclMo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contentType')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 19, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiSclMo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'description')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 20, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EtsiSclMo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 22, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(EtsiSclMo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 23, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                  25, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(EtsiSclMo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'regTargetNsclList')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
                                                 14, 20))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(EtsiSclMo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'regExpirationDuration')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
                                                 15, 20))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(EtsiSclMo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'regAccessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
                                                 16, 20))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(EtsiSclMo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'regSearchStrings')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
                                                 17, 20))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(EtsiSclMo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'announcedToSclList')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
                                                 18, 20))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(EtsiSclMo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'maxNumberOfDiscovRecords')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
                                                 19, 20))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(EtsiSclMo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'maxSizeOfDiscovAnswer')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
                                                 20, 20))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(EtsiSclMo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'sclActionStatus')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMo.xsd',
                                                 21, 20))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_19)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
    ]))
    transitions.append(fac.Transition(st_11, [
    ]))
    transitions.append(fac.Transition(st_12, [
    ]))
    transitions.append(fac.Transition(st_13, [
    ]))
    transitions.append(fac.Transition(st_14, [
    ]))
    transitions.append(fac.Transition(st_15, [
    ]))
    transitions.append(fac.Transition(st_16, [
    ]))
    transitions.append(fac.Transition(st_17, [
    ]))
    transitions.append(fac.Transition(st_18, [
    ]))
    transitions.append(fac.Transition(st_19, [
    ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False)]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False)]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False)]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True)]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False)]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True)]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False)]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True)]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False)]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, True)]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False)]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, True)]))
    st_19._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


EtsiSclMo._Automaton = _BuildAutomaton_103()

SclMoAction._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'reRegistration'),
    pyxb.binding.datatypes.anyURI, scope=SclMoAction,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMoAction.xsd',
        21, 4)))

SclMoAction._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'deRegistration'),
    pyxb.binding.datatypes.anyURI, scope=SclMoAction,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMoAction.xsd',
        22, 4)))


def _BuildAutomaton_104():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_104
    del _BuildAutomaton_104
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    11, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    12, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    13, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    14, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    19, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMoAction.xsd',
                                    13, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMoAction.xsd',
                                    14, 20))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SclMoAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SclMoAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 12, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SclMoAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 13, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SclMoAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 14, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SclMoAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SclMoAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                  19, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(SclMoAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'reRegistration')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMoAction.xsd',
                                                 13, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(SclMoAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'deRegistration')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSclMoAction.xsd',
                                                 14, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    transitions.append(fac.Transition(st_8, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True)]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


SclMoAction._Automaton = _BuildAutomaton_104()


def _BuildAutomaton_105():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_105
    del _BuildAutomaton_105
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    15, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    16, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    17, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    18, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    19, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    20, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    23, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None,
                                 metadata=pyxb.utils.utility.Location(
                                     u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                     25, 12))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiSoftware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiSoftware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiSoftware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiSoftware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiSoftware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiSoftware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'moID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiSoftware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 18, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiSoftware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contentType')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 19, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiSoftware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'description')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 20, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EtsiSoftware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 22, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(EtsiSoftware._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 23, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                  25, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
    ]))
    transitions.append(fac.Transition(st_11, [
    ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True)]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


EtsiSoftware._Automaton = _BuildAutomaton_105()

SoftwareAction._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'swDownload'),
    pyxb.binding.datatypes.anyURI, scope=SoftwareAction,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
        26, 4)))

SoftwareAction._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'swDownloadAndInstall'),
    pyxb.binding.datatypes.anyURI, scope=SoftwareAction,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
        27, 4)))

SoftwareAction._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'swInstall'),
    pyxb.binding.datatypes.anyURI, scope=SoftwareAction,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
        28, 4)))

SoftwareAction._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'swRemove'),
    pyxb.binding.datatypes.anyURI, scope=SoftwareAction,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
        29, 4)))

SoftwareAction._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'swActivate'),
    pyxb.binding.datatypes.anyURI, scope=SoftwareAction,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
        30, 4)))

SoftwareAction._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'swDeactivate'),
    pyxb.binding.datatypes.anyURI, scope=SoftwareAction,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
        31, 4)))


def _BuildAutomaton_106():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_106
    del _BuildAutomaton_106
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    11, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    12, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    13, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    14, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    19, 12))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SoftwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SoftwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 12, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SoftwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 13, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SoftwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 14, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SoftwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SoftwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                  19, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SoftwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'swDownload')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
                                                 14, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SoftwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'swDownloadAndInstall')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
                                                 15, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SoftwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'swInstall')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
                                                 16, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SoftwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'swRemove')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
                                                 17, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SoftwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'swActivate')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
                                                 18, 20))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SoftwareAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'swDeactivate')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareAction.xsd',
                                                 19, 20))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_12)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
    ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
    ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
    ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
    ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
    ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


SoftwareAction._Automaton = _BuildAutomaton_106()

SwInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'softwareVersion'), swVersion,
    scope=SwInstance, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 57,
        4)))

SwInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'softwareName'), swName,
    scope=SwInstance, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareInstance.xsd',
        23, 4)))

SwInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'softwareURL'), swURL,
    scope=SwInstance, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareInstance.xsd',
        32, 4)))

SwInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'swActionStatus'), ActionStatus,
    scope=SwInstance, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareInstance.xsd',
        40, 4)))


def _BuildAutomaton_107():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_107
    del _BuildAutomaton_107
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    11, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    12, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    13, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    14, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    19, 12))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SwInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SwInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 12, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SwInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 13, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SwInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 14, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SwInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SwInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                  19, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SwInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'softwareName')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareInstance.xsd',
                                                 13, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SwInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'softwareVersion')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareInstance.xsd',
                                                 14, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SwInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'softwareURL')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareInstance.xsd',
                                                 15, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SwInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'swActionStatus')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiSoftwareInstance.xsd',
                                                 16, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
    ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
    ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
    ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


SwInstance._Automaton = _BuildAutomaton_107()


def _BuildAutomaton_108():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_108
    del _BuildAutomaton_108
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    15, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    16, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    17, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    18, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    19, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    20, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                    23, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None,
                                 metadata=pyxb.utils.utility.Location(
                                     u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                     25, 12))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiTrapEvent._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiTrapEvent._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiTrapEvent._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiTrapEvent._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiTrapEvent._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiTrapEvent._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'moID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiTrapEvent._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 18, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiTrapEvent._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contentType')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 19, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EtsiTrapEvent._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'description')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 20, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EtsiTrapEvent._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 22, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(EtsiTrapEvent._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 23, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                  25, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
    ]))
    transitions.append(fac.Transition(st_11, [
    ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True)]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


EtsiTrapEvent._Automaton = _BuildAutomaton_108()

TrapEventAction._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'trapEventEnable'),
    pyxb.binding.datatypes.anyURI, scope=TrapEventAction,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapEventAction.xsd',
        21, 4)))

TrapEventAction._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'trapEventDisable'),
    pyxb.binding.datatypes.anyURI, scope=TrapEventAction,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapEventAction.xsd',
        23, 4)))


def _BuildAutomaton_109():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_109
    del _BuildAutomaton_109
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    11, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    12, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    13, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    14, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    19, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapEventAction.xsd',
                                    13, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapEventAction.xsd',
                                    14, 20))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TrapEventAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TrapEventAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 12, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TrapEventAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 13, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TrapEventAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 14, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TrapEventAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TrapEventAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                  19, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TrapEventAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'trapEventEnable')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapEventAction.xsd',
                                                 13, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(TrapEventAction._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'trapEventDisable')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapEventAction.xsd',
                                                 14, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    transitions.append(fac.Transition(st_8, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True)]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


TrapEventAction._Automaton = _BuildAutomaton_109()

TrapInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'trapId'),
    pyxb.binding.datatypes.string, scope=TrapInstance,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
        23, 4)))

TrapInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'eventOccured'), OccuredEvents,
    scope=TrapInstance,
    documentation=u'\n                This element indicates the last occurences of the event.\n            ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
        25, 4)))

TrapInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'trapActionStatus'), ActionStatus,
    scope=TrapInstance, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
        60, 4)))


def _BuildAutomaton_110():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_110
    del _BuildAutomaton_110
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    11, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    12, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    13, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    14, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                    19, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
                                    13, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
                                    14, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
                                    15, 20))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TrapInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TrapInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 12, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TrapInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 13, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TrapInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 14, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TrapInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TrapInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=(
        pyxb.binding.content.Wildcard.NC_not, u'http://uri.etsi.org/m2m')),
                                              pyxb.utils.utility.Location(
                                                  u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                  19, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TrapInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'trapId')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
                                                 13, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(TrapInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'eventOccured')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
                                                 14, 20))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(TrapInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'trapActionStatus')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
                                                 15, 20))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    transitions.append(fac.Transition(st_7, [
    ]))
    transitions.append(fac.Transition(st_8, [
    ]))
    transitions.append(fac.Transition(st_9, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True)]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


TrapInstance._Automaton = _BuildAutomaton_110()

LocationContainer._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'locationContainerType'),
    LocationContainerType, scope=LocationContainer,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/locationContainer.xsd',
        20, 4)))


def _BuildAutomaton_111():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_111
    del _BuildAutomaton_111
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                    15, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                    16, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                    17, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                    18, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                    19, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                    20, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                    23, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                     24, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                     25, 12))
    counters.add(cc_11)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LocationContainer._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LocationContainer._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LocationContainer._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LocationContainer._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LocationContainer._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LocationContainer._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'announceTo')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LocationContainer._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'maxNrOfInstances')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 18, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LocationContainer._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'maxByteSize')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 19, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LocationContainer._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'maxInstanceAge')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 20, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LocationContainer._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contentInstancesReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 23, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LocationContainer._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subcontainersReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 24, 12))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LocationContainer._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 25, 12))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LocationContainer._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'locationContainerType')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/locationContainer.xsd',
                                                 14, 20))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_12)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_12, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_12, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_12, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


LocationContainer._Automaton = _BuildAutomaton_111()


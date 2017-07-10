import pyxb
import pyxb.binding
import pyxb.utils
import pyxb.utils.utility

from _binding import *
from openmtc_etsi.serializer.xml.binding import \
    _xmlmime as _ImportedBinding__xmlmime


PermissionHolderType._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'holderRefs'), HolderRefListType,
    scope=PermissionHolderType, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        58, 4)))

PermissionHolderType._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'domains'), DomainListType,
    scope=PermissionHolderType, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        59, 4)))

PermissionHolderType._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'all'),
                               CTD_ANON, scope=PermissionHolderType,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                   75, 4)))

PermissionHolderType._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'applicationIDs'), ApplicationIDs,
    scope=PermissionHolderType, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        103, 4)))

PermissionHolderType._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclIDs'), SclIDs,
    scope=PermissionHolderType, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        114, 4)))


def _BuildAutomaton_3():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                    50, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                    51, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                    52, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                    53, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1L,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                    54, 12))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PermissionHolderType._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'holderRefs')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                                 50, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PermissionHolderType._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'applicationIDs')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                                 51, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(PermissionHolderType._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'sclIDs')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                                 52, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(PermissionHolderType._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'all')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                                 53, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(PermissionHolderType._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'domains')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                                 54, 12))
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


PermissionHolderType._Automaton = _BuildAutomaton_3()

HolderRefListType._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'holderRef'),
    pyxb.binding.datatypes.anyURI, scope=HolderRefListType,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        73, 4)))


def _BuildAutomaton_4():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                    63, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(HolderRefListType._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'holderRef')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                                 63, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


HolderRefListType._Automaton = _BuildAutomaton_4()

DomainListType._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'domain'),
    pyxb.binding.datatypes.anyURI, scope=DomainListType,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        83, 4)))


def _BuildAutomaton_5():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                    69, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DomainListType._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'domain')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                                 69, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


DomainListType._Automaton = _BuildAutomaton_5()

PermissionFlagListType._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'flag'),
                               PermissionFlagType, scope=PermissionFlagListType,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                   95, 4)))


def _BuildAutomaton_6():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                    99, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PermissionFlagListType._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'flag')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                                 99, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


PermissionFlagListType._Automaton = _BuildAutomaton_6()

ApplicationIDs._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'applicationID'),
    pyxb.binding.datatypes.string, scope=ApplicationIDs,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
        112, 4)))


def _BuildAutomaton_7():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                    107, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ApplicationIDs._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'applicationID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                                 107, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


ApplicationIDs._Automaton = _BuildAutomaton_7()

SclIDs._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sclID'),
                               pyxb.binding.datatypes.string, scope=SclIDs,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                   122, 4)))


def _BuildAutomaton_8():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
                                    118, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        SclIDs._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sclID')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRight.xsd',
            118, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


SclIDs._Automaton = _BuildAutomaton_8()

AccessRightAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=AccessRightAnnc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

AccessRightAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
    pyxb.binding.datatypes.dateTime, scope=AccessRightAnnc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 16,
        4)))

AccessRightAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'searchStrings'), SearchStrings,
    scope=AccessRightAnnc, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 18,
        4)))

AccessRightAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'announceTo'), AnnounceTo,
    scope=AccessRightAnnc, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 58,
        4)))

AccessRightAnnc._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'link'),
                               pyxb.binding.datatypes.anyURI,
                               scope=AccessRightAnnc,
                               location=pyxb.utils.utility.Location(
                                   u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                   74, 4)))


def _BuildAutomaton_9():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRightAnnc.xsd',
                                    13, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRightAnnc.xsd',
                                    14, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRightAnnc.xsd',
                                    15, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRightAnnc.xsd',
                                    16, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AccessRightAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'link')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRightAnnc.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AccessRightAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRightAnnc.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AccessRightAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRightAnnc.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AccessRightAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRightAnnc.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AccessRightAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'announceTo')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRightAnnc.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True)]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


AccessRightAnnc._Automaton = _BuildAutomaton_9()

AccessRights._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightCollection'),
    NamedReferenceCollection, scope=AccessRights,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRights.xsd',
        22, 4)))

AccessRights._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightAnncCollection'),
    NamedReferenceCollection, scope=AccessRights,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRights.xsd',
        23, 4)))

AccessRights._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=AccessRights,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

AccessRights._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=AccessRights,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

AccessRights._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=AccessRights,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

AccessRights._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=AccessRights,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))


def _BuildAutomaton_10():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRights.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRights.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRights.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRights.xsd',
                                    16, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRights.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRights.xsd',
                                    18, 12))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AccessRights._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRights.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AccessRights._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRights.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AccessRights._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRights.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AccessRights._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightCollection')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRights.xsd',
                                                 16, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AccessRights._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightAnncCollection')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRights.xsd',
                                                 17, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AccessRights._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/accessRights.xsd',
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


AccessRights._Automaton = _BuildAutomaton_10()

Application._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'referencePoint'), ReferencePoint,
    scope=Application, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
        32, 4)))

Application._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'aPoC'),
                               pyxb.binding.datatypes.anyURI, scope=Application,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                   33, 4)))

Application._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'aPoCPaths'), APoCPaths,
    scope=Application, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
        34, 4)))

Application._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'locRequestor'),
    pyxb.binding.datatypes.anyType, scope=Application,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
        36, 4)))

Application._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=Application,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

Application._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=Application,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

Application._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=Application,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

Application._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
    pyxb.binding.datatypes.dateTime, scope=Application,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 16,
        4)))

Application._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'searchStrings'), SearchStrings,
    scope=Application, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 18,
        4)))

Application._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'announceTo'), AnnounceTo,
    scope=Application, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 58,
        4)))

Application._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=Application,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))

Application._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'groupsReference'),
    pyxb.binding.datatypes.anyURI, scope=Application,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 77,
        4)))

Application._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'containersReference'),
    pyxb.binding.datatypes.anyURI, scope=Application,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 79,
        4)))

Application._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightsReference'),
    pyxb.binding.datatypes.anyURI, scope=Application,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 81,
        4)))

Application._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'notificationChannelsReference'),
    pyxb.binding.datatypes.anyURI, scope=Application,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 82,
        4)))


def _BuildAutomaton_11():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                    15, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                    16, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                    17, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                    18, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                    19, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                    20, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                    21, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                     23, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                     24, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                     25, 12))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                     26, 12))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                     27, 12))
    counters.add(cc_14)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Application._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Application._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Application._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Application._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Application._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Application._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'announceTo')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(
        Application._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'aPoC')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
            18, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Application._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'aPoCPaths')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                                 19, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Application._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'locRequestor')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                                 20, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Application._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'referencePoint')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                                 21, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Application._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'containersReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                                 23, 12))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Application._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'groupsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                                 24, 12))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(Application._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                                 25, 12))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(Application._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                                 26, 12))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(Application._UseForTag(
        pyxb.namespace.ExpandedName(Namespace,
                                    u'notificationChannelsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                                 27, 12))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update,
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
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False)]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False)]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True)]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Application._Automaton = _BuildAutomaton_11()

APoCPaths._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'aPoCPath'), APoCPath,
    scope=APoCPaths, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
        52, 4)))


def _BuildAutomaton_12():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                    48, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(APoCPaths._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'aPoCPath')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                                 48, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


APoCPaths._Automaton = _BuildAutomaton_12()

APoCPath._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'path'),
                               pyxb.binding.datatypes.anyURI, scope=APoCPath,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                   62, 4)))

APoCPath._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=APoCPath,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

APoCPath._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'searchStrings'), SearchStrings,
    scope=APoCPath, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 18,
        4)))


def _BuildAutomaton_13():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                    57, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                    58, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        APoCPath._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'path')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
            56, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(APoCPath._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                                 57, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(APoCPath._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/application.xsd',
                                                 58, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    transitions.append(fac.Transition(st_2, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True)]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


APoCPath._Automaton = _BuildAutomaton_13()

ApplicationAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=ApplicationAnnc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

ApplicationAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
    pyxb.binding.datatypes.dateTime, scope=ApplicationAnnc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 16,
        4)))

ApplicationAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'searchStrings'), SearchStrings,
    scope=ApplicationAnnc, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 18,
        4)))

ApplicationAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'announceTo'), AnnounceTo,
    scope=ApplicationAnnc, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 58,
        4)))

ApplicationAnnc._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'link'),
                               pyxb.binding.datatypes.anyURI,
                               scope=ApplicationAnnc,
                               location=pyxb.utils.utility.Location(
                                   u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                   74, 4)))

ApplicationAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'groupsReference'),
    pyxb.binding.datatypes.anyURI, scope=ApplicationAnnc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 77,
        4)))

ApplicationAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'containersReference'),
    pyxb.binding.datatypes.anyURI, scope=ApplicationAnnc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 79,
        4)))

ApplicationAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightsReference'),
    pyxb.binding.datatypes.anyURI, scope=ApplicationAnnc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 81,
        4)))


def _BuildAutomaton_14():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applicationAnnc.xsd',
                                    13, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applicationAnnc.xsd',
                                    14, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applicationAnnc.xsd',
                                    15, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applicationAnnc.xsd',
                                    16, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applicationAnnc.xsd',
                                    18, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applicationAnnc.xsd',
                                    19, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applicationAnnc.xsd',
                                    20, 12))
    counters.add(cc_6)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ApplicationAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'link')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applicationAnnc.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ApplicationAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applicationAnnc.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ApplicationAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applicationAnnc.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ApplicationAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applicationAnnc.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ApplicationAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'announceTo')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applicationAnnc.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ApplicationAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'containersReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applicationAnnc.xsd',
                                                 18, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ApplicationAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'groupsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applicationAnnc.xsd',
                                                 19, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(ApplicationAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applicationAnnc.xsd',
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


ApplicationAnnc._Automaton = _BuildAutomaton_14()

Applications._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'applicationCollection'),
    NamedReferenceCollection, scope=Applications,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
        23, 4)))

Applications._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'applicationAnncCollection'),
    NamedReferenceCollection, scope=Applications,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
        24, 4)))

Applications._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=Applications,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

Applications._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=Applications,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

Applications._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=Applications,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

Applications._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=Applications,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))

Applications._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'mgmtObjsReference'),
    pyxb.binding.datatypes.anyURI, scope=Applications,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 84,
        4)))


def _BuildAutomaton_15():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
                                    16, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
                                    18, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
                                    19, 12))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Applications._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Applications._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Applications._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Applications._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'applicationCollection')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
                                                 16, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Applications._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'applicationAnncCollection')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
                                                 17, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Applications._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
                                                 18, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Applications._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'mgmtObjsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/applications.xsd',
                                                 19, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Applications._Automaton = _BuildAutomaton_15()

AttachedDevice._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=AttachedDevice,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

AttachedDevice._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=AttachedDevice,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

AttachedDevice._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=AttachedDevice,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

AttachedDevice._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=AttachedDevice,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))

AttachedDevice._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'mgmtObjsReference'),
    pyxb.binding.datatypes.anyURI, scope=AttachedDevice,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 84,
        4)))


def _BuildAutomaton_16():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevice.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevice.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevice.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevice.xsd',
                                    17, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevice.xsd',
                                    18, 12))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AttachedDevice._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevice.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AttachedDevice._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevice.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AttachedDevice._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevice.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AttachedDevice._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'mgmtObjsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevice.xsd',
                                                 17, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AttachedDevice._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevice.xsd',
                                                 18, 12))
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


AttachedDevice._Automaton = _BuildAutomaton_16()

AttachedDevices._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'attachedDeviceCollection'),
    NamedReferenceCollection, scope=AttachedDevices,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevices.xsd',
        23, 4)))

AttachedDevices._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=AttachedDevices,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

AttachedDevices._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=AttachedDevices,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

AttachedDevices._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=AttachedDevices,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

AttachedDevices._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=AttachedDevices,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))

AttachedDevices._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'mgmtObjsReference'),
    pyxb.binding.datatypes.anyURI, scope=AttachedDevices,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 84,
        4)))


def _BuildAutomaton_17():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevices.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevices.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevices.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevices.xsd',
                                    17, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevices.xsd',
                                    18, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevices.xsd',
                                    19, 12))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AttachedDevices._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevices.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AttachedDevices._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevices.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AttachedDevices._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevices.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AttachedDevices._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'attachedDeviceCollection')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevices.xsd',
                                                 17, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AttachedDevices._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevices.xsd',
                                                 18, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AttachedDevices._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'mgmtObjsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/attachedDevices.xsd',
                                                 19, 12))
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


AttachedDevices._Automaton = _BuildAutomaton_17()

BootstrapParamSet._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclIdList'), AnyURIList,
    scope=BootstrapParamSet, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/bootstrapParamSet.xsd',
        23, 4)))

BootstrapParamSet._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sclId'),
                               pyxb.binding.datatypes.anyURI,
                               scope=BootstrapParamSet,
                               location=pyxb.utils.utility.Location(
                                   u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                   220, 4)))

BootstrapParamSet._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'securityM2MNodeId'), STD_ANON_,
    scope=BootstrapParamSet, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        6, 4)))

BootstrapParamSet._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'securityKmrIndex'),
    pyxb.binding.datatypes.unsignedInt, scope=BootstrapParamSet,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        14, 4)))

BootstrapParamSet._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'securityLifetime'),
    pyxb.binding.datatypes.dateTime, scope=BootstrapParamSet,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        16, 4)))

BootstrapParamSet._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'securityMasFqdn'),
    pyxb.binding.datatypes.anyURI, scope=BootstrapParamSet,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        18, 4)))

BootstrapParamSet._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'securityEncryptedM2MKey'),
    STD_ANON_2, scope=BootstrapParamSet, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        20, 4)))


def _BuildAutomaton_18():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/bootstrapParamSet.xsd',
                                    16, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/bootstrapParamSet.xsd',
                                    17, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/bootstrapParamSet.xsd',
                                    18, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/bootstrapParamSet.xsd',
                                    19, 12))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BootstrapParamSet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'securityM2MNodeId')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/bootstrapParamSet.xsd',
                                                 13, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BootstrapParamSet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'securityKmrIndex')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/bootstrapParamSet.xsd',
                                                 14, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BootstrapParamSet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'securityLifetime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/bootstrapParamSet.xsd',
                                                 15, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BootstrapParamSet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'securityMasFqdn')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/bootstrapParamSet.xsd',
                                                 16, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BootstrapParamSet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'securityEncryptedM2MKey')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/bootstrapParamSet.xsd',
                                                 17, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BootstrapParamSet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'sclId')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/bootstrapParamSet.xsd',
                                                 18, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(BootstrapParamSet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'sclIdList')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/bootstrapParamSet.xsd',
                                                 19, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True)]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


BootstrapParamSet._Automaton = _BuildAutomaton_18()

SearchStrings._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'searchString'),
    pyxb.binding.datatypes.string, scope=SearchStrings,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 28,
        4)))


def _BuildAutomaton_19():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                    22, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SearchStrings._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchString')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                                 22, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


SearchStrings._Automaton = _BuildAutomaton_19()

FilterCriteriaType._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'ifModifiedSince'),
    pyxb.binding.datatypes.dateTime, scope=FilterCriteriaType,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 34,
        12)))

FilterCriteriaType._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'ifUnmodifiedSince'),
    pyxb.binding.datatypes.dateTime, scope=FilterCriteriaType,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 36,
        12)))

FilterCriteriaType._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'ifNoneMatch'),
    pyxb.binding.datatypes.string, scope=FilterCriteriaType,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 38,
        12)))

FilterCriteriaType._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'attributeAccessor'),
    pyxb.binding.datatypes.anyURI, scope=FilterCriteriaType,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 40,
        12)))

FilterCriteriaType._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'searchString'),
    pyxb.binding.datatypes.string, scope=FilterCriteriaType,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 41,
        12)))

FilterCriteriaType._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'createdAfter'),
    pyxb.binding.datatypes.dateTime, scope=FilterCriteriaType,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 43,
        12)))

FilterCriteriaType._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'createdBefore'),
    pyxb.binding.datatypes.dateTime, scope=FilterCriteriaType,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 45,
        12)))


def _BuildAutomaton_20():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
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
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FilterCriteriaType._UseForTag(
        pyxb.namespace.ExpandedName(None, u'ifModifiedSince')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                                 34, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FilterCriteriaType._UseForTag(
        pyxb.namespace.ExpandedName(None, u'ifUnmodifiedSince')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                                 36, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FilterCriteriaType._UseForTag(
        pyxb.namespace.ExpandedName(None, u'ifNoneMatch')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                                 38, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FilterCriteriaType._UseForTag(
        pyxb.namespace.ExpandedName(None, u'attributeAccessor')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                                 40, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(FilterCriteriaType._UseForTag(
        pyxb.namespace.ExpandedName(None, u'searchString')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                                 41, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(FilterCriteriaType._UseForTag(
        pyxb.namespace.ExpandedName(None, u'createdAfter')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                                 43, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(FilterCriteriaType._UseForTag(
        pyxb.namespace.ExpandedName(None, u'createdBefore')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                                 45, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


FilterCriteriaType._Automaton = _BuildAutomaton_20()

AnyURIList._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reference'),
                               pyxb.binding.datatypes.anyURI, scope=AnyURIList,
                               location=pyxb.utils.utility.Location(
                                   u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                   53, 12)))


def _BuildAutomaton_21():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                    53, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        AnyURIList._UseForTag(pyxb.namespace.ExpandedName(None, u'reference')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            53, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


AnyURIList._Automaton = _BuildAutomaton_21()

AnnounceTo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'activated'),
    pyxb.binding.datatypes.boolean, scope=AnnounceTo,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 68,
        4)))

AnnounceTo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'sclList'), AnyURIList,
    scope=AnnounceTo, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 69,
        4)))

AnnounceTo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'global'),
    pyxb.binding.datatypes.boolean, scope=AnnounceTo,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 70,
        4)))


def _BuildAutomaton_22():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                    62, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                    64, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AnnounceTo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'activated')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                                 62, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AnnounceTo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'sclList')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                                 63, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AnnounceTo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'global')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                                 64, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True)]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


AnnounceTo._Automaton = _BuildAutomaton_22()

NamedReferenceCollection._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'namedReference'),
    ReferenceToNamedResource, scope=NamedReferenceCollection,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 104,
        4)))


def _BuildAutomaton_23():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                    91, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        NamedReferenceCollection._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, u'namedReference')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
            91, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


NamedReferenceCollection._Automaton = _BuildAutomaton_23()

Schedule._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'scheduleString'), ScheduleString,
    scope=Schedule, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 115,
        4)))


def _BuildAutomaton_24():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                    110, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'scheduleString')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                                 110, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Schedule._Automaton = _BuildAutomaton_24()

TrpdtType._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'tolerableDelay'),
    pyxb.binding.datatypes.duration, scope=TrpdtType,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 179,
        12)))

TrpdtType._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'tolerableTime'),
    pyxb.binding.datatypes.time, scope=TrpdtType,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 181,
        12)))


def _BuildAutomaton_25():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                    179, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                    181, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TrpdtType._UseForTag(
        pyxb.namespace.ExpandedName(None, u'tolerableDelay')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                                 179, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TrpdtType._UseForTag(
        pyxb.namespace.ExpandedName(None, u'tolerableTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                                 181, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


TrpdtType._Automaton = _BuildAutomaton_25()

ActionStatus._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'action'),
                               pyxb.binding.datatypes.anyURI,
                               scope=ActionStatus,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
                                   26, 12)))

ActionStatus._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'progress'),
                               STD_ANON, scope=ActionStatus,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
                                   27, 12)))

ActionStatus._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'finalStatus'), FinalStatus,
    scope=ActionStatus, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 35,
        12)))


def _BuildAutomaton_26():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        ActionStatus._UseForTag(pyxb.namespace.ExpandedName(None, u'action')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
            26, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        ActionStatus._UseForTag(pyxb.namespace.ExpandedName(None, u'progress')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
            27, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ActionStatus._UseForTag(
        pyxb.namespace.ExpandedName(None, u'finalStatus')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
                                                 35, 12))
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


ActionStatus._Automaton = _BuildAutomaton_26()

AreaNwkTypeInfoSet._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'areaNwkTypeItem'),
    NameValuePairItem, scope=AreaNwkTypeInfoSet,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 72,
        4)))


def _BuildAutomaton_27():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
                                    67, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AreaNwkTypeInfoSet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'areaNwkTypeItem')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
                                                 67, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


AreaNwkTypeInfoSet._Automaton = _BuildAutomaton_27()

NameValuePairItem._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'),
                               pyxb.binding.datatypes.string,
                               scope=NameValuePairItem,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
                                   81, 4)))

NameValuePairItem._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'value'),
                               pyxb.binding.datatypes.string,
                               scope=NameValuePairItem,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
                                   83, 4)))


def _BuildAutomaton_28():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(NameValuePairItem._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'name')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
                                                 76, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(NameValuePairItem._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'value')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
                                                 77, 12))
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


NameValuePairItem._Automaton = _BuildAutomaton_28()

CommunicationChannel._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=CommunicationChannel,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

CommunicationChannel._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=CommunicationChannel,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

CommunicationChannel._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contactURI'),
    pyxb.binding.datatypes.anyURI, scope=CommunicationChannel,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 136,
        4)))

CommunicationChannel._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'channelType'), ChannelType,
    scope=CommunicationChannel, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 138,
        4)))

CommunicationChannel._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'channelData'), ChannelData,
    scope=CommunicationChannel, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 146,
        4)))


def _BuildAutomaton_29():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannel.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannel.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannel.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannel.xsd',
                                    15, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannel.xsd',
                                    16, 12))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CommunicationChannel._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'channelType')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannel.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CommunicationChannel._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contactURI')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannel.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CommunicationChannel._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'channelData')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannel.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CommunicationChannel._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannel.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CommunicationChannel._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannel.xsd',
                                                 16, 12))
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


CommunicationChannel._Automaton = _BuildAutomaton_29()

CommunicationChannels._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=CommunicationChannels,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

CommunicationChannels._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=CommunicationChannels,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

CommunicationChannels._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'communicationChannelCollection'),
    NamedReferenceCollection, scope=CommunicationChannels,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannels.xsd',
        19, 4)))


def _BuildAutomaton_30():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannels.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannels.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannels.xsd',
                                    15, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CommunicationChannels._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannels.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CommunicationChannels._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannels.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CommunicationChannels._UseForTag(
        pyxb.namespace.ExpandedName(Namespace,
                                    u'communicationChannelCollection')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/communicationChannels.xsd',
                                                 15, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


CommunicationChannels._Automaton = _BuildAutomaton_30()

ConnectionParamSet._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sclId'),
                               pyxb.binding.datatypes.anyURI,
                               scope=ConnectionParamSet,
                               location=pyxb.utils.utility.Location(
                                   u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                   220, 4)))

ConnectionParamSet._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'securityLifetime'),
    pyxb.binding.datatypes.dateTime, scope=ConnectionParamSet,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        16, 4)))

ConnectionParamSet._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'securityEncryptedM2MKey'),
    STD_ANON_2, scope=ConnectionParamSet, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        20, 4)))

ConnectionParamSet._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'securityKmcIndex'),
    pyxb.binding.datatypes.unsignedInt, scope=ConnectionParamSet,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        30, 4)))

ConnectionParamSet._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'securitymIdFlags'), STD_ANON_3,
    scope=ConnectionParamSet, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        32, 4)))

ConnectionParamSet._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'securityConnectionId'),
    pyxb.binding.datatypes.unsignedLong, scope=ConnectionParamSet,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonSecurity.xsd',
        48, 4)))


def _BuildAutomaton_31():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConnectionParamSet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'securityConnectionId')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/connectionParamSet.xsd',
                                                 13, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConnectionParamSet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'securityKmcIndex')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/connectionParamSet.xsd',
                                                 14, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConnectionParamSet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'securityLifetime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/connectionParamSet.xsd',
                                                 15, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConnectionParamSet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'securityEncryptedM2MKey')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/connectionParamSet.xsd',
                                                 16, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConnectionParamSet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'sclId')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/connectionParamSet.xsd',
                                                 17, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ConnectionParamSet._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'securitymIdFlags')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/connectionParamSet.xsd',
                                                 18, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
    ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
    ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


ConnectionParamSet._Automaton = _BuildAutomaton_31()

Container._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=Container,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

Container._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=Container,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

Container._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=Container,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

Container._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
    pyxb.binding.datatypes.dateTime, scope=Container,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 16,
        4)))

Container._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'searchStrings'), SearchStrings,
    scope=Container, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 18,
        4)))

Container._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'announceTo'), AnnounceTo,
    scope=Container, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 58,
        4)))

Container._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=Container,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))

Container._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contentInstancesReference'),
    pyxb.binding.datatypes.anyURI, scope=Container,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 86,
        4)))

Container._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subcontainersReference'),
    pyxb.binding.datatypes.anyURI, scope=Container,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 87,
        4)))

Container._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'maxNrOfInstances'),
    pyxb.binding.datatypes.long, scope=Container,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd', 30,
        4)))

Container._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'maxByteSize'),
    pyxb.binding.datatypes.long, scope=Container,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd', 31,
        4)))

Container._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'maxInstanceAge'),
    pyxb.binding.datatypes.duration, scope=Container,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd', 32,
        4)))


def _BuildAutomaton_32():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
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
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Container._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Container._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Container._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Container._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Container._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Container._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'announceTo')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 17, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Container._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'maxNrOfInstances')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 18, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Container._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'maxByteSize')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 19, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Container._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'maxInstanceAge')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 20, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Container._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contentInstancesReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 23, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Container._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subcontainersReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
                                                 24, 12))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Container._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/container.xsd',
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


Container._Automaton = _BuildAutomaton_32()

ContainerAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=ContainerAnnc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

ContainerAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
    pyxb.binding.datatypes.dateTime, scope=ContainerAnnc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 16,
        4)))

ContainerAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'searchStrings'), SearchStrings,
    scope=ContainerAnnc, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 18,
        4)))

ContainerAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'announceTo'), AnnounceTo,
    scope=ContainerAnnc, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 58,
        4)))

ContainerAnnc._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'link'),
                               pyxb.binding.datatypes.anyURI,
                               scope=ContainerAnnc,
                               location=pyxb.utils.utility.Location(
                                   u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                   74, 4)))


def _BuildAutomaton_33():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containerAnnc.xsd',
                                    13, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containerAnnc.xsd',
                                    14, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containerAnnc.xsd',
                                    15, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containerAnnc.xsd',
                                    16, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ContainerAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'link')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containerAnnc.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ContainerAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containerAnnc.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ContainerAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containerAnnc.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ContainerAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containerAnnc.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ContainerAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'announceTo')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containerAnnc.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True)]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


ContainerAnnc._Automaton = _BuildAutomaton_33()

Containers._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=Containers,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

Containers._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=Containers,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

Containers._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=Containers,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

Containers._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=Containers,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))

Containers._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'containerCollection'),
    NamedReferenceCollection, scope=Containers,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd', 24,
        4)))

Containers._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'containerAnncCollection'),
    NamedReferenceCollection, scope=Containers,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd', 25,
        4)))

Containers._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'locationContainerCollection'),
    NamedReferenceCollection, scope=Containers,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd', 27,
        4)))

Containers._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'locationContainerAnncCollection'),
    NamedReferenceCollection, scope=Containers,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd', 29,
        4)))


def _BuildAutomaton_34():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd',
                                    16, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd',
                                    18, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd',
                                    19, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd',
                                    20, 12))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Containers._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Containers._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Containers._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Containers._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'containerCollection')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd',
                                                 16, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Containers._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'containerAnncCollection')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd',
                                                 17, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Containers._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'locationContainerCollection')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd',
                                                 18, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Containers._UseForTag(
        pyxb.namespace.ExpandedName(Namespace,
                                    u'locationContainerAnncCollection')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd',
                                                 19, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Containers._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/containers.xsd',
                                                 20, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
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
    transitions.append(fac.Transition(st_7, [
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Containers._Automaton = _BuildAutomaton_34()

ContentInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=ContentInstance,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

ContentInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=ContentInstance,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

ContentInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'searchStrings'), SearchStrings,
    scope=ContentInstance, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 18,
        4)))

ContentInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'delayTolerance'),
    pyxb.binding.datatypes.dateTime, scope=ContentInstance,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 72,
        4)))

ContentInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'content'), Content,
    scope=ContentInstance, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
        28, 4)))

ContentInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contentSize'),
    pyxb.binding.datatypes.long, scope=ContentInstance,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
        40, 4)))

ContentInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contentTypes'), ContentTypes,
    scope=ContentInstance, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
        41, 4)))


def _BuildAutomaton_35():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
                                    16, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
                                    17, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
                                    18, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
                                    19, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
                                    20, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
                                    21, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
                                    22, 12))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ContentInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
                                                 16, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ContentInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
                                                 17, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ContentInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'delayTolerance')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
                                                 18, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ContentInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
                                                 19, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ContentInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contentTypes')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
                                                 20, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ContentInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contentSize')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
                                                 21, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(ContentInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'content')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
                                                 22, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


ContentInstance._Automaton = _BuildAutomaton_35()

ContentTypes._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contentType'),
    pyxb.binding.datatypes.string, scope=ContentTypes,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 106,
        4)))


def _BuildAutomaton_36():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ContentTypes._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contentType')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
                                                 45, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
    ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


ContentTypes._Automaton = _BuildAutomaton_36()

ContentInstances._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=ContentInstances,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

ContentInstances._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=ContentInstances,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

ContentInstances._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=ContentInstances,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))

ContentInstances._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'currentNrOfInstances'),
    pyxb.binding.datatypes.long, scope=ContentInstances,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
        25, 4)))

ContentInstances._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'currentByteSize'),
    pyxb.binding.datatypes.long, scope=ContentInstances,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
        26, 4)))

ContentInstances._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'latest'), ReferenceToNamedResource,
    scope=ContentInstances, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
        28, 4)))

ContentInstances._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'oldest'), ReferenceToNamedResource,
    scope=ContentInstances, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
        29, 4)))

ContentInstances._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contentInstanceCollection'),
    ContentInstanceCollection, scope=ContentInstances,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
        31, 4)))


def _BuildAutomaton_37():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                    13, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                    14, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                    15, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                    16, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                    18, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                    19, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                    20, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                    21, 12))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ContentInstances._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                                 13, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ContentInstances._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                                 14, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ContentInstances._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'currentNrOfInstances')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                                 15, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ContentInstances._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'currentByteSize')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                                 16, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ContentInstances._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contentInstanceCollection')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                                 18, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ContentInstances._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'latest')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                                 19, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(ContentInstances._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'oldest')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                                 20, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(ContentInstances._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                                 21, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
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
    transitions.append(fac.Transition(st_7, [
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


ContentInstances._Automaton = _BuildAutomaton_37()

ContentInstanceCollection._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contentInstance'), ContentInstance,
    scope=ContentInstanceCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstance.xsd',
        12, 4)))


def _BuildAutomaton_38():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
                                    36, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        ContentInstanceCollection._UseForTag(
            pyxb.namespace.ExpandedName(Namespace, u'contentInstance')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/contentInstances.xsd',
            36, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


ContentInstanceCollection._Automaton = _BuildAutomaton_38()

Discovery._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'matchSize'),
    pyxb.binding.datatypes.long, scope=Discovery,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/discovery.xsd', 15,
        4)))

Discovery._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'truncated'),
    pyxb.binding.datatypes.boolean, scope=Discovery,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/discovery.xsd', 16,
        4)))

Discovery._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'discoveryURI'), AnyURIList,
    scope=Discovery, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/discovery.xsd', 17,
        4)))


def _BuildAutomaton_39():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/discovery.xsd',
                                    10, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/discovery.xsd',
                                    11, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/discovery.xsd',
                                    12, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Discovery._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'matchSize')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/discovery.xsd',
                                                 10, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Discovery._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'truncated')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/discovery.xsd',
                                                 11, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Discovery._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'discoveryURI')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/discovery.xsd',
                                                 12, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Discovery._Automaton = _BuildAutomaton_39()

ErrorInfo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'statusCode'), StatusCode,
    scope=ErrorInfo, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 186,
        4)))

ErrorInfo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'additionalInfo'),
    pyxb.binding.datatypes.string, scope=ErrorInfo,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/errorInfo.xsd', 17,
        4)))


def _BuildAutomaton_40():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/errorInfo.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/errorInfo.xsd',
                                    13, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ErrorInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'statusCode')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/errorInfo.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ErrorInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'additionalInfo')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/errorInfo.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


ErrorInfo._Automaton = _BuildAutomaton_40()


def _BuildAutomaton_41():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(
        process_contents=pyxb.binding.content.Wildcard.PC_lax,
        namespace_constraint=pyxb.binding.content.Wildcard.NC_any),
                                              pyxb.utils.utility.Location(
                                                  '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiPerformanceLog.xsd',
                                                  35, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


LogDataFile._Automaton = _BuildAutomaton_41()

RankedAnList._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessNetwork'),
    pyxb.binding.datatypes.token, scope=RankedAnList,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
        37, 4)))


def _BuildAutomaton_42():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RankedAnList._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessNetwork')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiRcatParamList.xsd',
                                                 32, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
    ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


RankedAnList._Automaton = _BuildAutomaton_42()

OccuredEvents._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'currentIndex'), trapEventIndex,
    scope=OccuredEvents,
    documentation=u'Indicates the rank of the last occured event\n                        in the table of timeStamps.\n                    ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
        35, 12)))

OccuredEvents._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'trapEventTimeStamp'),
    pyxb.binding.datatypes.dateTime, scope=OccuredEvents,
    documentation=u'It is a circular buffer of timeStamps of the\n                        last occured events. The number of logged events is\n                        limited to 100.\n                    ',
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
        42, 12)))


def _BuildAutomaton_43():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=100L,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
                                    42, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OccuredEvents._UseForTag(
        pyxb.namespace.ExpandedName(None, u'currentIndex')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
                                                 35, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OccuredEvents._UseForTag(
        pyxb.namespace.ExpandedName(None, u'trapEventTimeStamp')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/etsiTrapInstance.xsd',
                                                 42, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


OccuredEvents._Automaton = _BuildAutomaton_43()

ExecInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=ExecInstance,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

ExecInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=ExecInstance,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

ExecInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=ExecInstance,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

ExecInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
    pyxb.binding.datatypes.dateTime, scope=ExecInstance,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 16,
        4)))

ExecInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=ExecInstance,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))

ExecInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'execStatus'), ExecStatus,
    scope=ExecInstance, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
        29, 4)))

ExecInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'execDisable'),
    pyxb.binding.datatypes.anyURI, scope=ExecInstance,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
        30, 4)))

ExecInstance._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'execResult'), ExecResultList,
    scope=ExecInstance, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
        42, 4)))


def _BuildAutomaton_44():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
                                    13, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
                                    14, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
                                    15, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
                                    16, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
                                    19, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
                                    20, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
                                    21, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
                                    24, 12))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ExecInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
                                                 13, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ExecInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
                                                 14, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ExecInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
                                                 15, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ExecInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
                                                 16, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ExecInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'execStatus')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
                                                 19, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ExecInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'execResult')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
                                                 20, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(ExecInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'execDisable')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
                                                 21, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(ExecInstance._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
                                                 24, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
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
    transitions.append(fac.Transition(st_7, [
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


ExecInstance._Automaton = _BuildAutomaton_44()

ExecResultList._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'execResultItem'), ExecResultItem,
    scope=ExecResultList, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
        45, 12)))


def _BuildAutomaton_45():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
                                    45, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ExecResultList._UseForTag(
        pyxb.namespace.ExpandedName(None, u'execResultItem')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
                                                 45, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


ExecResultList._Automaton = _BuildAutomaton_45()

ExecResultItem._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'),
                               pyxb.binding.datatypes.string,
                               scope=ExecResultItem,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
                                   52, 12)))

ExecResultItem._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'value'),
                               pyxb.binding.datatypes.anyType,
                               scope=ExecResultItem,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
                                   53, 12)))


def _BuildAutomaton_46():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        ExecResultItem._UseForTag(pyxb.namespace.ExpandedName(None, u'name')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
            52, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        ExecResultItem._UseForTag(pyxb.namespace.ExpandedName(None, u'value')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstance.xsd',
            53, 12))
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


ExecResultItem._Automaton = _BuildAutomaton_46()

ExecInstances._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=ExecInstances,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

ExecInstances._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=ExecInstances,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

ExecInstances._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=ExecInstances,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))

ExecInstances._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'execInstanceCollection'),
    NamedReferenceCollection, scope=ExecInstances,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstances.xsd',
        24, 4)))


def _BuildAutomaton_47():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstances.xsd',
                                    14, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstances.xsd',
                                    15, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstances.xsd',
                                    18, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstances.xsd',
                                    19, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ExecInstances._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstances.xsd',
                                                 14, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ExecInstances._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstances.xsd',
                                                 15, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ExecInstances._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'execInstanceCollection')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstances.xsd',
                                                 18, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ExecInstances._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/execInstances.xsd',
                                                 19, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
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
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


ExecInstances._Automaton = _BuildAutomaton_47()

Group._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=Group,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

Group._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=Group,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

Group._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=Group,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

Group._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
    pyxb.binding.datatypes.dateTime, scope=Group,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 16,
        4)))

Group._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'searchStrings'), SearchStrings,
    scope=Group, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 18,
        4)))

Group._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'announceTo'), AnnounceTo,
    scope=Group, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 58,
        4)))

Group._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=Group,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))

Group._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'membersContentAccessRightID'),
    pyxb.binding.datatypes.anyURI, scope=Group,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 14,
        4)))

Group._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'memberType'), MemberType,
    scope=Group, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 38,
        4)))

Group._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'currentNrOfMembers'),
    pyxb.binding.datatypes.long, scope=Group,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 39,
        4)))

Group._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'maxNrOfMembers'),
    pyxb.binding.datatypes.long, scope=Group,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 40,
        4)))

Group._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'members'), AnyURIList, scope=Group,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 41,
        4)))

Group._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'memberTypeValidated'),
    pyxb.binding.datatypes.boolean, scope=Group,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 42,
        4)))

Group._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'consistencyStrategy'),
    ConsistencyStrategy, scope=Group, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 43,
        4)))

Group._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'membersContentReference'),
    pyxb.binding.datatypes.anyURI, scope=Group,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 45,
        4)))


def _BuildAutomaton_48():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                    18, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                    19, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                    20, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                    21, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                    22, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                    23, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                    24, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                    25, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                    26, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                    27, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                     28, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                     29, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                     30, 12))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                     32, 12))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                     33, 12))
    counters.add(cc_14)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Group._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                                 18, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Group._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                                 19, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Group._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                                 20, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Group._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                                 21, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Group._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                                 22, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(
        Group._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'announceTo')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 23,
            12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(
        Group._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'memberType')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 24,
            12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Group._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'currentNrOfMembers')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                                 25, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Group._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'maxNrOfMembers')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                                 26, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(
        Group._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'members')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd', 27,
            12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Group._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'membersContentAccessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                                 28, 12))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Group._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'memberTypeValidated')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                                 29, 12))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(Group._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'consistencyStrategy')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                                 30, 12))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(Group._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'membersContentReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                                 32, 12))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(Group._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/group.xsd',
                                                 33, 12))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update,
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
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False)]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False)]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True)]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Group._Automaton = _BuildAutomaton_48()

GroupAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=GroupAnnc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

GroupAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
    pyxb.binding.datatypes.dateTime, scope=GroupAnnc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 16,
        4)))

GroupAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'searchStrings'), SearchStrings,
    scope=GroupAnnc, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 18,
        4)))

GroupAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'announceTo'), AnnounceTo,
    scope=GroupAnnc, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 58,
        4)))

GroupAnnc._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'link'),
                               pyxb.binding.datatypes.anyURI, scope=GroupAnnc,
                               location=pyxb.utils.utility.Location(
                                   u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                   74, 4)))


def _BuildAutomaton_49():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groupAnnc.xsd',
                                    13, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groupAnnc.xsd',
                                    14, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groupAnnc.xsd',
                                    15, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groupAnnc.xsd',
                                    16, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        GroupAnnc._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'link')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groupAnnc.xsd',
            12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GroupAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groupAnnc.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GroupAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groupAnnc.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(GroupAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groupAnnc.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(GroupAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'announceTo')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groupAnnc.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True)]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


GroupAnnc._Automaton = _BuildAutomaton_49()

Groups._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=Groups,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

Groups._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=Groups,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

Groups._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=Groups,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

Groups._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=Groups,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))

Groups._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'groupCollection'),
    NamedReferenceCollection, scope=Groups,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groups.xsd', 22,
        4)))

Groups._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'groupAnncCollection'),
    NamedReferenceCollection, scope=Groups,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groups.xsd', 23,
        4)))


def _BuildAutomaton_50():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groups.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groups.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groups.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groups.xsd',
                                    16, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groups.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groups.xsd',
                                    18, 12))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Groups._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groups.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Groups._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groups.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Groups._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groups.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Groups._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'groupCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groups.xsd',
                                                 16, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Groups._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'groupAnncCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groups.xsd',
                                                 17, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Groups._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/groups.xsd',
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


Groups._Automaton = _BuildAutomaton_50()

LocationContainerAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=LocationContainerAnnc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

LocationContainerAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
    pyxb.binding.datatypes.dateTime, scope=LocationContainerAnnc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 16,
        4)))

LocationContainerAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'searchStrings'), SearchStrings,
    scope=LocationContainerAnnc, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 18,
        4)))

LocationContainerAnnc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'announceTo'), AnnounceTo,
    scope=LocationContainerAnnc, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 58,
        4)))

LocationContainerAnnc._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'link'),
                               pyxb.binding.datatypes.anyURI,
                               scope=LocationContainerAnnc,
                               location=pyxb.utils.utility.Location(
                                   u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd',
                                   74, 4)))


def _BuildAutomaton_51():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/locationContainerAnnc.xsd',
                                    13, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/locationContainerAnnc.xsd',
                                    14, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/locationContainerAnnc.xsd',
                                    15, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/locationContainerAnnc.xsd',
                                    16, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LocationContainerAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'link')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/locationContainerAnnc.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LocationContainerAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/locationContainerAnnc.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(LocationContainerAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/locationContainerAnnc.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(LocationContainerAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/locationContainerAnnc.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(LocationContainerAnnc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'announceTo')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/locationContainerAnnc.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True)]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


LocationContainerAnnc._Automaton = _BuildAutomaton_51()

M2MPoc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=M2MPoc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

M2MPoc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=M2MPoc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

M2MPoc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
    pyxb.binding.datatypes.dateTime, scope=M2MPoc,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 16,
        4)))

M2MPoc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'onlineStatus'), OnlineStatus,
    scope=M2MPoc, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 126,
        4)))

M2MPoc._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contactInfo'), ContactInfo,
    scope=M2MPoc, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd', 23,
        4)))


def _BuildAutomaton_52():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd',
                                    15, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd',
                                    16, 12))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(M2MPoc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contactInfo')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(M2MPoc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(M2MPoc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'onlineStatus')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(M2MPoc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(M2MPoc._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd',
                                                 16, 12))
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


M2MPoc._Automaton = _BuildAutomaton_52()

ContactInfo._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contactURI'),
    pyxb.binding.datatypes.anyURI, scope=ContactInfo,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 136,
        4)))

ContactInfo._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'other'),
                               pyxb.binding.datatypes.anyType,
                               scope=ContactInfo,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd',
                                   32, 4)))


def _BuildAutomaton_53():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ContactInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contactURI')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd',
                                                 26, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ContactInfo._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'other')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPoc.xsd',
                                                 27, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


ContactInfo._Automaton = _BuildAutomaton_53()

M2MPocs._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=M2MPocs,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

M2MPocs._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=M2MPocs,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

M2MPocs._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'm2mPocCollection'),
    NamedReferenceCollection, scope=M2MPocs,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPocs.xsd', 19,
        4)))


def _BuildAutomaton_54():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPocs.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPocs.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPocs.xsd',
                                    15, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(M2MPocs._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPocs.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(M2MPocs._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPocs.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(M2MPocs._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'm2mPocCollection')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/m2mPocs.xsd',
                                                 15, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


M2MPocs._Automaton = _BuildAutomaton_54()

CTD_ANON_._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'status'),
                               CTD_ANON_2, scope=CTD_ANON_,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
                                   15, 16)))


def _BuildAutomaton_55():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
                                    15, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'status')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
            15, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_._Automaton = _BuildAutomaton_55()

CTD_ANON_2._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'statusCode'),
                               pyxb.binding.datatypes.string, scope=CTD_ANON_2,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
                                   18, 28)))

CTD_ANON_2._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'eTag'),
                               pyxb.binding.datatypes.string, scope=CTD_ANON_2,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
                                   19, 28)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'resourceURI'),
    pyxb.binding.datatypes.anyURI, scope=CTD_ANON_2,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
        20, 28)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=CTD_ANON_2,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
        21, 28)))

CTD_ANON_2._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'resultBody'),
                               _ImportedBinding__xmlmime.base64Binary,
                               scope=CTD_ANON_2,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
                                   23, 28)))


def _BuildAutomaton_56():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
                                    19, 28))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
                                    21, 28))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
                                    23, 28))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'statusCode')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
            18, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'eTag')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
            19, 28))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(
        pyxb.namespace.ExpandedName(None, u'resourceURI')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
                                                 20, 28))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(
        pyxb.namespace.ExpandedName(None, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
                                                 21, 28))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'resultBody')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/membersContent.xsd',
            23, 28))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    transitions.append(fac.Transition(st_2, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True)]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CTD_ANON_2._Automaton = _BuildAutomaton_56()

MgmtCmd._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=MgmtCmd,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

MgmtCmd._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=MgmtCmd,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

MgmtCmd._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=MgmtCmd,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

MgmtCmd._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
    pyxb.binding.datatypes.dateTime, scope=MgmtCmd,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 16,
        4)))

MgmtCmd._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'searchStrings'), SearchStrings,
    scope=MgmtCmd, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 18,
        4)))

MgmtCmd._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=MgmtCmd,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))

MgmtCmd._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'description'),
    pyxb.binding.datatypes.string, scope=MgmtCmd,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 12,
        4)))

MgmtCmd._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'cmdType'), CmdType, scope=MgmtCmd,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd', 34,
        4)))

MgmtCmd._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'execEnable'),
    pyxb.binding.datatypes.anyURI, scope=MgmtCmd,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd', 47,
        4)))

MgmtCmd._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'execReqArgs'), ExecReqArgsList,
    scope=MgmtCmd, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd', 49,
        4)))

MgmtCmd._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'execInstancesReference'),
    pyxb.binding.datatypes.anyURI, scope=MgmtCmd,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd', 64,
        4)))


def _BuildAutomaton_57():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                    13, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                    14, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                    15, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                    16, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                    17, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                    20, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                    21, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                    22, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                    23, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                    26, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                     27, 12))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MgmtCmd._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                                 13, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MgmtCmd._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                                 14, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MgmtCmd._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                                 15, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MgmtCmd._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                                 16, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(MgmtCmd._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                                 17, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(MgmtCmd._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'description')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                                 20, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(
        MgmtCmd._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cmdType')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
            21, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(MgmtCmd._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'execEnable')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                                 22, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(MgmtCmd._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'execReqArgs')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                                 23, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(MgmtCmd._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'execInstancesReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                                 26, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(MgmtCmd._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                                 27, 12))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update,
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
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True)]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


MgmtCmd._Automaton = _BuildAutomaton_57()

ExecReqArgsList._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'execReqArg'),
                               ExecReqArg, scope=ExecReqArgsList,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                   52, 12)))


def _BuildAutomaton_58():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                    52, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ExecReqArgsList._UseForTag(
        pyxb.namespace.ExpandedName(None, u'execReqArg')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                                 52, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


ExecReqArgsList._Automaton = _BuildAutomaton_58()

ExecReqArg._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'),
                               pyxb.binding.datatypes.string, scope=ExecReqArg,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                   59, 12)))

ExecReqArg._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'value'),
                               pyxb.binding.datatypes.anyType, scope=ExecReqArg,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
                                   60, 12)))


def _BuildAutomaton_59():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        ExecReqArg._UseForTag(pyxb.namespace.ExpandedName(None, u'name')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
            59, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        ExecReqArg._UseForTag(pyxb.namespace.ExpandedName(None, u'value')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtCmd.xsd',
            60, 12))
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


ExecReqArg._Automaton = _BuildAutomaton_59()

MgmtObj._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=MgmtObj,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

MgmtObj._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=MgmtObj,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

MgmtObj._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=MgmtObj,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

MgmtObj._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'expirationTime'),
    pyxb.binding.datatypes.dateTime, scope=MgmtObj,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 16,
        4)))

MgmtObj._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'searchStrings'), SearchStrings,
    scope=MgmtObj, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 18,
        4)))

MgmtObj._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=MgmtObj,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))

MgmtObj._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contentType'),
    pyxb.binding.datatypes.string, scope=MgmtObj,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 106,
        4)))

MgmtObj._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'moID'),
                               pyxb.binding.datatypes.string, scope=MgmtObj,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd',
                                   8, 4)))

MgmtObj._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'originalMO'),
    pyxb.binding.datatypes.string, scope=MgmtObj,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 10,
        4)))

MgmtObj._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'description'),
    pyxb.binding.datatypes.string, scope=MgmtObj,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 12,
        4)))

MgmtObj._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'parametersCollection'),
    NamedReferenceCollection, scope=MgmtObj,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 14,
        4)))


def _BuildAutomaton_60():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
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
    symbol = pyxb.binding.content.ElementUse(MgmtObj._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'expirationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MgmtObj._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MgmtObj._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'searchStrings')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MgmtObj._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MgmtObj._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        MgmtObj._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'moID')),
        pyxb.utils.utility.Location(
            u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
            17, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MgmtObj._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 18, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MgmtObj._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contentType')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 19, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MgmtObj._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'description')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 20, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MgmtObj._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObj.xsd',
                                                 22, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(MgmtObj._UseForTag(
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


MgmtObj._Automaton = _BuildAutomaton_60()

MgmtObjs._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=MgmtObjs,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

MgmtObjs._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=MgmtObjs,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

MgmtObjs._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=MgmtObjs,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

MgmtObjs._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=MgmtObjs,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))

MgmtObjs._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'mgmtObjCollection'),
    NamedReferenceCollection, scope=MgmtObjs,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObjs.xsd', 21,
        4)))

MgmtObjs._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'mgmtCmdCollection'),
    NamedReferenceCollection, scope=MgmtObjs,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObjs.xsd', 22,
        4)))


def _BuildAutomaton_61():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObjs.xsd',
                                    10, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObjs.xsd',
                                    11, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObjs.xsd',
                                    12, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObjs.xsd',
                                    15, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObjs.xsd',
                                    16, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObjs.xsd',
                                    17, 12))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MgmtObjs._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObjs.xsd',
                                                 10, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MgmtObjs._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObjs.xsd',
                                                 11, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MgmtObjs._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObjs.xsd',
                                                 12, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(MgmtObjs._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'mgmtObjCollection')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObjs.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(MgmtObjs._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'mgmtCmdCollection')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObjs.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(MgmtObjs._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/mgmtObjs.xsd',
                                                 17, 12))
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


MgmtObjs._Automaton = _BuildAutomaton_61()

NotificationChannel._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=NotificationChannel,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

NotificationChannel._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=NotificationChannel,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

NotificationChannel._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'contactURI'),
    pyxb.binding.datatypes.anyURI, scope=NotificationChannel,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 136,
        4)))

NotificationChannel._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'channelType'), ChannelType,
    scope=NotificationChannel, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 138,
        4)))

NotificationChannel._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'channelData'), ChannelData,
    scope=NotificationChannel, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 146,
        4)))


def _BuildAutomaton_62():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannel.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannel.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannel.xsd',
                                    14, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannel.xsd',
                                    15, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannel.xsd',
                                    16, 12))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NotificationChannel._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'channelType')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannel.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NotificationChannel._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'contactURI')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannel.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(NotificationChannel._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'channelData')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannel.xsd',
                                                 14, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(NotificationChannel._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannel.xsd',
                                                 15, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(NotificationChannel._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannel.xsd',
                                                 16, 12))
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


NotificationChannel._Automaton = _BuildAutomaton_62()

NotificationChannels._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=NotificationChannels,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

NotificationChannels._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=NotificationChannels,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

NotificationChannels._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'notificationChannelCollection'),
    NamedReferenceCollection, scope=NotificationChannels,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannels.xsd',
        19, 4)))


def _BuildAutomaton_63():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannels.xsd',
                                    12, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannels.xsd',
                                    13, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannels.xsd',
                                    15, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NotificationChannels._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannels.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(NotificationChannels._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannels.xsd',
                                                 13, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(NotificationChannels._UseForTag(
        pyxb.namespace.ExpandedName(Namespace,
                                    u'notificationChannelCollection')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notificationChannels.xsd',
                                                 15, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


NotificationChannels._Automaton = _BuildAutomaton_63()

Notify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'statusCode'), StatusCode,
    scope=Notify, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 186,
        4)))

Notify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'representation'),
    _ImportedBinding__xmlmime.base64Binary, scope=Notify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd', 14,
        16)))

Notify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'timeoutReason'),
    pyxb.binding.datatypes.string, scope=Notify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd', 16,
        16)))

Notify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'subscriptionReference'),
    pyxb.binding.datatypes.anyURI, scope=Notify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd', 18,
        12)))

Notify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'requestingEntity'),
    pyxb.binding.datatypes.anyURI, scope=Notify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd', 19,
        12)))

Notify._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'contact'),
                               pyxb.binding.datatypes.anyURI, scope=Notify,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd',
                                   20, 12)))


def _BuildAutomaton_64():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd',
                                    14, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd',
                                    16, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd',
                                    19, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd',
                                    20, 12))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Notify._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'statusCode')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd',
                                                 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Notify._UseForTag(pyxb.namespace.ExpandedName(None, u'representation')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd', 14,
            16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Notify._UseForTag(pyxb.namespace.ExpandedName(None, u'timeoutReason')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd', 16,
            16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Notify._UseForTag(
        pyxb.namespace.ExpandedName(None, u'subscriptionReference')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd',
                                                 18, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Notify._UseForTag(
        pyxb.namespace.ExpandedName(None, u'requestingEntity')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd',
                                                 19, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(
        Notify._UseForTag(pyxb.namespace.ExpandedName(None, u'contact')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd', 20,
            12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
    ]))
    transitions.append(fac.Transition(st_5, [
    ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True)]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Notify._Automaton = _BuildAutomaton_64()

NotifyCollection._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'notify'), Notify,
    scope=NotifyCollection, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notify.xsd', 9, 4)))


def _BuildAutomaton_65():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_65
    del _BuildAutomaton_65
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notifyCollection.xsd',
                                    16, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NotifyCollection._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'notify')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notifyCollection.xsd',
                                                 16, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


NotifyCollection._Automaton = _BuildAutomaton_65()

CTD_ANON_3._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'status'),
                               CTD_ANON_4, scope=CTD_ANON_3,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notifyCollectionResponse.xsd',
                                   15, 16)))


def _BuildAutomaton_66():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_66
    del _BuildAutomaton_66
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notifyCollectionResponse.xsd',
                                    15, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'status')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notifyCollectionResponse.xsd',
            15, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


CTD_ANON_3._Automaton = _BuildAutomaton_66()

CTD_ANON_4._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'targetId'),
                               pyxb.binding.datatypes.anyURI, scope=CTD_ANON_4,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notifyCollectionResponse.xsd',
                                   18, 28)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'primitiveType'),
    pyxb.binding.datatypes.string, scope=CTD_ANON_4,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notifyCollectionResponse.xsd',
        19, 28)))

CTD_ANON_4._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'statusCode'),
                               pyxb.binding.datatypes.string, scope=CTD_ANON_4,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notifyCollectionResponse.xsd',
                                   20, 28)))


def _BuildAutomaton_67():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_67
    del _BuildAutomaton_67
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, u'targetId')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notifyCollectionResponse.xsd',
            18, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(
        pyxb.namespace.ExpandedName(None, u'primitiveType')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notifyCollectionResponse.xsd',
                                                 19, 28))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, u'statusCode')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/notifyCollectionResponse.xsd',
            20, 28))
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


CTD_ANON_4._Automaton = _BuildAutomaton_67()

Parameters._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'accessRightID'),
    pyxb.binding.datatypes.anyURI, scope=Parameters,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 10,
        4)))

Parameters._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'creationTime'),
    pyxb.binding.datatypes.dateTime, scope=Parameters,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 12,
        4)))

Parameters._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime'),
    pyxb.binding.datatypes.dateTime, scope=Parameters,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 14,
        4)))

Parameters._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'subscriptionsReference'),
    pyxb.binding.datatypes.anyURI, scope=Parameters,
    location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 76,
        4)))

Parameters._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'originalMO'),
    pyxb.binding.datatypes.string, scope=Parameters,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 10,
        4)))

Parameters._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'parametersCollection'),
    NamedReferenceCollection, scope=Parameters,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/commonDM.xsd', 14,
        4)))


def _BuildAutomaton_68():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_68
    del _BuildAutomaton_68
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
    symbol = pyxb.binding.content.ElementUse(Parameters._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'accessRightID')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Parameters._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'creationTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 12, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Parameters._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'lastModifiedTime')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 13, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Parameters._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'originalMO')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 14, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Parameters._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'parametersCollection')),
                                             pyxb.utils.utility.Location(
                                                 u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/parameters.xsd',
                                                 16, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Parameters._UseForTag(
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True)]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Parameters._Automaton = _BuildAutomaton_68()

RequestNotify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'requestingEntity'),
    pyxb.binding.datatypes.anyURI, scope=RequestNotify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
        14, 12)))

RequestNotify._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'targetID'),
                               pyxb.binding.datatypes.anyURI,
                               scope=RequestNotify,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                   15, 12)))

RequestNotify._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'method'),
                               MethodType, scope=RequestNotify,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                   16, 12)))

RequestNotify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'filterCriteria'), FilterCriteriaType,
    scope=RequestNotify, location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
        17, 12)))

RequestNotify._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'maxSize'),
                               pyxb.binding.datatypes.long, scope=RequestNotify,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                   19, 12)))

RequestNotify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'searchPrefix'),
    pyxb.binding.datatypes.anyURI, scope=RequestNotify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
        20, 12)))

RequestNotify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'groupRequestIdentifier'),
    pyxb.binding.datatypes.hexBinary, scope=RequestNotify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
        21, 12)))

RequestNotify._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'TRPDT'),
                               TrpdtType, scope=RequestNotify,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                   23, 12)))

RequestNotify._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'RCAT'),
                               RcatType, scope=RequestNotify,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                   24, 12)))

RequestNotify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'contentTypeHeader'),
    pyxb.binding.datatypes.string, scope=RequestNotify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
        25, 12)))

RequestNotify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'acceptHeader'),
    pyxb.binding.datatypes.string, scope=RequestNotify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
        26, 12)))

RequestNotify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'ifModifiedSinceHeader'),
    pyxb.binding.datatypes.string, scope=RequestNotify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
        27, 12)))

RequestNotify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'ifUnmodifiedSinceHeader'),
    pyxb.binding.datatypes.string, scope=RequestNotify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
        28, 12)))

RequestNotify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'ifMatchHeader'),
    pyxb.binding.datatypes.string, scope=RequestNotify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
        30, 12)))

RequestNotify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'ifNoneMatchHeader'),
    pyxb.binding.datatypes.string, scope=RequestNotify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
        31, 12)))

RequestNotify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'xEtsiContactUriHeader'),
    pyxb.binding.datatypes.string, scope=RequestNotify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
        32, 12)))

RequestNotify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'xEtsiCorrelationIDHeader'),
    pyxb.binding.datatypes.string, scope=RequestNotify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
        33, 12)))

RequestNotify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'representation'),
    _ImportedBinding__xmlmime.base64Binary, scope=RequestNotify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
        34, 12)))


def _BuildAutomaton_69():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_69
    del _BuildAutomaton_69
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                    17, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                    19, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                    20, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                    21, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                    23, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                    24, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                    25, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                    26, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                    27, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                    28, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                     30, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                     31, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1,
                                 metadata=pyxb.utils.utility.Location(
                                     '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                     34, 12))
    counters.add(cc_12)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RequestNotify._UseForTag(
        pyxb.namespace.ExpandedName(None, u'requestingEntity')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                                 14, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RequestNotify._UseForTag(
        pyxb.namespace.ExpandedName(None, u'targetID')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                                 15, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RequestNotify._UseForTag(pyxb.namespace.ExpandedName(None, u'method')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            16, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RequestNotify._UseForTag(
        pyxb.namespace.ExpandedName(None, u'filterCriteria')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                                 17, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RequestNotify._UseForTag(pyxb.namespace.ExpandedName(None, u'maxSize')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            19, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RequestNotify._UseForTag(
        pyxb.namespace.ExpandedName(None, u'searchPrefix')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                                 20, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RequestNotify._UseForTag(
        pyxb.namespace.ExpandedName(None, u'groupRequestIdentifier')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                                 21, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RequestNotify._UseForTag(pyxb.namespace.ExpandedName(None, u'TRPDT')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            23, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        RequestNotify._UseForTag(pyxb.namespace.ExpandedName(None, u'RCAT')),
        pyxb.utils.utility.Location(
            '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
            24, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RequestNotify._UseForTag(
        pyxb.namespace.ExpandedName(None, u'contentTypeHeader')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                                 25, 12))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RequestNotify._UseForTag(
        pyxb.namespace.ExpandedName(None, u'acceptHeader')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                                 26, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RequestNotify._UseForTag(
        pyxb.namespace.ExpandedName(None, u'ifModifiedSinceHeader')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                                 27, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RequestNotify._UseForTag(
        pyxb.namespace.ExpandedName(None, u'ifUnmodifiedSinceHeader')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                                 28, 12))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RequestNotify._UseForTag(
        pyxb.namespace.ExpandedName(None, u'ifMatchHeader')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                                 30, 12))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RequestNotify._UseForTag(
        pyxb.namespace.ExpandedName(None, u'ifNoneMatchHeader')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                                 31, 12))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RequestNotify._UseForTag(
        pyxb.namespace.ExpandedName(None, u'xEtsiContactUriHeader')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                                 32, 12))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RequestNotify._UseForTag(
        pyxb.namespace.ExpandedName(None, u'xEtsiCorrelationIDHeader')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                                 33, 12))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(RequestNotify._UseForTag(
        pyxb.namespace.ExpandedName(None, u'representation')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/requestNotify.xsd',
                                                 34, 12))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update,
                      is_unordered_catenation=False)
    states.append(st_17)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
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
    transitions.append(fac.Transition(st_8, [
    ]))
    transitions.append(fac.Transition(st_9, [
    ]))
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True)]))
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True)]))
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True)]))
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True)]))
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
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True)]))
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
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, True)]))
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
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, True)]))
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
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, True)]))
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
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False)]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False)]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, True)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False)]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
    ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
    ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, True)]))
    st_17._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


RequestNotify._Automaton = _BuildAutomaton_69()

ResponseNotify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, u'statusCode'), StatusCode,
    scope=ResponseNotify, location=pyxb.utils.utility.Location(
        u'/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/common.xsd', 186,
        4)))

ResponseNotify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'representation'),
    _ImportedBinding__xmlmime.base64Binary, scope=ResponseNotify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/responseNotify.xsd',
        16, 12)))

ResponseNotify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'locationHeader'),
    pyxb.binding.datatypes.string, scope=ResponseNotify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/responseNotify.xsd',
        18, 12)))

ResponseNotify._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'etagHeader'),
                               pyxb.binding.datatypes.string,
                               scope=ResponseNotify,
                               location=pyxb.utils.utility.Location(
                                   '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/responseNotify.xsd',
                                   19, 12)))

ResponseNotify._AddElement(pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(None, u'lastModifiedHeader'),
    pyxb.binding.datatypes.string, scope=ResponseNotify,
    location=pyxb.utils.utility.Location(
        '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/responseNotify.xsd',
        20, 12)))


def _BuildAutomaton_70():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_70
    del _BuildAutomaton_70
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/responseNotify.xsd',
                                    16, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/responseNotify.xsd',
                                    18, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/responseNotify.xsd',
                                    19, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1,
                                metadata=pyxb.utils.utility.Location(
                                    '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/responseNotify.xsd',
                                    20, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ResponseNotify._UseForTag(
        pyxb.namespace.ExpandedName(Namespace, u'statusCode')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/responseNotify.xsd',
                                                 15, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ResponseNotify._UseForTag(
        pyxb.namespace.ExpandedName(None, u'representation')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/responseNotify.xsd',
                                                 16, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ResponseNotify._UseForTag(
        pyxb.namespace.ExpandedName(None, u'locationHeader')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/responseNotify.xsd',
                                                 18, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ResponseNotify._UseForTag(
        pyxb.namespace.ExpandedName(None, u'etagHeader')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/responseNotify.xsd',
                                                 19, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ResponseNotify._UseForTag(
        pyxb.namespace.ExpandedName(None, u'lastModifiedHeader')),
                                             pyxb.utils.utility.Location(
                                                 '/home/kca/vcs/openmtc/openmtc-python/tmp/XSDs v211/responseNotify.xsd',
                                                 20, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update,
                     is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True)]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


ResponseNotify._Automaton = _BuildAutomaton_70()




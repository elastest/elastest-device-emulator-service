import string
from datetime import datetime
from iso8601.iso8601 import parse_date, ParseError
from random import choice
from urlparse import urlparse

import openmtc_cse.api as api
from futile import uc
from futile.logging import LoggerMixin
from openmtc.exc import OpenMTCError
from openmtc.model import FlexibleAttributesMixin
from openmtc.util import datetime_now
from openmtc_cse.methoddomain.filtercriteria import check_match
from openmtc_onem2m.exc import (CSEOperationNotAllowed, STATUS_OK, CSETypeError,
                                CSEMissingValue, CSEValueError, STATUS_CREATED,
                                CSEError, CSESyntaxError, CSEBadRequest)
from openmtc_onem2m.model import (ExpiringResource, Notification,
                                  AccessControlOperationE, ResourceTypeE,
                                  NotificationContentTypeE, FilterUsageE,
                                  get_short_resource_name, URIList,
                                  DiscResTypeE, AttributeList)
from openmtc_onem2m.transport import (OneM2MResponse, MetaInformation,
                                      OneM2MRequest, OneM2MOperation)
from openmtc_scl.transportdomain.util import match_now_cron
from openmtc_server.db import DBError
from openmtc_server.util import uri_safe
from openmtc_server.util.async import async_all
from copy import copy

_resource_id_counter = {}


class OneM2MDefaultController(LoggerMixin):
    RANDOM_SOURCE = string.letters + string.digits

    result_content_type = None

    def __init__(self, db_session, resource_type, handle_onem2m_request):
        super(OneM2MDefaultController, self).__init__()
        self.resource_type = resource_type
        self.db_session = db_session
        self.handle_onem2m_request = handle_onem2m_request

    def __call__(self, request, target_resource):
        self.logger.debug("%s servicing request", type(self).__name__)

        self.request = request
        self.resource = target_resource

        self.global_config = api.config["global"]
        self.api = api.api
        self.events = api.events

        self.values = None

        return self._handle_request()

    def _handle_request(self):
        try:
            handler = getattr(self, "_handle_" + self.request.operation.name)
        except AttributeError as e:
            raise CSEOperationNotAllowed(e)
        return handler()

    def _check_authorization(self):
        pass  # TODO(rst): recheck later
        # self.logger.debug("checking authorization")
        #
        # # get accessControlPolicies of resource
        # if hasattr(self, "resource"):
        #     # self.logger.debug("resource: %s", self.resource)
        #
        #     # check selfPrivileges if resource is policy, otherwise get linked
        #     # policies and check their privileges
        #     if isinstance(self.resource, AccessControlPolicy):
        #         self.logger.debug("resource is AccessControlPolicy, checking "
        #                           "selfPrivileges '%s'",
        #                           self.resource.selfPrivileges)
        #         for selfpriv in self.resource.selfPrivileges:
        #             if self._is_privileged(self.request, selfpriv):
        #                 return
        #
        #         raise CSEPermissionDenied("authentication failed. Cause: "
        #                                   "selfPrivileges")
        #     elif isinstance(self.resource, AccessControlPolicyIDHolder):
        #
        #         policies = []
        #         for aid in self.resource.accessControlPolicyIDs:
        #             # get accessControlPolicy object (as Promise)
        #             policies.append(self.db_session.get(aid))
        #
        #         # get all policies and iterate through them and their privileges
        #         def _handle_policies(policies):
        #             for policy in policies:
        #                 for privilege in policy.privileges:
        #                     if self._is_privileged(self.request, privilege):
        #                         self.logger.debug("SUCCESS: checking "
        #                                           "accessControlPolicyIDs DONE")
        #                         return
        #
        #             # unable to authorize request, raise exception
        #             raise CSEPermissionDenied("authentication failed. Cause: "
        #                                       "Not matching any privilege")
        #
        #         if policies:
        #             return _handle_policies(policies)
        #         else:
        #             self.logger.debug("no policies to check. DONE")
        #     else:
        #         # TODO(rst): what happens with resources without policies?
        #         pass
        #
        # else:
        #     # TODO is this ok to happen?
        #     self.logger.warn("tried checking authorization without resource!")

    def _is_privileged(self, request, privilege):
        self.logger.debug("_is_privileged -> keys: %s", privilege.__dict__)

        # 1st - request originator in originators?
        # privilege.accessControlOriginators = ["all" || "<domain>" || "<originatorIdentifier>"]
        if hasattr(privilege,
                   "accessControlOriginators") and privilege.accessControlOriginators:
            for originator in privilege.accessControlOriginators:
                if originator == "all":
                    self.logger.debug(
                        "all originators are valid for this privilege")
                    break
                elif request.fr is None:
                    self.logger.debug(
                        "request originator is None(admin), therefore allowed")
                    return True
                else:  # check domain/identifier
                    parsed = urlparse(request.fr)
                    self.logger.debug("parsed originator: %s", parsed)
                    domain = parsed.hostname
                    originatorid = parsed.path
                    if originator == domain or originator == originatorid:
                        self.logger.debug(
                            "request originator matches domain/identifier")
                    else:
                        self.logger.debug("invalid originator: '%s' != '%s'",
                                          request.fr, originator)
                        return False
        else:
            self.logger.debug("no accessControlOriginators to check")

        # TODO: 2nd - request matches context criterias? (time window || location || ipAddress)
        if hasattr(privilege,
                   "accessControlContexts") and privilege.accessControlContexts:
            for context in privilege.accessControlContexts:
                # check time windows
                if hasattr(context, "accessControlWindows"):
                    window_match = False
                    for window in context.accessControlWindows:
                        if match_now_cron(window):
                            window_match = True
                            break

                    if window_match:
                        self.logger.debug("time window is open for request")
                    else:
                        self.logger.debug("time window closed for request")
                        return False

                elif (hasattr(context, "accessControlIpAddresses") and
                      privilege.accessControlIpAddresses):
                    ip_match = False
                    for ip in context.accessControlIpAddresses:
                        pass
                        # TODO (ren): match request ip with this ip

                elif (hasattr(context, "accessControlLocationRegions") and
                      privilege.accessControlLocationRegions):
                    loc_match = False
                    for locationRegion in context.accessControlLocationRegions:
                        pass
                        # TODO: implement location check when location
                        # TODO: information is available
                        # locationRegion.latitude
                        # locationRegion.longitude
                        # locationRegion.radius
                        # locationRegion.countryCode

        # 3rd - operation allowed?
        # privilege.accessControlOperations e.g. [1, 3] <- intEnums type AccessControlOperation
        if hasattr(privilege,
                   "accessControlOperations") and privilege.accessControlOperations:
            # get int of operation from AccessControlOperation class, and check if it's in privileged operations
            if getattr(AccessControlOperationE,
                       request.op) in privilege.accessControlOperations:
                self.logger.debug(
                    "request operation '%s' is part of allowed operations '%s'",
                    request.op,
                    privilege.accessControlOperations)
            else:
                self.logger.debug(
                    "request operation '%s' is not part of allowed operations '%s'",
                    request.op,
                    privilege.accessControlOperations)
                return False
        else:
            self.logger.debug("no accessControlOperations to check")

        # went through all stages -> success, return True
        return True

    # CREATE

    def _handle_create(self):
        self.parent = self.resource
        del self.resource

        self.now = datetime_now()
        self.fields = []

        self._check_authorization()
        self._check_create_representation()
        self._create_resource()
        self._finalize_create()
        return self._send_create_response()

    def _check_create_representation(self):
        rt = self.resource_type

        # TODO(rst): change controller to work on resource itself
        values = self.request.content.get_values(True)

        self.logger.debug("_check_create_representation: %s", values)

        # TODO: move this to expiration time handler plugin
        # but needs to be set to a value even if plugin is disabled
        if issubclass(self.resource_type, ExpiringResource):
            expiration_time = values.get("expirationTime")
            if not expiration_time:
                expiration_time = self.now + self.global_config[
                    "default_lifetime"]
                self.fields.append("expirationTime")
            else:
                if not isinstance(expiration_time, datetime):
                    try:
                        expiration_time = parse_date(expiration_time)
                    except ParseError as e:
                        raise CSEValueError(
                            "Illegal value for expirationTime: %s" % (e,))
                if expiration_time < self.now + self.global_config[
                        "min_lifetime"]:
                    self.logger.warn("expirationTime is too low. Adjusting")
                    expiration_time = self.now + self.global_config[
                        "min_lifetime"]
                    self.fields.append("expirationTime")
                elif expiration_time > self.now + self.global_config[
                        "max_lifetime"]:
                    self.logger.warn("expirationTime is too high. Adjusting")
                    expiration_time = self.now + self.global_config[
                        "max_lifetime"]
                    self.fields.append("expirationTime")

            values["expirationTime"] = expiration_time

        rt_attributes = rt.attributes
        ignore_extra = self.global_config["ignore_extra_attributes"]
        is_flex = ignore_extra and issubclass(self.resource_type,
                                              FlexibleAttributesMixin)

        # TODO: optimize
        if ignore_extra and not is_flex:
            names = rt.attribute_names
            for k in values.keys():
                if k not in names:
                    values.pop(k)

        for attribute in rt_attributes:
            have_attr = (attribute.name in values and
                         values[attribute.name] is not None)
            if not have_attr and attribute.mandatory:
                raise CSEMissingValue("Missing attribute: %s" %
                                      (attribute.name,))
            if have_attr and attribute.accesstype == attribute.RO:
                self._handle_ro_attribute(attribute)

        self.values = values

    def _handle_ro_attribute(self, attribute):
        if not self.request.internal:
            raise CSETypeError("Attribute must not be specified: %s" %
                               (attribute.name,))

    def _create_resource(self):
        # TODO(rst): change controller to work on resource itself
        if not self.values:
            values = self.request.content.get_values(True)
        else:
            values = self.values

        self._set_mandatory_create_attributes(values)

        self.logger.debug("Creating resource of type '%s' with values: %s",
                          self.resource_type, values)

        resource_type = self.resource_type

        if "stateTag" in resource_type.attribute_names:
            values["stateTag"] = 0

        resource = resource_type(**values)
        resource.path = self._get_resource_path()

        self.logger.info("Created resource of type '%s' at %s",
                         resource.typename, resource.path)

        self.resource = resource

        return self.db_session.store(resource)

    def _set_mandatory_create_attributes(self, values):
        values["creationTime"] = values["lastModifiedTime"] = self.now

        # set values for parentID and resourceID
        values["parentID"] = self.parent.resourceID
        short_name = get_short_resource_name(self.resource_type.typename)
        try:
            values["resourceID"] = short_name + str(
                _resource_id_counter[short_name])
            _resource_id_counter[short_name] += 1
        except KeyError:
            _resource_id_counter[short_name] = 0
            values["resourceID"] = short_name + str(
                _resource_id_counter[short_name])
            _resource_id_counter[short_name] += 1

        try:
            name = uc(values["resourceName"])
        except KeyError:
            name = "%s-%s" % (self.resource_type.typename, self._create_id())
        self.name = values["resourceName"] = name

        values["resourceType"] = ResourceTypeE[self.resource_type.typename]

    def _create_id(self):
        return ''.join([choice(self.RANDOM_SOURCE) for _ in range(16)])

    def _get_resource_path(self):
        try:
            return self.__resource_path
        except AttributeError:
            # TODO: current uri_safe is insufficient. need a better strategy
            rp = self.__resource_path = self.parent.path + "/" + uri_safe(
                self.name)
            return rp

    def _finalize_create(self):
        events = self.api.events
        events.resource_created.fire(self.resource,
                                     self.request)
        if self.parent is not None:
            events.resource_updated.fire(self.parent,
                                         self.request)

    def _send_create_response(self):
        return OneM2MResponse(STATUS_CREATED, pc=self.resource,
                              request=self.request)

    # RETRIEVE

    def _prepare_fields(self):
        """
        Make sure fields is a list
        :return:
        """

        self.fields = self.request.content and self.request.content.values

    def _handle_retrieve(self):
        try:
            fu = self.request.filter_criteria.filterUsage
        except AttributeError:
            fu = None
        self._prepare_fields()
        if fu == FilterUsageE.Discovery:
            self._prepare_discovery()
        else:
            self._check_authorization()
            self._prepare_resource()
        return self._send_retrieve_response()

    def _prepare_discovery(self):
        self.limit = None
        self.truncated = False

        try:
            self.drt = DiscResTypeE(int(self.request.drt))
        except TypeError:
            self.drt = DiscResTypeE.structured
        except ValueError:
            raise CSEBadRequest()

        if hasattr(self.request.filter_criteria, 'limit'):
            self.limit = self.request.filter_criteria.limit

        self.logger.debug("_prepare_resource -> _handle_result: %s" %
                          self.resource)

        self.discovered = []
        self.result = URIList(self.discovered)
        self._discovery()

    def _discovery(self):
        try:
            return self._do_discovery(self.resource)
        except OpenMTCError:
            self.logger.exception("Error during discovery")
            raise CSEError("Error during discovery")

    def _do_discovery(self, node):
        self.logger.debug("_do_discovery: %s", node)

        if self.limit and len(self.discovered) >= self.limit:
            self.logger.debug("stopping discovery: limit reached")
            self.truncated = True
            return True

        if check_match(node, self.request.filter_criteria):
            if self.drt == DiscResTypeE.unstructured:
                self.discovered.append(node.resourceID)
            else:
                self.discovered.append(node.path)

        if not self.truncated:
            self._retrieve_children_for_resource(node)
            self.logger.debug("checking sub resources of: %s", node)
            self.logger.debug("childResource: %s", node.childResource)
            for s in node.childResource:
                self.logger.debug("is resource '%s' virtual? -> %s", s.name,
                                  s.virtual)
                if not s.virtual:
                    sub_node = self.db_session.get(s.path)
                    self._do_discovery(sub_node)

    def _prepare_resource(self):
        self.logger.debug("preparing resource.")
        res = self.result = self.resource
        try:
            res.resourceType = getattr(ResourceTypeE,
                                       type(res).__name__)
        except AttributeError:
            self.logger.debug("no resourceType for %s", res)

        if self.fields and isinstance(self.fields, list):
            res.set_values({k: v if k in self.fields else None for
                            k, v in res.get_values().items()})
        return self._retrieve_children()

    def _send_retrieve_response(self):
        return OneM2MResponse(STATUS_OK, pc=self.result, request=self.request)

    def _retrieve_children(self):
        return self._retrieve_children_for_resource(self.resource)

    def _retrieve_children_for_resource(self, resource):
        self.logger.debug("getting children of: %s", resource)
        children = self.db_session.get_collection(None, resource)
        resource.childResource = children

    # UPDATE

    def _handle_update(self):
        self.now = datetime_now()
        self.fields = []

        self._check_authorization()
        self._check_update_representation()
        self._update_resource()
        self._finalize_update()
        return self._send_update_response()

    def _check_update_representation(self):
        rt = self.resource_type

        # TODO(rst): change controller to work on resource itself
        values = self.request.content.get_values(True)

        self.logger.debug("_check_update_representation: %s", values)

        for k in ("lastModifiedTime", "stateTag", "childResource"):
            values.pop(k, None)

        # TODO: move this to expiration time handler plugin
        # but needs to be set to a value even if plugin is disabled
        if issubclass(self.resource_type, ExpiringResource):
            expiration_time = values.get("expirationTime")
            if not expiration_time:
                expiration_time = self.now + self.global_config[
                    "default_lifetime"]
                self.fields.append("expirationTime")
            else:
                if not isinstance(expiration_time, datetime):
                    try:
                        expiration_time = parse_date(expiration_time)
                    except ParseError as e:
                        raise CSEValueError(
                            "Illegal value for expirationTime: %s" % (e,))
                if expiration_time < self.now + self.global_config[
                        "min_lifetime"]:
                    self.logger.warn("expirationTime is too low. Adjusting")
                    expiration_time = self.now + self.global_config[
                        "min_lifetime"]
                    self.fields.append("expirationTime")
                elif expiration_time > self.now + self.global_config[
                        "max_lifetime"]:
                    self.logger.warn("expirationTime is too high. Adjusting")
                    expiration_time = self.now + self.global_config[
                        "max_lifetime"]
                    self.fields.append("expirationTime")

            values["expirationTime"] = expiration_time

        rt_attributes = rt.attributes
        ignore_extra = self.global_config["ignore_extra_attributes"]
        is_flex = ignore_extra and issubclass(self.resource_type,
                                              FlexibleAttributesMixin)

        # TODO: optimize
        if ignore_extra and not is_flex:
            names = rt.attribute_names
            for k in values.keys():
                if k not in names:
                    values.pop(k)

        for attribute in rt_attributes:
            have_attr = attribute.name in values
            if have_attr and attribute.accesstype == attribute.WO:
                self._handle_wo_attribute(attribute)

    def _handle_wo_attribute(self, attribute):
        if not self.request.internal:
            raise CSETypeError("Attribute must not be specified: %s" %
                               (attribute.name,))

    def _update_resource(self):
        # TODO(rst): change controller to work on resource itself (partly done)
        values = self.request.content.get_values(True)

        self._set_mandatory_update_attributes(values)

        self.logger.debug("Updating resource of type '%s' with values: %s",
                          self.resource_type, values)

        resource_type = self.resource_type

        if "stateTag" in resource_type.attribute_names:
            values["stateTag"] = 0

        resource = resource_type(**values)

        for v in values.keys():
            setattr(self.resource, v, values[v])

        # resource.path = self.resource.path

#        self.logger.info("Updated resource of type '%s' at %s",
#                        resource.typename, resource.path)
        self.logger.info("Updated resource of type '%s' at %s",
                         self.resource.typename, self.resource.path)

        # self.resource = resource

        return self.db_session.update(self.resource)
        # return self.db_session.update(resource, values.keys())

    def _set_mandatory_update_attributes(self, values):
        values["lastModifiedTime"] = self.now

    def _finalize_update(self):
        events = self.api.events
        events.resource_updated.fire(self.resource,
                                     self.request)

    def _send_update_response(self):
        return OneM2MResponse(STATUS_OK, pc=self.resource,
                              request=self.request)

    # DELETE

    def _handle_delete(self):
        self._check_authorization()
        self._delete_resource()
        if not self.request.cascading:
            self._get_parent()
        self._finalize_delete()
        return self._send_delete_response()

    def _get_parent(self):
        self.parent = self.db_session.get(self.resource.parent_path)

    def _delete_resource(self):
        self._delete_children()
        self._do_delete_resource()

    def _do_delete_resource(self):
        return self.db_session.delete(self.resource)

    def _delete_children(self):
        self._retrieve_children()
        self._do_delete_children()

    def _do_delete_children(self):
        child_promises = []

        for child in self.resource.childResource:
            request = OneM2MRequest(OneM2MOperation.delete, child.path, fr=None,
                                    rqi=self.request.rqi)
            request.cascading = True
            child_promises.append(self.handle_onem2m_request(request))

        async_all(child_promises, fulfill_with_none=True).get()

    def _finalize_delete(self):
        if not self.request.cascading:
            self.events.resource_updated.fire(self.parent,
                                              self.request)
        self.events.resource_deleted.fire(self.resource, self.request)

    def _send_delete_response(self):
        return OneM2MResponse(STATUS_OK, request=self.request)


# see TS-0004 7.4.4
class CSEBaseController(OneM2MDefaultController):
    def _handle_create(self):
        raise CSEOperationNotAllowed()

    def _prepare_resource(self):
        super(CSEBaseController, self)._prepare_resource()
        self.resource.pointOfAccess = self.api.get_onem2m_endpoints()

    def _handle_delete(self):
        raise CSEOperationNotAllowed()


# see TS-0004 7.4.5
class RemoteCSEController(OneM2MDefaultController):
    # TODO(rst): add Mca check -> 7.4.5.2.1 Create
    pass


class AEController(OneM2MDefaultController):
    def _set_mandatory_create_attributes(self, vals):
        super(AEController, self)._set_mandatory_create_attributes(vals)

        originator = self.request.fr

        if originator and originator.startswith('C'):
            vals["AE-ID"] = originator
        else:
            vals["AE-ID"] = "C" + str(_resource_id_counter["ae"] - 1)

        # TODO(rst): set AE-ID and nodeLink
        vals["nodeLink"] = "dummy"


class SubscriptionController(OneM2MDefaultController):
    def _handle_create(self):
        self.parent = self.resource
        del self.resource

        self.now = datetime_now()
        self.fields = []

        self._check_authorization()
        self._check_originator_access()
        self._check_notification_uri()
        self._check_create_representation()
        self._create_resource()
        self._finalize_create()
        return self._send_create_response()

    # def _check_syntax_create(self):
    #     super(SubscriptionController, self)._check_syntax_create()
    #     try:
    #         criterias = self.request.pc["eventNotificationCriteria"]
    #         if criterias:
    #             from openmtc_cse.methoddomain.filtercriteria import filters
    #
    #             self.logger.debug("validating filter criterias: %s", criterias)
    #             for crit in criterias:
    #                 if crit != "attribute":
    #                     if hasattr(filters, crit):
    #                         self.logger.debug("criterion '%s' is valid", crit)
    #                         pass  # valid filter
    #                     else:
    #                         self.logger.error("criterion '%s' is invalid", crit)
    #                         raise CSESyntaxError("unknown criterion: %s", crit)
    #     except KeyError as e:
    #         pass
    #         # self.logger.warn(e)

    def _check_originator_access(self):
        # TODO(rst): TS-004 7.3.8.2.1
        # 3. Check if the subscribed-to resource, addressed in To parameter in
        # the Request, is subscribable. Subscribable resource types are defined
        # in TS-0001 Functional Architecture [6], they have <subscription>
        # resource types as their child resources.
        # If it is not subscribable, the Hosting CSE shall return the Notify
        # response primitive with a Response Status Code indicating
        # "TARGET_NOT_SUBSCRIBABLE" error.

        # 4. Check if the Originator has privileges for retrieving the
        # subscribed-to resource.
        # If the Originator does not have the privilege, the Hosting CSE shall
        # return the Notify response primitive with Response Status Code
        # indicating "NO_PRIVILEGE" error.
        return

    def _check_notification_uri(self):
        # TODO(rst): TS-004 7.3.8.2.1
        # 5. If the notificationURI is not the Originator, the Hosting CSE
        # should send a Notify request primitive to the notificationURI with
        # verificationRequest parameter set as TRUE (clause 7.4.1.2.2).

        # debug only
        if self.request.originator is None:
            return

        try:
            self.logger.debug("Checking notificationURI: %s",
                              self.request.content.notificationURI)
            uris = [uri for uri in
                    self.request.content.notificationURI if
                    not uri.startswith(self.request.originator)]
            # TODO(rst): change the check that it should be a valid AE-ID
            # for uri in uris:
            #     if not urlparse(uri).scheme:
            #         raise CSESyntaxError("Invalid notificationURI")
        except KeyError:
            raise CSESyntaxError("Invalid notificationURI")

        # a. If the Hosting CSE cannot send the Notify request primitive, the
        # Hosting CSE shall return the Notify response primitive with a Response
        # Status Code indicating "SUBSCRIPTION_VERIFICATION_INITIATION_FAILED"
        # error.

        def send_verification(notify_uri):
            notification = Notification(
                verificationRequest=True,
                creator=self.request.originator
            )

            send_notify_request = OneM2MRequest(OneM2MOperation.notify,
                                                notify_uri, None,
                                                MetaInformation(None),
                                                notification)
            return self.api.send_onem2m_request(send_notify_request)

        # b. If the Hosting CSE sent the primitive, the Hosting CSE shall
        # check if the Notify response primitive contains a Response Status Code
        # indicating "SUBSCRIPTION_CREATOR_HAS_NO_PRIVILEGE" or
        # "SUBSCRIPTION_HOST_HAS_NO_PRIVILEGE" error. If so, the Hosting CSE
        # shall return the Create response primitive with a Response Status Code
        # indicating the same error from the Notify response primitive to the
        # Originator.

        def handle_error(error):
            self.logger.info("Subscription verification failed: %s", error)
            raise CSEError
            # TODO(rst): check subscription error
            # if error.status_code in [
            #     STATUS_REQUEST_TIMEOUT,
            #     STATUS_BAD_GATEWAY,
            #     STATUS_SERVICE_UNAVAILABLE,
            #     STATUS_GATEWAY_TIMEOUT
            # ]:
            #     raise CannotInitiateSubscriptionVerification(error)
            # elif error.status_code == STATUS_SUBSCRIPTION_VERIFICATION_FAILED:
            #     raise SubscriptionVerificationFailed(error)
            # else:
            #     raise CSEBadGateway(error)

        try:
            async_all(map(send_verification, uris),
                      fulfill_with_none=True).get()
        except Exception as error:
            handle_error(error)

    def _set_mandatory_create_attributes(self, values):
        super(SubscriptionController,
              self)._set_mandatory_create_attributes(values)
        # TODO(rst): TS-004 7.3.8.2.1
        # 7. If the notificationURI is not the Originator, the Hosting CSE shall
        # store Originator ID to creator attribute.
        if (self.request.originator not in
                values["notificationURI"]):
            values["creator"] = self.request.originator

        # set notificationContentType if not set
        if "notificationContentType" not in values:
            values["notificationContentType"] = \
                NotificationContentTypeE.allAttributes


class ContainerController(OneM2MDefaultController):
    def _set_mandatory_create_attributes(self, values):
        super(ContainerController,
              self)._set_mandatory_create_attributes(values)
        values["creator"] = self.request.originator or 'nobody'
        values["currentNrOfInstances"] = 0
        values["currentByteSize"] = 0


class ContentInstanceController(OneM2MDefaultController):
    def _create_resource(self):
        super(ContentInstanceController, self)._create_resource()

        # handle_old_instances
        max_nr_of_instances = self.parent.maxNrOfInstances
        current_nr_of_instances = self.parent.currentNrOfInstances
        if 0 < max_nr_of_instances <= current_nr_of_instances:
            self.parent.currentNrOfInstances -= 1
            self.parent.currentByteSize -= self.parent.oldest.contentSize

            self.db_session.delete(self.parent.oldest)

            if self.parent.currentNrOfInstances >= 1:
                oldest = self.db_session.get_oldest_content_instance(
                    self.parent)
                self.logger.debug("Setting new oldest: %s", oldest)
                self.parent.oldest = oldest
            else:
                self.logger.debug("Setting oldest to None")
                self.parent.oldest = None

        # handle_new_instance
        self.parent.currentNrOfInstances += 1
        self.parent.currentByteSize += self.resource.contentSize
        if self.parent.oldest is None:
            self.logger.debug("Setting new resource as oldest: %s",
                              self.resource)
            self.parent.oldest = self.resource
        self.parent.latest = self.resource
        self.db_session.update(self.parent)

    def _set_mandatory_create_attributes(self, vals):
        self.request.name = None
        super(ContentInstanceController,
              self)._set_mandatory_create_attributes(vals)

        vals["contentSize"] = len(vals["content"].encode('utf-8'))
        if not vals.get("contentInfo"):
            vals["contentInfo"] = 'text/plain:0'

    def _delete_resource(self):
        super(ContentInstanceController, self)._delete_resource()

        cnt = self.db_session.get(self.resource.parentID)
        # TODO(rst): handle byte size
        try:
            ci_l = self.db_session.get_latest_content_instance(cnt)
            ci_o = self.db_session.get_oldest_content_instance(cnt)
        except (DBError, KeyError):
            cnt.latest = None
            cnt.oldest = None
            cnt.currentNrOfInstances = 0
        else:
            cnt.latest = ci_l
            cnt.oldest = ci_o
            cnt.currentNrOfInstances -= 1

        return self.db_session.update(cnt)


class AccessControlPolicyController(OneM2MDefaultController):
    def _set_mandatory_create_attributes(self, vals):
        super(AccessControlPolicyController,
              self)._set_mandatory_create_attributes(vals)

        # set selfPrivileges
        if vals.get("selfPrivileges") is None:
            accessControlRule = {}
            accessControlOriginators = {}
            accessControlOperations = {}
            # accessControlContexts = {}

            # fill accessControlOriginators
            reference = ["all"]
            accessControlOriginators["reference"] = reference

            # fill accessControlOperations
            # FIXME: use enum values
            accessControlOperation = [1, 2, 3, 4, 5, 6]
            accessControlOperations[
                "accessControlOperation"] = accessControlOperation

            # accessControlWindows = ["* * * * *"]
            # accessControlContexts["accessControlWindows"] = accessControlWindows

            # add -Originators & -Operations to accessControlRule
            accessControlRule[
                "accessControlOriginators"] = accessControlOriginators
            accessControlRule[
                "accessControlOperations"] = accessControlOperations
            # accessControlRule["accessControlContexts"] = accessControlContexts

            # set rule as selfPrivilege
            vals["selfPrivileges"] = [accessControlRule]

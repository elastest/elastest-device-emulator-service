import string
from base64 import b64decode, b64encode
from copy import copy
from datetime import datetime
from iso8601 import parse_date, ParseError
from operator import attrgetter
from random import choice
from re import compile as regex_compile
from urlparse import urlparse

from futile import uc
from futile.logging import LoggerMixin
from openmtc.model.exc import ModelError
from openmtc.util import datetime_now
from openmtc_etsi.exc import (SCLError, SCLValueError, SCLMissingValue,
                              SCLTypeError, SCLConflict, SCLNotFound,
                              STATUS_NOT_FOUND, SCLPermissionDenied,
                              SCLBadRequest, STATUS_PERMISSION_DENIED,
                              STATUS_OK, SCLNotAcceptable, SCLMethodNotAllowed,
                              SCLBadGateway, SCLForbidden)
from openmtc_etsi.model import (Application, ContentInstance,
                                Scl, Discovery, ContentInstances,
                                AccessRight, ExpiringResource,
                                AnnouncementResource, FlexibleAttributesMixin,
                                MembersContent, Group, get_etsi_types)
from openmtc_etsi.response import (RetrieveResponseConfirmation,
                                   CreateResponseConfirmation,
                                   DeleteResponseConfirmation,
                                   ErrorResponseConfirmation,
                                   UpdateResponseConfirmation)
from openmtc_etsi.scl import (RetrieveRequestIndication,
                              DeleteRequestIndication, CreateRequestIndication,
                              UpdateRequestIndication, RequestIndicationMethod)
from openmtc_etsi.serializer import get_serializer
from openmtc_scl.mappingfunction import get_request_method
from openmtc_scl.methoddomain.filtercriteria import (filter_resources,
                                                     parse_filter_criteria)
from openmtc_scl.methoddomain.util import get_decoded_content
from openmtc_server.transportdomain import Request
from openmtc_server.util import (get_regex_path_component, uri_safe,
                                 is_text_content, join_url)
from openmtc_server.util.async import async_all

# uri component
PATH_COMPONENT = get_regex_path_component()

# scl base -> /m2m
SCL_BASE = '/m2m'

# TODO: kca: Move this into some capability module (like XRAR)?


# TODO: kca: make this an ABC?
# TODO: move api, events and config into global modules
# can we get rid of handle_request_indication?

class Controller(LoggerMixin):
    RANDOM_SOURCE = string.letters + string.digits

    __methods__ = (RequestIndicationMethod.create,
                   RequestIndicationMethod.update,
                   RequestIndicationMethod.delete)

    result_content_type = None

    def __init__(self, db_session, resource_type, events, api, config,
                 handle_request_indication, *args, **kw):
        super(Controller, self).__init__(*args, **kw)

        assert (db_session is not None)

        self.api = api
        self.db_session = db_session
        self.resource_type = resource_type
        self.events = events
        self.config = config
        self.global_config = config["global"]
        self._handle_request_indication = handle_request_indication
        self.etsi_config = etsi_config = config["etsi"]

        self._etsi_version_1 = etsi_config["etsi_version"] < "2.0"
        etsi_compatibility = etsi_config.get("etsi_compatibility")
        if etsi_compatibility:
            self._etsi_compatibility_1 = etsi_compatibility < "2.0"
            self._etsi_compatibility_2 = etsi_compatibility >= "2.0"
        else:
            self._etsi_compatibility_1 = False
            self._etsi_compatibility_2 = False

    def __call__(self, request_indication, target_resource, endpoint):
        self.logger.debug("%s servicing request", type(self).__name__)

        self.request_indication = request_indication
        self.resource = target_resource
        self.endpoint = endpoint
        return self._handle_request()

    def _handle_request(self):
        try:
            handler = getattr(self, "_handle_" +
                              self.request_indication.method)
        except AttributeError as e:
            raise SCLMethodNotAllowed(e)

        return handler()

    def _handle_create(self):
        if RequestIndicationMethod.create not in self.__methods__:
            raise SCLMethodNotAllowed("Cannot create '%s' resources" %
                                      (self.resource_type.__name__,))

        self.parent = self.resource
        del self.resource

        self.now = datetime_now()
        self.fields = []

        self._check_syntax_create()
        self._check_create_representation()
        self._check_authorization()
        self._create_resource()
        self._update_parent()
        self._create_subresources()
        self._finalize_create()
        return self._send_create_response()

    def _fill_parent(self):
        if self.parent is not None:
            return self._do_fill_collections(self.parent)

    def _finalize_create(self):
        self.events.resource_created.fire(self.resource,
                                          self.request_indication)
        if self.parent is not None:
            self.events.resource_updated.fire(self.parent,
                                              self.request_indication)

    def _send_create_response(self):
        return CreateResponseConfirmation(resource=self.resource,
                                          fields=self.fields)

    def _handle_retrieve(self):
        # TODO: kca: handle PA

        # 10.3.2.5 Check authorization of the requestingEntity based on accessRightID
        # 10.3.2.6 Check authorization of the requestingEntity based on selfPermission
        # 10.3.2.7 Check authorization of the requestingEntity based on default access rights

        # 10.3.2.17 Send ResponseConfirm primitive

        self._check_syntax_retrieve()
        self._check_authorization()
        self._prepare_resource()
        return self._send_retrieve_response()

    def _get_pa_elem(self, node, name):
        try:
            return getattr(node, name)
        except AttributeError:
            try:
                return node[name]
            except (KeyError, IndexError, TypeError):
                raise SCLNotFound(name)

    def _prepare_resource(self):
        pa = self.request_indication.partial_accessor
        self.logger.debug("preparing resource. partial accessor: %s", pa)
        if pa:
            pa = pa.split("/")
            pa, pa_last = pa[:-1], pa[-1]

            node = self.resource

            self.logger.debug(pa, pa_last)

            for k in pa:
                node = self._get_pa_elem(node, k)

            if isinstance(node, list):
                if pa_last not in node:
                    raise SCLNotFound(pa_last)
                self.result = self.result_content_type = None
            else:
                result = self._get_pa_elem(node, pa_last)
                if isinstance(result, list):
                    result = {pa_last[:-1]: result}
                self.result = {pa_last: result}
        else:
            self.result = self.resource
            return self._fill_collections()

    def _check_syntax_retrieve(self):
        pass

    def _fill_collections(self):
        return self._do_fill_collections(self.resource)

    def _do_fill_collections(self, resource):
        arglist = [(resource, collection)
                   for collection in resource.collections]
        return self.api.starmap(self._fill_collection, arglist)

    def _fill_collection(self, resource, collection):
        results = self.db_session.get_collection(collection.content_type,
                                                resource)
        setattr(resource, collection.name, results)

    def _send_retrieve_response(self):
        ct = self.result_content_type
        self.logger.debug("Sending retrieve response: %s (%s)", self.result, ct)
        return RetrieveResponseConfirmation(self.result,
                                            content_type=ct)

    def _handle_update(self):
        if RequestIndicationMethod.update not in self.__methods__:
            raise SCLMethodNotAllowed("Cannot update '%s' resources" %
                                      (self.resource_type.__name__,))
        self.now = datetime_now()

        self._check_syntax_update()
        self._check_update_representation()
        self._check_authorization()
        self._update_resource()
        self._finalize_update()
        return self._send_update_response()

    def _check_syntax_update(self):
        pass

    def _check_update_representation(self):
        rt = type(self.resource)
        # TODO: this should probably go into check_syntax
        try:
            pa = self.request_indication.partial_accessor
            if pa:  # partial addressing
                try:
                    attr = getattr(rt, pa)
                except AttributeError:
                    raise SCLNotFound(self.request_indication.path + "/" + pa)
                if pa not in self.request_indication.resource:
                    raise SCLBadRequest()
                if attr.accesstype in (attr.RO, attr.WO):
                    self._handle_ro_attribute(attr)
                return
        except AttributeError:
            # TODO: kca: how do we get here?
            pass

        vals = self.request_indication.resource

        if self.global_config["ignore_extra_attributes"] and \
                not issubclass(self.resource_type, FlexibleAttributesMixin):
            names = map(attrgetter("name"), rt.attributes)
            for k in vals.keys():
                if k not in names:
                    vals.pop(k)

        for attribute in rt.attributes:
            have_attr = vals.get(attribute.name) is not None
            if (not have_attr and attribute.update_mandatory and
                    self.etsi_config["etsi_compatibility"] >=
                    attribute.version):
                raise SCLMissingValue("%s is mandatory on update" %
                                      (attribute.name, ))
            if have_attr and attribute.accesstype in (attribute.RO,
                                                      attribute.WO):
                self._handle_ro_attribute(attribute)

    def _update_resource(self):
        vals = self.request_indication.resource

        self._update_mandatory_attributes(vals)

        self.logger.debug("Updating resource %s with %s", self.resource,
                          self.request_indication.resource)
        self.resource.set_values(self.request_indication.resource)

        fields = self.request_indication.resource.keys()[:]
        if "lastModifiedTime" not in fields:
            fields.append("lastModifiedTime")
        return self.db_session.update(self.resource, fields=fields)

    def _finalize_update(self):
        self.events.resource_updated.fire(self.resource,
                                          self.request_indication)

    def _send_update_response(self):
        return UpdateResponseConfirmation()

    def _handle_delete(self):
        cascading = self.request_indication.cascading
        if (not cascading and
                RequestIndicationMethod.delete not in self.__methods__):
            raise SCLMethodNotAllowed("Cannot delete '%s' resources" %
                                      (self.resource_type.__name__,))
        self._check_syntax_delete()
        self._check_authorization()
        self._delete_resource()
        if not cascading:
            self._get_parent()
        self._finalize_delete()
        return self._send_delete_response()

        # 10.3.2.1 Check existence of the addressed resource
        # if not self.db_session.exists(self.resource_type,
        # (("path", self.request_indication.path), )):
        # raise SCLNotFound(self.request_indication.path)

        # 10.3.2.5 Check authorization of the requestingEntity based on accessRightID
        # 10.3.2.6 Check authorization of the requestingEntity based on selfPermission
        # 10.3.2.7 Check authorization of the requestingEntity based on default access rights
        #
        # self.db_session.delete(self.resource_type, self.request_indication.path)
        #
        # self.events.resource_deleted.fire(self.resource_type,
        # self.request_indication.path)
        #
        # return DeleteResponseConfirmation()

    def _get_parent(self):
        self.parent = self.db_session.get(self.resource.parent_path)
        self._fill_parent()

    def _check_syntax_delete(self):
        pass

    def _delete_resource(self):
        self._delete_children()
        self._delete_subresources()
        self._do_delete_resource()

    def _do_delete_resource(self):
        return self.db_session.delete(self.resource)

    def _delete_children(self):
        self._fill_collections()
        self._do_delete_children().get()

    def _do_delete_children(self):
        child_promises = []

        for attr in self.resource.collections:
            collection = getattr(self.resource, attr.name)
            for child in collection:
                req_ind = DeleteRequestIndication(child.path,
                                                  reason="cascading")
                child_promises.append(self._handle_request_indication(req_ind))

        return async_all(child_promises, fulfill_with_none=True)

    def _delete_subresources(self):
        promises = []

        for attr in self.resource.subresources:
            if not attr.virtual:
                sr = getattr(self.resource, attr.name)
                req_ind = DeleteRequestIndication(sr.path, reason="cascading")
                promises.append(self._handle_request_indication(req_ind))

        async_all(promises, fulfill_with_none=True).get()

    def _finalize_delete(self):
        if not self.request_indication.cascading:
            self.events.resource_updated.fire(self.parent,
                                              self.request_indication)
        self.events.resource_deleted.fire(self.resource,
                                          self.request_indication)

    def _send_delete_response(self):
        return DeleteResponseConfirmation()

    def _check_create_representation(self):
        rt = self.resource_type

        vals = self.request_indication.resource

        # TODO: move this to expirationtime handler plugin
        if issubclass(self.resource_type, ExpiringResource):
            expiration_time = vals.get("expirationTime")
            if not expiration_time:
                expiration_time = self.now + self.global_config[
                    "default_lifetime"]
                self.fields.append("expirationTime")
            else:
                if not isinstance(expiration_time, datetime):
                    try:
                        expiration_time = parse_date(expiration_time)
                    except ParseError as e:
                        raise SCLValueError(
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

            vals["expirationTime"] = expiration_time

        vals.pop("lastModifiedTime", None)

        rt_attributes = rt.attributes
        ignore_extra = self.global_config["ignore_extra_attributes"]
        is_flex = ignore_extra and issubclass(self.resource_type,
                                              FlexibleAttributesMixin)

        # TODO: optimize
        if ignore_extra and not is_flex:
            names = rt.attribute_names
            for k in vals.keys():
                if k not in names:
                    vals.pop(k)

        etsi_compat = self.etsi_config["etsi_compatibility"]
        for attribute in rt_attributes:
            have_attr = bool(vals.get(attribute.name))
            if not have_attr and attribute.mandatory:
                if etsi_compat >= attribute.version:
                    raise SCLMissingValue("Missing attribute: %s" %
                                          (attribute.name, ))
                vals[attribute.name] = self._get_compat_value(attribute)
            if have_attr and attribute.accesstype == attribute.RO:
                self._handle_ro_attribute(attribute)

    def _get_compat_value(self, attribute):
        if issubclass(attribute.type, basestring):
            return "<not_set>"
        return attribute.type()

    def _handle_ro_attribute(self, attribute):
        if not self.request_indication.internal:
            raise SCLTypeError("Attribute must not be specified: %s" %
                               (attribute.name, ))

    def _check_syntax_create(self):
        pass

    def _get_resource_path(self):
        try:
            return self.__resource_path
        except AttributeError:
            # TODO: current uri_safe is insufficient. need a better strategy
            rp = self.__resource_path = self.parent.path + "/" + uri_safe(
                self.resource_name)
            return rp

    def _create_resource(self):
        vals = self.request_indication.resource

        self._set_mandatory_attributes(vals)

        self.logger.debug("Creating resource of type '%s' with values: %s",
                          self.resource_type, vals)

        try:
            resource = self.resource_type(**vals)
        except ModelError as exc:
            raise SCLBadRequest(exc)

        resource.path = self._get_resource_path()

        self.logger.info("Created resource of type '%s' at %s",
                         resource.typename, resource.path)

        self.resource = resource

        return self.db_session.store(resource)

    def _update_parent(self):
        parent = self.parent
        if parent is not None:
            parent.lastModifiedTime = self.resource.creationTime
            return self.db_session.update(parent, ["lastModifiedTime"])

    def _do_create_subresources(self, resources):
        sub_resources = []

        for resource in resources:
            for attr in resource.subresources:
                if not attr.virtual:
                    sr = getattr(resource, attr.name)
                    sub_resources.append(sr)

        map(self.db_session.store, sub_resources)
        if sub_resources:
            self._do_create_subresources(sub_resources)

    def _create_subresources(self):
        return self._do_create_subresources((self.resource, ))

    def _set_mandatory_attributes(self, vals):
        vals["creationTime"] = vals["lastModifiedTime"] = self.now

        id_attribute = self.resource_type.id_attribute

        if not id_attribute:
            return

        try:
            vals[id_attribute] = uc(vals[id_attribute])
        except KeyError:
            vals[id_attribute] = self._create_random_name()

        path = self.request_indication.path + "/" + vals[id_attribute]
        fields = {"path": path}

        while self.db_session.exists(self.resource_type, fields):
            if self.resource_type.id_immutable:
                raise SCLConflict("Application with same name exists already!")
            vals[id_attribute] = self._create_random_name()
            path = self.request_indication.path + "/" + vals[id_attribute]
            fields = {"path": path}

        self.resource_name = vals[id_attribute]

    def _update_mandatory_attributes(self, vals):
        vals["lastModifiedTime"] = self.now

    # TODO: Get rid of the resource <-> accessRightID "duality" !!!
    def _check_auth_based_on_access_right_id(self, resource,
                                             accessRightID=None):
        """TS 102.921 10.3.2.5
        """
        if not self.request_indication.requestingEntity:
            return

        # added by bro due to accessRightID handling with a given
        # access_right_id
        if not accessRightID or resource.typename != "application":
            accessRightID = resource.accessRightID

        # no access right id set
        if accessRightID is None:
            return self._check_auth_based_on_default_access_rights(resource)

        def get_permissions(res_con):
            try:
                permissions = res_con.resource.permissions
            except (AttributeError, KeyError):
                raise SCLError()
            self._check_permissions(permissions)

        def err(res_con):
            if res_con.statusCode == STATUS_NOT_FOUND:
                return self._check_auth_based_on_default_access_rights(resource)

            # TODO: may be other cases have to be caught before
            raise SCLError("Internal error: %s" % (res_con, ))

        req_ent = self.request_indication.requestingEntity
        req_ind = RetrieveRequestIndication(accessRightID,
                                            requestingEntity=req_ent)
        if self.api.is_local_path_sync(accessRightID):
            handle_request = self._handle_request_indication
        else:
            handle_request = self.api.send_request_indication
        try:
            return handle_request(req_ind).then(get_permissions, err).get()
        except SCLNotFound:
            return self._check_auth_based_on_default_access_rights(resource)

    def _check_auth_based_on_self_permissions(self, resource=None):
        """TS 102.921 10.3.2.6
        """
        if not self.request_indication.requestingEntity:
            return

        resource = resource or self.resource

        permissions = resource.selfPermissions

        self._check_permissions(permissions)

    _app_annc_regex = regex_compile('^' + SCL_BASE + '/scls/' +
                                    PATH_COMPONENT +
                                    '/applications/' + PATH_COMPONENT)
    _scl_regex = regex_compile('^' + SCL_BASE + '/scls/(' +
                               PATH_COMPONENT + ')')
    _app_regex = regex_compile('^' + SCL_BASE + '/applications/(' +
                               PATH_COMPONENT + ')')

    def _check_auth_based_on_default_access_rights(self, resource=None):
        """TS 102.921 10.3.2.7
        """
        if not self.request_indication.requestingEntity:
            return

        req_ent = self.request_indication.requestingEntity
        target_id = resource.path if resource else self.request_indication.path

        self.logger.debug("_check_auth_based_on_default_access_rights: "
                          "%s on %s (%s)", req_ent, target_id,
                          self.request_indication.path)

        req_ent_path = urlparse(req_ent).path
        target_id_path = urlparse(target_id).path

        scl_match = self._scl_regex.match(target_id_path)

        if scl_match is not None:
            # <sclBase>/scls/<scl>
            if scl_match.group(0) == req_ent_path:
                # <scl> is allowed
                return

        app_annc_match = self._app_annc_regex.match(target_id_path)

        if app_annc_match is not None:
            # <sclBase>/scls/<scl>/applications/<applicationAnnc>
            if scl_match is not None and scl_match.group(0) == req_ent_path:
                # <scl> is allowed
                return

            def check_link(res_con):
                try:
                    if res_con.resource.link == req_ent:
                        return True
                except AttributeError:
                    pass

                self.logger.info("Not allowed to %s due to default access "
                                 "rights", self.request_indication.method)
                return False

            scl_retrieve_req_ind = RetrieveRequestIndication(scl_match.group(0))
            if self._handle_request_indication(scl_retrieve_req_ind).then(
                    check_link).get():
                # <scl> is allowed
                return

            app_annc_pass = app_annc_match.group(0)
            app_retrieve_req_ind = RetrieveRequestIndication(app_annc_pass)
            if self._handle_request_indication(app_retrieve_req_ind).then(
                    check_link).get():
                # <applicationAnnc> is allowed
                return

        app_match = self._app_regex.match(target_id_path)
        if app_match is not None:
            # <sclBase>/applications/<application>
            if app_match.group(0) == req_ent_path:
                # <application> is allowed
                return

        self.logger.info("Not allowed to %s due to default access rights" %
                         (self.request_indication.method, ))
        raise SCLNotFound(target_id_path)

    def _check_permissions(self, permissions):
        method = self.request_indication.method
        req_ent = self.request_indication.requestingEntity

        req_ent_path = urlparse(req_ent).path

        # TODO: do we need both regexes always? Can a reqent be both SCL and APP?
        scl_match = self._scl_regex.match(req_ent_path)
        app_match = self._app_regex.match(req_ent_path)

        found_not_empty_entry = False

        access_methods = {
            "create": "CREATE",
            "retrieve": "READ",
            "update": "WRITE",
            "delete": "DELETE"
        }

        for permission in permissions:
            permission_holders = permission.permissionHolders
            permission_flags = permission.permissionFlags

            # check if all is present
            is_permission_holder = (permission_holders.all or
                                    req_ent in permission_holders.holderRefs or
                                    (app_match and app_match.group(1) in
                                     permission_holders.applicationIDs) or
                                    (scl_match and scl_match.group(1) in
                                     permission_holders.sclIDs))

            # TODO: if scl, look if sclBase URI matches holderRefs

            # TODO: if scl, look if sclBase URI matches group

            # check permission flags if holders match
            if is_permission_holder:
                if len(permission_flags):
                    found_not_empty_entry = True
                for flag in permission_flags:
                    if flag == access_methods[method]:
                        return

        # discover right granted
        if found_not_empty_entry:
            # TODO: kca: provide an error message here!
            raise SCLPermissionDenied()

        raise SCLNotFound()

    def _check_authorization(self):
        try:
            resource = self.resource
        except AttributeError:
            resource = self.parent
        return self._check_auth_based_on_access_right_id(resource)

    def _create_id(self):
        return ''.join([choice(self.RANDOM_SOURCE) for _ in range(16)])

    def _create_random_name(self):
        return "%s-%s" % (self.resource_type.typename, self._create_id())


DefaultController = Controller


class CollectionController(Controller):
    __methods__ = (RequestIndicationMethod.update,)


class SubscriptionsController(CollectionController):
    __methods__ = ()


class LocationContainerController(Controller):
    def _check_syntax_create(self):
        grandfather = self.db_session.get(self.parent.parent_path)
        if not isinstance(grandfather, Application):
            raise SCLForbidden("LocationContainer must be created "
                               "under an Application")
        return super(LocationContainerController, self)._check_syntax_create()


class ApplicationController(Controller):
    # kca: Doing these two steps in one would be a tiny bit more efficient
    # (less dict lookups). But this seems to be more in line with the spec

    # Also, all of this could be done a bit more generic

    # dp the create specific parts here
    """
    @todo: bro
    MUST:
        - write model based tests with a retarget server echoing and
          responding some requests
    OPTIONAL:
        - performance enhancements: replace dot notation
        - [replace fields from ressource and request_indication instead of
          using them in the method body]
    """

    def _handle_request(self):
        if self._check_for_aPoC():
            return self._handle_generic_aPoC()

        return super(ApplicationController, self)._handle_request()

    def _check_create_representation(self):
        super(ApplicationController, self)._check_create_representation()
        self._prune_apoc_paths()

    def _check_update_representation(self):
        super(ApplicationController, self)._check_update_representation()
        self._prune_apoc_paths()

    def _prune_apoc_paths(self):
        try:
            paths = self.request_indication.resource["aPoCPaths"]["aPoCPath"]
        except KeyError:
            return
        for i, entry in enumerate(paths):
            if isinstance(entry, dict):
                if self._etsi_version_1 and not self._etsi_compatibility_2:
                    raise SCLValueError("Invalid aPoCPaths entry: %s", entry)
            else:
                if not (self._etsi_compatibility_1 or self._etsi_version_1):
                    raise SCLValueError("Invalid aPoCPaths entry: %s", entry)
                # TODO: Use Entity
                paths[i] = entry = {"path": entry}

            try:
                if not entry["path"]:
                    raise SCLValueError("Empty path in aPoCPaths")
            except KeyError:
                raise SCLMissingValue("Missing 'path' entry in aPoCPaths"
                                      " item")

    def _handle_notify(self):
        if self._check_for_aPoC():
            return self._handle_generic_aPoC()

        raise SCLMethodNotAllowed("notify")

    def _check_for_aPoC(self):
        """ Based on TS 102.921 v211 - 10.3.2.23 - 1-11)
        Checks for the existence of all apoc_path elements.
        """
        resource = self.resource
        # is an apoc path set? use default handling when nothing is set
        if not self.request_indication.aPoc_path:
            return False

        if (resource.aPoC and resource.aPoCPaths):
            self.logger.debug("Having an aPoC and aPoCPaths")
            return True

        raise SCLNotFound("No aPoC or aPoCPaths Definition could be found to "
                          "compare to: %s" %
                          (self.request_indication.aPoc_path, ))

    def _handle_generic_aPoC(self):
        """ Based on TS 102.921 v211 - 10.3.2.23 - 3-11)
        A Generic (Request Indication Independent) Retargeting Method that
        handles all the retarget procedures
        @return: the promised response from the retargeted server
        """
        self._check_syntax_create()
        self._check_aPoC()
        self._check_authentication_with_accessRighID()
        path = join_url(self.resource.aPoC,
                        self.request_indication.aPoc_path)
        return self._retarget(path)

    def _check_aPoC(self):
        """ Based on TS 102.921 v211 - 10.3.2.23 - 3, 4a-b, 5)
        Checks if the aPoC path is in the aPocPaths list
        @return: the accessRightId from the aPocPaths element matching the
                 request indications aPoC path
        @raise ErrorResponseConfirmation: if the request indications aPoC path
                                          could not be matched
        """
        aPoC_path = self.request_indication.aPoc_path
        aPoCPaths = self.resource.aPoCPaths

        # get the aPocHandling from somewhere.
        # Described in 102 690 V2.1.1 Table 9.4
        # TODO: APOC_HANDLING might change at runtime
        apoc_handling = self.etsi_config.get("APOC_HANDLING", "SHALLOW")

        self.logger.debug("Check if aPoc_path: %s is in the aPoCPaths "
                          "list %s under the given "
                          "apoc_handling: %s" % (aPoC_path, aPoCPaths,
                                                 apoc_handling))

        # TS 102.921 v211 - 10.3.2.23 - 3
        aPoCPaths = self._sort_aPoCPaths(aPoCPaths)

        # check if the aPoc_path is in the aPoCPaths based on the mechanisms
        # shallow or deep
        if (apoc_handling == "SHALLOW"):
            # TODO: this does not deal with fragments / query params
            # test for 1 level deepness or exact matching in the aPoc_path
            for aPoCPath in aPoCPaths:
                path, accessRightId = self._get_path_and_accessRightID(aPoCPath)
                # in SHALLOW handling - there must be an exact match if there
                # is no slash in the end of the path
                if path[-1] != "/":
                    # check the direct match
                    if path == aPoC_path:
                        return accessRightId
                else:
                    # path endswith slash, check if it is a prefix
                    if (aPoC_path.startswith(path)):
                        # as further condition check if there is one more uri
                        # elem  as this was build per regex already just assume
                        # some more content
                        aPoC_path_tail = aPoC_path[len(path):]
                        # do we have some more content??
                        if aPoC_path_tail.split("/"):
                            return accessRightId
        elif apoc_handling == "DEEP":
            for aPoCPath in aPoCPaths:
                path, accessRightId = self._get_path_and_accessRightID(aPoCPath)
                if path == aPoC_path:
                    return accessRightId
                if path[-1] != "/":
                    path += "/"
                # in DEEP Handling there must be a match only without any post
                # conditions
                if aPoC_path.startswith(path):
                    return accessRightId

        # if this is reached, return STATUS NOT FOUND
        raise ErrorResponseConfirmation(STATUS_NOT_FOUND,
                                        self.request_indication.method,
                                        "The targetID could not be matched "
                                        "with one of the aPoCPaths elements")

    def _sort_aPoCPaths(self, aPoCPaths):
        """ Based on TS 102.921 v211 - 10.3.2.23 - 3)
        Sorts a list of aPoCPath Elements (dicts) regarding to their "path"
        length
        @param aPoCPaths: a list of (unordered) aPoCPath Elements (list of dicts)
        @return: the ordered list of of aPoCPath Elements
        """
        return sorted(aPoCPaths, key=lambda aPoCPath: len(aPoCPath.path))

    def _get_path_and_accessRightID(self, aPoCPath):
        """
        Extracts the path and the accessRightID,
        while accessRightID is optional.
        Ensures that path begins with "/"
        @param aPoCPath: aPoCPath Element (contains path and opt accessRightID)
        @return: tuple of path and accessRightID
        """
        # this is for complex aPocPath object handling
        # from the schema definition aPoCPath has at least one path and
        # optional accessRight
        path = aPoCPath.path
        accessRightId = aPoCPath.accessRightID

        if path[0] != "/":
            path = "/" + path

        return path, accessRightId

    def _check_authentication_with_accessRighID(self, accessRightID=None):
        """ Based on TS 102.921 v211 - 10.3.2.23 - 4c, 6)
        Checks the authentication of the current resource based on the
        accessRightID from the resource or from the matched aPoCPath element
        @param accessRightID: explicit accessRightID (from an aPocPath item)
        @return: promise from the check authentication - fulfilled if the
                 authentication is successful
        """
        self.logger.debug("Checking authentication of the resource with the "
                          "accessRightID: %s" % accessRightID)
        try:
            resource = self.resource
        except AttributeError:
            resource = self.parent
        return self._check_auth_based_on_access_right_id(resource,
                                                         accessRightID)

    def _retarget(self, retarget_path):
        """ Based on TS 102.921 v211 - 10.3.2.23 - 8-11) - retargets the
        requestindication (with the same body) to another address
        @param retarget_path: the path to be retargeted to
        @return: promise from send_request_indication to the retargeted address
        """

        request_indication = self.request_indication

        self.logger.debug("Retargeting to aPoc: %s %s",
                          request_indication.method,
                          retarget_path)

        method = get_request_method(request_indication.method)

        try:
            data = request_indication.resource
            content_type = request_indication.content_type
        except AttributeError:
            data = content_type = None

        request = Request(method, retarget_path, data, content_type)

        def handle_error(e):
            raise SCLBadGateway(e)

        return self.api.send_request(request) \
            .then(None, handle_error).get()

    def _set_mandatory_attributes(self, vals):
        super(ApplicationController, self)._set_mandatory_attributes(vals)

        reference_point = self.endpoint.reference_point
        if reference_point is not None:
            if self.endpoint.is_mId:
                raise SCLForbidden("Application resource cannot be created on"
                                   " mId")
        else:
            if self.config["etsi"]["scl_type"].is_nscl:
                reference_point = "mIa"
            else:
                reference_point = "dIa"
            self.logger.warn("Creating application %s on unknown reference "
                             "point. Assuming %s.", vals["appId"],
                             reference_point)

        vals["referencePoint"] = (reference_point.upper() + "_REFERENCE_POINT")
        self.fields.append("referencePoint")

    def _check_authorization(self):
        if self.request_indication.method == "create":
            return
        return super(ApplicationController, self)._check_authorization()


class SclBaseController(Controller):
    def _check_existence_create(self):
        pass

    def _get_resource_path(self):
        return "/m2m"

    def _check_authorization(self):
        if self.request_indication.method == "create":
            return

        return super(SclBaseController, self)._check_authorization()


class AccessRightController(Controller):
    def _check_authorization(self):
        if self.request_indication.method == "create":
            return super(AccessRightController, self)._check_authorization()
        return self._check_auth_based_on_self_permissions()

    def _finalize_create(self):
        self.fields.append("selfPermissions")
        return super(AccessRightController, self)._finalize_create()


class ContentInstancesController(CollectionController):
    filter_criteria = None

    __methods__ = ()

    def _check_syntax_retrieve(self):
        if self.request_indication.filterCriteria:
            self.logger.debug("Parsing filtercriteria: %s",
                              self.request_indication.filterCriteria)
            fc = self.filter_criteria = parse_filter_criteria(
                self.request_indication.filterCriteria, ContentInstance)
            pa = fc.pop("attributeAccessor", None)
            if pa and not self.request_indication.partial_accessor:
                self.request_indication.partial_accessor = pa

        return super(ContentInstancesController, self)._check_syntax_retrieve()

    def _handle_pa(self):
        partial_accessor = self.request_indication.partial_accessor
        if partial_accessor:
            pa = partial_accessor.split("/")
            if pa[0] in ("latest", "oldest"):
                self.logger.debug("Handling pa %s for %s (%s - %s)",
                                  pa[0], self.resource, self.resource.latest,
                                  self.resource.oldest)
                result = getattr(self.resource, pa[0])
                if result is None:
                    raise SCLNotFound(self.request_indication.path + "/" +
                                      partial_accessor)
                # TODO: optimize
                if len(pa) == 1:
                    self.result = result
                    return
                if len(pa) == 2 and pa[1] == "content":
                    self.result = get_decoded_content(result.content)
                    self.result_content_type = result.content.contentType
                    return
                if len(pa) == 3 and pa[1] == "content":
                    content = result.content
                    if pa[2] == "textContent":
                        text_content = content.textContent
                        if text_content is not None:
                            self.result = {"textContent": text_content}
                            return

                        ct = result.content.contentType
                        if not is_text_content(ct):
                            raise SCLNotAcceptable(ct)

                        self.result = {"textContent":
                                       b64decode(result.content.binaryContent)}
                        return
                    if pa[2] == "binaryContent":
                        result_content = content.textContent
                        if result_content is not None:
                            result_content = b64encode(
                                result.content.textContent)
                        else:
                            result_content = result.content.binaryContent
                        self.result = {"binaryContent": result_content}
                        return

            # pa, but not specially handled
            return super(ContentInstancesController, self)._prepare_resource()

    def _prepare_contentInstances(self, collection):
        if self.filter_criteria:
            collection = filter_resources(collection, self.filter_criteria)

        if self.had_filters:
            self.resource.currentNrOfInstances = len(collection)
            # TODO: push this to DB as well
            sizes = map(attrgetter("contentSize"), collection)
            self.resource.currentByteSize = reduce(int.__add__, sizes, 0)

        self.resource.contentInstanceCollection = collection

        if len(collection) == 0:
            self.resource.latest = self.resource.oldest = None
        else:
            self.resource.oldest = collection[0]
            self.resource.latest = collection[-1]

        return self._handle_pa()

    def _prepare_resource(self):
        resource = self.result = self.resource
        self.had_filters = bool(self.filter_criteria)
        collection = self.db_session.get_collection(
            ContentInstance, resource, filter_criteria=self.filter_criteria)
        self._prepare_contentInstances(collection)

    def _check_authorization(self):
        try:
            resource = self.parent
        except AttributeError:
            # non-create case
            resource = self.db_session.get(self.resource.parent_path)
            return self._check_auth_based_on_access_right_id(resource)
        else:
            # create case
            return self._check_auth_based_on_access_right_id(resource)

    def _delete_children(self):
        return self.db_session.delete_children(ContentInstance, self.resource)


class ContentInstanceController(Controller):
    __methods__ = (RequestIndicationMethod.delete,
                   RequestIndicationMethod.create)

    _handle_notify = Controller._handle_create

    def _prepare_resource(self):
        partial_accessor = self.request_indication.partial_accessor
        if partial_accessor:
            if partial_accessor == "content":
                self.result = get_decoded_content(self.resource.content)
                self.result_content_type = self.resource.content["contentType"]
                return
            pa = partial_accessor.split("/")
            if len(pa) == 2 and pa[0] == "content":
                if pa[1] == "textContent":
                    try:
                        self.result = {"textContent":
                                       self.resource.content["textContent"]}
                        return
                    except KeyError:
                        pass

                    ct = self.resource.content["contentType"]
                    if not is_text_content(ct):
                        raise SCLNotAcceptable(ct)

                    try:
                        content = self.resource.content["binaryContent"]
                    except KeyError:
                        content = self.resource.content["$t"]

                    self.result = {"textContent": b64decode(content)}
                    return
                if pa[1] == "binaryContent":
                    try:
                        text_content = self.resource.content["textContent"]
                        content = b64encode(text_content)
                    except KeyError:
                        try:
                            content = self.resource.content["binaryContent"]
                        except KeyError:
                            content = self.resource.content["$t"]
                    self.result = {"binaryContent": content}
                    return

                    # pa, but not specially handled
        return super(ContentInstanceController, self)._prepare_resource()

    def _check_authorization(self):
        try:
            parent = self.parent
        except AttributeError:
            # non-create case
            content_instances = self.db_session.get(self.resource.parent_path)
            self.parent = content_instances
            container = self.db_session.get(content_instances.parent_path)
            return self._check_auth_based_on_access_right_id(container)
        else:
            # create case
            container = self.db_session.get(parent.parent_path)
            return self._check_auth_based_on_access_right_id(container)

    def _check_content_1(self, content):
        self.logger.debug("_check_content_1 %s", content)
        try:
            c = content["binaryContent"] = content.pop("$t")
            return c
        except KeyError as e:
            if self._etsi_compatibility_2:
                try:
                    return content["binaryContent"]
                except KeyError:
                    try:
                        text_content = content.pop("textContent")
                    except KeyError:
                        pass
                    else:
                        c = content["binaryContent"] = b64encode(text_content)
                        content.setdefault("contentType", "text/plain")
                        return c
            raise SCLMissingValue("content/%s" % (e, ))

    def _check_content_2(self, content):
        self.logger.debug("_check_content_2 %s", content)
        try:
            c = content["textContent"]
            content.setdefault("contentType", "text/plain")
            return c
        except KeyError:
            try:
                return content["binaryContent"]
            except KeyError:
                if self._etsi_compatibility_1:
                    try:
                        c = content["binaryContent"] = content.pop("$t")
                        return c
                    except KeyError:
                        pass
                raise SCLMissingValue("Either content/textContent or "
                                      "content/binaryContent must be present")

    def _check_create_representation(self):
        self.logger.debug("_check_create_representation")
        if self.request_indication.content_type:
            return

        try:
            content = self.request_indication.resource["content"]
        except KeyError:
            raise SCLMissingValue("content")

        try:
            if self._etsi_version_1:
                self.content = self._check_content_1(content)
            else:
                self.content = self._check_content_2(content)
        except (AttributeError, TypeError):
            raise SCLTypeError("Illegal value for 'content': %s" % (content, ))

        if not len(unicode(content.get("contentType", ""))):
            raise SCLMissingValue("content/contentType")

        return super(ContentInstanceController, self) \
            ._check_create_representation()

    def _set_mandatory_attributes(self, vals):
        super(ContentInstanceController, self)._set_mandatory_attributes(vals)
        content = vals["content"]
        vals["contentTypes"] = (content["contentType"],)
        vals["contentSize"] = len(self.content)

    def _get_container(self):
        self.container = self.db_session.get(self.parent.parent_path)

    def _handle_old_instances(self):
        max_nr_of_instances = self.container.maxNrOfInstances
        current_nr_of_instances = self.parent.currentNrOfInstances
        if 0 < max_nr_of_instances <= current_nr_of_instances:
            self.parent_fields.add("oldest")
            self.parent.currentNrOfInstances -= 1
            self.parent.currentByteSize -= self.parent.oldest.contentSize

            self.db_session.delete(self.parent.oldest)

            if self.parent.currentNrOfInstances >= 1:
                oldest = self.db_session.get_oldest_content_instance(self.parent)
                self.logger.debug("Setting new oldest: %s", oldest)
                self.parent.oldest = oldest
            else:
                self.logger.debug("Setting oldest to None")
                self.parent.oldest = None

    def _handle_new_instance(self):
        self.parent.currentNrOfInstances += 1
        self.parent.currentByteSize += self.resource.contentSize
        if self.parent.oldest is None:
            self.logger.debug("Setting new resource as oldest: %s",
                              self.resource)
            self.parent.oldest = self.resource
            self.parent_fields.add("oldest")
        self.parent.latest = self.resource
        self.db_session.update(self.parent, self.parent_fields)

    def _create_resource(self):
        self.parent_fields = {"currentNrOfInstances",
                              "currentByteSize", "latest"}

        content_type = self.request_indication.content_type
        if content_type:
            if (self._etsi_compatibility_1 or self._etsi_version_1 or
                    not is_text_content(content_type)):
                binary_content = self.content = b64encode(
                    self.request_indication.resource)
                content = {
                    "binaryContent": binary_content,
                    "contentType": content_type
                }
            else:
                text_content = self.content = self.request_indication.resource
                content = {
                    "textContent": text_content,
                    "contentType": content_type
                }

            self.request_indication.resource = {
                "content": content
            }

        super(ContentInstanceController, self)._create_resource()
        self._get_container()
        self._handle_old_instances()
        self._handle_new_instance()

    def _finalize_create(self):
        self.parent.latest = self.parent.oldest = None
        return super(ContentInstanceController, self)._finalize_create()

    def _delete_resource(self):
        self.parent.currentNrOfInstances -= 1
        self.parent.currentByteSize -= self.resource.contentSize
        fields = ["currentNrOfInstances", "currentByteSize"]
        if self.parent.currentNrOfInstances == 0:
            self.parent.latest = self.parent.oldest = None
            fields += ["latest", "oldest"]
        elif self.resource == self.parent.oldest:
            fields.append("oldest")

            super(ContentInstanceController, self)._delete_resource()
            oldest = self.db_session.get_oldest_content_instance(self.parent)
            self.parent.oldest = oldest
            return self.db_session.update(self.parent, fields=fields)
        elif self.resource == self.parent.latest:
            fields.append("latest")
            super(ContentInstanceController, self)._delete_resource()
            latest = self.db_session.get_latest_contentinstance(self.parent)
            self.parent.latest = latest
            return self.db_session.update(self.parent, fields=fields)

        self.db_session.update(self.parent, fields=fields)
        super(ContentInstanceController, self)._delete_resource()


class NotificationChannelController(Controller):
    def _check_create_representation(self):
        super(NotificationChannelController, self) \
            ._check_create_representation()

        channel_type = self.request_indication.resource["channelType"]
        channel_type = channel_type.upper()

        valid_channel_types = ("LONG_POLLING",)

        if channel_type not in valid_channel_types:
            raise SCLValueError("Invalid channelType: %s. Must be one of %s" %
                                (channel_type, valid_channel_types))

        self.request_indication.resource["channelType"] = channel_type

    def _set_mandatory_attributes(self, vals):
        super(NotificationChannelController, self) \
            ._set_mandatory_attributes(vals)

        channel_id = uri_safe(self._get_resource_path())

        vals["contactURI"] = "nc:///%s" % (channel_id, )

        if (self.etsi_config.get("notificationChannel_relative_contactURI") or
                self.endpoint.base_uri is None):
            base_uri = "/"
        else:
            base_uri = self.endpoint.base_uri
            if base_uri[-1] != "/":
                base_uri += "/"

        vals["channelData"] = {"longPollingURI": "%snc/%s" % (base_uri,
                                                              channel_id)}

        self.fields.extend(("contactURI", "channelData"))


class AnnouncementController(Controller):
    def _send_create_response(self):
        self.fields.append("link")
        return super(AnnouncementController, self)._send_create_response()

    # TODO(rst): this is not standard conform but it is more logical
    def _check_authorization(self):
        if (self.request_indication.method == "create" and
                self.parent.typename == 'applications'):
            return

        return super(AnnouncementController, self)._check_authorization()


class GroupController(Controller):
    def _send_create_response(self):
        self.fields.append("maxNrOfMembers")
        self.fields.append("consistencyStrategy")
        return super(GroupController, self)._send_create_response()

    def _check_create_representation(self):
        super(GroupController, self)._check_create_representation()
        member_type = self.request_indication.resource["memberType"]
        return self._check_group_members(member_type)

    def _check_update_representation(self):
        super(GroupController, self)._check_update_representation()

        if ("maxNrOfMembers" in self.request_indication.resource and
                "members" not in self.request_indication.resource):
            max_mem = int(self.request_indication.resource["maxNrOfMembers"])
            cur_mem = self.resource.currentNrOfMembers

            if 0 <= max_mem < cur_mem:
                # reject with STATUS_FORBIDDEN
                raise SCLPermissionDenied(
                    "currentNrOfMembers (%s) is larger than "
                    "maxNrOfMembers (%s)" % (cur_mem, max_mem))

        return self._check_group_members(self.resource.memberType, create=False)

    def _check_group_members(self, member_type, create=True):
        try:
            wrapper = self.request_indication.resource["members"]
        except (TypeError, AttributeError, KeyError):
            wrapper = {}
        try:
            if len(wrapper) > 1:
                raise SCLValueError(
                    "Illegal value for members: %s" % (wrapper, ))
            members = self.members = wrapper.values()[0]
            members = list(set(members))
        except (TypeError, AttributeError):
            raise SCLTypeError("Illegal value for members: %s" % (wrapper, ))
        except (KeyError, IndexError):
            members = ()

        self.members = members
        self.request_indication.resource["members"] = {"reference": members}

        try:
            max_mem = self.request_indication.resource["maxNrOfMembers"]
        except KeyError:
            self.request_indication.resource["maxNrOfMembers"] = max_mem = -1
        try:
            max_mem = int(max_mem)
            if 0 <= max_mem < len(members):
                # reject with STATUS_FORBIDDEN
                raise SCLPermissionDenied(
                    "currentNrOfMembers (%s) is larger than "
                    "maxNrOfMembers (%s)" % (len(members), max_mem))
        except (TypeError, ValueError):
            raise SCLValueError("Illegal value for maxNrOfMembers: %s",
                                max_mem)

        path_list = []
        for member in members:
            if self.api.is_local_path_sync(member):
                path_list.append(member)
            else:
                # FIXME (ren) I decided to not allow external paths for now,
                # FIXME since it blows up MembersContentController for now
                self.logger.warn("possible remote path gets removed")
                members.remove(member)

        if path_list:
            self._does_it_exist(path_list)
        # !memberType (provided by request)
        if not self._is_valid_member_type(member_type):
            raise SCLValueError("%s is not a valid member type" %
                                (member_type, ))

        # check each member's memberType if group's memberType is not MIXED
        if member_type != "MIXED":
            self._check_members_types(member_type, path_list, create=create)

    def _set_mandatory_attributes(self, vals):
        super(GroupController, self)._set_mandatory_attributes(vals)

        # announceTo -> done by parent
        # activated
        # sclList
        # consistencyStrategy : ABANDON_MEMBER (default) | ABANDON_GROUP |
        #                       MODIFY_TYPE

        vals.setdefault("consistencyStrategy", "ABANDON_MEMBER")
        # creationTime: self.now -> done by parent

        # memberTypeValidated -> True if each member's memberType equals
        # group's memberType
        vals.setdefault("memberTypeValidated", False)

        # currentNrOfMembers
        l = vals["currentNrOfMembers"] = len(self.members)
        if not l:
            vals["memberTypeValidated"] = True
        # id -> done by parent?
        # lastModifiedTime: self.now -> done by parent
        # maxNrOfMembers: -1
        vals.setdefault("maxNrOfMembers", -1)

        # members
        # membersContentReference -> done by parent

    def _does_it_exist(self, path_list):
        self.logger.debug("Check path existence for: %s", path_list)

        def yield_exists():
            for p in path_list:
                yield self.db_session.exists(None, {"path": p})

        strat = self.request_indication.resource["consistencyStrategy"]
        if strat == "ABANDON_MEMBER":
            members = self.members
            for i, exists in enumerate(yield_exists()):
                if not exists:
                    members.remove(path_list[i])
            return

        if strat == "MODIFY_TYPE":
            for exists in yield_exists():
                if not exists:
                    self.request_indication.resource["memberType"] = "MIXED"
                    return
            return

        for i, exists in enumerate(yield_exists()):
            if not exists:
                raise SCLNotFound("%s does not exist "
                                  "(consistencyStrategy = %s)" %
                                  (path_list[i], strat))

    def _check_members_types(self, member_type, path_list, create):
        self.logger.debug("checking members: %s", path_list)

        results = [self.db_session.get(path)
                   for path in path_list]
        for i, result in enumerate(results):
            typename = str(result.get_typename()).upper()
            self.logger.debug("get of %s returned: %s", path_list[i],
                              typename)

            self.logger.debug("comparing %s with %s", typename, member_type)

            try:
                if not self._is_valid_member_type(typename):
                    raise SCLValueError("%s is not a valid member type" %
                                        (typename, ))
                # check if typename equals memberType without underscore
                elif typename != str(member_type).translate(None, '_'):
                    raise SCLValueError("typename (%s) differs from group "
                                        "memberType [w/o underscore] (%s)" %
                                        (typename, member_type))
            except SCLValueError:
                if "consistencyStrategy" in self.request_indication.resource:
                    strat = self.request_indication.resource[
                        "consistencyStrategy"]
                    if strat == "ABANDON_MEMBER":
                        self.members.remove(path_list[i])
                    elif strat == "MODIFY_TYPE":
                        self.request_indication.resource["memberType"] = "MIXED"
                    else:  # strat == "ABANDON_GROUP"
                        if create:
                            raise
                        self._handle_request_indication(
                            DeleteRequestIndication(self.resource.path))
                        break

            self.request_indication.resource["memberTypeValidated"] = True

    @staticmethod
    def _is_valid_member_type(resource_type):
        types = ["APPLICATION", "CONTAINER", "ACCESS_RIGHT", "SCL", "SCL_BASE",
                 "LOCATION_CONTAINER", "MGMT_OBJ", "MGMT_CMD",
                 "ATTACHED_DEVICE", "MIXED"]

        # TODO: move to model (enum)
        return resource_type in types


class MembersContentController(Controller):
    def _get_group(self):
        """Sets self.group
        :return: promise
        """

        self.logger.debug("getting group path from: %s",
                          self.request_indication.path)
        group_path = str(self.request_indication.path).rpartition("/")[0]
        self.logger.debug("group path: %s", group_path)

        result = self.db_session.get(group_path)
        self.logger.debug("result: %s", result)
        self.logger.debug("result keys: %s", result.__dict__.keys())

        # this is the parent group
        self.group = self.parent = result

    def _handle_request(self):
        self._get_group()
        members = list(self.group.members)

        pa = self.request_indication.partial_accessor
        self.result = MembersContent()

        if pa:
            self.logger.debug("Found partial accessor: %s", pa)
            # add suffix of request (e.g. .../membersContent/containers to
            # member paths
            suffix = "/" + pa
            members = [member + suffix for member in self.members]

            self.logger.debug("updated member paths: %s", members)

        self.members = members

        return super(MembersContentController, self)._handle_request()

    def _handle_delete(self):
        self._check_syntax_delete()
        self._check_authorization()
        self._delete_resource()
        return self._send_delete_response()

    def _handle_create(self):
        self.parent = self.resource
        del self.resource

        self.now = datetime_now()
        self.fields = []

        self._check_syntax_create()
        self._check_create_representation()
        self._check_authorization()
        self._create_resource()
        return self._send_create_response()

    def _handle_update(self):
        self.now = datetime_now()

        # return self._check_syntax_update() \
        # .then(self._check_update_representation) \
        # .then(self._check_authorization) \
        # .then(self._update_resource) \
        # .then(self._send_update_response)

        self._check_syntax_update()
        self._check_authorization()
        self._update_resource()
        return self._send_update_response()

    # RETRIEVE
    def _prepare_resource(self):
        members = self.members

        def _handle_results(results):
            result = self.result
            for j, r in enumerate(results):
                self.logger.debug("RETRIEVE: _handle_request_indication of %s "
                                  "returned: %s, with keys %s", members[j], r,
                                  r.__dict__.keys())

                r.id = members[j]
                try:
                    r.lastModifiedTime = r.resource.lastModifiedTime
                except AttributeError:
                    pass
                result.membersContentResponses.append(r)

        return async_all(
            [self._handle_request_indication(RetrieveRequestIndication(m))
             for m in members]).then(_handle_results).get()

    # CREATE
    def _create_resource(self):
        pa = self.request_indication.partial_accessor
        self.resource = self.result = MembersContent()

        if pa:
            self.logger.debug("CREATE: Found partial accessor: %s", pa)

            # validate suffix type
            if self.group.memberType != "MIXED":
                self.logger.debug("CREATE: Trying to validate suffix")

                # create type checklist
                # e.g. if membersContent/containers/subscriptions and
                # group.memberType = APPLICATION
                # -> APPLICATION/CONTAINERS/SUBSCRIPTIONS
                translated = str(self.group.memberType).translate(None, '_')
                checklist = [translated] + pa.split("/")

                # validate the list
                self._validate_checklist(checklist)

            # add suffix of request (e.g. .../membersContent/containers to
            # member paths

            pa_last = pa.split("/")[-1:][0]
            self.logger.debug("PA: pa_last: %s, pa: %s", pa_last, pa)

            if pa_last == "subscriptions":
                self._handle_subscription()

        members = self.members

        def p_handler(results):
            result = self.result
            for j, r in enumerate(results):
                self.logger.debug("CREATE: _handle_request_indication of %s "
                                  "returned: %s, with keys %s", members[j], r,
                                  r.__dict__.keys())

                r.id = members[j]
                # FIXME: this "now" is not exact. get the real value
                r.lastModifiedTime = self.now
                result.membersContentResponses.append(r)

        resource = self.request_indication.resource

        try:
            resource = resource.read()
        except AttributeError:
            pass

        self.logger.debug("VV: resource: %s", resource)

        create_promises = [
            self._handle_request_indication(
                CreateRequestIndication(
                    path,
                    resource=copy(resource),
                    content_type=self.request_indication.content_type,
                    typename=self.request_indication.typename
                )
            )
            for path in members]
        return async_all(create_promises).then(p_handler).get()

    # UPDATE
    def _update_resource(self):
        pa = self.request_indication.partial_accessor
        members = self.members

        if pa:
            self.logger.debug("UPDATE: Found partial accessor: %s", pa)

            # validate suffix type
            if self.group.memberType != "MIXED":
                self.logger.debug("UPDATE: Trying to validate suffix")

                # create type checklist
                # e.g. if membersContent/containers/subscriptions and
                # group.memberType = APPLICATION
                # -> APPLICATION/CONTAINERS/SUBSCRIPTIONS
                translated = str(self.group.memberType).translate(None, '_')
                checklist = [translated] + pa.split("/")

                # validate the list
                self._validate_checklist(checklist)

            pa_last = pa.split("/")[-1:]

            if pa_last == "subscriptions":
                self._handle_subscription()

        # FIXME: this "now" is not exact. get the real value
        now = datetime_now()

        def p_handler(results):
            result = self.result
            for j, r in enumerate(results):
                self.logger.debug("UPDATE: _handle_request_indication of %s "
                                  "returned: %s, with keys %s", members[j], r,
                                  r.__dict__.keys())

                r.id = members[j]
                r.lastModifiedTime = now
                result.membersContentResponses.append(r)

        resource = self.request_indication.resource

        try:
            resource = resource.read()
        except AttributeError:
            pass

        update_promises = [self._handle_request_indication(
            UpdateRequestIndication(
                path, resource,
                content_type=self.request_indication.content_type
            )
        ) for path in members]
        return async_all(update_promises).then(p_handler).get()

    # DELETE
    def _delete_resource(self):
        pa = self.request_indication.partial_accessor
        members = self.members

        if pa:
            self.logger.debug("DELETE: Found partial accessor: %s", pa)

            # validate suffix type
            if self.group.memberType != "MIXED":
                self.logger.debug("DELETE: Trying to validate suffix")

                # create type checklist
                # e.g. if membersContent/containers/subscriptions and
                # group.memberType = APPLICATION
                # -> APPLICATION/CONTAINERS/SUBSCRIPTIONS
                checklist = ([str(self.group.memberType).translate(None, '_')] +
                             pa.split("/"))

                # validate the list
                self._validate_checklist(checklist)

            pa_last = pa.split("/")[-1:]

            if pa_last == "subscriptions":
                self._handle_subscription()
                pass

        def p_handler(results):
            group_path = str(self.request_indication.path).rpartition("/")[0]
            resource = Group()
            t_members = members
            result = self.result
            for j, r in enumerate(results):
                self.logger.debug("DELETE: _handle_request_indication of %s "
                                  "returned: %s, with keys %s",
                                  members[j], r, r.__dict__.keys())
                result.membersContentResponses.append(r)
                if r.statusCode == STATUS_OK:
                    t_members.remove(members[j])

            # FIXME: this breaks with PA
            resource.members = t_members
            self.logger.debug("UPDATING GROUP MEMBERS TO: %s", t_members)
            upd_req = UpdateRequestIndication(group_path, resource)
            return self._handle_request_indication(upd_req)

        delete_promises = [
            self._handle_request_indication(DeleteRequestIndication(path)) for
            path in members]
        return async_all(delete_promises).then(p_handler).get()

    def _validate_checklist(self, checklist):
        """Validates a checklist of types by checking if each item in the list
        is a possible parent of the next item

        :param checklist: list containing types, e.g. [application, containers,
                          subscriptions]
        :raise SCLBadRequest: if checklist[k+1] is not attribute of
                              checklist[k], or type could not be found
        """
        validated = False

        # openmtc.model has all types as classes
        types = get_etsi_types()

        self.logger.debug("checklist: %s", checklist)

        k = 0
        # iterate through checklist
        # for k, checklist_item in enumerate(checklist[:-1]):
        while (k + 1) < len(checklist):

            for c_type in types:
                typename = str(c_type.get_typename()).upper()
                # type matches checklist item
                if checklist[k].upper() == typename:
                    self.logger.debug("Found type matching checklist element: "
                                      "%s", typename)
                    # next checklist item is attribute of current item
                    if hasattr(c_type, checklist[k + 1]):
                        self.logger.debug("Type %s has attribute %s", typename,
                                          checklist[k + 1])
                        validated = True
                        break
                    else:
                        self.logger.debug("Type %s does not have attribute %s",
                                          typename, checklist[k + 1])

            if not validated:
                raise SCLBadRequest(
                    "Type %s does not not have attribute %s, or type was not "
                    "found" % (checklist[k], checklist[k + 1]))

            k += 1

    def _handle_subscription(self):
        # set custom aggregateURI from which you can extract the original
        # aggregateURI

        self.logger.debug("request_indication type: %s",
                          type(self.request_indication.resource))

        ct = self.request_indication.content_type
        if ct:
            serializer = get_serializer(ct)

            resource = self.request_indication.resource
            typename, resource = serializer.decode(resource)

            self.request_indication.resource = resource
            self.request_indication.typename = typename
            self.request_indication.content_type = None

            self.logger.debug("decoded resource: %s - %s", resource, typename)

        aggregate_uri = None
        try:
            aggregate_uri = self.request_indication.resource["aggregateURI"]
        except TypeError:
            self.logger.debug("subscription has no aggregateURI")

        if aggregate_uri is not None:

            self.logger.debug("aggregateURI: %s, len: %s", aggregate_uri,
                              len(aggregate_uri))
            if len(aggregate_uri) == 0:
                contact = ("aggregate:///" +
                           self.request_indication.resource["contact"])
                self.request_indication.resource["contact"] = contact
            else:
                self.request_indication.resource[
                    "contact"] = "aggregate:///" + aggregate_uri

                # old version, handled by methoddomain
                # if len(aggregate_uri) == 0:
                #     self.request_indication.resource["contact"] = (
                #         self.global_config.get("scl_base") + "/aggregate" +
                #         self.request_indication.resource["contact"])
                # else:
                #     self.request_indication.resource["contact"] = (
                #         self.global_config.get("scl_base") + "/aggregate" +
                #         aggregate_uri)

    def _check_create_representation(self):
        return


class DiscoveryController(Controller):
    filter_criteria = None
    discover_content_instance_resources = False
    max_size = None

    def _check_syntax_retrieve(self):
        if self.request_indication.filterCriteria:
            self.filter_criteria = parse_filter_criteria(
                self.request_indication.filterCriteria, ContentInstance)

        if self.request_indication.maxSize:
            try:
                ms = self.max_size = int(self.request_indication.maxSize)
            except (TypeError, ValueError):
                raise SCLBadRequest("Illegal value for maxSize: '%s'" %
                                    self.request_indication.maxSize)

            if ms <= 0:
                raise SCLValueError("maxSize must greater zero")

        return super(DiscoveryController, self)._check_syntax_retrieve()

    def _prepare_resource(self):
        prefix = self.request_indication.searchPrefix or "/m2m"

        resource = self.db_session.get(prefix)
        self.logger.debug("_prepare_resource -> _handle_result: %s", resource)

        self.resource = resource

        discovered = self.discovered = []

        self.result = Discovery(discoveryURI=discovered)
        self.logger.debug("isinstance(%s, %s)? -> %s", resource,
                          ContentInstance,
                          isinstance(resource, ContentInstance))

        if not isinstance(resource, ContentInstance):
            return self._discovery()

    def _discovery(self):
        if isinstance(self.resource, ContentInstances):
            # ContentInstance discovery was explicitly requested
            self.discover_content_instance_resources = True
        elif self.filter_criteria:
            # Only include content instance resources in result if specifically
            # We assume that it is requested when contentInstance
            # filterCriteria are given
            for k in ("metaDataOnly", "sizeFrom", "sizeUntil", "contentType"):
                if k in self.filter_criteria:
                    self.discover_content_instance_resources = True
                    break
            else:
                partial_accessor = self.filter_criteria.get("partialAccessor")
                if partial_accessor is not None:
                    # check if partialAccessor pertains to attrs exclusively
                    # found on contentInstance resources
                    ci_exclusives = ("contentTypes", "contentSize",
                                     "content", "href")
                    if partial_accessor.split("/", 1)[0] in ci_exclusives:
                        self.discover_content_instance_resources = True

        try:
            return self._do_discovery(self.resource)
        except Exception as error:
            self.logger.exception("Error during discovery")
            raise SCLError("Error during discovery: %r" % error)

    def _check_auth_for_discovery(self, resource):
        if isinstance(resource, ContentInstance):
            return

        if isinstance(resource, AccessRight):
            checker = self._check_auth_based_on_self_permissions
        elif hasattr(resource, "accessRightID"):
            checker = self._check_auth_based_on_access_right_id
        else:
            checker = self._check_auth_based_on_default_access_rights

        try:
            checker(resource)
            return resource
        except SCLError as exc:
            if exc.statusCode == STATUS_PERMISSION_DENIED:
                return resource
            if exc.statusCode != STATUS_NOT_FOUND:
                raise

    def _do_discovery(self, node):
        self.logger.debug("_do_discovery: %s", node)
        self.logger.debug("discover content instance resource? -> %s",
                          self.discover_content_instance_resources)
        self.logger.debug("isinstance(node, ContentInstances)? -> %s",
                          isinstance(node, ContentInstances))
        if (not self.discover_content_instance_resources and
                isinstance(node, ContentInstances)):
            self.logger.debug("returning")
            return

        self.logger.debug("_do_discovery after check: %s", node)

        include_results = ((not self.discover_content_instance_resources) or
                           isinstance(node, ContentInstances))
        max_size = self.max_size

        def _check_subresources(resource=None):
            resource = resource or node

            self.logger.debug("_check_subresources: %s", resource)
            self.logger.debug("tuncated?: %s", self.result.truncated)

            if not self.result.truncated:
                self.logger.debug("subresources: %s", resource.subresources)
                for s in resource.subresources:
                    if not s.virtual:
                        # TODO: parrallel
                        s = self.db_session.get(resource.path + "/" + s.name)
                        self._do_discovery(s)

        def _check_collection(collection):
            if include_results and self.filter_criteria:
                candidates = filter_resources(collection, self.filter_criteria)
            else:
                candidates = collection

            def _check_collection_subresources(target_collection):
                self.api.map(_check_subresources, target_collection)

            def _handle_permission_results(result):
                if self.result.truncated:
                    return

                # filter out all with no discovery permissions
                result = filter(None, result)

                if include_results:
                    if max_size:
                        max_results = max_size - self.result.matchSize
                        if max_results < len(result):
                            result = result[:max_results]
                            self.result.truncated = True

                    self.result.matchSize += len(result)
                    if result:
                        if isinstance(result[0], AnnouncementResource):
                            attr = "link"
                        else:
                            attr = "path"
                        self.discovered.extend(map(attrgetter(attr), result))

                    if self.result.truncated:
                        return

                # TODO(rst): investigate why this was in
                # with it inside no subcontainers will be considered if the
                # container was filtered out
                # if isinstance(node, Containers):
                #     _check_collection_subresources(result)
                # else:
                _check_collection_subresources(collection)

            if isinstance(node, ContentInstances):
                return _handle_permission_results(candidates)

            permission_results = self.api.map(self._check_auth_for_discovery,
                                              candidates)
            _handle_permission_results(permission_results)

        self._do_fill_collections(node)

        self.api.map(_check_collection,
                     [getattr(node, c.name) for c in node.collections])

        _check_subresources()

    def _check_authorization(self):
        pass


class SclController(Controller):
    def _check_create_representation(self):
        scl_type = self.request_indication.resource.get("sclType")
        if not scl_type:
            if self.config["etsi"]["scl_type"].is_nscl:
                self.request_indication.resource["sclType"] = "GSCL"
            else:
                self.request_indication.resource["sclType"] = "NSCL"

        super(SclController, self)._check_create_representation()
        # link = self.request_indication.resource["link"]
        # scl_type = self.request_indication.resource["sclType"]
        # 2) "Check existence of the addressed resource":
        # checkSclId
        scl_id = self.request_indication.resource["sclId"]
        path = self.request_indication.path + "/" + scl_id

        # TODO: kca: check for sclID only (not yet supported by the DB layer)
        fields = {"path": path}

        if self.db_session.exists(Scl, fields):
            raise SCLConflict("Scl already exists: %s." % (path, ))

    def _check_authorization(self):
        if self.request_indication.method == "create":
            return
        return super(SclController, self)._check_authorization()

    # 3) Primitive specific operations: The hosting SCL may reject the
    # request based on policies, which are not described in the present
    # document. If the hosting SCL decides not to accept the request the
    # request shall be rejected with a STATUS_PERMISSION_DENIED.
    # TODO
    # 4) "Check the syntax of received message".
    # TODO
    # 6) Primitive specific operation: The receiver shall execute the
    # following steps in order for integrity validation:
    # TODO
    # a) If IVal is supported by the receiver SCL and the issuer SCL is IVal
    # capable according to the information received during (clause 6) and
    # IntegrityValResults are not included in the CREATE primitive, the
    # hosting SCL shall reject the request with a STATUS_BAD_REQUEST.

    # b) If IVal is supported by the receiver and the issuer is not IVal
    # capable and IntegrityValResults are included in the CREATE primitive
    # the hosting SCL shall reject the request with a STATUS_BAD_REQUEST.

    # c) If IVal is supported by the receiver and the issuer is IVal Capable
    # and IntegrityValResults are included in the CREATE primitive:

    # i) The Ival key provided in the security attributes is used to validate
    # the IntegrityValResults object. If the IntegrityValResults object is
    # invalid , the receiver shall reject the request with a
    # STATUS_BAD_REQUEST.

    # ii) If the IntegrityValResults object is valid, the receiver shall use
    # the integrity results therein to make a policy based access control
    # decision.

    # iii) If the result of the policy is to deny access, the receiver shall
    # reject the request with a STATUS_FORBIDDEN.

    # d) If IVal is not supported by the receiver, or if IVal is supported by
    # the receiver and the result of the policy is to allow access, then
    # continue with following steps.

    def _set_mandatory_attributes(self, vals):
        super(SclController, self)._set_mandatory_attributes(vals)

        parsed_url = urlparse(vals.get("link", ""))
        if not parsed_url.netloc:
            raise SCLBadRequest("link is not an absolute URI: %s" %
                                parsed_url.geturl())
        if not parsed_url.scheme:
            vals['link'] = parsed_url._replace(scheme='http').geturl()

    #     if "sclId" not in vals:
    #     vals["sclId"] = self._create_id("scl")
    #
    #     # expirationTime should be set for most resources ...
    #     from openmtc.util import the_future
    #     OFFSET = 3600000
    #     # if "expirationTime" not in vals or not vals["expirationTime"]:
    #     #     vals["expirationTime"] = the_future(OFFSET)
    #     #     # TODO expirationTime handling
    #
    #     # When hosted in an NSCL the <scl> resource shall contain the
    #     # following sub-resources and attributes.
    #     # TODO
    #
    #     # When hosted by a D- or GSCL, the <scl> resource shall contain the
    #     # following sub-resources and attributes.
    #     defaults = (
    #         ( "expirationTime", the_future(OFFSET)),
    #         ( "pocs", { "reference": []}),
    #         ( "onlineStatus", "ONLINE"),
    #         ( "serverCapability", True),
    #     )
    #     for k, v in defaults:
    #         if not k in vals or not vals[k]:
    #             vals[k] = v

    # def _handle_update(self):
    #     # TODO
    #     fields = self.request_indication.fields
    #     internal_fields = []
    #     member_names = [ m.name for m in Scl.members ]
    #     for f in fields:
    #         if f not in member_names and f.endswith( "Reference"):
    #             internal_fields.append(f.replace("Reference", ""))
    #         else:
    #             internal_fields.append(f)
    #
    #     resource = self.request_indication.resource
    #     self.resource.set_values( resource)
    #
    #     return self.db_session.update(self.resource, fields=internal_fields)


class SubscriptionController(Controller):
    def _check_authorization(self):
        # TODO(rst): from the standard 10.25.2.2
        # 4) Primitive specific operation: The hosting SCL shall check if the
        # requestingEntity has READ permission on the parent resource of the
        # addressed subscriptions collection resource. If it does not have READ
        # permission the request shall be rejected with
        # STATUS_PERMISSION_DENIED.
        return

    def _check_create_representation(self):
        super(SubscriptionController, self)._check_create_representation()

        # TODO: check relative paths for validity?
        # contact = self.request_indication.resource["contact"]
        # try:
        #     parsed = urlparse(contact)
        # except Exception:
        #     raise SCLValueError("Illegal contact URI: %s" % (contact, ))
        # if not parsed.scheme:
        #     raise SCLValueError("Illegal contact URI: %s" % (contact, ))

        fc = self.request_indication.resource.get("filterCriteria")
        if fc:
            parse_filter_criteria(fc, ContentInstance, True)
        else:
            self.request_indication.resource.pop("filterCriteria", None)

    def _set_mandatory_attributes(self, vals):
        super(SubscriptionController, self)._set_mandatory_attributes(vals)
        try:
            fc = vals["filterCriteria"]
        except KeyError:
            pass
        else:
            # Interestingly enough, "attributeAccessor" is mandatory in
            # filterCritera (see table 11.23 in TS102.921 and XSDs).
            # It can be empty though.
            fc.setdefault("attributeAccessor", "")

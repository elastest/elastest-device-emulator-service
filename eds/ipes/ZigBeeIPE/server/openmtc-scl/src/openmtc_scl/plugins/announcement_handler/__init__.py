from collections import namedtuple
from copy import deepcopy
from re import sub
from urlparse import urlparse
from aplus import Promise

from openmtc_etsi.exc import SCLError
from openmtc_etsi.model import (AnnounceableResource, Scl, SclBase,
                                AnnouncementResource, AnnounceTo)
from openmtc_etsi.model import get_etsi_type as get_resource_type
from openmtc_etsi.scl import (RetrieveRequestIndication,
                              CreateRequestIndication, DeleteRequestIndication,
                              UpdateRequestIndication)
from openmtc_server.Plugin import Plugin
from openmtc_server.transportdomain import ErrorResponse
from openmtc_server.util.async import async_all

# url join with coap compatibility
from urlparse import urljoin, uses_relative, uses_netloc
from re import compile

import openmtc_scl.api

uses_relative.append('coap')
uses_netloc.append('coap')

# annc result
AnncResult = namedtuple('AnncResult', ['scl_uri', 'res_con'])

# create annc target parents
_annc_regex = compile(r'Annc$')
_special_parent_map = {}

def look_for_annc_parents(model):
    for subresource in model.subresources:
        if subresource.name == 'subcontainers':
            continue
        look_for_annc_parents(subresource.type)
    for collection in model.collections:
        if issubclass(collection.content_type, AnnouncementResource):
            res_name = _annc_regex.sub('', collection.content_type.typename)
            _special_parent_map[res_name] = model.typename
        look_for_annc_parents(collection.content_type)

look_for_annc_parents(SclBase)


class AnnouncementHandler(Plugin):
    # method constants
    _CREATE = 'create'
    _UPDATE = 'update'
    _DELETE = 'delete'

    def __init__(self, api, config, *args, **kw):
        super(AnnouncementHandler, self).__init__(api, config, *args, **kw)
        self._announcements = {}
        self._pending_operations = {}
        self.scl_id = openmtc_scl.api.config["etsi"]["scl_id"]
        self._scl_base = urlparse(
            "/" + openmtc_scl.api.config['etsi']['scl_base']).path
        self._scl_links = {}

    def _init(self):
        # subscribe for announceable resources
        self.events.resource_created.register_handler(self._update_annc_create,
                                                      AnnounceableResource)
        self.events.resource_updated.register_handler(self._update_annc_update,
                                                      AnnounceableResource)
        self.events.resource_deleted.register_handler(self._delete_annc,
                                                      AnnounceableResource)

        # We keep track of the SCLs that are registered,
        # in case we need to set default announceTo
        self.events.resource_created.register_handler(self._scl_created, Scl)
        self.events.resource_deleted.register_handler(self._scl_deleted, Scl)

        self._initialized()

    def _start(self):
        def retrieve_scl_list():
            scls_req_ind = RetrieveRequestIndication(self._scl_base + '/scls')
            return (self.api.handle_request_indication(scls_req_ind)
                    .then(lambda r: r.resource.sclCollection))

        def get_scl(scl):
            scl_req_ind = RetrieveRequestIndication(scl)
            return (self.api.handle_request_indication(scl_req_ind)
                    .then(lambda r: r.resource))

        def handle_scl_list(scl_list):
            for scl in scl_list:
                self._scl_links[scl.path] = scl.link

        return retrieve_scl_list().then(
            lambda scls_list: async_all(map(get_scl, scls_list))).then(
            handle_scl_list).then(
            self._started)

    def _scl_created(self, scl, req_ind):
        self._scl_links[scl.path] = scl.link

    def _scl_deleted(self, scl, req_ind):
        self._scl_links.pop(req_ind.path, None)

    def _wait_for_same_resource(self, path):
        p = Promise()
        try:
            self._pending_operations[path].append(p)
        except KeyError:
            self._pending_operations[path] = [p]
            p.fulfill(path)
        return p

    def _unwait_for_same_resource(self, path):
        self._pending_operations[path].pop(0)
        try:
            self._pending_operations[path][0].fulfill(path)
        except IndexError:
            del self._pending_operations[path]

    def _update_annc_create(self, resource, req_ind):
        self.logger.debug("_update_annc_create: %s", resource)
        self._announcements[resource.path] = {
            'resource': deepcopy(resource),
            'uris': {}
        }
        try:
            self._announcements[resource.path][
                'resource'].announceTo.sclList = []
        except KeyError:
            pass
        except (TypeError, AttributeError):
            self._announcements[resource.path][
                'resource'].announceTo = AnnounceTo(sclList=[])

        if resource.typename == 'application':
            req_ent = resource.path
        else:
            req_ent = req_ind.requestingEntity
        self._update_annc(resource, self._CREATE, req_ent)

    def _update_annc_update(self, resource, req_ind):
        if not req_ind.do_announce:
            return
        self._update_annc(resource, self._UPDATE, req_ind.requestingEntity)

    def _update_annc(self, resource, method, req_ent):
        self.logger.debug("_update_annc %s - %s: ", resource,
                          resource.announceTo)

        if resource.announceTo:
            # This action shall apply if the following conditions are met:
            # * A new announceable resource is created in the local SCL and the
            # CREATE request contains an announceTo attribute.
            # * The announceTo attribute of the announceable resource is
            # added/changed.
            self._update_annc_by_app(resource, method, req_ent)
        else:
            # This action shall apply if the following conditions are met:
            # * A new announceable resource is created in the local SCL, the
            # CREATE request does not contain an announceTo attribute.
            # * The announceTo attribute is removed from the resource
            # representation by an XXXUpdateRequestIndication (where XXX
            # represents the resource that contains the announceTo attribute).
            self._update_annc_by_scl(resource, req_ent)

    def _update_annc_by_app(self, resource, method, req_ent):
        if not resource.announceTo.activated:

            # 1) If the announceTo attribute contains the activated element set
            # to FALSE and the original request that triggered this action is
            # not a CREATE, then the local SCL shall reject the original
            # request with STATUS_NOT_FORBIDDEN and then this procedure stops.
            # Todo: handle this in the controller
            if method != self._CREATE:
                resource.announce_to.set('activated', True)

            # 2) If the announceTo attribute contains the activated element set
            # to FALSE and the original request that trigger this action is a
            # CREATE, then the announceTo attribute value is stored as-is in the
            # resource. No further actions are required.
            else:
                self._update_resource(resource)

        else:
            # 3) If the announceTo attribute contains the activated element set
            # to TRUE, or if the announceTo attribute does not contain the
            # activated element, then the local SCL shall:
            # 4) The local SCL shall update the announceTo attribute in the
            # resource.
            self._wait_for_same_resource(resource.path).then(
                lambda p: self._handle_announce_to(resource, req_ent)).then(
                lambda l: self._update_resource(resource, l[0], l[1])).then(
                lambda t: self._unwait_for_same_resource(resource.path))

    def _update_annc_by_scl(self, resource, req_ent):
        # 1) It checks if the issuer is an application registered to this local
        # SCL, if not the procedure stops here, otherwise the local SCL checks
        # if global element is set to TRUE. (If global is set to FALSE the
        # procedure does not apply).
        def get_app():
            get_app_req_ind = RetrieveRequestIndication(urlparse(req_ent).path)
            return self.api.handle_request_indication(get_app_req_ind).then(
                lambda r: r.resource)

        def handle_app(app):
            # Todo: get application if resource is not an application
            # 2) The sclList of announceTo of the application Registration is
            # used (note that the list may be empty, in case the issuer wants
            # to forbid announcing any created resources).

            # 3) If the activate element of the announceTo attribute from the
            # application resource is set to FALSE, then the local SCL adds the
            # announceTo attribute in the announceable resource (that trigger
            # this procedure) and it sets the activate element to FALSE. The
            # action returns.

            # 4) Otherwise (i.e. global set to FALSE or no announceTo is
            # present), the SCL determines based on its policies, if the
            # resource shall be announced:
            resource.announceTo = AnnounceTo(sclList=[])

            # a) If the policies state the resource shall not be announced,
            # this action returns and the original procedure is continued.

            # b) Otherwise, the SCL determines which SCLs shall be in the
            # sclList element of the announceTo attribute. The SCL also set the
            # active element to TRUE.

            # Then, the local SCL shall announce the resource to the SCLs in the
            # sclList element. This procedure is described in step 3, from a to e
            # in clause 10.3.2.8.1, with the exception that the requestingEntity
            # for any initiated request is set to the SCL hosting the announcing
            # resource.
            # 5) The announceTo with the updated sclList is set on the
            # original resource (that trigger this procedure). This may
            # trigger notifications to resources that have subscribed to
            # changes in the original resource or its announceTo attribute.
            pass

        # get_app().then(handle_app)
        if self.config.get("auto_announce", True):
            resource.announceTo = AnnounceTo(sclList=self._scl_links.values())
            # TODO: update the resource internally
        else:
            resource.announceTo = AnnounceTo(sclList=[])

        self._wait_for_same_resource(resource.path).then(
            lambda p: self._handle_announce_to(resource, req_ent)).then(
            lambda l: self._update_resource(resource, l[0], l[1], True)).then(
            lambda t: self._unwait_for_same_resource(resource.path))

    def _delete_annc(self, resource, req_ind):
        if req_ind.expired:
            return self._announcements.pop(req_ind.path, None)

        req_ent = req_ind.requestingEntity
        try:
            resource = deepcopy(self._announcements[req_ind.path]['resource'])
        except KeyError:
            return
        resource.announceTo = AnnounceTo(sclList=[])

        self._wait_for_same_resource(resource.path).then(
            lambda p: self._handle_announce_to(resource, req_ent)).then(
            lambda r: self._announcements.pop(req_ind.path, None)).then(
            lambda t: self._unwait_for_same_resource(resource.path))

    def _handle_announce_to(self, resource, req_ent):
        try:
            old_resource = self._announcements[resource.path]['resource']
        except KeyError:
            # todo: handle missing resource
            raise SCLError()
        try:
            old_scl_list = (old_resource.announceTo.sclList
                            if old_resource.announceTo.activated else [])
        except AttributeError:
            old_scl_list = []

        db_scl_list = resource.announceTo.sclList

        annc_model = get_resource_type(resource.typename + "Annc")

        resource_id = getattr(resource, resource.id_attribute)
        annc_id = resource_id + 'Annc'

        # a) Check if the SCLs indicated in the sclList element of the
        # announceTo attribute are registered to/from this local SCL. If any of
        # the SCLs in the sclList is not registered then those SCLs are removed
        # from the sclList and no further actions for those SCLs are performed.
        def check_scl_list():
            return filter(lambda x: x in db_scl_list, self._scl_links.values())

        # b) Send createXXXAnnouncementResourceRequestIndication (where XXX is
        # replaced by the type of the resource to be announced) for each SCL in
        # the sclLists element of the announceTo attribute that is NOT yet
        # included in the previous-announceTo. The request includes:
        def send_create_annc_pre(scl_uri):
            try:
                if resource.accessRightID is None:
                    return send_create_annc(scl_uri)
            except AttributeError:
                return send_create_annc(scl_uri)

            if self.api.is_local_path(resource.accessRightID):

                return send_create_annc(scl_uri, resource.accessRightID)
            else:
                return send_create_annc(scl_uri)

        def send_create_annc(scl_uri, local_ar=None):
            annc = annc_model()
            endpoint = self.api.get_mid_uri(urlparse(scl_uri).scheme)

            # * searchStrings from the original resource;
            annc.searchStrings = resource.searchStrings

            # * accessRightID from the original resource;
            if local_ar:
                annc.accessRightID = urljoin(endpoint, urlparse(
                    resource.accessRightID).path)
            elif local_ar is None:
                annc.accessRightID = local_ar
            else:
                annc.accessRightID = resource.accessRightID

            # * link is set to the URI of the original resource;
            annc.link = urljoin(endpoint, resource.path)

            # * requestingEntity is set to the application;
            # req_ent from from outer scope

            # * issuer is set to its own SCL ID (the local SCL performing the
            # action);
            # rst: not needed probably

            # * id of the resource shall be set to the id of the original
            # resource postfixed with Annc. I.e. if the original resource has id
            # "myApp", the announced resource shall have the id "myAppAnnc";
            annc.id = annc_id

            # * expirationTime handling is to the discretion of the SCL
            # implementation. It is the responsibility of the local SCL to keep
            # the announced resource in sync with the lifetime of the original
            # resource, as long as the announcement is active. One strategy to
            # minimize signalling would be to request the same expiration from
            # the original resource. If this is accepted by the remote SCL, then
            # no explicit de-announce is needed in case of expiration of the
            # original resource;
            annc.expirationTime = resource.expirationTime

            # * targetID is set as follow.
            # TODO: inline
            def get_target_id():
                scl_path = scl_uri + '/scls/' + self.scl_id
                apps_path = self._scl_base + '/applications/'
                if resource.typename == 'application':  # is appAnnc
                    return scl_path + '/applications/'
                else:
                    try:
                        parent = _special_parent_map[resource.typename] + '/'
                    except KeyError:
                        parent = resource.typename + 's/'
                    if resource.path.find(apps_path) == 0:  # is under appAnnc
                        # todo: lookup appAnnc in self._announcements
                        return (scl_path + '/applications/' +
                                sub(apps_path, '',
                                    resource.path).split('/')[0] +
                                'Annc/' + parent)
                    else:  # is other Annc
                        return scl_path + '/' + parent

            target_id = get_target_id()
            try:
                req_ent_mid = urljoin(endpoint, urlparse(req_ent).path)
            except AttributeError:  # probably req_ent was not set due to debug
                self.logger.debug("Could not midify")
                req_ent_mid = None

            create_annc_req_ind = CreateRequestIndication(
                target_id, annc, requestingEntity=req_ent_mid)

            return self.api.send_request_indication(create_annc_req_ind)

        # c) Ignore all SCLs in the sclList element of the announceTo attribute
        # that were already included in the previous-announceTo.

        # d) Send deleteXXXAnnouncementResourceRequestIndication (where XXX is
        # replaced by the type of resource to be de-announced) for each SCL in
        # the previous-announceTo that is not included in the sclList of the
        # provided announceTo attribute. The request shall include the URI of
        # the announcement resource to be removed. The request includes:
        def send_delete_annc(scl_uri):
            endpoint = self.api.get_mid_uri(urlparse(scl_uri).scheme)

            # * requestingEntity is set to the application;
            # req_ent from from outer scope

            # * issuer is set to its own SCL ID (the local SCL performing the
            # action);
            # rst: not needed probably

            # * targetID is set to the resource URI of the previously
            # announced-resource on the remote SCL. The local SCL received and
            # stored the URI of the announced resource after it was created.
            annc_path = self._announcements[resource.path]['uris'][scl_uri]
            target_id = urljoin(scl_uri, annc_path)

            try:
                req_ent_mid = urljoin(endpoint, urlparse(req_ent).path)
            except AttributeError:  # probably req_ent was not set due to debug
                self.logger.debug("Could not midify")
                req_ent_mid = None

            delete_annc_req_ind = DeleteRequestIndication(
                target_id, requestingEntity=req_ent_mid)

            return self.api.send_request_indication(delete_annc_req_ind)

        # e) Waits until all the createXXXAnnouncementResourceResponseConfirm
        # and/or deleteXXXAnnouncementResourceResponseConfirm are received and
        # it acts as follow:
        def send_anncs(scl_list):
            # i) For each unsuccessful
            # createXXXAnnouncementResourceResponseIndication, the remote SCL is
            # removed from the sclList in the announceTo attribute.
            def handle_create_err(res):
                return res.scl_uri

            # ii) For each successful
            # createXXXAnnouncementResourceResponseIndication, the local SCL
            # shall internally store the resourceURI of the created announced
            # resource. This URI is needed for delete the resource later on.
            def handle_create(res):
                if isinstance(res.res_con, ErrorResponse):
                    return handle_create_err(res)
                self._announcements[resource.path]['uris'][
                    res.scl_uri] = res.res_con.resourceURI
                return False

            # iii) For each unsuccessful
            # deleteXXXAnnouncementResourceRequestIndication with the statusCode
            # STATUS_NOT_FOUND, the remote SCL is removed from the sclList in
            # the announceTo attribute.
            # For all other statusCode value, no action is performed.
            def handle_delete_err(res):
                try:
                    if res.res_con.statusCode != 'STATUS_NOT_FOUND':
                        return res.scl_uri
                finally:
                    del self._announcements[resource.path]['uris'][res.scl_uri]
                    return False

            # iv) For each successful
            # deleteXXXAnnouncementResourceRequestIndication, the remote SCL is
            # removed from the sclList in the announceTo attribute.
            def handle_delete(res):
                if isinstance(res.res_con, ErrorResponse):
                    return handle_delete_err(res)
                del self._announcements[resource.path]['uris'][res.scl_uri]
                return False

            create_list = [x for x in scl_list if x not in set(old_scl_list)]
            delete_list = [x for x in old_scl_list if x not in set(scl_list)]

            filtered_scls = [x for x in db_scl_list if x not in set(scl_list)]

            # links the send funcs with the handle result funcs
            create_func = lambda s: send_create_annc_pre(s).then(
                lambda r: handle_create(AnncResult(s, r)),
                lambda r: handle_create_err(AnncResult(s, r)))
            delete_func = lambda s: send_delete_annc(s).then(
                lambda r: handle_delete(AnncResult(s, r)),
                lambda r: handle_delete_err(AnncResult(s, r)))

            # filters out all False in the list
            def filter_func(l):
                return filter(None, l)

            return async_all([
                (async_all(map(create_func, create_list)).then(filter_func)
                 .then(lambda l: l + filtered_scls)),
                async_all(map(delete_func, delete_list)).then(filter_func)
            ])

        return send_anncs(check_scl_list())

    def _update_resource(self, resource, remove_list=None, add_list=None,
                         force=False):
        if not add_list:
            add_list = []
        if not remove_list:
            remove_list = []

        old_resource = self._announcements[resource.path]['resource']
        update_needed = old_resource.announceTo.activated
        old_resource.announceTo = resource.announceTo

        def update_announce_to():
            update_req_ind = UpdateRequestIndication(resource.path +
                                                     '/announceTo', resource,
                                                     fields=['announceTo'],
                                                     do_announce=False)
            return self.api.handle_request_indication(update_req_ind).get()

        if len(remove_list) or len(add_list):
            scl_list = resource.announceTo.sclList
            for s in remove_list:
                scl_list.remove(s)
            scl_list.extend(add_list)
            if not len(scl_list):
                try:
                    resource.activated = False
                except KeyError:
                    pass
            old_resource.announceTo = resource.announceTo
            update_announce_to()

        if force:
            return update_announce_to()

        if update_needed:
            return self._update_announcements(resource, add_list)

        return None

    def _update_announcements(self, resource, add_list):
        old_resource = self._announcements[resource.path]['resource']
        uris = self._announcements[resource.path]['uris']

        attributes_changed = False

        try:
            if (resource.expirationTime != old_resource.expirationTime or
                    resource.searchStrings != old_resource.searchStrings or
                    resource.accessRightID != old_resource.accessRightID):
                attributes_changed = True
        except AttributeError:
            if (resource.expirationTime != old_resource.expirationTime or
                    resource.searchStrings != old_resource.searchStrings):
                attributes_changed = True

        if attributes_changed:

            annc_model = get_resource_type(resource.typename + "Annc")

            def send_update_annc_pre(scl_uri):
                try:
                    if not resource.accessRightID:
                        return send_update_annc(scl_uri)
                except AttributeError:
                    return send_update_annc(scl_uri)

                return send_update_annc(scl_uri, self.api.is_local_path(
                    resource.accessRightID))

            def send_update_annc(scl_uri, local_ar=False):
                endpoint = self.api.get_mid_uri(urlparse(scl_uri).scheme)

                annc = annc_model()

                # link hast to be set
                annc.link = urljoin(endpoint, resource.path)

                # * searchStrings from the original resource;
                annc.searchStrings = resource.searchStrings

                # * accessRightID from the original resource;
                if local_ar:
                    annc.accessRightID = urljoin(endpoint, urlparse(
                        resource.accessRightID).path)
                else:
                    annc.accessRightID = resource.accessRightID

                # * expirationTime handling is to the discretion of the SCL
                # implementation. It is the responsibility of the local SCL to
                # keep the announced resource in sync with the lifetime of the
                # original resource, as long as the announcement is active. One
                # strategy to minimize signalling would be to request the same
                # expiration from the original resource. If this is accepted by
                # the remote SCL, then no explicit de-announce is needed in case
                # of expiration of the original resource;
                annc.expirationTime = resource.expirationTime

                update_req_ind = UpdateRequestIndication(
                    uris[scl_uri], annc, requestingEntity=endpoint)

                # todo investigate response for not accepted expirationTime
                return self.api.send_request_indication(update_req_ind)

            old_resource.searchStrings = resource.searchStrings
            try:
                old_resource.accessRightID = resource.accessRightID
            except AttributeError:
                pass
            old_resource.expirationTime = resource.expirationTime

            scl_list = resource.announceTo.sclList
            # TODO: conversion to set()  is questionable
            update_list = [x for x in scl_list if x not in set(add_list)]

            return async_all(map(send_update_annc_pre, update_list))

        return None

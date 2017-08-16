"""
Created on 26.12.2013

@author: kca
"""

from datetime import timedelta
from urlparse import urlparse
from posixpath import normpath
from openmtc.model import ModelTypeError

from openmtc_etsi.exc import (SCLMethodNotAllowed, SCLBadRequest, SCLError,
                              SCLNotFound)
from openmtc_scl.methoddomain.controller import (
    DefaultController, AccessRightController, LocationContainerController,
    ContentInstanceController, ContentInstancesController, CollectionController,
    SclController, DiscoveryController, SubscriptionController, GroupController,
    NotificationChannelController, SclBaseController, AnnouncementController,
    SubscriptionsController, MembersContentController, ApplicationController)
from openmtc_etsi.scl import (RequestIndication,  CreateRequestIndication,
                              NotifyRequestIndication, RequestIndicationMethod)
from openmtc_etsi.model import (
    SclBase, Application, AccessRight, ContentInstance, ContentInstances, Scl,
    CollectionResource, Subscriptions, get_etsi_type, Discovery, Subscription,
    Group, MembersContent, NotificationChannel, AnnouncementResource,
    LocationContainer)
from aplus import Promise
from openmtc_server.db.exc import DBNotFound
from openmtc_scl.methoddomain.routes import match_route
from openmtc_etsi.response import ErrorResponseConfirmation,\
    NotifyResponseConfirmation
from openmtc_scl import ETSIEndpoint
import aggregate_data
from openmtc_etsi.serializer import get_serializer, Serializer
from openmtc_server import Component
from openmtc_scl.methoddomain.util import decode_content


class ETSIMethodDomain(Component):
    default_lifetime = 60 * 60  # 1 hour
    min_lifetime = 5  # 5 secs
    max_lifetime = 60 * 60 * 24  # 1 day

    def __init__(self, config, *args, **kw):
        super(ETSIMethodDomain, self).__init__(*args, **kw)

        self._api = None
        self.events = None

        self.config = config

        self.normalize_paths = bool(config["global"].get("normalize_paths",
                                                         True))
        self.default_content_type = config["global"].get(
            "default_content_type", "application/json")
        self.scl_id = config["etsi"]["scl_id"]
        self.req_storage = {}

        for k in ("default_lifetime", "min_lifetime", "max_lifetime"):
            try:
                v = self.config["global"][k]
            except KeyError:
                v = getattr(self, k)

            self.config["global"][k] = timedelta(seconds=v)

        # TODO: use proper config framework
        if self.config["etsi"].get("etsi_compatibility"):
            Serializer.compat = True

        # TODO: kca: I'm sure there's a nicer way
        self.controllers = {
            Application: ApplicationController,
            AccessRight: AccessRightController,
            ContentInstance: ContentInstanceController,
            ContentInstances: ContentInstancesController,
            SclBase: SclBaseController,
            Scl: SclController,
            Discovery: DiscoveryController,
            Subscription: SubscriptionController,
            Subscriptions: SubscriptionsController,
            Group: GroupController,
            MembersContent: MembersContentController,
            NotificationChannel: NotificationChannelController,
            LocationContainer: LocationContainerController
        }

        def all_subclasses(cls):
            return cls.__subclasses__() + [g for s in cls.__subclasses__()
                                           for g in all_subclasses(s)]

        self.controllers.update({sc: AnnouncementController
                                 for sc in AnnouncementResource.__subclasses__()
                                 if not sc.__subclasses__()
                                 })

        for sc in all_subclasses(CollectionResource):
            if not sc.__subclasses__():
                self.controllers.setdefault(sc, CollectionController)

    def initialize(self, api):
        self._api = api
        self.events = self._api.events

    def start(self):
        pass

    def stop(self):
        pass

    def init_scl_base(self):
        scl_base_name = self.config["etsi"]["scl_base"]
        scl_base = SclBase(
            path="/" + scl_base_name,
            aPocHandling="SHALLOW"
        )
        db_session = self._api.start_etsi_session()
        ctrl = self._get_controller(SclBase, db_session,
                                    self.handle_request_indication)

        try:
            result = ctrl(CreateRequestIndication("/", scl_base), None, None)
        except Exception as error:
            self.logger.exception("Initialization error")
            db_session.rollback()
            raise error
        else:
            db_session.commit()
            return result

    def save_resp(self, correlationID, resp):
        """
        Saves the response in the database
        :type correlationID: str
        :type resp: ResponseConfirmation
        """
        shelve = self._api.db.get_shelve("saf_resps")
        shelve.setitem(correlationID, resp)
        shelve.commit()

    def load_resps(self):
        """
        Loads the list of responses from the database
        """
        shelve = self._api.db.get_shelve("saf_resps")
        resps = shelve.items()
        shelve.commit()
        return resps

    def del_resp(self, correlationID):
        """
        Delete the response corresponding to a correlationID in the database
        :type correlationID: str
        :return: Promise fulfilled when the response is deleted
        :rtype: Promise
        """
        self.logger.debug("Deleting resp with correlationID %s" %
                          (correlationID, ))
        shelve = self._api.db.get_shelve("saf_resps")
        shelve.pop(correlationID)
        shelve.commit()
        return True

    def _handle_correlationID(self, request_indication):
        """
        When a correlationID is detected in a request, this function initiates
        the store and forward mechanism
        :param request_indication: Request containing a correlationID
        :type request_indication: RequestIndication
        :return: response to the request
        :rtype: ResponseConfirmation
        """
        def go(resps):
            # Check if the result is there
            for k, v in resps:
                if request_indication.correlationID == k:
                    return v
                    # TODO : Clear storage depending on policies (timer?)

            # TODO: use a promise
            def cb(respconf, correlationID, contactURI):
                # This implies HTTP makes a second request
                self.logger.debug("MethodDomain is called back, storing req "
                                  "with correlationID %s", correlationID)
                if contactURI:
                    self.logger.debug("Contact uri detected %s", contactURI)
                    # Send a notify with the resp encapsulated
                    try:
                        # TODO: check with Alex if this will work!
                        resource = respconf.resource
                        content_type = respconf.content_type
                    except AttributeError:
                        # removed content type, makes no sense without resource
                        # but: does it make sense to send an empty notify in
                        # this case?
                        resource = None
                        content_type = None
                    else:
                        if not content_type:
                            # only serialize if needed
                            # does it make sense to use default ct?
                            content_type = self.default_content_type
                            serializer = get_serializer(content_type)
                            resource = serializer.encode(resource)

                    # TODO : Add statusCode in Notify Request
                    #  (cf TS 102 921, C.4.8)
                    notify_request = NotifyRequestIndication(
                        path=contactURI,
                        resource=resource,
                        content_type=content_type
                    )
                    notify_request.correlationID = correlationID
                    # Hack to make a difference between this notify and an saf one.
                    # (They both include a correlationID)
                    notify_request.contactURI = "final_result"
                    self._api.send_request_indication(notify_request)
                else:
                    # Add the response to the reply queue
                    # self.req_storage[correlationID] = respconf
                    self.save_resp(correlationID, respconf)

            p = self._api.send_request_indication(request_indication)

            def check_status_code(resp):
                # check if the answer is an accept, set callback if so
                if resp.statusCode == 202:
                    resp.primitiveType = request_indication.method
                    self._api.set_store_forward_cb(cb, request_indication)
                return p

            return p.then(check_status_code)

        return go(self.load_resps())

    def _parse_pa_content(self, request_indication, resource):
        if request_indication.content_type:
            data = request_indication.resource

            serializer = get_serializer(request_indication.content_type)
            data = serializer.load_pa_content(data)

            request_indication.resource = data
            request_indication.content_type = None

    def _parse_content(self, request_indication, resource_types):
        if request_indication.content_type:
            try:
                typename, data = decode_content(request_indication)
            except SCLBadRequest:
                if resource_types[0] == ContentInstance:
                    return "contentInstance"
                raise

            if resource_types[0] == ContentInstance and \
                    typename != "contentInstance":
                return "contentInstance"

            request_indication.resource = data
            request_indication.content_type = None
            return typename
        else:
            return request_indication.typename

    def _handle_aggregate(self, request_indication):
        base_to_remove = "/m2m/aggregate"
        path = request_indication.path[len(base_to_remove):]
        self.logger.debug("aggregated path: %s", path)

        ct = request_indication.content_type
        if ct:
            serializer = get_serializer(ct)

            typename, resource = serializer.decode(request_indication.resource)
            self.logger.debug("decoded resource: %s - %s", resource, typename)

            data = resource
            data["requestingEntity"] = request_indication.requestingEntity

        else:
            data = request_indication.resource
            data["requestingEntity"] = request_indication.requestingEntity

        p = Promise()

        # TODO: use dict.get()
        if path in aggregate_data.ncolmap and \
                len(aggregate_data.ncolmap[path]) > 0:
            aggregate_data.ncolmap[path].append(data)
            aggregate_data.ncolpromises[path].append(p)
            self.logger.debug("added notification to database, size: %s",
                              len(aggregate_data.ncolmap[path]))
        else:
            self.logger.debug("no pending notifies for %s", path)
            aggregate_data.ncolmap[path] = [data]
            aggregate_data.ncolpromises[path] = [p]
            try:
                dtol = aggregate_data.ncoldelaytolerance[path]
            except KeyError:
                # FIXME put default delay tolerance somewhere
                dtol = 10

            def dtol_handler():
                self.logger.debug("dtol_handler FIRING")
                # payload = NotifyCollection()

                payload = list(aggregate_data.ncolmap[path])

                promises = list(aggregate_data.ncolpromises[path])

                # remove path from maps
                aggregate_data.ncolmap.pop(path, None)
                aggregate_data.ncolpromises.pop(path, None)

                notify_req_ind = NotifyRequestIndication(path,
                                                         {"notify": payload},
                                                         typename="notifyCollection")

                self.logger.debug("dtol_handler sends collection: %s", payload)

                def finished(response):
                    result = NotifyResponseConfirmation()
                    for pending_p in promises:
                        pending_p.fulfill(result)

                return self._api.send_request_indication(notify_req_ind) \
                    .then(finished)

            self.logger.debug("starting dtol_handler, countdown: %s seconds",
                              dtol)
            self._api.set_timer(dtol, dtol_handler)

        return p

        # return self._api.send_request_indication(notify)

    def _handle_error(self, request_indication, error):
        try:
            statusCode = error.statusCode
        except AttributeError:
            statusCode = 500

        method = request_indication.method
        raise ErrorResponseConfirmation(statusCode=statusCode,
                                        primitiveType=method,
                                        errorInfo=str(error)
                                        )

    def handle_request_indication(self, request_indication, endpoint=None,
                                  db_session=None):
        if endpoint is None:
            self.logger.debug("Endpoint is None, generating default")
            endpoint = ETSIEndpoint(None, None)

        self.logger.debug("Handling: %s %s on %s", request_indication.method,
                          request_indication.path, endpoint)

        try:
            return self._handle_request_indication(
                request_indication, endpoint, db_session).then(
                None, lambda error: self._handle_error(request_indication,
                                                       error))
        except Exception as error:
            if isinstance(error, SCLError):
                self.logger.debug("Error during request: %r", error)
            else:
                self.logger.exception("Error during request: %r", error)
            with Promise() as p:
                self._handle_error(request_indication, error)
            return p

    def _handle_request_indication(self, request_indication, endpoint,
                                   db_session):
        if self.scl_id in request_indication.via:
            raise SCLBadRequest("Retargeting loop detected: %s" %
                                request_indication.via)

        path = request_indication.path
        if path and path[0] != "/":
            # TODO: use urlsplit?
            path = urlparse(path).path

        # TODO: Send redirect?
        if self.normalize_paths:
            path = normpath(path)

        method = request_indication.method

        # TODO: also: switch to route handling instead of static path
        if method in ("create", "notify") and path.startswith("/m2m/aggregate"):
            return self._handle_aggregate(request_indication)

        resource_types, parent_types, path, partial_accessor, aPoc_path =\
            match_route(path, method)

        request_indication.path = path
        request_indication.partial_accessor = partial_accessor

        def get_resource(db_session):
            self.logger.debug("DB session acquired.")

            def handle_request_indication_with_session(request_indication):
                return self.handle_request_indication(request_indication,
                                                      endpoint=endpoint,
                                                      db_session=db_session)

            if resource_types[0].virtual:
                assert len(resource_types) == 1
                controller = self._get_controller(
                    resource_types[0], db_session,
                    handle_request_indication_with_session)
                result = controller(request_indication, None, endpoint)
                assert result, "No result from controller %s" % (controller, )
                return result

            is_create = method == RequestIndicationMethod.create

            try:
                resource = db_session.get(path)
            except DBNotFound:
                raise SCLNotFound()

            if aPoc_path:
                resource_type = Application
                request_indication.aPoc_path = "/" + aPoc_path
            elif is_create:
                typename = self._parse_content(request_indication,
                                               resource_types)
                try:
                    resource_type = get_etsi_type(typename)
                except ModelTypeError:
                    raise SCLBadRequest("%s is not a valid type" % typename)
                if resource_type not in resource_types:
                    # TODO: METHOD_NOT_ALLOWED?
                    raise SCLBadRequest("Cannot create %s at %s" %
                                        (typename, path))
            else:
                if method == RequestIndicationMethod.update:
                    if partial_accessor:
                        self._parse_pa_content(request_indication,
                                               resource)
                    else:
                        self._parse_content(request_indication,
                                            resource_types)
                resource_type = type(resource)

            if resource_type == SclBase and \
                    method not in (RequestIndicationMethod.retrieve,
                                   RequestIndicationMethod.update):
                raise SCLMethodNotAllowed("Cannot %s SCLBase resources" %
                                          (request_indication.method,))

            controller = self._get_controller(
                resource_type, db_session,
                handle_request_indication_with_session)

            if not is_create or request_indication.content_type is None:
                request_indication.typename = resource_type.get_typename()

            result = controller(request_indication, resource, endpoint)
            assert result, "No result from controller %s" % (controller, )
            return result

        with Promise() as p:
            if db_session is not None:
                try:
                    p.fulfill(get_resource(db_session))
                except BaseException as error:
                    self._handle_error(request_indication, error)
            else:
                self.logger.debug("Acquiring DB session...")
                db_session = self._api.start_etsi_session()

                try:
                    result = get_resource(db_session)
                    self.logger.debug("Committing. result: %s", result)
                    db_session.commit()
                    p.fulfill(result)
                except BaseException as error:
                    if isinstance(error, SCLError):
                        self.logger.debug(error)
                    else:
                        self.logger.error(error)
                    self.logger.debug("Rolling back", exc_info=True)
                    db_session.rollback()
                    self._handle_error(request_indication, error)

        return p

    def _get_controller(self, resource_type, db_session,
                        handle_request_indication):
        self.logger.debug("Getting controller for %s", resource_type)
        controller_class = self.controllers.get(resource_type,
                                                DefaultController)

        return controller_class(
            db_session=db_session,
            resource_type=resource_type,
            events=self.events,
            api=self._api,
            config=self.config,
            handle_request_indication=handle_request_indication)

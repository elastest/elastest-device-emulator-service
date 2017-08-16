import logging
import re
import time
from base64 import b64decode, b64encode
from datetime import datetime
from json import dumps as json_dumps, loads as json_loads
from urllib import urlencode

from flask import Response
from gevent import spawn, spawn_later
from iso8601 import parse_date

from futile.logging import LoggerMixin
from openmtc.util import UTC, datetime_now, datetime_the_future
from openmtc_app.flask_runner import SimpleFlaskRunner, FlaskRunner
from openmtc_onem2m.exc import (CSENotFound, CSENotImplemented, CSEError,
                                STATUS_CONFLICT)
from openmtc_onem2m.mapper import OneM2MMapper
from openmtc_onem2m.model import (AE, Container, ContentInstance, EncodingTypeE,
                                  get_short_member_name, Subscription,
                                  EventNotificationCriteria,
                                  NotificationEventTypeE)
from openmtc_onem2m.serializer import get_onem2m_decoder
from openmtc_onem2m.transport import OneM2MErrorResponse

logging.getLogger("iso8601").setLevel(logging.ERROR)

# fix missing SSLv3
try:
    from gevent.ssl import PROTOCOL_SSLv3
except ImportError:
    import gevent.ssl

    gevent.ssl.PROTOCOL_SSLv3 = gevent.ssl.PROTOCOL_TLSv1


class XAE(LoggerMixin):
    """ Generic OpenMTC application class.
    Implements functionality common to all typical OpenMTC applications.
    """

    # TODO(rst): add more features
    # support several AEs using the same App-ID and appName

    name = None
    containers = ()
    labels = ()
    # default_access_right = True
    default_lifetime = 3600
    max_nr_of_instances = 3
    resume_registration = True
    remove_registration = True
    cse_base = "onem2m"

    def __init__(self, name=None, cse_base=None, expiration_time=None,
                 announce_to=None, *args, **kw):
        super(XAE, self).__init__(*args, **kw)

        self.__app = None
        self.__subscriptions = []

        if name:
            self.name = name
        elif not self.name:
            self.name = type(self).__name__

        if cse_base:
            self.cse_base = cse_base

        self.ae_id = "C" + self.name

        if expiration_time is not None:
            if isinstance(expiration_time, basestring):
                expiration_time = parse_date(expiration_time)
            elif isinstance(expiration_time, (int, float)):
                expiration_time = datetime.fromtimestamp(expiration_time, UTC)

            if not isinstance(expiration_time, datetime):
                raise ValueError(expiration_time)

            self.default_lifetime = (
                expiration_time - datetime_now()).total_seconds()

        self.announceTo = announce_to

        self.__resumed_registration = False
        self.__known_containers = set()
        self.__shutdown = False

        self.mapper = None
        self.allow_duplicate = None
        self.runner = None

        self.fmt_json_regex = re.compile(r'application/([\w]+\+)?json')
        self.fmt_xml_regex = re.compile(r'application/([\w]+\+)?xml')

    def get_expiration_time(self):
        if self.default_lifetime is None:
            return None
        return datetime_the_future(self.default_lifetime)

    expirationTime = property(get_expiration_time)

    @property
    def application(self):
        return self.__app

    def run(self, runner, cse, allow_duplicate=True):
        self.mapper = OneM2MMapper(cse, self.ae_id)

        self.allow_duplicate = allow_duplicate
        self.runner = runner
        self.register()

    def shutdown(self):
        """ Graceful shutdown.
        Deletes all Applications and Subscriptions.
        """
        try:
            self._on_shutdown()
        except:
            self.logger.exception("Error in shutdown handler")

        self.logger.debug("shutdown handler is finished")

        self.__shutdown = True

        self._remove_subscriptions()

        self._remove_apps()

    def _remove_subscriptions(self):
        for subscription in reversed(self.__subscriptions):
            try:
                self.mapper.delete(subscription)
            except:
                pass
        self.logger.debug("subscriptions deleted")

    def _remove_apps(self):
        if self.remove_registration:
            try:
                if self.__app:
                    self.mapper.delete(self.__app)
            except Exception:
                pass
            self.logger.debug("app deleted")

    @staticmethod
    def run_forever(period=1000, func=None, *args, **kw):

        if func is None:
            def func(*_):
                pass

        def run_periodically():
            func(*args, **kw)
            spawn_later(period, run_periodically)

        return spawn(run_periodically)

    def periodic_discover(self, path, fc, interval, cb, err_cb=None):
        if not isinstance(fc, dict):
            fc = {}

        def run_discovery(o):
            try:
                cb(self.discover(path, o))
            except OneM2MErrorResponse as error_response:
                if err_cb:
                    return err_cb(error_response)
            else:
                o['createdAfter'] = datetime_now()

                spawn_later(interval, run_discovery, o)

        return spawn(run_discovery, fc)

    def register(self):
        """ Registers the Application with the CSE. """
        self.logger.info("Registering application as %s." % (self.name,))
        try:
            poa = [self.runner.base_uri]
        except AttributeError:
            poa = []
        app = AE(resourceName=self.name, labels=list(self.labels),
                 pointOfAccess=poa)
        app.announceTo = self.announceTo

        try:
            registration = self.create_application(app)
        except OneM2MErrorResponse as error_response:
            if error_response.response_status_code is STATUS_CONFLICT:
                registration = self._handle_registration_conflict(app)
                if not registration:
                    raise
            else:
                self.logger.error('Error at start up')
                self.logger.error(error_response.response_status_code)
                raise SystemExit
        self.__app = registration

        assert registration.path

        try:
            self._on_register()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.logger.exception("Error on initialization")
            raise

    def _handle_registration_conflict(self, app):
        if not self.resume_registration:
            return None

        app = self.get_application(app)

        self.__start_refresher(app)

        self.__resumed_registration = True

        return app

    def emit(self, event, message=None):
        """ Websocket emit. """
        if not isinstance(self.runner, FlaskRunner):
            raise RuntimeError('Runner is not supporting emit!')
        self.runner.emit(event, message)

    def _on_register(self):
        pass

    def _on_shutdown(self):
        pass

    def get_application(self, application, path=None):
        """ Retrieves an Application resource.

        :param application: old app instance or appId
        :param path: (optional) path in the resource tree
        """
        if path is None:
            # FIXME(rst): use app path and not cse base path
            path = self.cse_base

        if not isinstance(application, AE):
            application = AE(resourceName=application)

        name = application.resourceName

        path = "%s/%s" % (path, name) if path else name
        app = self.mapper.get(path)

        self.logger.debug("retrieved app: %s" % app)

        return app

    def create_application(self, application, path=None):
        """ Creates an Application resource.

        :param application: Application instance or appId as str
        :param path: (optional) path in the resource tree
        """
        # TODO(rst): set app_id via config
        # TODO(rst): set requestReachability based on used runner
        if path is None:
            path = self.cse_base

        def restore_app(app):
            self.logger.warn("Restoring app: %s", app.path)
            app.expirationTime = None
            self.create_application(app, path=path)

        if not isinstance(application, AE):
            application = AE(resourceName=application, App_ID='dummy',
                             requestReachability=False)
        else:
            if not application.App_ID:
                application.App_ID = 'dummy'
            if not application.requestReachability:
                application.requestReachability = False

        if application.expirationTime is None:
            application.expirationTime = self.get_expiration_time()
        app = self.mapper.create(path, application)
        self.logger.debug("Created application at %s", app.path)
        app = self.get_application(application, path)
        assert app.path
        self.__start_refresher(app, restore=restore_app)
        self.logger.info("Registration successful: %s." % (app.path,))

        # TODO(rst): handle when ACP is reimplemented
        # if accessRight:
        #     if not isinstance(accessRight, AccessRight):
        #         accessRight = AccessRight(
        #             id="ar",
        #             selfPermissions={"permission": [{
        #                 "id": "perm",
        #                 "permissionFlags": {
        #                     "flag": ["READ", "WRITE", "CREATE", "DELETE"]
        #                 },
        #                 "permissionHolders": {
        #                     "all": "all"
        #                 }
        #             }]},
        #             permissions={"permission": [{
        #                 "id": "perm",
        #                 "permissionFlags": {
        #                     "flag": ["READ", "WRITE", "CREATE", "DELETE"]
        #                 },
        #                 "permissionHolders": {
        #                     "all": "all"
        #                 }
        #             }]}
        #         )
        #     accessRight = self.create_accessRight(app, accessRight)
        #
        #     app.accessRightID = accessRight.path
        #
        #     self.mapper.update(app, ("accessRightID",))

        return app

    # TODO(rst): use FilterCriteria from model and convert
    def discover(self, path=None, filter_criteria=None, unstructured=False):
        """ Discovers Container resources.

        :param path: the target path to start the discovery
        :param filter_criteria: (optional) FilterCriteria for the for the discovery
        :param unstructured: (optional) set discovery_result_type
        """
        if path is None:
            path = self.cse_base

        # TODO(rst): use filter_criteria from model
        if not filter_criteria:
            filter_criteria = {}
        path += "?fu=1"
        if filter_criteria:
            path += "&" + urlencode({get_short_member_name(k): v
                                     for k, v in filter_criteria.iteritems()},
                                    True)

        path += '&drt' + str(1 if unstructured else 2)

        discovery = self.mapper.get(path)

        return discovery.CONTENT

    def create_container(self, target, container, labels=None,
                         max_nr_of_instances=None):
        """ Creates a Container resource.

        :param target: the target resource/path parenting the Container
        :param container: the Container resource or a valid container ID
        :param labels: (optional) the container's labels
        :param max_nr_of_instances: (optional) the container's maximum number
                                    of instances (0=unlimited)
        """

        def restore_container(c):
            self.logger.warn("Restoring container: %s", c.path)
            c.expirationTime = None
            self.__known_containers.remove(c.path)
            self.create_container(target, c, labels=labels)

        if target is None:
            target = self.__app

        if not isinstance(container, Container):
            container = Container(resourceName=container)

        # if we got max instances..set them
        if max_nr_of_instances:
            container.maxNrOfInstances = max_nr_of_instances
        # if we did not set max instances yet, set them
        else:
            container.maxNrOfInstances = self.max_nr_of_instances

        if container.expirationTime is None:
            container.expirationTime = self.get_expiration_time()

        if labels:
            container.labels = labels

        path = getattr(target, "path", target)

        try:
            container = self.mapper.create(path, container)
        except OneM2MErrorResponse as error_response:
            if error_response.response_status_code is STATUS_CONFLICT:
                c_path = path + '/' + container.resourceName
                container.path = c_path
                if (self.__resumed_registration and
                        c_path not in self.__known_containers):
                    container = self.mapper.update(container)
                else:
                    raise error_response
            else:
                raise error_response

        self.__known_containers.add(container.path)
        self.__start_refresher(container, restore=restore_container)
        self.logger.info("Container created: %s." % (container.path,))
        return container

    # TODO(rst): handle when ACP is reimplemented
    # def create_access_right(self, application, accessRight):
    #     """ Creates an AccessRight resource.
    #
    #     :param application: the Application which will contain the AR
    #     :param accessRight: the AccessRight instance
    #     """
    #     self.logger.debug("Creating accessRight for %s", application)
    #
    #     if application is None:
    #         application = self.__app
    #         assert application.path
    #
    #     path = getattr(application, "path", application)
    #
    #     if not path.endswith("/accessRights"):
    #         path += "/accessRights"
    #
    #     accessRight = self.mapper.create(path, accessRight)
    #     accessRight = self.mapper.get(accessRight.path)
    #     self.__start_refresher(accessRight, extra_fields=["selfPermissions"])
    #     self.logger.info("accessRight created: %s." % (accessRight.path,))
    #     return accessRight
    #
    # create_accessRight = create_access_right

    def get_resource(self, path, app_local=False):
        if app_local:
            path = self.__app.path + '/' + path

        if not path:
            return None
        try:
            resource = self.mapper.get(path)
        except OneM2MErrorResponse:
            resource = None
        return resource

    def push_content(self, container, content, fmt=None, text=None):
        """ Creates a ContentInstance resource in the given container,
        wrapping the content.
        Defaults to serialising the content as JSON and base64 encodes it.
        NOTE: Will attempt to create the container, if not found.

        :param container: Container object or container path string
        :param content: the content data
        :param fmt:
        :param text:
        """
        path = getattr(container, "path", container)

        if isinstance(content, (str, unicode)):
            fmt = 'text/plain' if fmt is None else fmt
            text = True if text is None else text
        elif isinstance(content, (dict, list)):
            fmt = 'application/json' if fmt is None else fmt
            text = False if text is None else text
        else:
            raise CSENotImplemented("Only dict, list and str are supported!")

        if fmt == 'application/json' or re.search(self.fmt_json_regex, fmt):
            if text:
                # TODO(rst): check if it should be with masked quotation marks
                # con = json_dumps(content)
                # cnf = fmt + ':' + str(EncodingTypeE.plain.value)
                raise CSENotImplemented("Only json as b64 is supported!")
            else:
                con = b64encode(json_dumps(content))
                cnf = fmt + ':' + str(EncodingTypeE.base64String.value)
        elif fmt == 'text/plain':
            if text:
                con = content
                cnf = fmt + ':' + str(EncodingTypeE.plain.value)
            else:
                con = b64encode(content)
                cnf = fmt + ':' + str(EncodingTypeE.base64String.value)
        else:
            # TODO(rst): add handling of other formats or raise not implemented
            raise CSENotImplemented("Only json and text are supported!")

        cin = ContentInstance(
            content=con,
            contentInfo=cnf
        )

        try:
            return self.mapper.create(path, cin)
        except CSENotFound:
            raise CSENotFound()

    @staticmethod
    def _get_content_from_cin(cin):
        if isinstance(cin, ContentInstance):
            # TODO(rst): handle contentInfo and decode
            # resource.contentInfo -> application/json:1
            # media, encodingType = split(':')
            # encodingType = 1 -> base64.decodeString(resource.content)
            # encodingType = 2 -> not supported
            media_type, encoding_type = cin.contentInfo.split(':')
            content = cin.content
            try:
                if int(encoding_type) == EncodingTypeE.base64String:
                    content = b64decode(content)

                if media_type == 'application/json':
                    content = json_loads(content)
            except ValueError:
                pass

            return content

        return cin

    def get_content(self, container):
        """ Retrieve the latest ContentInstance of a Container.

        :param container: Container object or container path string
        """
        path = getattr(container, "path", container) + "/latest"

        cin = self.mapper.get(path)
        return self._get_content_from_cin(cin)

    def _get_notification_data(self, data, content_type):
        try:
            serializer = get_onem2m_decoder(content_type)
            notification = serializer.decode(data)
            resource = notification.notificationEvent.representation
            return resource
        except (KeyError, TypeError, ValueError, IndexError):
            self.logger.error("Failed to get notification data from %s" % data)
            return None

    def _remove_route(self, route):
        self.logger.debug("removing route: %s", route)
        self.runner.flask_app.url_map._rules = filter(
            lambda x: x.rule != route,
            self.runner.flask_app.url_map._rules)

    have = set()

    def _add_subscription(self, path, contact, handler, delete_handler,
                          filter_criteria=None, expiration_time=None):

        if not isinstance(self.runner, SimpleFlaskRunner):
            # TODO(rst): use notification channel instead
            raise RuntimeError('Runner not supporting subscription!')

        contact = contact.replace("%", "_").replace(":", "_")

        route_handle = "/notify/%s-handle" % (contact,)
        route_delete = "/notify/%s-delete" % (contact,)

        self.have |= {
            route_handle,
            route_delete,
            path,
        }

        expiration_time = expiration_time or self.get_expiration_time()
        subscription = Subscription(
            notificationURI=["%s%s" % (self.ae_id, route_handle)],
            subscriberURI="%s%s" % (self.ae_id, route_delete),
            expirationTime=expiration_time)
        if filter_criteria:
            subscription.eventNotificationCriteria = filter_criteria

        self.mapper.create(path, subscription)
        self.__subscriptions.append(subscription)

        def remove_sub(sub):
            # cleanup of subscription
            try:
                self.__subscriptions.remove(sub)
                self._remove_route(route_handle)
                self._remove_route(route_delete)
                self.have -= {
                    route_handle,
                    route_delete,
                    path,
                }
                del sub
            except ValueError:
                pass

        def restore_sub(sub):
            # called to recreate the subscription
            # for some reason subscription is not assigned here,
            # so we make it a parameter
            self.logger.warn("Restoring subscription: %s", sub.name)
            remove_sub(sub)
            self._add_subscription(path, contact, handler, filter_criteria)

        # refresh expirationTime regularly
        self.__start_refresher(subscription, restore=restore_sub)
        self.logger.debug("Added subscription: %s -> %s", path, contact)

        # create good response with correct rsc header
        resp = Response(headers={'x-m2m-rsc': 2000})

        def h(request):
            # to make the handling of the data async from the response
            n_data = self._get_notification_data(request.get_data(),
                                                 request.content_type)
            if n_data:
                spawn(handler, n_data)
            return resp

        def d(_):
            remove_sub(subscription)
            if delete_handler:
                spawn(delete_handler, path)
            return resp

        self.runner.add_route(route_handle, h, methods=("POST",))
        self.runner.add_route(route_delete, d, methods=("POST",))

    def add_subscription(self, path, handler, delete_handler=None):
        """ Creates a subscription resource at path.
        And registers handler to receive notification data.

        :param path: path to subscribe to
        :param handler: notification handler
        :param delete_handler: reference to delete handling function
        """

        # def content_handler(n_data):
        #     handler(n_data)

        self._add_subscription(
            path,
            path.replace('/', '_'),
            handler,
            delete_handler
        )

    def add_container_subscription(self, container, handler, delete_handler=None,
                                   filter_criteria=EventNotificationCriteria()):
        """ Creates a Subscription to the ContentInstances of the given
        Container.

        :param container: Container object or container path string
        :param handler: reference of the notification handling function
        :param delete_handler: reference to delete handling function
        :param filter_criteria: (optional) FilterCriteria for the subscription
        """

        path = getattr(container, "path", container)

        # check if target is container
        cnt = self.mapper.get(path)
        if not isinstance(cnt, Container):
            raise RuntimeError('Target is not a container.')

        def content_handler(n_data):
            handler(container, self._get_content_from_cin(n_data))

        filter_criteria.notificationEventType = list([
            NotificationEventTypeE.createOfDirectChildResource,
        ])

        self._add_subscription(
            path,
            'container_' + path.replace('/', '_'),
            content_handler,
            delete_handler,
            filter_criteria
        )

    def __start_refresher(self, instance, extra_fields=(), restore=None):
        """ Starts a threading.Timer chain,
        to repeatedly update a resource instance's expirationTime.
        NOTE: instance.expirationTime should already be set and the instance
        created.

        :param instance: resource instance
        :param extra_fields: additional fields, needed in the update request
        :param restore: function that will restore the instance, if it has
                        expired accidentally. Has to restart the refresher.
        """
        if not instance.expirationTime:
            return
        interval = time.mktime(instance.expirationTime.timetuple()) - (
            time.time() + time.timezone)
        if interval > 120:
            interval -= 60
        else:
            interval = max(1, interval * 0.75)

        self.logger.debug("Will update expiration time of %s in %s seconds",
                          instance, interval)
        self.runner.set_timer(interval, self.__update_exp_time,
                              instance=instance, extra_fields=extra_fields,
                              restore=restore)

    def start_refresher(self, instance, extra_fields=(), restore=None):
        self.__start_refresher(instance, extra_fields=extra_fields,
                               restore=restore)

    def __update_exp_time(self, instance=None, the_future=None, extra_fields=(),
                          interval=None, offset=None, restore=None):
        """ Updates a resource instance's expirationTime to the_future
        or a default value sometime in the future.

        :note: If instance is not provided or None or False, self.__app is
               updated.
        :note: Starts a new Timer.
        :param instance: resource instance to update
        :param the_future: new expirationTime value
        :param extra_fields: additional fields, needed in the update request
        :param interval: update interval
        :param offset: expirationTime offset (should be >0)
        :param restore: function that will restore the instance, if it has
                        expired accidentally. Has to restart the refresher.
        :raise CSENotFound: If the instance could not be found and no restore
                            was provided.
        """
        self.logger.debug("updating ExpirationTime of %s", instance)
        if self.__shutdown:
            # not sure this ever happens.
            return

        interval = interval or 60 * 10  # TODO make configurable
        offset = offset or 60 * 10  # 10min default
        if not the_future:
            the_future = time.time() + interval + offset
            the_future = datetime.utcfromtimestamp(the_future)
        fields = ["expirationTime"]
        fields.extend(extra_fields)
        if not instance:
            # does this happen if the instance was deleted?
            instance = self.__app
        instance.expirationTime = the_future
        try:
            self.mapper.update(instance, fields)
        except CSENotFound as e:
            self.logger.warn("ExpirationTime update of %s failed: %s", instance,
                             e)
            # subscription disappeared?
            # missed the expirationTime?
            # mb sync issue?; mb congestion?
            if restore:
                restore(instance)
                return
            else:
                raise
        # NOTE: expirationTime might have been changed by CSE at this point.
        # update could/should return the updated instance in this case, but
        # doesnt. => additional GET to confirm expirationTime ?

        self.logger.debug("Will update expiration time in %s seconds", interval)
        self.runner.set_timer(interval, self.__update_exp_time,
                              instance=instance, extra_fields=extra_fields,
                              restore=restore)

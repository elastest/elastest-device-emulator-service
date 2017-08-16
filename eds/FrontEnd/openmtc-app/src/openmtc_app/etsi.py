import logging
import time
from base64 import b64decode, b64encode
from datetime import datetime
from json import dumps as json_dumps, loads as json_loads
from urllib import urlencode

import re
from gevent import spawn, spawn_later
from iso8601 import parse_date

from futile.logging import LoggerMixin
from futile.net.http.exc import HTTPError400  # TODO(rst): try to remove
from openmtc.util import UTC, datetime_now, datetime_the_future
from openmtc_etsi.exc import SCLNotFound, SCLConflict, SCLBadGateway, \
    SCLNotImplemented, SCLError
from openmtc_etsi.mapper import ETSIMapper
from openmtc_etsi.model import (Application, Subscription, Container,
                                AccessRight)
from openmtc_etsi.scl import CreateRequestIndication

logging.getLogger("iso8601").setLevel(logging.ERROR)

# fix missing SSLv3
try:
    from gevent.ssl import PROTOCOL_SSLv3
except ImportError:
    import gevent.ssl

    gevent.ssl.PROTOCOL_SSLv3 = gevent.ssl.PROTOCOL_TLSv1


class XA(LoggerMixin):
    """ Generic OpenMTC application class.
    Implements functionality common to all typical OpenMTC applications.
    """
    name = None
    containers = ()
    search_strings = ()
    default_access_right = True
    default_lifetime = 3600
    max_nr_of_instances = 30
    resume_registration = True
    remove_registration = True
    scl_base = "m2m"

    def __init__(self, name=None, scl_base=None, expiration_time=None,
                 announce_to=None, *args, **kw):
        super(XA, self).__init__(*args, **kw)

        self.__app = None
        self.__subscriptions = []

        if name:
            self.name = name
        elif not self.name:
            self.name = type(self).__name__

        if scl_base:
            self.scl_base = scl_base

        if expiration_time is not None:
            if isinstance(expiration_time, basestring):
                expiration_time = parse_date(expiration_time)
            elif isinstance(expiration_time, (int, float)):
                expiration_time = datetime.fromtimestamp(expiration_time, UTC)

            if not isinstance(expiration_time, datetime):
                raise ValueError(expiration_time)

            self.default_lifetime = (
                expiration_time - datetime_now()).total_seconds()

        self.announce_to = announce_to

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

    def run(self, runner, scl, allow_duplicate=True):
        self.mapper = ETSIMapper(scl)

        self.allow_duplicate = allow_duplicate
        self.runner = runner
        self.register()

    def shutdown(self):
        """ Graceful shutdown.
        Deletes all Applications and Subscriptions.
        """
        if self.__shutdown:
            return

        self.__shutdown = True

        try:
            self._on_shutdown()
        except Exception:
            self.logger.exception("Error in shutdown handler")

        self.logger.debug("shutdown handler is finished")

        self._remove_subscriptions()

        self._remove_apps()

        # if self.__app is not None:
        #    self.mapper.delete(self.__app)

    def _remove_subscriptions(self):
        for subscription in reversed(self.__subscriptions):
            try:
                self.mapper.delete(subscription)
            except Exception:
                pass
        self.logger.debug("subscriptions deleted")

    def _remove_apps(self):
        if self.remove_registration:
            try:
                self.mapper.delete(self.__app)
            except Exception:
                pass
            self.logger.debug("app deleted")

    @staticmethod
    def run_forever(period=1000, func=None, *args, **kw):

        if func is None:
            def func():
                pass

        def run_periodically():
            func(*args, **kw)
            spawn_later(period, run_periodically).join()

        return spawn(run_periodically)

    def periodic_discover(self, fc, interval, func):
        try:
            func(self.discover(fc))
        except SCLError:
            pass
        now = datetime_now()
        try:
            fc['createdAfter'] = now
        except AttributeError:
            fc = {
                'createdAfter': now
            }

        def rerun_discovery(o):
            try:
                func(self.discover(fc))
            except SCLError:
                pass
            o['createdAfter'] = datetime_now()

            spawn_later(interval, rerun_discovery, o)

        return spawn_later(interval, rerun_discovery, fc)

    def register(self):
        """ Registers the Application with the XSCL. """
        self.logger.info("Registering application as %s." % (self.name,))
        app = Application(appId=self.name,
                          searchStrings=list(self.search_strings))
        app.announceTo = self.announce_to

        try:
            registration = self.create_application(
                app, access_right=self.default_access_right)
        except SCLConflict:
            registration = self._handle_registration_conflict(app)
            if not registration:
                raise
        self.__app = registration

        assert registration.path

        # self.mapper.set_requesting_entity(registration.path)

        try:
            self._on_register()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.logger.exception("Error on initialization")
            raise

    def _handle_registration_conflict(self, app, parent="/m2m/applications"):
        if not self.resume_registration:
            return None

        app = self.get_application(app, parent)

        self.__start_refresher(app)

        self.__resumed_registration = True

        return app

    def emit(self, message, event):
        """ Websocket emit. """
        self.runner.emit(message, event)

    def _on_register(self):
        pass

    def _on_shutdown(self):
        pass

    def get_application(self, application, path="/applications"):
        """ Retrieves an Application resource.

        :param application: old app instance or appId
        :param path: (optional) path in the resource tree
        """
        if not isinstance(application, Application):
            application = Application(appId=application)

        app = self.mapper.get("%s/%s" % (path, application.appId))

        self.logger.debug("retrieved app: %s" % app)

        return app

    def create_application(self, application, path="/applications",
                           access_right=True):
        """ Creates an Application resource.

        :param application: Application instance or appId as str
        :param path: (optional) path in the resource tree
        :param access_right: (optional) accessRight instance or boolean
                            indicating use of def AR
        """

        def restore_app(app):
            self.logger.warn("Restoring app: %s", app.path)
            app.expirationTime = None
            self.create_application(app, path=path, access_right=access_right)

        if not isinstance(application, Application):
            application = Application(appId=application)

        if application.expirationTime is None:
            application.expirationTime = self.get_expiration_time()
        app = self.mapper.create(path, application)
        self.logger.debug("Created application at %s", app.path)
        app = self.get_application(application, path)
        assert app.path
        self.__start_refresher(app, restore=restore_app)
        self.logger.info("Registration successful: %s." % (app.path,))

        if access_right:
            if not isinstance(access_right, AccessRight):
                access_right = AccessRight(
                    id="ar",
                    selfPermissions={"permission": [{
                        "id": "perm",
                        "permissionFlags": {
                            "flag": ["READ", "WRITE", "CREATE", "DELETE"]
                        },
                        "permissionHolders": {
                            "all": "all"
                        }
                    }]},
                    permissions={"permission": [{
                        "id": "perm",
                        "permissionFlags": {
                            "flag": ["READ", "WRITE", "CREATE", "DELETE"]
                        },
                        "permissionHolders": {
                            "all": "all"
                        }
                    }]}
                )
            access_right = self.create_accessRight(app, access_right)

            app.accessRightID = access_right.path

            self.mapper.update(app, ("accessRightID",))

        return app

    def discover(self, filter_criteria=None):
        if filter_criteria is None:
            filter_criteria = {}

        path = "/m2m/discovery"
        if filter_criteria:
            path += "?" + urlencode(filter_criteria, True)

        discovery = self.mapper.get(path)

        return discovery.discoveryURI

    def create_container(self, target, container, search_strings=None,
                         max_nr_of_instances=None, access_right_id=True):
        """ Creates a Container resource.

        :param target: the target resource/path parenting the Container
        :param container: the Container resource or a valid container ID
        :param search_strings: (optional) the container's searchStrings
        :param max_nr_of_instances: (optional) the container's maxNrOfInstances
        :param access_right_id: (optional) the container's accessRightID
        """

        def restore_container(c):
            # leaky? references in calling code cant be updated
            self.logger.warn("Restoring container: %s", c.path)
            c.expirationTime = None
            self.__known_containers.remove(c.path)
            self.create_container(target, c, search_strings=search_strings)

        if target is None:
            target = self.__app

        if not isinstance(container, Container):
            container = Container(id=container)

        if access_right_id is True:
            try:
                access_right_id = self.__app.accessRightID
            except AttributeError:
                pass
            else:
                container.accessRightID = access_right_id

        # if we got max instances..set them
        if max_nr_of_instances:
            container.maxNrOfInstances = max_nr_of_instances

        # if we did not set max instances yet, set them
        if container.maxNrOfInstances is None:
            container.maxNrOfInstances = self.max_nr_of_instances

        if container.expirationTime is None:
            container.expirationTime = self.get_expiration_time()
        if search_strings:
            container.searchStrings = search_strings

        path = getattr(target, "path", target)

        if '/containers/' in path:
            path_suffix = '/subcontainers'
        else:
            path_suffix = '/containers'

        if not path.endswith(path_suffix):
            path += path_suffix

        c_path = path + '/' + container.id
        if (self.__resumed_registration and
                c_path not in self.__known_containers):
            container.path = c_path
            self.mapper.update(container)
        else:
            container = self.mapper.create(path, container)

        self.__known_containers.add(container.path)
        self.__start_refresher(container, restore=restore_container)
        self.logger.info("Container created: %s." % (container.path,))
        return container

    def create_access_right(self, application, access_right):
        """ Creates an AccessRight resource.

        :param application: the Application which will contain the AR
        :param access_right: the AccessRight instance
        """
        self.logger.debug("Creating accessRight for %s", application)

        if application is None:
            application = self.__app
            assert application.path

        path = getattr(application, "path", application)

        if not path.endswith("/accessRights"):
            path += "/accessRights"

        access_right = self.mapper.create(path, access_right)
        access_right = self.mapper.get(access_right.path)
        self.__start_refresher(access_right, extra_fields=["selfPermissions"])
        self.logger.info("accessRight created: %s." % (access_right.path,))
        return access_right

    create_accessRight = create_access_right

    def get_resource(self, path, app_local=False):
        if app_local:
            path = self.__app.path + '/' + path

        if not path:
            return None
        try:
            resource = self.mapper.get(path)
        except Exception:
            resource = None
        return resource

    # TODO(rst): handle fmt and text similiar to OneM2M
    def push_content(self, container, content, fmt=None, text=None):
        """ Creates a ContentInstance resource in the given container,
        wrapping the content.
        Serialises content as JSON and base64 encodes it.
        NOTE: Will attempt to create the container, if not found.

        :param container: the Container
        :param content: the content data
        :param fmt:
        :param text:
        """
        path = getattr(container, "path", container)

        if not path.endswith("/contentInstances"):
            path += "/contentInstances"

        if isinstance(content, (str, unicode)):
            fmt = 'text/plain' if fmt is None else fmt
            text = True if text is None else text
        elif isinstance(content, (dict, list)):
            fmt = 'application/json' if fmt is None else fmt
            text = False if text is None else text
        else:
            raise SCLNotImplemented("Only dict, list and str are supported!")

        if re.search(self.fmt_json_regex, fmt):
            if text:
                # TODO(rst): check if it should be with masked quotation marks
                # con = json_dumps(content)
                # cnf = fmt + ':' + str(EncodingTypeE.plain.value)
                raise SCLNotImplemented("Only json as b64 is supported!")
            else:
                ci = {
                    "content": {
                        "binaryContent": b64encode(json_dumps(content)),
                        "contentType": fmt
                    }
                }
        elif fmt == 'text/plain':
            if text:
                ci = {
                    "content": {
                        "textContent": content,
                        "contentType": fmt
                    }
                }
                raise SCLNotImplemented("Only json as b64 is supported!")
            else:
                ci = {
                    "content": {
                        "binaryContent": b64encode(content),
                        "contentType": fmt
                    }
                }
                raise SCLNotImplemented("Only json as b64 is supported!")
        else:
            # TODO(rst): add handling of other formats or raise not implemented
            raise SCLNotImplemented("Only json and text are supported!")

        request_indication = CreateRequestIndication(path=path,
                                                     resource=ci,
                                                     typename="contentInstance"
                                                     )

        try:
            return self.mapper.send_request(request_indication)
        except SCLNotFound:
            # where did the container go? or is it the application?
            self.logger.warn("NotFound: %s; attempting to restore.",
                             container.path)
            container.expirationTime = self.get_expiration_time()
            self.__start_refresher(container)
            self.mapper.create(container.parent_path, container)
            return self.mapper.send_request(request_indication)

    def get_content(self, container):
        """ Retrieve the ContentInstances of a Container.

        :param container: the Container
        """
        path = getattr(container, "path", container)

        if not path.endswith("/contentInstances/latest/content"):
            path += "/contentInstances/latest/content"

        content = self.mapper.get(path)
        return content

    # TODO(rst): add notification decoding like in onem2m
    def __get_notification_data(self, data, parser=None):
        try:
            # FIXME: very dirty hack to workaround broken ETSI notify behaviour
            try:
                notify = data["notify"]
            except KeyError:
                notify = data
            try:
                subscription = notify["subscription"]
            except KeyError:
                subscription = notify["subscriptionReference"]
            path = subscription.rsplit("/", 2)[0]
            data = b64decode(notify["representation"]["$t"])
            self.logger.debug("Notification received: %s" % (path,))
            data = json_loads(data)
            if "errorInfo" in data:
                return data
            if len(data) != 1:
                self.logger.error("Invalid notification: %s" % (data,))
                raise HTTPError400()
            if parser:
                return parser(data)
            else:
                rtype, object = data.items()[0]
                return self.mapper._map(path, rtype, object)
        except (KeyError, TypeError, ValueError, IndexError):
            self.logger.exception("Failed to get notification data from %s" %
                                  (data,))
            raise HTTPError400()

    def __get_content_notification_data(self, data):
        def parser(data):
            data = data["contentInstances"]["contentInstanceCollection"][
                "contentInstance"]

            def get_content(d):
                content = d["content"]

                binary_content = None
                try:
                    binary_content = content["binaryContent"]
                except KeyError:
                    try:
                        binary_content = content["$t"]
                    except KeyError:
                        pass

                if binary_content is not None:
                    text_content = b64decode(binary_content)
                else:
                    text_content = content["textContent"]
                return json_loads(text_content)

            # todo(rst): check why map is used here
            return map(get_content, data)[0]

        return self.__get_notification_data(data, parser)

    def _remove_route(self, route):
        # TODO seems hack-ish
        self.logger.debug("removing route: %s", route)
        self.runner.flask_app.url_map._rules = filter(
            lambda x: not (x.rule == route),
            self.runner.flask_app.url_map._rules)

    have = set()

    def _add_subscription(self, path, contact, handler, filter_criteria=None,
                          expiration_time=None, search_strings=None):

        if not path.endswith("/subscriptions"):
            path += "/subscriptions"

        contact = contact.replace("%", "_").replace(":", "_")

        route = "/notify/%s" % (contact,)

        # if ":" in contact or "%" in contact:
        # if route in self.have or path in self.have:
        #    raise Exception("huhu", contact)

        self.have.add(route)
        self.have.add(path)

        #         from openmtc.util import datetime_the_future
        #         expirationTime = datetime_the_future(180)
        expiration_time = expiration_time or self.get_expiration_time()
        subscription = Subscription(
            contact="%s%s" % (self.runner.base_uri, route),
            expirationTime=expiration_time)
        if filter_criteria:
            subscription.filterCriteria = filter_criteria
            if search_strings:
                # don't want to break compatibility
                subscription.filterCriteria["searchString"] = search_strings
        elif search_strings:
            subscription.filterCriteria = {"searchString": search_strings}
        self.mapper.create(path, subscription)
        self.__subscriptions.append(subscription)

        def remove_sub(sub):
            # cleanup of subscription
            try:
                self.__subscriptions.remove(sub)
                self._remove_route(route)
                self.have.remove(route)
                self.have.remove(path)
                del sub
            except ValueError:
                pass

        def restore_sub(sub):
            # called to recreate the subscription
            # for some reason subscription is not assigned here,
            # so we make it a parameter
            self.logger.warn("Restoring subscription: %s", sub.name)
            remove_sub(sub)
            self._add_subscription(path, contact, handler, filter_criteria,
                                   None, search_strings)

        # refresh expirationTime regularly
        self.__start_refresher(subscription, restore=restore_sub)
        self.logger.debug("Added subscription: %s -> %s", path, contact)

        def h(request):
            handler(request)
            DELETED = ("STATUS_DELETED", 410, "410")
            if request.json["notify"]["statusCode"] in DELETED:
                # resource was deleted
                remove_sub(subscription)
            return ""

        self.runner.add_route(route, h, methods=("POST",))

    def add_subscription(self, path, handler):
        """ Creates a subscription resource at path.
        And registers handler to receive notification data.

        :param path: path to subscribe to
        :param handler: notification handler
        """

        def content_handler(request):
            o = self.__get_notification_data(request.json)
            handler(o)

            return ""

        contact = path.replace("/", "_")
        self._add_subscription(path, contact, content_handler)

    def add_container_subscription(self, container, handler, data_handler=None,
                                   filter_criteria=None):
        """ Creates a Subscription to the ContentInstances of the given Container.

        :param container: the Container or it's path
        :param handler: reference of the notification handling function
        :param data_handler: (optional) reference of the function parsing/decoding the data
        :param filter_criteria: (optional) FilterCriteria for the subscription
        """
        if not data_handler:
            data_handler = self.__get_content_notification_data
        path = getattr(container, "path", container)
        if not path.endswith("/subscriptions"):
            if not path.endswith("/contentInstances"):
                path += "/contentInstances"
            path += "/subscriptions"

        def content_handler(request):
            o = data_handler(request.json)
            self.logger.debug("Handler: %s", o)
            if True or o:  # ???
                handler(container, o)  # TODO: Transmit application ere as well
            return ""

        contact = "container_" + path.replace("/", "_")
        self._add_subscription(path, contact, content_handler, filter_criteria)

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
            interval = max(1, interval - interval * 0.25)

        self.logger.debug("Will update expiration time of %s in %s seconds",
                          instance, interval)
        self.runner.set_timer(interval, self.__updateExpTime,
                              instance=instance, extra_fields=extra_fields,
                              restore=restore)

    def start_refresher(self, instance, extra_fields=(), restore=None):
        self.__start_refresher(instance, extra_fields=extra_fields,
                               restore=restore)

    def __updateExpTime(self, instance=None, the_future=None, extra_fields=(),
                        interval=None, offset=None, restore=None):
        """ Updates a resource instance's expirationTime to the_future
        or a default value sometime in the future.

        :note: If instance is not provided or None or False, self.__app is updated.
        :note: Starts a new Timer.
        :param instance: resource instance to update
        :param the_future: new expirationTime value
        :param extra_fields: additional fields, needed in the update request
        :param interval: update interval
        :param offset: expirationTime offset (should be >0)
        :param restore: function that will restore the instance, if it has expired accidentally. Has to restart the refresher.
        :raise SCLNotFound: If the instance could not be found and no restore was provided.
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
        fields = ["expirationTime", ]
        fields.extend(extra_fields)
        if not instance:
            # does this happen if the instance was deleted?
            instance = self.__app
        instance.expirationTime = the_future
        try:
            self.mapper.update(instance, fields)
        except SCLNotFound as e:
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
        # NOTE: expirationTime might have been changed by SCL at this point.
        # update could/should return the updated instance in this case, but doesnt.
        # => additional GET to confirm expirationTime ?

        self.logger.debug("Will update expiration time in %s seconds", interval)
        self.runner.set_timer(interval, self.__updateExpTime,
                              instance=instance, extra_fields=extra_fields,
                              restore=restore)


NA = XA


class GA(XA):
    """ OpenMTC Gateway application.
    """

    @property
    def nscl(self):
        try:
            return self.__nscl
        except AttributeError:
            scls = self.mapper.get("/scls")
            try:
                path = scls.sclCollection[0].path
            except IndexError:
                scl = None
            else:
                self.__nscl = scl = self.mapper.get(path)

            return scl

    @property
    def scl(self):
        try:
            return self.__scl
        except AttributeError:
            self.__scl = scl = self.mapper.get("/")
            return scl

    def create_application(self, application, path="/applications",
                           retarget=False, access_right=True):
        if retarget:
            nscl = self.nscl
            if not nscl:
                raise SCLBadGateway("Not registered at an NSCL. Retargeting "
                                    "not possible")
            path = nscl.link + path
        return super(GA, self).create_application(application, path=path,
                                                  access_right=access_right)


DA = GA

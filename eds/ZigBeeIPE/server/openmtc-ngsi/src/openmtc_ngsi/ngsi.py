import json
import re
from base64 import b64encode, b64decode
from json import dumps, loads
from logging import DEBUG
from random import choice
from string import digits
from time import sleep
from urllib2 import urlopen, Request
from urlparse import urlparse, urlunparse, ParseResult

from openmtc.client.http import MIDClient
from openmtc.scl import CreateRequestIndication

from futile.logging import LoggerMixin
from futile.net.http import quote, unquote
from openmtc.exc import OpenMTCError, SCLNotFound, SCLError
from openmtc.model import Application, Container, Subscription
from openmtc_ngsi.db.SCLDb import SCLDb
from openmtc_ngsi.db.exc import DBEntityNotFound
from openmtc_ngsi.exc import NGSIError, InvalidRequest
from openmtc_ngsi.ngsi_json import NGSIJSONWriter
from openmtc_ngsi.requests import (RegisterContextResponse, EntityId,
                                   ContextRegistrationAttribute, DiscoverContextAvailabilityResponse,
                                   ContextRegistrationResponse, ContextRegistration, ContextMetadata,
                                   SubscribeContextAvailabilityResponse,
                                   UpdateContextAvailabilitySubscriptionResponse,
                                   UnsubscribeContextAvailabilityResponse, ContextElement,
                                   ContextElementResponse, UpdateContextResponse, QueryContextResponse,
                                   ContextAttribute, NotifyContextAvailabilityRequest, SubscribeContextResponse,
                                   SubscribeError, StatusCode, SubscribeResponse,
                                   UpdateContextRequest,
                                   UnsubscribeContextResponse, UpdateContextSubscriptionResponse)
from openmtc_ngsi.xml import NGSIXMLWriter


class NGSIInterface(LoggerMixin):
    content_instance_content_type = "application/openmtc-fiware-iot+json"
    id_prefix = "IoT"
    internal_app_id = id_prefix + "openmtc-ngsi"
    _internal_app_id_quoted = quote(internal_app_id)
    default_entity_type = "Generic"
    _last_notification = None

    def get_cfg(self, config, param):
        if param in config:
            return config[param]
        return None

    def __init__(self, scl=None, scl_uri=None, notify_uri=None, config=None,
                 db=None, send_rq=None, *args, **kw):
        super(NGSIInterface, self).__init__(*args, **kw)

        self.notify_uri = notify_uri
        try:
            self.client_secret = config["client_secret"]
            self.client_id = config["client_id"]
            self.username = config["username"]
            self.password = config["password"]
            scl_uri = self.get_cfg(config, "scl") or scl_uri or "http://localhost:5001"
            self.logger.info("Using %s as scl URI." % (scl_uri))
        except TypeError:
            try:
                config = open(config or "../config.cfg")
                cfg = json.load(config)
                self.client_secret = cfg["client_secret"]
                self.client_id = cfg["client_id"]
                self.username = cfg["username"]
                self.password = cfg["password"]
                scl_uri = self.get_cfg(cfg, "scl") or "http://localhost:5001"
                self.logger.info("Using %s as scl URI." % (scl_uri))

            except Exception as e:
                self.logger.error("Cannot load configuration file: %s" % (e, ))
                raise
        self.access_token = None
        if scl is None:
            scl =  MIDClient(scl_uri)
        self.scl = scl

        if send_rq is not None:
            self._send_req = send_rq

        self.db = db or SCLDb(self.scl, self.id_prefix, self, self.name)

        self.xml_writer = NGSIXMLWriter()
        self.json_writer = NGSIJSONWriter()

        self._init_subscriptions()

    def _init_subscriptions(self):
        self._check_subscriptions("/applications")

        apps = self.scl.retrieve("/applications").resource

        for app in apps.applicationCollection:
            if not self.is_internal_app(app.appId):
                #self._check_subscriptions(app["$t"] + "/containers")
                self._check_subscriptions("/applications/" + app.appId + "/containers")

    def _check_subscriptions(self, path):
        path += "/subscriptions"
        subscriptions = self.scl.retrieve(path).resource
        for subscription in subscriptions.subscriptionCollection:
            p = path+"/"+subscription.id
            subscription = self.scl.retrieve(p).resource
            if subscription.contact == self.notify_uri:
                return

        self._subscribe(path)

    def _subscribe(self, path):
        if not path.endswith("/subscriptions"):
            path += "/subscriptions"
        self.scl.create(path, Subscription(contact=self.notify_uri))

    def is_internal_app(self, app_id):
        return app_id in (self._internal_app_id_quoted, self.internal_app_id)

    def split_app_id(self, app_id):
        app_id = unquote(app_id)

        entity_type, entity_id = "Generic", app_id

        if app_id.startswith(self.id_prefix):
            app_id = app_id[len(self.id_prefix):]
            try:
                entity_type, entity_id = app_id.split(".")
            except ValueError:
                pass

        return entity_type, entity_id

    def _get_appdata(self):
        scl_applications = self.scl.retrieve("/applications").resource

        app_data = []
        for scl_app_reference in scl_applications.applicationCollection:
            if self.is_internal_app(scl_app_reference.appId):
                continue

            entity_type, entity_id = self.split_app_id(scl_app_reference.appId)

            app_data.append((entity_type, entity_id, '/applications/' + scl_app_reference.appId))

        return app_data

    def _get_relevant_apps(self, request):
        return self._get_relevant_apps_dict(request).values()

    def _get_relevant_apps_dict(self, request):
        if not request.entityIdList:
            raise InvalidRequest("entityIdList missing in request.")

        app_data = self._get_appdata()

        relevant_apps = {}

        for entityId in request.entityIdList:
            for entity_type, entity_id, path in app_data:
                if not entityId.type or entityId.type == entity_type:
                    if entityId.isPattern:
                        if re.match(entityId.id, entity_id):
                            relevant_apps[entityId] = (entity_type, entity_id, path)
                    elif not entityId.id or entityId.id == entity_id:
                        relevant_apps[entityId] = (entity_type, entity_id, path)
        return relevant_apps

    def id_matches(self, entity_type, is_pattern, entity_id, app_type, app_id):
        if entity_type and entity_type != app_type:
            return False
        if is_pattern:
            return bool(re.match(entity_id, app_id))
        return not entity_id or entity_id == app_id

    def _get_relevant_app(self, entityId, app_data):
        for entity_type, entity_id, path in app_data:
            self.logger.debug("---- check %s %s", entity_type, entity_id)
            if entityId.id == entity_id: # and (not entityId.type or entityId.type == entity_type)
                return entity_type, entity_id, path

    def _create_content_instance(self, path, content):
        content_instance_data = {
            "content": {
                "contentType": self.content_instance_content_type,
                "$t": b64encode(dumps(content))
            }
        }
        from openmtc.model import ContentInstance
        ci = ContentInstance(
            content={
                "contentType": self.content_instance_content_type,
                "$t": b64encode(dumps(content))
            }
        )
        request_indication = CreateRequestIndication(path, ci, "contentInstance")
        return self.scl.send_request_indication(request_indication)
    create_content_instance = _create_content_instance

    def _marshal_metadata(self, entity):
        if not entity.metadata:
            return []

        return [
            {
                "name": md.name or "",
                "type": md.type or "",
                "value": md.value or ""
            } for md in entity.metadata
        ]

    def _parse_metadata(self, meta_data):
        return [ContextMetadata(name=md["name"], type=md["type"], value=md["value"]) for md in meta_data]

    def _get_latest_instance(self, content_instances):
        latest = content_instances["latest"]
        latest_id = latest["id"]
        for content_instance in content_instances["contentInstanceCollection"]["contentInstance"]:
            if latest_id == content_instance["id"]:
                return content_instance
        raise Exception("Latest instance (%s) not found in collection." % (latest, ))

    def get_content_instances(self, path):
        if not path.endswith("/contentInstances"):
            path += "/contentInstances"

        content_instances = self.scl.retrieve(path).resource

        for content_instance in content_instances.contentInstanceCollection:
            try:
                data = content_instance.content["$t"]
            except KeyError:
                data = content_instance.content["binaryContent"]
            try:
                data = b64decode(data)
                data = loads(data)
            except:
                self.logger.exception("Could not decode content: %s" % (data, ))

            yield (content_instance, data)

    def _get_access_token(self, url):
        """Returns the current access token.

        Generates a new access token if no current access token can be found"""
        if self.access_token:
            return self.access_token
        data = "client_id=%s&client_secret=%s&grant_type=password&username=%s&password=%s&scope=write" %\
            (self.client_id, self.client_secret, self.username, self.password)

        parsed = urlparse(url)
        path = urlunparse(ParseResult(parsed.scheme, parsed.netloc, "/oauth2/access_token", None, None, None))

        auth_resp = urlopen(Request(path, data), timeout=10)
        if auth_resp.getcode() != 200:
            self.logger.error("Error with client credentials")
            return self.access_token
        auth_resp_data = json.loads(auth_resp.read())

        if "access_token" in auth_resp_data:
            self.access_token = auth_resp_data["access_token"]
        else:
            self.logger.error("Error with client credentials")
        return self.access_token

    def _send_req(self, notify_request, content_type, subscription):
        """Sends a notify request to the Event Service with a given access token.

        If the access token has expired, this function calls _get_access_token that generates a new one"""
        if content_type == "json":
            feed = urlopen(
                Request(
                    subscription["reference"],
                    self.json_writer.serialize(notify_request),
                    {
                        "Content-Type": "application/json",
                        "Authorization": "OAuth " + self._get_access_token(subscription["reference"])
                    }
                ),
                timeout=10)
            if feed.getcode() == 401:
                # Access_token has expired
                self.access_token = None
                feed = urlopen(
                    Request(
                        subscription["reference"],
                        self.json_writer.serialize(notify_request),
                        {
                            "Content-Type": "application/json",
                            "Authorization": "OAuth " + self._get_access_token(subscription["reference"])
                        }
                    ),
                    timeout=10)

        else:
            feed = urlopen(
                Request(
                    subscription["reference"],
                    self.xml_writer.serialize(notify_request),
                    {"Content-Type": "application/xml"}
                ),
                timeout=10)
        return feed

    def _send_notifications(self, subscriptions, notify_request):
        """Pushes content to the event service.

        First tries to update the event,
        if it is impossible, this function creates a new event (APPEND)"""
        for subscription in subscriptions:
            if self.logger.isEnabledFor(DEBUG):
                self.logger.debug("Sending notification: %s", self.xml_writer.serialize(notify_request))
            else:
                print "Sending notification: %s"%self.xml_writer.serialize(notify_request)
            try:
                notify_request.subscriptionId = subscription["subscriptionId"]
            except AttributeError:
                # req is an update
                try:
                    feed = self._send_req(notify_request, "json", subscription)
                except Exception as e:
                    self.logger.error("Failed to send notification to %s: %s", subscription["reference"], e)

                try:
                    repload = json.loads(feed.read())
                    respcode = int(repload["contextResponses"][0]["statusCode"]["code"])
                    if respcode == 472 or respcode == 404:
                        self.logger.info("Update notification failed, trying append")
                        notify_request.updateAction = "APPEND"
                        self._send_req(notify_request, "json", subscription)
                except Exception as e:
                    self.logger.error("Failed to send notification to %s: %s", subscription["reference"], e)
            else:
                try:
                    self._send_req(notify_request, "xml", subscription)
                except Exception as e:
                    self.logger.error("Failed to send notification to %s: %s", subscription["reference"], e)

    def handle_notification(self, type, notification):
        self._last_notification = (type, notification)

        if type not in ("applications", "containers"):
            raise InvalidRequest(type)

        singular = type[:-1]

        collection = notification[singular + "Collection"]["namedReference"]
        try:
            latest = collection[-1]
        except IndexError:
            return False

        if ((type == "applications" and self.is_internal_app(latest["id"])) or
                (type == "containers" and unquote(latest["id"]).endswith(":meta"))):
            return False

        getattr(self, "_handle_" + singular)(latest, collection)
        return True

    def _handle_application(self, latest_app, collection):
        self._subscribe(latest_app["$t"] + "/containers")
        app_type = ""
        app_id = latest_app["id"]
        subs = self.db.find_app_subscriptions(app_type, app_id)
        # TODO send notifications
        # TODO build cr
        cr = ContextRegistration(entityIdList=[ EntityId(type=app_type, id=app_id, isPattern=False) ],
                                contextRegistrationAttributeList= [],#ContextRegistrationAttribute],
                                registrationMetaData= [],
                                providingApplication="eu.fistar.sdcs")
        crr = ContextRegistrationResponse(contextRegistration=cr)
        notify_request = NotifyContextAvailabilityRequest(contextRegistrationResponseList=[ crr ],
                                                          errorCode=StatusCode(200))
        self._send_notifications(subs, notify_request)
        # TODO alternative: send a RegisterContextRequest?
        # register_request = RegisterContextRequest(contextRegistrationList=[ cr ])
        # self._send_notifications(subs, register_request)

    def _handle_container(self, container, collection):
        pass


class NGSI_9(NGSIInterface):
    name = "ngsi9"

    def __init__(self, scl=None, scl_uri=None, notify_uri="http://localhost:5050/_notify/9", config=None, *args, **kw):
        super(NGSI_9, self).__init__(scl=scl, scl_uri=scl_uri, notify_uri=notify_uri, config=config, *args, **kw)

    def registerContext(self, registerContextRequest):

        registrationId = ''.join([choice(digits) for _ in range(16)])

        for contextRegistration in registerContextRequest.contextRegistrationList:
            for entityId in contextRegistration.entityIdList:
                #app_id = entityId.type
                #app_id = app_id and quote(app_id) or self.default_entity_type
                #app_id += "." + quote(entityId.id)
                #app_id = self.id_prefix + app_id
                app_id = quote(entityId.id)

                app = Application(appId=app_id)

                try:
                    scl_app_id = self.scl.create("/applications", app).resourceURI
                    scl_containers_id = scl_app_id + "/containers"

                    if contextRegistration.contextRegistrationAttributeList:
                        sleep(1)
                        try:
                            for contextRegistrationAttribute in contextRegistration.contextRegistrationAttributeList:
                                container_id = quote(contextRegistrationAttribute.name)

                                container = Container(id=container_id)
                                meta_container = Container(id=container_id + ".meta")

                                self.scl.create(scl_containers_id, container)
                                scl_meta_container_id = self.scl.create(scl_containers_id, meta_container).resourceURI

                                metadata = {
                                    "type": contextRegistrationAttribute.type,
                                    "isDomain":  contextRegistrationAttribute.isDomain,
                                    "metadata": self._marshal_metadata(contextRegistrationAttribute)
                                }

                                self._create_content_instance(scl_meta_container_id + "/contentInstances", metadata),

                            sleep(len(contextRegistration.contextRegistrationAttributeList))
                        except OpenMTCError:
                            #self.scl.delete(scl_app_id)
                            return False
                            raise
                except OpenMTCError as e:
                    return False
                    raise NGSIError(e)

        response = RegisterContextResponse(
            errorCode=200,
            duration=3600 * 24,
            registrationId=registrationId
        )

        response._m2m_path = scl_app_id

        return response

    def discoverContextAvailability(self, discoverContextAvailabilityRequest):
        relevant_apps = self._get_relevant_apps(discoverContextAvailabilityRequest)

        result_apps = set()
        attributes = []
        cache = {}

        for entity_type, entity_id, path in relevant_apps:
            containers_path = path + "/containers"

            try:
                containers = cache[containers_path]
            except KeyError:
                containers = cache[containers_path] = self.scl.retrieve(containers_path).resource

            for reference in containers.containerCollection:
                if (not unquote(reference.id).endswith(":meta") and
                    (not discoverContextAvailabilityRequest.attributeList or
                        reference.id in discoverContextAvailabilityRequest.attributeList)):
                    result_apps.add((entity_type, entity_id))

                    try:
                        metadata = cache[reference.id]
                    except KeyError:
                        try:
                            #ci_path = unquote(reference["$t"]) + ":meta/contentInstances"
                            ci_path = unquote(containers_path+'/'+reference.id) + ":meta/contentInstances"
                            meta_content_instances = self.scl.retrieve(quote(ci_path)).resource
                            b64json = meta_content_instances.contentInstanceCollection[0].content["$t"]
                            metadata = cache[reference.id] = loads(b64decode(b64json))
                        except SCLNotFound:
                            metadata = cache[reference.id] = {
                                "type": "Generic",
                                "isDomain": False,
                                "metadata": []
                            }

                        attributes.append((reference.id, metadata))

        if not result_apps:
            return DiscoverContextAvailabilityResponse(errorCode=404)

        entity_ids = [EntityId(type=entity_type, id=entity_id, isPattern=False)
                      for entity_type, entity_id in result_apps]

        context_attributes = []

        for name, metadata in attributes:
            context_attributes.append(
                ContextRegistrationAttribute(
                    name=name,
                    type=metadata["type"],
                    isDomain=metadata["isDomain"],
                    metadata=[
                        ContextMetadata(
                            type=md["type"],
                            name=md["name"],
                            value=md["value"]
                        ) for md in metadata["metadata"]
                    ]
                )
            )

        return DiscoverContextAvailabilityResponse(
            errorCode=200,
            contextRegistrationResponseList=[
                ContextRegistrationResponse(
                    contextRegistration=
                        ContextRegistration(
                            entityIdList=entity_ids,
                            contextRegistrationAttributeList=context_attributes
                        )

                )
            ]
        )

    def subscribeContextAvailability(self, subscribeContextAvailabilityRequest):
        #relevant_apps = self._get_relevant_apps(subscribeContextAvailabilityRequest)

        if not subscribeContextAvailabilityRequest.entityIdList:
            raise InvalidRequest("entityIdList missing.")

        if not subscribeContextAvailabilityRequest.reference:
            raise InvalidRequest("reference missing.")

        subscription_data = {
            "reference": subscribeContextAvailabilityRequest.reference,
            "entityIdList": tuple(set([(e.type, e.isPattern, e.id)
                for e in subscribeContextAvailabilityRequest.entityIdList
            ])),
            "attributeList": (subscribeContextAvailabilityRequest.attributeList is not None and
                    tuple(set(filter(None, subscribeContextAvailabilityRequest.attributeList))) or ()),
            "isCtxAvSub": True
        }

        subscription_id = self.db.add_subscription(subscription_data)

        return SubscribeContextAvailabilityResponse(
            subscriptionId=subscription_id,
            duration=subscribeContextAvailabilityRequest.duration or 24 * 3600
        )

    def unsubscribeContextAvailability(self, unsubscribeContextAvailabilityRequest):
        try:
            self.db.delete_subscription(unsubscribeContextAvailabilityRequest.subscriptionId)
            statusCode = 200
        except DBEntityNotFound:
            statusCode = 404

        return UnsubscribeContextAvailabilityResponse(
            statusCode=statusCode,
            subscriptionId=unsubscribeContextAvailabilityRequest.subscriptionId
        )

    def updateContextAvailabilitySubscription(self, updateContextAvailabilitySubscriptionRequest):
        if updateContextAvailabilitySubscriptionRequest.subscriptionId:
            try:
                self.scl.delete(updateContextAvailabilitySubscriptionRequest.subscriptionId)
            except SCLError:
                pass

        r = self.subscribeContextAvailability(updateContextAvailabilitySubscriptionRequest)

        return UpdateContextAvailabilitySubscriptionResponse(
            subscriptionId=r.subscriptionId,
            duration=r.duration
        )

    def _get_attribute_metadata(self, path):
        if not path.endswith(":meta"):
            path = quote(unquote(path) + ":meta")

        _content_instance, data = list(self.get_content_instances(path))[0]

        return (data["type"], data["isDomain"], self._parse_metadata(data["metadata"]))

    def _handle_application(self, latest_app, collection):
        subscriptions = self.db.find_app_subscriptions(*self.split_app_id(latest_app["id"]))

        if subscriptions:
            app_type, app_id = self.split_app_id(latest_app["id"])
            #application = self.scl.retrieve(latest_app["$t"])[1]

            notify_request = NotifyContextAvailabilityRequest(
                errorCode=200,
                contextRegistrationResponseList=[
                    ContextRegistrationResponse(
                        errorCode=200,
                        contextRegistration=
                            ContextRegistration(
                                entityIdList=[
                                    EntityId(
                                        type=app_type,
                                        id=app_id
                                    )
                                ]
                            )

                    )
                ]
            )

            self._send_notifications(subscriptions, notify_request)

        super(NGSI_9, self)._handle_application(latest_app, collection)

    def _handle_container(self, container, collection):
        app_id = container["$t"].rsplit("/", 2)[0].rpartition("/")[-1]
        subscriptions = self.db.find_container_subscriptions(*self.split_app_id(app_id), attribute=container["id"])

        if subscriptions:
            app_type, app_id = self.split_app_id(app_id)
            attributes = []

            sleep(1)

            for attribute in collection:
                type, isDomain, metadata = self._get_attribute_metadata(attribute["$t"])
                attributes.append(
                    ContextRegistrationAttribute(
                        name=attribute["id"],
                        type=type,
                        isDomain=isDomain,
                        metadata=metadata
                    )
                )

            notify_request = NotifyContextAvailabilityRequest(
                errorCode=200,
                contextRegistrationResponseList=[
                    ContextRegistrationResponse(
                        errorCode=200,
                        contextRegistration=
                            ContextRegistration(
                                entityIdList=[
                                    EntityId(
                                        type=app_type,
                                        id=app_id
                                    )
                                ],
                                contextRegistrationAttributeList=attributes
                            )

                    )
                ]
            )

            self._send_notifications(subscriptions, notify_request)

        super(NGSI_9, self)._handle_container(container, collection)


class NGSI_10(NGSIInterface):
    name = "ngsi10"

    def __init__(self, scl=None, scl_uri=None, notify_uri="http://localhost:5050/_notify/10", config=None, send_rq=None, *args, **kw):
        super(NGSI_10, self).__init__(scl=scl, scl_uri=scl_uri, notify_uri=notify_uri, config=config, send_rq=send_rq, *args, **kw)

    def _get_context_attribute_value(self, content_instances):
        latest = self._get_latest_instance(content_instances)["content"]

        try:
            data = b64decode(latest["$t"])
        except ValueError:
            return {"contextValue": latest["$t"], "metadata": None, "type": "", "name": ""}

        if latest["contentType"] == self.content_instance_content_type:
            data = loads(data)
            data["metadata"] = self._parse_metadata(data["metadata"])
        else:
            data = {
                "type": "", "name": "",
                "contextValue": data,
                "metadata": [ContextMetadata(name="contentType",
                                             type="str", value=latest["contentType"])]
            }

        return data

    def queryContext(self, queryContextRequest):
        responses = []

        relevant_apps_dict = self._get_relevant_apps_dict(queryContextRequest)

        for entityId in queryContextRequest.entityIdList:
            app_data = relevant_apps_dict.get(entityId)

            if app_data is None:
                responses.append(
                    ContextElementResponse(
                        contextElement=ContextElement(entityId=entityId),
                        statusCode=404
                    )
                )
            else:
                entity_type, entity_id, app_path = app_data
                for attribute in queryContextRequest.attributeList:
                    content_instances_id = app_path + "/containers/" + attribute + "/contentInstances"

                    contextAttribute = ContextAttribute(name=attribute)

                    try:
                        content_instances = self.scl.retrieve(content_instances_id).resource
                    except SCLError as e:
                        self.logger.exception("Could not get container for: %s:%s-%s" %
                                              (entity_type, entity_id, attribute))
                        statusCode = e[1].status
                    else:
                        if content_instances["currentNrOfInstances"] < 1:
                            statusCode = 404
                        else:
                            data = self._get_context_attribute_value(content_instances)
                            contextAttribute.contextValue = data["contextValue"]
                            contextAttribute.metadata = data["metadata)"]
                            contextAttribute.type = data["type"]
                            contextAttribute.name = data["name"] or attribute

                            statusCode = 200

                    responses.append(
                        ContextElementResponse(
                            contextElement=ContextElement(
                                entityId=entityId,
                                contextAttributeList=[contextAttribute]
                            ),
                            statusCode=statusCode
                        )
                    )

        return QueryContextResponse(
            errorCode=200,
            contextResponseList=responses
        )

    def subscribeContext(self, subscribeContextRequest):
        try:
            if not subscribeContextRequest.entityIdList:
                raise InvalidRequest("entityIdList missing in request.")

            if not subscribeContextRequest.reference:
                raise InvalidRequest("reference missing in request.")

            subscription_data = {
                "reference": subscribeContextRequest.reference,
                "entityIdList": tuple(set([(e.type, e.isPattern, e.id)
                    for e in subscribeContextRequest.entityIdList
                ])),
                "attributeList": (subscribeContextRequest.attributeList is not None and
                    tuple(set(filter(None, subscribeContextRequest.attributeList))) or ()),
                "isCtxAvSub": False
            }

            subscription_id = self.db.add_subscription(subscription_data)

            return SubscribeContextResponse(
                subscribeResponse=SubscribeResponse(
                    duration=24 * 3600,
                    subscriptionId=subscription_id,
                    throttling=0
                )
            )

        except InvalidRequest as e:
            errorCode = StatusCode(400, details=str(e))
        except Exception as e:
            self.logger.exception("Error in subscribeContext")
            errorCode = 500

        return SubscribeContextResponse(
            subscribeError=SubscribeError(
                errorCode=errorCode
            )
        )

    def updateContextSubscription(self, updateContextSubscriptionRequest):
        if not updateContextSubscriptionRequest.subscriptionId:
            errorCode = StatusCode(400, details="subscriptionId missing in request.")
        else:
            return UpdateContextSubscriptionResponse(
                subscribeResponse=SubscribeResponse(
                    duration=24 * 3600,
                    subscriptionId=updateContextSubscriptionRequest.subscriptionId,
                    throttling=0
                )
            )

        return UpdateContextSubscriptionResponse(
            subscribeError=SubscribeError(errorCode=errorCode)
        )

    def unsubscribeContext(self, unsubscribeContextRequest):
        if not unsubscribeContextRequest.subscriptionId:
            statusCode = StatusCode(400, details="subscriptionId missing in request.")
        else:
            try:
                self.db.delete_subscription(unsubscribeContextRequest.subscriptionId)
                statusCode = 200
            except DBEntityNotFound:
                statusCode = StatusCode(404, "subscription not found.")

        return UnsubscribeContextResponse(
            subscriptionId=unsubscribeContextRequest.subscriptionId,
            statusCode=statusCode
        )

    def updateContext(self, updateContextRequest):
        responses = []
        all_apps = self._get_appdata()

        for contextElement in updateContextRequest.contextElementList:
            if not contextElement.entityId or contextElement.entityId.isPattern or not contextElement.entityId.id:
                responses.append(
                    ContextElementResponse(
                        contextElement=ContextElement(entityId=contextElement.entityId),
                        statusCode=400
                    )
                )
                continue

            app_data = self._get_relevant_app(contextElement.entityId, all_apps)

            if app_data is None:
                responses.append(
                    ContextElementResponse(
                        contextElement=ContextElement(entityId=contextElement.entityId),
                        statusCode=404
                    )
                )
                continue

            entity_type, entity_id, app_path = app_data

            for contextAttribute in contextElement.contextAttributeList:
                if not contextAttribute.contextValue:
                    statusCode = 400
                else:
                    content_instances_id = app_path + "/containers/" + contextAttribute.name + "/contentInstances"

                    content_instance_data = {
                        "contextValue": contextAttribute.contextValue,
                        "type": contextAttribute.type,
                        "name": contextAttribute.name,
                        "metadata": self._marshal_metadata(contextAttribute)
                    }

                    try:
                        self._create_content_instance(content_instances_id, content_instance_data)
                        statusCode = 200
                    except SCLError as e:
                        self.logger.exception("Could not get container for %s: %s:%s-%s (%s)",
                                              updateContextRequest.updateAction, entity_type, entity_id,
                                              contextAttribute.name, content_instances_id)
                        statusCode = e[1].status

                responses.append(
                    ContextElementResponse(
                        contextElement=ContextElement(
                            entityId=contextElement.entityId,
                            contextAttributeList=[contextAttribute]
                        ),
                        statusCode=statusCode
                    )
                )

        return UpdateContextResponse(
            errorCode=200,
            contextResponseList=responses
        )

    def _handle_container(self, container, collection):
        #self._subscribe(container["$t"] + "/contentInstances")
        #raise Exception("huh")
        # subscribe to all containers, not just latest
        # TBD: issues if already subscribed to a container?
        for c in collection:
            self._subscribe(c["$t"] + "/contentInstances")

    def handle_notification(self, type, notification):
        """Handles different notifications from SCL subscriptions.
        :param type: String containing 'applications', 'containers', 'contentinstances'
        """
        print "Notified ! %s"%type
        if type != "contentInstances":
            return super(NGSI_10, self).handle_notification(type, notification)

        if not notification["currentNrOfInstances"]:
            return False

        container_id = notification["subscriptionsReference"].rsplit("/", 2)[0].rpartition("/")[-1]
        app_id = notification["subscriptionsReference"].rsplit("/", 4)[0].rpartition("/")[-1]

        app_type, app_id = self.split_app_id(app_id)
        subscriptions = self.db.find_container_subscriptions(app_type, app_id, attribute=container_id)
        if subscriptions:
            data = self._get_context_attribute_value(notification)
            """
            notify_request = NotifyContextRequest(
                contextResponseList = [
                    ContextElementResponse(
                        statusCode = 200,
                        contextElement = ContextElement(
                            entityId = EntityId(type = app_type, id = app_id, isPattern = False),
                            contextAttributeList = [
                                ContextAttribute(
                                    name = data["name"] or container_id,
                                    contextValue = data["contextValue"],
                                    metadata = data["metadata"],
                                    type = data["type"]
                                )
                            ]
                        )
                    )
                ]
            )
            """
            update_request = UpdateContextRequest(
                contextElementList=[
                    ContextElement(
                        entityId=EntityId(type=app_type, id=app_id, isPattern=False),
                        contextAttributeList=[
                            ContextAttribute(
                                name=data["name"] or container_id,
                                contextValue=str(data["contextValue"]),
                                metadata=data["metadata"],
                                type=data["type"]
                            )
                        ]
                    )
                ],
                updateAction="UPDATE"
            )

            self._send_notifications(subscriptions, update_request)

        #raise Exception(latest, container_id, app_id)

        return True

from openmtc_server.Plugin import Plugin
from openmtc_etsi.model import NotificationChannel
from collections import deque
from aplus import Promise
from openmtc_etsi.exc import SCLMethodNotAllowed, SCLNotFound
from urlparse import urlparse
from openmtc_etsi.response import RetrieveResponseConfirmation,\
    NotifyResponseConfirmation
from openmtc_server.util import uri_safe
from openmtc_scl.mappingfunction import map_request_to_request_indication,\
    map_response_confirmation_to_response
from openmtc_server.transportdomain import RequestMethod, ErrorResponse,\
    ResponseCode

PREFIX = "/nc"


class NotificationChannelHandler(Plugin):
    def _init(self):
        #TODO: gather existing channels at start (or store them)
        lp_timeout = float(self.config.get("long_polling_timeout", 60))

        self.long_polling_timeout = lp_timeout

        self.queues = {}
        self.waiting = {}

        self.events.resource_created.register_handler(self.channel_created,
                                                      NotificationChannel)
        self.events.resource_deleted.register_handler(self.channel_deleted,
                                                      NotificationChannel)

        self.api.register_client(("nc", ), self.send_request)

        connectors = self.api.get_connectors(None, self._handle_connector)
        map(self._handle_connector, connectors)

        self._initialized()

    def _handle_connector(self, connector):
        connector.register_route(PREFIX, self.handle_request)

    def handle_request(self, request):
        request_indication = map_request_to_request_indication(request)
        #TODO: "check authorization of requestingEntity based on default access rights"

        p = Promise()

        if request_indication.method != "retrieve":
            return p.reject(SCLMethodNotAllowed(request_indication.method))

        path = urlparse(request_indication.path).path

        channel_id = path[len(PREFIX) + 1:]

        try:
            notification, content_type = self.queues[channel_id].popleft()
        except KeyError:
            self.logger.info("Polling on unknown channel: %s", channel_id)
            return p.reject(SCLNotFound(path))
        except IndexError:
            #TODO: handle timeouts
            self.waiting[channel_id].append(p)
        else:
            response_confirmation = RetrieveResponseConfirmation(notification,
                                                                 content_type)
            response = map_response_confirmation_to_response(request, response_confirmation)
            p.fulfill(response)

        self.logger.debug("Returning channel promise: %s", p.isPending())
        return p

    def send_request(self, request):
        p = Promise()

        if request.method not in (RequestMethod.create, RequestMethod.notify):
            return p.reject(ErrorResponse(ResponseCode.method_not_allowed, RequestMethod, "text/plain"))

        request_indication = map_request_to_request_indication(request)

        notification = request_indication.resource
        content_type = request_indication.content_type

        channel_id = urlparse(request_indication.path).path[1:]

        self.logger.debug("Received notification on channel '%s' (%s)", channel_id, request_indication.path)

        try:
            waiting = self.waiting[channel_id]
        except KeyError:
            return p.reject(SCLNotFound(request_indication.path))

        if waiting:
            self.waiting[channel_id] = []

            response_confirmation = RetrieveResponseConfirmation(notification,
                                                                 content_type)

            response = map_response_confirmation_to_response(request, response_confirmation)

            for waiting_promise in waiting:
                waiting_promise.fulfill(response)
        else:
            self.queues[channel_id].append((notification, content_type))

        response = map_response_confirmation_to_response(request, NotifyResponseConfirmation())
        return p.fulfill(response)

    def channel_created(self, instance,  request_indication):
        channel_id = uri_safe(instance.path)
        self.logger.debug("Created notificationChannel: %s", channel_id)
        self.queues[channel_id] = deque()
        self.waiting[channel_id] = []

    def channel_deleted(self, instance, request_indication):
        channel_id = uri_safe(request_indication.path)
        self.logger.debug("Removing notificationChannel: %s", channel_id)
        del self.queues[channel_id]
        for p in self.waiting[channel_id]:
            p.reject(SCLNotFound("notificationChannel was removed"))
        del self.waiting[channel_id]

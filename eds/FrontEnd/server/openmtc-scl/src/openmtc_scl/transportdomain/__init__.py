from urlparse import urlparse, urlsplit
from aplus import Promise
from openmtc_etsi.exc import OpenMTCError
from openmtc_etsi.response import (ErrorResponseConfirmation,
                                   SuccessResponseConfirmation)
from CommunicationChannelManager import CommunicationChannelManager
from datetime import datetime
from iso8601 import parse_date
from openmtc_server import Component
from openmtc_scl.mappingfunction import (
    map_request_indication_to_request, map_response_to_response_confirmation,
    get_etsi_request_mapper, map_error_response_to_error_response_confirmation)
from openmtc_scl import ETSIEndpointType, ETSIEndpoint
from funcy.seqs import flatten
from openmtc_server.util import join_url
from openmtc_server.transportdomain import ConnectorSpec


class ETSITransportDomain(Component):
    def __init__(self, config, *args, **kw):
        """
        Create and initialize the transport domain.
        """

        super(ETSITransportDomain, self).__init__(*args, **kw)

        self._api = None

        self.config = config
        self.etsi_config = self.config["etsi"]

        self._mid_endpoints = []
        self._mia_endpoints = []
        self._dia_endpoints = []

        self.scl_base = self.etsi_config["scl_base"]

    def _init_connectors(self, specs, handler):
        connectors = [self._api.get_connectors(ConnectorSpec(**spec), handler)
                      for spec in specs or (None, )]
        map(handler, flatten(connectors))

    def initialize(self, api):
        self._api = api
        self.__init_saf()

        if self.etsi_config["dIa"] is not None:
            self._init_connectors(self.etsi_config["dIa"]["connectors"],
                                  self._handle_dia_connector)
        if self.etsi_config["mIa"] is not None:
            self._init_connectors(self.etsi_config["mIa"]["connectors"],
                                  self._handle_mia_connector)
        if self.etsi_config["mId"] is not None:
            self._init_connectors(self.etsi_config["mId"]["connectors"],
                                  self._handle_mid_connector)

    def _handle_mid_connector(self, connector):
        if not connector.is_wan:
            return
        self.logger.debug("Registering mId endpoint on %s", connector)
        mapping_function = get_etsi_request_mapper(
            self._api.handle_request_indication, ETSIEndpointType.mId)
        connector.register_route(self.scl_base, mapping_function)
        self._mid_endpoints.append(ETSIEndpoint(
            ETSIEndpointType.mId, join_url(connector.base_uri, self.scl_base)))

    def _handle_mia_connector(self, connector):
        if connector.is_wan:
            return
        self.logger.debug("Registering mIa endpoint on %s", connector)
        mapping_function = get_etsi_request_mapper(
            self._api.handle_request_indication, ETSIEndpointType.mIa)
        connector.register_route(self.scl_base, mapping_function)
        self._mia_endpoints.append(ETSIEndpoint(
            ETSIEndpointType.mIa, join_url(connector.base_uri, self.scl_base)))

    def _handle_dia_connector(self, connector):
        if connector.is_wan:
            return
        self.logger.debug("Registering dIa endpoint on %s", connector)
        mapping_function = get_etsi_request_mapper(
            self._api.handle_request_indication,  ETSIEndpointType.dIa)
        connector.register_route(self.scl_base, mapping_function)
        self._dia_endpoints.append(ETSIEndpoint(
            ETSIEndpointType.dIa, join_url(connector.base_uri, self.scl_base)))

    def get_mid_endpoints(self, scheme=None):
        endpoints = self._mid_endpoints
        if scheme:
            endpoints = [e for e in endpoints
                         if urlsplit(e.base_uri).scheme == scheme]
        return endpoints

    def get_mid_uri(self, scheme=None):
        try:
            return self.get_mid_endpoints(scheme)[0].base_uri
        except IndexError:
            if not scheme:
                raise OpenMTCError("No mId endpoint exists")
            raise OpenMTCError("No mId endpoint for %s exists" % (scheme, ))

    def start(self):
        pass

    def stop(self):
        pass

    def save_req(self, req):
        """Saves a request in database using its correlationID.

        :param req: RequestIndication to be saved
        :return: Promise(database result)
        """
        def go(shelve):
            self.logger.debug("Saving req with rcat %s and correlationID %s",
                              req.rcat, req.correlationID)
            return shelve.setitem(req.correlationID, req).then(shelve.commit)
        return self._api.db.get_shelve("rcat_%s" % req.rcat).then(go)

    def load_req(self, rcat, correlationID):
        """Loads a request from database using correlationID and rcat.

        :param rcat: Request category of the request
        :param correlationID: correlationId of the request
        :return: Promise(RequestIndication)
        """
        def go(shelve):
            self.logger.debug("Loading req with rcat %s and correlationID %s" %
                              (rcat, correlationID))
            req = shelve.get(correlationID)
            shelve.commit()
            return req
        return self._api.db.get_shelve("rcat_%s" % rcat).then(go)

    def load_reqs(self, rcat):
        """Loads a list of requests from database matching an rcat.

        :param rcat: Request category of the requests
        :return: Promise(List of RequestIndication)
        """
        def go(shelve):
            self.logger.debug("Loading requests for rcat %s"%rcat)
            reqs = shelve.items()
            shelve.commit()
            return reqs
        return self._api.db.get_shelve("rcat_%s" % rcat).then(go)

    def del_req(self, rcat, correlationID):
        """Deletes a request from database using correlationID and rcat.

        :param rcat: Request category of the request
        :param correlationID: correlationId of the request
        :return: Promise(True)
        """
        def go(shelve):
            self.logger.debug("Deleting req with rcat %s and correlationID %s",
                              rcat, correlationID)
            # TODO: use delitem?
            shelve.pop(correlationID)
            shelve.commit()
            return True
        return self._api.db.get_shelve("rcat_%s" % rcat).then(go)

    def __init_saf(self):
        """Initalizes Store and Forward specific variables"""
        self.__cb = {}

        self.__timers = {}

        self.CommunicationChannelManager = CommunicationChannelManager()
        self.current_channel = None

    def get_etsi_client(self, scheme):
        try:
            return self.__clients[scheme]
        except KeyError:
            raise OpenMTCError("Unknown protocol: %s" % (scheme, ))

    def register_connectivity_handler(self, process_connectivity_request):
        """Registers an handler used when connectivity information is needed.

        :param process_connectivity_request: function expecting rcat and
                                             potential channel_name as
                                             parameters and returning
                                             tuple(channel_name, rcat)
        """
        self.CommunicationChannelManager.register_connectivity_handler(
            process_connectivity_request)

    def expired_timer(self, request_indication):
        """This function is triggered when the timer corresponding to the TRPDT
        of a RequestIndication expires."""
        try:
            del self.__timers[request_indication.correlationID]
        except KeyError:
            pass
        self.logger.debug("Timer expired with correlationID %s",
                          request_indication.correlationID)

        channel = self.CommunicationChannelManager.get_channel(
            int(request_indication.rcat),
            0,
            self.send_pending_requests
        )
        if channel:
            self.logger.debug("Using existing channel %s" % channel)
            self.send_pending_requests(channel, request_indication.rcat)

    def _set_timer(self, request_indication, trpdt, f):
        """Launches a timer corresponding to a RequestIndication TRPDT

        :param request_indication: RequestIndication stored
        :param trdpt: Waiting time, in seconds
        :param f: handler triggered when timer is over (expired_timer)
        """
        self.logger.debug("Setting up timer for %f s" % trpdt)
        if trpdt == 0.0:
            self._api.run_task(lambda: self.expired_timer(request_indication))
        else:
            # TODO: timers are local,
            #   what if req are sent by another proc in cloud
            cid = request_indication.correlationID
            self.__timers[cid] = self._api.set_timer(trpdt, f)

    def set_store_forward_cb(self, cb, request_indication):
        """Saves a RequestIndication and triggers the Store and Forward
         functionalities.

        Calls back cb when a response is ready.

        :param cb: Callback function to the methoddomain used when a response is
                   ready
        :param request_indication: RequestIndication to be stored and forwarded.
        """
        request_indication.rcat = int(request_indication.rcat)

        def go(req):
            if not req:
                _trpdt = request_indication.trpdt
                c_rcat = self.CommunicationChannelManager._get_current_rcat(
                    self.current_channel)

                if c_rcat <= request_indication.rcat:
                    # We can handle the request right away
                    _trpdt = 0.0
                else:
                    self.CommunicationChannelManager.get_channel(
                        request_indication.rcat,
                        request_indication.trpdt,
                        self.send_pending_requests
                    )

                f = lambda: self.expired_timer(request_indication)
                try:
                    _trpdt = float(_trpdt)
                except ValueError:
                    _now = datetime.now()
                    if _trpdt < _now:
                        total = 0.0
                        self.logger.info("Specified Date is in the past, "
                                         "assuming 0s as trpdt")
                    else:
                        seconds = (_trpdt - _now).seconds
                        micro = (_trpdt - _now).microseconds
                        total = seconds + (micro/1000000.0)
                    self._set_timer(request_indication, total, f)
                else:
                    self._set_timer(request_indication, _trpdt, f)

                self.save_req(request_indication)

                if not self.__cb:
                    self.__cb = cb

        self.load_req(request_indication.rcat,
                      request_indication.correlationID).then(go)

    def error_reply(self, req, rcat, pend_reqs):
        """In case a request could not be sent because of channel
        unavailability, calls back the methoddomain with an Error.

        :param req: RequestIndication not sent in time
        :param rcat: Request Category value on which no channels could be
                     established
        :param pend_reqs: Sending queue
        """
        resp = Promise()
        resp.reject(ErrorResponseConfirmation(
            504, self.req.method, "No suitable channel could be established"))
        correlationID = self.req.correlationID
        contactURI = self.req.contactURI
        # Remove the req from the sending queue
        if correlationID in pend_reqs:
            self.del_req(rcat, correlationID)
        # When resp is ready, we call back the methoddomain
        self.__cb(resp, correlationID, contactURI)

    def send_pending_requests(self, channel, rcat):
        """Sends pending requests following the given rcat using a specified
        channel.

        :param channel: Channel used to send requests on
        :param rcat: Request Category supported by the channel
        """
        self.logger.debug("Enter in pending req with channel %s" % channel)

        def go(loaded_list):
            """Sends requests out of a list of pending requests.

            Calls back the methoddomain with the responses.

            :param loaded_list: List of pending requests
            """
            pend_reqs = {}
            for k, v in loaded_list:
                pend_reqs[int(k)] = v
            self.logger.debug("Pending req for rcat %s : %s", rcat, pend_reqs)

            if channel:
                self.current_channel = channel
                # Parses pending requests with the correct rcat values
                for self.req in pend_reqs.values():
                    self.logger.debug("Sending pending req %s"%self.req)

                    # Remove pending timers since the request is already being
                    # processed
                    if self.req.correlationID in self.__timers:
                        self.logger.debug(
                            "Removing timer associated with correlationID %s" %
                            self.req.correlationID)
                        self._api.cancel_timer(
                            self.__timers[self.req.correlationID])
                        del self.__timers[self.req.correlationID]

                    parsed = urlparse(self.req.path)
                    client = self.get_etsi_client(parsed.scheme)
                    resp = client(self.req)

                    def handle_success(response):
                        correlationID = self.req.correlationID
                        contactURI = self.req.contactURI
                        # Remove the req from the sending queue
                        if correlationID in pend_reqs:
                            # It is pretty ugly to call the shelve for every
                            # pending req
                            # We could optimize by keeping track of a list of
                            # sent requests, and remove all of them at once
                            self.del_req(rcat, correlationID)
                        # When resp is ready, we call back the methoddomain
                        self.logger.debug(
                            "Calling back method domain with response %s" %
                            response)
                        self.__cb(response, correlationID, contactURI)

                    # Errors can happen when Server is unreachable, the request
                    # in kept in buffer to retry later
                    # TODO: Add test on error type, checking if Channel has to
                    # TODO: be deleted because not valid anymore
                    def handle_error(x):
                        self.logger.debug(
                            "Connectivity failure using channel %s",
                            channel.anName)
                        self.CommunicationChannelManager.delete_channel(
                            channel.anName)
                        self.error_reply(self.req, rcat, pend_reqs)

                    resp.then(handle_success, handle_error)
            else:
                for self.req in pend_reqs.values():
                    if self.req.trpdt == 0:
                        self.error_reply(self.req, rcat)

        self.load_reqs(rcat).then(go)

    def send_request_indication(self, request_indication):
        path = request_indication.path

        with Promise() as p:
            if (request_indication.correlationID is None or
                        request_indication.contactURI is "final_result"):
                request = map_request_indication_to_request(request_indication)

                def handle_success(response):
                    return map_response_to_response_confirmation(
                        request_indication.method, path, response)

                def handle_error(response):
                    raise map_error_response_to_error_response_confirmation(
                        request_indication, request, response
                    )

                return self._api.send_request(request).then(handle_success,
                                                            handle_error)

            # In that case we have a delayed execution
            # TODO!
            request_indication.rcat = int(request_indication.rcat)
            if type(request_indication.trpdt) is str and \
                    (request_indication.trpdt.find('-') >= 0 or
                             request_indication.trpdt.find(',') >= 0):
                # trpdt might be an ISO 8601
                request_indication.trpdt = parse_date(request_indication.trpdt)
            else:
                request_indication.trpdt = float(request_indication.trpdt)

            def go(pend_reqs):
                """Checks if the number of pending requests is not reaching its
                limit.

                Answers with a SuccessResponseConfirmation(202).

                :param pend_reqs: List of pending requests
                """
                cm = self.CommunicationChannelManager
                rcatParamList = cm.get_rcatParamList(request_indication.rcat)
                # Todo : Check number of bytes saved too
                if len(pend_reqs) > rcatParamList.maxPendReq:
                    self.logger.warn(
                        "Error: Pending request buffer overflow %s" %
                        rcatParamList.maxPendReq)
                    p.reject(ErrorResponseConfirmation(
                        500,
                        request_indication.method,
                        "Pending request buffer is full"
                    ))
                else:
                    # fulfill with accept
                    self.logger.debug("fulfill with accept")
                    p.fulfill(SuccessResponseConfirmation(202))

            self.load_reqs(request_indication.rcat).then(go)

        return p

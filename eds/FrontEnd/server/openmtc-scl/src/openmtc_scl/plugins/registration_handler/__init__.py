"""
    @since: 2014-04-16
    @author: fei
"""

from aplus import Promise
from openmtc.exc import OpenMTCError
from openmtc_etsi.model import Scl, M2mPoc
from openmtc_etsi.response import ErrorResponseConfirmation
from openmtc_etsi.scl import CreateRequestIndication, RetrieveRequestIndication, \
    UpdateRequestIndication, DeleteRequestIndication
from openmtc_scl.util import ExpTimeUpdater, datetime_the_future
from openmtc_server.Plugin import Plugin
from openmtc_server.util.async import async_all
from openmtc_etsi.exc import SCLError, STATUS_CONFLICT
import openmtc_server.api as api


class RegistrationHandler(Plugin):
    """ Plugin to handle the GSCL registration with the NSCL.
        TODO: is this supposed to be sync or async?
    """
    # defaults:
    DEF_INTERVAL = 60 * 60
    DEF_OFFSET = 60 * 60
    # DEF_INTERVAL = 5
    # DEF_OFFSET = 10

    # configurable properties
    # TODO sanity checks?
    def get_nscl_uri(self):
        """ The NSCL URI.
        """
        return self.config["nscl_uri"]
    nscl_uri = property(get_nscl_uri)

    def get_nscl_id(self):
        """ The NSCL ID.
        """
        return self.config["nscl_id"]
    nscl_id = property(get_nscl_id)

    def get_gscl_id(self):
        """ The GSCL ID.
        """
        return api.config["etsi"]["scl_id"]
    gscl_id = property(get_gscl_id)

    def get_interval(self):
        """ ExpirationTime update interval.
        """
        return self.config.get("interval", self.DEF_INTERVAL)
    interval = property(get_interval)

    def get_offset(self):
        """ Offset added to ExpirationTime to ensure it can be met early.
        """
        return self.config.get("offset", self.DEF_OFFSET)
    offset = property(get_offset)

    def get_mgmt_protocol(self):
        """ The management protocol type.
        """
        return self.config.get("mgmt_protocol_type", "OMA_DM")
    mgmt_protocol = property(get_mgmt_protocol)

    def get_scl_type(self):
        """ The SCL type: DSCL, GSCL or NSCL.
        """
        return api.config["etsi"]["scl_type"]
    scl_type = property(get_scl_type)

    def get_subscription_id(self):
        """ EPC subscription ID.
        """
        return self.config.get("subscription_id", None)
    subscription_id = property(get_subscription_id)

    m2mpocs = {}

    def _start(self):
        """ Creates the SCL resource on the NSCL.
            Starts an ExpTimeUpdater for this resource.
        """
        self.refresher = None
        self._registered = False
        self._register().then(self._started, self._error)

    def _handle_registration_error(self, error):
        if isinstance(error, ErrorResponseConfirmation):
            self.logger.warn("Could not register: %s", error.errorInfo)
        else:
            self.logger.warn("Could not register: %s", error)
#         if not isinstance(error, OpenMTCNetworkError):
#             raise error
        self.__timer = self.api.set_timer(12000, self._register)

    def _register(self):
        promise = self._create_gscl().then(
            self._create_nscl).then(
            self._retrieve_nscl).then(
            self._start_refresher).then(
            self._register_pocs, self._handle_registration_error)

        return promise

    def _register_pocs(self):
        def send_update(m2mpoc, fields):
            uri = self.nscl_uri + "/" + "scls/" + self.gscl_id\
                + "/" + "m2mPocs" + "/" + m2mpoc.id
            rq = UpdateRequestIndication(uri, m2mpoc)
            rq.requestingEntity = self.config.get("requesting_entity")
            # TODO: add restore function in case of 404 or something
            return self.api.send_request_indication(rq)

        def _start_endpoint_refresher(response, m2mpoc):
            m2mpoc.set_path(response.resourceURI)
            self.poc_refresher.start(m2mpoc, [])

        def _register_endpoint(endpoint):

            # create a M2mPoc with the endpoint as contact info in the NSCL
            # (onlineStatus=ONLINE)
            uri = self.nscl_uri + "/" + "scls/" + self.gscl_id + "/" + "m2mPocs"
            m2mpoc = M2mPoc()
            m2mpoc.onlineStatus = "ONLINE"
            m2mpoc.contactInfo = endpoint.base_uri
            m2mpoc.expirationTime = self._gscl.expirationTime

            rq = CreateRequestIndication(uri, m2mpoc)
            rq.requestingEntity = self.config.get("requesting_entity")
            p = self.api.send_request_indication(rq).then(
                lambda evt, m2mpoc=m2mpoc: _start_endpoint_refresher(evt,m2mpoc)
            )

            return p

        # we use a separate refresher for pocs,
        # because refresher is specifically for Scl (see send_update)
        self.poc_refresher = ExpTimeUpdater(self.api, send_update,
                                            interval=self.interval,
                                            offset=self.offset)

        promise_list = map(_register_endpoint, self.api.get_mid_endpoints())
        return async_all(promise_list, True)

    def _create_gscl(self):
        """ Sends a CreateRequestIndication for the scl resource.
            Retrieves resource data afterwards.

            @return: Scl instance representing the created resource.
        """
        # 1) "Compose RequestIndication primitive":
        path = "/scls"
        uri = self.nscl_uri + path
        self.logger.debug("registering %s at %s", self.gscl_id, uri)
        # init SCL object
        gscl = Scl()
        # a) In the RequestIndication, the issuer shall provide its SCL-ID
        # in the sclId attribute as the name of the new resource
        # that will be created in the Hosting SCL.
        gscl.sclId = self.gscl_id
        #  b) The issuer shall include its < sclBase > in the "link" attribute.
        mid_endpoints = self.api.get_mid_endpoints()
        try:
            gscl.link = mid_endpoints[0].base_uri
        except IndexError:
            # TODO: retry
            raise OpenMTCError("No mId endpoint present")
        # c) The issuer shall fill the device management protocol
        #    that it supports in the "mgmtProtocolType" attribute.
        gscl.mgmtProtocolType = self.mgmt_protocol
        # d) The issuer shall fill the sclType attribute indicating its type of
        #    SCL.
        gscl.sclType = self.scl_type

        # TODO put subscription_id somewhere.
#         if self.subscription_id:
#             gscl.pocs = [ "SID:" + self.subscription_id ]
        # set expirationTime as configured
        gscl.expirationTime = datetime_the_future(self.interval + self.offset)

        def _convert(response):
            gscl = self._gscl = response.resource
            return gscl

        def _retrieve_gscl(data):
            self._registered = True
            path = "/scls/" + self.gscl_id
            if isinstance(data, str):
                uri = data
            else:
                uri = self.nscl_uri + path
            # send RetrieveRequest and wait
            rq = RetrieveRequestIndication(uri)
            rq.requestingEntity = self.config.get("requesting_entity")
            return self.api.send_request_indication(rq).then(_convert)

        def update_gscl(data):
            data.expirationTime = gscl.expirationTime
            rq = UpdateRequestIndication(uri + '/' + gscl.sclId, data)
            rq.requestingEntity = self.config.get("requesting_entity")
            return self.api.send_request_indication(rq).then(lambda x: data)

        def _check_error(err):
            try:
                if err.statusCode == STATUS_CONFLICT:
                    self._registered = True
                    return _retrieve_gscl(None).then(update_gscl)
                raise err
            except AttributeError:
                raise err

        def create_gscl():
            rq = CreateRequestIndication(uri, gscl)
            rq.requestingEntity = self.config.get("requesting_entity")
            return self.api.send_request_indication(rq)

        return create_gscl().then(
            _retrieve_gscl, _check_error)

    def _create_nscl(self, gscl):
        """ Creates an SCL resource for the NSCL.

        1) Upon receiving a successful response,
        the Issuer SCL shall create a new local scl resource, using the
        <sclBase> of the Hosting SCL to identify the local resource.

        2) The values of the attributes for the local <scl> resource shall be
        assigned default values initially. With the exception of the expirationTime ...

        3) The Issuer SCL shall set the value of "link" for the local <scl>
        resource to the sclBase resource URI of the receiver SCL.

        In the following "Step 3" designates the step of waiting for the Create
        ResponseConfirm.
        11) If the ResponseConfirm received in Step 3 contains a resource
        representation and the that resource representation contains a
        aPocHandling attribute value, then the issuer SCL shall set the
        aPocHandling attribute in its local <sclBase> resource to the received
        value.

        12) If the ResponseConfirm received in Step 3 contains a resource
        representation and the that resource representation does not contain a
        aPocHandling attribute value, then the issuer SCL shall set the
        aPocHandling attribute in its local <sclBase> resource to "SHALLOW".
        """

        def _done(data):
            return nscl
        self.logger.debug("retrieving NSCL resource.")
        path = "/m2m/scls"
        data = {
            "sclId": self.nscl_id,  # "using the sclBase of the Hostring SCL"?
            "link": self.nscl_uri,  # 3)
            "mgmtProtocolType": self.mgmt_protocol,
            "expirationTime": gscl.expirationTime or None,  # 2)
            "aPocHandling": gscl.aPocHandling or "SHALLOW",  # 11) and 12)
            "sclType": "NSCL",
        }
        nscl = Scl(path, **data)
        rq = CreateRequestIndication(path, nscl)
        rq.internal = True
        return self.api.handle_request_indication(rq).then(_done)

    def _retrieve_nscl(self, instance):
        """
        5) The issuer SCL shall perform a RETRIEVE request on the sclBase
        resource of the Hosting SCL (sclBaseRetrieveRequestIndication)
        to request the sclBase resource attribute values.

        6) The Receiver SCL ...

        7) Upon receiving an unsuccessful sclBaseRetrieveResponseConfirm,
        the issuer SCL shall continue on Step 10.
        The issuer SCL may retry the post-response operation at a later time,
        starting from Step 5. The issuer SCL shall only do this if it has
        reasons to believe the error is of a transient nature.
        For example, on receiving a STATUS_SERVER_UNAVAILABLE.

        8) Upon receiving the successful sclBaseRetrieveResponseConfirm,
        the Issuer SCL shall update the value of the attribute(s) of its local
        SCL resource to match the received values from the sclBase resource
        representation in the sclBaseRetrieveResponseConfirm.

        9) Specifically, the Issuer SCL shall set the value of the searchStrings
        and accessRightID attributes in its local scl resource to the value of
        the searchStrings and accessRightID attributes in sclBase resource
        representation received in the sclBaseRetrieveResponseConfirm from Step 8.
        """
        def _create_nscl_copy(response):
            resource = response.resource
            # 8)
            path = instance.path = "/m2m/scls" + "/" + self.nscl_id
            # 9)
            fields = [
                "searchStrings", "aPocHandling", "accessRightID",
                # "creationTime", "lastModifiedTime",
            ]
            for f in fields:
                if f == "searchStrings":
                    # HACK: setattr or even a simple assignment wont work
                    instance.values[f]["searchString"].extend(resource.searchStrings)
                else:
                    setattr(instance, f, getattr(resource, f))

            setattr(instance, "mgmtProtocolType", self.mgmt_protocol)
            fields.append("mgmtProtocolType")

            rq = UpdateRequestIndication(path, instance, fields=fields)
            rq.internal = True
            return self.api.handle_request_indication(rq)

        rq = RetrieveRequestIndication(self.nscl_uri)  # 5)
        rq.requestingEntity = self.config.get("requesting_entity")

        promise = self.api.send_request_indication(rq)
        return promise.then(_create_nscl_copy)

    def _start_refresher(self, data):
        """ Starts the expiration time updater. """
        def send_update(instance, fields):
            # TODO fields param??
            def _update_instance(data=None):
                def _fill_instance(result):
                    # instance = Scl( self._gscl.path, **data[1])
                    self._gscl.expirationTime = result.resource.expirationTime  # side effect
                    # update expirationTime of NSCL copy
                    path = "/m2m/scls/" + self.nscl_id + "/expirationTime"
                    fields = ["expirationTime"]
                    rq = UpdateRequestIndication(path, self._gscl,
                                                 fields=fields)

                    p = self.api.handle_request_indication(rq)
                    # p.fulfill(instance)
                    return p

                def _retrieve_instance():
                    rq = RetrieveRequestIndication(uri)
                    rq.requestingEntity = self.config.get("requesting_entity")
                    promise = self.api.send_request_indication(rq)
                    return promise
                return _retrieve_instance().then(_fill_instance)

            def _restore(err):
                """ Restarts registration, if 404. """
                def reregister(a=None, b=None):
                    return self._register().then(failure=self._error)
                # ISSUE; dont know what request it was? <- m2mPocs?
                self.logger.warn("GSCL ExpirationTime update failed: %s", err)
                NOT_FOUND = (404, "404", "STATUS_NOT_FOUND", "NOT_FOUND")
                if err.statusCode in NOT_FOUND:
                    # FIXME: better error handling
                    # cleanup
                    rq = DeleteRequestIndication("/m2m/scls/" + self.nscl_id)
                    p = self.api.handle_request_indication(rq)\
                        .then(reregister)
                    self.refresher.stop()
                    self.poc_refresher.stop()
                    return p
                else:
                    # TODO other statuses possible?
                    return Promise().fulfill(None)

            uri = instance.path
            if not uri.startswith((self.nscl_uri, "coap://", "http://")):
                # TODO: kca: use urljoin
                uri = self.nscl_uri + uri
            rq = UpdateRequestIndication(uri, instance)
            rq.requestingEntity = self.config.get("requesting_entity")

#            rq = UpdateRequestIndication(uri, instance, fields=fields)
            promise = self.api.send_request_indication(rq) \
                .then(_update_instance, _restore)
            return promise

        self.logger.debug("creating ExpTimeUpdater:%s", self.interval)

        # start a timer to update scl resource before it expires
        self.refresher = ExpTimeUpdater(self.api, send_update,
                                        interval=self.interval,
                                        offset=self.offset)
        self.refresher.start(self._gscl, fields=["mgmtProtocolType"])

    def _stop(self):
        """ Stops the plugin.
            DELETES scl resource.
        """
        # remove registration from NSCL
        sclId = self.gscl_id
        path = "/scls/" + sclId
        self.logger.debug("deregistering %s at %s", sclId, path)

        try:
            self.api.cancel_timer(self.__timer)
        except AttributeError:
            pass

        try:
            self.refresher.stop()
        except AttributeError:
            pass

        if self._registered:
            try:
                rq = DeleteRequestIndication(self.nscl_uri + path)
                rq.requestingEntity = self.config.get("requesting_entity")
                promise = self.api.send_request_indication(rq)
            except SCLError as e:
                # TODO handle errors?
                # only really expect SCLNotFound
                return self._error(e)
        self._stopped()

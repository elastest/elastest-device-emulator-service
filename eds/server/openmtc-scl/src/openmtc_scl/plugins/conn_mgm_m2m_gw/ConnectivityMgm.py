from openmtc.scl import RetrieveRequestIndication, CreateRequestIndication
from openmtc_scl.serializer import JsonSerializer

from aplus import Promise
from futile.logging import LoggerMixin
from openmtc.model import MgmtObj


class ConnectivityMgm(LoggerMixin):

    def __init__(self, config, logger, api):
        self.config = config
        self.logger = logger
        self.api = api
        self.wifi_manager = None
        self.serializer = JsonSerializer()

    def create_lwm2m_mgm_resources(self):
        path = "/m2m/scls"
        request = RetrieveRequestIndication(path=path)
        result_promise = self.api.handle_request_indication(request)
        result = result_promise.get()
        self.logger.info("result for reading is: "+str(result))
        if result.resource is not None:
            content = self.serializer.encode(result.resource)
            self.logger.info("response content is "+content)
        else:
            self.logger.info("response content is None")

        path = "/m2m/scls/mgmtObjs"
        mgmtObj = MgmtObj(id="ConnectivityMonitoring", moID="urn:oma:lwm2m:oma:4")
        key="IP_Addresses"
        value=""
        mgmtObj.__setattr__(key, value)
        request = CreateRequestIndication(path=path,
                                          resource=mgmtObj)
        result_promise = self.api.handle_request_indication(request)
        result = result_promise.get()
        self.logger.info("result is for creating connectivity monitoring is: " + str(result))
        if result.resourceURI is not None:
            content = self.serializer.encode(result.resourceURI)
            self.logger.info("response content is " + content)
        else:
            self.logger.info("response content is None")

    def start(self):
        self.logger.info("config data is %s", str(self.config))
        if self.config["wifi"] and self.config["wifi"]["enabled"]:
            self.logger.info("config wifi " + str(self.config["wifi"]))
            self.logger.info("config wifi enabled " + str(self.config["wifi"]["enabled"]))
            self.logger.info("wifi enabled")

            if self.config["platform"] and self.config["platform"]["android"] and self.config["platform"]["android"]["enabled"]:
                from android.AndroidWiFiManager import AndroidWiFiManager
                self.wifi_manager = AndroidWiFiManager(config=self.config["wifi"], logger=self.logger, api=self.api)
            if self.wifi_manager is not None:
                self.wifi_manager.start()

    def process_connectivity_request(self, req_category, requested_ssid=None):
        self.logger.info("processing connectivity request with request category " + str(req_category))
        p = Promise()
        if requested_ssid:
            ssid = requested_ssid
        else:
            #get the AN info for which the req_category can be served
            ssid = self.wifi_manager.get_ssid_for_req_category(req_category)
        self.logger.info("found suitable network with ssid %s", ssid)
        if ssid is not None:

            self.logger.info("found suitable network with ssid %s, current ssid %s", ssid, self.wifi_manager.current_ssid)

            def conn_callback(dict_reply):
                if dict_reply is None:
                    self.logger.info("invalid conn_callback dict_reply")
                    #p.reject()
                self.logger.info("connectivity callback for trying to connect on "+ssid+" has status "+dict_reply["status"])

                if dict_reply["ssid"].startswith('"'):
                    # Unquote
                    dict_reply["ssid"] = dict_reply["ssid"][1:-1]
                if dict_reply["status"]!="CONNECTED" or dict_reply["ssid"]!=ssid:
                    self.logger.info("status is not CONNECTED or current ssid not %s rejecting... (%s instead)"%(ssid, dict_reply["ssid"]))
                    #p.reject()
                else:
                    channel_tuple = (ssid, req_category)
                    self.logger.debug("Handover is done, fulfilling with ssid %s"%ssid)
                    p.fulfill(channel_tuple)
                    self.wifi_manager.removeConnectionAlert(conn_callback)

            if ssid == self.wifi_manager.current_ssid:
                self.logger.info("no need to handover, the current ssid is good enough")
                channel_tuple = (ssid, req_category)
                p.fulfill(channel_tuple)

            else:
                self.wifi_manager.addConnectionAlert(conn_callback)
                self.wifi_manager.connectToNetwork(ssid, conn_callback)
                self.logger.info("trying to connect on network with ssid %s", ssid)
        else:
            p.reject("no WiFi for request category " + req_category + " available")
        return p

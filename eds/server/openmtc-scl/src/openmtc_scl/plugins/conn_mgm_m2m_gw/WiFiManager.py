from futile.logging import LoggerMixin
import json


class WiFiManager(LoggerMixin):
    def __init__(self, config, logger, api):
        self.config = config
        self.logger = logger
        self.api = api
        self.conn_change_callback_list = []
        self.current_ssid = ""

    def get_ssid_for_req_category(self, req_category):
        self.logger.info(" searching for network for rcat " + str(req_category))
        self.logger.info(" the current network with ssid " + self.current_ssid)
        network_array = json.loads(json.dumps(self.config["networks"], separators=(',', ':')))
        for network in network_array:
            self.logger.info(" the current network with ssid " + network["ssid"] +\
                             " can be used to send request category " + str(network["rcat"]))
            if network["ssid"] == self.current_ssid and network["rcat"] <= req_category:
                self.logger.info(" the current network with ssid " + network["ssid"] +\
                                 " can be used to send request category " + str(req_category))
                return network["ssid"]

        for network in network_array:
            if network["rcat"] <= req_category:
                self.logger.info("for request category %i found network with ssid %s", req_category, network["ssid"])
                return network["ssid"]
        return None

    def addConnectionAlert(self, callback):
        self.conn_change_callback_list.append(callback)

    def removeConnectionAlert(self, callback):
        self.conn_change_callback_list.remove(callback)

    def connectToNetwork(self, networkSSID, conn_callback=None):
        pass 

    def conn_change_callback(self, status, ip_address, ssid):
        self.logger.info("calling conn_change_callback in WiFiManager %s %s %s"%(status, ip_address, ssid))
        msg = {}
        msg['status'] = status
        msg['ip_address'] = ip_address
        msg['ssid'] = ssid
        self.logger.info("calling conn_change_callback in WiFiManager")
        for callback in self.conn_change_callback_list:
            self.logger.info("calling conn_change_callback in WiFiManager %s" + str(callback))
#            self.api.run_task(callback, msg)
            callback(msg)

    def start(self):
        pass

    def stop(self):
        pass

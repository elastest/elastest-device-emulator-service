from jnius import autoclass
from openmtc.scl import UpdateRequestIndication


PythonService = autoclass('org.renpy.android.PythonService')
String = autoclass('java.lang.String')
NetworkInterface = autoclass('java.net.NetworkInterface')


class GeneralAndroidConnectivity():
    #self.conn_mgmt_action=""

    def __init__(self, logger, api):
        self.api = api
        self.logger = logger

    def updateConnectivityMgmtObj(self, dict_reply):
        try:
            ip_address = dict_reply["ip_address"]
            ssid = dict_reply["ssid"]
            if ip_address is not None:
                self.logger.info("updating conn mgmt obj with ip address " + ip_address + " and ssid " + ssid)
                update_content = "{\"mgmtObj\":{\"IP_Addresses\":\"" + ip_address + "\"}}"
                req = UpdateRequestIndication(
                    path="/m2m/scls/mgmtObjs/ConnectivityMonitoring",
                    resource=update_content,
                    content_type="application/json"
                )
                self.api.handle_request_indication(req)
            return
        except Exception as e:
            self.logger.error(str(e))
        return

    def getLocalIpAddress(self):
        self.logger.info("retrieving local ip address")
        en = NetworkInterface.getNetworkInterfaces()
        while en.hasMoreElements():
            intf = en.nextElement()
            enumIpAddr = intf.getInetAddresses()
            while enumIpAddr.hasMoreElements():
                address = enumIpAddr.nextElement()
                if address.isLoopbackAddress() or address.isLinkLocalAddress():
                    pass
                else:
                    output = str(address.toString())[1:]
                    self.logger.info("found ip address " + output)
                    return output
        return None

    def getLocalConnectivityStatus(self):
        self.logger.info("retrieving local ip address")
        en = NetworkInterface.getNetworkInterfaces()
        while en.hasMoreElements():
            intf = en.nextElement()
            enumIpAddr = intf.getInetAddresses()
            while enumIpAddr.hasMoreElements():
                address = enumIpAddr.nextElement()
                if address.isLoopbackAddress() or address.isLinkLocalAddress():
                    pass
                else:
                    output = str(address.toString())[1:]
                    self.logger.info("found ip address " + output)
                    return [str(intf.getName()), output]
        return None

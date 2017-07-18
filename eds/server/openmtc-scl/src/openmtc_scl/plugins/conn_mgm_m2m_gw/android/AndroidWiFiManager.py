import json

from android.broadcast import BroadcastReceiver
from jnius import autoclass

from openmtc_scl.plugins.conn_mgm_m2m_gw.WiFiManager import WiFiManager
from .GeneralAndroidConnectivity import GeneralAndroidConnectivity
from .WiFiAndroidController import WiFiAndroidController

#Hardware = autoclass('org.renpy.android.Hardware')
#WiFiController = autoclass('org.openmtc.conn_mgm.android.wifi.WiFiController')
GeneralConnectivity = autoclass('org.openmtc.conn_mgm.android.GeneralConnectivity')
PythonService = autoclass('org.renpy.android.PythonService')
String = autoclass('java.lang.String')
ConnectivityManager = autoclass('android.net.ConnectivityManager')
Context = autoclass('android.content.Context')


def ip_connection_notification():
    print "got new ip connection"


class AndroidWiFiManager(WiFiManager):
    def __init__(self, config, logger, api):
        super(AndroidWiFiManager, self).__init__(config, logger, api)
        self.general_android_conn = GeneralAndroidConnectivity(self.logger, self.api)
        self.wifi_android_controller = WiFiAndroidController(self.logger, self.general_android_conn)

        self.context = PythonService.mService
        self.wifi_manager = self.context.getSystemService(Context.WIFI_SERVICE)
        self.conn_manager = self.context.getSystemService(Context.CONNECTIVITY_SERVICE)

        self.conn_change_br = BroadcastReceiver(self.handle_conn_change_alert, actions=[ConnectivityManager.CONNECTIVITY_ACTION])
        self.addConnectionAlert(self.general_android_conn.updateConnectivityMgmtObj)

    def start(self):
        super(AndroidWiFiManager, self).start()
        ip_addr = self.general_android_conn.getLocalIpAddress()
        if ip_addr is not None and ip_addr != "":
            self.general_android_conn.updateConnectivityMgmtObj("{\"status\":\"CONNECTED\", \"ip_address\":\""+ip_addr+"\", \"ssid\":\" \"}")

        #GeneralConnectivity.setOpenMTCIntentAction(self.internalIntentAction)
        #GeneralConnectivity.setOpenMTCAndroidAppPackageName(self.android_app_package)
        #WiFiController.startConnectionAlert()
        results = self.wifi_android_controller.scanWiFiNetworks()
        #results = WiFiAndroidController.scanWiFiNetworks()
#        results = Hardware.getWiFiNetworks()
        self.logger.info("the result of wifi scan was "+results)

#        WiFiController.addNetworks(String(str(json.dumps(self.config["networks"],separators=(',', ':')))))
        network_array = json.loads(json.dumps(self.config["networks"], separators=(',', ':')))
        for network in network_array:
            self.logger.info("network info is "+str(network))
            network_str = str(json.dumps(network, separators=(',', ':')))
            self.logger.info("network info is "+network_str)
            self.wifi_android_controller.addConfiguredNetwork(network_str)
            #WiFiController.addConfiguredNetwork(String(network_str))

#        default_network = "guest_open"
#        default_network = "guest_wpa_preshared"
        default_network = self.config["default_network"]
        self.logger.info("default_network is "+default_network)
        self.wifi_android_controller.connectToNetwork(default_network)
        #WiFiController.connectToNetwork(default_network)

    def connectToNetwork(self, networkSSID, conn_callback=None):
        self.wifi_android_controller.connectToNetwork(networkSSID, conn_callback)

    def addConnectionAlert(self, callback):
        if len(self.conn_change_callback_list) == 0:
            self.conn_change_br.start()
        super(AndroidWiFiManager, self).addConnectionAlert(callback)

    def removeConnectionAlert(self, callback):
        super(AndroidWiFiManager, self).removeConnectionAlert(callback)
        if len(self.conn_change_callback_list) == 0:
            self.conn_change_br.stop()

    def handle_conn_change_alert(self, context, intent):
        action = intent.getAction()
        ssid = ""
        ip_address = ""
        self.logger.info("received intent on "+action)

        if action != ConnectivityManager.CONNECTIVITY_ACTION:
            return

        if intent.hasExtra(ConnectivityManager.EXTRA_NO_CONNECTIVITY):
            #intent.getBooleanExtra(ConnectivityManager.EXTRA_NO_CONNECTIVITY, true)){
            self.logger.info("received information that the device disconnected and no network is available")
            self.conn_change_callback("DISCONNECTED", "", "")
            return

        net_type = intent.getIntExtra("networkType", -1)
        self.logger.info("network type is "+str(net_type))

        if net_type != ConnectivityManager.TYPE_WIFI:
            return

        info = self.conn_manager.getNetworkInfo(net_type)
        state = info.getState()
        self.logger.info("wifi connectivity state is "+str(state.toString()))

        if str(state.toString()) != "CONNECTED":
            return

        self.logger.info("received information about connectivity change for WiFi")

        # send intent to update connectivity status
        self.logger.info("received information that the device connected on WiFi")
        wifiInfo = self.wifi_manager.getConnectionInfo()
        ssid = wifiInfo.getSSID()
        self.logger.info("device is now connected on WiFi on SSID "+str(ssid))

#        ip_address = self.general_android_conn.getLocalIpAddress()
        ip_address = GeneralConnectivity.getLocalIpAddress()

        if ip_address is None:
            self.logger.info("device is not having any IP assigned")
            self.conn_change_callback("NO IP ADDRESS", "", ssid)
        else:
            self.logger.info("device is now connected with IP "+str(ip_address))
            #TODO: handle any promise that is waiting for the reply
            self.conn_change_callback("CONNECTED", ip_address, ssid)
            self.current_ssid = ssid[1:-1]
            return

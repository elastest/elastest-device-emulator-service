from futile.logging import LoggerMixin
from jnius import autoclass
import json

from .GeneralAndroidConnectivity import GeneralAndroidConnectivity

PythonService = autoclass('org.renpy.android.PythonService')
String = autoclass('java.lang.String')
NetworkInterface = autoclass('java.net.NetworkInterface')
PythonService = autoclass('org.renpy.android.PythonService')
WifiManager = autoclass('android.net.wifi.WifiManager')
WifiConfiguration = autoclass('android.net.wifi.WifiConfiguration')
Context = autoclass('android.content.Context')
ConnectivityManager = autoclass('android.net.ConnectivityManager')
WifiConfiguration_KeyMgmt_NONE = 0
WifiConfiguration_GroupCipher_WEP40 = 0
WifiConfiguration_GroupCipher_WEP104 = 1
WifiConfiguration_GroupCipher_TKIP = 2
WifiConfiguration_GroupCipher_CCMP = 3
#NetworkInfoState = autoclass('android.net.NetworkInfo.State')


class WiFiAndroidController(LoggerMixin):
    def __init__(self, logger, gen_connectivity):
        self.logger = logger
        self.context = PythonService.mService
        self.wifi_manager = self.context.getSystemService(Context.WIFI_SERVICE)
        self.wifi_manager.setWifiEnabled(True)
        self.conn_manager = self.context.getSystemService(Context.CONNECTIVITY_SERVICE)
        self.gen_connectivity = gen_connectivity

    def scanWiFiNetworks(self):
                #if not already enabled
        if self.wifi_manager.getWifiState()!=3:
            self.wifi_manager.setWifiEnabled(True)
        ap_list = self.wifi_manager.getScanResults()
        if ap_list is None:
            return ""
        iterator = ap_list.iterator()
        output = ""
        while iterator.hasNext():
            ap = iterator.next()
            output += "\t" + str(ap.SSID) + "\t" + str(ap.BSSID) + "\t" + str(ap.level) + "\n"

        self.logger.info("got ap list "+output)
        return output

    def addConfiguredNetwork(self, config_str):
        config = json.loads(config_str)

        wifi_config = WifiConfiguration()
        ssid = config["ssid"]
        wifi_config.SSID = "\"" + ssid + "\""

        auth_method = config["auth_method"]
        self.logger.info("adding network with auth_method  "+auth_method)

        if auth_method == "open_system":
            wifi_config.allowedKeyManagement.set(WifiConfiguration_KeyMgmt_NONE)
            self.logger.info("adding open network with ssid  " + ssid)
        elif auth_method == "WPA":
            password = config["password"]
            self.logger.info("adding wpa network with ssid  " + ssid + " and password " + password)
            wifi_config.preSharedKey = "\"" + password + "\""
        elif auth_method == "WEP_64":
            password = config["password"]
            self.logger.info("adding wep network with ssid  " + ssid + " and password " + password)

            wifi_config.wepKeys[0] = password
            wifi_config.wepTxKeyIndex = 0
            wifi_config.allowedKeyManagement.set(WifiConfiguration_KeyMgmt_NONE)
            wifi_config.allowedGroupCiphers.set(WifiConfiguration_GroupCipher_WEP40)
            wifi_config.allowedGroupCiphers.set(WifiConfiguration_GroupCipher_WEP104)
            wifi_config.allowedGroupCiphers.set(WifiConfiguration_GroupCipher_TKIP)
            wifi_config.allowedGroupCiphers.set(WifiConfiguration_GroupCipher_CCMP)
        self.wifi_manager.addNetwork(wifi_config)

    def connectToNetwork(self, networkSSID, conn_callback=None):
        #if not already enabled
        if self.wifi_manager.getWifiState()!=3:
            self.wifi_manager.setWifiEnabled(True)
        self.logger.info("trying to connect to network with ssid " + networkSSID)
        config_list = self.wifi_manager.getConfiguredNetworks()
        self.logger.info("size of the list of configured networks is %i" % config_list.size())
        if config_list.isEmpty():
            self.logger.info("no configured network, exiting")
            return
        iterator = config_list.iterator()
        while iterator.hasNext():
            network = iterator.next()
            if network.SSID is not None and network.SSID == ("\"" + networkSSID + "\""):
                self.logger.info("found network with ssid %s configured in the wifi manager" % networkSSID)
                #self.wifi_manager.disconnect()
                self.wifi_manager.enableNetwork(network.networkId, True)
                #self.wifi_manager.reconnect()
                return
        if conn_callback is not None:
            msg = {}
            msg["status"] = "NOT FOUND"
            msg["ip_address"] = ""
            msg["ssid"] = ""
            conn_callback(msg)

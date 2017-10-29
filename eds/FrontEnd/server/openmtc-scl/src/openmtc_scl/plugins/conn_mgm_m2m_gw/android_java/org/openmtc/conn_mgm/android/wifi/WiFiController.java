
package org.openmtc.conn_mgm.android.wifi;

import android.content.Context;
import org.renpy.android.PythonService;
import org.json.JSONObject;
import org.json.JSONArray;
import org.json.JSONException;
import android.net.wifi.WifiManager;
import android.net.wifi.WifiConfiguration;
import java.util.List;
import java.util.ArrayList;
import android.net.wifi.ScanResult;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.net.NetworkInfo.State;
import android.util.Log;
import android.content.Intent;
import android.net.wifi.WifiInfo;
import android.content.IntentFilter;
import android.net.ConnectivityManager;
import android.content.BroadcastReceiver;
import org.openmtc.conn_mgm.android.GeneralConnectivity;

public class WiFiController{
	
	static Context context = (Context)PythonService.mService;
	static WifiManager wifiManager = (WifiManager) context.getSystemService(Context.WIFI_SERVICE);
	static ConnectivityManager connectivityManager = (ConnectivityManager) context.getSystemService(Context.CONNECTIVITY_SERVICE);
	private static final String TAG = "FOKUS WiFi Controller";
	
    public static String scanWiFiNetworks(){
    	
    	List<ScanResult> apList = wifiManager.getScanResults();
    	Log.v(TAG, "got AP list "+apList);
    	
    	if (apList!=null){
    		String latestResultString = "";
            for (ScanResult result : apList)
            {
		
            	latestResultString += String.format("%s\t%s\t%d\n", result.SSID, result.BSSID, result.level);
            }
            
            Log.v(TAG, "got AP list "+latestResultString);
            return latestResultString;
    	}
    	Log.v(TAG, "got empty AP list ");
    	return "";

    }
    
    /*  {
			"ssid":"guest",
			"auth_method":"open_system"
		},
		{
			"ssid":"guest_wpa",
			"auth_method":"wpa",
			"password":"12345"
		}*/
    
    public static void addConfiguredNetwork(String config_string){
    	 
		try{
	
			JSONObject config = new JSONObject(config_string);
		    	WifiConfiguration conf = new WifiConfiguration();
	    		conf.SSID = "\"" + config.getString("ssid") + "\"";   // Please note the quotes. String should contain ssid in quotes
	    	
		    	String auth_method = config.getString("auth_method");
	    		Log.v(TAG, "adding network with auth_method  "+config.getString("auth_method"));
	    		if (auth_method.equals("open_system")){
	    		
		    		conf.allowedKeyManagement.set(WifiConfiguration.KeyMgmt.NONE);
	    			Log.v(TAG, "adding open network with ssid  "+config.getString("ssid"));
	    		}else if (auth_method.equals("WPA")){
	    			Log.v(TAG, "adding wpa network with ssid  "+config.getString("ssid")+" and password "+config.getString("password"));
		    		conf.preSharedKey = "\""+ config.getString("password") +"\"";
	    		}else if (auth_method.equals("WEP_64")){
	    			
	    			Log.v(TAG, "adding wep network with ssid  "+config.getString("ssid")+" and password "+config.getString("password"));
	    			//conf.wepKeys[0] = "\"" + config.getString("password") + "\""; 
	    			conf.wepKeys[0] = config.getString("password") ; 
		    		conf.wepTxKeyIndex = 0;
	    			conf.allowedKeyManagement.set(WifiConfiguration.KeyMgmt.NONE);
	    			conf.allowedGroupCiphers.set(WifiConfiguration.GroupCipher.WEP40); 
	    			conf.allowedGroupCiphers.set(WifiConfiguration.GroupCipher.WEP104); 
		    	}
	    	
	    		wifiManager.addNetwork(conf);
		
	    	}catch(JSONException e){
	        	Log.e(TAG, "error on json object retrieval",e);
			return;
		}
    }
    
    public static void addNetworks(String networks){
    	
    	try{
    		
    		Log.v(TAG, "decoding json array for configured networks: "+networks);
    		JSONArray config = new JSONArray(networks);
    		JSONObject obj = null;
    		for (int i=0; i<config.length(); i++){
    			obj = config.getJSONObject(i);
    			if (obj !=null)
    				WiFiController.addConfiguredNetwork(obj.toString());
    		}
    		Log.v(TAG, "added all the networks");
    	}catch(JSONException e){
            Log.e(TAG, "error on parsing the content:["+networks+"]",e);
            return;
        }
    }
    
    public static void connectToNetwork(String networkSSID){
    	
        Log.v(TAG, "trying to connect to network with ssid "+networkSSID);
    	List<WifiConfiguration> list = wifiManager.getConfiguredNetworks();
    	for( WifiConfiguration i : list ) {
    	    if(i.SSID != null && i.SSID.equals("\"" + networkSSID + "\"")) {
        	 Log.v(TAG, "found network "+networkSSID);
    	         wifiManager.disconnect();
    	         wifiManager.enableNetwork(i.networkId, true);
    	         wifiManager.reconnect();               

    	         return;
    	    }           
    	 }

         Log.v(TAG, "did not find the network "+networkSSID);
    }
    
    public static void onReceiveConnectionChange(Context context, Intent intent) {
        final String action = intent.getAction();
	String ssid = "";
	String ip_address = "";
        Log.v(TAG, "received intent on "+action);
        if (action.equals(ConnectivityManager.CONNECTIVITY_ACTION)) {
	    if(intent.hasExtra(ConnectivityManager.EXTRA_NO_CONNECTIVITY) && intent.getBooleanExtra(ConnectivityManager.EXTRA_NO_CONNECTIVITY, true)){
            	Log.v(TAG, "received information that the device disconnected and no network is available");
            	GeneralConnectivity.updateConnectivityMgmtObj("", "");  
	    }else {
		int net_type = intent.getIntExtra("networkType",-1);
	        Log.v(TAG, "network type is "+net_type);
		if(net_type==ConnectivityManager.TYPE_WIFI){

			NetworkInfo info = connectivityManager.getNetworkInfo(net_type);
			NetworkInfo.State state = info.getState();
	            	Log.v(TAG, "wifi connectivity state is "+state);
			if(state.equals(NetworkInfo.State.CONNECTED)){
	            		Log.v(TAG, "received information about connectivity change for WiFi");
			
        	        	// send intent to update connectivity status
	        	    	Log.v(TAG, "received information that the device connected on WiFi");
	        	    	WifiInfo wifiInfo = wifiManager.getConnectionInfo();
        	    		ssid = wifiInfo.getSSID();
	        	    	ip_address = GeneralConnectivity.getLocalIpAddress();
        	    		Log.v(TAG, "device is now connected on WiFi on SSID "+ssid);
	            		if (ip_address == null){
        	    			Log.v(TAG, "device is not having any IP assigned");
	        	    	}else{
        	    			Log.v(TAG, "device is now connected with IP "+ip_address);
	            		}
		            	GeneralConnectivity.updateConnectivityMgmtObj(ip_address, ssid);
			}
		}
	     }
        }
    }
    
    public static void startConnectionAlert(){
	IntentFilter i = new IntentFilter();
        i.addAction(ConnectivityManager.CONNECTIVITY_ACTION);
        Log.v(TAG, "starting listening for event "+WifiManager.SUPPLICANT_CONNECTION_CHANGE_ACTION);
	
        context.registerReceiver(new BroadcastReceiver() {

            @Override
            public void onReceive(Context c, Intent i) {
                WiFiController.onReceiveConnectionChange(c, i);
            }

        }, i);    	
    }
    
}

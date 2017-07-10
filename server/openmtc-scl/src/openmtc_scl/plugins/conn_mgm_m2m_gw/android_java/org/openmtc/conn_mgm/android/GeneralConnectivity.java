
package org.openmtc.conn_mgm.android;

import android.util.Log;
import java.net.NetworkInterface;
import java.util.Enumeration;
import java.net.InetAddress;
import java.net.Inet4Address;
import java.net.Inet6Address;
import android.content.Intent;
import android.content.Context;
import org.renpy.android.PythonService;
import org.json.JSONObject;
import org.json.JSONException;

public class GeneralConnectivity{

	static String ConnectivityMgmtAction = "OpenMTC_M2M_Gw_Connectivity";
    private static final String TAG = "FOKUS GeneralConnectivity";	
    static String OpenMTC_intent_action = "";
    static String OpenMTC_android_package = "";
    static Context context = (Context)PythonService.mService;
    
    public static void setOpenMTCIntentAction(String action){
    	OpenMTC_intent_action = action;
    }
    
    public static void setOpenMTCAndroidAppPackageName(String android_package){
    	OpenMTC_android_package = android_package;
    }
    
    public static void updateConnectivityMgmtObj(String IP_Address, String ssid){
    	
    	Intent intent = new Intent(OpenMTC_intent_action);
    	intent.putExtra("method", "retrieve");
    	intent.putExtra("path", "/m2m/scls/mgmtObjs/ConnectivityMonitoring");
    	intent.putExtra("Issuer", OpenMTC_android_package);
    	intent.putExtra("replyAction", ConnectivityMgmtAction); 
	context.sendBroadcast(intent);
    	
	intent = new Intent(OpenMTC_intent_action);
    	intent.putExtra("method", "update");
    	intent.putExtra("path", "/m2m/scls/mgmtObjs/ConnectivityMonitoring");
	
	JSONObject mgmt_repr;
	try{
		JSONObject ip_addr_repr = new JSONObject();
		ip_addr_repr.put("IP_Addresses", IP_Address);

		mgmt_repr = new JSONObject();
		mgmt_repr.put("mgmtObj", ip_addr_repr);
	}catch(JSONException e){
            Log.e(TAG, "error on building the json payload: ",e);
            return;
        }

    	intent.putExtra("content", mgmt_repr.toString());
    	intent.putExtra("Issuer", OpenMTC_android_package);
//    	intent.setPackage(OpenMTC_android_package);
    	intent.putExtra("replyAction", ConnectivityMgmtAction); 
	Log.v(TAG, "sending intent with content "+intent.getStringExtra("content")+" Issuer "+intent.getStringExtra("Issuer")+" and replyAction "+intent.getStringExtra("replyAction"));   	
	
	context.sendBroadcast(intent);
	Log.v(TAG, "sent intent with extras "+intent.getExtras().toString());   	
    }
    
	public static String getLocalIpAddress(){
		
		try {
	       for (Enumeration<NetworkInterface> en = NetworkInterface.getNetworkInterfaces();  
		       en.hasMoreElements();) {
		       NetworkInterface intf = en.nextElement();
		           for (Enumeration<InetAddress> enumIpAddr = intf.getInetAddresses(); enumIpAddr.hasMoreElements();) {
			           InetAddress inetAddress = enumIpAddr.nextElement();
			                if (!inetAddress.isLoopbackAddress() && !inetAddress.isLinkLocalAddress()) {
						Log.v(TAG, "found ip address "+inetAddress.getHostAddress().toString());
						if(Inet4Address.class.isInstance(inetAddress)){
							Log.v(TAG, "ip address is vs4 ");

						}
						if(Inet6Address.class.isInstance(inetAddress)){
							Log.v(TAG, "ip address is vs6 ");
						}
						if(!enumIpAddr.hasMoreElements()){
							Log.v(TAG, "returning ip address "+inetAddress.getHostAddress().toString());
			                		return inetAddress.getHostAddress().toString();
						}
			                }
			       }
			   }
		} catch (Exception ex) {
			Log.e("IP Address", ex.toString());
		}
		return null;
	}
}
	

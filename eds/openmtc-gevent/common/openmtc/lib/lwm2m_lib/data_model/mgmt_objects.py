
#LWM2MSecurity
security_resources_list={}
reverse_security_resources_list={}

#LWM2MServer
server_resources_list = {
    "0" : {"resInstID" : 0, "multiInst": False, "resName" : "ShortServerID", "type" : "integer", "operation" : "R", "resValue" : ""},
    "1" : {"resInstID" : 0, "multiInst": False, "resName" : "LifeTime", "type" : "integer", "operation" : "RW", "resValue" : ""},
    "2" : {"resInstID" : 0, "multiInst" : False, "resName" : "DefaultMinimumPeriod", "type" : "integer", "operation" : "RW", "resValue" : ""},
    "3" : {"resInstID" : 0, "multiInst" : False, "resName" : "DefaultMaximumPeriod", "type" : "integer", "operation" : "RW", "resValue" : ""},
    "4" : {"resInstID" : 0, "multiInst": False, "resName" : "Disable", "type" : "", "operation" : "E", "resValue" : ""},
    "5" : {"resInstID" : 0, "multiInst": False, "resName" : "DisableTimeout", "type" : "integer", "operation" : "RW", "resValue" : ""},
    "6" : {"resInstID" : 0, "multiInst": False, "resName" : "NotificationStoringWhenDisabledorOffline", "type" : "boolean", "operation" : "RW", "resValue" : ""},
    "7" : {"resInstID" : 0, "multiInst": False, "resName" : "Binding", "type" : "string", "operation" : "RW", "resValue" : ""},
    "8" : {"resInstID" : 0, "multiInst" : False, "resName" : "RegistrationUpdateTrigger", "operation" : "E", "resValue" : ""}
}

reverse_server_resources_list= {
    "ShortServerID" :                           {"resInstID" : 0, "multiInst": False, "resId" : "0", "type" : "integer", "operation" : "R", "resValue" : ""},
    "LifeTime" :                                {"resInstID" : 0, "multiInst": False, "resId" : "1", "type" : "integer", "operation" : "RW", "resValue" : ""},
    "DefaultMinimumPeriod" :                    {"resInstID" : 0, "multiInst" : False, "resId" : "2", "type" : "integer", "operation" : "RW", "resValue" : ""},
    "DefaultMaximumPeriod" :                    {"resInstID" : 0, "multiInst" : False, "resId" : "3", "type" : "integer", "operation" : "RW", "resValue" : ""},
    "Disable" :                                 {"resInstID" : 0, "multiInst": False, "resId" : "4", "type" : "", "operation" : "E", "resValue" : ""},
    "DisableTimeout" :                          {"resInstID" : 0, "multiInst": False, "resId" : "5", "type" : "integer", "operation" : "RW", "resValue" : ""},
    "NotificationStoringWhenDisabledorOffline" :{"resInstID" : 0, "multiInst": False, "resId" : "6", "type" : "boolean", "operation" : "RW", "resValue" : ""},
    "Binding" :                                 {"resInstID" : 0, "multiInst": False, "resId" : "7", "type" : "string", "operation" : "RW", "resValue" : ""},
    "RegistrationUpdateTrigger" :               {"resInstID" : 0, "multiInst" : False, "resId" : "8", "operation" : "E", "resValue" : ""}
}

#Access Control
access_control_resources_list={}
reverse_access_control_resources_list={}

#Device
device_resources_list = {
    "0" : {"resInstID" : 0, "multiInst": False, "resName" : "Manufacturer", "type" : "string", "operation" : "R", "resValue" : ""},
    "1" : {"resInstID" : 0, "multiInst": False, "resName" : "ModelNumber", "type" : "string","operation" :"R", "resValue" : ""},
    "2" : {"resInstID" : 0, "multiInst": False, "resName" : "SerialNumber", "type" : "string", "operation" :"R", "resValue" : ""},
    "3" : {"resInstID" : 0, "multiInst": False, "resName" : "FirmwareVersion", "type" : "string", "operation" :"R", "resValue" : ""},
    "4" : {"resInstID" : 0, "multiInst": False, "resName" : "Reboot", "type" : "", "operation" : "E", "resValue" : ""},
    "5" : {"resInstID" : 0, "multiInst": False, "resName" : "FactoryReset", "type" : "", "operation" : "E", "resValue" : ""},
    "6" : {"resInstID" : 0, "multiInst": True, "resName" : "AvailablePowerSources", "type" : "integer","operation" : "R", "resValue" : ""},
    "7" : {"resInstID" : 0, "multiInst": True, "resName" : "PowerSourceVoltages", "type" : "integer", "operation" : "R", "resValue" : ""},
    "8" : {"resInstID" : 0, "multiInst": True, "resName" : "PowerSourceCurrent", "type" : "integer", "operation" : "R", "resValue" : ""},
    "9" : { "resInstID" : 0, "multiInst": False, "resName" : "BatteryLevel", "type" : "integer", "operation" : "R", "resValue" : ""},
    "10" : {"resInstID" : 0, "multiInst": False, "resName" : "MemoryFree", "type" : "integer", "operation" : "R", "resValue" : ""},
    "11" : {"resInstID" : 0, "multiInst": True, "resName" : "ErrorCode" , "type" : "integer", "operation" : "R", "resValue" : ""},
    "12" : {"resInstID" : 0, "multiInst": False, "resName" : "ResetErrorCode", "type" : "", "operation" : "R", "resValue" : ""},
    "13" : {"resInstID" : 0, "multiInst": False, "resName" : "CurrentTime", "type" : "time", "operation" : "RW", "resValue" : ""},
    "14" : {"resInstID" : 0, "multiInst": False, "resName" : "UTCOffset", "type" : "string", "operation" : "RW", "resValue" : ""},
    "15" : {"resInstID" : 0, "multiInst": False, "resName" : "TimeZone", "type" : "string", "operation" : "RW", "resValue" : ""},
    "16" : {"resInstID" : 0, "multiInst": False, "resName" : "SupportedBindingandModes", "type" : "string", "operation" :"R", "resValue" : ""},
}
        
reverse_device_resources_list = {
    "Manufacturer" :             {"resInstID" : 0, "multiInst": False, "resId" : "0", "type" : "string", "operation" : "R", "resValue" : ""},
    "ModelNumber" :             {"resInstID" : 0, "multiInst": False, "resId" : "1", "type" : "string","operation" :"R", "resValue" : ""},
    "SerialNumber" :            {"resInstID" : 0, "multiInst": False, "resId" : "2", "type" : "string", "operation" :"R", "resValue" : ""},
    "FirmwareVersion" :         {"resInstID" : 0, "multiInst": False, "resId" : "3", "type" : "string", "operation" :"R", "resValue" : ""},
    "Reboot" :                  {"resInstID" : 0, "multiInst": False, "resId" : "4", "type" : "", "operation" : "E", "resValue" : ""},
    "FactoryReset" :            {"resInstID" : 0, "multiInst": False, "resId" : "5", "type" : "", "operation" : "E", "resValue" : ""},
    "AvailablePowerSources" :   {"resInstID" : 0, "multiInst": True, "resId" : "6", "type" : "integer","operation" : "R", "resValue" : ""},
    "PowerSourceVoltages" :     {"resInstID" : 0, "multiInst": True, "resId" : "7", "type" : "integer", "operation" : "R", "resValue" : ""},
    "PowerSourceCurrent" :      {"resInstID" : 0, "multiInst": True, "resId" : "8", "type" : "integer", "operation" : "R", "resValue" : ""},
    "BatteryLevel" :            { "resInstID" : 0, "multiInst": False, "resId" : "9", "type" : "integer", "operation" : "R", "resValue" : ""},
    "MemoryFree" :              {"resInstID" : 0, "multiInst": False, "resId" : "10", "type" : "integer", "operation" : "R", "resValue" : ""},
    "ErrorCode" :               {"resInstID" : 0, "multiInst": True, "resId" : "11" , "type" : "integer", "operation" : "R", "resValue" : ""},
    "ResetErrorCode" :          {"resInstID" : 0, "multiInst": False, "resId" : "12", "type" : "", "operation" : "R", "resValue" : ""},
    "CurrentTime" :             {"resInstID" : 0, "multiInst": False, "resId" : "13", "type" : "time", "operation" : "RW", "resValue" : ""},
    "UTCOffset" :               {"resInstID" : 0, "multiInst": False, "resId" : "14", "type" : "string", "operation" : "RW", "resValue" : ""},
    "TimeZone" :                {"resInstID" : 0, "multiInst": False, "resId" : "15", "type" : "string", "operation" : "RW", "resValue" : ""},
    "SupportedBindingandModes" : {"resInstID" : 0, "multiInst": False, "resId" : "16", "type" : "string", "operation" :"R", "resValue" : ""},
}

#Connectivity Monitoring        
connectivity_monitoring_resources_list = {
    "0" : {"resInstID" : 0, "multiInst" : False, "resName" : "NetworkBearer", "type" : "integer", "operation" : "R", "resValue" : ""},
    "1" : {"resInstID" : 0, "multiInst" : True, "resName" : "AvailableNetworkBearer", "type" : "integer", "operation" : "R", "resValue" : ""},
    "2" : {"resInstID" : 0, "multiInst" : False, "resName" : "RadioSignalStrength", "type" : "integer", "operation" : "R", "resValue" : ""},
    "3" : {"resInstID" : 0, "multiInst" : False, "resName" : "LinkQuality", "type" : "integer", "operation" : "R", "resValue" : ""},
    "4" : {"resInstID" : 0, "multiInst" : True, "resName" : "IPAddresses", "type" : "string", "operation" : "R", "resValue" : ""},
    "5" : {"resInstID" : 0, "multiInst" : True, "resName" : "RouterIPAddresses", "type" : "string", "operation" : "R", "resValue" : ""},
    "6" : {"resInstID" : 0, "multiInst" : False, "resName" : "LinkUtilization", "type" : "integer", "operation" : "R", "resValue" : ""},
    "7" : {"resInstID" : 0, "multiInst" : True, "resName" : "APN", "type" : "string", "operation" : "R", "resValue" : ""},
    "8" : {"resInstID" : 0, "multiInst" : False, "resName" : "CellID", "type" : "integer", "operation" : "R", "resValue" : ""},
    "9" : {"resInstID" : 0, "multiInst" : False, "resName" : "SMNC", "type" : "integer", "operation" : "R", "resValue" : ""},
    "10" : {"resInstID" : 0, "multiInst" : False, "resName" : "SMCC", "type" : "integer", "operation" : "R", "resValue" : ""}
}

reverse_connectivity_monitoring_resources_list={
    "NetworkBearer" :               {"resInstID" : 0, "multiInst" : False, "resId" : "0", "resName" : "NetworkBearer", "type" : "integer", "operation" : "R", "resValue" : ""},
    "AvailableNetworkBearer" :    {"resInstID" : 0, "multiInst" : True,  "resId" : "1", "resName" : "AvailableNetworkBearer", "type" : "integer", "operation" : "R", "resValue" : ""},
    "RadioSignalStrength" :       {"resInstID" : 0, "multiInst" : False, "resId" : "2", "resName" : "RadioSignalStrength", "type" : "integer", "operation" : "R", "resValue" : ""},
    "LinkQuality" :                {"resInstID" : 0, "multiInst" : False, "resId" : "3", "resName" : "LinkQuality", "type" : "integer", "operation" : "R", "resValue" : ""},
    "IPAddresses" :                {"resInstID" : 0, "multiInst" : True,  "resId" : "4", "resName" : "IPAddresses", "type" : "string", "operation" : "R", "resValue" : ""},
    "RouterIPAddresses" :         {"resInstID" : 0, "multiInst" : True,  "resId" : "5", "resName" : "RouterIPAddresses", "type" : "string", "operation" : "R", "resValue" : ""},
    "LinkUtilization" :            {"resInstID" : 0, "multiInst" : False, "resId" : "6", "resName" : "LinkUtilization", "type" : "integer", "operation" : "R", "resValue" : ""},
    "APN" :                         {"resInstID" : 0, "multiInst" : True,  "resId" : "7", "resName" : "APN", "type" : "string", "operation" : "R", "resValue" : ""},
    "CellID" :                     {"resInstID" : 0, "multiInst" : False, "resId" : "8", "resName" : "CellID", "type" : "integer", "operation" : "R", "resValue" : ""},
    "SMNC" :                        {"resInstID" : 0, "multiInst" : False, "resId" : "9", "resName" : "SMNC", "type" : "integer", "operation" : "R", "resValue" : ""},
    "SMCC" :                        {"resInstID" : 0, "multiInst" : False, "resId" : "10", "resName" : "SMCC", "type" : "integer", "operation" : "R", "resValue" : ""}
}

#Firmware Update
firmware_update_resources_list={
    "0" : {"resInstID" : 0, "multiInst" : False, "resName" : "Package", "type" : "opaque", "operation" : "W", "resValue" : ""},
    "1" : {"resInstID" : 0, "multiInst" : False, "resName" : "PackageURI", "type" : "string", "operation" : "W", "resValue" : ""},
    "2" : {"resInstID" : 0, "multiInst" : False, "resName" : "Update", "type" : "", "operation" : "E", "resValue" : ""},
    "3" : {"resInstID" : 0, "multiInst" : False, "resName" : "State", "type" : "integer", "operation" : "R", "resValue" : ""},
    "4" : {"resInstID" : 0, "multiInst" : False, "resName" : "UpdateSupportedObjects", "type" : "boolean", "operation" : "RW", "resValue" : ""},
    "5" : {"resInstID" : 0, "multiInst" : False, "resName" : "UpdateResult", "type" : "integer", "operation" : "R", "resValue" : ""}
}
        
reverse_firmware_update_resources_list={
    "Package" :                 {"resInstID" : 0, "multiInst" : False, "resId" : "0", "resName" : "Package", "type" : "opaque", "operation" : "W", "resValue" : ""},
    "PackageURI" :              {"resInstID" : 0, "multiInst" : False, "resId" : "1", "resName" : "PackageURI", "type" : "string", "operation" : "W", "resValue" : ""},
    "Update" :                  {"resInstID" : 0, "multiInst" : False, "resId" : "2", "resName" : "Update", "type" : "", "operation" : "E", "resValue" : ""},
    "State" :                   {"resInstID" : 0, "multiInst" : False, "resId" : "3", "resName" : "State", "type" : "integer", "operation" : "R", "resValue" : ""},
    "UpdateSupportedObjects" :  {"resInstID" : 0, "multiInst" : False, "resId" : "4", "resName" : "UpdateSupportedObjects", "type" : "boolean", "operation" : "RW", "resValue" : ""},
    "UpdateResult" :            {"resInstID" : 0, "multiInst" : False, "resId" : "5", "resName" : "UpdateResult", "type" : "integer", "operation" : "R", "resValue" : ""}
}

#Location
location_resources_list={
    "0" : {"resInstID" : 0, "multiInst" : False, "resName" : "Latitude", "type" : "string", "operation" : "R", "resValue" : ""},
    "1" : {"resInstID" : 0, "multiInst" : False, "resName" : "Longitude", "type" : "string", "operation" : "R", "resValue" : ""},
    "2" : {"resInstID" : 0, "multiInst" : False, "resName" : "Altitude", "type" : "string", "operation" : "R", "resValue" : ""},
    "3" : {"resInstID" : 0, "multiInst" : False, "resName" : "Uncertainty", "type" : "string", "operation" : "R", "resValue" : ""},
    "4" : {"resInstID" : 0, "multiInst" : False, "resName" : "Velocity", "type" : "opaque", "operation" : "R", "resValue" : ""},
    "5" : {"resInstID" : 0, "multiInst" : False, "resName" : "TimeStamp", "type" : "time", "operation" : "R", "resValue" :""}
}

reverse_location_resources_list={
    "Latitude" :    {"resInstID" : 0, "multiInst" : False, "resId" : "0", "resName" : "Latitude", "type" : "string", "operation" : "R", "resValue" : ""},
    "Longitude" :   {"resInstID" : 0, "multiInst" : False, "resId" : "1", "resName" : "Longitude", "type" : "string", "operation" : "R", "resValue" : ""},
    "Altitude" :    {"resInstID" : 0, "multiInst" : False, "resId" : "2", "resName" : "Altitude", "type" : "string", "operation" : "R", "resValue" : ""},
    "Uncertainty" : {"resInstID" : 0, "multiInst" : False, "resId" : "3", "resName" : "Uncertainty", "type" : "string", "operation" : "R", "resValue" : ""},
    "Velocity" :    {"resInstID" : 0, "multiInst" : False, "resId" : "4", "resName" : "Velocity", "type" : "opaque", "operation" : "R", "resValue" : ""},
    "TimeStamp" :   {"resInstID" : 0, "multiInst" : False, "resId" : "5", "resName" : "TimeStamp", "type" : "time", "operation" : "R", "resValue" :""}
}

#Connectivity Statistics
connectivity_statistics_resources_list={
    "0" : {"resInstID" : 0, "multiInst" : False, "resName" : "SMSTxCounter", "type" : "integer", "operation" : "R", "resValue" : ""},
    "1" : {"resInstID" : 0, "multiInst" : False, "resName" : "SMSRxCounter", "type" : "integer", "operation" : "R", "resValue" : ""},
    "2" : {"resInstID" : 0, "multiInst" : False, "resName" : "TxData", "type" : "integer", "operation" : "R", "resValue" : ""},
    "3" : {"resInstID" : 0, "multiInst" : False, "resName" : "RxData", "type" : "integer", "operation" : "R", "resValue" : ""},
    "4" : {"resInstID" : 0, "multiInst" : False, "resName" : "MaxMessageSize", "type" : "integer", "operation" : "R", "resValue" : ""},
    "5" : {"resInstID" : 0, "multiInst" : False, "resName" : "AverageMessageSize", "type" : "integer", "operation" : "R", "resValue" : ""},
    "6" : {"resInstID" : 0, "multiInst" : False, "resName" : "StartOrReset", "type" : "", "operation" : "E", "resValue" : ""}
}
reverse_connectivity_statistics_resources_list={
    "SMSTxCounter" :        {"resInstID" : 0, "multiInst" : False, "resId" : "0", "resName" : "SMSTxCounter", "type" : "integer", "operation" : "R", "resValue" : ""},
    "SMSRxCounter" :        {"resInstID" : 0, "multiInst" : False, "resId" : "1", "resName" : "SMSRxCounter", "type" : "integer", "operation" : "R", "resValue" : ""},
    "TxData" :              {"resInstID" : 0, "multiInst" : False, "resId" : "2", "resName" : "TxData", "type" : "integer", "operation" : "R", "resValue" : ""},
    "RxData" :              {"resInstID" : 0, "multiInst" : False, "resId" : "3", "resName" : "RxData", "type" : "integer", "operation" : "R", "resValue" : ""},
    "MaxMessageSize" :      {"resInstID" : 0, "multiInst" : False, "resId" : "4", "resName" : "MaxMessageSize", "type" : "integer", "operation" : "R", "resValue" : ""},
    "AverageMessageSize" :  {"resInstID" : 0, "multiInst" : False, "resId" : "5", "resName" : "AverageMessageSize", "type" : "integer", "operation" : "R", "resValue" : ""},
    "StartOrReset" :        {"resInstID" : 0, "multiInst" : False, "resId" : "6", "resName" : "StartOrReset", "type" : "", "operation" : "E", "resValue" : ""}
}

################################################################################
#
# Connectivity Management Objects
#
#    Implementation according to: LwM2M Object -- ConnMgmt Candidate 
#    Version 1.0 -- 13 Jan 2015
#
################################################################################

# Cellular network connectivity
#    This object specifies resources to enable a device to connect to a 3GPP 
#    or 3GPP2 bearer, including GPRS/EDGE, UMTS, LTE, SMS. For cellular 
#    connectivity, this object focuses on Packet Switched (PS) connectivity
#    and does not aim to provide comprehensive Circuit Switched (CS) connectivity 
#    management.
cellular_connectivity_resources_list={
    "4000" : {"resInstID"       : 0,
              "resName"         : "ActivatedProfileNames",
              "operation"       : "R",
              "multiInst"       : True,
              "type"            : "objlnk",
              "resUnit"         : "",
              "resValue"        : ""
              # Mandatory resource definition.  
              # Links to instances of the APN connection profile object representing 
              # every APN connection profile that has an activate connection to a PDN
              },
    "0"    : {"resInstID"       : 0,
              "resName"         : "SMSCAddress",
              "operation"       : "RW",
              "multiInst"       : False,
              "type"            : "string",
              "resUnit"         : "",
              "resValue"        : "",
              # Optional resource definition.  E.164 address of SMSC.  
              #
              # Applicable for 3GPP2 networks where SMSC is not available from a 
              # smart card, or for 3GPP/3GPP2 networks to provide the application with 
              # a customer specific SMSC. The application decides how to use this 
              # parameter, e.g. precedence over UICC based SMSC address.
              },
    "1"    : {"resInstID"       : 0,
              "resName"         : "DisableRadioPeriod",
              "operation"       : "RW",
              "multiInst"       : False,
              "type"            : "integer",
              "resUnit"         : "s",  # valid range is 0 -- 86400
              "resValue"        : "",
              # Optional resource definition.  Time period for which device shall
              # disconnect from cellular radio (PS detach, CS detach if applicable).
              # Can be used to handle network overload situations
              },          
    "2"    : {"resInstID"       : 0,
              "resName"         : "ModuleActivationCode",
              "operation"       : "RW",
              "multiInst"       : False,
              "type"            : "string",
              "resUnit"         : "",
              "resValue"        : "",
              # Optional resource definition.  Configurable in case the application
              # needs to issue a code (e.g. via AT command) to activate the 
              # module. e.g. "*98".
              },
    "3"    : {"resInstID"       : 0,
              "resName"         : "VendorSpecificExtensions",
              "operation"       : "R",
              "multiInst"       : False,
              "type"            : "objlnk",
              "resUnit"         : "",
              "resValue"        : "",
              # Optional resource definition.  Links to a vendor specific object.
              }
    }

reverse_cellular_connectivity_resources_list={
    "ActivatedProfileNames" : {
              "resInstID"       : 0,
              "resId"           : "4000",
              "operation"       : "R",
              "multiInst"       : True,
              "type"            : "objlnk",
              "resUnit"         : "",
              "resValue"        : ""
              # Mandatory resource definition.  
              # Links to instances of the APN connection profile object representing 
              # every APN connection profile that has an activate connection to a PDN
              },
    "SMSCAddress"    : {
              "resInstID"       : 0,
              "resId"           : "0",
              "operation"       : "RW",
              "multiInst"       : False,
              "type"            : "string",
              "resUnit"         : "",
              "resValue"        : "",
              # Optional resource definition.  E.164 address of SMSC.  
              #
              # Applicable for 3GPP2 networks where SMSC is not available from a 
              # smart card, or for 3GPP/3GPP2 networks to provide the application with 
              # a customer specific SMSC. The application decides how to use this 
              # parameter, e.g. precedence over UICC based SMSC address.
              },
    "DisableRadioPeriod"    : {
              "resInstID"       : 0,
              "resId"           : "1",
              "operation"       : "RW",
              "multiInst"       : False,
              "type"            : "integer",
              "resUnit"         : "s",  # valid range is 0 -- 86400
              "resValue"        : "",
              # Optional resource definition.  Time period for which device shall
              # disconnect from cellular radio (PS detach, CS detach if applicable).
              # Can be used to handle network overload situations
              },          
    "ModuleActivationCode"    : {
              "resInstID"       : 0,
              "resId"           : "2",
              "operation"       : "RW",
              "multiInst"       : False,
              "type"            : "string",
              "resUnit"         : "",
              "resValue"        : "",
              # Optional resource definition.  Configurable in case the application
              # needs to issue a code (e.g. via AT command) to activate the 
              # module. e.g. "*98".
              },
    "VendorSpecificExtensions"    : {
              "resInstID"       : 0,
              "resId"           : "3",
              "operation"       : "R",
              "multiInst"       : False,
              "type"            : "objlnk",
              "resUnit"         : "",
              "resValue"        : "",
              # Optional resource definition.  Links to a vendor specific object.
              }
    }


# APN connection profile
#    This object specifies resources to enable a device to connect to an Access 
#    Point Name(APN)
apn_connection_profile_resources_list={
        "0"    : {"resInstID"       : 0,
                  "resName"         : "ProfileName",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  Human-readable identifier. Multiple
                  # connection profiles can share the same Access Point Name (APN)
                  # value but e.g. have different credentials.
                  }, 
        "1"    : {"resInstID"       : 0,
                  "resName"         : "APN",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  Presented to network during connection
                  # to PDN e.g. "internet.15.234". This resource is not included in 
                  # case "Auto select APN by device" resource has the value TRUE.
                  #
                  # If the APN resource is present but contains an empty string, then the device
                  # shall not provide an APN in the connection request (invoking default APN
                  # procedures in the network).
                  },
        "2"    : {"resInstID"       : 0,
                  "resName"         : "AutoSelectAPNByRWDevice",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "boolean",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  If this resource is present for a 
                  # connection profile, it enables the device to choose an APN according 
                  # to a device specific algorithm. It provides a fall-back mechanism 
                  # e.g. for some MVNO SIMs the configured APN may not work. Resource
                  # not included in case the "APN" resource is specified.
                  },
        "3"    : {"resInstID"       : 0,
                  "resName"         : "EnableStatus",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "boolean",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # True: connection is activated.   False: connection is de-activated.
                  # Allows the profile to be remotely activated or deactivated.
                  },        
        "4"    : {"resInstID"       : 0,
                  "resName"         : "AuthenticationType",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # Enumerated type:
                  #    0: PAP
                  #    1: CHAP
                  },                                                                                                                             
        "5"    : {"resInstID"       : 0,
                  "resName"         : "UserName",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Used with e.g. PAP
                  },  
        "6"    : {"resInstID"       : 0,
                  "resName"         : "Secret",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Used with e.g. PAP
                  },  
        "7"    : {"resInstID"       : 0,
                  "resName"         : "ReconnectSchedule",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Comma separated list of retry delay values in seconds to be 
                  # used in case of unsuccessful connection establishment 
                  # attempts. e.g. "10,60,600,3600,86400"
                  },                                     
        "8"    : {"resInstID"       : 0,
                  "resName"         : "Validity",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Comma separated mobile country code,then mobile network code
                  # (MCC, MNC), for which this APN is valid.
                  },    
        # Note for the following 4 resource definitions (ConnectionEstablishmentTime, 
        # ConnectionEstablishmentResult, ConnectionEstablishmentRejectCause, and 
        # ConnectionEndTime):
        #
        # For each activated PDP context request, the device may store at least one 
        # value of "Connection establishment time", "connection establishment result",
        # "Connection end time" and if activation is unsuccessful then a 
        # "connection establishment reject cause". It is a device decision how many 
        # instances to keep.
        "9"    : {"resInstID"       : 0,
                  "resName"         : "ConnectionEstablishmentTime",
                  "operation"       : "R",
                  "multiInst"       : True,
                  "type"            : "time",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # UTC time of connection request
                  },     
        "10"   : {"resInstID"       : 0,
                  "resName"         : "ConnectionEstablishmentResult",
                  "operation"       : "R",
                  "multiInst"       : True,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # 0 = accepted   ---  1 = rejected
                  },    
        "11"   : {"resInstID"       : 0,
                  "resName"         : "ConnectionEstablishmentRejectCause",
                  "operation"       : "R",
                  "multiInst"       : True,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Reject cause (3GPP TS 24.008).  Valid range: 0 -- 111
                  },    
        "12"   : {"resInstID"       : 0,
                  "resName"         : "ConnectionEndTime",
                  "operation"       : "R",
                  "multiInst"       : True,
                  "type"            : "time",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # UTC time of connection end.
                  },    
        "13"   : {"resInstID"       : 0,
                  "resName"         : "TotalBytesSent",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Rolling counter for total number of bytes sent via this interface 
                  # since last device reset.
                  },    
        "14"   : {"resInstID"       : 0,
                  "resName"         : "TotalBytesReceived",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Rolling counter for total number of bytes received via this 
                  # interface since last device reset.
                  },                    
        # Note for the following 6 resource definitions (IPAddress, PrefixLength, 
        # SubnetMask, Gateway, PrimaryDNSAddress, and SecondaryDNSAddress)
        #
        # These resources are used in case IP related parameters are defined statically, 
        # and are also set with the IP related parameters in case of dynamic IP address 
        # assignment. The normal use case would be to have one IPv4 and one IPv6 address 
        # which have each associated a prefix length (IPv6 only), a subnet mask, a gateway, 
        # and a primary and secondary DNS address.                             
        "15"   : {"resInstID"       : 0,
                  "resName"         : "IPAddress",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # May be IPv4 or IPv6 address.
                  },  
        "16"   : {"resInstID"       : 0,
                  "resName"         : "PrefixLength",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Associated with IPv6 address.
                  },                             
        "17"   : {"resInstID"       : 0,
                  "resName"         : "SubnetMask",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  },
        "18"   : {"resInstID"       : 0,
                  "resName"         : "Gateway",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  },           
        "19"   : {"resInstID"       : 0,
                  "resName"         : "PrimaryDNSAddress",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  },                            
        "20"   : {"resInstID"       : 0,
                  "resName"         : "SecondaryDNSAddress",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  },               
        "21"   : {"resInstID"       : 0,
                  "resName"         : "QCI",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # For LTE only.
                  # QCI=Quality of service Class Identifier
                  # This resource enables the LWM2M server to signal the LWM2M 
                  # client which QCI it shall request from the network. 
                  # See [3GPP-TS_23.203] for a description of QCI values.
                  #
                  # Note: For LTE a higher QoS may be established by setting up 
                  # an additional bearer ("dedicated bearer") in addition to the 
                  # default bearer which is established to the default APN. A 
                  # dedicated bearer which is set up by the network on request by the device containing a requested QCI value can either be established to the same APN as the default bearer or to another APN. The QoS of a dedicated bearer may be modified on request by the device. The association of QoS values and APNs for a subscriber is stored in the network and checked during the establishment of a bearer.
                  },           
        "22"   : {"resInstID"       : 0,
                  "resName"         : "VendorSpecificExtensions",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "objlnk",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Links to a vendor specific object.
                  }                                                                                                                                                               
    }                 

reverse_apn_connection_profile_resources_list={
        "ProfileName"    : {
                  "resInstID"       : 0,
                  "resID"           : "0",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  Human-readable identifier. Multiple
                  # connection profiles can share the same Access Point Name (APN)
                  # value but e.g. have different credentials.
                  }, 
        "APN"    : {
                  "resInstID"       : 0,
                  "resID"           : "1",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  Presented to network during connection
                  # to PDN e.g. "internet.15.234". This resource is not included in 
                  # case "Auto select APN by device" resource has the value TRUE.
                  #
                  # If the APN resource is present but contains an empty string, then the device
                  # shall not provide an APN in the connection request (invoking default APN
                  # procedures in the network).
                  },
        "AutoSelectAPNByRWDevice"   : {
                  "resInstID"       : 0,
                  "resID"           : "2",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "boolean",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  If this resource is present for a 
                  # connection profile, it enables the device to choose an APN according 
                  # to a device specific algorithm. It provides a fall-back mechanism 
                  # e.g. for some MVNO SIMs the configured APN may not work. Resource
                  # not included in case the "APN" resource is specified.
                  },
        "EnableStatus"    : {
                  "resInstID"       : 0,
                  "resID"           : "3",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "boolean",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # True: connection is activated.   False: connection is de-activated.
                  # Allows the profile to be remotely activated or deactivated.
                  },        
        "AuthenticationType"    : {
                  "resInstID"       : 0,
                  "resID"           : "4",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # Enumerated type:
                  #    0: PAP
                  #    1: CHAP
                  },                                                                                                                             
        "UserName"    : {
                  "resInstID"       : 0,
                  "resID"           : "5",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Used with e.g. PAP
                  },  
        "Secret"    : {
                  "resInstID"       : 0,
                  "resID"           : "6",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Used with e.g. PAP
                  },  
        "ReconnectSchedule"    : {
                  "resInstID"       : 0,
                  "resID"           : "7",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Comma separated list of retry delay values in seconds to be 
                  # used in case of unsuccessful connection establishment 
                  # attempts. e.g. "10,60,600,3600,86400"
                  },                                     
        "Validity"    : {
                  "resInstID"       : 0,
                  "resID"           : "8",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Comma separated mobile country code,then mobile network code
                  # (MCC, MNC), for which this APN is valid.
                  },    
        # Note for the following 4 resource definitions (ConnectionEstablishmentTime, 
        # ConnectionEstablishmentResult, ConnectionEstablishmentRejectCause, and 
        # ConnectionEndTime):
        #
        # For each activated PDP context request, the device may store at least one 
        # value of "Connection establishment time", "connection establishment result",
        # "Connection end time" and if activation is unsuccessful then a 
        # "connection establishment reject cause". It is a device decision how many 
        # instances to keep.
        "ConnectionEstablishmentTime"    : {
                  "resInstID"       : 0,
                  "resID"           : "9",
                  "operation"       : "R",
                  "multiInst"       : True,
                  "type"            : "time",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # UTC time of connection request
                  },     
        "ConnectionEstablishmentResult"   : {
                  "resInstID"       : 0,
                  "resID"           : "10",
                  "operation"       : "R",
                  "multiInst"       : True,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # 0 = accepted   ---  1 = rejected
                  },    
        "ConnectionEstablishmentRejectCause"   : {
                  "resInstID"       : 0,
                  "resID"           : "11",
                  "operation"       : "R",
                  "multiInst"       : True,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Reject cause (3GPP TS 24.008).  Valid range: 0 -- 111
                  },    
        "ConnectionEndTime"   : {
                  "resInstID"       : 0,
                  "resID"           : "12",
                  "operation"       : "R",
                  "multiInst"       : True,
                  "type"            : "time",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # UTC time of connection end.
                  },    
        "TotalBytesSent"   : {
                  "resInstID"       : 0,
                  "resID"           : "13",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Rolling counter for total number of bytes sent via this interface 
                  # since last device reset.
                  },    
        "TotalBytesReceived"   : {
                  "resInstID"       : 0,
                  "resID"           : "14",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Rolling counter for total number of bytes received via this 
                  # interface since last device reset.
                  },                    
        # Note for the following 6 resource definitions (IPAddress, PrefixLength, 
        # SubnetMask, Gateway, PrimaryDNSAddress, and SecondaryDNSAddress)
        #
        # These resources are used in case IP related parameters are defined statically, 
        # and are also set with the IP related parameters in case of dynamic IP address 
        # assignment. The normal use case would be to have one IPv4 and one IPv6 address 
        # which have each associated a prefix length (IPv6 only), a subnet mask, a gateway, 
        # and a primary and secondary DNS address.                             
        "IPAddress"   : {
                  "resInstID"       : 0,
                  "resID"           : "15",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # May be IPv4 or IPv6 address.
                  },  
        "PrefixLength"   : {
                  "resInstID"       : 0,
                  "resID"           : "16",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Associated with IPv6 address.
                  },                             
        "SubnetMask"   : {
                  "resInstID"       : 0,
                  "resID"           : "17",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  },
        "Gateway"   : {
                  "resInstID"       : 0,
                  "resID"           : "18",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  },           
        "PrimaryDNSAddress"   : {
                  "resInstID"       : 0,
                  "resID"           : "19",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  },                            
        "SecondaryDNSAddress"   : {
                  "resInstID"       : 0,
                  "resID"           : "20",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  },               
        "QCI"   : {
                  "resInstID"       : 0,
                  "resID"           : "21",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # For LTE only.
                  # QCI=Quality of service Class Identifier
                  # This resource enables the LWM2M server to signal the LWM2M 
                  # client which QCI it shall request from the network. 
                  # See [3GPP-TS_23.203] for a description of QCI values.
                  #
                  # Note: For LTE a higher QoS may be established by setting up 
                  # an additional bearer ("dedicated bearer") in addition to the 
                  # default bearer which is established to the default APN. A 
                  # dedicated bearer which is set up by the network on request by the device containing a requested QCI value can either be established to the same APN as the default bearer or to another APN. The QoS of a dedicated bearer may be modified on request by the device. The association of QoS values and APNs for a subscriber is stored in the network and checked during the establishment of a bearer.
                  },           
        "VendorSpecificExtensions"   : {
                  "resInstID"       : 0,
                  "resID"           : "22",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "objlnk",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Links to a vendor specific object.
                  }                                                                                                                                                               
    }       




# WLAN connectivity resources list
#    This object specifies resources to enable a device to connect to 
#    a WLAN bearer.
wlan_connectivity_resources_list={
        "0"    : {"resInstID"       : 0,
                  "resName"         : "InterfaceName",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # Human-readable identifier, e.g. wlan0
                  }, 
        "1"    : {"resInstID"       : 0,
                  "resName"         : "Enable",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "boolean",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # 0: Disabled
                  # 1: Enabled
                  # Enable / Disable interface:  When disabled 
                  # radio must also be disable
                  },
        # Note:  Standard  Lightweight M2M -- Connectivity Management Object (LwM2M
        # Object -- ConnMgmt), Candidate Version 1.0 -- 13 Jan 2015, does only
        # define values for operation in the 2.4GHz and 5GHz band even though
        # IEEE 802.11 standardizes operation in additional bands as well. 
        "2"    : {"resInstID"       : 0,
                  "resName"         : "RadioEnabled",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # 0: Disabled
                  # 1: 2.4 GHz
                  # 2: 5 GHz
                  },     
        "3"    : {"resInstID"       : 0,
                  "resName"         : "Status",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # 0: Disabled
                  # 1: UP (OK)
                  # 2: Error
                  },                                                                 
        "4"    : {"resInstID"       : 0,
                  "resName"         : "BSSID",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "string",  # 12 bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # The MAC address of the interface, in
                  # hexadecimal form.
                  },       
        "5"    : {"resInstID"       : 0,
                  "resName"         : "SSID",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "string",  # 1 -- 32 bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # The Service Set Identifier for this
                  # interface.
                  },       
        "6"    : {"resInstID"       : 0,
                  "resName"         : "BroadcastSSID",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "boolean",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # 0: Do not broadcast SSID
                  # 1: Broadcast SSID
                  }, 
        "7"    : {"resInstID"       : 0,
                  "resName"         : "BeaconEnabled",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "boolean",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # 0: Do not broadcast beacons
                  # 1: Broadcast beacons
                  },    
        "8"    : {"resInstID"       : 0,
                  "resName"         : "Mode",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # 0: Do not broadcast beacons
                  # 1: Broadcast beacons
                  },        
        "9"    : {"resInstID"       : 0,
                  "resName"         : "Channel",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer", # range: 0 -- 255
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # The current radio channel in use by
                  # this interface.
                  },                                   
        "10"   : {"resInstID"       : 0,
                  "resName"         : "AutoChannel",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "boolean",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # 0: Disabled
                  # 1: Enabled
                  },   
        "11"   : {"resInstID"       : 0,
                  "resName"         : "SupportedChannels",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Array of supported radio channels.
                  }, 
        "12"   : {"resInstID"       : 0,
                  "resName"         : "ChannelsInUse",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Array of channels which the access
                  # point has determined are "in use".
                  # Including any channels in-use by
                  # access point itself.                  
                  },
        "13"   : {"resInstID"       : 0,
                  "resName"         : "RegulatoryDomain",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "string",  ## 3 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # 802.11d Regulatory Domain String.
                  # First two octets are ISO/IEC 3166-1
                  # two-character country code. The third octet is 
                  # either " " (all environments), "0" (outside) 
                  # or "I" (inside).            
                  },    
        # Attention:  The standard is inconsistent for Res ID 2 and 14.
        # ResID 14 allows to specify 802.11ah (sub-1G operation) but
        # ResID 2 does not allow to specify sub-1g bands.  As both
        # resource IDs are mandatory, this might cause issues when
        # filling the management object with information for 11ah systems.                                         
        "14"   : {"resInstID"       : 0,
                  "resName"         : "Standard",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # 0: 802.11a
                  # 1: 802.11b
                  # 2: 802.11bg
                  # 3: 802.11g
                  # 4: 802.11n
                  # 5: 802.11bgn
                  # 6: 802.11ac
                  # 7: 802.11ah          
                  },     
        "15"   : {"resInstID"       : 0,
                  "resName"         : "AuthenticationMode",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # 0: None (Open)
                  # 1: PSK
                  # 2: EAP
                  # 3: EAP+PSK
                  # 4: EAPSIM
                  },     
        # Note for EncryptionMode resource:
        # WEP is supported by this object for legacy devices. All encryption 
        # parameter resources are optional e.g. a Wifi Alliance "HotSpot 2.0" 
        # device would not support WEP related resources.    
        "16"   : {"resInstID"       : 0,
                  "resName"         : "EncryptionMode",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # 0: AES (WPA2)
                  # 1: TKIP (WPA)
                  # 2: WEP (1)
                  },          
        "17"   : {"resInstID"       : 0,
                  "resName"         : "WPAPreSharedKey",
                  "operation"       : "W",
                  "multiInst"       : False,
                  "type"            : "string",  # 64 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # WPA/WPA2 Key expressed as a hex string.
                  # Write - Only.
                  },     
        "18"   : {"resInstID"       : 0,
                  "resName"         : "WPAKeyPhrase",
                  "operation"       : "W",
                  "multiInst"       : False,
                  "type"            : "string",  # 1 -- 64 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # WPA/WPA2 Key Phrase.
                  # Write Only.
                  },                                                                  
        "19"   : {"resInstID"       : 0,
                  "resName"         : "WEPEncryptionType",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # 0: None
                  # 1: 40-bit
                  # 2: 104-bit
                  },     
        "20"   : {"resInstID"       : 0,
                  "resName"         : "WEPKeyIndex",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer", # range 1 -- 4
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Index of the default WEP key.
                  },            
        "21"   : {"resInstID"       : 0,
                  "resName"         : "WEPKeyPhrase",
                  "operation"       : "W",
                  "multiInst"       : False,
                  "type"            : "string", # 1 -- 65 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Index of the default WEP key.
                  },                   
        "22"   : {"resInstID"       : 0,
                  "resName"         : "WEPKey1",
                  "operation"       : "W",
                  "multiInst"       : False,
                  "type"            : "string", # 10 or 26 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # WEP Key 1 expressed as a hexadecimal string.
                  # 10 Bytes for a 40 Bit key
                  # 26 Bytes for a 104 Bit key
                  },                
        "23"   : {"resInstID"       : 0,
                  "resName"         : "WEPKey2",
                  "operation"       : "W",
                  "multiInst"       : False,
                  "type"            : "string", # 10 or 26 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # WEP Key 2 expressed as a hexadecimal string.
                  # 10 Bytes for a 40 Bit key
                  # 26 Bytes for a 104 Bit key
                  },          
        "24"   : {"resInstID"       : 0,
                  "resName"         : "WEPKey3",
                  "operation"       : "W",
                  "multiInst"       : False,
                  "type"            : "string", # 10 or 26 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # WEP Key 3 expressed as a hexadecimal string.
                  # 10 Bytes for a 40 Bit key
                  # 26 Bytes for a 104 Bit key
                  },                                   
        "25"   : {"resInstID"       : 0,
                  "resName"         : "WEPKey4",
                  "operation"       : "W",
                  "multiInst"       : False,
                  "type"            : "string", # 10 or 26 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # WEP Key 4 expressed as a hexadecimal string.
                  # 10 Bytes for a 40 Bit key
                  # 26 Bytes for a 104 Bit key
                  }, 
        "26"   : {"resInstID"       : 0,
                  "resName"         : "RADIUSServer",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "string", # 1 - 125 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # RADIUS Authentication Server Address
                  }, 
        "27"   : {"resInstID"       : 0,
                  "resName"         : "RADIUSServerPort",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # RADIUS Authentication Server Port Number
                  }, 
        "28"   : {"resInstID"       : 0,
                  "resName"         : "RADIUSSecret",
                  "operation"       : "W",
                  "multiInst"       : False,
                  "type"            : "string", # 1 - 256 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # RADIUS Shared Secret
                  }, 
        "29"   : {"resInstID"       : 0,
                  "resName"         : "WMMSupported",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "boolean",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # 0: WMM NOT Supported
                  # 1: WMM Wupported
                  },                                                                                                       
        "30"   : {"resInstID"       : 0,
                  "resName"         : "WMMEnabled",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "boolean",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # 0: Disabled
                  # 1: Enabled
                  },  
        "31"   : {"resInstID"       : 0,
                  "resName"         : "MACControlEnabled",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "boolean",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # 0: Any Client MAC Address accepted
                  # 1: Client MAC address must exist in
                  # MACAddressList
                  },                                      
        "32"   : {"resInstID"       : 0,
                  "resName"         : "MACAddressList",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "string",  # 12 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Array of allowed client MAC addresses, in 
                  # hexadecimal form.
                  }, 
        "33"   : {"resInstID"       : 0,
                  "resName"         : "TotalBytesSent",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Total number of bytes sent via this interface
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  }, 
        "34"   : {"resInstID"       : 0,
                  "resName"         : "TotalBytesReceived",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Total number of bytes received via this interface
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },  
        "35"   : {"resInstID"       : 0,
                  "resName"         : "TotalPacketsSent",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Total number of packets sent via this interface
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },                                       
        "36"   : {"resInstID"       : 0,
                  "resName"         : "TotalPacketsReceived",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Total number of packets received via this interface
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },   
        "37"   : {"resInstID"       : 0,
                  "resName"         : "TransmitErrors",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Total number of packets which could not be 
                  # transmitted because of errors.
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },               
        "38"   : {"resInstID"       : 0,
                  "resName"         : "ReceiveErrors",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Total number of packets received with errors 
                  # which prevented those packets from being delivered.
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },       
        "39"   : {"resInstID"       : 0,
                  "resName"         : "UnicastPacketsSent",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Count of Unicast Packets Sent
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },
        "40"   : {"resInstID"       : 0,
                  "resName"         : "UnicastPacketsReceived",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Count of Unicast Packets received
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },          
        "41"   : {"resInstID"       : 0,
                  "resName"         : "MulticastPacketsSent",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Count of Multicast Packets Sent
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },
        "42"   : {"resInstID"       : 0,
                  "resName"         : "MulticastPacketsReceived",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Count of Multicast Packets received
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },   
        "43"   : {"resInstID"       : 0,
                  "resName"         : "BroadcastPacketsSent",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Count of Broadcast Packets Sent
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },
        "44"   : {"resInstID"       : 0,
                  "resName"         : "BroadcastPacketsReceived",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Count of Broadcast Packets received
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },       
        "45"   : {"resInstID"       : 0,
                  "resName"         : "DiscardPacketsSent",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Count of valid outbound packets intentionally discarded 
                  # without transmission, for example a packet may be 
                  # discarded to manage buffer space.
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },
        "46"   : {"resInstID"       : 0,
                  "resName"         : "DiscardPacketsReceived",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Count of valid packets received and intentionally discarded 
                  # without transmission, for example a packet may be 
                  # discarded to manage buffer space.
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },       
        "47"   : {"resInstID"       : 0,
                  "resName"         : "UnknownPacketsReceived",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Count of Unknown Packets Received
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },         
        "48"   : {"resInstID"       : 0,
                  "resName"         : "VendorSpecificExtensions",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "objlnk", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Links to a vendor specific object.
                  }
    }  

reverse_wlan_connectivity_resources_list={
        "InterfaceName"    : {
                  "resInstID"       : 0,
                  "resID"         : "0",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "string",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # Human-readable identifier, e.g. wlan0
                  }, 
        "Enable"    : {
                  "resInstID"       : 0,
                  "resID"           : "1",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "boolean",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # 0: Disabled
                  # 1: Enabled
                  # Enable / Disable interface:  When disabled 
                  # radio must also be disable
                  },
        # Note:  Standard  Lightweight M2M -- Connectivity Management Object (LwM2M
        # Object -- ConnMgmt), Candidate Version 1.0 -- 13 Jan 2015, does only
        # define values for operation in the 2.4GHz and 5GHz band even though
        # IEEE 802.11 standardizes operation in additional bands as well. 
        "RadioEnabled"    : {
                  "resInstID"       : 0,
                  "resID"           : "2",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # 0: Disabled
                  # 1: 2.4 GHz
                  # 2: 5 GHz
                  },     
        "Status"    : {
                  "resInstID"       : 0,
                  "resID"           : "3",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # 0: Disabled
                  # 1: UP (OK)
                  # 2: Error
                  },                                                                 
        "BSSID"    : {
                  "resInstID"       : 0,
                  "resID"           : "4",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "string",  # 12 bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # The MAC address of the interface, in
                  # hexadecimal form.
                  },       
        "SSID"    : {
                  "resInstID"       : 0,
                  "resID"           : "5",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "string",  # 1 -- 32 bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # The Service Set Identifier for this
                  # interface.
                  },       
        "BroadcastSSID"    : {
                  "resInstID"       : 0,
                  "resID"           : "6",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "boolean",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # 0: Do not broadcast SSID
                  # 1: Broadcast SSID
                  }, 
        "BeaconEnabled"    : {
                  "resInstID"       : 0,
                  "resID"           : "7",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "boolean",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # 0: Do not broadcast beacons
                  # 1: Broadcast beacons
                  },    
        "Mode"    : {
                  "resInstID"       : 0,
                  "resID"           : "8",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # 0: Do not broadcast beacons
                  # 1: Broadcast beacons
                  },        
        "Channel"    : {
                  "resInstID"       : 0,
                  "resID"           : "9",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer", # range: 0 -- 255
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # The current radio channel in use by
                  # this interface.
                  },                                   
        "AutoChannel"   : {
                  "resInstID"       : 0,
                  "resID"           : "10",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "boolean",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # 0: Disabled
                  # 1: Enabled
                  },   
        "SupportedChannels"   : {
                  "resInstID"       : 0,
                  "resID"           : "11",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Array of supported radio channels.
                  }, 
        "ChannelsInUse"   : {
                  "resInstID"       : 0,
                  "resID"           : "12",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Array of channels which the access
                  # point has determined are "in use".
                  # Including any channels in-use by
                  # access point itself.                  
                  },
        "RegulatoryDomain"   : {
                  "resInstID"       : 0,
                  "resID"           : "13",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "string",  ## 3 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # 802.11d Regulatory Domain String.
                  # First two octets are ISO/IEC 3166-1
                  # two-character country code. The third octet is 
                  # either " " (all environments), "0" (outside) 
                  # or "I" (inside).            
                  },    
        # Attention:  The standard is inconsistent for Res ID 2 and 14.
        # ResID 14 allows to specify 802.11ah (sub-1G operation) but
        # ResID 2 does not allow to specify sub-1g bands.  As both
        # resource IDs are mandatory, this might cause issues when
        # filling the management object with information for 11ah systems.                                         
        "Standard"   : {
                  "resInstID"       : 0,
                  "resID"           : "14",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # 0: 802.11a
                  # 1: 802.11b
                  # 2: 802.11bg
                  # 3: 802.11g
                  # 4: 802.11n
                  # 5: 802.11bgn
                  # 6: 802.11ac
                  # 7: 802.11ah          
                  },     
        "AuthenticationMode"   : {
                  "resInstID"       : 0,
                  "resID"           : "15",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Mandatory resource definition.  
                  # 0: None (Open)
                  # 1: PSK
                  # 2: EAP
                  # 3: EAP+PSK
                  # 4: EAPSIM
                  },     
        # Note for EncryptionMode resource:
        # WEP is supported by this object for legacy devices. All encryption 
        # parameter resources are optional e.g. a Wifi Alliance "HotSpot 2.0" 
        # device would not support WEP related resources.    
        "EncryptionMode"   : {
                  "resInstID"       : 0,
                  "resID"           : "16",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # 0: AES (WPA2)
                  # 1: TKIP (WPA)
                  # 2: WEP (1)
                  },          
        "WPAPreSharedKey"   : {
                  "resInstID"       : 0,
                  "resID"           : "17",
                  "operation"       : "W",
                  "multiInst"       : False,
                  "type"            : "string",  # 64 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # WPA/WPA2 Key expressed as a hex string.
                  # Write - Only.
                  },     
        "WPAKeyPhrase"   : {
                  "resInstID"       : 0,
                  "resID"           : "18",
                  "operation"       : "W",
                  "multiInst"       : False,
                  "type"            : "string",  # 1 -- 64 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # WPA/WPA2 Key Phrase.
                  # Write Only.
                  },                                                                  
        "WEPEncryptionType"   : {
                  "resInstID"       : 0,
                  "resID"           : "19",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # 0: None
                  # 1: 40-bit
                  # 2: 104-bit
                  },     
        "WEPKeyIndex"   : {
                  "resInstID"       : 0,
                  "resID"           : "20",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer", # range 1 -- 4
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Index of the default WEP key.
                  },            
        "WEPKeyPhrase"   : {
                  "resInstID"       : 0,
                  "resID"           : "21",
                  "operation"       : "W",
                  "multiInst"       : False,
                  "type"            : "string", # 1 -- 65 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Index of the default WEP key.
                  },                   
        "WEPKey1"   : {
                  "resInstID"       : 0,
                  "resID"           : "22",
                  "operation"       : "W",
                  "multiInst"       : False,
                  "type"            : "string", # 10 or 26 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # WEP Key 1 expressed as a hexadecimal string.
                  # 10 Bytes for a 40 Bit key
                  # 26 Bytes for a 104 Bit key
                  },                
        "WEPKey2"   : {
                  "resInstID"       : 0,
                  "resID"           : "23",
                  "operation"       : "W",
                  "multiInst"       : False,
                  "type"            : "string", # 10 or 26 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # WEP Key 2 expressed as a hexadecimal string.
                  # 10 Bytes for a 40 Bit key
                  # 26 Bytes for a 104 Bit key
                  },          
        "WEPKey3"   : {
                  "resInstID"       : 0,
                  "resID"           : "24",
                  "operation"       : "W",
                  "multiInst"       : False,
                  "type"            : "string", # 10 or 26 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # WEP Key 3 expressed as a hexadecimal string.
                  # 10 Bytes for a 40 Bit key
                  # 26 Bytes for a 104 Bit key
                  },                                   
        "WEPKey4"   : {
                  "resInstID"       : 0,
                  "resID"           : "25",
                  "operation"       : "W",
                  "multiInst"       : False,
                  "type"            : "string", # 10 or 26 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # WEP Key 4 expressed as a hexadecimal string.
                  # 10 Bytes for a 40 Bit key
                  # 26 Bytes for a 104 Bit key
                  }, 
        "RADIUSServer"   : {
                  "resInstID"       : 0,
                  "resID"           : "26",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "string", # 1 - 125 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # RADIUS Authentication Server Address
                  }, 
        "RADIUSServerPort"   : {
                  "resInstID"       : 0,
                  "resID"           : "27",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # RADIUS Authentication Server Port Number
                  }, 
        "RADIUSSecret"   : {
                  "resInstID"       : 0,
                  "resID"           : "28",
                  "operation"       : "W",
                  "multiInst"       : False,
                  "type"            : "string", # 1 - 256 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # RADIUS Shared Secret
                  }, 
        "WMMSupported"   : {
                  "resInstID"       : 0,
                  "resID"           : "29",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "boolean",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # 0: WMM NOT Supported
                  # 1: WMM Wupported
                  },                                                                                                       
        "WMMEnabled"   : {
                  "resInstID"       : 0,
                  "resID"           : "30",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "boolean",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # 0: Disabled
                  # 1: Enabled
                  },  
        "MACControlEnabled"   : {
                  "resInstID"       : 0,
                  "resID"           : "31",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "boolean",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # 0: Any Client MAC Address accepted
                  # 1: Client MAC address must exist in
                  # MACAddressList
                  },                                      
        "MACAddressList"   : {
                  "resInstID"       : 0,
                  "resID"           : "32",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "string",  # 12 Bytes
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Array of allowed client MAC addresses, in 
                  # hexadecimal form.
                  }, 
        "TotalBytesSent"   : {
                  "resInstID"       : 0,
                  "resID"           : "33",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Total number of bytes sent via this interface
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  }, 
        "TotalBytesReceived"   : {
                  "resInstID"       : 0,
                  "resID"           : "34",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Total number of bytes received via this interface
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },  
        "TotalPacketsSent"   : {
                  "resInstID"       : 0,
                  "resID"           : "35",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Total number of packets sent via this interface
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },                                       
        "TotalPacketsReceived"   : {
                  "resInstID"       : 0,
                  "resID"           : "36",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Total number of packets received via this interface
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },   
        "TransmitErrors"   : {
                  "resInstID"       : 0,
                  "resID"           : "37",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Total number of packets which could not be 
                  # transmitted because of errors.
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },               
        "ReceiveErrors"   : {
                  "resInstID"       : 0,
                  "resID"           : "38",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Total number of packets received with errors 
                  # which prevented those packets from being delivered.
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },       
        "UnicastPacketsSent"   : {
                  "resInstID"       : 0,
                  "resID"           : "39",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Count of Unicast Packets Sent
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },
        "UnicastPacketsReceived"   : {
                  "resInstID"       : 0,
                  "resID"           : "40",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Count of Unicast Packets received
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },          
        "MulticastPacketsSent"   : {
                  "resInstID"       : 0,
                  "resID"           : "41",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Count of Multicast Packets Sent
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },
        "MulticastPacketsReceived"   : {
                  "resInstID"       : 0,
                  "resID"           : "42",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Count of Multicast Packets received
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },   
        "BroadcastPacketsSent"   : {
                  "resInstID"       : 0,
                  "resID"           : "43",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Count of Broadcast Packets Sent
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },
        "BroadcastPacketsReceived"   : {
                  "resInstID"       : 0,
                  "resID"           : "44",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Count of Broadcast Packets received
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },       
        "DiscardPacketsSent"   : {
                  "resInstID"       : 0,
                  "resID"           : "45",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Count of valid outbound packets intentionally discarded 
                  # without transmission, for example a packet may be 
                  # discarded to manage buffer space.
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },
        "DiscardPacketsReceived"   : {
                  "resInstID"       : 0,
                  "resID"           : "46",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Count of valid packets received and intentionally discarded 
                  # without transmission, for example a packet may be 
                  # discarded to manage buffer space.
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },       
        "UnknownPacketsReceived"   : {
                  "resInstID"       : 0,
                  "resID"           : "47",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Count of Unknown Packets Received
                  # Note: standard does not specify "since when".
                  # assume since last reset of interface.
                  },         
        "VendorSpecificExtensions"   : {
                  "resInstID"       : 0,
                  "resID"           : "48",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "objlnk", 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Links to a vendor specific object.
                  }
    }  

# Bearer Selection
#    This object specifies resources to enable a device to choose a 
#    communications bearer on which to connect.
bearer_selection_resources_list={
        # Note for resource ID 0 (PreferredCommunicationsBearer):
        #     (1) Remote management of this communications
        #        bearer via LWM2M is currently not supported.
        #
        # Attention: The spec for this resource (LwM2M 
        # Object -- ConnMgmtCandidate Version 1.0 -- 13 Jan 2015) information is
        # incomplete as it does not define values above 100 (neither
        # to be reserved, vendor-specific, etc).
        "0"   : {"resInstID"        : 0,
                  "resName"         : "PreferredCommunicationsBearer",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "integer", # 8 bit 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Used in network selection:
                  #    0: auto connect
                  #    1: 3GPP PS preferred
                  #    2: 3GPP PS GSM (GPRS) preferred
                  #    3: 3GPP PS UMTS preferred
                  #    4: 3GPP PS LTE preferred
                  #    5: 1xEV-DO preferred (1; see note above)
                  #    6: 3GPP CS preferred (1; see note above)
                  #    7: WLAN preferred
                  #    8: Ethernet preferred (1; see note above)
                  #    9: DSL preferred (1; see note above)
                  #    10: Bluetooth preferred (1; see note above)
                  #    11: WIMAX preferred (1; see note above)
                  #    12-100: Reserved for future use
                  #
                  # The Preferred Communications Bearer resource specifies the preferred 
                  # communications bearer that the LWM2M Client is requested to use for 
                  # connecting to the LWM2M Server. If multiple preferred communications 
                  # bearers are specified, the priority order is reflected by the resource 
                  # instance order. E.g. the bearer which appears first in the list of 
                  # resource instances is to have higher priority over the rest of available 
                  # bearers. The LWM2M Client SHOULD use the preferred bearers with higher 
                  # priority first if they are available. If none of indicated preferred 
                  # bearers is available, the LWM2M Client SHOULD wait until one of them 
                  # becomes available.
                  },
        "1"   : {"resInstID"        : 0,
                  "resName"         : "AcceptableRSSIGSM",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Provides guide to the application when performing 
                  # manual network selection.
                  },       
        "2"   : {"resInstID"        : 0,
                  "resName"         : "AcceptableRSCPUMTS",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Provides guide to the application when performing 
                  # manual network selection.
                  },       
        "3"   : {"resInstID"        : 0,
                  "resName"         : "AcceptableRSRPLTE",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Provides guide to the application when performing 
                  # manual network selection.
                  },    
        "4"   : {"resInstID"        : 0,
                  "resName"         : "AcceptableRSSI1xEVDO",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Provides guide to the application when performing 
                  # manual network selection.
                  },  
        "5"   : {"resInstID"        : 0,
                  "resName"         : "CellLockList",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Comma separated list of allowed Global
                  # Cell Identities.
                  },  
        "6"   : {"resInstID"        : 0,
                  "resName"         : "OperatorList",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Comma separated list of MCC+MNC of
                  # operators, in priority order.
                  # Resource "operator list mode" indicates
                  # how to process this list.
                  },  
        "7"   : {"resInstID"        : 0,
                  "resName"         : "OperatorListMode",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Indicates whether resource "operator list" 
                  # represents the allowed operator list
                  # (white list), or, the preferred operator list.
                  #
                  # 0=preferred
                  # 1=allowed
                  },  
        "8"   : {"resInstID"        : 0,
                  "resName"         : "ListOfAvailablePLMNs",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Allows server to see results of network
                  # scan (e.g. result of AT+COPS=?)
                  },       
        "9"   : {"resInstID"        : 0,
                  "resName"         : "VendorSpecificExtensions",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "objlnk",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Links to a vendor specific object.
                  }                                                      
    }

reverse_bearer_selection_resources_list={
        # Note for resource ID 0 (PreferredCommunicationsBearer):
        #     (1) Remote management of this communications
        #        bearer via LWM2M is currently not supported.
        #
        # Attention: The spec for this resource (LwM2M 
        # Object -- ConnMgmtCandidate Version 1.0 -- 13 Jan 2015) information is
        # incomplete as it does not define values above 100 (neither
        # to be reserved, vendor-specific, etc).
        "PreferredCommunicationsBearer"   : {
                  "resInstID"       : 0,
                  "resID"           : "0",
                  "operation"       : "RW",
                  "multiInst"       : True,
                  "type"            : "integer", # 8 bit 
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Used in network selection:
                  #    0: auto connect
                  #    1: 3GPP PS preferred
                  #    2: 3GPP PS GSM (GPRS) preferred
                  #    3: 3GPP PS UMTS preferred
                  #    4: 3GPP PS LTE preferred
                  #    5: 1xEV-DO preferred (1; see note above)
                  #    6: 3GPP CS preferred (1; see note above)
                  #    7: WLAN preferred
                  #    8: Ethernet preferred (1; see note above)
                  #    9: DSL preferred (1; see note above)
                  #    10: Bluetooth preferred (1; see note above)
                  #    11: WIMAX preferred (1; see note above)
                  #    12-100: Reserved for future use
                  #
                  # The Preferred Communications Bearer resource specifies the preferred 
                  # communications bearer that the LWM2M Client is requested to use for 
                  # connecting to the LWM2M Server. If multiple preferred communications 
                  # bearers are specified, the priority order is reflected by the resource 
                  # instance order. E.g. the bearer which appears first in the list of 
                  # resource instances is to have higher priority over the rest of available 
                  # bearers. The LWM2M Client SHOULD use the preferred bearers with higher 
                  # priority first if they are available. If none of indicated preferred 
                  # bearers is available, the LWM2M Client SHOULD wait until one of them 
                  # becomes available.
                  },
        "AcceptableRSSIGSM"   : {
                  "resInstID"       : 0,
                  "resID"           : "1",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Provides guide to the application when performing 
                  # manual network selection.
                  },       
        "AcceptableRSCPUMTS"   : {
                  "resInstID"       : 0,
                  "resID"           : "2",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Provides guide to the application when performing 
                  # manual network selection.
                  },       
        "AcceptableRSRPLTE"   : {
                  "resInstID"       : 0,
                  "resID"           : "3",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Provides guide to the application when performing 
                  # manual network selection.
                  },    
        "AcceptableRSSI1xEVDO"   : {
                  "resInstID"       : 0,
                  "resID"           : "4",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Provides guide to the application when performing 
                  # manual network selection.
                  },  
        "CellLockList"   : {
                  "resInstID"       : 0,
                  "resID"           : "5",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Comma separated list of allowed Global
                  # Cell Identities.
                  },  
        "OperatorList"   : {
                  "resInstID"       : 0,
                  "resID"           : "6",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Comma separated list of MCC+MNC of
                  # operators, in priority order.
                  # Resource "operator list mode" indicates
                  # how to process this list.
                  },  
        "OperatorListMode"   : {
                  "resInstID"       : 0,
                  "resID"           : "7",
                  "operation"       : "RW",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Indicates whether resource "operator list" 
                  # represents the allowed operator list
                  # (white list), or, the preferred operator list.
                  #
                  # 0=preferred
                  # 1=allowed
                  },  
        "ListOfAvailablePLMNs"   : {
                  "resInstID"       : 0,
                  "resID"           : "8",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "integer",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Allows server to see results of network
                  # scan (e.g. result of AT+COPS=?)
                  },       
        "VendorSpecificExtensions"   : {
                  "resInstID"       : 0,
                  "resID"           : "9",
                  "operation"       : "R",
                  "multiInst"       : False,
                  "type"            : "objlnk",
                  "resUnit"         : "",
                  "resValue"        : "",
                  # Optional resource definition.  
                  # Links to a vendor specific object.
                  }                                                      
    }





#oneM2M device capability
device_capability_resource_list = {
    "0" : {"resInstID" : 0, "multiInst" : False, "resName" : "Property", "type" : "string", "operation" : "R", "resValue" : ""},
    "1" : {"resInstID" : 0, "multiInst" : False, "resName" : "Group", "type" : "string", "operation" : "R", "resValue" : ""},
    "2" : {"resInstID" : 0, "multiInst" : False, "resName" : "Description", "type" : "string", "operation" : "R", "resValue" : ""},
    "3" : {"resInstID" : 0, "multiInst" : False, "resName" : "Attached", "type" : "boolean", "operation" : "R", "resValue" : ""},
    "4" : {"resInstID" : 0, "multiInst" : False, "resName" : "Enabled", "type" : "boolean", "operation" : "R", "resValue" : ""},
    "5" : {"resInstID" : 0, "multiInst" : False, "resName" : "opEnable", "type" : "", "operation" : "E", "resValue" : ""},
    "6" : {"resInstID" : 0, "multiInst" : False, "resName" : "opDisable", "type" : "", "operation" : "E", "resValue" : ""},
    "7" : {"resInstID" : 0, "multiInst" : False, "resName" : "DenyUserEn", "type" : "boolean", "operation" : "", "resValue" : ""},
    "8" : {"resInstID" : 0, "multiInst" : False, "resName" : "NotifyUser", "type" : "boolean", "operation" : "", "resValue" : ""},
}

reverse_device_capability_resource_list = {
    "Property" : {"resInstID" : 0, "multiInst" : False, "resId" : "0", "type" : "string", "operation" : "R", "resValue" : ""},
    "Group" : {"resInstID" : 0, "multiInst" : False, "resId" : "1", "type" : "string", "operation" : "R", "resValue" : ""},
    "Description" : {"resInstID" : 0, "multiInst" : False, "resId" : "2", "type" : "string", "operation" : "R", "resValue" : ""},
    "Attached" : {"resInstID" : 0, "multiInst" : False, "resId" : "3", "type" : "boolean", "operation" : "R", "resValue" : ""},
    "Enabled" : {"resInstID" : 0, "multiInst" : False, "resId" : "4", "type" : "boolean", "operation" : "R", "resValue" : ""},
    "opEnable" : {"resInstID" : 0, "multiInst" : False, "resId" : "5", "type" : "", "operation" : "E", "resValue" : ""},
    "opDisable" : {"resInstID" : 0, "multiInst" : False, "resId" : "6", "type" : "", "operation" : "E", "resValue" : ""},
    "DenyUserEn" : {"resInstID" : 0, "multiInst" : False, "resId" : "7", "type" : "boolean", "operation" : "", "resValue" : ""},
    "NotifyUser" : {"resInstID" : 0, "multiInst" : False, "resId" : "8", "type" : "boolean", "operation" : "", "resValue" : ""},
}

#FOKUS dm object
transport_mgm_resource_list={
    "0": {"resInstID" : 0, "multiInst" : False, "resName": "appidPolicyMapping", "resId" : "0", "type" : "string", "operation" : "RW", "resValue" : ""},
    "1": {"resInstID" : 0, "multiInst" : False, "resName": "IPAddress"  , "resId" : "1", "type" : "string", "operation" : "RW", "resValue" : ""},
    "2": {"resInstID" : 0, "multiInst" : False, "resName": "port"       , "resId" : "2", "type" : "integer", "operation" : "RW", "resValue" : ""},
    "3": {"resInstID" : 0, "multiInst" : False, "resName": "InitProtocol", "resId" : "3", "type" : "string", "operation" : "RW", "resValue" : ""},
    "4": {"resInstID" : 0, "multiInst" : False, "resName": "FinalProtocol", "resId" : "4", "type" : "string", "operation" : "RW", "resValue" : ""}
}

reverse_transport_mgm_resource_list={
    "appidPolicyMapping":  {"resInstID" : 0, "multiInst" : False, "resName": "appidPolicyMapping", "resId" : "0", "type" : "string", "operation" : "RW", "resValue" : ""},
    "IPAddress":    {"resInstID" : 0, "multiInst" : False, "resName": "IPAddress"  , "resId" : "1", "type" : "string", "operation" : "RW", "resValue" : ""},
    "port":         {"resInstID" : 0, "multiInst" : False, "resName": "port"       , "resId" : "2", "type" : "integer", "operation" : "RW", "resValue" : ""},
    "InitProtocol": {"resInstID" : 0, "multiInst" : False, "resName": "InitProtocol", "resId" : "3", "type" : "string", "operation" : "RW", "resValue" : ""},
    "FinalProtocol": {"resInstID" : 0, "multiInst" : False, "resName": "FinalProtocol", "resId" : "4", "type" : "string", "operation" : "RW", "resValue" : ""}
}

configuration_mgmt_list={
    "0": {"resInstID" : 0, "multiInst": False, "resName": "configuration", "resId" : "0", "type" : "string", "operation" : "RW", "resValue" : ""},
    "1": {"resInstID" : 0, "multiInst": False, "resName": "type", "resId" : "1", "type" : "string", "operation" : "R", "resValue" : ""}
}

reverse_configuration_mgmt_list={
    "configuration" : {"resInstID" : 0, "multiInst" : False, "resName": "configuration", "resId": "0", "type": "string", "operation": "RW", "resValue" : ""},
    "type" : {"resInstID" : 0, "multiInst" : False, "resName": "type", "resId": "1", "type": "string", "operation": "R", "resValue" : ""}
}

lwm2m_dict_objects = {
    "0" : {"object_name" : "LWM2MSecurity", "alias" : "LWM2MSecurity", "multiInst" : True, "urn":"urn:oma:lwm2m:oma:0", "resource_list": security_resources_list},
    "1" : {"object_name" : "LWM2MServer", "alias" : "LWM2MServer", "multiInst" : True, "urn":"urn:oma:lwm2m:oma:1", "resource_list" : server_resources_list},
    "2" : {"object_name" : "AccessControl", "alias" : "AccessControl", "multiInst" : True, "urn":"urn:oma:lwm2m:oma:2","resource_list" : access_control_resources_list},
    "3" : {"object_name" : "Device", "alias" : "Device", "multiInst" : False, "urn":"urn:oma:lwm2m:oma:3", "resource_list" : device_resources_list},
    "4" : {"object_name" : "ConnectivityMonitoring", "alias" : "ConnectivityMonitoring", "multiInst" : False, "urn":"urn:oma:lwm2m:oma:4", "resource_list" : connectivity_monitoring_resources_list},
    "5" : {"object_name" : "FirmwareUpdate", "alias" : "FirmwareUpdate", "multiInst" : False, "urn":"urn:oma:lwm2m:oma:5","resource_list" : firmware_update_resources_list},
    "6" : {"object_name" : "Location", "alias" : "Location", "urn":"urn:oma:lwm2m:oma:6", "multiInst" : False, "resource_list" : location_resources_list},
    "7" : {"object_name" : "ConnectivityStatistics", "urn":"urn:oma:lwm2m:oma:7", "alias" : "ConnectivityStatistics", "multiInst" : False, "resource_list" : connectivity_statistics_resources_list},
    "10": {"object_name" : "CellularConnectivity", "alias":"CellularConnectivity", "urn":"urn:oma:lwm2m:oma:10", "resource_list": cellular_connectivity_resources_list},
    "11": {"object_name" : "APNConnectionProfile", "alias":"APNConnectionProfile", "urn":"urn:oma:lwm2m:oma:11", "resource_list": apn_connection_profile_resources_list},
    "12": {"object_name" : "WLANConnectivity", "alias":"WLANConnectivity", "urn":"urn:oma:lwm2m:oma:12", "resource_list": wlan_connectivity_resources_list},
    "13": {"object_name" : "BearerSelection", "alias":"BearerSelection", "urn":"urn:oma:lwm2m:oma:13", "resource_list": bearer_selection_resources_list},
    #from oneM2M Pg.No. 51 http://www.onem2m.org/images/files/deliverables/TS-0005-Management_Enablement_OMA-V-2014-08.pdf
    "4200" : {"object_name" : "DeviceCapability", "alias" : "DeviceCapability", "multiInst" : True, "urn":"urn:oma:lwm2m:ext:4200", "resource_list" : device_capability_resource_list},
    #FOKUS Management Objects
    "4300" : {"object_name" : "TransportMgmtPolicy", "alias" : "TransportManagementPolicy", "multiInst" : False, "urn":"urn:oma:lwm2m:ext:4300", "resource_list" :transport_mgm_resource_list},
    "4400" : {"object_name" : "ConfigurationMgmt", "alias" :"ConfigurationMgmt", "multiInst" : True, "urn" : "urn:oma:lwm2m:ext:4400", "resource_list" : configuration_mgmt_list}
}
        
lwm2m_reverse_dict_objects = {
    "LWM2MSecurity" :           {"object_id" : "0", "alias" : "LWM2MSecurity", "urn":"urn:oma:lwm2m:oma:0", "multiInst" : True,  "resource_list": reverse_security_resources_list},
    "LWM2MServer" :             {"object_id" : "1", "alias" : "LWM2MServer", "urn":"urn:oma:lwm2m:oma:1", "multiInst" : True, "resource_list" : reverse_server_resources_list},
    "AccessControl" :           {"object_id" : "2", "alias" : "AccessControl", "urn":"urn:oma:lwm2m:oma:2", "multiInst" : True, "resource_list" : reverse_access_control_resources_list},
    "Device" :                  {"object_id" : "3", "alias" : "Device", "urn":"urn:oma:lwm2m:oma:3", "multiInst" : False, "resource_list" : reverse_device_resources_list},
    "ConnectivityMonitoring" :  {"object_id" : "4", "alias" : "ConnectivityMonitoring", "urn":"urn:oma:lwm2m:oma:4", "multiInst" : False,  "resource_list" : reverse_connectivity_monitoring_resources_list},
    "FirmwareUpdate" :          {"object_id" : "5", "alias" : "FirmwareUpdate", "urn":"urn:oma:lwm2m:oma:5", "multiInst" : False, "resource_list" : reverse_firmware_update_resources_list},
    "Location" :                {"object_id" : "6", "alias" : "Location", "urn":"urn:oma:lwm2m:oma:6", "multiInst" : False, "resource_list" : reverse_location_resources_list},
    "ConnectivityStatistics" :  {"object_id" : "7", "alias" : "ConnectivityStatistics", "urn":"urn:oma:lwm2m:oma:7", "multiInst" : False, "resource_list" : reverse_connectivity_statistics_resources_list},
    "CellularConnectivity":   {"object_id" : "10", "alias":"CellularConnectivity", "urn":"urn:oma:lwm2m:oma:10", "multiInst" : False, "resource_list": reverse_cellular_connectivity_resources_list},
    "APNConnectionProfile":     {"object_id" : "11", "alias":"APNConnectionProfile", "urn":"urn:oma:lwm2m:oma:11", "multiInst" : False, "resource_list": reverse_apn_connection_profile_resources_list},
    "WLANConnectivity":         {"object_id" : "12", "alias":"WLANConnectivity", "urn":"urn:oma:lwm2m:oma:12", "multiInst" : False, "resource_list": reverse_wlan_connectivity_resources_list},
    "BearerSelection":         {"object_id" : "13", "alias":"BearerSelection", "urn":"urn:oma:lwm2m:oma:13", "multiInst" : False, "resource_list": reverse_bearer_selection_resources_list},
    
    #from oneM2M
    "DeviceCapability" :        {"object_id" : "4200", "alias" : "DeviceCapability", "urn":"urn:oma:lwm2m:ext:4200", "multiInst" : True, "resource_list" : reverse_device_capability_resource_list},
    #FOKUS Management Objects
    "TransportMgmtPolicy": {"object_id" : "4300", "alias" : "TransportMgmtPolicy", "urn":"urn:oma:lwm2m:ext:4300", "multiInst" : False, "resource_list" :reverse_transport_mgm_resource_list},
    "ConfigurationMgmt" : {"object_id" : "4400", "alias" : "ConfigurationMgmt", "urn":"urn:oma:lwm2m:ext:4400", "multiInst": True, "resource_list": reverse_configuration_mgmt_list}
}

from openmtc_scl.Plugin import Plugin
import json
from lwm2m import lwm2m_ClientRegIntf
from gevent.server import DatagramServer
import sys
import os
from subprocess import call
import subprocess
from parserClient import ParseQueryPayload
from MgmtObjClient import ClientCollection
from allClassesClient import DeviceClass

spath = "../openmtc/lib/coap/coapy/coapy"
sys.path.append(os.path.abspath(spath))

import connection
import options
import link
import time
import constants


#Declaring Constants
OBSERVE_OPTION_VALUE_OBSERVATION = 0
OBSERVE_OPTION_VALUE_CANCEL_OBSERVATION = 1
URI_QUERY_VALUE = 15
LOCATION_VALUE = 8
URI_PATH_VALUE = 11
URI_HOST_VALUE = 3
URI_PORT_VALUE = 7

local_lwm2m_client = ClientCollection()
client_request = lwm2m_ClientRegIntf()
pars = ParseQueryPayload()
location_address = ""
lwm2m_server_ip_port = ""
resourceString = None

class DMClient_CoAP_Server(DeviceClass):
    """ Handles and process the CoAP requests for Registration, Discovery, Observation/Notifications and etc """
    
    def __init__(self, api, dm_server_ip, dm_server_port, local_server_ip, local_server_port,
                 local_client_ip, local_client_port):
        super(DMClient_CoAP_Server, self).__init__()
        self.subscription_list = []
        self.sender_info = []
        self.lwm2m_dm_server_ip = dm_server_ip
        self.lwm2m_dm_server_port = dm_server_port
        self.local_server_ip = local_server_ip
        self.local_server_port = local_server_port
        self.local_client_ip = local_client_ip
        self.local_client_port = local_client_port
        #TODO: change datagram server to wrapper of coap server
        self.local_server = DatagramServer((self.local_server_ip, self.local_server_port), self.handle_request)
        self.api = api
    
    def handle_request(self, message, remote):
        rx_record = connection.ReceptionRecord(None, message, remote)
        msg = rx_record.message
        uriQuery = msg.findOption(options.UriQuery)
        self.process(rx_record, remote, uriQuery)
    
    def start_server(self, ):
        print "Local Server Started"
        self.local_server.start()
        
    def stop_server(self, ):
        print "Local Server Stopped"
        self.local_server.stop()
    
    def process(self, rx_record, remote, uriQ):
        """ Processes the POST, PUT and GET requests """
        msg=rx_record.message
        self.uriQuery1 = uriQ
        self.payload = msg.payload
        global resourceString
        if constants.POST == msg.code:
            #Registration Client
            global server_ip_port, location_address

            q = rx_record.message.findOption(URI_QUERY_VALUE)[0].value
            #TODO: check if coap says somthing about execute messages
            if str(q).find("execute") != -1:
                print "entered in client:: execute field"
                self.executeResource(rx_record)
                msg = connection.Message(connection.Message.ACK, code=constants.CHANGED, payload="execution")
                self.local_server.sendto(msg._pack(rx_record.transaction_id), remote)
            else:
                server_ip = self.lwm2m_dm_server_ip
                server_port = self.lwm2m_dm_server_port
                server_ip_port = server_ip + ":" + str(server_port)
                payload = msg.payload
                path = "rd?"
                query = rx_record.message.findOption(URI_QUERY_VALUE)[0].value.strip()
                #Creates objects in the local database
                local_lwm2m_client.create_mgmt_objects(query, payload)
                
                msg = connection.Message(connection.Message.ACK, code=constants.CREATED, payload="Client Registered")
                self.local_server.sendto(msg._pack(rx_record.transaction_id), remote)
                #Registration in the Server
                res_register = client_request.clientRegistration(lwm2m_server_ip_port, path, query, payload, client_port = 5683)

                location_address = res_register.findOption(LOCATION_VALUE)[0].value
                self.storeDiscoverPaths.append({ "path" : "rd", "location" : location_address, "objectID" : None, "objectInstID" : None, "resID" : None})
            
        elif constants.PUT == msg.code:
            check_pmax = 0
            #pmin and pmax imposed from the dm server, upath related to an object
            for val1 in uriQ:
                if str(val1).find("pmax") != -1:
                    check_pmax = 1
            if check_pmax == 1:
               	path = []
                for v in rx_record.message.findOption(URI_PATH_VALUE):
                    path.append(v.value)
                upath = "/".join(path)

        	pmax = str(rx_record.message.findOption(URI_QUERY_VALUE)[0].value).split("=")[1]
        	pmin = str(rx_record.message.findOption(URI_QUERY_VALUE)[1].value).split("=")[1]
                check_pmax = 0
                filtered_resources = self.write_attributes(upath, pmax, pmin)
                
                msg = connection.Message(connection.Message.ACK, code=constants.CHANGED, payload=filtered_resources)
                self.local_server.sendto(msg._pack(rx_record.transaction_id), remote)
            else:
                #TODO: Write: standard exists for writing resources?
                self.resource_update(rx_record, self.uriQuery1, remote)
            
        elif constants.GET == msg.code:
            try:
                observe_value = rx_record.message.findOption(options.Observe).value
            except ValueError:
                observe_value = None #-1
            
            if observe_value == OBSERVE_OPTION_VALUE_OBSERVATION:
                filtered_resources = self.observe_resource(rx_record, self.uriQuery1)
            elif observe_value == OBSERVE_OPTION_VALUE_CANCEL_OBSERVATION:
                filtered_resources = self.cancel_observe_resource(rx_record)
            elif str(rx_record.message.findOption(URI_PATH_VALUE)[0].value).find("rd") != -1:
                filtered_resources = self.handle_discover_request(rx_record)
                
            msg = connection.Message(connection.Message.ACK, code=constants.CONTENT, payload=json.dumps(filtered_resources))
            self.local_server.sendto(msg._pack(rx_record.transaction_id), remote)
    
    def resource_update(self, rx_record, uriQuery1, remote):
        """ Updates the resources in the local database and LWM2M server  """
        
        store_query = []
        for val in self.uriQuery1:
            splitQuery = str(str(val).split(":")[1]).strip()
            store_query.append({"id" : -1,
                                "code" : str(splitQuery).split("=")[0],
                                "value" : str(splitQuery).split("=")[1]})
        split_payload = str(rx_record.message.payload).split("/")

        local_lwm2m_client.update_mgmt_object(split_payload[0], split_payload[1], store_query)        
        payloadForServer = rx_record.message.payload
        
        msg = connection.Message(connection.Message.ACK, code=constants.CHANGED, payload="Resource Updated")
        self.local_server.sendto(msg._pack(rx_record.transaction_id), remote)
        
        # Updates the LWM2M Server
        path = "rd/" + location_address +"?"
        query = str(splitQuery).split("=")[0] + "=" + str(splitQuery).split("=")[1]
        payload = payloadForServer
        client_request.clientUpdate(lwm2m_server_ip_port, query, payload, path=path, client_port=self.local_client_port)

    def myfunc(self,):
        self.p1 = subprocess.Popen(['sh', 'webcamstart.sh', '127.0.0.1', '34000']) #, stdout = subprocess.PIPE)
        self.p1.communicate()
    
    def executeResource(self, rx_record):
        for path_element in rx_record.message.findOption(URI_PATH_VALUE):
            print "client: elements %s" %path_element            
        
        objectID = rx_record.message.findOption(URI_PATH_VALUE)[2].value
        objectInstID = rx_record.message.findOption(URI_PATH_VALUE)[3].value
        resID = rx_record.message.findOption(URI_PATH_VALUE)[4].value
        
        print objectID, objectInstID, resID
        print rx_record.message.payload
        
        storeQuery = []
        storeQuery.append({"id" : int(resID), "code" : "Null", "value" : int(rx_record.message.payload)})
        
        local_lwm2m_client.update_mgmt_object(objectID, objectInstID, storeQuery)
        
        #self.p = subprocess.Popen(['sh', 'webcamstart.sh', '127.0.0.1', '34000'], stdout = subprocess.PIPE)
        #self.api.run_task(self.p.communicate)
        #self.api.run_task(self.myfunc)
        #self.myfunc()
        #print "reached down:: client"
        self.api.run_task(call, ["cheese"])
        #call(["cheese"])

    def handle_discover_request(self, rx_record):
        path = []
        for v in rx_record.message.findOption(URI_PATH_VALUE):
            path.append(v.value)
        pload = str(rx_record.message.payload).split("&")
        app_ip = str(pload[0]).split("=")[1]
        app_port = str(pload[1]).split("=")[1]

        if len(path) == 2:
            filtered_resources = self.discover_resource(app_ip, app_port, endPoint = path[1],
                                                        objectID = None, objectInstID = None, resID = None)
        elif len(path) == 3:
            filtered_resources = self.discover_resource(app_ip, app_port, endPoint = path[1],
                                                        objectID = path[2], objectInstID = None, resID = None)
        elif len(path) == 4:
            filtered_resources = self.discover_resource(app_ip, app_port, endPoint = path[1],
                                                        objectID = path[2], objectInstID = path[3], resID = None)
        elif len(path) == 5:
            filtered_resources = self.discover_resource(app_ip, app_port, endPoint = path[1],
                                                        objectID = path[2], objectInstID = path[3], resID = path[4])
    
        return filtered_resources

    def discover_resource(self, app_ip, app_port, endPoint, objectID=None, objectInstID=None, resID=None):
        total_result = []
        if objectID is None:
            answer = local_lwm2m_client.return_maintain_objects()
            for ans in answer:
                total_result.append({"app_ip" : app_ip, "app_port" : app_port, "endPointName" : endPoint,
                                     "objectID" : ans["objectID"], "objectInstID" : ans["objectInstID"],
                                     "pmax" : ans["pmax"], "pmin" : ans["pmin"]})
        elif objectID != None and objectInstID != None and resID == None:
            answer = local_lwm2m_client.return_resources(objectID, objectInstID)
            for ans in answer:
                total_result.append({"app_ip" : app_ip, "app_port" : app_port, "endPointName" : endPoint,
                                     "objectID" : objectID, "objectInstID" : objectInstID, "pmax" : ans["pmax"],
                                     "pmin" : ans["pmin"], "resID" : ans["resID"], "resValue" : ans["resValue"]})
        return total_result
        
    def observe_resource(self, rx_record, query):
        first_notification = None
        uri_port = rx_record.message.findOption(URI_PORT_VALUE).value
        uri_host = rx_record.message.findOption(URI_HOST_VALUE).value
        s_list = {}
        sender_details = {}
        path = []
        for v in rx_record.message.findOption(URI_PATH_VALUE):
            path.append(v.value)
        pload = str(rx_record.message.payload).split("&")
        app_ip = str(pload[0]).split("=")[1]
        app_port = str(pload[1]).split("=")[1]
        #check if the path includes the object instance id or just the object id
        if len(path) == 3:
            #observation to object id
            path.append("None")
            path.append("None")
        elif len(path) == 4:
            #observation to resource id
            path.append("None")
        
        objectID = path[2]
        objectInstID = path[3]
        resID = path[4]
 
        s_list = {"app_ip" : app_ip, "app_port" : app_port, "objectID" : objectID,
                  "objectInstID" : objectInstID, "resID" : resID}
        sender_details = {"transaction_id" : rx_record.transaction_id, "uri_host" : uri_host, "uri_port" : uri_port}
        #store the new observation
        if len(self.subscription_list) == 0:
            self.subscription_list.append(s_list)
            self.sender_info.append(sender_details) 
            first_notification = local_lwm2m_client.observe_res(self.subscription_list, s_list, self.sender_info)
        else:
            for test in self.subscription_list:
                if test != s_list:
                    self.subscription_list.append(s_list)
                    self.sender_info.append(sender_details) 
                    first_notification = local_lwm2m_client.observe_res(self.subscription_list, s_list, self.sender_info)

        return first_notification
    
    def cancel_observe_resource(self, rx_record):
        counter = 0
        path = []
        for v in rx_record.message.findOption(URI_PATH_VALUE):
            path.append(v.value) 
        pload = str(rx_record.message.payload).split("&")
        app_ip = str(pload[0]).split("=")[1]
        app_port = str(pload[1]).split("=")[1]
        
        if len(path) == 3:
            path.append("None")
            path.append("None")
        elif len(path) == 4:
            path.append("None")
        
        objectID = path[2]
        objectInstID = path[3]
        resID = path[4]
        
        try:
            for val in self.subscription_list:
                if val["app_ip"] == app_ip and val["app_port"] == app_port and val["objectID"] == objectID:
                    self.subscription_list.remove({"app_ip" : app_ip, "app_port" : app_port,
                                                   "objectID" : objectID, "objectInstID" : objectInstID, "resID" : resID})
                    self.sender_info.pop(counter)
                counter += 1
            local_lwm2m_client.cancel_obs_res(objectID, self.subscription_list)
        except:
            print "The Object ID %s is not present" %objectID
        
        return "Unsubscribed Successful"
        
    def write_attributes(self, upath, pmax, pmin):
        splitPath = str(upath).split("/")
        create_str = []
        create_str.append({"attCode" : "pmax", "attValue" : pmax})
        create_str.append({"attCode" : "pmin", "attValue" : pmin})
        return local_lwm2m_client.write_attr(create_str, splitPath[2])
            
class lwm2m_Client(Plugin):
    def _init(self):
        self.run = True
        self._initialized()
    
    def setting_address(self, ):
        """ Reads the configuration file to set LWM2M Server and Client Address(ip:port)
        and other few parameters/resources.
        """
        
        self.lwm2m_server_ip = self.config["lwm2m_dm_server_ip"]
        self.lwm2m_server_port = self.config["lwm2m_dm_server_port"]
        self.local_server_ip = self.config["local_server_ip"]
        self.local_server_port = self.config["local_server_port"]
        self.local_client_ip = self.config["local_client_ip"]
        self.local_client_port = self.config["local_client_port"]
        self.endpoint_name = self.config["endpoint_name"]
        self.objects = self.config["objects"]

    def registration(self, ):
        """ Registers the LWM2M Client in the local database and in the LWM2M server """
        
        print "Starting of Registration"
        global lwm2m_server_ip_port, location_address
        
        self.path = "rd?"
        self.query = ''.join(["ep=", self.endpoint_name, "&local_server_ip=", self.local_server_ip,
                              "&local_server_port=", str(self.local_server_port)])
        self.payload = self.objects
        lwm2m_server_ip_port = self.lwm2m_server_ip + ":" + str(self.lwm2m_server_port)
        
        #Registers in the local database
        local_lwm2m_client.create_mgmt_objects(self.query, self.payload)
        
        #Registers in the server database
        server_response = client_request.clientRegistration(lwm2m_server_ip_port, self.path, self.query,
                                                            self.payload, client_port = self.local_client_port)
        
        print "Registration Response:  %s" %server_response
        
        #Returns the location of the client in the server. Option '8' is the Location.
        location_address = server_response.findOption(LOCATION_VALUE)[0].value 
        
    def loc_server(self, ):
        """ Creates and executes a local server """
        self.l_server = DMClient_CoAP_Server(self.api, self.lwm2m_server_ip, self.lwm2m_server_port,
                                             self.local_server_ip, self.local_server_port,
                                             self.local_client_ip, self.local_client_port)
        self.l_server.start_server()
        
    def _start(self):
        self.api.run_task(self.loc_server)   
        self.setting_address()
        self.registration()
                
        self._started()

    def _stop(self):
        self.l_server.stop_server()
        self._stopped()

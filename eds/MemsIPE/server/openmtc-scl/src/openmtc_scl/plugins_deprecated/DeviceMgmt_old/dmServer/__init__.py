import sys
from openmtc_server.Plugin import Plugin
import os
import subprocess
spath = "../openmtc/lib/coap/coapy/coapy"
sys.path.append(os.path.abspath(spath))
from coap import connection
from coap import options
from coap import link
from coap import constants
import json
import time
import socket
from gevent.server import DatagramServer
import random
import string
from lwm2m import lwm2m_ClientRegIntf
import threading
from parserServer import ParseQueryPayload
from MgmtObjServer import ClientCollection


# Constants
OBSERVE_OPTION_VALUE_OBSERVATION = 0
OBSERVE_OPTION_VALUE_CANCEL_OBSERVATION = 1

URI_QUERY_VALUE = 15
LOCATION_VALUE = 8
URI_PATH_VALUE = 11
URI_HOST_VALUE = 3
URI_PORT_VALUE = 7

pars = ParseQueryPayload()
client_request = lwm2m_ClientRegIntf()
maintain_clients = []
    #dmServer
class dmServer(Plugin):
    count_client = 0  
    discover_client_paths = []
    
    def _init(self):
        self._initialized()

    def _start(self):
        self.start_observation_nscl = False
        self.total_clients = {}
        self.setting_address()
        self.server = DatagramServer((self.lwm2m_dm_server_ip, self.lwm2m_dm_server_port), self.handle_request)
        self.start_server()

        self._started()

    def _stop(self):
        self.stop_server()
        self._stopped()
    
    def setting_address(self, ):
        self.lwm2m_dm_server_ip = self.config["lwm2m_dm_server_ip"]
        self.lwm2m_dm_server_port = self.config["lwm2m_dm_server_port"]
        self.client_ip = self.config["client_ip"]
        self.client_port = self.config["client_port"]
        self.nscl_dm_adapter_listener_ip = self.config["nscl_dm_adapter_listener_ip"]
        self.nscl_dm_adapter_listener_port = self.config["nscl_dm_adapter_listener_port"]
        self.nscl_dm_adapter_client_ip = self.config["nscl_dm_adapter_client_ip"]
        self.nscl_dm_adapter_client_port = self.config["nscl_dm_adapter_client_port"]

    def handle_request(self, message, remote):
        rx_record = connection.ReceptionRecord(None, message, remote)
        msg = rx_record.message
        uriQuery = msg.findOption(options.UriQuery)
        self.process(rx_record, remote, uriQuery)
    
    def start_server(self, ):
        print "LWM2M Server Started"
        self.server.start()
        
    def stop_server(self, ):
        print "LWM2M Server Stopped"
        self.server.stop()
    
    def process(self, rx_record, remote, uriQ):
        position_client = 0
        msg=rx_record.message
        self.uriQuery1 = uriQ
        payload_type = False
        if msg.transaction_type == connection.Message.CON:
            if constants.POST == msg.code:
                check_for_execute = 0
                for val1 in uriQ:
                    if str(val1).find("execute") != -1:
                        check_for_execute = 1
    
                if check_for_execute == 1:
                    check_for_execute = 0
                    msg = connection.Message(connection.Message.ACK, code=constants.CREATED)
                    self.server.sendto(msg._pack(rx_record.transaction_id), remote)
                    self.execute_resource(rx_record)
                else:
                    notify_list = self.client_registration(rx_record, msg, payload_type, remote)
                    self.send_notifications_nscl_adapter(notify_list)

            elif constants.PUT == msg.code:
                check_pmax = 0
                try:
                    for val1 in uriQ:
                        if str(val1).find("pmax") != -1:
                            check_pmax = 1
                except:
                    pass
    
                if check_pmax == 1:
                    self.write_attributes(rx_record)
                    check_pmax = 0
                else:
                    pars.parse_uri_query(self.uriQuery1)
                    pars.parse_payload(str(msg.payload), payload_type)

                    location_address = str(str(msg.options[1]).split(":")[1]).strip()
    
                    for val1 in maintain_clients:
                        if (val1["client_ip"] == rx_record.remote[0] and val1["client_port"] == rx_record.remote[1]) or val1["location"] == location_address:
                            position_client = val1["client_id"]
                            endpoint_name = val1["endPointName"]
                            notify_list = self.total_clients[position_client].update_mgmt_object(pars.return_parse_uri_query(), pars.return_parse_payload(), endpoint_name, self.start_observation_nscl) #mayn't be about creating objects:: so can be calling another function
    
                            if self.start_observation_nscl:
                                self.send_notifications_nscl_adapter(notify_list)
                            break

                msg = connection.Message(connection.Message.ACK, code=constants.CHANGED, payload="Changed")
                self.server.sendto(msg._pack(rx_record.transaction_id), remote)

            elif constants.DELETE == msg.code:
                self.__storage = ""
                print 'Deleting value: %s' % (self.__storage,)
    
                msg = connection.Message(connection.Message.ACK, code=constants.DELETED, payload='Deleting value: %s' % (self.__storage,))
                #sendto line msising

            elif constants.GET == msg.code:
                try:
                    observe_value = rx_record.message.findOption(options.Observe).value
                except ValueError:
                    observe_value = None #-1
                if observe_value == OBSERVE_OPTION_VALUE_OBSERVATION:
                    if rx_record.remote[0] == self.nscl_dm_adapter_client_ip and rx_record.remote[1] == self.nscl_dm_adapter_client_port:
                        for v in rx_record.message.findOption(URI_PATH_VALUE):
                            self.start_observation_nscl = True
			    self.msg_transaction_id = rx_record.transaction_id
			    self.msg_uri_port = rx_record.message.findOption(URI_PORT_VALUE).value
			    self.msg_uri_host = rx_record.message.findOption(URI_HOST_VALUE).value
                    else:
                        self.resource_observation(rx_record)
                elif observe_value == OBSERVE_OPTION_VALUE_CANCEL_OBSERVATION:
                    self.cancel_observation(rx_record)
                elif str(rx_record.message.findOption(URI_PATH_VALUE)[0].value).find(".well-known") != -1:
                    print "Discovered Clients .."
                    for val4 in dmServer.discover_client_paths:
                        print ''.join(["/" , val4["path"] , "/" , val4["endPointName"]])
                elif str(rx_record.message.findOption(URI_PATH_VALUE)[0].value).find("rd") != -1:
                    self.resource_discovery(rx_record)
                
                msg = connection.Message(connection.Message.ACK, code=constants.CONTENT, payload="Request Received")
                self.server.sendto(msg._pack(rx_record.transaction_id), remote)
        elif msg.transaction_type == connection.Message.ACK:
            self.notifications_display(msg.payload)

    def myfunc(self, ):
        self.p = subprocess.Popen(['sh', 'recv_mp4v.sh', '34000']) #, stdout=subprocess.PIPE)
        self.p.communicate()
    
    def execute_resource(self, rx_record):
        path = []
        upath = ""
        i = 0
        for v in rx_record.message.findOption(11):
            print "inside execute : server:: %s" %v
            path.append(str(rx_record.message.findOption(URI_PATH_VALUE)[i].value))
            upath += path[i] + "/"
            i += 1
        upath = upath[:len(upath)-1]

        for val2 in maintain_clients:
            if val2["location"] == path[1]:
                c_server_ip = val2["serverIPInClient"]
                c_server_port = val2["serverPortInClient"]
                break
        
        c_server_ip_port = str(c_server_ip) + ":" + str(c_server_port)
        #self.p.communicate()
        print "reached down :: after runtask"
        client_request.executeResource(c_server_ip_port, rx_record.message.payload, path = upath, client_port=self.client_port)
        print "after executeresource:: server"
        #self.p = subprocess.Popen(['sh', 'recv_mp4v.sh', '34000'], stdout=subprocess.PIPE)
        #self.api.run_task(self.p.communicate)
        #self.api.run_task(self.myfunc)  ###
        #self.myfunc()
        print "reached last ..."
    
    def client_registration(self, rx_record, msg, payload_type, remote):
	temp = []
	endpoint_name = rx_record.message.findOption(URI_QUERY_VALUE)[0].value.split("=")[1]
	server_ip_in_client = rx_record.message.findOption(URI_QUERY_VALUE)[1].value.split("=")[1]  #option 15 is for UriQuery
	server_port_in_client = rx_record.message.findOption(URI_QUERY_VALUE)[2].value.split("=")[1]

	temp.append(self.uriQuery1[0])
	self.uriQuery1 = temp

	pars.parse_uri_query(self.uriQuery1)
	pars.parse_payload(str(msg.payload), payload_type)
	pars.return_parse_payload()

	locationAddr = self.locID_generator(10)
	info_dict = {"client_ip" : rx_record.remote[0], "client_port" : rx_record.remote[1], "serverIPInClient" : server_ip_in_client,
		     "serverPortInClient" : server_port_in_client, "client_id" : dmServer.count_client,
		     "location" : locationAddr, "endPointName" : endpoint_name}

	dmServer.discover_client_paths.append({"path" : "rd", "location" : locationAddr,
					       "endPointName": endpoint_name, "objectID" : None,
					       "objectInstID" : None, "resID" : None})

	maintain_clients.append(info_dict)
	position_client = dmServer.count_client
	self.total_clients[position_client] = ClientCollection()

	dmServer.count_client += 1

	msg = connection.Message(connection.Message.ACK, code=constants.CREATED, location=locationAddr)
	self.server.sendto(msg._pack(rx_record.transaction_id), remote)

        return self.total_clients[position_client].create_mgmt_objects(pars.return_parse_uri_query(), pars.return_parse_payload(), endpoint_name, self.start_observation_nscl)
    
    def send_notifications_nscl_adapter(self, notify_list):
	if self.start_observation_nscl:
	    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	    msg_notify = connection.Message(connection.Message.ACK, code=constants.CONTENT, payload=json.dumps(notify_list))
	    sock.sendto(msg_notify._pack(self.msg_transaction_id), (self.msg_uri_host, int(self.msg_uri_port)))
	    sock.close()

    
    def notifications_display(self, notifications):
        print "NOTIFICATIONS ..."
        storeNotification = json.loads(notifications)
        for val2 in storeNotification:
            print "App. IP : %s, App. Port: %s, ObjectID : %s, Instance ID : %s, Resource Name : %s, Resource Value : %s" %(val2["app_ip"], val2["app_port"], val2["objectID"], val2["objectInstID"], val2["resName"], val2["resValue"])
    
        # Send to the app's ip (and port)
    def resource_discovery(self, rx_record):
        app_ip = rx_record.remote[0]
        app_port = rx_record.remote[1]
        path = []
        upath = ""
        for v in rx_record.message.findOption(URI_PATH_VALUE):
            path.append(v.value)
        upath = "/".join(path)
        for val2 in maintain_clients:
                if val2["endPointName"] == path[1] or val2["location"] == path[1]:
                    c_server_ip = val2["serverIPInClient"]
                    c_server_port = val2["serverPortInClient"]
                    count_val = val2["client_id"]
                    break
        c_server_ip_port = str(c_server_ip) + ":" + str(c_server_port)
        payload = ''.join(["app_ip=" , str(app_ip) , "&app_port=" , str(app_port)])
        discoveredResources = client_request.discoverResource(c_server_ip_port, path=upath, payload=payload, client_port=self.client_port)
    
        print "Discovered Resources .."
        for val3 in json.loads(discoveredResources.payload): #it contains requesting application ip and port :: val3["app_ip"] and val3["app_port"]
            if val3.has_key("resID"):
                print ''.join(["/rd/" , val3["endPointName"] , "/" , val3["objectID"] , "/" , val3["objectInstID"] , "/" , str(val3["resID"]) , " ; pmax : " , str(val3["pmax"]) , " , pmin : " , str(val3["pmin"]) , " , value : " , str(val3["resValue"])])
            else:
                print ''.join(["/rd/" , val3["endPointName"] , "/" , val3["objectID"] , "/" , val3["objectInstID"] , " ; pmax :" , str(val3["pmax"]) , " , pmin : " , str(val3["pmin"])])
         
    def resource_observation(self, rx_record):
        print "OBSERVATION STARTED .."

        self.observeCollection = []
        tempObserve = {}

        app_ip = rx_record.remote[0]
        app_port = rx_record.remote[1]
        #move below two lines in the init
        path = []
        for v in rx_record.message.findOption(URI_PATH_VALUE):
            path.append(v.value)
        upath = "/".join(path)

        if len(path) == 3:
            path.append("None")
            path.append("None")
        elif len(path) == 4:
            path.append("None")             #here client means app ip and port

        self.observeCollection.append({"clientIP" : app_ip, "clientPort" : app_port, "endPointName" : path[1], "objectID" : path[2], "objectInstID" : path[3], "resID" : path[4]})
        tempPayload = "clientIP=" + str(app_ip) + "&clientPort=" + str(app_port)

        for val2 in maintain_clients:
            if val2["endPointName"] == path[1] or val2["location"] == path[1]:
                c_server_ip = val2["serverIPInClient"]
                c_server_port = val2["serverPortInClient"]
                break
        
        c_server_ip_port = str(c_server_ip) + ":" + str(c_server_port)
        first_notification = client_request.observeResource(c_server_ip_port, path=upath, payload=tempPayload,
                                       uri_host=self.lwm2m_dm_server_ip, uri_port=self.lwm2m_dm_server_port,
                                       client_port=self.client_port)
        if first_notification.payload != "null":
            self.notifications_display(first_notification.payload)
        else:
            print "Already Exists"


    def cancel_observation(self,rx_record):
        print "CANCEL OBSERVATION .."
        app_ip = rx_record.remote[0]
        app_port = rx_record.remote[1]
        path = []
        for v in rx_record.message.findOption(URI_PATH_VALUE):
            path.append(str(rx_record.message.findOption(URI_PATH_VALUE)[i].value))
        upath = "/".join(path)
        tempObserve = {}

        if len(path) == 3:
            path.append("None")
            path.append("None")
        elif len(path) == 4:
            path.append("None")             #here client means app ip and port
        tempCancelObs = "clientIP=" + str(app_ip) + "&clientPort=" + str(app_port)

        for val2 in maintain_clients:
            if val2["endPointName"] == path[1] or val2["location"] == path[1]:
                c_server_ip = val2["serverIPInClient"]
                c_server_port = val2["serverPortInClient"]
                break

        c_server_ip_port = str(c_server_ip) + ":" + str(c_server_port)
        client_request.cancelSubscription(c_server_ip_port, path=upath, payload=tempCancelObs, client_port=self.client_port)
        
    def write_attributes(self, rx_record):
        path = []
        for v in rx_record.message.findOption(URI_PATH_VALUE):
            path.append(v.value)
        upath = "/".join(path)

        pmax = rx_record.message.findOption(URI_QUERY_VALUE)[0].value.split("=")[1]
        pmin = rx_record.message.findOption(URI_QUERY_VALUE)[1].value.split("=")[1]

        for val2 in maintain_clients:
            if val2["endPointName"] == path[1] or val2["location"] == path[1]:
                c_server_ip = val2["serverIPInClient"]
                c_server_port = val2["serverPortInClient"]
                break
        
        c_server_ip_port = str(c_server_ip) + ":" + str(c_server_port)
        
        query = ''.join(["pmax=", str(pmax), "&pmin=", str(pmin)])
        reply = client_request.writeAttributes(c_server_ip_port, query, path=upath, client_port=self.client_port)

        print reply
        #update pmax and pmin in server too 
        
    def locID_generator(self, str_size, chars=string.ascii_uppercase + string.digits):
        return ''.join([random.choice(chars) for _ in range(str_size)])

    

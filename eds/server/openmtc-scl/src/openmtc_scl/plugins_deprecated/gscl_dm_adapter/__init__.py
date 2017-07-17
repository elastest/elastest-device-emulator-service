#DM Adapter (GSCL side)

from openmtc.model import Application, Scl, Subscription
from openmtc_server.Plugin import Plugin
from gevent.wsgi import WSGIServer
from openmtc_scl.platform.gevent.ServerRack import GEventServerRack
import json
from time import sleep
from openmtc.scl import CreateRequestIndication, RetrieveRequestIndication
from openmtc.client.http import XIXClient
from base64 import b64decode
import sys, os
from lwm2m import lwm2m_ClientRegIntf
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

#spath = "../openmtc-app/src"
#sys.path.append(os.path.abspath(spath))

#from openmtc_app import DA, ContentSubscription



server_ip_port = "localhost:5688" #Server running in the Client
class DictStorage(object): 
    def initiateDevRes(self, ):
        obj_id = 3    # later take these parameters as arguments
        obj_inst_id = 0
        self.storeDeviceParams = [
            {"objID" : obj_id, "objInstID" : obj_inst_id, "resID" : 0, "resCode": "manu", "resValue" : ""},
            {"objID" : obj_id, "objInstID" : obj_inst_id, "resID" : 1, "resCode" : "mnum", "resValue" : ""},
            {"objID" : obj_id, "objInstID" : obj_inst_id, "resID" : 2, "resCode" : "snum", "resValue" : ""},
            {"objID" : obj_id, "objInstID" : obj_inst_id, "resID" : 3, "resCode" : "lwm2m", "resValue" : ""},
            {"objID" : obj_id, "objInstID" : obj_inst_id, "resID" : 4, "resCode" : "reboot", "resValue" : ""},
            {"objID" : obj_id, "objInstID" : obj_inst_id, "resID" : 5, "resCode" : "facreset", "resValue" : ""},
            {"objID" : obj_id, "objInstID" : obj_inst_id, "resID" : 6, "resCode" : "aposo", "resValue" : ""},
            {"objID" : obj_id, "objInstID" : obj_inst_id, "resID" : 7, "resCode" : "posovo", "resValue" : ""},
            {"objID" : obj_id, "objInstID" : obj_inst_id, "resID" : 8, "resCode" : "posocu", "resValue" : ""},
            {"objID" : obj_id, "objInstID" : obj_inst_id, "resID" : 9, "resCode" : "batlev", "resValue" : ""},
            {"objID" : obj_id, "objInstID" : obj_inst_id, "resID" : 10, "resCode" : "memfre", "resValue" : ""},
            {"objID" : obj_id, "objInstID" : obj_inst_id, "resID" : 11, "resCode" : "errcod", "resValue" : ""},
            {"objID" : obj_id, "objInstID" : obj_inst_id, "resID" : 12, "resCode" : "reerco", "resValue" : ""},
            {"objID" : obj_id, "objInstID" : obj_inst_id, "resID" : 13, "resCode" : "cutim", "resValue" : ""},
            {"objID" : obj_id, "objInstID" : obj_inst_id, "resID" : 14, "resCode" : "utcof", "resValue" : ""},
            {"objID" : obj_id, "objInstID" : obj_inst_id, "resID" : 15, "resCode" : "timz",  "resValue" : ""},
            {"objID" : obj_id, "objInstID" : obj_inst_id, "resID" : 16, "resCode" : "b", "resValue" : ""},
            {"objID" : obj_id, "objInstID" : obj_inst_id, "resID" : 17, "resCode" : "ep", "resValue" : ""},  #
            {"objID" : obj_id, "objInstID" : obj_inst_id, "resID" : 18, "resCode" : "lt", "resValue" : ""}
                        
        ]
    


class gscl_dm_adapter(Plugin, DictStorage):
    def _init(self,):
        self._initialized()
   
    def runHTTPServer(self, ):

        port = 33333
        server_address = ('', port)
        print "Listening on port", port
    
        httpd = HTTPServer(server_address, Handler)
        try:
            httpd.serve_forever()
        except (KeyboardInterrupt, SystemExit):
            pass
    
        print "Exiting"
    
    
    def initialUpdates(self, ):
        sleep(6)
        self.requestUpdate = lwm2m_ClientRegIntf()
        path = "/m2m/scls/gscl/applications"
        request1 = RetrieveRequestIndication(path) #%"http://localhost:5001/m2m/applications/da_app/containers/container1/contentInstances")
        y1 = self.client.send_request_indication(request1)
        
        for val in y1.resource.applicationCollection:
            val1 = val.path 
    
            req1 = RetrieveRequestIndication(val1  + "/containers")
            y2 = self.client.send_request_indication(req1)
    
            for val in y2.resource.containerCollection:
                print "VAL of containers %s" %val.path
                print "ID of the container %s " %val.id #to c
                
                req2 = RetrieveRequestIndication(val.path + "/contentInstances")
                y3 = self.client.send_request_indication(req2)
                
                req3 = RetrieveRequestIndication(y3.resource.latest.path)
                y4 = self.client.send_request_indication(req3)
                
                y5 = y4.resource.content["$t"]
                y6 = json.loads(b64decode(y5))
                
                for val in self.storeDeviceParams:
                    if val["resCode"] == y6["code"]:
                        #print "The resource is %s/%s/%s" %(val["objID"], val["objInstID"], val["resID"])
                        resource_path = "%s/%s/%s" %(val["objID"], val["objInstID"], val["resID"])
                        final_value = "value=" + str(y6["value"])
                        #send a post request here to the server (created in the client) for updating  at port 5688
                        answer = self.requestUpdate.clientUpdateFromGSCL(server_ip_port, "rd?", final_value, resource_path)
                        print "Server Answers :: %s" %answer
    
    def createSubscription(self, ):
        
        sleep(15)
        
        print "Entered the test function of dm adapter"
        
        listSubscriptions = str(self.config["subscriptions"]).split(",")
        
        path = "/m2m/scls/gscl/applications/"
        
        request1 = RetrieveRequestIndication(path) #%"http://localhost:5001/m2m/applications/da_app/containers/container1/contentInstances")
    #try:
        y1 = self.client.send_request_indication(request1)
    #except:
        #print "ERROR"
        
        for val in y1.resource.applicationCollection:
            val1 = val.path 
    
            req1 = RetrieveRequestIndication(val1  + "/containers")
            y2 = self.client.send_request_indication(req1)
            
        
            for val in y2.resource.containerCollection:
                print "VAL of containers %s" %val.path
                print "ID of the container %s " %val.id #to check if the subscription is reqd.
                for valsub in listSubscriptions:
                    if val.id == str(valsub).strip(): #"BatteryLevel":        #control mechanism to subscribe for only a particular resource.
                        path = val.path + "/contentInstances/subscriptions"
                        
                        req2 = CreateRequestIndication(path, resource = Subscription(contact = "http://localhost:33333"))
                        
                        y3 = self.client.send_request_indication(req2)
            
                   
    def _start(self,):
        print "entered start adapter func >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>."
        self.client = XIXClient("http://localhost:5001")
        self.initiateDevRes()
        self.api.run_task(self.runHTTPServer)
        self.initialUpdates()
        self.createSubscription()
        
    def _stop(self, ):
        print "Entered stop func"
        

class Handler(BaseHTTPRequestHandler, DictStorage):
    
    #dont use __init__(self) function.. something goes wrong..dont know what, how
    def do_GET(self):
        self.client = XIXClient("http://localhost:5001")
        self.requestUpdate = lwm2m_ClientRegIntf()
        self.initiateDevRes()
       
        try:
            l = int(self.headers["Content-Length"])
        except KeyError:
            print "<no content>"
        else:
            msg_notify = self.decode_notify(self.rfile.read(l))
            print "NOTIFICATION %s" %msg_notify
            
            msg_notify1 = json.loads(msg_notify)

            for val in msg_notify1:
                
                path = msg_notify1["contentInstances"]["latest"]["$t"]
                #print "path %s" %path
                request = RetrieveRequestIndication(str(path).strip())
                answer = self.client.send_request_indication(request)
                #
                decoded_dict = json.loads(b64decode(answer.resource.content["$t"]))
                
                for val in self.storeDeviceParams:
                    if val["resCode"] == decoded_dict["code"]:
                        print "The resource is %s/%s/%s" %(val["objID"], val["objInstID"], val["resID"])
                        resource_path = "%s/%s/%s" %(val["objID"], val["objInstID"], val["resID"])
                        final_value = "value=" + str(decoded_dict["value"])
                        #send a post request here to the server (created in the client) for updating  at port 5688
                        answer = self.requestUpdate.clientUpdateFromGSCL(server_ip_port, "rd?", final_value, resource_path)
                        print "Server Answers :: %s" %answer

        self.send_response(204, "OK")
        
    def decode_notify(self, msg):
        notify_dict = json.loads(msg)
        retrieve_encoded  = notify_dict["notify"]["representation"]["$t"]
        return b64decode(retrieve_encoded)
    
    do_POST = do_PUT = do_DELETE = do_GET
    

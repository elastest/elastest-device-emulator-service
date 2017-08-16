from futile.logging import LoggerMixin
from openmtc_server.Plugin import Plugin
from base64 import b64decode, b64encode
from json import loads, dumps
from time import sleep
from threading import Thread
from openmtc_etsi.model import Scl, MgmtObj, AttachedDevice, ContentInstance, Application, Container
from openmtc_etsi.scl import CreateRequestIndication, RetrieveRequestIndication, UpdateRequestIndication
from futile.logging import LoggerMixin

APP_ID = "device_emulator"
CONTAINER_ID = "configuration"
CONTENT_INST_ID = "device_info"
NO_OF_DEVICES = 1000
INTERVAL = 3
DATA_SIZE = 200
DESTINATION_PATH = "http://localhost:24000/m2m/applications/ScalableDynamicApp/containers/ImportantData/contentInstances/"

class config_mgmt_app(LoggerMixin):
    
    def __init__(self, api):
         self.api = api
    
    def _start(self, ):
        self.create_application()
        
    def create_application(self, ):
        path = "/m2m/applications"
        app_object = Application(path=path, appId=APP_ID)
        request = CreateRequestIndication(path=path, resource=app_object)
        response = self.api.handle_request_indication(request)
        response.then(self.create_container)
    
    def create_container(self, result):
        path = result.resource.path + "/containers"
        container_object = Container(path=path, id=CONTAINER_ID)
        request = CreateRequestIndication(path=path, resource=container_object)
        response = self.api.handle_request_indication(request)
        #response.then(self.create_contentInstances) # Content Instance Create is disabled now
        
    def create_contentInstances(self, result):
        content = {"traffic_group" : {"nb_devices" : NO_OF_DEVICES,
                                      "interval" : INTERVAL,
                                      "data_size" : DATA_SIZE},
                   "destination_path" : DESTINATION_PATH }
        ci = ContentInstance(id=CONTENT_INST_ID,
            content={
                "contentType": "application/json",
                "$t": b64encode(dumps(content))
            })
    
        path = result.resource.path + "/contentInstances"
        
        request = CreateRequestIndication(path=path, resource=ci, content_type="application/json")
        response = self.api.handle_request_indication(request)

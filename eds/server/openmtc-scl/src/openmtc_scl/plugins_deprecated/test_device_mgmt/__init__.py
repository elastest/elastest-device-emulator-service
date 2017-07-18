from openmtc_server.Plugin import Plugin
from openmtc.scl import RetrieveRequestIndication, CreateRequestIndication,\
    DeleteRequestIndication
from openmtc.response import CreateResponseConfirmation, RetrieveResponseConfirmation, UpdateResponseConfirmation, DeleteResponseConfirmation, SuccessResponseConfirmation, ErrorResponseConfirmation



class TestDA:
    
    def _init(self):
        #self.api.register_transport_client(("intent", "intent"), self.send_request_indication)
        
        self._initialized()
        
    def _start(self):
        self.logger.info("starting the Test DA")
        
        #registering the DA
        req = CreateRequestIndication(path="/m2m/applications", 
                                      resource="{ “application”: {“appId”: “TestDA”, “searchStrings”:{“searchString”:[“MngtDevice”]}}}",
                                      content_type="application/json"
                                      )
        self.api.handle_request_indication(req)
        
        #creating mngmt Obj for Device Battery Level the DA
        req = CreateRequestIndication(path="/m2m/applications/TestDA/mgmtObjs/",
                                      resource="",
                                      content_type="" 
                                      )
        self.api.handle_request_indication(req)
        
from openmtc_server.Plugin import Plugin
from openmtc_etsi.scl import CreateRequestIndication, DeleteRequestIndication, RetrieveRequestIndication
from openmtc_etsi.model import Subcontainers, Container
from json import dumps, loads

class EmulatedDevices(Plugin):
    def _init(self):
        self.config_parameters()
        self._initialized()
    
    def config_parameters(self, ):
        self.emulated_devices_number = self.config.get("emulated_device_num")
        self.app_name = self.config["app_nam"]
        self.container_name_list = self.config["container_name_list"]
        self.subcontainer_name = self.config["subcontainer_name"]
        self.sub_subcontainer_name_list = self.config["sub_subcontainer_name_list"]
    
    
    def create_subcontainer(self, subcontainer_id, path, search_strings, contentType):
        
        subcontainer_object = Container(id=subcontainer_id,
                                        searchStrings=search_strings) 
        req_indication = CreateRequestIndication(path = path,
                                                resource = subcontainer_object, #"{\"container\":{\"id\":\""+sub_subcontainer_id+"\"}}",
                                                content_type = contentType)
        
        result = self.api.handle_request_indication(req_indication)
        
    
    
    def devices_list(self, result):
        path = result.resource.path + "/subcontainers"
        
        for i in range(0, self.emulated_devices_number, 1):
            subcontainer_id = self.subcontainer_name + "_" + str(i)
            search_strings = [';rt="thing"'];
            contentType = "application/json"
            result = self.create_subcontainer(subcontainer_id, path, search_strings, contentType)
            
            sub_subcontainer_id = self.sub_subcontainer_name_list[0]
            path_subcontainer = path + "/" + subcontainer_id + "/subcontainers"
            search_strings = [';ct=50']
            contentType = "application/json"
            self.create_subcontainer(sub_subcontainer_id, path_subcontainer, search_strings, contentType)
            
            sub_subcontainer_id = self.sub_subcontainer_name_list[1]
            path_subcontainer = path + "/" + subcontainer_id + "/subcontainers"
            search_strings = [';rt="unique-text"']
            contentType = "application/json"
            self.create_subcontainer(sub_subcontainer_id, path_subcontainer, search_strings, contentType)
            
           
    def retrieve_path(self, ):
        
        def error_handle(result):
            self.logger.error("The path doesn't exist")
            
            
        path = "/m2m/applications/" + self.app_name + "/containers/" + self.container_name_list[0]
        request = RetrieveRequestIndication(path)
        response = self.api.handle_request_indication(request)
        
        response.then(self.devices_list, error_handle)
        
        
    
    def deregister_app(self):
        try:
            req_indication = DeleteRequestIndication(path = self.app_path)
            promise = self.api.handle_request_indication(req_indication)
        except:
            pass
        
    def _start(self): 
        self.retrieve_path()
       
        self._started()
        
    def _stop(self):
        self.deregister_app()
        self._stopped()
        
    
            
            
            
            
    
            
        
 
        
        
        
        

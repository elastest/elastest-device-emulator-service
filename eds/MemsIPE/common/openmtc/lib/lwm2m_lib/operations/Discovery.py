from OperationRequest import OperationRequest
from lwm2m_lib.api import lwm2m_api

class Discovery(OperationRequest): 
    def __init__(self, lwm2m_resources=None):
        self.lwm2m_resourcrs = lwm2m_resources
        super(Discovery, self).__init__()
        
    def get_all_resources(self, ):
        """ Returns the list of endpoint related information for discovery request which is
        .well-known/core """
        
        total_resources = {}
        
        for endpoint_name, endpoint_object in self.lwm2m_resourcrs.endpoint_dict.iteritems():
            for _, objects_desc in endpoint_object["object"].objects_dict.iteritems():
                object_id = objects_desc["object_id"]
                object_inst_id = objects_desc["object_inst_id"]
                for _, resources_desc in objects_desc["object"].resources_id_dict.iteritems():
                    res_id = resources_desc["object"].res_id
                    res_inst_id = resources_desc["object"].res_inst_id
                    
                    link = endpoint_name + "/" + str(object_id) + "/" + str(object_inst_id) + \
                            "/" + str(res_id) + "/" + str(res_inst_id)
                    
                    total_resources.update({
                        link : {"endpoint_name" : endpoint_name, "object_id" : object_id, \
                                "object_inst_id" : object_inst_id, "res_id" : res_id, \
                                "res_inst_id" : res_inst_id}
                    })
                    
        return total_resources
    
    def get_resource(self, path, remote):
        
        resource_payload = {}
        
        endpoint_name, object_id, object_inst_id, res_id, res_inst_id, \
                            _, _ = self.find_elements(path, remote)
        endpoint = self.lwm2m_resourcrs.return_endpoint_object(endpoint_name=endpoint_name)
        if (endpoint and object_id) is not None:
            if object_inst_id is not None:
                object_id_object_inst_id = str(object_id) + "_" + str(object_inst_id)
                if endpoint.objects_dict.has_key(object_id_object_inst_id) or object_inst_id is not None:
                    object_attributes = endpoint.objects_dict[object_id_object_inst_id]["object"].attributes
                    obj_pmax = object_attributes.pmax
                    obj_pmin = object_attributes.pmin
                    resources_dict = endpoint.objects_dict[object_id_object_inst_id]["object"].resources_id_dict
                    res_id_res_inst_id = str(res_id) + "_" + str(res_inst_id)
                    if resources_dict.has_key(res_id_res_inst_id):
                        res_attributes = resources_dict[res_id_res_inst_id]["object"].attributes
                        res_pmax = res_attributes.pmax
                        res_pmin = res_attributes.pmin
                        parameters_dict = endpoint.param_dict
                        link = endpoint_name + "/" + str(object_id) + "/" + str(object_inst_id) + "/" + \
                                str(res_id) + "/" + str(res_inst_id)
                        resource_payload["2"] = {"link" : link, "pmax" : res_pmax, "pmin" : res_pmin, "parameters_dict" : parameters_dict}
                        return resource_payload
                
                    link = endpoint_name + "/" + str(object_id) + "/" + str(object_inst_id)
                    resource_payload["1"] = {"link" : link, "pmax" : obj_pmax, "pmin" : obj_pmin}
                    return resource_payload
            else:
                object_inst_id = 0
                object_id_object_inst_id = str(object_id) + "_" + str(object_inst_id)
                if endpoint.objects_dict.has_key(object_id_object_inst_id):
                    object_attributes = endpoint.objects_dict[object_id_object_inst_id]["object"].attributes
                    obj_pmax = object_attributes.pmax
                    obj_pmin = object_attributes.pmin
                    resources_dict = endpoint.objects_dict[object_id_object_inst_id]["object"].resources_id_dict
                    counter = 0
                    self.logger.info("resources dict %s", resources_dict)
                    for _, res_list in resources_dict.iteritems():
                        res_id = res_list["object"].res_id
                        res_inst_id = res_list["object"].res_inst_id
                        self.logger.info("counter %s", counter)
                        counter = counter + 1
                        link = endpoint_name + "/" + str(object_id) + "/" + str(object_inst_id) + "/" +  str(res_id) + "/" + str(res_inst_id)
                        
                        resource_payload[link] = {"object_id" : object_id, "pmax" : obj_pmax, "pmin" : obj_pmin}
                    return resource_payload
                
    def forward_request(self, path, remote, client_port):
        endpoint_name, object_id, object_inst_id, res_id, res_inst_id, \
                            _, _ = self.find_elements(path, remote)
        endpoint = self.lwm2m_resourcrs.return_endpoint_object(endpoint_name=endpoint_name)
        if endpoint is not None:
            listener_ip = endpoint.listener_ip
            listener_port = endpoint.listener_port
            
            request = lwm2m_api()
            response = request.discover_resources(listener_ip, listener_port, endpoint_name=endpoint_name, object_id=object_id, \
                                object_inst_id=object_inst_id, res_id=res_id,
                                res_inst_id=res_inst_id, client_port=client_port)
            return response
        else:
            self.logger.error("Invalid Endpoint Name")
            return
                
    def display_resources(self, resources):
        if resources.has_key("1"):
            self.logger.info("Discovered Resources")
            link = resources["1"]["link"]
            pmin = resources["1"]["pmin"]
            pmax = resources["1"]["pmax"]
            self.logger.info("<%s>;pmin=%s;pmax=%s", link, pmin, pmax)
        elif resources.has_key("2"):
            self.logger.info("Discovered Resources")
            link = resources["2"]["link"]
            pmin = resources["2"]["pmin"]
            pmax = resources["2"]["pmax"]
            lifetime = resources["2"]["parameters_dict"]["lt"]
            self.logger.info("<%s>;pmin=%s;pmax=%s;lt=%s", link, pmin, pmax, lifetime)
        else:
            resource_string = ""
            self.logger.info("Discovered Resources")
            for link, res_info in resources.iteritems():
                object_id = link.split("/")[1]
                res_id = link.split("/")[3]
                resource_string += "</" + object_id + "//" + res_id + ">" + ", "
                pmin = res_info["pmin"]
                pmax = res_info["pmax"]
            self.logger.info("</%s>;pmin=%s;pmax=%s, %s", res_info["object_id"], pmin, pmax, resource_string)
            

    def display_all_resources(self, resources):
        self.logger.info("Discovered Resource Links")
        counter = 1
        for resource_link, _ in resources.iteritems():
            self.logger.info("%s: %s", counter, resource_link)
            counter += 1
        
        

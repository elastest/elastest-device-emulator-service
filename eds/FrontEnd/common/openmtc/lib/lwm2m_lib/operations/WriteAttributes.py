from lwm2m_lib.operations.OperationRequest import OperationRequest
from lwm2m_lib.api import lwm2m_api
from json import dumps, loads

class WriteAttributes(OperationRequest):
    
    def __init__(self, lwm2m_resources):
        self.lwm2m_resources = lwm2m_resources
    
    def set_attributes(self, path, remote, payload):
        endpoint_name, object_id, object_inst_id, res_id, res_inst_id, \
                            _, _ = self.find_elements(path, remote)
        endpoint = self.lwm2m_resources.return_endpoint_object(endpoint_name=endpoint_name)
        if (endpoint and object_id) is not None:
            if object_inst_id is not None:
                object_id_object_inst_id = str(object_id) + "_" + str(object_inst_id)
                if endpoint.objects_dict.has_key(object_id_object_inst_id):
                    if res_id is not None:
                        if res_inst_id is None:
                            res_inst_id = 0
                        res_id_res_inst_id = str(res_id) + "_" + str(res_inst_id)
                        resources_dict = endpoint.objects_dict[object_id_object_inst_id]["object"].resources_id_dict
                        if resources_dict.has_key(res_id_res_inst_id):
                            res_attributes = resources_dict[res_id_res_inst_id]["object"].attributes
                            self.assign_attributes(res_attributes, payload)
                    else:
                        object_attributes = endpoint.objects_dict[object_id_object_inst_id]["object"].attributes
                        self.assign_attributes(object_attributes, payload)
            else:
                object_inst_exist = True
                object_inst_id = 0
                while object_inst_exist:
                    object_id_object_inst_id = str(object_id) + "_" + str(object_inst_id)
                    if endpoint.objects_dict.has_key(object_id_object_inst_id):
                        object_attributes = endpoint.objects_dict[object_id_object_inst_id]["object"].attributes
                        self.assign_attributes(object_attributes, payload)
                        object_inst_id += 1
                    else:
                        object_inst_exist = False
        else:
            self.logger.error("Invalid Endpoint Name/Object ID missing")
    
    def assign_attributes(self, attributes, attribute_values_dict):
        if "pmax" in attribute_values_dict:
            attributes.pmax = attribute_values_dict["pmax"]
        if "pmin" in attribute_values_dict:
            attributes.pmin = attribute_values_dict["pmin"]
        if "gt" in attribute_values_dict:
            attributes.gt = attribute_values_dict["gt"]
        if "lt" in attribute_values_dict:
            attributes.lt = attribute_values_dict["lt"]
        if "st" in attribute_values_dict:
            attributes.st = attribute_values_dict["st"]
        if "cancel" in attribute_values_dict:
            attributes.cancel = attribute_values_dict["cancel"]


    def forward_request(self, path, remote, payload, content_type, client_port):
        endpoint_name, object_id, object_inst_id, res_id, res_inst_id, \
                            _, _ = self.find_elements(path, remote)
        endpoint = self.lwm2m_resources.return_endpoint_object(endpoint_name=endpoint_name)
        
        listener_ip = endpoint.listener_ip
        listener_port = endpoint.listener_port
        
        payload = dumps(payload)
        
        request = lwm2m_api()
        response = request.write_attributes(listener_ip, listener_port, endpoint_name, object_id, \
                            payload, content_type, object_inst_id=object_inst_id, \
                            res_id=res_id, res_inst_id=res_inst_id, client_port=client_port)

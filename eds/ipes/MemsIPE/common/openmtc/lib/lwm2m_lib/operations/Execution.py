from lwm2m_lib.api import lwm2m_api
from lwm2m_lib.operations.OperationRequest import OperationRequest
from json import dumps, loads

action_mapping = {}
action_mapping["4200/5"] = {"target_object_id" : 4200, "target_res_id" : 4, "target_action" : True}
action_mapping["4200/6"] = {"target_object_id" : 4200, "target_res_id" : 4, "target_action" : False}

class Execution(OperationRequest):
    
    def __init__(self, lwm2m_resources):
        self.lwm2m_resources = lwm2m_resources
        
    def forward_request(self, path, remote, payload, client_port):
        self.logger.info("Forwarding Execution Request")
        endpoint_name, object_id, object_inst_id, res_id, res_inst_id, \
                            _, _ = self.find_elements(path, remote)
        if (endpoint_name or object_id or object_inst_id or res_id) is None:
            self.logger.warn("Missing Parameter(s). Cannot perform Execution.")
            return 
        else:
            if endpoint_name is not None:
                endpoint = self.lwm2m_resources.return_endpoint_object(endpoint_name=endpoint_name)
                if endpoint is not None:
                    listener_ip = endpoint.listener_ip
                    listener_port = endpoint.listener_port
                    
                    payload = payload
                    
                    request = lwm2m_api()
                    response = request.execute_resource(listener_ip, listener_port, endpoint_name, \
                                object_id, object_inst_id, res_id, res_inst_id=res_inst_id,\
                                payload=payload, client_port=client_port)
    
    
    def execute_resource(self, path, remote, payload):
        endpoint_name, object_id, object_inst_id, res_id, res_inst_id, \
                            _, _ = self.find_elements(path, remote)
        self.logger.info("Executing the Resource %s/%s/%s/%s", endpoint_name, object_id, object_inst_id, res_id)
        endpoint = self.lwm2m_resources.return_endpoint_object(endpoint_name=endpoint_name)
        if endpoint is not None:
            object_id_object_inst_id = str(object_id) + "_" + str(object_inst_id)
            if endpoint.objects_dict.has_key(object_id_object_inst_id):
                    if res_id is not None:
                        if res_inst_id is None:
                            res_inst_id = 0
                        res_id_res_inst_id = str(res_id) + "_" + str(res_inst_id)
                        resources_dict = endpoint.objects_dict[object_id_object_inst_id]["object"].resources_id_dict
                        if resources_dict.has_key(res_id_res_inst_id):
                            object_id_res_id = str(object_id) + "/" + str(res_id)
                            if object_id_res_id in action_mapping:
                                target_res_id = action_mapping[object_id_res_id]["target_res_id"]
                                target_action = action_mapping[object_id_res_id]["target_action"]
                                res_id_res_inst_id = str(target_res_id) + "_" + str(res_inst_id)
                                resources_dict[res_id_res_inst_id]["object"].res_value = target_action
                                self.logger.info("Execution on resource %s is carried out", path)
                                return (endpoint_name, object_id, object_inst_id, target_res_id, target_action)
                        else:
                            self.logger.error("Resource ID not found")
                            return
                    else:
                        self.logger.error("Resource ID is Invalid")
                        return
            else:
                self.logger.error("Object ID not found")
                return
        else:
            self.logger.error("Endpoint doesn't exist.")
            return

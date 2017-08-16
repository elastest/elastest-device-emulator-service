from lwm2m_lib.operations.Read import Read
from lwm2m_lib.operations.OperationRequest import OperationRequest
from lwm2m_lib.api import lwm2m_api
import json

class Write(OperationRequest):
    
    def __init__(self, lwm2m_object):
        super(Write, self).__init__()
        self.lwm2m_resources = lwm2m_object
        
    def write_resource(self, payload, path, content_type):
        
        if content_type == "application/json":
            
            resources = {}
            endpoint_name = path[1].value
            object_id = path[2].value
            object_inst_id = path[3].value
            object_id_object_inst_id = str(object_id) + "_" + str(object_inst_id)
            
            resources = json.loads(payload)
            
            self.logger.info("Updating the Resource using Write Operation")
            
            endpoint_object = self.lwm2m_resources.return_endpoint_object(endpoint_name=endpoint_name)
            for res_id, res in resources.iteritems():
                res_id_res_inst_id = str(res_id) + "_" + str(res["res_inst_id"])
                endpoint_object.objects_dict[object_id_object_inst_id]["object"].resources_id_dict[res_id_res_inst_id]\
                ["object"].res_value = res["res_value"]
            
        elif content_type == "text/plain":
            pass
        
    
    def forward_write_request(self, path, payload, content_type, remote, client_port):
        
        endpoint_name, object_id, object_inst_id, res_id, \
        res_inst_id, sender_ip, sender_port = self.find_elements(path, remote)
        
        self.logger.info("Forwarding Write Resource Request to Endpoint %s", endpoint_name)
        endpoint_object = self.lwm2m_resources.return_endpoint_object(endpoint_name=endpoint_name)
        listener_ip = endpoint_object.listener_ip
        listener_port = endpoint_object.listener_port

        request = lwm2m_api()
        response = request.write_resource(listener_ip, listener_port, endpoint_name, object_id, \
                                        payload, content_type, object_inst_id=object_inst_id, \
                                        res_id=res_id, res_inst_id=res_inst_id, client_port=client_port)
    

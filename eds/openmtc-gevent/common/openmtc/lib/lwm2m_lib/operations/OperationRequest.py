from lwm2m_lib.data_model.ParseQueryPayload import ParsePath, ParsePayload, ParseQuery
from lwm2m_lib.data_model.ResourcesList import CommonLists
from futile.logging import LoggerMixin
from lwm2m_lib.import_common_libs import  options, constants, json
from lwm2m_lib.api import lwm2m_api

class OperationRequest(LoggerMixin, ParsePath, ParsePayload, ParseQuery, CommonLists):
    
    def __init__(self, ):
        super(OperationRequest, self).__init__()
        
    
    def translate_key_info(self, parsed_path, clients):
        client_id = object_id = object_inst_id = resource_id = r_id = r_code = resource_value =\
                pmin = pmax = None
        
        if parsed_path.has_key("clientID"):
            client_id = parsed_path["clientID"]
        if parsed_path.has_key("objectID"):
            object_id = parsed_path["objectID"]
            attributes = clients.get_attributes(client_id, int(object_id))
        if parsed_path.has_key("objectInstID"):
            object_inst_id = parsed_path["objectInstID"]
            attributes = clients.get_attributes(client_id, int(object_id), int(object_inst_id))
        if parsed_path.has_key("resID"):
            resource_id = parsed_path["resID"]
            r_id,r_code = clients.return_resource_identifier(res_id=int(resource_id))
            res_value = clients.read_client(client_id, int(object_id),
                                              int(object_inst_id), res_id=int(resource_id))
            resource_value = str(res_value.res_value)
            attributes = clients.get_attributes(client_id, int(object_id),
                                             int(object_inst_id), int(resource_id))
            
        pmin = str(attributes["pmin"])
        pmax = str(attributes["pmax"])
        sender_ip = parsed_path["sender_ip"]
        sender_port = parsed_path["sender_port"]
        
        return (client_id, object_id, object_inst_id, resource_id, r_id, r_code, resource_value,
                pmin, pmax, sender_ip, sender_port)
        
    def find_elements(self, path, remote):
        parsed_path = self.parse_path(path, remote)
        endpoint_name = object_id = object_inst_id = res_id = res_inst_id = sender_ip = sender_port = None
        if "endpoint_name" in parsed_path:
            endpoint_name = parsed_path["endpoint_name"]
        if "object_id" in parsed_path:
            object_id = parsed_path["object_id"]
        if "object_inst_id" in parsed_path:
            object_inst_id = parsed_path["object_inst_id"]
        if "res_id" in parsed_path:
            res_id = parsed_path["res_id"]
        if "res_inst_id" in parsed_path:
            res_inst_id = parsed_path["res_inst_id"]
        if "sender_ip" in parsed_path:
            sender_ip = parsed_path["sender_ip"]
        if "sender_port" in parsed_path:
            sender_port = parsed_path["sender_port"]
        
        return (endpoint_name, object_id, object_inst_id, res_id, res_inst_id, sender_ip, sender_port)
    
    
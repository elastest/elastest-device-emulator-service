from lwm2m_lib.operations.OperationRequest import OperationRequest


class Read(OperationRequest):
    
    def __init__(self, lwm2m_resources):
        super(Read, self).__init__()
        self.lwm2m_resources = lwm2m_resources
    
    def read_resource(self, path, remote):
        endpoint_name, object_id, object_inst_id, res_id, res_inst_id, \
                            _, _ = self.find_elements(path, remote)
        
        if object_inst_id is not None and res_id is not None:
            endpoint_object = self.lwm2m_resources.return_endpoint_object(endpoint_name=endpoint_name)
            
            object_id_object_inst_id = str(object_id) + "_" + str(object_inst_id)
            if res_inst_id is not None:
                res_id_res_inst_id = str(res_id) + "_" + str(res_inst_id)
            else:
                res_id_res_inst_id = str(res_id) + "_" + "0"
            
            response = endpoint_object.objects_dict[object_id_object_inst_id]["object"].resources_id_dict[res_id_res_inst_id]["object"].res_value
            content_type = "text/plain"
            
            return response, content_type
        
        elif object_inst_id is None:
            object_resource = {}
            endpoint_object = self.lwm2m_resources.return_endpoint_object(endpoint_name=endpoint_name)
            object_dict = endpoint_object.objects_dict
            for object_id_object_inst_id, obj_resource in object_dict:
                if object_id_object_inst_id.startswith(object_id):
                    object_resource.update({
                        object_id_object_inst_id : {"object_id" : obj_resource["object_id"]}
                    })
            
            response = object_resource
            self.logger.info(response)
            content_type = "application/json"
            
            
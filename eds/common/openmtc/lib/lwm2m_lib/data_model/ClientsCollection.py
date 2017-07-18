import string
import random
from ObjectsCollection import ObjectsCollection, DeviceMgmtObject
from mgmt_objects import lwm2m_dict_objects
from futile.logging import LoggerMixin
from lwm2m_lib.operations.ObservationNotification import ResourceEventHandler

class ClientEndpoint(object):
    def __init__(self, endpoint_name, objects=None, unique_location_id=None, local_ip=None, \
                 local_port=None, local_listen_ip=None, local_listen_port=None):
        """
        For endpoint parameters, they are defined as:
        lt = lifetime, lwm2m = lwm2m version, b = binding_mode, sms = SMS ISDN number
        """
        self.endpoint_name = endpoint_name
        self.objects = objects
        self.objects_dict = {} #key: object_id_object_instance_id, value: dictionary of resource instances
        self.unique_id = unique_location_id
        self.param_dict = {}
        self.local_ip = local_ip
        self.local_port = local_port
        self.listener_ip = local_listen_ip
        self.listener_port = local_listen_port
    
    def get_parameters(self, ):
        return self.param_dict
    
    def set_parameters(self, endpoint_parameters):
        if endpoint_parameters.has_key("lt"):
            self.param_dict["lt"] = endpoint_parameters["lt"]
        if endpoint_parameters.has_key("lwm2m"):
            self.param_dict["lwm2m"] = endpoint_parameters["lwm2m"]
        if endpoint_parameters.has_key("b"):
            self.param_dict["b"] = endpoint_parameters["b"]
        if endpoint_parameters.has_key("sms"):
            self.param_dict["sms"] = endpoint_parameters["sms"]
    
    def set_address(self, local_ip, local_port, listener_ip, listener_port):
        if local_ip is not None:
            self.local_ip = local_ip
        if local_port is not None:
            self.local_port = local_port
        if listener_ip is not None:
            self.listener_ip = listener_ip
        if listener_port is not None:
            self.listener_port = listener_port
            
    def update_resource(self, objects):
        if objects is not None or objects != "":
            for key, value in objects.iteritems():
                object_id = key.split("_")[0]
                object_inst_id = key.split("_")[1]
                res_id = key.split("_")[2]
                res_inst_id = key.split("_")[3]
                object_id_object_inst_id = str(object_id) + "_" + str(object_inst_id)
                res_id_res_inst_id = str(res_id) + "_" + str(res_inst_id)
                res_value = value
                    
                if self.objects_dict.has_key(object_id_object_inst_id):
                    object_id_object_inst_id_object = self.objects_dict[object_id_object_inst_id]["object"]
                    resources_list = lwm2m_dict_objects[str(object_id)]["resource_list"]
                    operation_type = resources_list[str(res_id)]["operation"]
                    
                    if object_id_object_inst_id_object.resources_id_dict.has_key(res_id_res_inst_id):
                        resource_object = object_id_object_inst_id_object.resources_id_dict[res_id_res_inst_id]["res_object"]
                        if "R" in operation_type and resource_object.res_value=="":
                            resource_object.res_value = res_value
                        elif "W" in operation_type:
                            resource_object.res_value = res_value

class ObjectInstance():
    def __init__(self):
        self.observations = []
    
#Observation: parses the Observe, used by the ClientsCollection to store the observationInfo at the right place in the resource tree
    

#TODO: resource tree dictionary of endpoint name and ClientEndpoint objects - done
#rename as LWM2MResourceTree - done
class LWM2MResourceTree(LoggerMixin):
    def __init__(self, dispatcher=None):
        super(LWM2MResourceTree, self).__init__()
        self.dispatcher = dispatcher
        self.res_handler = None
        self.logger.debug("Dispatcher Object : %s", dispatcher)
        if self.dispatcher is not None:
            self.res_handler = ResourceEventHandler(self.dispatcher)
        self.endpoint_dict = {}
        self.location_to_endpoint_dict={}
        self.endpoint_name_to_location = {}
        self.object_collection = ObjectsCollection()
    

    def process_client(self, endpoint):
        
        if not self.endpoint_dict.has_key(endpoint.endpoint_name):
            self.endpoint_dict.update({
                endpoint.endpoint_name : {"object" : endpoint}
            })
            #what if endpoint ip changes
            """ Generates the Location """
            endpoint.unique_id = self.locID_generator(15)
            
            self.location_to_endpoint_dict.update({
                endpoint.unique_id : {"object" : endpoint}
            })
            
            self.endpoint_name_to_location[endpoint.endpoint_name] = endpoint.unique_id
            
            for endpt_objs, _ in endpoint.objects_dict.iteritems():
                object_id = endpoint.objects_dict[endpt_objs]["object_id"]
                object_inst_id = endpoint.objects_dict[endpt_objs]["object_inst_id"]
                
                endpoint.objects_dict[endpt_objs]["object"] = DeviceMgmtObject(endpt_objs, endpoint.local_ip, endpoint.local_port)
                
                self.object_collection.process_object(endpoint.objects_dict[endpt_objs]["object"], object_id, endpoint.local_ip, endpoint.local_port)
        elif self.endpoint_dict.has_key(endpoint.endpoint_name):
            endpoint.unique_id = self.endpoint_name_to_location[endpoint.endpoint_name]
            
        return endpoint.unique_id
        
    
    def add_object_instance_resource_instance(self, endpoint, object_id, res_id, res_value, \
                                              object_inst_id=None, res_inst_id=None):
        resource_change_flag = False
        
        def add_resource(endpoint, object_id_object_inst_id, res_id_res_inst_id, res_value):
            resource_change_flag = result = False
            object_id_object_inst_id_object = endpoint.objects_dict[object_id_object_inst_id]["object"]
            resources_list = lwm2m_dict_objects[str(object_id)]["resource_list"]
            operation_type = resources_list[str(res_id)]["operation"]
            if object_id_object_inst_id_object.resources_id_dict.has_key(res_id_res_inst_id):
                resource_object = object_id_object_inst_id_object.resources_id_dict[res_id_res_inst_id]["object"]
                if ("R" in operation_type or "W" in operation_type) and resource_object.res_value == "" and res_value != "":
                    resource_object.res_value = res_value
                    resource_change_flag = True
                    
                    resource = {
                        object_id_object_inst_id : {"endpoint_name": endpoint.endpoint_name, "resources" : {res_id : {"res_value" : resource_object.res_value, "res_inst_id" : ''}}}
                    }
                    if self.res_handler is not None and resource is not None:
                        result = self.res_handler.resource_notification(resource)
                    
                elif "W" in operation_type:
                    if str(resource_object.res_value) != str(res_value):
                        resource_object.res_value = res_value
                        resource_change_flag = True
                        
                        resource = {
                        object_id_object_inst_id : {"endpoint_name": endpoint.endpoint_name, "resources" : {res_id : {"res_value" : resource_object.res_value, "res_inst_id" : ''}}}
                        }
                        if self.res_handler is not None and resource is not None:
                            result = self.res_handler.resource_notification(resource)
            if result:
                return
            else:
                return resource_change_flag
        
        if object_inst_id is None:
            object_inst_id = 0
            object_id_object_inst_id = str(object_id) + "_" + str(object_inst_id)
            
        else:
            object_id_object_inst_id = str(object_id) + "_" + str(object_inst_id)
        
        if res_inst_id is None:
            res_id_res_inst_id = str(res_id) + "_" + "0"
        else:
            res_id_res_inst_id = str(res_id) + "_" + str(res_inst_id)
        if endpoint.objects_dict.has_key(object_id_object_inst_id):
            resource_change_flag = add_resource(endpoint, object_id_object_inst_id, res_id_res_inst_id, res_value)
        else:
            endpoint.objects_dict.update({
                object_id_object_inst_id : {"object" : None, "object_id" : object_id, \
                                                     "object_inst_id" : object_inst_id}
            })
            
            endpoint.objects_dict[object_id_object_inst_id]["object"] = DeviceMgmtObject(object_id_object_inst_id, endpoint.local_ip, endpoint.local_port)
            
            self.object_collection.process_object(endpoint.objects_dict[object_id_object_inst_id]["object"], object_id, endpoint.local_ip, endpoint.local_port)
            resource_change_flag = add_resource(endpoint, object_id_object_inst_id, res_id_res_inst_id, res_value)
            
        return resource_change_flag
    
    
    def create_object_object_inst(self, endpoint_name, object_id, object_inst_id=None):
        """ Object Instance ID for each Object is automatically generated if the object multiInstance
        is allowed as per the specification
        """
        
        if self.endpoint_dict.has_key(endpoint_name):
            endpoint = self.endpoint_dict[endpoint_name]["object"]
            if lwm2m_dict_objects.has_key(str(object_id)):
                object_multi_instance = lwm2m_dict_objects[str(object_id)]["multiInst"]
                if not object_multi_instance:
                    self.logger.error("Multi-Instance of the Object %s is not allowed !", object_id)
                    message = "Multi-Instance of the object is not allowed"
                    return message
                else:
                    if object_inst_id is None:
                        object_inst_id = 0
                        object_id_object_inst_id = str(object_id) + "_" + str(object_inst_id)
                        while True:
                            if endpoint.objects_dict.has_key(object_id_object_inst_id):
                                object_inst_id += 1
                                object_id_object_inst_id = str(object_id) + "_" + str(object_inst_id)
                            else:
                                break
                    object_id_object_inst_id = str(object_id) + "_" + str(object_inst_id)
                
                if not endpoint.objects_dict.has_key(object_id_object_inst_id):        
                    endpoint.objects_dict.update({
                        object_id_object_inst_id : {"object" : None, "object_id" : object_id, \
                                                         "object_inst_id" : object_inst_id}
                    })
                    endpoint.objects_dict[object_id_object_inst_id]["object"] = DeviceMgmtObject(object_id_object_inst_id, endpoint.local_ip, endpoint.local_port)
            
                    self.object_collection.process_object(endpoint.objects_dict[object_id_object_inst_id]["object"], object_id, endpoint.local_ip, endpoint.local_port)
                    return int(object_inst_id)
                else:
                    message = "Object Instance already exists"
                    return message
        else:
            message = "Endpoint doesn't exist"
            return message
    
        
    def update_endpoint_parameters(self, endpoint_name=None, endpoint_location=None, \
                                    endpoint_parameters={}, objects=None, local_ip=None, local_port=None, \
                                    listener_ip=None, listener_port=None):
        if endpoint_name is not None:
            if self.endpoint_dict.has_key(endpoint_name):
                endpoint = self.endpoint_dict[endpoint_name]["object"]
        elif endpoint_location is not None:
            if self.location_to_endpoint_dict.has_key(endpoint_location):
                endpoint = self.location_to_endpoint_dict[endpoint_location]["object"]
        else:
            return None
        
        endpoint.set_parameters(endpoint_parameters)
        endpoint.set_address(local_ip, local_port, listener_ip, listener_port)
        endpoint.update_resource(objects)
        
        
    def return_endpoint_object(self, endpoint_name=None, endpoint_location=None):
        if endpoint_name is not None:
            if self.endpoint_dict.has_key(endpoint_name):
                return self.endpoint_dict[endpoint_name]["object"]
        
        if endpoint_location is not None:
            if self.location_to_endpoint_dict.has_key(endpoint_location):
                return self.location_to_endpoint_dict[endpoint_location]["object"]
        
        return None
                
    
    def locID_generator(self, str_size, chars=string.ascii_uppercase + string.digits):
        """ Generates a random 10 digit alpha numeric which is used as location for the
        registered endpoint(or client) """
        
        return ''.join([random.choice(chars) for _ in range(str_size)])

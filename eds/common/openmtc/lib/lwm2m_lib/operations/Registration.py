from lwm2m_lib.import_common_libs import constants, options, json
from lwm2m_lib.api import lwm2m_api
from lwm2m_lib.operations.OperationRequest import OperationRequest
from lwm2m_lib.data_model.ClientsCollection import LWM2MResourceTree, ClientEndpoint
import random
from json import dumps

URI_QUERY_VALUE = 15
LOCATION_VALUE = 8
URI_PATH_VALUE = 11
URI_HOST_VALUE = 3
URI_PORT_VALUE = 7
CONTENT_TYPE_VALUE = 12


class Endpoint(object):
    def __init__(self, endpoint_name, objects=None, lifetime=None, version=None, sms_number=None, binding_mode=None, \
                 local_ip=None, local_port=None, listener_ip=None, listener_port=None):
        self.endpoint = ClientEndpoint(endpoint_name)
        self.endpoint.objects = objects
        self.endpoint.param_dict = {"lt" : lifetime, "lwm2m" : version, \
                               "b" : binding_mode, "sms" : sms_number}
        self.endpoint.local_ip = local_ip
        self.endpoint.local_port = local_port
        self.endpoint.listener_ip = listener_ip
        self.endpoint.listener_port = listener_port
        if objects is not None:
            parsed_objects = objects.split(",")
            for objs in parsed_objects:
                object_id = objs.strip().split("/")[0]
                object_inst_id = objs.strip().split("/")[1]
                self.endpoint.objects_dict.update({
                    objs.strip().replace("/","_") : {"object" : None, "object_id" : object_id, \
                                                     "object_inst_id" : object_inst_id}
                })
            
        

class Registration(OperationRequest):
    
    def __init__(self, lwm2m_resources):
        self.lwm2m_resources = lwm2m_resources
        self.unique_ports = set()
        super(Registration, self).__init__()
    
    def register_client(self, endpoint):
        """ Sends the registration details to the LWM2M Resource Tree
        
        @param: endpoint: object containing all the endpoint details for registration
        
        """
        return self.lwm2m_resources.process_client(endpoint)
    
    
    def process_registration(self, msg, uri_query):
        """ To process the contents of Registration POST request """
        
        endpoint_name = lifetime = sms_number = version = binding_mode = client_local_ip = \
                        client_local_port = client_listener_ip = client_listener_port= None
        
        objects = msg.payload
        if objects == "None" or objects=="":
            objects = None
        for item in uri_query:
            if "ep" in item.value:
                endpoint_name = item.value.split("=")[1]
            if "lt" in item.value:
                lifetime = item.value.split("=")[1]
            if "sms" in item.value:
                sms_number = item.value.split("=")[1]
            if "lwm2m" in item.value:
                version = item.value.split("=")[1]
            if "b" in item.value:
                binding_mode = item.value.split("=")[1]
            if "local_ip" in item.value:
                client_local_ip = item.value.split("=")[1]
            if "local_port" in item.value:
                client_local_port = item.value.split("=")[1]
            if "listener_ip" in item.value:
                client_listener_ip = item.value.split("=")[1]
            if "listener_port" in item.value:
                client_listener_port = item.value.split("=")[1]

        self_object = Endpoint(endpoint_name, objects, lifetime=lifetime, version=version, \
                           sms_number=sms_number, binding_mode=binding_mode, local_ip=client_local_ip, \
                           local_port=client_local_port, listener_ip=client_listener_ip, \
                           listener_port=client_listener_port)
        endpoint = self_object.endpoint
        return endpoint
    
    def process_registration_update(self, msg, uri_query):
        
        lifetime = sms_number = binding_mode = client_local_ip = \
                        client_local_port = client_listener_ip = client_listener_port= None
        
        for item in uri_query:
            if "ep" in item.value:
                endpoint_name = item.value.split("=")[1]
            if "lt" in item.value:
                lifetime = item.value.split("=")[1]
            if "sms" in item.value:
                sms_number = item.value.split("=")[1]
            if "b" in item.value:
                binding_mode = item.value.split("=")[1]
            if "local_ip" in item.value:
                client_local_ip = item.value.split("=")[1]
            if "local_port" in item.value:
                client_local_port = item.value.split("=")[1]
            if "listener_ip" in item.value:
                client_listener_ip = item.value.split("=")[1]
            if "listener_port" in item.value:
                client_listener_port = item.value.split("=")[1]
        
        endpoint_parameters = {"lt" : lifetime, "sms" : sms_number, "b" : binding_mode}
        
        return endpoint_parameters, client_local_ip, client_local_port, client_listener_ip, client_listener_port
    
    
    def send_client_registration(self, endpoint, registration_params, \
                                 dm_server_ip, dm_server_port, listener_ip, listener_port, client_port):
        """ Client registration request to the LWM2M server """
        
        self.logger.debug("Client port is %s", client_port)
        self.logger.info("Sending Endpoint Registration request to the LWM2M Server")
        
        query_params = "ep=" + endpoint.endpoint_name
        for param, value in registration_params.iteritems(): #endpoint.param_dict.iteritems():
            query_params += "&" + param + "=" + str(value)
        query_params += "&" + "listener_ip=" + listener_ip + "&" + "listener_port=" + str(listener_port)
        query_params += "&" + "local_ip=" + "localhost" + "&" + "local_port=" + str(client_port)

        payload = None #endpoint.objects
        
        #unique_client_port = self.generate_unique_random_port(client_port_start, client_port_stop)
        
        request = lwm2m_api()
        client, response = request.client_registration(dm_server_ip, dm_server_port, query_params,
                                                  payload, client_port=client_port)
        
        return client, response
    
    
    #TODO
    def update_endpoint_params(self, endpoint_location, endpoint_parameters, objects, local_ip, \
                                                local_port, listener_ip, listener_port):
        """ Updating endpoint parameters in the Resource Tree """
        
        self.lwm2m_resources.update_endpoint_parameters(endpoint_location=endpoint_location, \
                                    endpoint_parameters=endpoint_parameters, objects=objects, local_ip=local_ip, \
                                    local_port=local_port, listener_ip=listener_ip, \
                                    listener_port=listener_port)
        
    
    def handle_put_resource_updates(self, payload, endpoint_location=None, endpoint_name=None):
        if endpoint_location is not None:
            endpoint = self.lwm2m_resources.return_endpoint_object(endpoint_location=endpoint_location)
        elif endpoint_name is not None:
            endpoint = self.lwm2m_resources.return_endpoint_object(endpoint_name=endpoint_name)
        for object_ids, resources in payload.iteritems():
            object_id = object_ids.split("_")[0]
            object_inst_id = object_ids.split("_")[1]
            for res_ids, res in resources["resources"].iteritems():
                res_id = res_ids
                res_inst_id = res["res_inst_id"]
                if res_inst_id == "":
                    res_inst_id = None    #todo: rsh:: res_inst_id = 0 ???
                res_value = res["res_value"]
                self.lwm2m_resources.add_object_instance_resource_instance(endpoint, object_id, res_id, res_value, \
                                                object_inst_id=object_inst_id, res_inst_id=res_inst_id)
            
        return endpoint
    
    
    def send_update_registration(self, endpoint_location, endpoint_local_location, objects, dm_server_ip, dm_server_port):
        
        path = endpoint_location
        endpoint = self.lwm2m_resources.return_endpoint_object(endpoint_location=endpoint_local_location)
        
        query_params = ""
        for param, value in endpoint.param_dict.iteritems():
            query_params += param + "=" + str(value) + "&"
        query_params += "local_ip=" + endpoint.local_ip + "&" + "local_port=" + str(endpoint.local_port) + "&"
        query_params += "listener_ip=" + endpoint.listener_ip + "&" + "listener_port=" + str(endpoint.listener_port)
        
        if objects == "" or objects is None:
            payload = ""
        else:
            payload = json.dumps(objects)
        
        request = lwm2m_api()
        response = request.client_registration_update(dm_server_ip, dm_server_port, path, query_params, payload,
                                                client_port=endpoint.local_port)
        
    
    def send_delete(self):
        pass
    
    def generate_unique_random_port(self, client_port_start, client_port_end):
        while True:
            unique_port = random.randint(client_port_start, client_port_end)
            if unique_port in self.unique_ports:
                pass
            else:
                self.unique_ports.add(unique_port)
                break
            if len(self.unique_ports) == int(client_port_end) - int(client_port_start):
                self.unique_ports = {}
        return unique_port

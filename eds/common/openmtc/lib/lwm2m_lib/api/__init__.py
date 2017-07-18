from futile.logging import LoggerMixin
from lwm2m_lib.import_common_libs import connection, constants
from coap import CoapClient
from json import dumps
import socket
from random import randint


class lwm2m_api(LoggerMixin):
    def __init__(self, ):
        super(lwm2m_api, self).__init__()
    
    
    def client_registration(self, server_ip, server_port, query, payload,
                            path="rd?", content_type="application/link-format", client_port=5683):
        
        server_ip_port = server_ip + ":" + str(server_port)
        
        client = CoapClient("coap://" + server_ip_port, client_port=client_port)
        result = client.post(str(path+query), payload, timeout=10000, content_type=content_type)
        
        return client, result
    
    #def client_registration(self, server_ip, server_port, query, payload,
    #                        path="rd?", content_type="application/link-format", client_port=15683):
    #    
    #    server_ip_port = server_ip + ":" + str(server_port)
    #    path += query
    #    client = CoapClient("coap://" + server_ip_port, client_port=client_port)
    #    result = client.post(path, payload)
    #    
    #    return result
    
    
    def client_registration_update(self, server_ip, server_port, path, query, payload, \
                                   client_port=5683, client=None):
        server_ip_port = server_ip + ":" + str(server_port)
        path_query = str(path)  + "?" + query
        payload = payload
        if client is None:
            client = CoapClient("coap://" + server_ip_port, client_port=client_port)
        result = client.put(path_query,  payload, timeout=10000)
        
        return result
        
        
    def read_resource(self, server_ip, server_port, endpoint_name, object_id, res_id, object_inst_id=None, \
                      res_inst_id=None, client_port=5683):
        
        query = "?method=read"
        server_ip_port = server_ip + ":" + str(server_port)
        
        path = "rd/" + endpoint_name + "/" + str(object_id)
        if object_inst_id is not None:
            path += "/" + str(object_inst_id)
        else:
            path +="/0"
        if res_id is not None:
            path += "/" + str(res_id)
            if res_inst_id is not None:
                path += "/" +str(res_inst_id)
            else:
                path += "/0"
                
        payload = None
        #content_type = "application/json"
        path += query
        
        client = CoapClient("coap://" + server_ip_port, client_port=client_port)
        #result = client.get(path, data=payload, content_type=content_type)
        result = client.get(path, data=payload, timeout=10000)
        
        return result
    
    def write_resource(self, server_ip, server_port, endpoint_name, object_id, \
                       payload, content_type, object_inst_id=None, res_id=None, \
                       res_inst_id=None, client_port=5683):
        
        query = "?method=write"
        server_ip_port = server_ip + ":" + str(server_port)
        
        path = "rd/" + endpoint_name + "/" + str(object_id)
        if object_inst_id is not None:
            path += "/" + str(object_inst_id)
        else:
            path +="/0"
        if res_id is not None:
            path += "/" + str(res_id)
            if res_inst_id is not None:
                path += "/" +str(res_inst_id)
            else:
                path += "/0"
        
        path += query
        
        client = CoapClient("coap://" + server_ip_port, client_port=client_port)
        result = client.put(path, payload, timeout=10000, content_type=content_type)
            
    
    def create_object_instance(self, server_ip, server_port, endpoint_name, object_id, \
                               payload, content_type, object_inst_id=None, client_port=5683):
        
        server_ip_port = server_ip + ":" + str(server_port)
        query = "?method=create"
        path = "rd"
        if (endpoint_name and object_id) is not None:
                path += "/" + endpoint_name + "/" + str(object_id)
                if object_inst_id is not None:
                    path += "/" + str(object_inst_id)
        else:
            self.logger.error("Endpoint Name and object_id should be specified")
            return
        
        path += query
        
        client = CoapClient("coap://" + server_ip_port, client_port=client_port)
        result = client.post(path, payload, timeout=10000, content_type=content_type)
        
    
    def discover_resources(self, server_ip, server_port, payload=None, endpoint_name=None,
                                  object_id=None, object_inst_id=None, res_id=None, res_inst_id=None, client_port=5683):

        server_ip_port = server_ip + ":" + str(server_port)
        query = "?method=discover"
        content_type = None
        path = "rd"
        if payload is not None:
            """ ".well-known/core" is a payload """
            content_type = "text/plain"
        else:
            if (endpoint_name or object_id) is not None:
                path += "/" + endpoint_name + "/" + str(object_id)
                if object_inst_id is None and res_id is not None:
                    object_inst_id = 0
                    path += "/" + str(object_inst_id)
                elif object_inst_id is not None:
                    path += "/" + str(object_inst_id)
                
                if res_id is not None:
                    path += "/" + str(res_id)
                    if res_inst_id is None:
                        res_inst_id = 0
                    path += "/" + str(res_inst_id)
            else:
                self.logger.error("Endpoint Name and object_id should be specified")
                return
        path += query

        client = CoapClient("coap://" + server_ip_port, client_port=client_port)
        result = client.get(path, data=payload, timeout=10000, content_type=content_type)
        
        return result
    
    def observe_resource(self, server_ip, server_port, app_ip=None, app_port=None, endpoint_name=None, object_id=None, payload=None, 
                         object_inst_id=None, res_id=None, res_inst_id=None, content_type=None, client_port=5683):
        observe = 0
        result = self.send_observe_request(server_ip, server_port, app_ip, app_port, endpoint_name, object_id, observe, \
                                    payload=payload, object_inst_id=object_inst_id, \
                                    res_id=res_id, res_inst_id=res_inst_id, \
                                    content_type=content_type, client_port=client_port)
        return result
    
    def cancel_observe_resource(self, server_ip, server_port, app_ip, app_port, endpoint_name, object_id, payload=None, 
                         object_inst_id=None, res_id=None, res_inst_id=None, client_port=5683):
        observe = 1
        result = self.send_observe_request(server_ip, server_port, app_ip, app_port, endpoint_name, object_id, observe, \
                                    payload=payload, object_inst_id=object_inst_id, \
                                    res_id=res_id, res_inst_id=res_inst_id, client_port=client_port)
        return result
        
    def send_observe_request(self, server_ip, server_port, app_ip, app_port, endpoint_name, object_id, observe, \
                               payload=None, object_inst_id=None, res_id=None, \
                               res_inst_id=None, content_type=None, token=None, client_port=5683):
        
        server_ip_port = server_ip + ":" + str(server_port)
        path = "rd"
        if payload is not None and endpoint_name is None:
            pass
        elif endpoint_name is not None:
            path += "/" + endpoint_name
            payload = dumps({"app_ip" : app_ip, "app_port" : app_port})
            content_type = "application/json"
            if object_id is not None:
                path += "/" + str(object_id)
                if object_inst_id is not None:
                    path += "/" + str(object_inst_id)
                    if res_id is not None:
                        path += "/" + str(res_id)
                        if res_inst_id is not None:
                            path += "/" + str(res_inst_id)
            else:
                message = "Object ID is missing"
                self.logger.error(message)
                return message
        else:
            message = "Endpoint is missing"
            self.logger.error(message)
            return message
        
        try:
            client = CoapClient("coap://" + server_ip_port, client_port=client_port)
            result = client.get(path, data=payload, observe=observe, content_type=content_type, token=token)
        except:
            return None
        return result
    
    def send_notification(self, server_ip, server_port, token_id, payload, content_type=None, time_elapse=1, client_ip=None, client_port=None):
        path = "rd?"
        query = "method=notify"
        path += query
        server_ip_port = server_ip + ":" + str(server_port)
        client = CoapClient("coap://" + server_ip_port, client_port=client_port)
        result = client.post(path, dumps(payload), timeout=10000, content_type=content_type, token=token_id, observe=time_elapse)
        return result
    
        #NON - ACK METHOD
        #msg_transaction_id = randint(100, 2**16)-1
        #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #sock.bind(('', client_port))
        #msg = connection.Message(connection.Message.NON, code=constants.CONTENT, payload=dumps(payload), content_type=content_type)
        #sock.sendto(msg._pack(msg_transaction_id, token_id), (server_ip, int(server_port)))
        #sock.close()
        
        
    def write_attributes(self, server_ip, server_port, endpoint_name, object_id, payload, content_type,
                        object_inst_id=None, res_id=None, res_inst_id=None, client_port=5683):
        
        server_ip_port = server_ip + ":" + str(server_port)
        query = "?method=write_attributes"
        path = "rd/" + endpoint_name + "/" + str(object_id)
        if object_inst_id is not None:
            path += "/" + str(object_inst_id)
            if res_id is not None:
                path += "/" + str(res_id)
                if res_inst_id is None:
                    res_inst_id = 0
                path += "/" + str(res_inst_id)
        
        path += query
        client = CoapClient("coap://" + server_ip_port, client_port=client_port)
        result = client.put(path, payload, timeout=10000, content_type=content_type)
        
        return result
        
        
    def execute_resource(self, server_ip, server_port, endpoint_name, object_id, object_inst_id, \
                        res_id, res_inst_id=None, payload=None, client_port=5683):
        
        server_ip_port = server_ip + ":" + str(server_port)
        path = "rd"
        query =  "?method=execute"
        if (endpoint_name and object_id and object_inst_id and res_id) is not None:
            path += "/" + endpoint_name + "/" + str(object_id) + "/" + str(object_inst_id) + \
                        "/" + str(res_id)
            if res_inst_id is not None:
                path += "/" + str(res_inst_id)
        
        path += query
        client = CoapClient("coap://" + server_ip_port, client_port=client_port)
        result = client.post(path, payload, timeout=10000)
        
        return result
    
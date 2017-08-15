from json import loads
from lwm2m_lib.operations.OperationRequest import OperationRequest
from lwm2m_lib.data_model.ResourcesList import CommonLists
from lwm2m_lib.api import lwm2m_api
from lwm2m_lib.operations.EventDispatcher import Event
import threading
from time import sleep
import datetime
from futile.logging import LoggerMixin

class GeneralObservationInformation(object):
    def __init__(self, listener_ip, listener_port, token_id):
        self.listener_ip = listener_ip
        self.listener_port = listener_port
        self.token_id = token_id

class SpecificObservationInformation(object):
    
    def __init__(self, local_ip, local_port):
        self.local_ip = local_ip
        self.local_port = local_port
        self.specific_observers = {}
    
    def add_observation(self, token_id):
        initial_time = datetime.datetime.now()
        self.specific_observers.update({
            token_id : {"initial_time" : initial_time}
        })
    
     
class ObservationNotificationEngine(OperationRequest):  
    """ note: Observation has to be done starting from client_name/object_id"""
    
    def __init__(self, lwm2m_resources, dispatcher=None):
        self.lwm2m_resources = lwm2m_resources
        self.objects_list = []
        self.dispatcher = dispatcher 
        self.observe_token_dict = {}
        super(ObservationNotificationEngine, self).__init__()
    
    def forward_request(self, path, remote, observe_value, server_ip, server_port, app_ip, app_port, token, client_port):
        """ Forwards the Observation/Cancel Observation requests """
        
        self.logger.info("Forwarding the Observation Request")
        request = lwm2m_api()
        
        payload = {"server_ip" : server_ip, "server_port" : server_port, "app_ip" : app_ip, "app_port" : app_port}
        content_type = "application/json"
        
        endpoint_name, object_id, object_inst_id, res_id, res_inst_id, \
                            _, _ = self.find_elements(path, remote)
        endpoint = self.lwm2m_resources.return_endpoint_object(endpoint_name=endpoint_name)
        if endpoint is not None:
            listener_ip = endpoint.listener_ip
            listener_port = endpoint.listener_port
            if (listener_ip and listener_port) is not None:
                if observe_value == 0:
                    response = request.send_observe_request(listener_ip, listener_port, app_ip, app_port, endpoint_name, \
                                        object_id, observe_value, payload=payload, object_inst_id=object_inst_id, \
                                        res_id=res_id, res_inst_id=res_inst_id, content_type=content_type, token=token, \
                                        client_port=client_port)
                    return response
                elif observe_value == 1:
                    response = request.send_observe_request(listener_ip, listener_port, app_ip, app_port, endpoint_name, \
                                        object_id, observe_value, payload=payload, object_inst_id=object_inst_id, \
                                        res_id=res_id, res_inst_id=res_inst_id, content_type=content_type, token=token, \
                                        client_port=client_port)
                    return response
            else:
                response = None
            return response
    
    
    def set_observation(self, endpoint_name, object_id, object_inst_id, res_id, token_id, payload, server_ip, server_port, res_inst_id=0):
        object_id_object_inst_id = str(object_id) + "_" + str(object_inst_id)
        res_id_res_inst_id = str(res_id) + "_" + str(res_inst_id)
        resource_object = self.lwm2m_resources.endpoint_dict[endpoint_name]["object"].objects_dict[object_id_object_inst_id]["object"].resources_id_dict[res_id_res_inst_id]["object"]
        resource_object.observe_info.add_observation(token_id)
        
        listener_object = ResourceListenerNotifier(self.lwm2m_resources, self.dispatcher, endpoint_name, object_id, object_inst_id, res_id, res_inst_id, token_id, payload, server_ip, server_port)
        self.objects_list.append(listener_object)
    
    def cancel_observation(self, endpoint_name, object_id, object_inst_id, res_id, token_id, payload, server_ip, server_port, res_inst_id=0):
        object_id_object_inst_id = str(object_id) + "_" + str(object_inst_id)
        observer_ip = loads(payload)["app_ip"]
        observer_port = int(loads(payload)["app_port"])
        obj_removed = False
        underscore_str = "_"
        res_list = (object_id_object_inst_id, str(res_id), str(res_inst_id))
        event_name = underscore_str.join(res_list)
        
        for obj in self.objects_list:
            if obj.observer_ip == observer_ip and obj.observer_port == observer_port:
                result = obj.remove_listener(event_name)
                if not result:
                    continue
                message = "Observation Cancelled Successfully"
                self.logger.info(message)
                self.objects_list.remove(obj)
                del obj
                obj_removed = True
                break
        if not obj_removed:
            message = "Information don't match !! Invalid Cancel Observation Request"
            self.logger.info(message)
        return message
        

class ResourceListenerNotifier(OperationRequest):
    
    def __init__(self, lwm2m_resources, event_dispatcher, endpoint_name, object_id, object_inst_id, res_id, res_inst_id, token_id, payload, server_ip, server_port):
        self.lwm2m_resources = lwm2m_resources
        self.event_dispatcher = event_dispatcher
        self.observer_ip = loads(payload)["app_ip"]
        self.observer_port = int(loads(payload)["app_port"])
        self.server_ip = server_ip
        self.server_port = server_port
        self.token_id = token_id
        
        object_id_object_inst_id = str(object_id) + "_" + str(object_inst_id)
        underscore_str = "_"
        res_list = (object_id_object_inst_id, str(res_id), str(res_inst_id))
        event_name = underscore_str.join(res_list)
        self.event_dispatcher.add_event_listener(event_name, self.notify)
    
    def remove_listener(self, event_name):
        result = self.event_dispatcher.remove_event_listener(event_name, self.notify)
        return result
    
    def notify(self, event):
        
        for element1, element2 in event.data.iteritems():
           object_id_object_inst_id = element1
           endpoint_name = element2["endpoint_name"]
           for element3, element4 in element2["resources"].iteritems():
               res_id = element3
               res_value = element4["res_value"]
               res_inst_id = element4["res_inst_id"]
       
        if res_inst_id == "" or res_inst_id == None:
            res_inst_id = 0
        
        res_id_res_inst_id = str(res_id) + "_" + str(res_inst_id)

        resource_object = self.lwm2m_resources.endpoint_dict[endpoint_name]["object"].objects_dict[object_id_object_inst_id]["object"].resources_id_dict[res_id_res_inst_id]["object"]
        client_ip = resource_object.observe_info.local_ip
        client_port = resource_object.observe_info.local_port
        last_time = datetime.datetime.now() - resource_object.observe_info.specific_observers[self.token_id]["initial_time"]
        #ToDO: rsh: deal with hours, minutes too
        self.logger.info("Sending Notification after %s sec", last_time.seconds)

        payload = {
            endpoint_name : {object_id_object_inst_id : {"resources" : {res_id_res_inst_id : res_value}}},
            "observer_ip" : self.observer_ip,
            "observer_port" : self.observer_port
        }
        content_type = "application/json"
        request = lwm2m_api()
        response = request.send_notification(self.server_ip, self.server_port, self.token_id, payload, content_type=content_type, time_elapse=last_time.seconds, client_ip=client_ip, client_port=client_port)
        

class ResourceEventHandler(LoggerMixin):
    def __init__(self, event_dispatcher):
        self.event_dispatcher = event_dispatcher
        
        self.event_dispatcher.add_event_listener("send_reply", self.send_response)
    
    def resource_notification(self, res_info):
        result = self.event_dispatcher.dispatch_event(Event("send_reply", res_info))
        return result
    
    def send_response(self, event):
        
        for element1, element2 in event.data.iteritems():
            object_id_object_inst_id = element1
            for element3, element4 in element2["resources"].iteritems():
                res_id = element3
                res_value = element4["res_value"]
                res_inst_id = element4["res_inst_id"]
        
        if res_inst_id == "" or res_inst_id == None:
            res_inst_id = 0
        
        underscore_str = "_"
        res_list = (object_id_object_inst_id, str(res_id), str(res_inst_id))
        event_name = underscore_str.join(res_list)

        result = self.event_dispatcher.dispatch_event(Event(event_name, event.data))
        return result
        

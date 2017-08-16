from futile.logging import LoggerMixin
from openmtc_etsi.model import Scl, Application, Subscription, MgmtObj, \
                AttachedDevice, Parameters, MgmtCmd, ContentInstance, Container
from openmtc_etsi.scl import CreateRequestIndication, RetrieveRequestIndication, UpdateRequestIndication
from lwm2m_lib.data_model.mgmt_objects import lwm2m_reverse_dict_objects, lwm2m_dict_objects
from base64 import b64decode
from json import dumps, loads
import threading
from gevent.coros import Semaphore
from LocalClientCore import LocalClientCore
from time import sleep
from random import randint


class M2M_Device_Gateway_DM_Adapter(LoggerMixin):
    def __init__(self, events, config, api, client):
        
        self.events = events
        self.config = config
        self.api = api
        self.client = client
        
        self.clients_collection = {}
        self.gscl_collection = {}
        self.sem = Semaphore()
        self.sem_counter = 0
        self.events.resource_created.register_handler(self._handle_scl_created, Scl)
        self.events.resource_created.register_handler(self._handle_mgmtobj_created, MgmtObj)
        self.events.resource_created.register_handler(self._handle_mgmtcmd_created, MgmtCmd)
        self.events.resource_updated.register_handler(self._handle_mgmtobj_updated, MgmtObj)
        self.events.resource_created.register_handler(self._handle_attached_device_created, AttachedDevice)
    
    def _handle_scl_created(self, instance, request_indication):
        gscl_name = instance.path.split("/")[-1]
        if gscl_name != "nscl":
            self.create_scl_client(gscl_name)
    
    def create_scl_client(self, gscl_name):
        self.sem.acquire()
        self.sem_counter += 1
        sem_counter = self.sem_counter
        self.sem.release()
        
        local_listener_port = self.config["local_listener_port"] + sem_counter
        local_client_port = self.config["local_client_port"] + sem_counter
        
        dm_client = self.client.create_client(local_listener_port, local_client_port)
        if dm_client is not None:
            self.gscl_collection[gscl_name] = dm_client
            dm_client.load_dm_adapter(self)
            self.client.do_registration(gscl_name)
        else:
            self.client.do_registration(gscl_name, status=True, cb=self.load_elements)
    
    def load_elements(self, endpoint_name, dm_client_object):
        self.gscl_collection[endpoint_name] = dm_client_object
        dm_client_object.load_dm_adapter(self)
    
    def load_elements1(self, endpoint_name, dm_client_object):
        self.clients_collection[endpoint_name] = dm_client_object #self.gscl_collection[instance.path.split("/")[3]]
        
    def _handle_attached_device_created(self, instance, request_indication):
        
        #self.sem.acquire()
        self.sem_counter += 1
        sem_counter = self.sem_counter
        #self.sem.release()
        generate_endpoint = instance.path.split("/")[3:]
        endpoint_name = "/".join(generate_endpoint)
        local_client_port = self.config["local_client_port"] + sem_counter
        try:
            self.clients_collection[endpoint_name] = self.gscl_collection[instance.path.split("/")[3]]
            self.client.do_registration(endpoint_name, local_client_port=local_client_port)
        except KeyError:
            self.client.do_registration(endpoint_name, local_client_port=local_client_port, status=True, cb=self.load_elements1)
        
        
    def _handle_mgmtobj(self, dm_client, endpoint_name, instance, request_indication):
        send_update_flag = False
        object_and_resources = {}
        resources = {}
        path = instance.path
        resource = request_indication.resource
        #get object name and resource name
        mgmt_obj_name = path.split("/")[-1]
        
        self.logger.debug("endpoint_name: %s", endpoint_name)
        self.logger.debug("management object %s was added" % (mgmt_obj_name))
        lwm2m_mgmt_obj = lwm2m_reverse_dict_objects[mgmt_obj_name.split("_")[0]]
        lwm2m_mgmt_obj_inst_id = mgmt_obj_name.split("_")[1] 
        if lwm2m_mgmt_obj is not None:
            lwm2m_mgmt_obj_id = lwm2m_mgmt_obj["object_id"]
            self.logger.debug("flex values are "+str(instance.flex_values))
            for param_name, param_value in instance.flex_values.items():
                self.logger.debug("param name [%s] and param value [%s]" % (param_name, param_value))
                lwm2m_resource_id = lwm2m_mgmt_obj["resource_list"][param_name.split("_")[0]]["resId"]
                if lwm2m_mgmt_obj["resource_list"][param_name.split("_")[0]]["multiInst"]:
                    lwm2m_resource_id_inst = param_name.split("_")[1]
                else:
                    lwm2m_resource_id_inst = ""
                resource_change_flag = dm_client.add_resource(endpoint_name, lwm2m_mgmt_obj_id, \
                                        lwm2m_resource_id, param_value, lwm2m_mgmt_obj_inst_id=lwm2m_mgmt_obj_inst_id)
                
                if resource_change_flag:
                    send_update_flag = True
                resources.update({
                    lwm2m_resource_id : {"res_inst_id" : lwm2m_resource_id_inst, "res_value" : param_value}
                })
                    
            object_and_resources = {
                str(lwm2m_mgmt_obj_id) + "_" + str(lwm2m_mgmt_obj_inst_id) : {"resources" : resources}
            }
            mgmt_obj_id_inst_id = str(lwm2m_mgmt_obj_id) + "_" + str(lwm2m_mgmt_obj_inst_id)
            return mgmt_obj_id_inst_id, object_and_resources, send_update_flag 
        else:
            self.logger.error("could not find management object for management object name %s" % (mgmt_obj_name))
            return None
    
    
    def create_mgmtobj_dict(self, endpoint_name, instance, request_indication):
        send_update_flag = False
        object_and_resources = {}
        resources = {}
        path = instance.path
        resource = request_indication.resource
        mgmt_obj_name = path.split("/")[-1]
        
        lwm2m_mgmt_obj = lwm2m_reverse_dict_objects[mgmt_obj_name.split("_")[0]]
        lwm2m_mgmt_obj_inst_id = mgmt_obj_name.split("_")[1] 
        if lwm2m_mgmt_obj is not None:
            lwm2m_mgmt_obj_id = lwm2m_mgmt_obj["object_id"]
            for param_name, param_value in instance.flex_values.items():
                lwm2m_resource_id = lwm2m_mgmt_obj["resource_list"][param_name.split("_")[0]]["resId"]
                if lwm2m_mgmt_obj["resource_list"][param_name.split("_")[0]]["multiInst"]:
                    lwm2m_resource_id_inst = param_name.split("_")[1]
                else:
                    lwm2m_resource_id_inst = ""
                
                resources.update({
                    lwm2m_resource_id : {"res_inst_id" : lwm2m_resource_id_inst, "res_value" : param_value}
                })
                    
            object_and_resources = {
                str(lwm2m_mgmt_obj_id) + "_" + str(lwm2m_mgmt_obj_inst_id) : {"resources" : resources}
            }
            mgmt_obj_id_inst_id = str(lwm2m_mgmt_obj_id) + "_" + str(lwm2m_mgmt_obj_inst_id)
            return mgmt_obj_id_inst_id, object_and_resources
        else:
            self.logger.error("Could not find management object name %s" % (mgmt_obj_name))
            return None
    
    
    def _handle_mgmtobj_created(self, instance, request_indication):
        generate_endpoint = instance.path.split("/")[3:-2]
        endpoint_name = "/".join(generate_endpoint)
        if endpoint_name == "":
            endpoint_name = self.config["global"]["scl_id"]
            if not self.gscl_collection.has_key(endpoint_name):
                if not any(self.gscl_collection):
                    self.create_scl_client(endpoint_name)
                else:
                    for _, obj in self.gscl_collection.iteritems():
                        self.gscl_collection[endpoint_name] = obj
                        self.sem_counter += 1
                        sem_counter = self.sem_counter
                        local_client_port = self.config["local_client_port"] + sem_counter
                        self.client.do_registration(endpoint_name, local_client_port=local_client_port)
                        break
        try:
            dm_client = self.clients_collection[endpoint_name]
        except KeyError:
            try:
                dm_client = self.gscl_collection[endpoint_name]
            except KeyError:
                self.logger.error("Error while creating mgmtObj!! Endpoint mayn't be registered. Storing MgmtObj contents")
                self.logger.debug("%s, %s", instance.path, endpoint_name)
                mgmt_obj_id_inst_id, object_and_resources = self.create_mgmtobj_dict(endpoint_name, instance, request_indication)
                self.client.store_mgmtobj(endpoint_name, mgmt_obj_id_inst_id, object_and_resources)
                return
        mgmt_obj_id_inst_id, object_and_resources, send_update_flag = self._handle_mgmtobj(dm_client, endpoint_name, instance, request_indication)
        if object_and_resources is not None:
            self.logger.info("Sending add resource updates from gateway(create) to client")
            response = dm_client.send_add_resources(object_and_resources, endpoint_name, mgmt_obj_id_inst_id)
        else:
            self.logger.info("Not sending add resource updates from gateway(create) to client")
            
    def _handle_mgmtcmd_created(self, instance, request_indication):
        path =  instance.path
        return
    
    def _handle_mgmtobj_updated(self, instance, request_indication):
        generate_endpoint = instance.path.split("/")[3:-2]
        endpoint_name = "/".join(generate_endpoint)
        
        if endpoint_name == "":
            endpoint_name = self.config["global"]["scl_id"]
        
        try:
            dm_client = self.clients_collection[endpoint_name]
        except KeyError:
            try:
                dm_client = self.gscl_collection[endpoint_name]
            except KeyError:
                self.logger.error("Error while updating mgmtObj!! Endpoint mayn't be registered. Storing MgmtObj contents")
                self.logger.debug("%s, %s", instance.path, endpoint_name)
                mgmt_obj_id_inst_id, object_and_resources = self.create_mgmtobj_dict(endpoint_name, instance, request_indication)
                self.client.store_mgmtobj(endpoint_name, mgmt_obj_id_inst_id, object_and_resources)
                return
        mgmt_obj_id_inst_id, object_and_resources, send_update_flag = self._handle_mgmtobj(dm_client, endpoint_name, instance, request_indication)
        if object_and_resources is not None and send_update_flag:
            self.logger.info("Sending add resource updates from gateway(update) to client")
            response = dm_client.send_add_resources(object_and_resources, endpoint_name, mgmt_obj_id_inst_id)
        else:
            self.logger.info("Not sending add resource updates from gateway(udpate) to client!! Already has updated information")
    
    def update_resources(self, endpoint_name, object_id, object_inst_id, payload, content_type=None):
        """ Push the resouces change/update on the gateway resource tree """
        
        self.logger.info("Updating the Gateway Resource Tree")
        resource_dict = {}
        resources = loads(payload)
        object_id_object_inst_id = str(object_id) + "_" + str(object_inst_id)
        
        object_name = lwm2m_dict_objects[str(object_id)]["object_name"]
        object_name_obj_inst_id = object_name + "_" + str(object_inst_id)
        for res_id, res in resources.iteritems():
            res_name = lwm2m_dict_objects[str(object_id)]["resource_list"][str(res_id)]["resName"]
            if lwm2m_dict_objects[str(object_id)]["resource_list"][str(res_id)]["multiInst"]:
                res_name_res_inst_id = res_name + "_" + res["res_inst_id"]
            else:
                res_name_res_inst_id = res_name
            res_value = res["res_value"]
            resource_dict.update({
                res_name_res_inst_id : res_value
            })
        
        def success(result):
           self.logger.info("Resource Tree is updated")
        
        def failure(result):
            self.logger.error("Error occurred: %s", result)
        
        def error_handling(result):
            path = "/m2m/scls/mgmtObjs/" + object_name_obj_inst_id
            self.logger.warning("Path not found. %s", result)
            self.logger.info("Looking for other path at %s", path)
            resource = ('{"mgmtObjs" : ' + dumps(resource_dict) + '}')
            request = UpdateRequestIndication(path, resource, content_type="application/json")
            response = self.api.handle_request_indication(request)
            response.then(success, failure)
        
        path = "/m2m/scls/" + endpoint_name + "/mgmtObjs/" + object_name_obj_inst_id
        
        resource = ('{"mgmtObjs" : ' + dumps(resource_dict) + '}')
        request = UpdateRequestIndication(path, resource, content_type="application/json")
        response = self.api.handle_request_indication(request)
        response.then(success, error_handling)
        
        
        
        

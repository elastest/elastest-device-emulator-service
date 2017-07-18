from openmtc_server.Plugin import Plugin
from LocalClientCore import LocalClientCore
from M2M_Device_Gateway_DM_Adapter import M2M_Device_Gateway_DM_Adapter
from openmtc_gevent.GEventNetworkManager import GEventNetworkManager, Interface
from StoreAndForward import StoreAndForward
from copy import deepcopy

class lwm2m_dm_client(Plugin):
    def _init(self, ):
        self.init_parameters()
        
        self.dm_adapter = M2M_Device_Gateway_DM_Adapter(self.events, self.config, self.api, self)
        self.api.events.interface_created.register_handler(self._handle_interface_created)
        self.store_and_forward = StoreAndForward()
        self.multiple_trigger = True
        self.ep_location_mapping = {}
        self._initialized()
    
    def interfaces_list(self, result):
                
        self.logger.debug("Total Interfaces: %s", result)
        interface_exist = False
        
        for int_info in result:
            if int_info.name not in self.blacklist_interfaces and int_info.name != "lo":
                try:
                    for addr_list in int_info.addresses:
                        if addr_list.family == 2: 
                            self.local_listener_ip = addr_list.address 
                            self.local_client_ip = addr_list.address
                            self.store_and_forward.enabled = False
                            break
                except IndexError:
                    continue
       
    
    def _start(self, ):
        
        self.api.networkmanager.get_interfaces().then(self.interfaces_list)
        self._started()
    
    def _stop(self, ):

        self._stopped()
    
    def _handle_interface_created(self, ip_info):
        if self.multiple_trigger:
            self.multiple_trigger = False
            return

        interface_name = ip_info.name
        for addr_list in ip_info.addresses:
            if addr_list.family == 2:
                interface_ip = addr_list.address
                break

        self.logger.info("New Interface Found !!")
        self.logger.info("Interface name %s", interface_name)
        self.logger.info("Interface IP %s", interface_ip)
        if interface_ip != "lo":
            if self.store_and_forward.enabled and not hasattr(self, "dm_client"):
                self.handle_store_forward(interface_ip)
                
            else:
                # Stopping the Listener Server
                self.dm_client.stop_server()
                # Creating the Listener Server with new ip info
                self.dm_client.create_server(interface_ip)
                # Updating newly detected IP in local domain
                for local_endpoint, registered_location in self.ep_location_mapping.iteritems():
                    local_endpoint.listener_ip = interface_ip
                    local_endpoint.local_ip = interface_ip
                    # Sending updated IP info to LWM2M DM server
                    self.dm_client.registration.send_update_registration(registered_location, local_endpoint.unique_id, \
                                                None, self.lwm2m_server_ip, self.lwm2m_server_port)
        
        
    
    def init_parameters(self, ):
        """ Reads the configuration file to set LWM2M Server and Client Address(ip:port)
        and other few parameters/resources.
        """

        self.lwm2m_server_ip = self.config["lwm2m_dm_server_ip"]
        self.lwm2m_server_port = self.config["lwm2m_dm_server_port"]
        self.blacklist_interfaces = self.config["blacklist_interfaces"]
        self.life_time = self.config["resources"]["life_time"]
        self.version = self.config["resources"]["version"]
        self.sms_num = self.config["resources"]["sms_num"]
        self.binding = self.config["resources"]["binding"]
        
    
    def create_client(self, local_listener_port, local_client_port):
        self.local_listener_port = local_listener_port
        self.local_client_port = local_client_port
        
        if not hasattr(self, "local_listener_ip"):
            self.logger.warning("Not connected to active Network !! Store-and-Forward for client enabled")
            return None
        else:
            self.logger.info("Connected to a Network !!")

        self.dm_client = LocalClientCore(self.local_listener_ip, local_listener_port,
                                self.lwm2m_server_ip, self.lwm2m_server_port,
                                self.local_client_ip, local_client_port)
        self.dm_client.create_server()
        return self.dm_client
    
    def do_registration(self, endpoint_name, local_client_port=None, status=False, cb=None):
        if local_client_port is not None:
                self.local_client_port = local_client_port
        if status:
            self.store_and_forward.store_endpoints(endpoint_name)
            self.store_and_forward.store_reg_parameters(endpoint_name)
            self.store_and_forward.r_params[endpoint_name].store_reg_params(life_time=self.life_time, version=self.version, \
                                        sms_num=self.sms_num, binding=self.binding)
            self.store_and_forward.store_ip_ports(endpoint_name)
            self.store_and_forward.ip_ports[endpoint_name].store_ip_info(lwm2m_dm_server_ip=self.lwm2m_server_ip, lwm2m_dm_server_port=self.lwm2m_server_port, \
                                        local_listener_ip=None, local_listener_port=self.local_listener_port, \
                                        local_client_ip=None, local_client_port=self.local_client_port)
            self.store_and_forward.cb[endpoint_name] = cb
        else:
            self.dm_client.load_registration_params(self.life_time, self.version, self.sms_num, self.binding)
            local_endpoint, registered_location = self.dm_client.local_registration(endpoint_name, self.local_client_port)
    
            self.ep_location_mapping[local_endpoint] = registered_location
            
            
    def store_mgmtobj(self, endpoint_name, mgmt_obj_id_inst_id, object_and_resources):
        self.store_and_forward.store_mgmtobjs(endpoint_name, mgmt_obj_id_inst_id, object_and_resources)
        

    def handle_store_forward(self, interface_ip):
        self.local_listener_ip = interface_ip
        self.local_client_ip = interface_ip
        self.dm_client = LocalClientCore(self.local_listener_ip, self.local_listener_port,
                        self.lwm2m_server_ip, self.lwm2m_server_port,
                        self.local_client_ip, self.local_client_port)
        if any(self.store_and_forward.endpoints):
            ep_set = deepcopy(self.store_and_forward.endpoints)
            for ep_name in ep_set:
                if any(self.store_and_forward.r_params[ep_name].reg_params):
                    r_params = self.store_and_forward.r_params[ep_name].reg_params
                    self.dm_client.load_registration_params(r_params["life_time"], r_params["version"], r_params["sms_num"], r_params["binding"])
                    del self.store_and_forward.r_params[ep_name]
                    ip_port = self.store_and_forward.ip_ports[ep_name].all_ip_ports
                    local_endpoint, registered_location = self.dm_client.local_registration(ep_name, ip_port["local_client_port"])
                    self.ep_location_mapping[local_endpoint] = registered_location
                    self.store_and_forward.cb[ep_name](ep_name, self.dm_client)
                    del self.store_and_forward.ip_ports[ep_name]
                    del self.store_and_forward.cb[ep_name]
                    # Handling saved management objects
                    if self.store_and_forward.mgmtobj_infos.has_key(ep_name):
                        self.logger.info("Adding stored management objects and resources locally for %s", ep_name)
                        temp_mgmtobj = deepcopy(self.store_and_forward.mgmtobj_infos[ep_name])
                        for object_id_inst_id, contents in temp_mgmtobj.iteritems():
                            for obj_id_inst_id, resources in contents.iteritems():
                                obj_id = obj_id_inst_id.split("_")[0]
                                obj_inst_id = obj_id_inst_id.split("_")[1]
                                for res_id, res in resources["resources"].iteritems():
                                    self.dm_client.add_resource(ep_name, obj_id, res_id, res["res_value"], lwm2m_mgmt_obj_inst_id=obj_inst_id)
                                    del self.store_and_forward.mgmtobj_infos[ep_name][object_id_inst_id][obj_id_inst_id]["resources"][res_id]
                                if not any(self.store_and_forward.mgmtobj_infos[ep_name][object_id_inst_id][obj_id_inst_id]["resources"]):
                                    del self.store_and_forward.mgmtobj_infos[ep_name][object_id_inst_id][obj_id_inst_id]["resources"]
                            if not any(self.store_and_forward.mgmtobj_infos[ep_name][object_id_inst_id][obj_id_inst_id]):
                                del self.store_and_forward.mgmtobj_infos[ep_name][object_id_inst_id][obj_id_inst_id]
                            if not any(self.store_and_forward.mgmtobj_infos[ep_name][object_id_inst_id]):
                                del self.store_and_forward.mgmtobj_infos[ep_name][object_id_inst_id]
                        if not any(self.store_and_forward.mgmtobj_infos[ep_name]):
                                del self.store_and_forward.mgmtobj_infos[ep_name]
                        self.logger.info("Sending stored management objects and resources")            
                        for mgmt_obj_id_inst_id, object_and_resources in temp_mgmtobj.iteritems():
                            self.dm_client.send_add_resources(object_and_resources, ep_name, mgmt_obj_id_inst_id)
                self.store_and_forward.endpoints.remove(ep_name)
        self.store_and_forward.enabled = False

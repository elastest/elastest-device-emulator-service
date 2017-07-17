from openmtc_server.Plugin import Plugin
from DMServerCore import DMServerCore

class lwm2m_dm_server(Plugin):
    def _init(self, ):
        #self.api.events.lwm2m_dm_m2m_resource_updated.register_handler(self._handle_internal_update_trigger)
        self._initialized()
    
    def _start(self, ):
        self.initial_parameters()
        self.start_dm_server()
        
        self._started()
    
    def _stop(self, ):
        self.stop_dm_server()
        self._stopped()
        
    def initial_parameters(self, ):
        """ Reads the configuration file for ip and port information of the LWM2M DM Server """
        
        self.lwm2m_dm_server_ip = self.config["lwm2m_dm_server_ip"]
        self.lwm2m_dm_server_port = self.config["lwm2m_dm_server_port"]
        self.client_ip = self.config["client_ip"]
        self.client_port = self.config["client_port"]
        
    
    def start_dm_server(self, ):
        """ Starts the LWM2M DM Server """
        
        self.dm_server = DMServerCore(self.lwm2m_dm_server_ip, self.lwm2m_dm_server_port,
                                      self.client_ip, self.client_port)
        self.dm_server.create_server()

        self.logger.info("LWM2M DM Server Started")
    
    def stop_dm_server(self, ):
        """ Stops the LWM2M DM Server """
        
        self.dm_server.stop_server()
        self.logger.info("LWM2M DM Server Stopped")
        
    def _handle_internal_update_trigger(self):
        pass
    


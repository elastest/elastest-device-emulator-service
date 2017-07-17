
#Session Service Class:
#session identifier
#session credentials
#session descriptor (e.g. device identifiers, type of participant, 
    #services that the participant supports, interface requirements of the participant, type of compression used)
#session routing information
#session context/history: 
#session policies: session routing policies, session store-and-forward policies, session access control policies

import time
#import network_service.UnderlyingNetworkSession as UnderlyingNetworkSession
from UnderlyingNetworkSession import UnderlyingNetworkSession
from UnderlyingNetwork_SessionManager import UnderlyingNetwork_SessionManager


class Service_Session(object):
    #identifier
    def __init__(self, device_id, participant_type, logger, db_config):
        self.identifier=self.create_new_identifier(device_id)
        self.device_id = device_id
        self.participant_type = participant_type
        self.db_config = db_config
        self.logger = logger
        
    def get_id(self):
        return self.identifier
    
    def get_device_id(self):
        return self.device_id
        
    def create_new_identifier(self, device_id):
        return device_id+"_"+str(int(time.time()))
       
    def save_to_db(self):
        #TODO: aon: how to integrate with the db module?
        return
    def print_session(self):
        self.logger.info("Service Session Id "+self.identifier)
    
class Service_Session_CSE_AE(Service_Session):
    
    def __init__(self, device_id, participant_type, 
                 subscr_id, ip_address, 
                 app_id, logger, 
                 db_config, unet_manager):
        super(Service_Session_CSE_AE, self).__init__(device_id, participant_type, 
                                                     logger, db_config)
        self.identifier += "_"+app_id
        self.subscr_id = subscr_id
        self.ip_address_list = []
        self.unet_session = None
        if ip_address:
            self.ip_address_list.append(ip_address)
        self.app_id = app_id
        self.unet_manager = unet_manager
        self.not_yet_checked_ips = []
        self.resource_path = None
    
    def get_app_id(self):
        return self.app_id
        
    def add_ip_address(self, ip_address):
        if ip_address in self.ip_address_list:
            return 0
        else:
            self.ip_address_list.append(ip_address)
            return 1    
        
    def print_session(self):
        self.logger.info("Service Session Id ["+self.identifier)
        self.logger.info("]Device Id is ["+self.device_id+
                         "] Subscriber Id ["+str(self.subscr_id)+
                         "] IP Address list ["+str(self.ip_address_list)+"] App Id ["+self.app_id+"]")
        if self.unet_session:
            self.logger.info("Underlying network sessions:")
            self.unet_session.print_session()
        self.logger.info("----------------------------------")
    
    def network_callback(self, event_info):
        #received event information and Json object
        event_type = event_info["event_type"]
        if event_type=='loss_of_bearer':
            self.logger.warn("the device disconnected")
        elif event_type=='recovery_of_bearer':
            self.logger.warn("the device disconnected")
        elif event_type=='release of bearer':
            self.logger.warn("the device disconnected")
        elif event_type=='successful_resource_allocation':
            self.logger.warn("the network session was established and resources were allocated")
        elif event_type=='failed_resource_allocation':
            self.logger.warn("the network session was established but resources were not successfully allocated")
        elif event_type=='charging_correlation_and_exchange':
            self.logger.warn("the network session network level charging information was received")
        else:
            self.logger.warn("the session got an event "+event_type)
        self.logger.info("network session status is "+self.underlying_network_sess.getStatus())
        self.save_to_db()
            
    def add_ip_underlying_network_sess(self, ip_address, duration, 
                                       media_descr, ott_api):
        self.logger.info("\n\n\n\ninitiate underlying network session for session id "+self.identifier+" and ip address "+ip_address)
        #self.underlying_network_sess = UnderlyingNetworkSession()
        if not self.unet_session:
            self.unet_session = self.unet_manager.add_unet_session(self.device_id, self.subscr_id, 
                                                                   ip_address, self.app_id, 
                                                                   duration, media_descr, 
                                                                   ott_api, self)
            if not self.unet_session:
                raise Exception("underlying network session could not be created")
            self.unet_session.initiate()
        elif self.unet_session.get_state() == "Open":
            self.unet_session.process_new_registered_ip_address(ip_address)
        elif self.unet_session.get_state() != "Open":
            self.not_yet_checked_ips.append(ip_address)
        return
    
    def unet_session_terminated(self, unet_session):
        if self.unet_session == unet_session:
            self.unet_session = None
        else:
            return
        #very strange code
        '''
        if len(self.not_yet_checked_ips) > 0:
            self.unet_session = self.unet_manager.add_unet_session(self.device_id, self.subscr_id, 
                                                                   self.not_yet_checked_ips[0], 
                                                                   self.app_id,
                                                                   None, None, 
                                                                   self)
            if not self.unet_session:
                raise Exception("underlying network session could not be created")
            self.unet_session.initiate()
            #remove first element
            self.not_yet_checked_ips = self.not_yet_checked_ips[1:]
        '''
    def terminate_unet_session(self):
        if self.unet_session:
            self.unet_session.terminate_epc_rx_session()
            
    def remove_ip_underlying_network_sess(self, ip_address):
        return 
    
    def set_resource(self, path, resource):
        self.resource_path = path
        self.resource_data = resource

        
      
        
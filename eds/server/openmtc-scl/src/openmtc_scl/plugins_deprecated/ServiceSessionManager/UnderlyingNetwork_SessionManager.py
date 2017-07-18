import json
import time
from aplus import Promise

from UnderlyingNetworkSession import UnderlyingNetworkSession
try:
    from core.event_bus import EventBus
except ImportError:
    EventBus = None

class UnderlyingNetwork_Session_Not_Found(Exception):
    pass

global unet_sess_manager_dict_sessions
unet_sess_manager_dict_sessions={}

def find_session_by_session_id(unet_session_id):
    try:
        session = unet_sess_manager_dict_sessions[unet_session_id]
        return session
    except KeyError:
        raise UnderlyingNetwork_Session_Not_Found("underlying session for session id "+unet_session_id+" was not found")

def rx_callback_handler(message):
    print message.body
    print "\n\n\nrx_callback_handler: message is "+str(message.body)+"\n\n\n"
    try:
        session_id = message.body["ReferenceId"]
        session = find_session_by_session_id(session_id)
        session.process_epc_event(message.body)
    except KeyError:
        print "message body "+str(message.body)+" has no key ReferenceId"
    except UnderlyingNetwork_Session_Not_Found:
        print "session for session id "+session_id+" was not found"
        return
    return

class UnderlyingNetwork_SessionManager:
    
    DEF_EVENT_BUS_EPC_Rx_CALLBACK_ADDRESS = "org.openmtc.network_service.underlying_network_session.epc_rx"
    
    def __init__(self, logger, epc_db_info, shelve_name):
        self.dict_sessions = unet_sess_manager_dict_sessions
        self.logger = logger
        self.db_config = epc_db_info
        self.epc_shelve_name = shelve_name 
        self.epc_shelve = None
        #self.db_config_apply()
    
    def _load_epc_id(self, shelve):
        
        #self.logger.info("\n>>>>>>>>>>>db config is %s",self.db_config)
        self.epc_shelve = shelve          
        for pair in self.db_config:
            #self.logger.info("gscl id is "+str(pair["gsclId"])+" epc id is  "+str(pair["epc_id"]))
            self.epc_shelve.setitem(str(pair["gsclId"]), pair["epc_id"])
        #self.logger.info("added epc ids in the shelve")
        
    def get_def_bearer_media_descr(self, ip_address):
        flow_list=[]
        '''flow_up={      'MAX_DL':2000,
                       'MAX_UL':2000,
                       'MediaType':'application', 
                       'FlowStatus':'enabled',
                       'Src_IP':ip_address,
                       'Dst_IP':'0.0.0.0',
                       'Protocol':'ip',
                       }
    
        flow_down={    'MAX_DL':2000,
                       'MAX_UL':2000,
                       'MediaType':'application', 
                       'FlowStatus':'enabled',
                       'Src_IP':'0.0.0.0',
                       'Dst_IP':ip_address,
                       'Protocol':'ip',
                       }
        flow_list.append(flow_up)
        flow_list.append(flow_down)
        self.logger.info("flow list is %s" %(str(flow_list)))'''
        return flow_list
    
    def get_epc_subscription_id(self, endpointId):
        #TODO: add DB search
        if self.epc_shelve is not None:
            return self.epc_shelve.getitem(endpointId)
        else: 
            return Promise().reject(reason="UnderlyingNetwork_SessionManager: epc id shelve not found")
        
    def event_bus_reg(self):
  
        if EventBus:
            EventBus.register_handler(self.DEF_EVENT_BUS_EPC_Rx_CALLBACK_ADDRESS, handler = rx_callback_handler)
            
    def find_session_by_session_id(self, unet_session_id):
        
        if unet_session_id in self.dict_sessions.keys():
            session = self.dict_sessions[unet_session_id]
            return session
        else:
            raise UnderlyingNetwork_Session_Not_Found("underlying session for session id "+unet_session_id+" was not found")
    
    def find_session_by_device_id(self, device_id, app_id):
        
        if device_id in self.dict_sessions.keys():
            session_list = self.dict_sessions[device_id]
            if not session_list:
                raise UnderlyingNetwork_Session_Not_Found("underlying network session for device id "+device_id+" and app_id "+app_id+" was not found")
            for session in session_list:
                if app_id in session.get_id():
                    self.logger.info("found unet session for device %s and app id %s in session with id %s" %(device_id, app_id, session.get_id))
                    return session
        
        raise UnderlyingNetwork_Session_Not_Found("underlying network session for device id "+device_id+" and app_id "+app_id+" was not found")
        
    
    def save_locally(self, session):
        
        device_id= session.get_device_id()
        if device_id in self.dict_sessions.keys():
            list = self.dict_sessions[device_id]
        else:
            list=[]
        list.append(session)
        self.dict_sessions[device_id] = list
        self.dict_sessions[session.get_id()] = session
        self.logger.info("dict sessions is "+str(self.dict_sessions))                      
    #add_unet_session(self.device_id, self.subscr_id, 
                    #ip_address, self.app_id, duration, media_descr, ott_api, self)
    def add_unet_session(self, device_id, subscr_id, 
                         ip_address, app_id, 
                         duration, media_descr, 
                         ott_api,  service_session):
        '''
        try:
            unet_session = self.find_session_by_device_id(device_id, app_id)
        except UnderlyingNetwork_Session_Not_Found:
        '''
            
        self.logger.info("\n\n\n adding underlying network session for device id %s and app_id %s and ip address %s"%(device_id, app_id, ip_address))
        unet_session = UnderlyingNetworkSession(device_id, ip_address, 
                                                    subscr_id, app_id, 
                                                    media_descr, ott_api,
                                                    service_session, 
                                                    self.DEF_EVENT_BUS_EPC_Rx_CALLBACK_ADDRESS, 
                                                    rx_callback_handler, 
                                                    self, self.logger, duration)
        self.save_locally(unet_session)
        return unet_session 
    
    def remove_unet_session(self, unet_session):
        device_id = unet_session.get_device_id()
        if device_id in self.dict_sessions.keys():
            list = self.dict_sessions[device_id]
            if unet_session in list:
                list.remove(unet_session)
                if len(list) > 0:
                    self.dict_sessions[unet_session.get_device_id()] = list
                else:
                    del self.dict_sessions[unet_session.get_device_id()] 
        if unet_session.get_id() in self.dict_sessions:
            del self.dict_sessions[unet_session.get_id()]
        self.logger.info("\n\n\n after removing session dict sessions is "+str(self.dict_sessions))
                
    def print_sessions(self):
        self.logger.info("Underlying Network Session Manager Sessions: ")
        self.logger.info("----------------------------------")
        for list in self.dict_sessions.values():
            for session in list:
                session.print_session()
        self.logger.info("----------------------------------")
            
        
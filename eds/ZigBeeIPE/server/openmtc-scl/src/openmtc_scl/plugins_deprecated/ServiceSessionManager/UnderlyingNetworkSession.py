import time
#import vertx
try:
    from core.event_bus import EventBus
except ImportError:
    EventBus = None

'''
json object to be sent to diameter_peer
myObj = {
      'requestType' : 'SessionInitiation',
      'SubscriptionID': '01001234567890',
      'ip_address':'192.168.3.100',
      'applicationIdentifier':'MyApplication',
      'eventBusAddressRxEvent':'CallbackEventAddress',
      'MediaCompList':[{
                       'MAX_DL':2000,
                       'MAX_UL':2000,
                       'MediaType':'application', 
                       'FlowStatus':'enabled',
                       'Src_IP':'192.168.3.100',
                       'Dst_IP':'any',
                       'Src_Port':'80',
                       'Dst_Port':'80',
                       'Protocol':'ip',
                       }
            ],
      'NetworkEventSubscriptions':[ 
                {'Event':'loss_of_bearer'}, 
                {'Event':'recovery_of_bearer'},
                {'Event':'release_of_bearer'},
                {'Event':'successful_resource_allocation'},
                {'Event':'failed_resource_allocation'},
                {'Event':'charging_correlation_and_exchange'}
                
            ]
            
    }
'''

class UnderlyingNetworkSession:
    
    DEF_EPC_Rx_SESSION_LIFETIME = 3600
    DEF_EVENT_BUS_ADDRES_EPC_Rx = "org.openxsp.epc_rx.send"
    #DEF_EVENT_BUS_EPC_Rx_CALLBACK_ADDRESS = "org.openmtc.network_service.underlying_network_session.epc_rx"
    
    def __init__(self, device_id, ip_address, 
                 subscr_id, app_id, 
                 media_descr, ott_api, 
                 service_session,
                 rx_callback_address, rx_callback_handler, 
                 unet_manager, logger, 
                 epc_rx_lifetime=DEF_EPC_Rx_SESSION_LIFETIME):
        
        self.device_id = device_id
        self.subscr_id = subscr_id
        self.ip_address_list = []
        self.ip_address_list.append(ip_address)
        self.app_id = app_id
        self.media_comp_list = []
        for comp in media_descr:
            self.media_comp_list.append(comp)
        self.ott_api = ott_api
        self.logger = logger
        self.unet_manager = unet_manager
        self.identifier=self.create_new_identifier(device_id, subscr_id, app_id)
        self.service_session = service_session
        self.service_session_id = service_session.get_id()
        self.epc_rx_send_address = self.DEF_EVENT_BUS_ADDRES_EPC_Rx
        self.epc_rx_callback_address = rx_callback_address
        self.epc_rx_callback_handler = rx_callback_handler
        
        self.epc_rx_session_id = ""
        if epc_rx_lifetime is None:
            self.epc_rx_session_lifetime = self.DEF_EPC_Rx_SESSION_LIFETIME
        else:
            self.epc_rx_session_lifetime = epc_rx_lifetime
        self.device_connected = 0
        self.ipcan = ""
        self.rat= ""
        self.logger.info("\n\ninitiating underlying network session for ip address %s\n\n"%(ip_address))
        self.state = "Idle"
      
    def add_media_comp(self, media_comp):
        self.media_comp_list.append(media_comp)              
            
        if self.epc_rx_session_id is not "":
            self.logger.info("media comp added, time to update session")
    
    def set_epc_rx_session_id(self, rx_session_id):
        self.epc_rx_session_id = rx_session_id
        
    def get_id(self):
        return self.identifier
    
    def get_device_id(self):
        return self.device_id
    
    def get_service_session_id(self):
        return self.service_session_id
    
    def get_state(self):
        return self.state
        
    def create_new_identifier(self, device_id, subscr_id, app_id):
        return device_id+"_"+subscr_id+"_"+app_id+"_"+str(int(time.time()))
    
    def set_callback(self, event_callback):
        self.event_callback = event_callback
        
    def print_session(self):
        self.logger.info("Id: "+self.identifier)
        if self.epc_rx_session_id:
            self.logger.info("EPC Session Id "+self.epc_rx_session_id)
        if self.epc_rx_session_lifetime:
            self.logger.info("EPC Session Lifetime "+str(self.epc_rx_session_lifetime))
        if self.ipcan:
            self.logger.info("EPC Session IPCAN Type "+self.ipcan)
        if self.rat:
            self.logger.info("EPC Session RAT Type "+self.rat)
        self.logger.info("connection status "+str(self.device_connected))
    
    def initiate(self):
        #if subscr_id is from EPC, initiate the EPC Rx Session
        self.logger.info("\n\n\n ip address list is %s\n\n"%(str(self.ip_address_list)))
        
        request = {
            'requestType' : 'RxSessionInitiation',
            'SessionLifetime':self.epc_rx_session_lifetime,
            'SubscriptionID': self.subscr_id,
            'ue_ip_address':self.ip_address_list[0],
            'applicationIdentifier':self.app_id,
            'eventBusAddressRxEvent':self.epc_rx_callback_address,
            'ReferenceId':self.identifier,
            'MediaCompList':self.media_comp_list,
            'NetworkEventSubscriptions':[ 
                      {'Event':'CHARGING_CORRELATION_AND_EXCHANGE'}, 
                      {'Event':'INDICATION_OF_LOSS_OF_BEARER'},
                      {'Event':'INDICATION_OF_RECOVERY_OF_BEARER'},
                      {'Event':'INDICATION_OF_RELEASE_OF_BEARER'},
                      {'Event':'IP_CAN_CHANGE'},
                      {'Event':'INDICATION_OF_SUCCESSFUL_RESOURCE_ALLOCATION'},
                      {'Event':'INDICATION_OF_FAILED_RESOURCE_ALLOCATION'},
                      {'Event':'ACCESS_NETWORK_INFO_REPORT'},
                      {'Event':'IP_ADDRESS_INFO_REPORT'}                
                  ]
                  
            }
        self.logger.info("request is %s" %(request))
        
        if EventBus:    
            EventBus.send(self.epc_rx_send_address, request, self.epc_rx_callback_handler)
            
    def terminate_epc_rx_session(self):
        request = {
            'requestType' : 'RxSessionTermination',
            'SessionId':    self.epc_rx_session_id
            }
        if EventBus:    
            EventBus.send(self.epc_rx_send_address, request, self.epc_rx_callback_handler)
    
    def process_new_registered_ip_address(self, ip_address):
        if ip_address not in self.ip_address_list:
            self.ip_address_list.append(ip_address)
            request = {
                       'requestType' : 'RxSessionNewIPAddress',
                       'SessionId':    self.epc_rx_session_id,
                       'ip_address':   ip_address
            }
        if EventBus:    
            EventBus.send(self.epc_rx_send_address, request, self.epc_rx_callback_handler)
            
    def set_device_connection_status(self, status):
        self.device_connected = status
            
    def process_epc_event(self, message):
        
        self.logger.info("\n\n\process epc event with message "+str(message)+"\n\n\n")
        try:
            if not self.epc_rx_session_id:
                self.epc_rx_session_id = message["SessionId"]
        
            eventName= message["Event"]
            if eventName=="StateChange":
                new_state = message["NewState"]
                if new_state == "Open":
                    self.set_device_connection_status('True')
                    if "ANInfo" in message.keys():
                        an_info=message["ANInfo"]
                        if "IP_CAN_Type" in an_info.keys():
                            self.ipcan = an_info["IP_CAN_Type"]
                        if "RAT_Type" in an_info.keys():
                            self.rat = an_info["RAT_Type"]
                    #self.logger.info("session is now Open, terminating it")
                    #time.sleep(2)
                    #self.terminate_epc_rx_session()
                #elif new_state == "Discon":
                #    self.unet_manager.remove_unet_session(self)
                #    self.service_session.unet_session_terminated(self)
                    
            #elif eventName=="IP_CAN_CHANGE":
            elif eventName=="INDICATION_OF_LOSS_OF_BEARER":
                #device was disconnected
                self.set_device_connection_status('False')
            elif eventName=="INDICATION_OF_RECOVERY_OF_BEARER":
                self.set_device_connection_status('True')
            elif eventName=="Removed":
                self.unet_manager.remove_unet_session(self)
                self.service_session.unet_session_terminated(self)
            
            #TODO: store ip address, ipcan type, rat type, if provided
            if eventName!="Removed":
                self.ott_api.update_service_session(self.service_session)
            else:
                self.ott_api.remove_service_session(self.service_session)
            self.print_session()
        except KeyError:
            print "message body "+str(message)+" does not contain any Event or SessionId key"
      
        
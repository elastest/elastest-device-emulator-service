from openmtc_server.Plugin import Plugin
from Service_Session import Service_Session_CSE_AE
from UnderlyingNetwork_SessionManager import UnderlyingNetwork_SessionManager
from openmtc.model import Scl, ApplicationAnnc
from urlparse import ParseResult, urlparse, urlunparse
from socket import gethostbyname
from openmtc.model import M2mPoc

class Service_Session_Not_Found(Exception):
    pass

class ServiceSessionManager(Plugin):
    DEF_GSCL_REG_APP_ID = "OpenMTC_GSCL_Registration"
    dict_sessions = {}

    def _init(self):
        #self.events.resource_announced.register_handler(self._initiate_service_session, AnnouncementResource)
        #self.config.
        self.events.resource_created.register_handler(self._handle_gscl_created, Scl)
        self.events.resource_deleted.register_handler(self._handle_gscl_deleted, Scl)
        self.events.resource_created.register_handler(self._handle_poc_created, M2mPoc)
        self.events.resource_deleted.register_handler(self._handle_poc_deleted, M2mPoc)
#        self.events.resource_created.register_handler(self... , ApplicationAnnc)

        self.dict_sessions = {}
        self.db_config = self.config["db"]
        self.unet_manager = UnderlyingNetwork_SessionManager(self.logger, self.db_config, "m2m_id_epc_id")
        self.unet_manager.event_bus_reg()
        self.get_shelve("m2m_id_epc_id") \
            .then(self.unet_manager._load_epc_id)
        #self.test()
        self._ready()

    def stop(self):
        return

    def test(self):
        self.add_cse_ae_service_session("GSCL_1", "Gateway", "001011234567890", '192.168.3.100', 'OpenMTCApp')
        self.print_sessions()

    def find_session(self, device_id, app_id):
        try:
            session = self.get_session(device_id, app_id)
            return session.get_id()
        except:
            raise Service_Session_Not_Found("service session for device id %s and app id %s was not found" %(device_id, app_id))

    def get_session(self, device_id, app_id):
        if device_id in self.dict_sessions.keys():
            list = self.dict_sessions[device_id]
            if not list:
                raise Service_Session_Not_Found("service session for device id "+device_id+" was not found")
            for session in list:
                if app_id in session.get_id():
                    return session
        else:
            raise Service_Session_Not_Found("service session for device id %s and app id %s was not found" %(device_id, app_id))


    def save_locally(self, session):
        self.logger.info("Service Session Adding session with id "+session.get_id()+" for device "+session.get_device_id())
        list = []
        device_id= session.get_device_id()
        if device_id in self.dict_sessions.keys():
            list = self.dict_sessions[device_id]
        list.append(session)
        self.dict_sessions[device_id] = list

        self.print_sessions()

    def remove_session(self, session):
        device_id = session.get_device_id()
        if device_id in self.dict_sessions.keys():
            list = self.dict_sessions[device_id]
            if session in list:
                list.remove(session)
                if len(list) > 0:
                    self.dict_sessions[session.get_device_id()] = list
                else:
                    del self.dict_sessions[session.get_device_id()]



    def add_cse_ae_service_session(self, device_id, participant_type, subscr_id, ip_address, app_id):
        try:
            service_session_id = self.find_session(device_id, app_id)
        except Service_Session_Not_Found:
            service_session = Service_Session_CSE_AE(device_id, participant_type,
                                                     subscr_id, ip_address, app_id,
                                                     self.logger, self.db_config, self.unet_manager)
            self.save_locally(service_session)
            if subscr_id and ip_address:
                service_session.initiate_underlying_network_sess()

    def print_sessions(self):
        self.logger.info("Service Session Manager Sessions: ")
        self.logger.info("----------------------------------")
        for list in self.dict_sessions.values():
            for session in list:
                session.print_session()
        self.logger.info("----------------------------------")

    def _initiate_service_session(self, instance, req_ind):
        #sclId example: GSCL_1
        #sclType example: GSCL
        '''
        self.logger.info("initiating service session for an Scl instance")
        self.logger.info("Scl id is "+instance.sclId)
        self.logger.info("Scl type is "+instance.sclType)
        self.logger.info("Scl link is "+instance.link)
        if instance.sclId is not None and (
            instance.sclType is not None and
            instance.link is not None):

            epc_subscription_id = self.get_epc_subscription_id(instance.sclId)
            parsed_link= urlparse(instance.link)
            ip_address = gethostbyname(parsed_link.hostname)
            self.add_cse_ae_service_session(instance.sclId, instance.sclType,
                                            epc_subscription_id, ip_address, "OpenMTC_GSCL_Registration")
       '''
    def _handle_gscl_created(self, instance, req_ind):
        self.logger.info("initiating service session for an Scl instance")
        self.logger.info("Scl id is "+instance.sclId)
        self.logger.info("Scl type is "+instance.sclType)
        self.logger.info("Scl link is "+instance.link)
        if instance.sclId is not None and (
            instance.sclType is not None and
            instance.link is not None):

            def handle_ok_subscr_id(epc_subscription_id):
                self.add_cse_ae_service_session(instance.sclId, instance.sclType,
                                            epc_subscription_id, None, self.DEF_GSCL_REG_APP_ID)
            def handle_error_subscr_id(epc_subscription_id):
                self.add_cse_ae_service_session(instance.sclId, instance.sclType,
                                            None, None, self.DEF_GSCL_REG_APP_ID)
            self.unet_manager.get_epc_subscription_id(instance.sclId).then(handle_ok_subscr_id, handle_error_subscr_id)
            #parsed_link= urlparse(instance.link)
            #ip_address = gethostbyname(parsed_link.hostname)

    def _handle_gscl_deleted(self, instance, req_ind):

        #self.logger.info("\n\n\n\nparam is "+str(req_ind)+"\n\n\n\n")
        token_list = req_ind.path.strip().split("/")
        device_id = token_list[3]
        self.logger.info("\n\n\n\n deleted a gscl with id %s\n\n\n\n"%(device_id))
        session = self.get_session(device_id, self.DEF_GSCL_REG_APP_ID)
        if not session:
            return
        session.terminate_unet_session()
        self.remove_session(session)

    def _handle_poc_created(self, instance, req_ind):
        """
        #example:
        instance:M2mPoc(path='/m2m/scls/gscl/m2mPocs/m2mPocnRIjsAAZmqm1U49j', name='m2mPocnRIjsAAZmqm1U49j')
        req_ind:RequestIndication: {
            path: /m2m/scls/gscl/m2mPocs,
            method: create,
            typename: m2mPoc,
            resource: {
                'creationTime': datetime.datetime(2014, 7, 11, 13, 37, 40, 385438,
                    tzinfo=<openmtc.util.Utc object at 0x7f4d9bf68e50>),
                'expirationTime': datetime.datetime(2014, 7, 11, 13, 43, 40,
                    tzinfo=<FixedOffset '+00:00'>),
                'onlineStatus': 'ONLINE',
                'contactInfo': 'http://[2001:638:806:65:f4bf:ccb0:cad5:a203]:5000',
                'lastModifiedTime': datetime.datetime(2014, 7, 11, 13, 37, 40, 385438,
                    tzinfo=<openmtc.util.Utc object at 0x7f4d9bf68e50>)
            }
        }
        """

        self.logger.debug("_handle_created: instance:%s req_ind:%s", instance, req_ind)

        resource = req_ind.resource
        poc_path = instance.path
        self.logger.info("\n\n\npoc path is "+poc_path+"\n\n\n")
        token_list=poc_path.strip().split("/")
        self.logger.info("\n\n\n token list is "+str(token_list)+"\n\n\n")
        device_id = token_list[3]
        #scl_path = req_ind.path.rstrip('/m2mPocs')
        self.logger.info("\n\n\n device id is "+device_id+"\n\n\n")
        self.logger.info("\n\n\n resource is of type "+resource.__class__.__name__+"\n\n\n")
        contact_info = resource['contactInfo']
        parsed_contact = urlparse(contact_info)
        ip_address = gethostbyname(parsed_contact.hostname)
        self.logger.info("\n\n\n ip address is "+ip_address+"\n\n\n")
        try:
            service_session = self.get_session(device_id, self.DEF_GSCL_REG_APP_ID)
            if service_session.subscr_id is not None and ip_address is not None:
                if service_session.add_ip_address(ip_address) == 1:
                    service_session.add_ip_underlying_network_sess(ip_address)
        except Service_Session_Not_Found:
            self.logger.error("could not find session for device id "+device_id+" and app "+self.DEF_GSCL_REG_APP_ID)

    def _handle_poc_deleted(self, instance, req_ind):
        return

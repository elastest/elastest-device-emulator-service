from futile.logging import LoggerMixin
from gevent.server import DatagramServer
from json import loads, dumps
from lwm2m_lib.import_common_libs import connection, options, link, constants, json
from lwm2m_lib.operations.Registration import Registration, Endpoint
from lwm2m_lib.api import lwm2m_api
from lwm2m_lib.data_model.ClientsCollection import ClientEndpoint, LWM2MResourceTree
from lwm2m_lib.data_model.ParseQueryPayload import ParsePath, ParsePayload, ParseQuery
from lwm2m_lib.operations.Execution import Execution
from lwm2m_lib.operations.Discovery import Discovery
from lwm2m_lib.operations.Read import Read
from lwm2m_lib.operations.Write import Write
from lwm2m_lib.operations.Create import Create
from lwm2m_lib.operations.WriteAttributes import WriteAttributes
from lwm2m_lib.operations.ObservationNotification import ObservationNotificationEngine, GeneralObservationInformation
from lwm2m_lib.operations.OperationRequest import OperationRequest
from lwm2m_lib.data_model.ParseQueryPayload import ParsePath, ParsePayload, ParseQuery
from gevent.coros import Semaphore
from lwm2m_lib.operations.EventDispatcher import EventDispatcher
from copy import deepcopy

OBSERVE_OPTION_VALUE_OBSERVATION = 0
OBSERVE_OPTION_VALUE_CANCEL_OBSERVATION = 1

URI_QUERY_VALUE = 15
LOCATION_VALUE = 8
URI_PATH_VALUE = 11
URI_HOST_VALUE = 3
URI_PORT_VALUE = 7

class LocalClientCore(LoggerMixin):
    
    def __init__(self, local_listener_ip, local_listener_port, lwm2m_server_ip, lwm2m_server_port,
                 local_client_ip, local_client_port):
        
        self.ep_location_mapping = {}
        self.total_resources = {}
        self.res_dict = {}
        self.lwm2m_dm_server_ip = lwm2m_server_ip
        self.lwm2m_dm_server_port = lwm2m_server_port
        self.sem = Semaphore()
        self.local_listener_ip = local_listener_ip
        self.local_listener_port = local_listener_port
        self.local_client_ip_ = local_client_ip
        self.local_client_port =  local_client_port #local_client_port
        #self.local_client_port_end = local_client_port_end  #local_client_port
        self.dispatcher = EventDispatcher()
        self.lwm2m_resources = LWM2MResourceTree(self.dispatcher)
        self.registration = Registration(self.lwm2m_resources)
        self.read = Read(self.lwm2m_resources)
        self.write = Write(self.lwm2m_resources)
        self.write_attributes = WriteAttributes(self.lwm2m_resources)
        self.create_object_instance = Create(self.lwm2m_resources)
        self.observation = ObservationNotificationEngine(self.lwm2m_resources, self.dispatcher)
        self.execution = Execution(self.lwm2m_resources)
        self.discover = Discovery(lwm2m_resources=self.lwm2m_resources)
        
        self.observation_started = False
    
    def load_dm_adapter(self, dm_adapter):
        self.dm_adapter = dm_adapter
    
    def create_server(self, local_listener_ip=None):
        """ Creates and starts a local server using Gevent DatagramServer. The server
        listens at the ip and port specified below. A handler is used to entertain the
        requests coming at that port """
        
        if local_listener_ip is not None:
            self.local_listener_ip = local_listener_ip
            
        self.logger.info("Local Server Created")
        self.logger.info("local_listener_ip %s", self.local_listener_ip)
        self.logger.info("local_listener_port %s", self.local_listener_port)
        
        self.local_server = DatagramServer((self.local_listener_ip, self.local_listener_port), self.handle_lwm2m_request)
        self.local_server.start()
        
    def stop_server(self, ):
        """ Stops the local server """
        
        self.local_server.stop()
        
    def handle_lwm2m_request(self, message, remote):
        """ Handles the requests coming at the specified ip and port """
        
        rx_record = connection.ReceptionRecord(None, message, remote)
        msg = rx_record.message
        uri_query = msg.findOption(options.UriQuery)
        self.process(rx_record, remote, uri_query)
    
    """ Used for Create Object Instance, Execution Operation Request """
    def handle_lwm2m_post(self, msg, uri_query, remote, rx_record):
        method = None
        try:
            method = uri_query[0].value.split("=")[1]
        except:
            pass
        
        if method == "create":
            path = msg.findOption(URI_PATH_VALUE)
            content_type_number = msg.findOption(options.ContentType)
            if content_type_number is None:
                content_type = "text/plain"
            else:
                content_type =  constants.media_types[content_type_number.value]
            self.create_object_instance.create_instance(path, remote, content_type, loads(msg.payload))
            
            msg = connection.Message(connection.Message.ACK, code=constants.CREATED, payload="Resource Created")
            self.local_server.sendto(msg._pack(rx_record.transaction_id), remote)
            
        elif method == "execute":
            path = msg.findOption(URI_PATH_VALUE)
            content_type_number = msg.findOption(options.ContentType)
            if content_type_number is None:
                content_type = "text/plain"
            else:
                content_type =  constants.media_types[content_type_number.value]

            endpoint_name, object_id, object_inst_id, res_id, res_value = \
                                self.execution.execute_resource(path, remote, msg.payload)

            msg = connection.Message(connection.Message.ACK, code=constants.CHANGED, payload="Resource Executed")
            self.local_server.sendto(msg._pack(rx_record.transaction_id), remote)
            
            resource = {}
            resource[res_id] = {"res_value" : res_value}
            content_type = "application/json"
            self.dm_adapter.update_resources(endpoint_name, object_id, object_inst_id, dumps(resource), content_type=content_type)
                    
            
    """ It consists of Normal Update, Write Operation, Write Attribute Operation.
    Write Operation is used to update the resource(s) as per the request. Write
    Attributes operation is used to update the attributes of the object, object
    instance or resource. """
    def handle_lwm2m_put(self, msg, remote, rx_record):
        uri_query = msg.findOption(options.UriQuery)
        
        method = None
        try:
            method = uri_query[0].value.split("=")[1]
        except:
            pass
        
        if method == "write":
            self.logger.info("Updating the Resources in the Client")
            
            path = msg.findOption(URI_PATH_VALUE)
            content_type_number = msg.findOption(options.ContentType)
            if content_type_number is None:
                content_type = "text/plain"
            else:
                content_type =  constants.media_types[content_type_number.value]
            self.write.write_resource(msg.payload, path, content_type)
            
            payload_forward = msg.payload
            
            msg = connection.Message(connection.Message.ACK, code=constants.CHANGED, payload="CHANGED")
            self.local_server.sendto(msg._pack(rx_record.transaction_id), remote)
        
            endpoint_name, object_id, object_inst_id, res_id, res_inst_id, _,_ = OperationRequest().find_elements(path, remote)
            
            self.dm_adapter.update_resources(endpoint_name, object_id, object_inst_id, \
                                    payload_forward, content_type=content_type)
        
        elif method == "write_attributes":
            path = msg.findOption(URI_PATH_VALUE)
            content_type_number = msg.findOption(options.ContentType)
            if content_type_number is None:
                content_type = "text/plain"
            else:
                content_type =  constants.media_types[content_type_number.value]
            payload = loads(msg.payload)
            self.write_attributes.set_attributes(path, remote, payload)
            
            msg = connection.Message(connection.Message.ACK, code=constants.CHANGED, payload="Resource Attributes Changed")
            self.local_server.sendto(msg._pack(rx_record.transaction_id), remote)
        
    """ Sets the Observation. Two types of observations. General Observation
    and Specific Observation. General Observation is used for anything that is
    not observed and updates are sent as general notifications using a general
    token. Specific observation is implicitly defined by the observer(as request)
    and handled as specific notification with a specific token """
    def handle_lwm2m_observe(self, msg, remote, rx_record):
        path = msg.findOption(URI_PATH_VALUE)
        if len(path) == 1:
            token_id = self.set_generation_observation_params(msg)
            payload = "General Observation Started at the Client"
            content_type = "text/plain"
        else:
            self.logger.info("Specific Observation Received")
            
            endpoint_name, object_id, object_inst_id, res_id, res_inst_id, _,_ = OperationRequest().find_elements(path, remote)

            token_id = msg.token
            payload = msg.payload

            self.observation.set_observation(endpoint_name, object_id, object_inst_id, res_id, token_id, payload, self.lwm2m_dm_server_ip, self.lwm2m_dm_server_port, res_inst_id=res_inst_id)
            
        msg = connection.Message(connection.Message.ACK, code=constants.CONTENT)
        self.local_server.sendto(msg._pack(rx_record.transaction_id, token_id), remote)
        
    """ Removes the observation from the List """
    def handle_lwm2m_cancel_observe(self, msg, remote, rx_record):
        self.logger.info("Cancel Observation Request Received")
        path = msg.findOption(URI_PATH_VALUE)
        
        endpoint_name, object_id, object_inst_id, res_id, res_inst_id, _,_ = OperationRequest().find_elements(path, remote)
        
        token_id = msg.token
        payload = msg.payload
        
        message = self.observation.cancel_observation(endpoint_name, object_id, object_inst_id, res_id, token_id, payload, self.lwm2m_dm_server_ip, self.lwm2m_dm_server_port, res_inst_id=res_inst_id)
        
        msg = connection.Message(connection.Message.ACK, code=constants.CONTENT, payload=message)
        self.local_server.sendto(msg._pack(rx_record.transaction_id), remote)
    
    def process(self, rx_record, remote, uri_query):
        """ Processes various requests like CON (POST, PUT, GET) or NON.
        POST requests : Generally used for Registration and Execution
        PUT requests : Generally used for updating the resources
        GET requests : Generally used for Discovery, Observation, Cancel Observation """
        
        msg = rx_record.message
        self.uri_query = uri_query
        
        if msg.transaction_type == connection.Message.CON:
            if constants.POST == msg.code:
                """ Used for Registration requests, Execution Operation Request """
                self.handle_lwm2m_post(msg, uri_query, remote, rx_record)
                
            elif constants.PUT == msg.code:
                """ It consists of Normal Update, Write Operation, Write Attribute Operation.
                Write Operation is used to update the resource(s) as per the request. Write
                Attributes operation is used to update the attributes of the object, object
                instance or resource. """
                
                self.handle_lwm2m_put(msg, remote, rx_record)

            elif constants.GET == msg.code:
                """ Handles Requests like Discovery, Observation """
                try:
                    observe_value = msg.findOption(options.Observe).value
                except:
                    observe_value = ""
                if observe_value == OBSERVE_OPTION_VALUE_OBSERVATION:
                    """ Sets the Observation. Two types of observations. General Observation
                    and Specific Observation. General Observation is used for anything that is
                    not observed and updates are sent as general notifications using a general
                    token. Specific observation is implicitly defined by the observer(as request) 
                    and handled as specific notification with a specific token """
                    self.handle_lwm2m_observe(msg, remote, rx_record)

                elif observe_value == OBSERVE_OPTION_VALUE_CANCEL_OBSERVATION:
                    """ Removes the observation from the List """
                    
                    self.handle_lwm2m_cancel_observe(msg, remote, rx_record)

                else:
                    uri_query = msg.findOption(options.UriQuery)
        
                    method = None
                    try:
                        method = uri_query[0].value.split("=")[1]
                    except:
                        pass
                    
                    if method == "discover":
                        path = msg.findOption(URI_PATH_VALUE)
                        payload = self.discover.get_resource(path, remote)
                        
                        msg = connection.Message(connection.Message.ACK, code=constants.CONTENT, payload=dumps(payload))
                        self.local_server.sendto(msg._pack(rx_record.transaction_id), remote)
    
    
    def set_generation_observation_params(self, msg):
        listener_address = json.loads(msg.payload)
        listener_ip = listener_address["listener_ip"]
        listener_port = listener_address["listener_port"]
        token_id = msg.token
        self.general_observation = GeneralObservationInformation(listener_ip, listener_port, token_id)
        return token_id
    
    
    def send_client_registration(self, endpoint, local_client_port):
        """ Client registration request to the LWM2M server """
        
        self.logger.info("Preparing Client Registration parameters for LWM2M DM Server")
        registration_params = {"lt" : self.lifetime, "lwm2m" : self.version, "sms" : self.sms_number, "b" : self.binding_mode}
        client_object, response = self.registration.send_client_registration(endpoint, registration_params, self.lwm2m_dm_server_ip, \
                                self.lwm2m_dm_server_port, self.local_listener_ip, self.local_listener_port, \
                                local_client_port)
        self.client = client_object

        def _handle_response(response):
            location_address = response.findOption(LOCATION_VALUE)[0].value
            self.logger.debug("The registered location address of Client in DM Server is %s", location_address)
            self.ep_location_mapping[endpoint.endpoint_name] = location_address

            temp_total_resources = deepcopy(self.total_resources)
            for ep_name, resdict in temp_total_resources.iteritems():
                for mgmt_obj_id, resources in resdict.iteritems():
                    if self.ep_location_mapping.has_key(ep_name):
                        self.logger.info("Endpoint Location now available. Forwarding saved resources")
                        self.send_add_resources(resources, ep_name, mgmt_obj_id)
                        del self.total_resources[ep_name][mgmt_obj_id]
                if not any(self.total_resources[ep_name]):
                    del self.total_resources[ep_name]
            return location_address

        return response.then(_handle_response)

    def load_registration_params(self, lifetime=None, version=None, sms_number=None, binding_mode=None):
        self.lifetime = lifetime
        self.version = version
        self.sms_number = sms_number
        self.binding_mode = binding_mode
        
        
    def local_registration(self, endpoint_name, local_client_port):
        """ Local registration of the resources in the local server """
        self.logger.info("Local Registration Started for Endpoint: %s", endpoint_name)
        
        self_object = Endpoint(endpoint_name, objects=None, lifetime=self.lifetime, version=self.version, \
                                        sms_number=self.sms_number, binding_mode=self.binding_mode, \
                                        local_ip=self.local_client_ip_, local_port=local_client_port, \
                                        listener_ip=self.local_listener_ip, listener_port=self.local_listener_port)
        endpoint = self_object.endpoint
        response = self.registration.register_client(endpoint)
        
        """ Sending Client Registration to the DM Server """
        registration_location = self.send_client_registration(endpoint, local_client_port)
        return endpoint, registration_location
    
    def add_resource(self, emulated_device_name, lwm2m_mgmt_obj_id, lwm2m_resource_id, param_value, \
                     lwm2m_mgmt_obj_inst_id=None, lwm2m_resource_inst_id=None):
        
        self.logger.info("Adding Resources in the Resource Model")
        endpoint = self.lwm2m_resources.return_endpoint_object(emulated_device_name)
        
        resource_change_flag = self.lwm2m_resources.add_object_instance_resource_instance(endpoint, lwm2m_mgmt_obj_id, \
                             lwm2m_resource_id, param_value, object_inst_id=lwm2m_mgmt_obj_inst_id, \
                             res_inst_id=lwm2m_resource_inst_id)
        
        return resource_change_flag
    
    def send_add_resources(self, object_and_resources, endpoint_name, mgmt_obj_id_inst_id):
        if self.ep_location_mapping.has_key(endpoint_name):
            location_address = self.ep_location_mapping[endpoint_name]
        else:
            location_address = None
            
        if location_address == None:
            self.logger.warning("Location couldn't be fetched !! Saving the Resources")
            self.res_dict[mgmt_obj_id_inst_id] = object_and_resources
            self.total_resources[endpoint_name] = self.res_dict
        else:
            self.logger.info("Sending Updates on the Resources..")
            path = location_address
            query_params = ""
            payload = json.dumps(object_and_resources)
            request = lwm2m_api()
            response = request.client_registration_update(self.lwm2m_dm_server_ip, self.lwm2m_dm_server_port, \
                                                    path, query_params, payload, \
                                                    client=self.client)
            
    def send_total_resources(self, ):
        #Not used currently
        self.logger.info("Sending Updates on the Resources")
        path = self.location_address
        query_params = ""
        payload = json.dumps(self.total_resources)
        request = lwm2m_api()
        response = request.client_registration_update(self.lwm2m_dm_server_ip, self.lwm2m_dm_server_port, \
                                                path, query_params, payload, \
                                                client_port=self.local_client_port)
        
        self.total_resources = {}
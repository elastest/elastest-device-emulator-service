from gevent.server import DatagramServer
from json import dumps, loads
from aplus import Promise
from lwm2m_lib.import_common_libs import connection, options, link, constants
from lwm2m_lib.operations.Registration import Registration, Endpoint
from lwm2m_lib.operations.ObservationNotification import ObservationNotificationEngine, GeneralObservationInformation
from lwm2m_lib.operations.Execution import Execution
from lwm2m_lib.operations.Discovery import Discovery
from lwm2m_lib.operations.Read import Read
from lwm2m_lib.operations.Write import Write
from lwm2m_lib.operations.Create import Create
from lwm2m_lib.operations.WriteAttributes import WriteAttributes
from lwm2m_lib.operations.OperationRequest import OperationRequest
from lwm2m_lib.data_model.ParseQueryPayload import ParsePath, ParsePayload, ParseQuery
from lwm2m_lib.data_model.ClientsCollection import ClientEndpoint, LWM2MResourceTree #ClientsCollection
from lwm2m_lib.operations.OperationRequest import OperationRequest
from lwm2m_lib.api import lwm2m_api
from gevent.coros import Semaphore

# Constants
OBSERVE_OPTION_VALUE_OBSERVATION = 0
OBSERVE_OPTION_VALUE_CANCEL_OBSERVATION = 1

URI_QUERY_VALUE = 15
LOCATION_VALUE = 8
URI_PATH_VALUE = 11
URI_HOST_VALUE = 3
URI_PORT_VALUE = 7


class DMServerCore(OperationRequest):
    def __init__(self, server_ip, server_port, client_ip, client_port):
        super(DMServerCore, self).__init__()
        
        self.lwm2m_dm_server_ip = server_ip
        self.lwm2m_dm_server_port = server_port
        self.local_client_ip_ = client_ip
        self.local_client_port_ = client_port
        self.sem = Semaphore()
        self.sem_counter = 0
        
        self.lwm2m_resources = LWM2MResourceTree()
        self.registration = Registration(self.lwm2m_resources)
        self.execution = Execution(self.lwm2m_resources)
        self.discover = Discovery(lwm2m_resources=self.lwm2m_resources)
        self.observation = ObservationNotificationEngine(self.lwm2m_resources)
        self.read  = Read(self.lwm2m_resources)
        self.write = Write(self.lwm2m_resources)
        self.create_object_instance = Create(self.lwm2m_resources)
        self.write_attributes = WriteAttributes(self.lwm2m_resources)
        
        
    def create_server(self, ):
        """ Creates and starts a LWM2M DM Server using Gevent DatagramServer. The server
        listens at the ip and port specified below. A handler is used to entertain the
        requests coming at that port """
        
        self.dm_server = DatagramServer((self.lwm2m_dm_server_ip, \
                                         self.lwm2m_dm_server_port), self.handle_request)
        self.dm_server.start()
        
    
    def stop_server(self, ):
        """ Stops the LWM2M DM Server """
        
        self.dm_server.stop()
    
    def handle_request(self, message, remote):
        """ Handles the requests coming at the specified ip and port """
        
        rx_record = connection.ReceptionRecord(None, message, remote)
        msg = rx_record.message
        uri_query = msg.findOption(options.UriQuery)
        self.process(rx_record, remote, uri_query)
        
    
    
    def handle_lwm2m_put(self, msg, uri_query, remote, rx_record):
        
        """ It consists of Normal Update, Write Operation, Write Attribute Operation.
        Write Operation is used to update the resource(s) as per the request. Write
        Attributes operation is used to update the attributes of the object, object
        instance or resource. """
        
        method = None
        try:
            method = uri_query[0].value.split("=")[1]
        except:
            pass
        
        if method == "write":
            path = msg.findOption(URI_PATH_VALUE)
            content_type_number = msg.findOption(options.ContentType)
            if content_type_number is None:
                content_type = "text/plain"
            else:
                content_type =  constants.media_types[content_type_number.value]
            self.write.write_resource(msg.payload, path, content_type)
            
            payload_forward = msg.payload
            
            msg = connection.Message(connection.Message.ACK, code=constants.CHANGED, payload="Resource Updated")
            self.dm_server.sendto(msg._pack(rx_record.transaction_id), remote)
            
            client_port = self.generate_client_port()
            self.write.forward_write_request(path, payload_forward, \
                                        content_type, remote, client_port)
        
        elif method == "write_attributes":
            path = msg.findOption(URI_PATH_VALUE)
            content_type_number = msg.findOption(options.ContentType)
            if content_type_number is None:
                content_type = "text/plain"
            else:
                content_type =  constants.media_types[content_type_number.value]
            payload = loads(msg.payload)
            self.write_attributes.set_attributes(path, remote, payload)
            msg = connection.Message(connection.Message.ACK, code=constants.CHANGED, payload="Resource Attributes Updated")
            self.dm_server.sendto(msg._pack(rx_record.transaction_id), remote)
            
            client_port = self.generate_client_port()
            self.write_attributes.forward_request(path, remote, payload, content_type, client_port)
            
        else:
            
            endpoint_location = msg.findOption(URI_PATH_VALUE)[0].value
            if msg.payload == "":
                self.logger.info("Updating the Registration Params")
                endpoint_object = self.lwm2m_resources.return_endpoint_object(endpoint_location=endpoint_location)
                endpoint_object.listener_ip = uri_query[6].value.split("=")[1]
                endpoint_object.local_ip = uri_query[6].value.split("=")[1]
                
                msg = connection.Message(connection.Message.ACK, code=constants.CHANGED, payload="Resource Updated")
                self.dm_server.sendto(msg._pack(rx_record.transaction_id), remote)
            else:
                self.logger.info("Adding/Updating the Resources")
                payload = self.update_resource(loads(msg.payload), endpoint_location=endpoint_location)
            
                msg = connection.Message(connection.Message.ACK, code=constants.CHANGED, payload="Resource Updated")
                self.dm_server.sendto(msg._pack(rx_record.transaction_id), remote)
                
                self.logger.info("Forwarding the Notification")
                request = lwm2m_api()
                client_port = self.generate_client_port()
                
                response = request.send_notification(self.general_observation.listener_ip, self.general_observation.listener_port, \
                                                     self.general_observation.token_id, payload, content_type="application/json", client_port=client_port)
            
            
    def update_resource(self, res_payload, endpoint_location=None, endpoint_name=None):
        
        total_res_dict = {}
        total_object_info = {}
        
        payload = res_payload
        endpoint_object = self.registration.handle_put_resource_updates(res_payload, endpoint_location=endpoint_location, endpoint_name=endpoint_name)
                
        for item, value in payload.iteritems():
            resources_dict = endpoint_object.objects_dict[item]["object"].resources_id_dict
            res_dict = {}
            for item1, value1 in resources_dict.iteritems():
                res_dict.update({
                    item1 : value1["object"].res_value
                })
            total_res_dict.update({
                item : {"resources" : res_dict }
            })
        
        total_object_info = {endpoint_object.endpoint_name : total_res_dict}
        return total_object_info
        
    def process(self, rx_record, remote, uri_query):
        """ Processes various requests like CON (POST, PUT, GET) or NON.
        POST requests : Generally used for Registration and Execution
        PUT requests : Generally used for Updating the resources
        GET requests : Generally used for Discovery, Observation, Cancel Observation """
        
        msg = rx_record.message
        self.uri_query = uri_query
        if msg.transaction_type == connection.Message.CON:
            if constants.POST == msg.code:
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
                    resources = loads(msg.payload)
                    msg = connection.Message(connection.Message.ACK, code=constants.CREATED, payload="Resource Created")
                    self.dm_server.sendto(msg._pack(rx_record.transaction_id), remote)
                    
                    client_port = self.generate_client_port()
                    self.create_object_instance.forward_request(path, remote, resources, content_type, client_port)
                
                elif method == "execute":
                    path = msg.findOption(URI_PATH_VALUE)
                    content_type_number = msg.findOption(options.ContentType)
                    if content_type_number is None:
                        content_type = "text/plain"
                    else:
                        content_type =  constants.media_types[content_type_number.value]
                    self.execution.execute_resource(path, remote, msg.payload)
                    execute_payload = msg.payload
                    msg = connection.Message(connection.Message.ACK, code=constants.CHANGED, payload="Resource Executed")
                    self.dm_server.sendto(msg._pack(rx_record.transaction_id), remote)
                    
                    client_port = self.generate_client_port()
                    self.execution.forward_request(path, remote, execute_payload, client_port)
                
                elif method == "notify":
                    self.logger.info("Notification Received")
                    client_port = self.generate_client_port()
                    for item1, item2 in loads(msg.payload).iteritems():
                        if item1 == "observer_ip":
                            observer_ip = item2
                        elif item1 == "observer_port":
                            observer_port = item2
                        elif item1 != "observer_ip" and item1 != "observer_port":
                            endpoint_name = item1
                            for item3, item4 in item2.iteritems():
                                for item5, item6 in item4["resources"].iteritems():
                                    pass

                    res = {
                        item3 : {"resources" : {item5.split("_")[0]:{"res_value" : item6, "res_inst_id" : item5.split("_")[1]}}}
                    }
                    payload = {}
                    payload = self.update_resource(res, endpoint_name=endpoint_name)
                    
                    payload["observer_ip"] = observer_ip
                    payload["observer_port"] = observer_port
                    
                    token_id = msg.token
                    observe_value = msg.findOption(options.Observe).value
                    self.logger.info("Forwarding Notification")
                    
                    content_type = "application/json"
                    request = lwm2m_api()
                    response = request.send_notification(self.general_observation.listener_ip, self.general_observation.listener_port, token_id, payload, \
                                content_type=content_type, time_elapse=observe_value, client_port=client_port)
        
                    msg = connection.Message(connection.Message.ACK, code=constants.CREATED, payload="Notification Received")
                    self.dm_server.sendto(msg._pack(rx_record.transaction_id), remote)
                    
                else:
                    """ Handles the Client Registration Request """
                    
                    self.logger.info("Registering Client Endpoint in the LWM2M DM Server")
                    
                    endpoint = self.registration.process_registration(msg, uri_query)
                
                    response = self.registration.register_client(endpoint)
                    registered_client_location = response
                    if registered_client_location is not None:
                        self.logger.info("Client Endpoint Registration Successful for Endpoint : %s", endpoint.endpoint_name)
                        self.logger.info("The registered location is %s", registered_client_location)
                        payload = self.set_general_observation_params()
                    else:
                        self.logger.info("Client Endpoint Registration Failed")
                        
                    msg = connection.Message(connection.Message.ACK, code=constants.CREATED, location=registered_client_location)
                    self.dm_server.sendto(msg._pack(rx_record.transaction_id), remote)
                    
                    #Send the General Observation to the Registered Client
                    #self.send_general_observation(registered_client_location)
                
            elif constants.PUT == msg.code:
                """ It consists of Normal Update, Write Operation, Write Attribute Operation.
                Write Operation is used to update the resource(s) as per the request. Write
                Attributes operation is used to update the attributes of the object, object
                instance or resource. """
                self.handle_lwm2m_put(msg, uri_query, remote, rx_record)


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
                    
                    path = msg.findOption(URI_PATH_VALUE)
                    if len(path) == 1:
                        self.set_m2m_server_adapter_params(rx_record, remote)
                    else:
                        self.logger.info("Specific Observation Request Received")
                        
                        content_type_number = msg.findOption(options.ContentType)
                        if content_type_number is None:
                            content_type = "text/plain"
                        else:
                            content_type =  constants.media_types[content_type_number.value]
                        
                        token_id = msg.token
                        app_ip = loads(msg.payload)["app_ip"]
                        app_port = loads(msg.payload)["app_port"]
                        client_port = self.generate_client_port()

                        response = self.observation.forward_request(path, remote, observe_value, \
                                            self.lwm2m_dm_server_ip, self.lwm2m_dm_server_port, \
                                            app_ip, app_port, token_id, client_port)

                        msg = connection.Message(connection.Message.ACK, code=constants.CONTENT, \
                                                 payload="test") #todo: payload to be replaced
                        self.dm_server.sendto(msg._pack(rx_record.transaction_id, token_id), remote)
                    
                elif observe_value == OBSERVE_OPTION_VALUE_CANCEL_OBSERVATION:
                    """ Removes the observation from the List """
                    self.logger.info("Cancel Observation Request Received")
                    path = msg.findOption(URI_PATH_VALUE)
                    token_id = msg.token
                    app_ip = loads(msg.payload)["app_ip"]
                    app_port = loads(msg.payload)["app_port"]
                    client_port = self.generate_client_port()
                    
                    response = self.observation.forward_request(path, remote, observe_value, \
                                self.lwm2m_dm_server_ip, self.lwm2m_dm_server_port, \
                                app_ip, app_port, token_id, client_port)

                    def _handle_response(response):
                        msg = connection.Message(connection.Message.ACK, code=constants.CONTENT, payload=response)
                        self.dm_server.sendto(msg._pack(rx_record.transaction_id), remote)

                    response.then(_handle_response)

                else:
                    method = None
                    try:
                        method = uri_query[0].value.split("=")[1]
                    except:
                        pass
                    
                    if method == "read":
                        path = msg.findOption(URI_PATH_VALUE)
                        self.read.read_resource(path, remote)
                        msg = connection.Message(connection.Message.ACK, code=constants.CONTENT, \
                                             payload="info read", content_type="text/plain")
                        self.dm_server.sendto(msg._pack(rx_record.transaction_id), remote)
                    
                    elif method == "discover":
                        if msg.payload == "/.well-known/core":
                            payload = dumps(self.discover.get_all_resources())
                        else:
                            path = msg.findOption(URI_PATH_VALUE)
                            client_port = self.generate_client_port()
                            payload = self.discover.forward_request(path, remote, client_port)

                        def _handle_response(payload):
                            msg = connection.Message(connection.Message.ACK, code=constants.CONTENT, \
                                                 payload=payload, content_type="application/json")
                            self.dm_server.sendto(msg._pack(rx_record.transaction_id), remote)

                        if payload is Promise:
                            payload.then(_handle_response)
                        else:
                            _handle_response(payload)


        elif msg.transaction_type == connection.Message.NON:
            print "reached msg non"
            payload = msg.payload
            print payload
                    

    
    
    def set_general_observation_params(self, ):
        return {"listener_ip" : self.lwm2m_dm_server_ip, "listener_port" : self.lwm2m_dm_server_port}
    
    def send_general_observation(self, registered_client_location):
        if registered_client_location is not None:
            payload = dumps(self.set_general_observation_params())
            endpoint_object = self.lwm2m_resources.return_endpoint_object(endpoint_location=registered_client_location)
            client_listener_ip = endpoint_object.listener_ip
            client_listener_port = endpoint_object.listener_port

            request = lwm2m_api()
            response = request.observe_resource(client_listener_ip, client_listener_port, \
                                                payload=payload, client_port=self.generate_client_port())
        
    def set_m2m_server_adapter_params(self, rx_record, remote):
        msg = rx_record.message
        #content_type is application/json
        listener_ip = loads(msg.payload)["listener_ip"] 
        listener_port = loads(msg.payload)["listener_port"] 
        token_id = msg.token
        
        self.general_observation = GeneralObservationInformation(listener_ip, listener_port, token_id)
        
        response = "Observation Started on the LWM2M Server"
        msg = connection.Message(connection.Message.ACK, code=constants.CONTENT, payload=response)
        self.dm_server.sendto(msg._pack(rx_record.transaction_id, token_id), remote)
        
    
    def generate_client_port(self, ):
        if self.sem_counter >= 1000:
                self.sem_counter = 0
                
        self.sem.acquire()
        self.sem_counter += 1
    
        sem_counter = self.sem_counter
        self.sem.release()
        
        client_port = self.local_client_port_ + sem_counter
        return client_port

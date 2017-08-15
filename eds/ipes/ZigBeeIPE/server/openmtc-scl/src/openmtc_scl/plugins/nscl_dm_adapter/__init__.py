import json
from gevent.coros import Semaphore
from gevent.server import DatagramServer
from time import sleep

from lwm2m_lib.api import lwm2m_api
from lwm2m_lib.data_model.mgmt_objects import lwm2m_dict_objects, \
    lwm2m_reverse_dict_objects
from lwm2m_lib.import_common_libs import connection, options, constants
from lwm2m_lib.operations.Discovery import Discovery
from openmtc_etsi.model import Scl, MgmtObj, AttachedDevice, MgmtCmd
from openmtc_etsi.scl import CreateRequestIndication, RetrieveRequestIndication, \
    UpdateRequestIndication
from openmtc_server.Plugin import Plugin


class nscl_dm_adapter(Plugin):
    def _init(self, ):
        self._initialized()

    def _start(self, ):
        self.sem = Semaphore()
        self.sem_counter = 0
        self.set_configurations()
        self.api.run_task(self.create_server)
        self.subscribe_nscl()
        self.api.run_task(self.subscribe_dm_server)
        if self.config["enable_test"]:
            pass
            # self.api.run_task(self.send_execute_command)
            # Uncomment to check these operations
            # self.api.run_task(self.send_specific_observation)
            # self.api.run_task(self.send_specific_observation1)
            # self.api.run_task(self.send_cancel_observation)
            #self.api.run_task(self.send_discover_resources)
            #self.api.run_task(self.send_write_attributes)
            #self.api.run_task(self.send_create)
        self._started()

    def _stop(self, ):
        self.local_server.stop()
        self._stopped()

    def set_configurations(self, ):
        self.lwm2m_server_ip = self.config["lwm2m_dm_server_ip"]
        self.lwm2m_server_port = self.config["lwm2m_dm_server_port"]
        self.nscl_dm_adapter_listener_ip = self.config["nscl_dm_adapter_listener_ip"]
        self.nscl_dm_adapter_listener_port = self.config["nscl_dm_adapter_listener_port"]
        self.nscl_dm_adapter_client_ip = self.config["nscl_dm_adapter_client_ip"]
        self.nscl_dm_adapter_client_port = self.config["nscl_dm_adapter_client_port"]

    def create_server(self, ):
        self.local_server = DatagramServer((self.nscl_dm_adapter_listener_ip, self.nscl_dm_adapter_listener_port),
                                           self.handle_request)
        self.local_server.start()

    def handle_request(self, message, remote):
        rx_record = connection.ReceptionRecord(None, message, remote)
        msg = rx_record.message
        uriQuery = msg.findOption(options.UriQuery)
        self.process(rx_record, remote, uriQuery)

    def process(self, rx_record, remote, uri_query):
        if rx_record.message.transaction_type == connection.Message.CON:
            if constants.POST == rx_record.message.code:
                if self.general_notification_token == rx_record.message.token:
                    self.logger.info("General Notification received")
                    msg = connection.Message(connection.Message.ACK, code=constants.CREATED)
                    self.local_server.sendto(msg._pack(rx_record.transaction_id), remote)

                    self.process_resources(json.loads(rx_record.message.payload))
                else:
                    self.logger.info("Specific Notification received")
                    msg = connection.Message(connection.Message.ACK, code=constants.CREATED)
                    self.local_server.sendto(msg._pack(rx_record.transaction_id), remote)

                    payload = json.loads(rx_record.message.payload)
                    observer_ip = payload["observer_ip"]
                    observer_port = payload["observer_port"]
                    del payload["observer_ip"]
                    del payload["observer_port"]
                    self.process_resources(payload, observer_ip=observer_ip, observer_port=observer_port)

        elif rx_record.message.transaction_type == connection.Message.NON:
            if self.general_notification_token == rx_record.message.token:
                self.logger.info("General Notification received")
                self.process_resources(json.loads(rx_record.message.payload))
            else:
                self.logger.info("Specific Notification received")
                payload = json.loads(rx_record.message.payload)
                observer_ip = payload["observer_ip"]
                observer_port = payload["observer_port"]
                del payload["observer_ip"]
                del payload["observer_port"]
                self.process_resources(payload, observer_ip=observer_ip, observer_port=observer_port)

    def process_resources(self, payload, observer_ip=None, observer_port=None):
        total_resources = payload
        if observer_ip != None and observer_port != None:
            self.logger.info("The notification should be sent to %s:%s", observer_ip, observer_port)

        for ep_name, object_resources in total_resources.iteritems():
            endpoint_name = ep_name
            for object_ids, resources in object_resources.iteritems():
                object_id = object_ids.split("_")[0]
                object_inst_id = object_ids.split("_")[1]
                resources_dict = {}
                for res_ids, res_value in resources["resources"].iteritems():
                    res_id = res_ids.split("_")[0]
                    res_inst_id = res_ids.split("_")[1]
                    res_value = res_value
                    resource_name = lwm2m_dict_objects[str(object_id)]["resource_list"][str(res_id)]["resName"]
                    is_multi_inst = lwm2m_dict_objects[str(object_id)]["resource_list"][str(res_id)]["multiInst"]
                    if not is_multi_inst:
                        resources_dict.update({
                            resource_name: res_value
                        })
                    else:
                        resources_dict.update({
                            resource_name + "_" + str(res_inst_id): res_value
                        })

                self.handle_m2m_server(endpoint_name, object_id, object_inst_id, res_id, res_inst_id, resource_name,
                                       res_value, resources_dict)

    def handle_m2m_server(self, endpoint_name, object_id, object_inst_id, res_id, res_inst_id, res_name, res_value,
                          resources_dict):
        preferred_scl = endpoint_name.split("/")[0]
        if endpoint_name.find("attachedDevices") == -1:
            bool_attachedDevices = False
        else:
            attached_device_name = endpoint_name.split("/")[-1]
            bool_attachedDevices = True
        object_name = lwm2m_dict_objects[str(object_id)]["object_name"]
        resource_name = lwm2m_dict_objects[str(object_id)]["resource_list"][str(res_id)]["resName"]
        moID_value = lwm2m_dict_objects[str(object_id)]["urn"]
        res_name_res_inst_id = resource_name + "_" + str(res_inst_id)

        def add_parameters(response):
            path = response.resource.path
            resource = ('{"mgmtObjs" : ' + json.dumps(resources_dict) + '}')
            request = UpdateRequestIndication(path, resource, content_type="application/json")
            response = self.api.handle_request_indication(request)

        def handle_mgmtobjs(response):
            mgmtobj_exists = False
            for mgmtobj in response.resource.mgmtObjCollection:
                if mgmtobj.name == object_name + "_" + str(object_inst_id):
                    mgmtobj_exists = True
                    path = mgmtobj.path
                    request = RetrieveRequestIndication(path)
                    response = self.api.handle_request_indication(request)
                    try:
                        if res_name_res_inst_id in response.value.resource.flex_values:
                            if response.value.resource.flex_values[res_name_res_inst_id] == str(res_value):
                                continue
                        elif res_name in response.value.resource.flex_values:
                            if response.value.resource.flex_values[res_name] == str(res_value):
                                continue
                    except:
                        pass
                    resource = ('{"mgmtObjs" : ' + json.dumps(resources_dict) + '}')
                    request = UpdateRequestIndication(path, resource, content_type="application/json")
                    response = self.api.handle_request_indication(request)
                    break

            if not mgmtobj_exists:
                mgmtobj_ = MgmtObj(id=str(object_name) + "_" + str(object_inst_id), moID=moID_value)
                path = response.resource.path
                request = CreateRequestIndication(path, mgmtobj_)
                response = self.api.handle_request_indication(request)
                response.then(add_parameters)

        def retrieve_mgmtobjs(response):
            path = response.resource.path + "/mgmtObjs"
            request = RetrieveRequestIndication(path)
            response = self.api.handle_request_indication(request)
            response.then(handle_mgmtobjs)

        def handle_attached_devices(response):
            attached_device_exists = False
            for attached_device in response.resource.attachedDeviceCollection:
                if attached_device.name == attached_device_name:
                    attached_device_exists = True
                    path = attached_device.path + "/mgmtObjs"
                    request = RetrieveRequestIndication(path)
                    response = self.api.handle_request_indication(request)
                    response.then(handle_mgmtobjs)
                    break
            if not attached_device_exists:
                attached_device_object = AttachedDevice(id=attached_device_name)
                path = response.resource.path
                request = CreateRequestIndication(path=path, resource=attached_device_object)
                response = self.api.handle_request_indication(request)
                response.then(retrieve_mgmtobjs)

        def retrieve_attached_devices(response):
            path = response.resource.path + "/attachedDevices"
            request = RetrieveRequestIndication(path)
            response = self.api.handle_request_indication(request)
            response.then(handle_attached_devices)

        def handle_scl(response):
            scl_exists = False
            for _scl in response.resource.sclCollection:
                if _scl.name == preferred_scl:
                    scl_exists = True
                    if bool_attachedDevices:
                        path = _scl.path + "/attachedDevices"
                    else:
                        path = _scl.path + "/mgmtObjs"
                    request = RetrieveRequestIndication(path)
                    response = self.api.handle_request_indication(request)
                    if bool_attachedDevices:
                        response.then(handle_attached_devices)
                    else:
                        response.then(handle_mgmtobjs)
                    break
            if not scl_exists:
                scl_object = Scl(sclId=preferred_scl, link="127.0.0.1", sclType="GSCL", mgmtProtocolType="LWM2M")
                request = CreateRequestIndication(path="/m2m/scls", resource=scl_object)
                response = self.api.handle_request_indication(request)
                if bool_attachedDevices:
                    response.then(retrieve_attached_devices)
                else:
                    response.then(retrieve_mgmtobjs)

        path = "/m2m/scls"
        request = RetrieveRequestIndication(path)
        response = self.api.handle_request_indication(request)
        response.then(handle_scl)


    def _handle_mgmtcmd_created(self, instance, request_indication):
        pass

    def _handle_mgmtcmd_updated(self, instance, request_indication):
        pass


    def _handle_mgmtobj_created(self, instance, request_indication):
        pass

    def _handle_mgmtobj_updated(self, instance, request_indication):
        filter_keyword = "TransportMgmtPolicy"
        filter_keyword1 = "DeviceCapability"

        mgmtobj_name = instance.path.split("/")[-1]
        if mgmtobj_name.startswith(filter_keyword):
            self.handle_transport_mgmt_policy(instance, mgmtobj_name)
        elif mgmtobj_name.startswith(filter_keyword1):
            self.handle_device_capability(instance, mgmtobj_name, request_indication)

    def handle_device_capability(self, instance, mgmtobj_name, request_indication):
        generate_endpoint = instance.path.split("/")[3:-2]
        endpoint_name = "/".join(generate_endpoint)
        object_name = mgmtobj_name.split("_")[0]
        object_id = lwm2m_reverse_dict_objects[object_name]["object_id"]
        object_inst_id = mgmtobj_name.split("_")[1]

        if "opEnable" in request_indication.resource and "opDisable" in request_indication.resource:
            return
        elif "opEnable" in request_indication.resource:
            res_id = 5
            res_inst_id = 0
        elif "opDisable" in request_indication.resource:
            res_id = 6
            res_inst_id = 0
        else:
            return
        self.send_execute_resource(endpoint_name, object_id, object_inst_id, res_id, res_inst_id)


    def handle_transport_mgmt_policy(self, instance, mgmtobj_name):
        res_value_exists = False
        resources_dict = {}
        total_dict = {}
        endpoint_dict = {}
        generate_endpoint = instance.path.split("/")[3:-2]
        endpoint_name = "/".join(generate_endpoint)

        object_name = mgmtobj_name.split("_")[0]
        object_id = lwm2m_reverse_dict_objects[object_name]["object_id"]
        object_inst_id = mgmtobj_name.split("_")[1]
        for key, value in instance.flex_values.iteritems():
            res_name = key.split("_")[0]
            try:
                res_inst_id = key.split("_")[1]
            except:
                res_inst_id = 0
            res_value = value
            res_id = lwm2m_reverse_dict_objects[object_name]["resource_list"][res_name]["resId"]
            resources_dict.update({
                res_id: {"res_inst_id": res_inst_id, "res_value": res_value}
            })
            if res_value != "" and not res_value_exists:
                res_value_exists = True

        if res_value_exists:
            self.logger.info("Sending the Resource Updates to LWM2M Server")
            payload = json.dumps(resources_dict)
            content_type = "application/json"

            request = lwm2m_api()
            self.sem.acquire()
            client_port = self.generate_client_port()
            response = request.write_resource(self.lwm2m_server_ip, self.lwm2m_server_port,
                                              endpoint_name, object_id, payload, content_type,
                                              object_inst_id=object_inst_id, client_port=client_port)
            self.sem.release()

    def generate_client_port(self, ):
        if self.sem_counter >= 1000:
            self.sem_counter = 0

        self.sem_counter += 1

        sem_counter = self.sem_counter

        client_port = self.nscl_dm_adapter_client_port + sem_counter
        return client_port

    def subscribe_dm_server(self, ):
        self.logger.info("Trying to subscribe to LWM2M DM Server for General Subscription")
        payload = json.dumps({"listener_ip": self.nscl_dm_adapter_listener_ip, "listener_port": \
            self.nscl_dm_adapter_listener_port})
        content_type = "application/json"
        request = lwm2m_api()
        response = request.observe_resource(self.lwm2m_server_ip, self.lwm2m_server_port,
                                            payload=payload, content_type=content_type,
                                            client_port=self.generate_client_port())

        def _handle_response(response):
            self.logger.info("Successfully subscribed to LWM2M DM Server for General Subscription")
            self.general_notification_token = response.token

        def _handle_error(*args):
            self.subscribe_dm_server()

        response.then(_handle_response, _handle_error)


    def subscribe_nscl(self, ):
        self.events.resource_created.register_handler(self._handle_mgmtobj_created, MgmtObj)
        self.events.resource_updated.register_handler(self._handle_mgmtobj_updated, MgmtObj)
        self.events.resource_created.register_handler(self._handle_mgmtcmd_created, MgmtCmd)
        self.events.resource_updated.register_handler(self._handle_mgmtcmd_updated, MgmtCmd)


    def send_discover_resources(self, ):
        sleep(20)
        self.logger.info("Sending discover request to Dm server")
        server_ip = self.lwm2m_server_ip
        server_port = self.lwm2m_server_port
        payload = "/.well-known/core"
        request = lwm2m_api()
        response = request.discover_resources(server_ip, server_port, payload=payload,
                                              client_port=self.generate_client_port())
        discover = Discovery()
        payload = json.loads(response.payload)
        discover.display_all_resources(payload)


    def send_write_attributes(self, ):
        sleep(10)
        self.logger.info("Sending attributes info to DM server")
        server_ip = self.lwm2m_server_ip
        server_port = self.lwm2m_server_port

        endpoint_name = "emulated_device_nb_0"
        object_id = 3
        object_inst_id = 0
        res_id = 1
        res_inst_id = 0

        pmax = 50
        pmin = 10
        gt = None
        lt = None
        st = None
        cancel = None

        content_type = "application/json"
        payload = json.dumps({"pmax": pmax, "pmin": pmin, "gt": gt, "lt": lt, "st": st, "cancel": cancel})

        request = lwm2m_api()
        response = request.write_attributes(server_ip, server_port, endpoint_name, object_id,
                                            payload, content_type, object_inst_id=object_inst_id,
                                            res_id=res_id, res_inst_id=res_inst_id,
                                            client_port=self.generate_client_port())


    def send_create(self, ):
        sleep(10)
        self.logger.info("Sending create info to DM server")

        server_ip = self.lwm2m_server_ip
        server_port = self.lwm2m_server_port

        endpoint_name = "emulated_device_nb_0"
        object_id = 3
        object_inst_id = 4
        res_id = 0
        res_inst_id = 0
        res_value = "fokus"
        res_id_res_inst_id = str(res_id) + "_" + str(res_inst_id)
        payload = {}
        res_id_res_inst_id = str(res_id) + "_" + str(res_inst_id)
        payload[res_id_res_inst_id] = {"res_id": res_id, "res_inst_id": res_inst_id, "res_value": res_value}
        content_type = "application/json"

        request = lwm2m_api()
        response = request.create_object_instance(server_ip, server_port, endpoint_name, object_id,
                                                  json.dumps(payload), content_type, object_inst_id=object_inst_id,
                                                  client_port=self.generate_client_port())


    def send_specific_observation(self, ):
        sleep(15)
        self.logger.info("Sending specific observation to DM server")

        app_ip = "localhost"
        app_port = "1111"

        server_ip = self.lwm2m_server_ip
        server_port = self.lwm2m_server_port

        endpoint_name = "gscl/attachedDevices/PulseOximeter"
        object_id = 4200
        object_inst_id = 0
        res_id = 1
        res_inst_id = 0

        request = lwm2m_api()
        response = request.observe_resource(server_ip, server_port, app_ip=app_ip, app_port=app_port,
                                            endpoint_name=endpoint_name, object_id=object_id,
                                            object_inst_id=object_inst_id
                                            , res_id=res_id, res_inst_id=res_inst_id,
                                            client_port=self.generate_client_port())

        def _handle_response(response):
            self.logger.info("response token: %s", response.token)

        response.then(_handle_response)

    def send_specific_observation1(self, ):
        sleep(20)
        self.logger.info("Sending specific observation to DM server")

        app_ip = "localhost"
        app_port = "1115"

        server_ip = self.lwm2m_server_ip
        server_port = self.lwm2m_server_port

        endpoint_name = "gscl_PulseOximeter"
        object_id = 4200
        object_inst_id = 0
        res_id = 0
        res_inst_id = 0

        request = lwm2m_api()
        response = request.observe_resource(server_ip, server_port, app_ip=app_ip, app_port=app_port,
                                            endpoint_name=endpoint_name, object_id=object_id,
                                            object_inst_id=object_inst_id
                                            , res_id=res_id, res_inst_id=res_inst_id,
                                            client_port=self.generate_client_port())

        def _handle_response(response):
            self.logger.info("response token: %s", response.token)

        response.then(_handle_response)


    def send_cancel_observation(self, ):
        sleep(22)
        self.logger.info("Sending Cancel Observation to DM server")

        app_ip = "localhost"
        app_port = "1111"

        server_ip = self.lwm2m_server_ip
        server_port = self.lwm2m_server_port

        endpoint_name = "gscl/attachedDevices/PulseOximeter"
        object_id = 4200
        object_inst_id = 0
        res_id = 1
        res_inst_id = 0

        request = lwm2m_api()
        response = request.cancel_observe_resource(server_ip, server_port, app_ip, app_port,
                                                   endpoint_name, object_id, object_inst_id=object_inst_id
                                                   , res_id=res_id, res_inst_id=res_inst_id,
                                                   client_port=self.generate_client_port())

        def _handle_response(response):
            self.logger.info("response token: %s", response.token)
            self.logger.info("response %s", response.payload)

        response.then(_handle_response)


    def send_execute_resource(self, endpoint_name, object_id, object_inst_id, res_id, res_inst_id,
                              payload=None):
        self.logger.info("Sending execution to DM server")

        server_ip = self.lwm2m_server_ip
        server_port = self.lwm2m_server_port

        payload = None
        request = lwm2m_api()
        response = request.execute_resource(server_ip, server_port, endpoint_name,
                                            object_id, object_inst_id, res_id,
                                            res_inst_id=res_inst_id, payload=payload,
                                            client_port=self.generate_client_port())

        self.logger.info("Updating M2M Resource Tree")
        resources_dict = {}
        object_id_res_id = str(object_id) + "/" + str(res_id)
        if object_id_res_id in action_mapping:
            res_id = action_mapping[object_id_res_id]["target_res_id"]
            res_value = action_mapping[object_id_res_id]["target_action"]
            res_name = lwm2m_dict_objects[str(object_id)]["resource_list"][str(res_id)]["resName"]
            is_multi_inst = lwm2m_dict_objects[str(object_id)]["resource_list"][str(res_id)]["multiInst"]
            if not is_multi_inst:
                resources_dict.update({
                    res_name: res_value
                })
            else:
                resources_dict.update({
                    res_name + "_" + str(res_inst_id): res_value
                })
            self.handle_m2m_server(endpoint_name, object_id, object_inst_id, res_id,
                                   res_inst_id, res_name, res_value, resources_dict)


action_mapping = {}
action_mapping["4200/5"] = {"target_object_id": 4200, "target_res_id": 4, "target_action": True}
action_mapping["4200/6"] = {"target_object_id": 4200, "target_res_id": 4, "target_action": False}

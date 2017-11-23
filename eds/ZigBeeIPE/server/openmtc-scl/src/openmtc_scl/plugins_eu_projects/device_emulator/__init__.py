from aplus import Promise
from futile.logging import LoggerMixin
from openmtc_server.Plugin import Plugin
from openmtc_etsi.exc import OpenMTCError
from gevent.server import DatagramServer, StreamServer
from openmtc_scl.platform.gevent.ServerRack import GEventServerRack
from openmtc_etsi.scl import CreateRequestIndication, RetrieveRequestIndication
from openmtc_etsi.model import Scl, MgmtObj, ContentInstance
from json import loads
from base64 import b64decode, b64encode
import threading
from threading import Thread
from time import sleep
from sys import getsizeof
from .create_app import config_mgmt_app
from json import dumps, load
from copy import deepcopy
from random import choice
from string import lowercase
from timeit import timeit
import shelve


DEFAULT_NB_DEVICES = 1
DEFAULT_INTERVAL = 0
DEFAULT_DATA_SIZE = None
DEFAULT_DESTINATION_PATH = None #"coap://localhost:24000/m2m/applications/ScalableDynamicApp/containers/ImportantData/contentInstances/"
DEFAULT_PAYLOAD_FILE = None


class MsgSender(LoggerMixin):
        def __init__(self, api, nb_devices, interval, data_size, destination_path, payload_file_path, counter):
            self.total_time = 0
            self.db_iteration_counter = 0
            self.counter = counter
            self.api = api
            thread = Thread(target=self.start_sending_data, args=(nb_devices, interval, data_size, destination_path, payload_file_path))
            thread.start()
            
            
        def send_data_item(self, nb_device, data_size, path, payload_file_path, payload=None):
            
            def resp_success(result):
                self.logger.info("Message sent successfully !! %s", result)
            
            def resp_error(result):
                self.logger.info("Error sending message !! %s", result)
            
            
            def send_message():
                self.logger.info("Sending Message")
                request = CreateRequestIndication(path=path, resource=payload, content_type="application/json")
    
                split_path = path.split("/")
                get_index = split_path.index("applications")
                app_id = split_path[get_index + 1]
    
                request.targeted_appid = app_id
                request.originator = originator
                response = self.api.send_request_indication(request)
                response.then(resp_success, resp_error)
                
            
            if payload_file_path is None:
                dummy = "Dummy "
                #Sample default Message
                if data_size is not None:
                    # Create Dummy Message of size "data_size"
                    
                    effective_size = data_size - 48
                    msg = "a" * effective_size
                    payload = dumps({"key":msg}) # getsizeof of empty msg is :: 48 -- > getsizeof(dumps({"key":msg})) is 48
                    
                    originator = None
            else:
                originator = None
                dummy = ""
                
            payload_size = getsizeof(payload)
            self.logger.info("%sMessage is %s of size %s bytes", dummy, payload, payload_size)
            
            if data_size is not None:
                if data_size < payload_size:
                    self.logger.warning("Payload size exceeded %s bytes", data_size)

            # Sending message
            t = timeit(lambda: send_message(), number=nb_device)
            self.total_time = t
            
         
        def send_data(self, nb_devices, data_size, destination_path, payload_file_path):
            if not self.sending_data:
                return
            
            if destination_path is not None:
                path = destination_path 
            else:
                self.log.error("Destination Path is not Available. Default path is None")
                return
            
            if payload_file_path is not None:
                try:
                    with open(payload_file_path) as f:
                        try:
                            payload = load(f)
                            payload = dumps(payload)
                        except:
                            self.logger.error("Some errors while reading the contents. \
                                            Possibly JSON format error. Setting Payload to Default")
                            payload = None
                except IOError:
                    self.logger.error("Couldn't open the file. Verify the path.")
                    return
            else:
                payload = None
            
            #for i in range(nb_devices):
            self.send_data_item(nb_devices, data_size, path, payload_file_path, payload=payload)
        
        
        def start_sending_data(self, nb_devices, interval, data_size, destination_path, payload_file_path):
            def success_handle(result):
                self.send_interval_data(nb_devices, interval, \
                        data_size, destination_path, payload_file_path)
            
            def success_handle_1(result):
                self.send_data(nb_devices, data_size, destination_path, payload_file_path)
            
            def error_handle(result):
                self.logger.error("Error occurred. %s", result)
                self.sending_data = False
                return 
                
            self.sending_data=True
            path = destination_path
            split_path = path.split("/")
            path = "/".join(split_path[:len(split_path)-1])
            
            request = RetrieveRequestIndication(path)
            response = self.api.send_request_indication(request)
            
            if interval !=0:
                response.then(success_handle, error_handle)
            else:
                response.then(success_handle_1, error_handle)
        
        def send_interval_data(self, nb_devices, interval, data_size, destination_path, payload_file_path):
            while self.sending_data:
                
                self.send_data(nb_devices, data_size, destination_path, payload_file_path)

                total_delay = self.total_time
                
                self.logger.info("Total delay is %s", total_delay)
                avg_delay = total_delay/nb_devices
                self.logger.info("Average delay is %s", avg_delay)
                if interval-total_delay > 0:
                    interval = interval-total_delay
                else:
                    interval = 1
                filename = "delay_measurements_" + str(self.counter) + ".db"
                s = shelve.open(filename)
                try:
                    config_json = {"nb_devices" : nb_devices, "interval" : interval, "data_size" : data_size}
                    s["iteration_" + str(self.db_iteration_counter)] = {"total_delay" : total_delay, "avg_delay" : avg_delay, "config_json" : config_json}
                    self.db_iteration_counter += 1
                finally:
                    s.close()
                sleep(interval)
        
        def stop_sending_data(self):
            self.sending_data=False
    

class EmulatedDevicesPlugin(Plugin):
    def _init(self):
        self.events.resource_created.register_handler(self._handle_content_inst_created, ContentInstance)
        self.config_mgmt_app = config_mgmt_app(self.api)
        self._initialized()
    
    def _start(self):
        self.config_mgmt_app._start()
        self.obj_dict = {}
        self.counter = 0
        self._started()
        
    def _stop(self):
        self._stopped()
    
    def _handle_content_inst_created(self, instance, request_indication):
        temp_obj_dict = deepcopy(self.obj_dict)
        for key in temp_obj_dict.keys():
            self.obj_dict[key].stop_sending_data()
            del self.obj_dict[key]
        
        try:
            dev_dict = loads(b64decode(request_indication.resource["content"]["$t"]))
        except KeyError:
            dev_dict = loads(b64decode(request_indication.resource["content"]["binaryContent"]))
        
        traffic_group = dev_dict["traffic_group"]
        nb_devices = traffic_group.get("nb_devices", DEFAULT_NB_DEVICES)
        interval = traffic_group.get("interval", DEFAULT_INTERVAL)
        data_size = traffic_group.get("data_size", DEFAULT_DATA_SIZE)
        destination_path = dev_dict.get("destination_path", DEFAULT_DESTINATION_PATH)
        payload_file_path = dev_dict.get("payload_file_path", DEFAULT_PAYLOAD_FILE)
        
        
        if interval == 0:
            self.logger.info(" --- DELAY MEASUREMENT SUMMARY ----")
            for val in range(self.counter):
                filename = "delay_measurements_" + str(val) + ".db"
                self.logger.info("Filename :: %s", filename)
                s = shelve.open(filename)
                counter = 0
                display = True
                condn = True
                try:
                    while condn:
                        if "iteration_" + str(counter) in s:
                            content = s['iteration_' + str(counter)]
                            if display:
                                self.logger.info("Configuration: devices=%s, interval=%s, data_size=%s", content["config_json"]["nb_devices"], \
                                                 content["config_json"]["interval"], content["config_json"]["data_size"])
                                display = False
                            self.logger.info("Iteration %s, Total_Delay=%s, Average_Delay=%s", counter, content["total_delay"], content["avg_delay"])
                            counter += 1
                        else:
                            condn = False
                finally:
                    s.close()
            return


        
        self.obj_dict["obj_" + str(self.counter)] = MsgSender(self.api, nb_devices, interval, data_size, destination_path, payload_file_path, self.counter)
        self.counter += 1
        
    
    

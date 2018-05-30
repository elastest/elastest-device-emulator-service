from openmtc_app.onem2m import XAE
from openmtc_onem2m.model import Container
import gevent
import uuid
import os
import signal

def _register_App():
     # register the application - 0
     #request_ID = (uuid.uuid4().hex)[:12]
     request_ID = str('app_' + _generate_request_uuid())
     # append the request to requests
     request = [{'register':{'application':{'app_ID':self.app_ID,
     'request_ID':request_ID}}}]
     request_path = self.orch_path + 'request'
     self.push_content(request_path, request)
     self.requests.append(request_ID)
     self.logger.info('sent request to register application')
     gevent.sleep(3)
     print("Application have been registerd")

def _register_Sensor():
    request_ID = _generate_request_uuid()
    request_ID = str('app_' + request_ID)
    request_ID = str('sensor_temp_' + request_ID)
    request = [{'register':{'sensor':{'app_ID':self.app_ID,
        'request_ID':request_ID, 'sensor_type':'temperature'}}}]
    self.push_content(request_path, request)
    self.requests.append(request_ID)
    self.logger.info('sent request to register sensor')
    gevent.sleep(3)
    print("Sensor have been registerd")

def _register_Actuator():
    request_ID = _generate_request_uuid()
    request_ID = str('actuator_simple_' + request_ID)
    request = [{'register':{'actuator':{'app_ID':self.app_ID,
        'request_ID':request_ID, 'actuator_type':'simple'}}}]
    self.push_content(request_path, request)
    self.requests.append(request_ID)
    self.logger.info('sent request to register actuator')
    gevent.sleep(3)

def _modify_Sensor():
    # switch on the temperature sensor - 3
    #request_ID = (uuid.uuid4().hex)[:12]
    request_ID = str('modify_' + _generate_request_uuid())
    sensor_name = self.requests_ID[self.requests[1]]['conf']['name']
    self.requests.append(request_ID)
    request = [{'modify':{'app_ID':self.app_ID, 'request_ID':
        request_ID, 'name' : sensor_name, 'conf':{'onoff':'ON', 'period':5}}}]
    request_path = self.sensor_temp_path + 'request'
    self.push_content(request_path, request)
    print("Sensorregister_app")


def _modify_Actuatur():
    # switch on the temperature sensor - 3
    #request_ID = (uuid.uuid4().hex)[:12]
    #request_ID = (uuid.uuid4().hex)[:12]
    request_ID = str('modify_' + _generate_request_uuid())
    actuator_name = self.requests_ID[self.requests[2]]['conf']['name']
    self.requests.append(request_ID)
    request = [{'modify':{'app_ID':self.app_ID, 'request_ID':
        request_ID, 'name' : actuator_name, 'conf':{'delay':3}}}]
    request_path = self.actuator_simple_path + 'request'
    self.push_content(request_path, request)
    print("Actuator have been modified")

def _generate_request_uuid():
    x = (uuid.uuid4().hex)[:12]
    return x

#Create dictionary and store the functions
functions_dict = {
    "registerApp": _register_App,
    "registerSensor" : _register_Sensor,
    "registerActuator" : _register_Actuator,
    "modifySensor" : _modify_Sensor,
    "modifyActuatur" : _modify_Actuatur
}

register_app = functions_dict['registerApp']
register_sensor = functions_dict['registerSensor']
register_actuator = functions_dict['registerActuator']
modify_Sensor = functions_dict['modifySensor']
modify_Actuatur = functions_dict['modifyActuatur']

#to call the function from the dictionary
# register_app()
# register_sensor()

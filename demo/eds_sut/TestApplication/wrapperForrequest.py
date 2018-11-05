from openmtc_app.onem2m import XAE
from openmtc_onem2m.model import Container
import gevent
import uuid
import os
import signal

class Wrapper(XAE):
    def __init__(self, *args, **kw):
        super(Wrapper, self).__init__(*args, **kw)

        self.orch_path = 'onem2m/EDSOrch/edsorch/'
        self.sensor_temp_path = 'onem2m/TemperatureSensor/'
        self.sensor_pressure_path = 'onem2m/PressureSensor/'
        self.actuator_simple_path = 'onem2m/SimpleActuator/'

        self.requests_ID = {}
        self.sensors = {}
        self.actuators = {}
        self.app_ID = "testapplication"
        self.requests = []
        self.setup = False

    def _on_shutdown(self):
        # deregister the application - 4
        request_ID = (uuid.uuid4().hex)[:12]
        request_ID = str('deregister_'+ request_ID)
        request = [{'deregister':{'application':{'app_ID':self.app_ID, 'request_ID':
        request_ID}}}]
        request_path = self.orch_path + 'request'
        self.requests.append(request_ID)
        self.push_content(request_path, request)


        # to call the function from the dictionary
        # register_app()
        # register_sensor()

    def _register_App(self):
        # register the application - 0
        request_ID = (uuid.uuid4().hex)[:12]
        # append the request to requests
        request_ID = str('app_' + request_ID)
        request = [{'register':{'application':{'app_ID':self.app_ID,
            'request_ID':request_ID}}}]
        request_path = self.orch_path + 'request'
        self.push_content(request_path, request)
        self.requests.append(request_ID)
        self.logger.info('sent request to register application')
        gevent.sleep(3)

    def _register_Actuator(self):
        # register the actuator - 2
        request_ID = (uuid.uuid4().hex)[:12]
        request_ID = str('actuator_simple_' + request_ID)
        request = [{'register':{'actuator':{'app_ID':self.app_ID,
        'request_ID':request_ID, 'actuator_type':'simple'}}}]
        request_path = self.orch_path  + 'request'
        self.push_content(request_path, request)
        self.equest = [{'register':{'application':{'app_ID':self.app_ID,
        'request_ID':request_ID}}}]
        self.requests.append(request_ID)
        self.logger.info('sent request to register actuator')
        gevent.sleep(3)

    def _register_Temp_Sensor(self):
        # register the sensor - 1
        request_ID = (uuid.uuid4().hex)[:12]
        request_ID = str('sensor_temp_' + request_ID)
        request = [{'register':{'sensor':{'app_ID':self.app_ID,
        'request_ID':request_ID, 'sensor_type':'temperature'}}}]
        request_path = self.orch_path + 'request'
        self.push_content(request_path, request)
        self.requests.append(request_ID)
        self.logger.info('sent request to register sensor')
        gevent.sleep(3)

    def _register_Pressure_Sensor(self):
        # register the sensor - 1
        #request_ID = (uuid.uuid4().hex)[:12]
        request_ID = str('sensor_pressure_' + (uuid.uuid4().hex)[:12])
        request = [{'register':{'sensor':{'app_ID':self.app_ID,
        'request_ID':request_ID, 'sensor_type':'pressure'}}}]
        request_path = self.orch_path + 'request'
        self.push_content(request_path, request)
        self.requests.append(request_ID)
        self.logger.info('sent request to register sensor')
        gevent.sleep(3)
        print("pressue Sensor is registered")


    def _modify_Sensor(self):
        # switch on the temperature sensor - 3
        request_ID = (uuid.uuid4().hex)[:12]
        request_ID = str('modify_' + request_ID)
        sensor_name = self.requests_ID[self.requests[2]]['conf']['name']
        print(sensor_name)
        self.requests.append(request_ID)
        request = [{'modify':{'app_ID':self.app_ID, 'request_ID':
        request_ID, 'name' : sensor_name, 'conf':{'onoff':'ON', 'period':5}}}]
        print("---------------------------------------")
        print("im the modify sensor")
        print("---------------------------------------")
        request_path = self.sensor_temp_path + 'request'
        self.push_content(request_path, request)

    def _modify_Actuatur(self):
        request_ID = (uuid.uuid4().hex)[:12]
        request_ID = str('modify_' + request_ID)
        actuator_name = self.requests_ID[self.requests[3]]['conf']['name']
        self.requests.append(request_ID)
        print(self.requests)
        request = [{'modify':{'app_ID':self.app_ID, 'request_ID':
        request_ID, 'name' : actuator_name, 'conf':{'delay':3}}}]
        request_path = self.actuator_simple_path + 'request'
        self.push_content(request_path, request)

    def _subscribe_Sensor(self, requests, id):
        self.logger.info('waiting for system to be established...')
        gevent.sleep(5)
        sensor_request = self.requests[id]
        print(sensor_request)
        self.add_container_subscription(self.requests_ID[sensor_request]['conf']['path'],
            self.handle_temperature_sensor)

    def _subscribe_Actuator(self, id, requests):
        if any(id in s for s in requests) == True:
            actuator_request = self.requests[requests.index(s)]
            self.add_container_subscription(self.requests_ID[actuator_request]['conf']['out_path'], self.handle_actuator_out)
        else:
            print("Actuator not existing")

    #Create dictionary and store the functions
    functions_dict = {
    "registerApp": _register_App,
    "registerSensor" : _register_Temp_Sensor,
    "registerPressureSensor" : _register_Pressure_Sensor,
    "registerActuator" : _register_Actuator,
    "modifySensor" : _modify_Sensor,
    "modifyActuatur" : _modify_Actuatur
    }

    register_app = functions_dict['registerApp']
    register_sensor = functions_dict['registerSensor']
    register_pressure_sensor = functions_dict['registerPressureSensor']
    register_actuator = functions_dict['registerActuator']
    modify_Sensor = functions_dict['modifySensor']
    modify_Actuatur = functions_dict['modifyActuatur']

    def app_shutdown(self):
        os.kill(os.getpid(), signal.SIGTERM)

    def handle_actuator_out(self, cnt, con):
        self.logger.info(':actuator:' + con)
        self.logger.info(cnt)

    def handle_temperature_sensor(self, cnt, con):
        # actual logic is placed here
        for str in self.requests:
            if 'actuator_simple' in str:
                x = self.requests.index(str)
                actuator_request = self.requests[x]
                print(actuator_request)
                self.logger.info(':sensor:'+ con)
                self.logger.info(cnt)
                if float(con) > 30:
                    self.push_content(self.requests_ID[actuator_request]['conf']['in_path'],
                            con)



    def handle_orch_response(self, cnt, con):
        print("debug orch")
        reply = con
        # check if reply is for this application
        if 'app_ID' in reply and reply['app_ID'] == self.app_ID:
            # check the result in the reply
            if 'result' in reply and reply['result'] == 'SUCCESS':
                # the reply contains, everything went well
                request_ID = reply['request_ID']
                self.requests_ID[request_ID] = reply
                print("++++++++++++++++++++++++++++")
                self.logger.info(request_ID + ' was a success')

            else:
                request_ID = reply['request_ID']
                error_string = reply['error_string']
                self.logger.info(request_ID + ' did not succeed')
                self.logger.info('error ' + error_string)

        else:
            self.logger.info('received message not for this app')

    def handle_temp_response(self, cnt, con):
        reply = con
        if 'app_ID' in reply and reply['app_ID'] == self.app_ID:
            if 'result' in reply and reply['result'] == 'SUCCESS':
                request_ID = reply['request_ID']
                self.logger.info(request_ID + ' was a success')

            else:
                request_ID = reply['request_ID']
                error = reply['error_string']
                self.logger.info(request_ID + ' did not succeed')
        else:
            self.logger.info('received message not for this app')

    def handle_pressure_response(self, cnt, con):
        reply = con
        print("-----------------------------------")
        print(reply)
        print("-----------------------------------")
        if 'app_ID' in reply and reply['app_ID'] == self.app_ID:
            if 'result' in reply and reply['result'] == 'SUCCESS':
                request_ID = reply['request_ID']
                self.logger.info(request_ID + ' was a success')
            else:
                request_ID = reply['request_ID']
                error = reply['error_string']
                self.logger.info(request_ID + ' did not succeed')
        else:
            self.logger.info('received message not for this app')

    def handle_simple_response(self, cnt, con):
        reply = con
        print("debug simple response")
        print(reply)
        if 'app_ID' in reply and reply['app_ID'] == self.app_ID:
            if 'result' in reply and reply['result'] == 'SUCCESS':
                request_ID = reply['request_ID']
                self.logger.info(request_ID + ' was a success')

            else:
                request_ID = reply['request_ID']
                error = reply['error_string']
                self.logger.info(request_ID + ' did not succeed')
        else:
            self.logger.info('received message not for this app')

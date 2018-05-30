_from openmtc_app.onem2m import XAE
from openmtc_onem2m.model import Container
import time
import uuid
import subprocess
from threading import Timer
import gevent
from openmtc_onem2m.client.http import OneM2MHTTPClient
from openmtc_onem2m.transport import OneM2MRequest

class EDSOrch(XAE):

    def __init__(self, *args, **kw):
        super(EDSOrch, self).__init__(*args, **kw)
        self.logger.debug('initializing')

        # contains all the registered apps in the format of
        # {'app_ID': {'sensors':[list of sensor names],
        # 'actuators': {list of actuator names}}
        self.registered_apps = {}
        self.status = 'IDLE'

        # Holds the expected request templates for a request from the user
        self.request_template = {'register':{}, 'deregister':{}}
        self.request_template['register']['application'] = ['app_ID', 'request_ID']
        self.request_template['register']['sensor'] = ['app_ID', 'request_ID',
                'sensor_type']
        self.request_template['register']['actuator'] = ['app_ID', 'request_ID',
                'actuator_type']
        self.request_template['deregister']['application'] = {'app_ID', 'request_ID'}
        # request format

        # with register
        # {'register' : {'application':{'app_ID':'uuid', 'request_ID': 'uuid'}}}
        # {'register' : {'sensor':{'app_ID':'uuid', 'request_ID': 'uuid',
        # 'sensor_type': 'temperature'}}
        # {'register': {'actuator': {'app_ID': 'uuid', 'request_ID': 'uuid',
        # 'actuator': 'relay'}}}

        # with deregister
        # {'deregister': {'application':{'app_ID': 'uuid', 'request_ID': 'uuid'}}}

        # reply format for SUCCESS
        # {'request_ID': 'uuid', 'result': 'SUCCESS', 'conf': dict(conf),
        # 'error': 'error_string'}

        # this list is used to add all the available sensors that EDS can provide
        # when an application registers. This list needs to be updated when a new
        # sensor is added to manifest
        self.available_sensors = ['temperature']
        # this list is used to add all the available actuators that EDS can provide
        # when an application registers. This list needs to be update when a new
        # actuator is added
        self.available_actuators = ['simple']

        # contains the reference for process components
        self.process_list = []
    def _on_register(self):
        # create the channels for orch by creating respective containers

        # first create orch container
        self.orch_cnt = Container(resourceName='edsorch',
                labels=['elastest:edsorch'],
                maxNrOfInstances=5)
        self.orch_cnt = self.create_container(None, self.orch_cnt)

        #create request container
        self.request_cnt = Container(resourceName='request',
                labels=['elastest:edsorch:request'],
                maxNrOfInstances=5)
        self.request_cnt = self.create_container(self.orch_cnt,
                self.request_cnt)
        self.add_container_subscription(self.request_cnt,
                self._handle_request)

        # create response container
        self.response_cnt = Container(resourceName='response',
                labels=['elastest:edsorch:response'],
                maxNrOfInstances=5)
        self.response_cnt = self.create_container(self.orch_cnt,
                self.response_cnt)
        #self.add_container_subscription(self.response_cnt,
        #        self.handle_response)

        # create status container
        self.status_cnt = Container(resourceName='status',
                labels=['elastest:edsorch:status'],
                maxNrOfInstances=5)
        self.status_cnt = self.create_container(self.orch_cnt,
                self.status_cnt)
        #self.add_container_subscription(self.status_cnt,
        #        self.handle_status)

        # call each available sensor's corresponding script
        # also subscribe to their response channels
        for sensor in self.available_sensors:
            # execute the sensor script
            script = "/usr/local/src/openmtc/apps/" + sensor + "-sensor"
            component_path = "onem2m/" + sensor.title() + "Sensor/response"
            component_name = sensor + "_sensor"
            process = subprocess.Popen([script, "-v"])
            self.process_list.append(process)
            # add subscription after 5 seconds
            gevent.spawn_later(5, self.subscribe_component_response, component_name,
                    component_path)
            #Timer(5, self.subscribe_component_response, [component_name,
            #    component_path]).start()

        for actuator in self.available_actuators:
            # execute the actuator script
            script = "/usr/local/src/openmtc/apps/" + actuator + "-actuator"
            component_path = "onem2m/" + actuator.title() + "Actuator/response"
            component_name = actuator + "_actuator"
            subprocess.Popen([script, "-v"])
            self.process_list.append(process)
            # add subscription after 5 seconds
            gevent.spawn_later(5, self.subscribe_component_response, component_name,
                    component_path)
            #Timer(5, self.subscribe_component_response, [component_name,
            #    component_path]).start()

        # start endless loop
        self.logger.info('all registration finished')
        #time.sleep(1)
        #self.push_content('onem2m/EDSOrch/edsorch/request', [{"register":{'application':{'app_ID':'some_ID', 'request_ID': 'some1'}}}])
        #gevent.sleep(7)
        #self.push_content('onem2m/EDSOrch/edsorch/request', [{"register":{'actuator':{'app_ID':'some_ID', 'request_ID': 'some', 'actuator_type':'simple'}}}])
        #gevent.sleep(4)
        #self.push_content('onem2m/EDSOrch/edsorch/request', [{"register":{'sensor':{'app_ID':'some_ID', 'request_ID': 'some1', 'sensor_type':'temperature'}}}])
        #self.run_forever()

    def subscribe_component_response(self, component_name, component_path):
        # prepare a handle function
        def add_handler(cnt, con):
            self.push_content(self.response_cnt, con)
        handler_name = "handle_" + component_name + "_response"
        add_handler.__name__ = handler_name
        setattr(self, add_handler.__name__, add_handler)
        func = getattr(self, handler_name)
        self.logger.info('executes timer handle')
        self.add_container_subscription(component_path, func)

    def _on_shutdown(self):
        for process in self.process_list:
            process.kill()

    def handle_response(self, cnt, con):
        self.logger.info(con)

    def handle_status(self, cnt, con):
        self.logger.info(con)

    def _handle_request(self, cnt, con):
        _response_cnt = self.response_cnt
        _status_cnt = self.status_cnt
        timestamp = format(round(time.time(), 3), '.3f')
        status_data = [{'n': 'orchestrator',
            't': timestamp,
            's': str(self.status)}]

        if self.status == 'IDLE':
            self.status = 'BUSY'
            status_data[0]['s'] = self.status
            self.push_content(_status_cnt, status_data)

            request = con[0]
            # analyze the incoming request
            # analyze if all the info is available already in the request,
            # based on the incoming request
            # compare with the request and the expected information
            # Analyze the provided strings for each request from application
            # This where the request is checked for errors
            valid, error_string = self.check_request_content(request)

            # check if the request was valid
            # if not valid, send an error response
            if not valid:
                self.push_content(_response_cnt, {'result':'FAIL',
                    'request_ID':'FFFFFFFF', 'error_string' : error_string})
                self.status = 'IDLE'
                status_data[0]['s'] = str(self.status)
                timestamp = format(round(time.time(), 3), '.3f')
                status_data[0]['t'] = timestamp
                self.push_content(_status_cnt, status_data)
                return


            # a valid request was found
            # process it now
            # the request could contain at most register and deregister
            for key in request:
                # if key is register
                if key == 'register':
                    request_1 = request[key]
                    # iterate over request_1
                    for key_1 in request_1:
                        lambda key_1: self.handle_register_application(request) if key_1 == 'application'
                        else (self.handle_register_sensor(request) if key_1 = 'sensor'
                        else (self.handle_register_actuator(request) if key_1 = 'actuator')
                        else self.logger.info("unknown component"))

                        '''if key_1 == 'application':
                            self.handle_register_application(request)
                        elif key_1 == 'sensor':
                            self.handle_register_sensor(request)
                        elif key_1 == 'actuator':
                            self.handle_register_actuator(request)
                        else:
                            self.logger.info("unknown component")'''

                elif key == 'deregister':
                    request_1 = request[key]
                    for key_1 in request_1:
                        if key_1 == 'application':
                            self.handle_deregister_application(request)

            self.status = 'IDLE'
            status_data[0]['s'] = str(self.status)
            timestamp = format(round(time.time(), 3), '.3f')
            status_data[0]['t'] = timestamp
        self.push_content(_status_cnt, status_data)

    def handle_register_application(self, request):
        # check if application name is already registered
        app_ID = str(request['register']['application']['app_ID'])
        request_ID = str(request['register']['application']['request_ID'])
        if app_ID in self.registered_apps:
            result = 'FAIL'
            error_string = 'app_ID already registered with orchestrator'
            reply = {'result': result, 'request_ID': request_ID, 'response': {},
                    'error_string': error_string}
            self.push_content(self.response_cnt, reply)
        # request format
        # {'register' : {'application' : {'app_ID':'uuid', 'request_ID': 'uuid'}}}
        label = 'elastest:application'
        # create a container with the name of app_ID
        app_cnt = Container(resourceName=app_ID,
                labels=[label],
                maxNrOfInstances=1)
        app_cnt = self.create_container(None, app_cnt)
        label = label + ':sensors'
        # create a sensors container
        sensors_cnt = Container(resourceName='sensors',
                labels=[label],
                maxNrOfInstances=1)
        sensors_cnt = self.create_container(app_cnt, sensors_cnt)
        # create an actuators container
        label = 'elastest:application:actuators'
        actuators_cnt = Container(resourceName='actuators',
                labels=[label],
                maxNrOfInstances=1)
        actuators_cnt = self.create_container(app_cnt, actuators_cnt)
        # attach containers for future possible types of actuators
        # reply format
        # {'request_ID': 'uuid', 'result': 'SUCCESS', 'conf': dict(conf),
        # 'error': 'error_string'}
        result = 'SUCCESS'
        error_string = ''
        conf = {'path' : app_cnt.path}
        reply = {'request_ID' : request_ID, 'result' : result, 'conf' : conf,
                'error_string' : error_string}
        self.registered_apps[app_ID] = {'path': app_cnt.path, 'sensors': [],
                'actuators':[]}
        self.push_content(self.response_cnt, reply)

    def _generate_request_uuid():
        x = (uuid.uuid4().hex)[:12]
        return x

    def handle_register_sensor(self, request):
        app_ID = str(request['register']['sensor']['app_ID'])
        request_ID = str(request['register']['sensor']['request_ID'])
        sensor_type = str(request['register']['sensor']['sensor_type'])
        # check if the app is registered with the orchestrator
        if app_ID not in self.registered_apps:
            result = 'FAIL'
            error_string = 'register:sensor:app not registered with orchestrator\n'
            reply = {}
            reply['request_ID'] = request_ID
            reply['app_ID'] = app_ID
            reply['result'] = result
            reply['error_string'] = error_string
            self.push_content(self.response_cnt, reply)

        sensor_name = _generate_request_uuid()
        data_path = 'onem2m/EDSOrch/' + app_ID + '/sensors'
        request = {'register':{'request_ID': request_ID,
            'app_ID': app_ID}}
        if sensor_type == 'temperature':
            # add the sensor name to the application
            sensor_name = 'temp_' + sensor_name
            request['register']['name'] = sensor_name
            request['register']['path'] = data_path
            self.registered_apps[app_ID]['sensors'].append(sensor_name)
            request_path = 'onem2m/TemperatureSensor/request'
            self.push_content(request_path, [request])

        else:
            result = 'FAIL'
            error_string = 'register:sensor:required sensor not found in manifest\n'
            reply = {'result': result, 'error_string': error_string,
                    'request_ID': request_ID, 'app_ID':app_ID}
            self.push_content(self.response_cnt, reply)

    def handle_register_actuator(self, request):
        app_ID = str(request['register']['actuator']['app_ID'])
        request_ID = str(request['register']['actuator']['request_ID'])
        actuator_type = str(request['register']['actuator']['actuator_type'])
        #check if the app is registered with the orchestrator
        if app_ID not in self.registered_apps:
            result = 'FAIL'
            error_string = 'register:actuator:app not registered with the orchestrator\n'
            reply = {}
            reply['request_ID'] = request_ID
            reply['result'] = result
            reply['error_string'] = error_string
            reply['conf'] = {}
            self.push_content(self.response_cnt, reply)

        actuator_name = _generate_request_uuid()
        data_path = 'onem2m/EDSOrch/' + app_ID + '/actuators'
        request = {'register':{'request_ID': request_ID, 'app_ID':app_ID}}
        if actuator_type == 'simple':
            # add the actuator name to the application
            actuator_name = 'simple_' + actuator_name
            request['register']['name'] = actuator_name
            request['register']['path'] = data_path
            self.registered_apps[app_ID]['actuators'].append(actuator_name)
            request_path = 'onem2m/SimpleActuator/request'
            self.push_content(request_path, [request])
        else:
            result = 'FAIL'
            error_string = 'register:actuator:required actuator not found in manifest\n'
            reply = {'result': result, 'error_string':error_string,
                    'request_ID':request_ID, 'app_ID': app_ID}
            self.push_content(self.response_cnt, reply)

    def handle_deregister_application(self, request):
        # check if the app is registered
        app_ID = request['deregister']['application']['app_ID']
        request_ID = request['deregister']['application']['request_ID']
        if not app_ID in self.registered_apps:
            result = 'FAIL'
            error_string = 'deregister:application:app_ID not found to be registered with orchestrator\n'
            reply = {'result':result, 'error_string': error_string, 'app_ID': app_ID,
                    'request_ID': request_ID}
            self.push_content(self.response_cnt, reply)

        # app_ID was found to be registered
        # deregister all the sensors, by sending shutdown to all sensors
        for sensor_name in self.registered_apps[app_ID]['sensors']:
            request = [{'modify':{'name':sensor_name, 'conf':{'onoff':'OFF'},
                'request_ID':request_ID, 'app_ID':app_ID}}]
            if 'temp' in sensor_name:
                pass
                self.push_content('onem2m/TemperatureSensor/request', request)

        for actuator_name in self.registered_apps[app_ID]['actuators']:
            request = [{'modify':{'name':actuator_name, 'request_ID':request_ID,
                'app_ID': app_ID, 'conf':{}}}]
            if 'simple' in actuator_name:
                pass
                self.push_content('onem2m/SimpleActuator/request', request)

        # pop the app_ID from the registered apps
        self.registered_apps.pop(app_ID)
        #client = OneM2MHTTPClient("http://localhost:8000", False)
        #path = "onem2m/" + app_ID
        #onem2m_request = OneM2MRequest("delete", to=path)
        #promise = client.send_onem2m_request(onem2m_request)
        #response = promise.get()
        #self.logger.info(str(response.response_status_code))

    def decision(result):
        if result == 1:
            return "continue"
        else:
            return pass

    def check_request_content(self, con):
        request = con
        error_string = ''
        valid_request = True

        # check if the request is an empty dictionary
        if not isinstance(request, dict):
            return False, "Request is not a dictionary"
        if bool(request) == False:
            return False, "Request dictionary is empty"
        self.logger.debug('check_request: Non-empty request dictionary received')

        # check if the first element is register or deregister, else continue
       # this loop can iterate twice if register and deregister are present
        def test_func(element):
            # if available key is not register or deregister flag an error
            # update error string and valid_request
            f = lambda key: (False, "valid first key not found") if key not in ['register', 'deregister'] else (
            True, "")
            g = lambda result: 1 if result == False else 0
            # decision = [continue, pass]
            valid, error = (f(key))
            if decision(g(valid)) ==
                self.logger.debug('check_request: Valid first level key found')
            request_1 = request[key]

            # A register or deregister key word was found
            # check if the key holds a dictionary, else up date error and continue
            if not isinstance(request_1, dict):
                valid_request = False
                error_string = error_string + 'the element of ' + key + ' not a dictionary\n'
                continue
            self.logger.debug('check_request: element of first level key is a dictionary')
            # Check if request_1 is empty
            if not request_1:
                valid_request = False
                error_string = error_string + 'the dictionary of ' + key + ' is empty\n'
                continue
            self.logger.debug('check_request: element of first level key is not empty')

            if not isinstance(request_2, dict):
                    valid_request = False
                    error_string = error_string + 'element of ' + key_1 + ' is not a dictionary\n'
                    continue

            request_2 = request_1[key_1]
            rgstr = lambda key, key_1: (False, error_string + key_1 + ' not a valid application')
            if (key == 'register' and key_1 not in ['application', 'sensor', 'actuator']) else (True, "")
            dergstr = lambda key, key_1: (False, error_string + key_1 + ' not a valid application')
            if (key == 'deregister' and key_1 not in ['application']) else (True, "")
            g = lambda result: 1 if result == False else 0
            # decision = [continue, pass]
            valid, error = (rgstr(key))
            valid, error = (dergstr(key))
            decision(g(valid))
            # check if key_1 is a valid key
            self.logger.debug('check_request: valid component key found')
            # check if the key dictionary element of key_1 is a dictionary
            # and not empty
            if not isinstance(request_2, dict):
                valid_request = False
                error_string = error_string + 'element of ' + key_1 + ' is not a dictionary\n'
                continue
            if not request_2:
                valid_request = False
                error_string = error_string + 'dictionary of ' + key_1 + ' is an empty dictionary\n'
                continue
            self.logger.debug('check_request: element of component key is a non empty dictionary')

            # The dictionary component was found to be not empty
            # check if required fields are present in the dictionary
            diff = set(self.request_template[key][key_1]) - set(request_2.keys())

            if len(diff) > 0:
                self.logger.debug('check_request: Not all required fields present in the component request')
                valid_request = False
                for field in diff:
                    error_string = error_string + key + ':' + key_1 + ':' + \
                                   field + ' not found in request\n'

        new_request = filter(test_func, request)
        return new_request["valid_request"], new_request["error_string"]
from openmtc_app.onem2m import XAE
from openmtc_onem2m.model import Container
import time
from threading import Timer
from random import uniform
import gevent

class TemperatureSensor(XAE):

    def __init__(self, *args, **kw):
        super(TemperatureSensor, self).__init__(*args, **kw)

        # request format has 2 keywords, register, modify
        # from the keywords we operate on the sensors
        # request format:
        # request format for register
        # {'register' : {'name' : 'unique_sensorname', 'path' : 'attachpath',
        # 'request_ID': 'uuid', 'app_ID': 'uuid'}}
        # request format for modify
        # {'modify' : {'name' : 'unique_sensorname', 'conf': dict(conf),
        # 'request_ID': 'uuid', 'app_ID':'uuid'}}
        # holds entry of all registered sensors
        # sensor names are mapped with their configurations added for example
        # self.registered_sensors['sensorName'] = {'onoff' : 'OFF', 'period' : 1,
        # 'shutdown' : 'NO', 'path' : 'sensor' registered path'}

        # reply format:
        # {'request_ID': 'uuid','result' : 'SUCCESS', 'response' : dict(conf),
        # 'error_string': error_string}

        self.registered_sensors = {}
        self.default_conf = {'onoff': 'OFF', 'period' : 1, 'shutdown' : False,
                'instance':None, 'timerinstance':None}
        self.status = 'IDLE'

        # Holds the expected request templates for a request from the user
        self.request_template = {}
        self.request_template['register'] = ['name', 'path', 'request_ID', 'app_ID']
        self.request_template['modify'] = ['name', 'conf', 'request_ID', 'app_ID']

    def _on_register(self):
        #create a request channel
        self.request_cnt = Container(resourceName='request',
                labels=['elastest:sensor:temperature:request'],
                maxNrOfInstances=5)
        self.request_cnt = self.create_container(None, self.request_cnt)
        # subscribe to the request channel
        self.add_container_subscription(self.request_cnt, self.handle_request)

        # create a response channel
        self.response_cnt = Container(resourceName='response',
                labels=['elastest:sensor:temperature:response'],
                maxNrOfInstances=5)
        self.response_cnt = self.create_container(None, self.response_cnt)

        # create a status channel
        self.status_cnt = Container(resourceName='status',
                labels=['elastest:sensor:temperature:status'],
                maxNrOfInstances=5)
        self.status_cnt = self.create_container(None, self.status_cnt)

        self.run_forever()


     def build_Reply_register_Request(request, self.registered_sensors[sensor_name]):
            reply = {type : 'register:sensor', 'app_ID' : request['app_ID'], 'result' : request['request_ID'] , 'conf' : self.registered_sensors[sensor_name], 'result' : 'SUCCESS'}
            return reply


        def build_Reply_modify_Request(request, self.registered_sensors[sensor_name]):
             reply = {type: 'modify:sensor', 'app_ID': request_1['app_ID'], 'result': request_1['request_ID'], 'conf': self.registered_sensors[sensor_name], 'result': 'SUCCESS'}
         if sensor_name not in self.registered_sensors:
            reply['result'] = 'FAIL'
            error_string = sensor_name + ' sensor name not registered\n'
            reply['error_string'] = error_string
            self.push_content(_response_cnt, reply)
            continue
            modify_conf = request_1['conf']
            for key_2 in modify_conf:
                self.registered_sensors[sensor_name][key_2] = \
                modify_conf[key_2]
                reply['result'] = 'SUCCESS'
                reply['conf'] = self.registered_sensors[sensor_name]
            return reply



     # con is a list. The index 0 element is a dictionary containing the request
    def handle_request(self, cnt, con):
        _response_cnt = self.response_cnt
        _status_cnt = self.status_cnt
        timestamp = format(round(time.time(), 3), '.3f')
        status_data = [{'n': 'temperature_sensor',
            't': timestamp,
            's': str(self.status)}]

        if self.status == 'IDLE':
            self.status = 'BUSY'
            status_data[0]['s'] = self.status
            self.push_content(_status_cnt, status_data)

            request = con[0]
            # analyze the incoming request
            valid, error_string = self.check_request_content(request)

            if not valid:
                self.push_content(_response_cnt, {'result':'FAIL',
                    'request_ID':'FFFFFFFF', 'error_string': error_string})
                self.status = 'IDLE'
                status_data[0]['s'] = str(self.status)
                timestamp = format(round(time.time(), 3), '.3f')
                status_data[0]['t'] = timestamp
                self.push_content(_status_cnt, status_data)

            # the request was valid
            # at most two requests/commands could be found in a request
            # register or modify
            # we iterate through the request
        for key in request:
            if key == 'register':
                request_1 = request[key]
                sensor_name = request_1['name']
                path = request_1['path']
                self.registered_sensors[sensor_name] = self.default_conf
                self.add_sensor_method(path, sensor_name)go
                replyRegister_= build_Reply_register_Request(request, sensor. registerd_sensor)
                self.push_content(_response_cnt, replyRegister_)

                elif key == 'modify':
                    # modify the sensor configuration
                    request_1 = request[key]
                    sensor_name = request_1['name']
                    modifyReply_ = build_Reply_modify_Request(request, sensor.registerd_sensor)
                    self.push_content(_response_cnt, modifyReply)
            self.status = 'IDLE'
            status_data[0]['s'] = str(self.status)
            timestamp = format(round(time.time(), 3), '.3f')
            status_data[0]['t'] = timestamp
        self.push_content(_status_cnt, status_data)

    def add_sensor_method(self, path, name):
        # containers on the given attach path
        sensor_name = name
        sensor_cnt = Container(resourceName=sensor_name,
                labels=['elastest:sensor:temperature'],
                maxNrOfInstances=1)
        sensor_cnt = self.create_container(path, sensor_cnt)
        # create a data container on top of sensor container
        data_cnt = Container(resourceName='data',
                labels=['elastest:sensor:temperature:data'],
                maxNrOfInstances=5)
        data_cnt = self.create_container(sensor_cnt, data_cnt)
        # create a class method to update sensor values
        def add_update_method(func, name):
            data = uniform(20,50)
            conf = self.registered_sensors[name]
            if not conf['shutdown']:
                gevent.spawn_later(float(conf['period']), func, func, name)
            if conf['onoff'] == 'ON':
                self.push_content(data_cnt, str(data))
        add_update_method.__name__ = str(sensor_name + '_func')
        setattr(self, add_update_method.__name__, add_update_method)
        funcname = sensor_name + '_func'
        sensorfunc = getattr(self, funcname)
        self.registered_sensors[sensor_name]['path'] = data_cnt.path
        self.registered_sensors[sensor_name]['name'] = sensor_name
        #self.call_timer(sensorfunc, name)
        sensorfunc(sensorfunc, name)


    def call_timer(self, func, name):
        sensorfunc = func
        conf = self.registered_sensors[name]
        if not conf['shutdown']:
            gevent.spawn_later(float(conf['period']), self.call_timer, func, name)
        if conf['onoff'] == 'ON':
            sensorfunc()

    def check_request_content(self, con):
        request = con
        error_string = ''
        valid_request = True

        if not isinstance(request, dict):
            return False, "Request is not a dictionary"

        # check if the request is an empty dictionary
        if not request:
            return False, 'Request dictionary is empty'

         def check_request(request):
            f = lambda key: (False, error_string + key + ' is not a valid request key\n') if key not in ['register','modify'] else (True, "")
            g = lambda result: 1 if result == False else 0
            valid, error = (f(key))
            decision(g(valid))
            request_1 = request[key]

        new_request = filter(test_func, request)
        return new_request["valid_request"], new_request["error_string"]


       for key in request:

            request_1 = request[key]
            if not isinstance(request_1, dict):
                valid_request = False
                error_string = error_string + 'the element of ' + key + ' not a dictionary\n'
                continue

            if not request_1:
                valid_request = False
                error_string = error_string + 'the dictionary of ' + key + ' is empty\n'
                continue

            diff = set(self.request_template[key]) - set(request_1.keys())

            if len(diff) > 0:
                valid_request = False
                for field in diff:
                    error_string = error_string + key + ':' + field + ' not found in request\n'

            return valid_request, error_string

from openmtc_app.onem2m import XAE
from openmtc_onem2m.model import Container
import time
from random import uniform
import gevent


class SimpleActuator(XAE):

    def __init__(self, *args, **kw):
        super(SimpleActuator, self).__init__(*args, **kw)

        # request format has 3 keywords register and modify
        # from keywords we operate on the actuators
        # request format:
        # request format for register
        # {'register':{'name': 'unique_actuator_name', 'conf': dict(conf),
        # 'request_ID':'uuid', 'app_ID':'uuid}}
        # request format for modify
        # {'modify': {'name':'unique_actuator_name', 'conf':dict(conf),
        # 'request_ID': 'uuid', 'app_ID':'uuid'}}

        # holds entry of all registered actuators
        # actuator names are mapped with their configurations added for example
        # self.registered_actuators['actuatorName'] = {'onoff':'OFF', 'delay': 1,
        # 'path': 'actuator data paht'}

        # reply format:
        # {'request_ID': 'uuid', 'result':'SUCCESS', 'response':dict(conf),
        # 'error_string': error_string'}

        self.registered_actuators = {}
        self.default_conf = {'onoff':'ON', 'delay':1}
        self.status = 'IDLE'

        # Holds the expected request templates for a request from the user
        self.request_template = {}
        self.request_template['register'] = ['name', 'path', 'request_ID', 'app_ID']
        self.request_template['modify'] = ['name', 'conf', 'request_ID', 'app_ID']

    def _on_register(self):
        # create a request channel
        self.request_cnt = Container(resourceName='request',
                labels=['elastest:actuator:simple:request'],
                maxNrOfInstances=5)
        self.request_cnt = self.create_container(None, self.request_cnt)
        # subscribe to the request channel
        self.add_container_subscription(self.request_cnt, self.handle_request)

        # create response channel
        self.response_cnt = Container(resourceName='response',
                labels=['elastest:actuator:simple:response'],
                maxNrOfInstances=5)
        self.response_cnt = self.create_container(None, self.response_cnt)

        # create status channel
        self.status_cnt = Container(resourceName='status',
                labels=['elastest:actuator:simple:status'],
                maxNrOfInstances=5)
        self.status_cnt = self.create_container(None, self.status_cnt)

        # start endless loop
        self.run_forever()

    def build_Reply_register_Request(request, self.registered_sensors[sensor_name]):
        reply = {type: 'register:sensor', 'app_ID': request['app_ID'], 'result': request['request_ID'],
        'conf': self.registered_sensors[sensor_name], 'result': 'SUCCESS'}
        return reply


    def build_Reply_modify_Request(request, self.registered_sensors[sensor_name]):
        reply = {type: 'modify:acuator', 'app_ID': request_1['app_ID'], 'result': request_1['request_ID']}
        if actuator_name not in self.registered_actuators:
            reply['result'] = 'FAIL'
            error_string = actuator_name + ' actuator name is not registered\n'
            reply['error_string'] = error_string
            self.push_content(_response_cnt, reply)
            continue
        modify_conf = request_1['conf']
        for key_2 in modify_conf:
            self.registered_actuators[actuator_name][key_2] = \
            modify_conf[key_2]
        reply['result'] = 'SUCCESS'
        reply['conf'] = self.registered_actuators[actuator_name]
        self.push_content(_response_cnt, reply)



    def handle_request(self, cnt, con):
        _response_cnt = self.response_cnt
        _status_cnt = self.status_cnt
        timestamp = format(round(time.time()))
        status_data = [{'n': 'simple_actuator',
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
                    'request_ID':'FFFFFFFF', 'error_string':error_string})
                self.status = 'IDLE'
                status_data[0]['s'] = self.status
                timestamp = format(round(time.time(), 3), '.3f')
                status_data[0]['t'] = timestamp
                self.push_content(_status_cnt, status_data)

            # the request was valid
            for key in request:
                if key == 'register':
                    request_1 = request[key]
                    actuator_name = request_1['name']
                    path = request_1['path']
                    self.registered_actuators[actuator_name] = self.default_conf
                    self.add_actuator(path, actuator_name)
                    replyReq = build_Reply_Register_Request(request_1, self.registered_sensors[sensor_name])
                    self.push_content(_response_cnt, replyReq)

                if key == 'modify':
                    request_1 = request[key]
                    actuator_name = request_1['name']
                    modify_req = build_Reply_modify_Request(request_1, self.registerd_sensors[sensor_name])
                    self.push_content(_response_cnt, modify_reqreply)
            self.status = 'IDLE'
            status_data[0]['s'] = str(self.status)
            timestamp = format(round(time.time(), 3), '.3f')
            status_data[0]['t'] = timestamp
        self.push_content(_status_cnt, status_data)

    def add_actuator(self, path, name):
        # containers on the given attach path
        actuator_name = name
        actuator_cnt = Container(resourceName=actuator_name,
                labels=['elastest:actuator:simple'],
                maxNrOfInstances=1)
        actuator_cnt = self.create_container(path, actuator_cnt)

        # create data in and data our containers
        data_in_cnt = Container(resourceName='data_in',
                labels=['elastest:actuator:simple:data_in'],
                maxNrOfInstances=5)
        data_in_cnt = self.create_container(actuator_cnt, data_in_cnt)

        data_out_cnt = Container(resourceName='data_out',
                labels=['elastest:actuator:simple:data_out'],
                maxNrOfInstances=5)
        data_out_cnt = self.create_container(actuator_cnt, data_out_cnt)

        def add_actuator_method(cnt, con):
            # forwards the data received on data in to data out with a delay
            delay = self.registered_actuators[actuator_name]['delay']
            gevent.sleep(delay)
            if self.registered_actuators[actuator_name]['onoff'] == 'ON':
                self.push_content(data_out_cnt, con)
        add_actuator_method.__name__ = str(actuator_name + '_func')
        setattr(self, add_actuator_method.__name__, add_actuator_method)
        funcname = actuator_name + '_func'
        actuatorfunc = getattr(self, funcname)
        #self.add_container_subscription(data_in_cnt, actuatorfunc)
        self.registered_actuators[actuator_name]['in_path'] = data_in_cnt.path
        self.registered_actuators[actuator_name]['out_path'] = data_out_cnt.path
        self.registered_actuators[actuator_name]['name'] = actuator_name
        # finally subscribe to the incoming data
        self.add_container_subscription(data_in_cnt, actuatorfunc)

   def check_request_content(self, con):
        request = con
        error_string = ''
        valid_request = True

        if not isinstance(request, dict):
            return False, "Request is not a dictionary"

        if not request:
            return False, "Request dictionary is empty"

        def check_request(request):
            f = lambda key: (False, error_string + key + ' is not a valid request key\n') if key not in ['register',
            'modify'] else (True, "")
            valid, error = (f(key))
            valid_request = valid

        return f(request), valid_request


        for key in request:
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

import json
from base64 import b64decode
from collections import deque

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from openmtc_app.onem2m import XAE
from openmtc_onem2m.model import CSETypeIDE, RemoteCSE, ResourceTypeE


class FrontEnd(XAE):
    remove_registration = True
    interval = 10
    max_values = 10

    def _on_register(self):
        # init variables
        self._known_remote_cses = {}
        self._discovered_devices = {}
        self._discovered_sensors = {}
        self._discovered_actuators = {}

        # incoming sockets
        self.runner.add_message_handler("echo", self._echo)
        self.runner.add_message_handler("getSensorList", self._get_sensor_list)
        self.runner.add_message_handler("getActuatorList",
                                        self._get_actuator_list)
        self.runner.add_message_handler("pushContent", self._push_content)

        # connected to backend or gateway?
        cse_base = self.get_resource(self.cse_base)
        if (cse_base.cseType == CSETypeIDE.MN_CSE or
                cse_base.cseType == CSETypeIDE.AEN_CSE):
            # discover gateway
            self._discover_cse(cse_base.CSE_ID + '/' + self.cse_base)
        else:
            # discover backend
            self._discover_cse(cse_base.CSE_ID + '/' + self.cse_base)
            # discover remote gateways
            self._get_remote_cses(cse_base)

    # socket handlers

    def _echo(self, data):
        self.emit('echo-back', {
            'message': 'foo',
            'clientId': data.get("clientId")
        })

    @staticmethod
    def _map_sensor_data(sensor):
        return {k: v if k != 'data' else list(v) for k, v in sensor.items()}

    def _get_sensor_list(self):
        self.emit('sensorList', map(self._map_sensor_data,
                                    self._discovered_sensors.values()))

    def _get_actuator_list(self):
        self.emit('actuatorList', self._discovered_actuators.values())

    def _push_content(self, target, content):
        if content == "ON":
            content = [{'v': 1.0}]
        else:
            content = [{'v': 0.0}]
        self.push_content(target, content)

    # get remote CSEs

    def _get_remote_cses(self, cse_base):

        def get_cse_base():
            handle_cse_base(self.get_resource(self.cse_base))

        def handle_cse_base(cb):
            for resource in cb.childResource:
                if (type(resource) == RemoteCSE and
                        resource.path not in self._known_remote_cses):
                    remote_cse = self.get_resource(resource.id)
                    self._known_remote_cses[resource.path] = remote_cse
                    remote_cse_base = (remote_cse.CSE_ID + '/' +
                                       remote_cse.CSEBase)
                    self._discover_cse(remote_cse_base, resource.path)

        handle_cse_base(cse_base)
        self.run_forever(self.interval, get_cse_base)

    # discover CSE

    def _discover_cse(self, cse_base, remote_cse_id=None):

        def err_cb(errror_response):
            try:
                del self._known_remote_cses[remote_cse_id]
            except KeyError:
                pass

        # discover devices
        self.periodic_discover(cse_base, {'labels': ['openmtc:device']},
                               self.interval,
                               self._discover_devices, err_cb)

        self.periodic_discover(cse_base, {'labels': ['openmtc:sensor_data']},
                               self.interval,
                               self._discover_sensors, err_cb)

        self.periodic_discover(cse_base, {'labels': ['openmtc:actuator_data']},
                               self.interval,
                               self._discover_actuators, err_cb)

    def _discover_devices(self, discovery):
        for device_path in discovery:
            self._discovered_devices[device_path] = 0

    def _handle_sensor_data(self, cnt, con):
        sensor = self._discovered_sensors[cnt]
        con = con[0]
        if not sensor['data']:
            sensor['u'] = con.get('u')
            sensor['n'] = con['n']
            self.emit('newSensor', self._map_sensor_data(sensor))
        else:
            self.emit('sensorData', {'ID': cnt, 'data': con})
        sensor['data'].append(con)

    def _handle_new_sensor(self, sensor_path):
        sensor_cnt = self.get_resource(sensor_path)
        sensor = self._discovered_sensors[sensor_path]
        max_len = max(self.max_values, sensor_cnt.maxNrOfInstances)
        sensor['data'] = deque(maxlen=max_len)
        sensor['max_data'] = max_len

        def filter_cin(res):
            return res.resourceType == ResourceTypeE.contentInstance

        def get_cin(res):
            return self.get_resource(res.resourceID)

        # get existing data
        cin_list = map(get_cin, filter(filter_cin, sensor_cnt.childResource))

        # filter out not existing
        cin_list = filter(None, cin_list)

        # sort by creation Time
        cin_list.sort(key=lambda x: x.creationTime)

        # data existing
        if cin_list:
            for cin in cin_list:
                con = json.loads(b64decode(cin.content))[0]
                sensor['data'].append(con)
            con = json.loads(b64decode(cin_list[0].content))[0]
            sensor['u'] = con.get('u')
            sensor['n'] = con['n']
            self.emit('newSensor', self._map_sensor_data(sensor))
        self.add_container_subscription(sensor_path, self._handle_sensor_data)

    def _discover_sensors(self, discovery):
        for sensor_path in discovery:
            try:
                dev_path = [x for x in self._discovered_devices.keys()
                            if sensor_path.startswith(x)][0]
            except IndexError:  # todo(rst): ignore, but should not happen
                continue
            self._discovered_sensors[sensor_path] = {
                'ID': sensor_path,
                'dev_name': dev_path.split('/')[-1],
                'cse_id': sensor_path.split('/')[1],
                'data': None,
                'max_data': 0,
                'type': 'sensor',
                'n': None,
                'u': None
            }
            self._handle_new_sensor(sensor_path)

    def _discover_actuators(self, discovery):
        for actuator_path in discovery:
            try:
                dev_path = [x for x in self._discovered_devices.keys()
                            if actuator_path.startswith(x)][0]
            except IndexError:  # todo(rst): ignore, but should not happen
                continue
            self._discovered_actuators[actuator_path] = {
                'ID': actuator_path,
                'dev_name': dev_path.split('/')[-1],
                'cse_id': actuator_path.split('/')[1],
                'type': 'actuator',
                'n': actuator_path.split('/')[-1]
            }
            self.emit('newActuator', self._discovered_actuators[actuator_path])

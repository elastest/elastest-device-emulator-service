from openmtc_app.onem2m import XAE
from openmtc_onem2m.exc import CSENotFound
import json
import requests
import base64


class FrontEnd(XAE):
    remove_registration = True
    remote_cse = 'onem2m/OPCUAIPE/'

    remote_cse_mems = 'onem2m/MemsIPE/'
    interval = 10

    def _on_register(self):
        # init variables
        self.history = []  # list of history data sets

        # incoming sockets
        self.runner.add_message_handler("get_history", self.send_history)
        self.runner.add_message_handler("motor_start", self.send_motor_start)
        self.runner.add_message_handler("motor_stop", self.send_motor_stop)

        # start endless loop
        self.periodic_discover(self.remote_cse, {'labels': ['openmtc:sensor_data']},self.interval, self.handle_sensors)
        self.periodic_discover(self.remote_cse_mems, {'labels': ['openmtc:sensor_data']},self.interval, self.handle_sensors_mems)

    def send_history(self):
        print "send history ..........."
        self.emit('history', self.history)

    def send_data(self, data):
        self.emit(data['n'], data)

        # limit history to 100 entries
        if len(self.history) >= 100:
            del self.history[0]
        # append data to history
        self.history.append(data)

    def sensor_handler(self, uri, data):
        r = json.dumps(data[0])
        l_r = json.loads(r)
        self.send_data(l_r)




    def handle_sensor(self, uri):
        print "handle sensor triggered"
        try:
            data = self.get_content(uri)
            print data
            r = json.dumps(data[0])
            l_r = json.loads(r)
            self.send_data(l_r)
        except CSENotFound:
            pass
        self.logger.debug('Subscribing to Resource: ' + uri)
        self.add_container_subscription(
            uri, self.sensor_handler)

    def handle_sensors(self, discovery):
        # for each device container discovered
        for uri in discovery:

            print "show uri below:"+ uri
            # subscribe to device container with handler
            if uri.endswith('/actual_speed'):
                self.handle_sensor(uri)
            if uri.endswith('/MachineStatusLED'):
                self.handle_sensor(uri)

    def handle_sensors_mems(self, discovery):
        # for each device container discovered
        for uri in discovery:

            print "show uri below:"+ uri
            # subscribe to device container with handler
            if uri.endswith('/x'):
                self.handle_sensor(uri)
            if uri.endswith('/y'):
                self.handle_sensor(uri)

            if uri.endswith('/z'):
                self.handle_sensor(uri)

    def send_motor_start(self):

        static_json = '{"m2m:cin": {"con": "W3sidiI6dHJ1ZX1d", "cnf": "application/json:1"}}'
        h = {'Content-Type': 'application/vnd.onem2m-res+json'}
        r = requests.post("http://10.147.175.171:8000/onem2m/OPCUAIPE/plc_2/actuator_data/CW1_Bit00_OFF1", data =static_json, headers=h)
        print r.status_code

    def send_motor_stop(self):

        static_json = '{"m2m:cin": {"con": "W3sidiI6ZmFsc2V9XQ==", "cnf": "application/json:1"}}'
        h = {'Content-Type': 'application/vnd.onem2m-res+json'}
        r = requests.post("http://10.147.175.171:8000/onem2m/OPCUAIPE/plc_2/actuator_data/CW1_Bit00_OFF1", data =static_json, headers=h)
        print r.status_code

        # def measurements_handler(self, uri, data):
        #     self.logger.debug('measurements_handler...')
        #
        #     # limit history to 100 entries
        #     if len(self.history) >= 100:
        #         del self.history[0]
        #     # append data to history
        #     self.history.append(data)
        #
        #     # send new data set to webserver
        #     self.emit(data['sensor'], data)

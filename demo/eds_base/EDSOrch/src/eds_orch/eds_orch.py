from openmtc_app.onem2m import XAE
from openmtc_onem2m.model import Container
import time
import docker
import json

class EDSOrch(XAE):

    def __init__(self, *args, **kw):
        super(EDSOrch, self).__init__(*args, **kw)
        self.logger.debug('initializing')

        # contains all the registered apps in the format of
        # {'app_ID': {'sensors':[list of sensor names],
        # 'actuators': {list of actuator names}}
        self.registered_apps = {}
        self.base_path = 'onem2m/EDSOrch/'
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
        # {'request_ID': 'uuid', 'result': 'SUCCESS', 'response': dict(response),
        # 'error': 'error_string'}

        # response format for application
        # {'path' : 'application path'}
        # response format for sensor
        # {'name'}

        # this list is used to add all the available sensors that EDS can provide
        # when an application registers. This list needs to be updated when a new
        # sensor is added to manifest
        self.available_sensors = ['temperature']
        # this list is used to add all the available actuators that EDS can provide
        # when an application registers. This list needs to be update when a new
        # actuator is added
        self.available_actuators = ['simple']

    def _on_register(self):
        # create the channels for orch by creating respective containers

        # first create orch container
        self.orch_cnt = Container(resourceName='edsorch',
                labels=['elastest:edsorch'],
                maxNrOfInstances=5)
        self.orch_cnt = self.create_container(None, self.orch_cnt)

        #create request container
        self.request_cnt = mContainer(resourceName='request',
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
        self.add_container_subscription(self.response_cnt,
                self.handle_response)

        # create status container
        self.status_cnt = Container(resourceName='status',
                labels=['elastest:edsorch:status'],
                maxNrOfInstances=5)
        self.status_cnt = self.create_container(self.orch_cnt,
                self.status_cnt)
        self.add_container_subscription(self.status_cnt,
                self.handle_status)

        # call each available sensor's corresponding script
        # also subscribe to their response channels

        # start endless loop
        self.logger.info('all registration finished')
        time.sleep(1)
        self.push_content('onem2m/EDSOrch/edsorch/request', [{"register":{'application':{'app_ID':0, 'request_ID': 0}}}])
        self.run_forever()

    def _on_shutdown(self):
        pass

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
                        if key_1 == 'application':
                            request_response, response_1, error_string = \
                            self.handle_register_application(request)
                        elif key_1 == 'sensor':
                            request_response, response_1, error_string = \
                                    self.handle_register_sensor(request)
                        elif key_1 == 'actuator':
                            request_response, response_1, error_string = \
                                    self.handle_register_actuator(request)
                        else:
                            request_response = 'FAIL'
                            response_1 = {}
                            response_string = error_string + 'component to \
                                    register not recognized\n'

                elif key == 'deregister':
                    request_1 = request[key]
                    for key_1 in request_1:
                        if key_1 == 'application':
                            request_response, response_1, error_string = \
                                    self.handle_deregister_application(request)
                        else:
                            request_response = 'FAIL'
                            response_1 = {}
                            response_string = error_string + 'component to \
                                    deregister not recognized\n'
                        reponse[key][key_1] = {'result': request_response,
                                'response': response_1, 'error': error_string}

            print response
            self.status = 'IDLE'
            status_data[0]['s'] = str(self.status)
            timestamp = format(round(time.time(), 3), '.3f')
            status_data[0]['t'] = timestamp
        self.push_content(_status_cnt, status_data)

    def handle_register_application(self, request):
        # request format
        # {'register' : {'application' : {'app_ID':'uuid', 'request_ID': 'uuid'}}}
        label = 'elastest:application'
        # create a container with the name of app_ID
        app_cnt = Container(resourceName=request['register']['application']['app_ID'],
                labels=[label],
                maxNrOfInstances=1)
        app_cnt = self.create_container(None, app_cnt)
        label = label + ':sensors'
        # create a sensors container
        sensors_cnt = Container(resourceName='sensors',
                labels=[label],
                maxNrOfInstances=1)
 # {'request_ID': 'uuid', 'result': 'SUCCESS', 'response': dict(response),
        # 'error': 'error_string'}
        sensors_cnt = self.create_container(app_cnt, sensors_cnt)
        # attach containers for all available sensors
        # Sensors of a specific type attach to the sensor containers
        for sensor in self.available_sensors:
            label_1 = label + ':' + sensor
            sensor_cnt = Container(resourceName=sensor,
                    labels=[label_1],
                    maxNrOfInstances=1)

        # create an actuators container
        label = 'elastest:application:actuators'
        actuators_cnt = Container(resourceName='actuators',
                labels=[label],
                maxNrOfInstance=1)
        # attach containers for future possible types of actuators
        for actuator in self.available_actuators:
            label_1 = label + ':' + actuator
            actuator_cnt = Container(resourceName=actuator,
                    labels=[label_1],
                    maxNrOfInstances=1)
        # reply format
        # {'request_ID': 'uuid', 'result': 'SUCCESS', 'response': dict(response),
        # 'error': 'error_string'}
        request_ID = request['register']['application']['request_ID']
        result = 'SUCCESS'
        error_string = ''
        response = {'path' : app_cnt.path}
        reply = {'request_ID' : request_ID, 'result' : result, 'response' : response,
                'error_string' : error_string}
        self.registered_apps[app_ID] = {'path': app_container.path}
        self.push_content(self.response_cnt, reply)

    def handle_register_sersor(self, request):
        return "SUCCESS", {}, ""

    def handle_register_actuator(self, request):
        return "SUCCESS", {}, ""

    def handle_deregister_application(request):
        return "SUCCESS", {}, ""

    def _on_shutdown(self):
        pass


    def check_request_content(self, con):
        request = con
        error_string = ''
        valid_request = True
        if not isinstance(request, dict):
            return False, "Request is not a dictionary"
        # check if the request is an empty dictionary
        if not request:
            return False, "Request dictionary is empty"

        self.logger.debug('check_request: Non-empty request dictionary received')

        # check if the first element is register or deregister, else continue
        # this loop can iterate twice if register and deregister are present
        for key in request:
            # if available key is not register or deregister flag an error
            # update error string and valid_request
            if key not in ['register', 'deregister']:
                valid_request = False
                error_string = error_string + key + 'is not a valid request key \n'
                continue
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
            # the dictionary element can have three maximum, therefore need to
            # iterate over each one of them
            for key_1 in request_1:
                request_2 = request_1[key_1]

                # check if key_1 is a valid key
                if key == 'register' and key_1 not in ['application', 'sensor', 'actuator']:
                    valid_request = False
                    error_string = error_string + key_1 + ' not a valid component\n'
                    continue
                elif key == 'deregister' and key_1 not in ['application']:
                    valid_request = False
                    error_string = error_string + key_1 + ' not a valid component\n'
                    continue
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

                if len(diff) > 0 :
                    self.logger.debug('check_request: Not all required fields present in the component request')
                    valid_request = False
                    for field in diff:
                        error_string = error_string + key + ':' + key_1 + ':' + \
                        field + ' not found in request\n'


        return valid_request, error_string


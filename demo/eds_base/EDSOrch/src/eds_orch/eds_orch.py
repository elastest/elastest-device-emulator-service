from openmtc_app.onem2m import XAE
from openmtc_onem2m.model import Container
import time

class EDSOrch(XAE):

    def __init__(self, *args, **kw):
        super(EDSOrch, self).__init__(*args, **kw)
        self.logger.debug('initializing')
        self.registered_apps = {}
        self.base_path = 'onem2m/EDSOrch/edsorch/'
        self.status = 'idle'
        self.request_template = {'register':{}, 'deregister':{}}
        self.request_template['register']['application'] = ['app_ID', 'request_ID']
        self.request_template['register']['sensor'] = ['app_ID', 'request_ID',
                'sensor_type']
        self.request_template['register']['actuator'] = ['app_ID', 'request_ID',
                'actuator_type']
        self.request_template['deregister']['application'] = {'app_ID', 'request_ID'}

        # request format
        # { 'register' : {'application':{'app_ID':'uuid'}}}

    def _on_register(self):
        # create the channels for orch by creating respective containers

        # first create orch container
        self.orch_cnt = Container(resourceName='edsorch',
                labels=['elastest:edsorch'],
                maxNrOfInstances=1)
        self.orch_cnt = self.create_container(None, self.orch_cnt)

        #create request container
        self.request_cnt = Container(resourceName='request',
                labels=['elastest:edsorch:request'],
                maxNrOfInstances=1)
        self.request_cnt = self.create_container(self.orch_cnt,
                self.request_cnt)
        self.add_container_container_subscription(self.request_cnt,
                self._handle_request)

        # create response container
        self.response_cnt = Container(resourceName='response',
                labels=['elastest:edsorch:response'],
                maxNrOfInstances=1)
        self.response_cnt = self.create_container(self.orch_cnt,
                self.response_cnt)

        # create status container
        self.status_cnt = Container(resourceName='status',
                labels=['elastest:edsorch:status'],
                maxNrOfInstances=1)
        self.status_cnt = self.create_container(self.orch_cnt,
                self.status_cnt)

        # start endless loop
        self.run_forever()

    def _handle_request(self, cnt, con):
        _response_cnt = self.response_cnt
        _status_cnt = self.status_cnt
        timestamp = format(round(time.time(), 3), '.3f')
        status_data = [{'n': 'orchestrator',
            't': timestamp,
            's': str(self.status)}]

        if self.status == 'idle':
            self.status = 'busy'
            status_data[0]['s'] = self.status
            self.push_content(_status_cnt, self.status)

            # analyze the incoming request
            # analyze if all the info is available already in the request,
            # based on the incoming request
            # compare with the request and the expected information
            # look at this from a data base of strings having the expected
            # fields

            # Analyze the provided strings for each request from application
            valid_request = None

            # This where the request is checked for errors
            valid_request = self.check_request_content(con)


            self.handle_request_content(con)

            self.status = 'idle'
            status_data[0]['s'] = str(self.status)
            timestamp = format(round(time.time(), 3), '.3f')
            status_data[0]['t'] = timestamp




    def _on_shutdown(self):
        pass


    def check_request_content(con):

        request = con
        error_string = ''
        valid_request = True
        # check if the content is a dict
        if not isinstance(con, dict):
            return False, "Request not a dictionary"

        # check if the first element is register or deregister
        for key in request:
            # if available key is not register or deregister flag an error and
            # return
            if key not in ['register', 'deregister']:
                valid_request = False
                error_string = error_string + key + 'is not a valid request key \n'
                continue

            if not isinstance(request[key], dict):
                valid_request = False
                error_string = error_string + request[key] + 'in ' + key
            if request[key] not in ['application', 'sensor', 'actuator']:
                valid_request = False
                error_str
            diff = set(request[key].keys()) - set(request[key].keys())

            if len(diff) > 0 :
                valid_request = False
                for field in diff:
                    error_string = error_string + field + ' not found in request\n'




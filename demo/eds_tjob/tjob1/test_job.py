from openmtc_app.onem2m import XAE
from openmtc_onem2m.model import AE, Container, ContentInstance
from openmtc_onem2m.client.http import OneM2MHTTPClient
from openmtc_onem2m.transport import OneM2MRequest
import time
import os
class TestJob(XAE):
    
    def __init__(self, *args, **kw):
        super(TestJob, self).__init__(*args, **kw)
        
        self.actuator_trigger = False
        self.sensor_data = 0
        self.sensor_trigger_time = 0
        self.verdict = True
        self.threshold = 30
        self.trigger_duration = 3

    def _on_register(self):
        # start endless loop
        eds_base = os.environ["ET_EDS_EDS_BASE_API"]
        eds_base = eds_base[:-8]

        client = OneM2MHTTPClient(eds_base, False)
        base_path = "onem2m/EDSOrch/testapplication/"
        sensors_path = base_path + "sensors/"
        onem2m_request = OneM2MRequest("retrieve", to=sensors_path)

        promise = client.send_onem2m_request(onem2m_request)
        onem2m_response = promise.get()

        children = onem2m_response.content.childResource
        sensor_path = children[0].path
        sensor_data = sensors_path + sensor_path + "/data"
        
        actuators_path = base_path + "actuators/"
        onem2m_request = OneM2MRequest("retrieve", to=actuators_path)

        promise = client.send_onem2m_request(onem2m_request)
        onem2m_response = promise.get()

        children = onem2m_response.content.childResource
        actuator_path = children[0].path
        actuator_data_out = actuators_path + actuator_path + "/data_out"
        

        self.add_container_subscription(sensor_data, self.handle_sensor_data)
        self.add_container_subscription(actuator_data_out, self.handle_actuator_out)


        self.run_forever()

    def handle_sensor_data(self, cnt, con):
        self.sensor_data = con
        self.sensor_trigger_time = time.time()

        if self.actuator_trigger:
            self.logger.info("FAIL: Actuator was not triggered")
            self.actuator_trigger = False
            self.verdict = False
        else:
            self.logger.info("PASS: Actuator was properly triggered")
        if self.sensor_data > self.threshold:
            self.actuator_trigger = True

    def handle_actuator_out(self, cnt, con):
        actuator_data = con
        if actuator_data == self.sensor_data:
            self.logger.info("PASS: Actuator data == Sensor data")
        else:
            self.logger.info("FAIL: Actuator data != Sensor data")
            self.verdict = False

        actuator_trigger_time = time.time()
        trigger_time = actuator_trigger_time - self.sensor_trigger_time
        if trigger_time < 0:
            self.logger.info("FAIL: Actuator trigger too late or obsolete")
            self.verdict = Faslse
        elif (trigger_time > (self.trigger_duration - 0.05)) and (trigger_time < (self.trigger_duration + 0.05)):
            self.logger.info("PASS: Actuator triggered in the correct time window")
        else:
            self.logger.info("FAIL: Actuator behaviour unknown")
            self.verdict = False
        self.actuator_trigger = False


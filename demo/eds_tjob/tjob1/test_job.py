from openmtc_app.onem2m import XAE
from openmtc_onem2m.model import AE, Container, ContentInstance
from openmtc_onem2m.client.http import OneM2MHTTPClient
from openmtc_onem2m.transport import OneM2MRequest
import time
import os
import unittest
import xmlrunner
import gevent
import signal

class AssertVariables():
    actuator_trigger = False
    actuator_data = 0
    sensor_data = 0
    sensor_trigger_time = 0
    threshold = 30.00
    trigger_duration = 3

variables = AssertVariables()

class TestSensorBehaviour(unittest.TestCase):

    def test_sensor_trigger_time(self):
        sensor_trigger_time = time.time()
        trigger_time = sensor_trigger_time - variables.sensor_trigger_time
        time_behaviour = trigger_time <= 6
        self.assertTrue(time_behaviour, "Sensor trigger beyond expected interval")

    def test_sensor_data(self):
        data_behaviour = type(variables.sensor_data) == float
        self.assertTrue(data_behaviour, "Sensor data is not float")
class TestActuatorTrigger(unittest.TestCase):

    def test_actuator_trigger(self):
        if variables.actuator_trigger:
            variables.actuator_trigger = False
        self.assertFalse(variables.actuator_trigger, "Actuator was not \
                         triggered")
class TestActuatorDataBehaviour(unittest.TestCase):

    def test_actuator_data(self):
        self.assertEqual(variables.sensor_data, variables.actuator_data,
                        "Received actuator data not equal to sensor data")

class TestActuatorTimeBehaviour(unittest.TestCase):

    def test_actuator_trigger_expected(self):
        self.assertTrue(variables.actuator_trigger, "Actuator trigger not expected")
        variables.actuator_trigger = False

    def test_actuator_not_late(self):
        actuator_trigger_time = time.time()
        trigger_time = actuator_trigger_time - variables.sensor_trigger_time
        self.assertGreater(trigger_time, 0, "Actuator trigger too late or \
                        obsolete")

    def test_actuator_behaviour_correct(self):
        actuator_trigger_time = time.time()
        trigger_time = actuator_trigger_time - variables.sensor_trigger_time        
        behaviour = variables.actuator_trigger and (trigger_time > 
                    (variables.trigger_duration - 1)) and (trigger_time < 
                    (variables.trigger_duration + 1))
        self.assertTrue(behaviour, "actuator behaviour unknown")
        
sensorBehavourSuite = unittest.TestLoader().loadTestsFromTestCase(TestSensorBehaviour)
actuatorTriggerSuite = unittest.TestLoader().loadTestsFromTestCase(TestActuatorTrigger)
actuatorDataBehaviourSuite = unittest.TestLoader().loadTestsFromTestCase(TestActuatorDataBehaviour)
actuatorTimeBehaviourSuite = unittest.TestLoader().loadTestsFromTestCase(TestActuatorTimeBehaviour)

class TestJob(XAE):
    
    def __init__(self, *args, **kw):
        super(TestJob, self).__init__(*args, **kw)
        
        self.verdict = True

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

        gevent.sleep(0)
        gevent.spawn_later(60, self.app_shutdown)

    def app_shutdown(self):
        os.kill(os.getpid(),signal.SIGTERM)

    def handle_sensor_data(self, cnt, con):
        variables.sensor_data = float(con)
        # unittest.TextTestRunner(verbosity=2).run(sensorBehavourSuite)
        xmlrunner.XMLTestRunner(verbosity=2, output='/tmp/test-reports').run(sensorBehavourSuite)
        variables.sensor_trigger_time = time.time()
        # unittest.TextTestRunner(verbosity=2).run(actuatorTriggerSuite)
        xmlrunner.XMLTestRunner(verbosity=2, output='/tmp/test-reports').run(actuatorTriggerSuite)
        if variables.sensor_data >= variables.threshold:
            variables.actuator_trigger = True
        else:
            variables.actuator_trigger = False

    def handle_actuator_out(self, cnt, con):
        variables.actuator_data = float(con)
        #unittest.TextTestRunner(verbosity=2).run(actuatorDataBehaviourSuite)
        #unittest.TextTestRunner(verbosity=2).run(actuatorTimeBehaviourSuite)
        xmlrunner.XMLTestRunner(verbosity=2, output='/tmp/test-reports').run(actuatorDataBehaviourSuite)
        xmlrunner.XMLTestRunner(verbosity=2, output='/tmp/test-reports').run(actuatorTimeBehaviourSuite)

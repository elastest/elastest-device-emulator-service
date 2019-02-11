##################################################
# This program subscribes to the sensor data container
# when it receives the data, it applies a logic > 30
# If greater then it is going to push data to the actuator data_in container
# it subscribes to the data_out container to check if it works properly
##################################################

from openmtc_app.onem2m import XAE
# import application entity and container class from openmtc model
# helps to create application entity and container
from openmtc_onem2m.model import AE, Container
# gevent need for event processing
import gevent

class LogicExample(XAE):

    def _on_register(self):
        # subscribe to the sensor data container
        # we already know the path where the sensor data container is
        self.actuator_data_in = "onem2m/ActuatorExample/actuator/data_in"
        self.actuator_data_out = "onem2m/ActuatorExample/actuator/data_out"
        self.sensor_data = "onem2m/SensorExample/sensor/data"
        self.add_container_subscription(self.sensor_data, self.handle_sensor_data)

        # subscribe to the data_out container of the actuator
        self.add_container_subscription(self.actuator_data_out, self.handle_actuator_data_out)
        # start endless loop
        self.run_forever()

    def handle_sensor_data(self, cnt, con):
        print "received sensor data", con
        # convert the con to floating point value
        data = float(con)
        # apply the logic
        if data > 30:
            print "sensor data greater than 30"
            print "push data to actuator data in container"
            self.push_content(self.actuator_data_in, con)

    def handle_actuator_data_out(self, cnt, con):
        print "actuator pushed data_out", con

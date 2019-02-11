##################################################
# This program creates necessary containers first
# Then pushes data to the necessary container periodically like a sensor
# It also attaches to the relevant container to show that data is pushed
##################################################

from openmtc_app.onem2m import XAE
# import application entity and container class from openmtc model
# helps to create application entity and container
from openmtc_onem2m.model import AE, Container
# this module is needed for generating random numbers in uniform distribution
import numpy
# gevent need for event processing
import gevent

class SensorExample(XAE):

    def _on_register(self):
        # create a sensor container with 5 instances history
        self.sensor_cnt = Container(resourceName='sensor', maxNrOfInstances=5)
        # attach the sensor container to the SensorExample base path
        # this container is now accessible under path "onem2m/SensorExample/sensor"
        self.sensor = self.create_container(None, self.sensor_cnt)
        # now create another container called data container which will hold the data
        # values sent by the container with max history of 5 instances
        self.data_cnt = Container(resourceName='data', maxNrOfInstances=5)
        # attach this container next to sensor
        # data container is accessible by
        # onem2m/SensorExample/sensor/data
        self.data = self.create_container(self.sensor, self.data_cnt)

        # register a handler to check if you actually send data
        self.add_container_subscription(self.data, self.handle_sensor_data)
        # call a periodic function which pumps sensor data into the data container
        self.generate_send_data()
        # it never goes after this because generate_send_data is having control always

    def app_shutdown(self):
        os.kill(os.getpid(), signal.SIGTERM)

    # this function generates and pushes data periodically to data container
    # every 5 seconds
    # data generation uses a uniform distribution from 0 to 100
    def generate_send_data(self):
        _data_cnt = self.data
        data = 0
        while(True):
            data = numpy.random.uniform(low=0, high=100, size=None)
            print "generating data", data
            # convert the data to string because thats how data should be pushed
            # container
            to_send = str(data)
            print "sending data"
            self.push_content(_data_cnt, to_send)
            # sleep for 5 seconds
            print "sleeping for 5 seconds"
            gevent.sleep(5)

    def handle_sensor_data(self, cnt, con):
        print "sensor received data", con

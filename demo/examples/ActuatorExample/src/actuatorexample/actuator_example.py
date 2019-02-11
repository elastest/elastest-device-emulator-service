##################################################
# This program creates an data_in and data_out container for the acutator
# If action is needed from the actuator, we push data to the data_in container
# The actuator subscribes to the data_in container
# when data is pushed to the data_in actuator, a handler is called and after that
# actuator waits for 3 seconds before pushing the data to the data_out actuator
# actuator also subscribes to data_out to verify if the sending is working as intended
##################################################

from openmtc_app.onem2m import XAE
# import application entity and container class from openmtc model
# helps to create application entity and container
from openmtc_onem2m.model import AE, Container
# gevent need for event processing
import gevent

class ActualtorExample(XAE):
    
    def _on_register(self):
        # create the actuator container as a base
        self.actuator_cnt = Container(resourceName='actuator', maxNrOfInstances=5)
        # attach the actuator container to the ActuatorExample base path
        self.actuator = self.create_container(None, self.actuator_cnt)
        # now create a data_in container for actuator input
        self.data_in_cnt = Container(resourceName='data_in', maxNrOfInstances=5)
        # attach the data_in container below the actuator
        # data_in path is onem2m/ActuatorExample/actuator/data_in
        self.data_in = self.create_container(self.actuator, self.data_in_cnt)
        # create a data_out container for the actuator output
        self.data_out_cnt = Container(resourceName='data_out', maxNrOfInstances=5)
        # attach the data_out container below the actuaor
        # data_out path is onem2m/ActuatorExample/actuator/data_out
        self.data_out = self.create_container(self.actuator, self.data_out_cnt)

        # subscribe to the data_in container because that's how actuator will be notified
        self.add_container_subscription(self.data_in, self.handle_actuator_data_in)

        # subscribe to the data_out container because we can check if the actuator did infact behave
        # as we like it to. As soon as we push something, we will be notified.
        self.add_container_subscription(self.data_out, self.handle_actuator_data_out)
        # start endless loop
        # we want actuator to run forever
        self.run_forever()

    def handle_actuator_data_in(self, cnt, con):
        data = con
        print "actuator received data on data_in ", data
        # the action of actuator is to wait for 3 seconds after it receives an input
        gevent.sleep(3)
        print "actuator sending data via data_out ", data
        self.push_content(self.data_out, data)

    def handle_actuator_data_out(self, cnt, con):
        data = con
        print "actuator received data on data_out ", data

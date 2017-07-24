from openmtc_app.onem2m import XAE
from openmtc_onem2m.exc import CSENotFound
from openmtc_onem2m.model import Container
from zigbeeipe.zig_bee_ipe import ZigBeeIPE
#from zigbeeipe.zig_bee_coordinator import ZigBeeCoordinator


class TestZigBeeIPE():
    def setUp(self):
        self.zigbee = ZigBeeIPE()
    def test__on_shutdown(self):
        self.zigbee.usb_device = "/dev/ttyUSB0"
        self.zigbee.coordinator = ZigBeeCoordinator(self.zigbee.usb_device)
        shut = self.zigbee .coordinator.shutdown
        assert shut
        # pass
    def test__on_register(self):
        #self.fail()#
        container1 = Container(resourceName1 = 'zigbee device1',maxNrOfInstances = 1)
        #container2 = Container(resourceName1 = 'zigbee devices2',maxNrOfInstances = 1)
        #container3 = Container(resourceName1 = 'zigbee devices3',maxNrOfInstances = 1)
        self.zigbee.devices_container1 = self.zigbee.create_container(None,container1)
     #   self.zigbee.devices_container2 = self.zigbee.create_container(None,container2)
      #  self.zigbee.devices_container3 = self.zigbee.create_container(None,container3)
        self.zigbee._on_register()
        self.assertEqual(0, self.zigbee.devices_container1)
        #verify it is ok to have 0 instances
        self.zigbee._on_register()
        self.assertEqual(0, self.zigbee.devices_container1)

        #pass
    def test__create_device_container(self):
        #self.fail()
        pass
    def test__register_device(self):
       # self.fail()
        pass
    def test__handle_zbs110_switch(self):
        #self.fail()
        pass
    def test__get_unified_data(self):
        #self.fail()
        pass
    def test__push_content(self):
        #self.fail()
        pass
    def test__handle_sensor_data(self):
        #self.fail()
        pass
    def test__handle_device_data(self):
        #self.fail()
        pass
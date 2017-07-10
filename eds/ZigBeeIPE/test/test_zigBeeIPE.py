

from zigbeeipe.zig_bee_ipe import *
from zigbeeipe.zig_bee_coordinator import *


class TestZigBeeIPE():
    def test__on_shutdown(self):
        self.usb_device = "/dev/ttyUSB0"
        self.coordinator = ZigBeeCoordinator(self.usb_device)
        shut= self.coordinator.shutdown
        assert shut

    def test__on_register(self):
        #self.fail()
        pass

    def test__create_device_container(self):
    #   self.fail()
        pass


    def test__register_device(self):
    #   self.fail()
         pass


    def test__handle_zbs110_switch(self):
    #   self.fail()
        pass


    def test__get_unified_data(self):
    #   self.fail()
        pass


    def test__push_content(self):
    #   self.fail()
         pass


    def test__handle_sensor_data(self):
    #   self.fail()
         pass


    def test__handle_device_data(self):
    #   self.fail()
         pass

# from unittest import TestCase
import time
from random import choice, randint

import serial
from gevent import sleep, spawn
from xbee import ZigBee

from futile.logging import LoggerMixin
from zigbeeipe.devices import Device, ZBS110, ZBS121, ZBS122
from zigbeeipe.zig_bee_coordinator import ZigBeeCoordinator

class TestZigBeeCoordinator():
	def test_get_simulated_device(self):
		pass

	def test_start(self):
		pass

	def test_start_simulation(self):
		pass

	def test__generate_simulated_data(self):
		pass

	def test_shutdown(self):
		pass

	def test_add_handler(self):
		pass

	def test__get_sensor_handler(self):
		pass

	def test__get_device_handler(self):
		pass

	def test__add_device_from_nd(self):
		pass

	def test__add_device_from_rx(self):
		pass

	def test__get_device_pid(self):
		pass

	def test__get_device_node_id(self):
		pass

	def test__set_device_pid(self):
		pass

	def test__update_device_data(self):
		pass

	def test__set_device_data(self):
		pass

	def test__set_tx_interval(self):
		pass

	def test__send_command_dev(self):
		pass

	def test__send_node_discover(self):
		pass

	def test_send_command_switch(self):
		pass

	def test__handle_frame(self):
		pass

	def test__handle_node_discover_frame(self):
		pass

	def test__handle_rx_frame(self):
		pass

	def test__handle_ack(self):
		pass

	def test__handle_device_data(self):
		pass

	def test__handle_sensor_data(self):
		pass

	def test__parse_device_data(self):
		pass

	def test__register_device(self):
		pass

	def test__hex(self):
		pass

	def test__time(self):
		pass



import time
from random import choice, randint

import serial
from gevent import sleep, spawn
from xbee import ZigBee

from futile.logging import LoggerMixin
from .devices import Device, ZBS110, ZBS121, ZBS122

BAUD_RATE = 9600
NODE_DISCOVER_INTERVAL = 6
SLEEP_INTERVAL = 0.1

NUMBER_OF_SIMULATED_DEVICES = 5


class ZigBeeCoordinator(LoggerMixin):

    simulated_device_counter = 0

    def get_simulated_device(self):
        dev = {
            'ID': 'ZBS122S%06d' % self.simulated_device_counter,
            'PID': 'ZBS-122',
            'hw_info': {
                'foo': 'bar'
            }
        }

        self.simulated_device_counter += 1

        return dev

    def __init__(self, usb_device="/dev/ttyUSB0", *args, **kw):
        super(ZigBeeCoordinator, self).__init__()
        self.usb_device = usb_device
        self.devices = {}
        self.handlers = {}
        self.parsers = {
            "ZBS-122": ZBS122(),
            "ZBS-121": ZBS121(),
            "ZBS-110": ZBS110()
        }
        self.serial_device = None
        self.zigbee_coord = None
        self.simulated_devices = []
        self.running = False

    def start(self):
        self.serial_device = serial.Serial(self.usb_device, BAUD_RATE)

        # async mode
        self.zigbee_coord = ZigBee(self.serial_device,
                                   callback=self._handle_frame)

        self.running = True
        self.logger.info("Coordinator started.")

        spawn(self._send_node_discover)

    def start_simulation(self, run_forever, period):
        for i in range(NUMBER_OF_SIMULATED_DEVICES):
            self.simulated_devices.append(self.get_simulated_device())
        run_forever(period, self._generate_simulated_data)

    def _generate_simulated_data(self):
        device = choice(self.simulated_devices)
        nid = device['ID']
        handler = self.handlers.get(nid + '_sensor')
        parser = self.parsers[device['PID']]
        device_data = parser.device_data
        sensor_data = parser.sensor_data
        if handler:
            data = parser.get_simulated_data(device_data + sensor_data)
            for d in data:
                d['timestamp'] = self._time()

            modified_data = {
                'sensor_data': filter(lambda x: x['type'] in sensor_data, data),
                'device_data': filter(lambda x: x['type'] in device_data, data)
            }

            handler(modified_data, nid)
        else:
            # register
            register_handler = self.handlers.get('REGISTER_DEVICE')
            register_handler(nid, [])

    def shutdown(self):
        self.logger.info("Shutting down.")
        self.running = False
        try:
            if self.zigbee_coord is not None:
                self.zigbee_coord.halt()
            if self.serial_device is not None:
                self.serial_device.close()
        except (KeyboardInterrupt, RuntimeError):
            pass

    def add_handler(self, nid, handler):
        self.handlers[nid] = handler

    def _get_sensor_handler(self, nid):
        return self.handlers[nid + '_sensor']

    def _get_device_handler(self, nid):
        return self.handlers[nid + '_device']

    def _add_device_from_nd(self, frame):
        dev_info = {}
        important_param = ['source_addr', 'source_addr_long', 'node_identifier']

        try:
            parameter = frame['parameter']

            for k, v in parameter.iteritems():
                if k in important_param:
                    dev_info[k] = v
        except KeyError as e:
            self.logger.exception("Missing parameters to add device: %s",
                                  e.args)

        try:
            device = Device(node_id=dev_info['node_identifier'],
                            addr=dev_info['source_addr'],
                            addr_long=dev_info['source_addr_long'])
            self.devices[device.addr_long] = device
            self.logger.debug("New device '%s' added to devices.",
                              self._hex(device.addr_long))
            self._send_command_dev(device.addr, device.addr_long)
        except KeyError as e:
            self.logger.error("Error creating device: %s", e.args)

    def _add_device_from_rx(self, frame):
        try:
            rf_data = dict(string.split('=')
                           for string in frame['rf_data'].split())
        except KeyError as e:
            self.logger.exception("Missing parameters to add device: %s",
                                  e.args)
            raise e

        try:
            device = Device(node_id=rf_data['ID'],
                            addr=frame['source_addr'],
                            addr_long=frame['source_addr_long'])
            self.devices[device.addr_long] = device
            self.logger.debug("New device '%s' added to devices.",
                              self._hex(device.addr_long))
            self._send_command_dev(device.addr, device.addr_long)
        except KeyError as e:
            self.logger.error("Error creating device: %s", e.args)

    def _get_device_pid(self, addr_long=None):
        self.logger.debug("Getting PID of device: %s", self._hex(addr_long))

        device = self.devices.get(addr_long)
        if device is None:
            return None
        else:
            return device.device_pid

    def _get_device_node_id(self, addr_long=None):
        self.logger.debug("Getting NID of device: %s", self._hex(addr_long))

        device = self.devices.get(addr_long)
        if device is None:
            return None
        else:
            return device.node_identifier

    def _set_device_pid(self, addr_long=None, pid=None):
        if pid is None:
            return

        device = self.devices.get(addr_long)
        if device is not None:
            self.logger.debug("Setting PID of device '%s' to %s",
                              self._hex(addr_long), pid)
            device.device_pid = pid

    def _update_device_data(self, addr_long=None, info=None):
        if info is None:
            return

        device = self.devices.get(addr_long)

        if device is not None:
            self.logger.debug("Setting hw_infos of device: %s",
                              self._hex(addr_long))
            device.device_hw_infos = info

    def _set_device_data(self, src_addr_long, rf_data):
        self.logger.debug("Handling device data...")
        try:
            dev_data = self._parse_device_data(rf_data)
            pid = dev_data["PID"]
            self._set_device_pid(addr_long=src_addr_long, pid=pid)
            self._update_device_data(addr_long=src_addr_long, info=dev_data)

        except KeyError as e:
            self.logger.error("Device data missing parameter: %s", e.args)
            return

    def _set_tx_interval(self, seconds, dest_addr, dest_addr_long):
        # set transmit interval
        self.zigbee_coord.send("tx", frame='A',
                               dest_addr=dest_addr,
                               dest_addr_long=dest_addr_long,
                               data='SET TXT=' + str(seconds) + '\n')
        self._send_node_discover()

    def _send_command_dev(self, dest_addr, dest_addr_long):
        self.logger.debug("Sending command 'DEV' to device '%s'",
                          self._hex(dest_addr_long))

        self.zigbee_coord.send("tx", frame='A',
                               dest_addr=dest_addr,
                               dest_addr_long=dest_addr_long,
                               data='DEV\n')

    def _send_node_discover(self):
        counter = 0
        if NODE_DISCOVER_INTERVAL > SLEEP_INTERVAL:
            sleep_time = SLEEP_INTERVAL
            max_counter = NODE_DISCOVER_INTERVAL/SLEEP_INTERVAL
        else:
            sleep_time = NODE_DISCOVER_INTERVAL
            max_counter = 1
        while self.running:
            if counter == 0:
                try:
                    self.zigbee_coord.send("at", frame='A', command='ND')
                except Exception:
                    self.logger.error("Error in node discover.")
                    return
            sleep(sleep_time)
            counter = (counter + 1) % max_counter

    def send_command_switch(self, nid, state):
        self.logger.debug("Trying to switch device %s to state %s.", nid, state)

        if state is None:
            return

        found_device = False
        for device in self.devices.values():
            dev_id = device.node_identifier
            if dev_id == nid:
                self.logger.debug("Switching device %s to state %s.",
                                  nid, state)
                found_device = True

                dest_addr = device.addr
                dest_addr_long = device.addr_long

                # use proper encoding
                rf_data = 'SET POW=' + state + '\n'
                rf_data = rf_data.decode('utf-8').encode('ascii', 'replace')

                self.zigbee_coord.send("tx", frame='A',
                                       data=rf_data,
                                       dest_addr=dest_addr,
                                       dest_addr_long=dest_addr_long)
            else:
                continue
        if not found_device:
            self.logger.debug("Device %s could not be found and switched.", nid)

    def _handle_frame(self, frame):
        # return if not running anymore
        if not self.running:
            return

        self.logger.debug("Received frame...")

        if frame['id'] == 'at_response' and frame['command'] == 'ND':
            self._handle_node_discover_frame(frame)

        elif frame['id'] == 'rx':
            self._handle_rx_frame(frame)
        else:
            self.logger.debug("Unknown frame. Frame dropped: %s", frame)

    def _handle_node_discover_frame(self, frame):
        self.logger.debug("Handling ND frame: %s", frame)

        try:
            parameter = frame['parameter']
            src_addr_long = parameter['source_addr_long']
        except KeyError as e:
            self.logger.error("Missing parameters to add device: %s", e.args)
            return

        # add device if not already known
        if src_addr_long not in self.devices:
            self._add_device_from_nd(frame)
        else:
            self.logger.debug("Device %s is already known",
                              self._hex(src_addr_long))

    def _handle_rx_frame(self, frame):
        self.logger.debug("Handling rx frame %s", frame)
        try:
            src_addr_long = frame["source_addr_long"]
            rf_data = frame["rf_data"]
        except KeyError as e:
            self.logger.error("Invalid rx frame. Missing key: %s", e.args)
            return

        if src_addr_long not in self.devices:
            if rf_data.startswith("PID"):
                self._add_device_from_rx(frame)
            else:
                self.logger.debug("RX from unknown device.")
                return

        # DEV data
        if rf_data.startswith("PID"):
            device = self.devices.get(src_addr_long)
            registered = device.registered
            if not registered:
                self._set_device_data(src_addr_long, rf_data)
                self._register_device(src_addr_long)
            nid = self._get_device_node_id(src_addr_long)
            self._handle_device_data(rf_data, nid)
        elif rf_data.startswith("ack"):
            self._handle_ack(rf_data)
        # sensor data
        else:
            pid = self._get_device_pid(src_addr_long)
            nid = self._get_device_node_id(src_addr_long)
            if pid is None:
                self.logger.debug("RX from unknown device product type.")
                return

            self.logger.debug("Handling rx frame for device %s with id %s and "
                              "with product type %s",
                              self._hex(src_addr_long), nid, pid)
            if pid in self.parsers:
                self.logger.debug("Calling handle data ...")
                self._handle_sensor_data(src_addr_long, rf_data, nid)

    def _handle_ack(self, rf_data):
        self.logger.debug("Handling ack...: %s", rf_data)

    def _handle_device_data(self, rf_data, node_id):
        handler = self._get_device_handler(node_id)
        if handler is None:
            self.logger.debug("device data handler not found")
            return
        self.logger.debug("Calling device data handler: %s", handler)

        handler(self._parse_device_data(rf_data), node_id)

    def _handle_sensor_data(self, src_addr_long, rf_data, node_id):
        handler = self._get_sensor_handler(node_id)
        if handler is None:
            self.logger.debug("sensor data handler not found")
            return
        self.logger.debug("Calling sensor data handler: %s", handler)

        product_type = self._get_device_pid(src_addr_long)
        if product_type is None:
            return

        try:
            data = self.parsers[product_type].parse(rf_data)
        except Exception:
            self.logger.exception("Error parsing line: %s", rf_data)
            return

        sensor_data = self.parsers[product_type].sensor_data
        device_data = self.parsers[product_type].device_data

        try:
            # adding timestamp for each sensor data
            for sensor in data:
                sensor["timestamp"] = self._time()

            modified_data = {
                'sensor_data': filter(lambda x: x['type'] in sensor_data, data),
                'device_data': filter(lambda x: x['type'] in device_data, data)
            }

            handler(modified_data, node_id)
        except Exception:
            self.logger.exception("Error in rx data handler.")

    def _parse_device_data(self, dev_data):
        self.logger.debug("Parsing dev data: %s", dev_data)
        result = dict(s.split('=') for s in dev_data.split())
        if 'UB' in result:
            del result['UB']
        self.logger.debug("Parse result: %s", result)
        return result

    def _register_device(self, addr_long):
        device = self.devices.get(addr_long)
        pid = device.device_pid
        nid = device.node_identifier
        actuator_data = self.parsers[pid].actuator_data

        handler = self.handlers.get("REGISTER_DEVICE")

        if handler is None:
            return

        try:
            handler(nid, actuator_data)
        except Exception as e:
            self.logger.error("Error registering device: %s", e)

        device.registered = True

    @staticmethod
    def _hex(x):
        return "".join([hex(ord(c))[2:].zfill(2) for c in x])

    @staticmethod
    def _time():
        return format(round(time.time(), 3), '.3f')


if __name__ == "__main__":
    from time import sleep
    zb = ZigBeeCoordinator("/dev/ttyUSB0")
    zb.start()
    try:
        while True:
            sleep(1000)
    finally:
        zb.shutdown()

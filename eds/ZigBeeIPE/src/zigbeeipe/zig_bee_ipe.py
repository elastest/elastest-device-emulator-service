from openmtc_app.onem2m import XAE
from openmtc_onem2m.exc import CSENotFound
from openmtc_onem2m.model import Container
from .zig_bee_coordinator import ZigBeeCoordinator


class ZigBeeIPE(XAE):
    max_nr_of_instances = 30
    default_access_right = False
    units = {
        'temperature': 'Cel',
        'humidity': '%RH',
        'brightness': 'lx',
        'pressure': 'hPa',
        'movement': '',
        'battery_status': '',
        'battery_voltage': 'V',
        'Power': '',
        'Frequency': 'Hz',
        'Work': 'Kwh',
        'Load': 'W',
        'VRMS': 'V',
        'IRMS': 'mA'
    }

    def __init__(self, usb_device="/dev/ttyUSB0", sim=True, sim_period=300,
                 *args, **kw):
        super(ZigBeeIPE, self).__init__(*args, **kw)
        self.usb_device = usb_device
        self.coordinator = ZigBeeCoordinator(usb_device=self.usb_device)
        self.containers = {}
        self.subscriptions = {}
        self.sim = sim
        self.sim_period = sim_period

    def _on_shutdown(self):
        self.coordinator.shutdown()

    def _on_register(self):
        self.logger.info("Starting Coordinator...")
        cnt = Container(resourceName='devices', maxNrOfInstances=0)
        self.devices_container = self.create_container(None, cnt)
        self.coordinator.add_handler('REGISTER_DEVICE', self._register_device)
        if self.sim:
            self.coordinator.start_simulation(self.run_forever,
                                              self.sim_period)
        else:
            self.coordinator.start()

    def _create_device_container(self, nid=None):
        self.logger.debug("Creating container for %s...", nid)

        if nid is not None:
            try:
                cnt = Container(resourceName=nid, maxNrOfInstances=0,
                                labels=["ZigBee-Device",
                                        "openmtc:device",
                                        "openmtc:device:zig_bee"])
                cnt = self.create_container(self.devices_container, cnt)

                self.coordinator.add_handler(nid + '_sensor',
                                             self._handle_sensor_data)
                self.coordinator.add_handler(nid + '_device',
                                             self._handle_device_data)
                return cnt
            except CSENotFound as e:
                self.logger.error("Error creating the container_id %s: %s",
                                  nid, e)
                return None

    def _register_device(self, nid, actuator_data=None):
        self.logger.debug("Registering device...")

        # create the main container for the device
        device_container = self._create_device_container(nid)
        self.containers[nid] = device_container

        if actuator_data:
            cnt = Container(resourceName='actuator_data',
                            maxNrOfInstances=0)
            cnt = self.create_container(device_container, cnt)
            for actuator in actuator_data:
                labels = ["openmtc:actuator_data",
                          "openmtc:actuator_data:%s" % actuator]
                actuator_cnt = Container(resourceName=actuator,
                                         maxNrOfInstances=1, labels=labels)
                actuator_cnt = self.create_container(cnt, actuator_cnt)
                self.add_container_subscription(actuator_cnt,
                                                self._handle_zbs110_switch)
                self.subscriptions[actuator_cnt.path] = nid

    def _handle_zbs110_switch(self, container, content):
        self.logger.debug("Handling ZBS110 switch...")

        path = container.path
        nid = self.subscriptions[path]
        try:
            value = round(float(content[0]['v']))
        except (KeyError, ValueError, TypeError):
            return
        state = 'ON' if value == 1.0 else 'OFF'
        self.coordinator.send_command_switch(nid, state)

    def _get_unified_data(self, cnt_id, data):
        entry = {
            'bn': 'urn:dev:xbee:' + cnt_id,     # basename
            'n': data['type'],                  # name
            't': data['timestamp']              # timestamp
        }

        unit = self.units[data['type']]
        if unit:                                # unit
            entry['u'] = unit

        value = data['value']
        try:
            entry['v'] = float(value)           # value
        except ValueError:
            if isinstance(value, bool):
                entry['vb'] = value
            elif value.lower() == "true":
                entry['vb'] = True
            elif value.lower() == "false":
                entry['vb'] = False
            else:
                entry['vs'] = str(value)

        return [entry]

    def _push_content(self, dev_id, data_type, val):
        val_cnt_id = val['type']
        val_id = dev_id + ":" + data_type + ":" + val_cnt_id
        try:
            val_cnt = self.containers[val_id]
        except KeyError:
            data_id = dev_id + ":" + data_type
            try:
                data_cnt = self.containers[data_id]
            except KeyError:
                dev_cnt = self.containers[dev_id]
                data_cnt = Container(resourceName=data_type,
                                     maxNrOfInstances=0)
                data_cnt = self.create_container(dev_cnt, data_cnt)
                self.containers[data_id] = data_cnt
            val_labels = ["openmtc:%s" % data_type,
                          "openmtc:%s:%s" % (data_type, val_cnt_id)]
            val_cnt = Container(resourceName=val_cnt_id, labels=val_labels)
            val_cnt = self.create_container(data_cnt, val_cnt)
            self.containers[val_id] = val_cnt
        con = self._get_unified_data(dev_id, val)
        self.logger.debug("Pushing content instance %s for id %s",
                          con, val_id)
        self.push_content(val_cnt, con)

    def _handle_sensor_data(self, data, dev_id):
        self.logger.debug("Handling data for device-id: %s, data: %s",
                          dev_id, data)

        for sensor_value in data['sensor_data']:
            self._push_content(dev_id, 'sensor_data', sensor_value)

        for device_value in data['device_data']:
            self._push_content(dev_id, 'device_data', device_value)

    def _handle_device_data(self, data, dev_id):
        dev_cnt = self.containers[dev_id]
        cnt_id = dev_id + ":device_data"

        try:
            cnt = self.containers[cnt_id]
        except KeyError:
            cnt = Container(resourceName='device_data', maxNrOfInstances=1)
            self.containers[cnt_id] = cnt = self.create_container(dev_cnt, cnt)

        self.push_content(cnt, data)

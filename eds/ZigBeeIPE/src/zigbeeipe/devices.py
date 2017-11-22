from random import randint, choice
from re import findall

from futile.logging import LoggerMixin


class Device(LoggerMixin):
    def __init__(self, node_id=None, addr=None, addr_long=None,
                 device_type=None):
        super(Device, self).__init__()
        self.addr = addr
        self.addr_long = addr_long
        self.device_type = device_type
        self.node_identifier = node_id
        self.device_pid = None
        self.device_hw_infos = {}
        self.registered = False


class ZBSBase(LoggerMixin):
    def __init__(self):
        super(ZBSBase, self).__init__()
        self.device_data = []
        self.sensor_data = []
        self.actuator_data = []
        self.pattern = ""
        self.replace = {}
        self.sim_types = {
            'battery_status': {
                'value': lambda: choice(['OK', 'NOT_OK']),
                'unit': ''
            },
            'battery_voltage': {
                'value': lambda: randint(270, 360) / 100.0,
                'unit': 'V'
            },
            'brightness': {
                'value': lambda: randint(20, 980),
                'unit': 'lx'

            },
            'temperature': {
                'value': lambda: randint(100, 300) / 10.0,
                'unit': 'C'
            },
            'pressure': {
                'value': lambda: randint(95000, 115000) / 100.0,
                'unit': 'hPa'
            },
            'humidity': {
                'value': lambda: randint(5, 95),
                'unit': '%'
            },
            'movement': {
                'value': lambda: 1,
                'unit': ''
            },
        }

    def parse(self, rf_data):
        self.logger.debug("Parsing rf_data: %s", rf_data)

        def convert_data(data):

            def _replace_name(n):
                return self.replace.get(n, n)

            if data == "MOVE":
                return {
                    "type": "movement",
                    "value": "1",
                    "unit": ""
                }
            else:
                match = findall(self.pattern, data)
                name = _replace_name(match[0][0])
                value = match[0][1]
                unit = match[0][2]

                return {
                    "type": name,
                    "value": value,
                    "unit": unit
                }

        result = map(convert_data, filter(bool, rf_data.split()))

        self.logger.debug("Parse result: %s", result)
        return result

    def get_simulated_data(self, types):

        def get_sim_data(t):
            try:
                sim_t = self.sim_types[t]
                return {
                    'type': t,
                    'value': sim_t['value'](),
                    'unit': sim_t['unit']
                }
            except KeyError:
                return None

        return filter(bool, map(get_sim_data, types))


class ZBS110(ZBSBase):
    def __init__(self):
        super(ZBS110, self).__init__()
        self.sensor_data = ["Power", "Work", "Load", "Frequency", "VRMS",
                            "IRMS"]
        self.actuator_data = ["Switch"]
        self.pattern = "(\D+)=(?:([a-zA-Z]+|[0-9]+\.?\d*)(\D*))"
        self.replace = {
            "POW": "Power",
            "WORK": "Work",
            "FREQ": "Frequency",
            "LOAD": "Load"
        }


class ZBS121(ZBSBase):
    def __init__(self):
        super(ZBS121, self).__init__()
        self.device_data = ["battery_status", "battery_voltage"]
        self.sensor_data = ["brightness", "temperature", "pressure"]
        self.pattern = "(\D+)=(?:([a-zA-Z]+|[0-9]+\.?\d*)(?:\\xb0|)(\D*))"
        self.replace = {
            "BRI": "brightness",
            "TEM": "temperature",
            "PRES": "pressure",
            "BAT": "battery_status",
            "UBAT": "battery_voltage"
        }


class ZBS122(ZBSBase):
    def __init__(self):
        super(ZBS122, self).__init__()
        self.device_data = ["battery_status", "battery_voltage"]
        self.sensor_data = ["brightness", "temperature", "pressure",
                            "humidity", "movement"]
        self.pattern = "(\D+)=(?:([a-zA-Z]+|[0-9]+\.?\d*)(?:\\xb0|)(\D*))"
        self.replace = {
            "BRI": "brightness",
            "TEM": "temperature",
            "HUM": "humidity",
            "PRES": "pressure",
            "MOVE": "movement",
            "BAT": "battery_status",
            "UBAT": "battery_voltage"
        }

from random import random
from acc import Accel
import time

# import gevent

from openmtc_app.onem2m import XAE
from openmtc_onem2m.model import Container


class MemsIPE(XAE):
    acc = None
    def __init__(self, is_simulation=True, interval=10,
                 *args, **kw):
        super(MemsIPE, self).__init__(*args, **kw)
        self.interval = 10 # in seconds!
        self._is_simulation = is_simulation
        acc = Accel()

    def _create_base_label_container(self):
        label = 'sensor_data'
        container = Container(resourceName=label)
        self._sensor_data_container = self.create_container(
            None,
            container,
            labels=[label, "openmtc:device"],
            max_nr_of_instances=10
        )
        self._single_sensor_map = {}
        for sensor in ["x", "y", "z"]:
            _labels = ["openmtc:sensor_data",
                       "openmtc:sensor_data:%s" % sensor]
            _container = Container(resourceName=sensor)
            _single_sensor_container = self.create_container(
                self._sensor_data_container.path,
                _container,
                labels=_labels,
                max_nr_of_instances=3
            )
            self._single_sensor_map[sensor] = _single_sensor_container


    def _get_sensor_data(self):
        x_l = acc.getValueX_l()
        x_h = acc.getValueX_h()
        y_l = acc.getValueY_l()
        z_l = acc.getValueZ_l()
        y_h = acc.getValueY_h()
        z_h = acc.getValueZ_h()
        

        x = x_l | (x_h<<8)#shifting bits combining High and low reading
        if(x & (1 << 16 - 1)):
            x = x - (1<<16)
        y = y_l | (y_h<<8)#shifting bits combining High and low reading

        if(y & (1 << 16 - 1)):
            y = y - (1<<16)
        z = z_l | (z_h<<8)#shifting bits combining High and low reading

        if(z & (1 << 16 - 1)):
            z = z - (1<<16)

        x = x * 0.001/15#scale shifted values according to selected values in the setup
        y = y * 0.001/15#scale shifted values according to selected values in the setup

        z = z * 0.001/15#scale shifted values according to selected values in the setup

        x = round(x, 4)
        y = round(y, 4)
        z = round(z, 4)

        self.push_sensor_data(x, y, z)


    def push_sensor_data(self, _x, _y, _z):
        _container1 = self._single_sensor_map["x"]
        _container2 = self._single_sensor_map["y"]
        _container3 = self._single_sensor_map["z"]
       # self._single_sensor_map = {}
      #  for sensor in ["x", "y", "z"]:
        timestamp = format(round(time.time(), 3), '.3f')
        unified_data1 = [ {
            'bn': 'urn:dev1:memsipe',      # basename
            'n': "x",                         # name
            't': timestamp,                  # timestamp
            'u': 'g',                         # unit
            'v': float(_x)        # value as float
        }]

        unified_data2 = [
            {
            'bn': 'urn:dev1:memsipe',      # basename
            'n': "y",                         # name
            't': timestamp,                  # timestamp
            'u': 'g',                         # unit
            'v': float(_y)        # value as float
        }]

        unified_data3 = [
            {
            'bn': 'urn:dev1:memsipe',      # basename
            'n': "z",                         # name
            't': timestamp,                  # timestamp
            'u': 'g',                         # unit
            'v': float(_z)        # value as float
        } ]
        self.push_content(_container1, unified_data1)
        self.push_content(_container2, unified_data2)
        self.push_content(_container3, unified_data3)


    def _on_register(self):
        self._create_base_label_container()

        if self._is_simulation is True:
            def simulate_loop():
                _x = random() / 2
                _y = random() / 2
                _z = random() / 2

                self.push_sensor_data(_x, _y, _z)

            # start endless loop
            self.run_forever(self.interval,
                             simulate_loop)

        else:
            acc.setUp()
            self.run_forever(self.interval, self._get_sensor_data)

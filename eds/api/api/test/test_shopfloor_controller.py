# coding: utf-8

from __future__ import absolute_import

from api.models.api_response import ApiResponse
from api.models.brightness_summary import BrightnessSummary
from api.models.humidity_summary import HumiditySummary
from api.models.pressure_summary import PressureSummary
from api.models.temperature_summary import TemperatureSummary
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestShopfloorController(BaseTestCase):
    """ ShopfloorController integration test stubs """

    def test_brightness_summary(self):
        """
        Test case for brightness_summary

        
        """
        response = self.client.open('/rowshan/eds/1.0.0/brightness',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_humidity_summary(self):
        """
        Test case for humidity_summary

        
        """
        response = self.client.open('/rowshan/eds/1.0.0/humidity',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_pressure_summary(self):
        """
        Test case for pressure_summary

        
        """
        response = self.client.open('/rowshan/eds/1.0.0/pressure',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_set_brightness(self):
        """
        Test case for set_brightness

        
        """
        brightness = BrightnessSummary()
        response = self.client.open('/rowshan/eds/1.0.0/brightness',
                                    method='POST',
                                    data=json.dumps(brightness),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_set_heater_state(self):
        """
        Test case for set_heater_state

        
        """
        response = self.client.open('/rowshan/eds/1.0.0/temperature/{device}/actuator/{state}'.format(device='device_example', state='state_example'),
                                    method='POST',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_set_humidity(self):
        """
        Test case for set_humidity

        
        """
        humidity = HumiditySummary()
        response = self.client.open('/rowshan/eds/1.0.0/humidity',
                                    method='POST',
                                    data=json.dumps(humidity),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_set_pressure(self):
        """
        Test case for set_pressure

        
        """
        pressure = PressureSummary()
        response = self.client.open('/rowshan/eds/1.0.0/pressure',
                                    method='POST',
                                    data=json.dumps(pressure),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_set_temperature(self):
        """
        Test case for set_temperature

        
        """
        temperature = TemperatureSummary()
        response = self.client.open('/rowshan/eds/1.0.0/temperature',
                                    method='POST',
                                    data=json.dumps(temperature),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_temperature_summary(self):
        """
        Test case for temperature_summary

        
        """
        response = self.client.open('/rowshan/eds/1.0.0/temperature',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

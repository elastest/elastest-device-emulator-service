# coding: utf-8

from __future__ import absolute_import

from eds_api.models.device_registration_info import DeviceRegistrationInfo
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDeviceController(BaseTestCase):
    """ DeviceController integration test stubs """

    def test_get_devices(self):
        """
        Test case for get_devices

        
        """
        query_string = [('skip', 56),
                        ('limit', 56)]
        response = self.client.open('/rowshan/eds/1.0.0/devices',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_register(self):
        """
        Test case for register

        
        """
        device = DeviceRegistrationInfo()
        response = self.client.open('/rowshan/eds/1.0.0/devices',
                                    method='POST',
                                    data=json.dumps(device),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

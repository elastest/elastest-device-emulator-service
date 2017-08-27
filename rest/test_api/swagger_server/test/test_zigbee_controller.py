# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.zigbee_ipe import ZigbeeIPE
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestZigbeeController(BaseTestCase):
    """ ZigbeeController integration test stubs """

    def test_get_sensor_data(self):
        """
        Test case for get_sensor_data

        
        """
        query_string = [('deviceName', 'deviceName_example')]
        response = self.client.open('/eds/ZigbeeIPE',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

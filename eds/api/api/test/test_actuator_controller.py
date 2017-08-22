# coding: utf-8

from __future__ import absolute_import

from api.models.api_response import ApiResponse
from api.models.device_state import DeviceState
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestActuatorController(BaseTestCase):
    """ ActuatorController integration test stubs """

    def test_get_switch_state(self):
        """
        Test case for get_switch_state

        
        """
        response = self.client.open('/rowshan/eds/1.0.0/actuator/{deviceName}'.format(deviceName='deviceName_example'),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_set_switch(self):
        """
        Test case for set_switch

        
        """
        response = self.client.open('/rowshan/eds/1.0.0/actuator/{deviceName}/{value}'.format(deviceName='deviceName_example', value='value_example'),
                                    method='POST',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

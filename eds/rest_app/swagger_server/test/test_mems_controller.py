# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.mems_data import MemsData
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestMemsController(BaseTestCase):
    """ MemsController integration test stubs """

    def test_get_memsdata(self):
        """
        Test case for get_memsdata

        
        """
        response = self.client.open('/eds/MemsIPE',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

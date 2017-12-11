import unittest

import openmtc_ngsi.wsgi_flask
from openmtc_ngsi.tests.xml import registerContextRequestXML, discoverContextAvailabilityRequestXML,\
    subscribeContextAvailabilityRequestXML,\
    unsubscribeContextAvailabilityRequestXML,\
    updateContextAvailabilityRequestXML
from openmtc_ngsi.tests.data_json_ngsi10 import updateContextRequestJSON,\
    queryContextRequestJSON

class TestJsonNGSI(unittest.TestCase):
    def setUp(self):
        openmtc_ngsi.wsgi_flask.app.config['TESTING'] = True
        self.app = openmtc_ngsi.wsgi_flask.app.test_client()
        
    def test_updateContext(self):
        r = self.app.post("/NGSI10/updateContext", data = updateContextRequestJSON, headers=[("Content-Type", "application/json")])

        self.assertTrue(r.status.startswith("200"), (r.status, list(r.response)))
        
    def test_queryContext(self):
        r = self.app.post("/NGSI10/queryContext", data = queryContextRequestJSON, headers=[("Content-Type", "application/json")])
        
        self.assertTrue(r.status.startswith("200"), (r.status, list(r.response)))

        

        
if __name__ == '__main__':
    unittest.main()
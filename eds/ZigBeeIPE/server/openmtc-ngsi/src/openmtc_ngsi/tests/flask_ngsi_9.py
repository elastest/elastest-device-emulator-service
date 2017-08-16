import unittest

import openmtc_ngsi.wsgi_flask
from openmtc_ngsi.tests.xml import registerContextRequestXML, discoverContextAvailabilityRequestXML,\
    subscribeContextAvailabilityRequestXML,\
    unsubscribeContextAvailabilityRequestXML,\
    updateContextAvailabilityRequestXML

class TestNGSI9(unittest.TestCase):
    def setUp(self):
        openmtc_ngsi.wsgi_flask.app.config['TESTING'] = True
        self.app = openmtc_ngsi.wsgi_flask.app.test_client()
        
    def test_registerContext(self):
        r = self.app.post("/NGSI9/registerContext", data = registerContextRequestXML)

        self.assertTrue(r.status.startswith("200"), (r.status, list(r.response)))
        
    def test_discoverContextAvailability(self):
        r = self.app.post("/NGSI9/discoverContextAvailability", data = discoverContextAvailabilityRequestXML)
        
        self.assertTrue(r.status.startswith("200"), (r.status, list(r.response)))
        
    def test_subscribeContextAvailability(self):
        r = self.app.post("/NGSI9/subscribeContextAvailability", data = subscribeContextAvailabilityRequestXML)
        
        self.assertTrue(r.status.startswith("200"), (r.status, list(r.response)))
        
    def test_updateContextAvailabilitySubscription(self):
        r = self.app.post("/NGSI9/updateContextAvailabilitySubscription", data = updateContextAvailabilityRequestXML)
        
        self.assertTrue(r.status.startswith("200"), (r.status, list(r.response)))
        
    def test_unsubscribeContextAvailability(self):
        r = self.app.post("/NGSI9/unsubscribeContextAvailability", data = unsubscribeContextAvailabilityRequestXML)
        
        self.assertTrue(r.status.startswith("200"), (r.status, list(r.response)))
        

        
if __name__ == '__main__':
    unittest.main()
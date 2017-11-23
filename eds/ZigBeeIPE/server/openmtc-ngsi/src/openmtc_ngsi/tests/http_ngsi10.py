import unittest

import openmtc_ngsi.tests.ngsi_base 
from openmtc_ngsi.tests.xml import registerContextRequestXML,\
    registerContextRequestXML2, subscribeContextAvailabilityRequestXML,\
    subscribeContextAvailabilityNoAttrsRequestXML
from openmtc_ngsi.requests import SubscribeContextAvailabilityRequest,\
    SubscribeContextAvailabilityResponse , SubscribeContextResponse,\
    UpdateContextResponse, SubscribeContextRequest, UnsubscribeContextRequest,\
    UnsubscribeContextResponse, SubscribeResponse
from openmtc_ngsi.tests.data_ngsi10 import subscribeContextRequestXML,\
    updateContextRequestXML

class TestHTTP_NGSI10(openmtc_ngsi.tests.ngsi_base.HTTPTestCaseBase):
    ngsi_name = "/NGSI10"
    num = 10
        
    """
    def test_subscribeContext(self):
        response = self._subscribe()
                
        self.assertIsInstance(response, SubscribeContextResponse)
    """
    def _subscribe(self):
        return self._send_request("/subscribeContext", subscribeContextRequestXML)
    
    def _update(self):
        return self._send_request("/updateContext", updateContextRequestXML)

    def test_subscribe(self):
        response = self._subscribe()
        
        self.assertIsInstance(response, SubscribeContextResponse)
        self.assertIsInstance(response.subscribeResponse, SubscribeResponse)
        self.assertIsNotNone(response.subscribeResponse.subscriptionId)
        
    def test_unscubscribe(self):
        response = self._subscribe()
        subscriptionId = response.subscribeResponse.subscriptionId
        request = UnsubscribeContextRequest(subscriptionId = subscriptionId)
        unsubscribe_response = self._send_request("/unsubscribeContext", request)
        self.assertIsInstance(unsubscribe_response, UnsubscribeContextResponse)
        self.assertEqual(unsubscribe_response.statusCode.code, 200)
    
    def test_register_update_subscribe_notify(self):
        self._register()
        
        self._subscribe()
        
        handler = self._install_notification_handler()
        
        response = self._update()
        
        handler.wait()
        
        self.assertIsInstance(response, UpdateContextResponse)
        
    def test_register_update(self):
        self._register()
        
        response = self._update()
        
        self.assertIsInstance(response, UpdateContextResponse)

    def test_update(self):
        response = self._update()
        
        self.assertIsInstance(response, UpdateContextResponse)

if __name__ == '__main__':
    unittest.main()

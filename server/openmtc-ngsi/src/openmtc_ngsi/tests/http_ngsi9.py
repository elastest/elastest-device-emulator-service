import unittest

import openmtc_ngsi.tests.ngsi_base 
from openmtc_ngsi.tests.xml import registerContextRequestXML,\
    registerContextRequestXML2, subscribeContextAvailabilityRequestXML,\
    subscribeContextAvailabilityNoAttrsRequestXML
from openmtc_ngsi.requests import SubscribeContextAvailabilityRequest,\
    SubscribeContextAvailabilityResponse ,\
    UnsubscribeContextAvailabilityResponse,\
    UnsubscribeContextAvailabilityRequest

class TestHTTP_NGSI9(openmtc_ngsi.tests.ngsi_base.HTTPTestCaseBase):
    ngsi_name = "/NGSI9"
    num = 9
        
    def test_register(self):
        response = self._register()
        
        self.assertEqual(response.errorCode.code, 200)
        
    def _subscribe(self):
        return self._send_request("/subscribeContextAvailability", subscribeContextAvailabilityNoAttrsRequestXML)

    def test_subscribe_notify_no_attrs(self):
        response = self._subscribe()
        
        self.assertIsInstance(response, SubscribeContextAvailabilityResponse)
        
        handler = self._install_notification_handler(2)
        
        self._register()
        
        handler.wait()
        
    def test_subscribe(self):
        response = self._subscribe()
        
        self.assertIsInstance(response, SubscribeContextAvailabilityResponse)
        self.assertIsNotNone(response.subscriptionId)

    def test_unscubscribe(self):
        response = self._subscribe()
        subscriptionId = response.subscriptionId
        request = UnsubscribeContextAvailabilityRequest(subscriptionId = subscriptionId)
        unsubscribe_response = self._send_request("/unsubscribeContextAvailability", request)
        self.assertIsInstance(unsubscribe_response, UnsubscribeContextAvailabilityResponse)
        self.assertEqual(unsubscribe_response.statusCode.code, 200)
        


if __name__ == '__main__':
    unittest.main()

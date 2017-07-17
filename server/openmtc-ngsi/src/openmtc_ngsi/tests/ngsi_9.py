
import unittest
from futile.StringIO import StringIO
from openmtc_ngsi.tests.ngsi_base import NGSITestCaseBase
from openmtc_ngsi.requests import StatusCode


class TestNGSI9Internal(NGSITestCaseBase):    
    def test_RegisterContext(self):
        from openmtc_ngsi.requests import RegisterContextResponse
        
        response = self._register()
        
        self.assertIsInstance(response, RegisterContextResponse)
        self.assertEqual(response.duration, 3600 * 24)
        self.assertIsNotNone(response.registrationId)
        self.assertIsInstance(response.errorCode, StatusCode)
        self.assertEqual(response.errorCode.code, 200)
        
    def test_DiscoverContextAvailability(self):
        from openmtc_ngsi.requests import DiscoverContextAvailabilityRequest, DiscoverContextAvailabilityResponse
        from openmtc_ngsi.tests.xml import discoverContextAvailabilityRequestXML
        
        self._safe_register()

        request = self.parser.parse_request(StringIO(discoverContextAvailabilityRequestXML), DiscoverContextAvailabilityRequest)

        response = self.ngsi9.discoverContextAvailability(request)
        
        self._log_message_element(response)
        
        self.assertIsInstance(response, DiscoverContextAvailabilityResponse)
        self.assertIsInstance(response.errorCode, StatusCode)
        self.assertEqual(response.errorCode.code, 200)
        


if __name__ == '__main__':
    unittest.main()

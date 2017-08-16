import unittest

import openmtc_ngsi.tests.ngsi_base 
from openmtc_ngsi.tests.xml import registerContextRequestXML,\
    registerContextRequestXML2, subscribeContextAvailabilityRequestXML,\
    subscribeContextAvailabilityNoAttrsRequestXML
from openmtc_ngsi.requests import SubscribeContextAvailabilityRequest,\
    SubscribeContextAvailabilityResponse , DiscoverContextAvailabilityResponse

class TestHTTP_Convenience_NGSI9(openmtc_ngsi.tests.ngsi_base.HTTPTestCaseBase):
    ngsi_name = "/NGSI9"
    num = 9
    
    def _send_get(self, path, name = None):
        name = name or self.ngsi_name
        with self.client.get(name + path) as response:
            self.logger.info("Response %s", response.data)
            return self.parser.parse_request(response.data)
        
    def _assert_list(self, o, count = None):
        if count == 0 and o is None:
            return
        self.assertIsInstance(o, list)
        if count is not None:
            self.assertEqual(len(o), count)

    def test_discover_all(self):
        self._register()
        response = self._send_get("/contextEntities")
        self.assertIsInstance(response, DiscoverContextAvailabilityResponse)
        self.assertEqual(response.errorCode.code, 200)
        self._assert_list(response.contextRegistrationResponseList, 1)
        self._assert_list(response.contextRegistrationResponseList[0].contextRegistrationList, 1)
        self._assert_list(response.contextRegistrationResponseList[0].contextRegistrationList[0].entityIdList, 1)
        self._assert_list(response.contextRegistrationResponseList[0].contextRegistrationList[0].contextRegistrationAttributeList, 1)
        
    def test_discover_by_id(self):
        self._register()
        response = self._send_get("/contextEntities/ConferenceRoom")
        self.assertIsInstance(response, DiscoverContextAvailabilityResponse)
        self.assertEqual(response.errorCode.code, 200)
        self._assert_list(response.contextRegistrationResponseList, 1)
        self._assert_list(response.contextRegistrationResponseList[0].contextRegistrationList, 1)
        self._assert_list(response.contextRegistrationResponseList[0].contextRegistrationList[0].entityIdList, 1)
        self._assert_list(response.contextRegistrationResponseList[0].contextRegistrationList[0].contextRegistrationAttributeList, 1)

    def test_discover_by_id_nomatch(self):
        self._register()
        response = self._send_get("/contextEntities/SomeRoom")
        self.assertIsInstance(response, DiscoverContextAvailabilityResponse)
        self.assertEqual(response.errorCode.code, 404)
        self._assert_list(response.contextRegistrationResponseList, 0)
        
    def test_discover_by_attr(self):
        self._register()
        response = self._send_get("/contextEntities/ConferenceRoom/attributes/pressure")
        self.assertIsInstance(response, DiscoverContextAvailabilityResponse)
        self.assertEqual(response.errorCode.code, 200)
        self._assert_list(response.contextRegistrationResponseList, 1)
        self._assert_list(response.contextRegistrationResponseList[0].contextRegistrationList, 1)
        self._assert_list(response.contextRegistrationResponseList[0].contextRegistrationList[0].entityIdList, 1)
        self._assert_list(response.contextRegistrationResponseList[0].contextRegistrationList[0].contextRegistrationAttributeList, 1)

    def test_discover_by_attr_no_match(self):
        self._register()
        response = self._send_get("/contextEntities/ConferenceRoom/attributes/foobar")
        self.assertIsInstance(response, DiscoverContextAvailabilityResponse)
        self.assertEqual(response.errorCode.code, 404)
        self._assert_list(response.contextRegistrationResponseList, 0)

        
if __name__ == '__main__':
    unittest.main()

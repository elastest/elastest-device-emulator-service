import unittest
from futile.StringIO import StringIO
from openmtc_ngsi.tests.ngsi_base import NGSITestCaseBase
from openmtc_ngsi.ngsi import NGSI_10
from openmtc_ngsi.tests.data_ngsi10 import updateContextRequestXML
from openmtc_ngsi.requests import QueryContextRequest, QueryContextResponse,\
    UpdateContextRequest, UpdateContextResponse, ContextElementResponse,\
    ContextElement, EntityId

class TestNGSI10Internal(NGSITestCaseBase):
    def setUp(self):
        super(TestNGSI10Internal, self).setUp()
        self.ngsi10 = NGSI_10()
        self._safe_register()
        
    def _update_context(self):
        request = self.parser.parse_request(StringIO(updateContextRequestXML), UpdateContextRequest)

        return self.ngsi10.updateContext(request)
        
    def test_updateContext(self):
        response = self._update_context()
        
        self.assertIsInstance(response, UpdateContextResponse)
        
    def test_queryContext(self):
        from openmtc_ngsi.tests.data_ngsi10 import queryContextRequestXML
        
        request = self.parser.parse_request(StringIO(queryContextRequestXML), QueryContextRequest)
        
        self._update_context()

        response = self.ngsi10.queryContext(request)
        
        self._log_message_element(response)
        
        self.assertIsInstance(response, QueryContextResponse)
        self.assertIsInstance(response.contextResponseList, list)
        self.assertEqual(len(response.contextResponseList), 3)
        for e in response.contextResponseList:
            self.assertIsInstance(e, ContextElementResponse)
            self.assertIsInstance(e.contextElement, ContextElement)
            self.assertIsInstance(e.contextElement.entityId, EntityId)
            self.assertIsNotNone(e.contextElement.entityId.id)
        
        
if __name__ == '__main__':
    unittest.main()

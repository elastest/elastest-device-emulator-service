import unittest
from futile.StringIO import StringIO
from openmtc_ngsi.tests.data_json_ngsi10 import updateContextRequestJSON,\
    queryContextRequestJSON
from openmtc_ngsi.requests import UpdateContextRequest, EntityId,\
    QueryContextRequest


class TestJSONParse_10(unittest.TestCase):
    def setUp(self):
        from openmtc_ngsi.ngsi_json import NGSIJSONReader  
        self.parser = NGSIJSONReader()
        
        
    def test_UpdateContextRequest(self):
        request = self.parser.parse_request(StringIO(updateContextRequestJSON), UpdateContextRequest)
        self.assertIsInstance(request, UpdateContextRequest)
        self.assertIsInstance(request.contextElementList, list)
        self.assertEqual(len(request.contextElementList), 1)
        self.assertIsInstance(request.contextElementList[0].entityId, EntityId)
        self.assertEqual(request.contextElementList[0].entityId.id, "urn:username:sergio")
        self.assertEqual(request.contextElementList[0].entityId.type, "urn:username")
        
    def test_queryContextRequest(self):
        request = self.parser.parse_request(StringIO(queryContextRequestJSON), QueryContextRequest)
        self.assertIsInstance(request, QueryContextRequest)
        self.assertIsInstance(request.entityIdList, list)
        self.assertEqual(len(request.entityIdList), 1)
        self.assertIsInstance(request.entityIdList[0], EntityId)
        self.assertEqual(request.entityIdList[0].id, "urn:username:sergio")
        self.assertEqual(request.entityIdList[0].type, "urn:username")
        
        
if __name__ == '__main__':
    unittest.main()

import unittest
from futile.StringIO import StringIO
from openmtc_ngsi.tests.data_ngsi10 import updateContextRequestXML
from openmtc_ngsi.requests import UpdateContextRequest, EntityId


class TestXMLParse_10(unittest.TestCase):
    def setUp(self):
        from openmtc_ngsi.xml import RequestParser 
        self.parser = RequestParser()
        
        
    def test_UpdateContextRequest(self):
        request = self.parser.parse_request(StringIO(updateContextRequestXML), UpdateContextRequest)
        self.assertIsInstance(request, UpdateContextRequest)
        self.assertIsInstance(request.contextElementList, list)
        self.assertEqual(len(request.contextElementList), 1)
        self.assertIsInstance(request.contextElementList[0].entityId, EntityId)
        self.assertEqual(request.contextElementList[0].entityId.id, "ConferenceRoom")
        self.assertEqual(request.contextElementList[0].entityId.type, "Room")
        
if __name__ == '__main__':
    unittest.main()

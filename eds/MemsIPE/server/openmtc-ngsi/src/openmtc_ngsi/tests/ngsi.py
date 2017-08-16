
import unittest
from futile.StringIO import StringIO
from openmtc_ngsi.ngsi import NGSI_9
from futile.subprocess import Popen
from signal import SIGTERM
from os.path import expanduser
from openmtc_ngsi.tests.xml import registerContextRequestXML
from openmtc_ngsi.requests import RegisterContextRequest


from openmtc_ngsi.tests.xml import TestXMLParse
from openmtc_ngsi.exc import NGSIError
from openmtc.exc import SCLConflict

SCL_PATH = "~/vcs/openmtc/openmtc-js/gscl"

class TestNGSI9Internal(unittest.TestCase):
    def setUp(self):
        #self.scl_process = Popen(expanduser(SCL_PATH))
        
        #self.scl_process.wait(10)
        
        #raise Exception(self.scl_process.returncode)
        
        from openmtc_ngsi.xml import RequestParser
        self.parser = RequestParser()
        self.ngsi9 = NGSI_9()
    """    
    def tearDown(self):
        self.scl_process.send_signal(SIGTERM)
        self.scl_process.wait(15)
    """
    
    def _register(self):
        request = self.parser.parse_request(StringIO(registerContextRequestXML), RegisterContextRequest)
        return self.ngsi9.registerContext(request)
        
        
    
    def test_RegisterContext(self):
        from openmtc_ngsi.requests import RegisterContextResponse
        
        response = self._register()
        
        self.assertIsInstance(response, RegisterContextResponse)
        self.assertEqual(response.duration, 3600 * 24)
        self.assertIsNotNone(response.registrationId)
        
    def test_DiscoverContextAvailability(self):
        from openmtc_ngsi.requests import DiscoverContextAvailabilityRequest, DiscoverContextAvailabilityResponse
        from openmtc_ngsi.tests.xml import discoverContextAvailabilityRequestXML
        
        try:
            self._register()
        except NGSIError as e:
            if not isinstance(e[0], SCLConflict):
                raise

        request = self.parser.parse_request(StringIO(discoverContextAvailabilityRequestXML), DiscoverContextAvailabilityRequest)

        response = self.ngsi9.discoverContextAvailability(request)
        
        self.assertIsInstance(response, DiscoverContextAvailabilityResponse)

if __name__ == '__main__':
    unittest.main()

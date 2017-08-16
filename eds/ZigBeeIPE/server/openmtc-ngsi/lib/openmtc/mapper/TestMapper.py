'''
Created on 04.06.2013

@author: kca
'''
from openmtc.mapper import BasicMapper

class TestMapper(BasicMapper):
    def _send_request_indication(self, request_indication):
        self.logger.info("Request indication: %s" % (request_indication, ))
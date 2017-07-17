#import json
#from openmtc_scl.serializer import JsonSerializer
from openmtc.scl import UpdateRequestIndication
from aplus import Promise
from futile.logging import LoggerMixin
from urlparse import ParseResult, urlparse, urlunparse


class PA_Activation(LoggerMixin):
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.logger.info("enable activate is %s" % self.config.get("enable_activate"))
        self.logger.info("activate path is %s" % self.config.get("activate_path"))
        self.logger.info("activate payload is %s" % self.config.get("activate_payload"))

    def start(self):
        with Promise() as p:
            
            if self.config.get("enable_activate") is True:

                    from .client import XIXIntentClient
                    fullpath = self.config["activate_path"]
#                    fullpath = "intent://eu.fistar.sdcs"
                    parsed = urlparse(fullpath)
                    request_indication = UpdateRequestIndication(path="/m2m",
                                                                 resource=str(self.config["activate_payload"]),
                                                                 content_type="application/json")
#                    request_indication.path = urlunparse(ParseResult("", "", *parsed[2:]))
                    client = XIXIntentClient(parsed.netloc, self.config["Issuer"], self.logger, self.config["listenActions"])
                    p.fulfill(client.send_request_indication(request_indication))

            else:
                #p.reject("test_only enabled")
                p.fulfill(None)
        return p

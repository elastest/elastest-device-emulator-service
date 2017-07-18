from openmtc_server.Plugin import Plugin
from copy import copy
from urlparse import ParseResult, urlparse, urlunparse
from aplus import Promise
from gevent.queue import Queue
from gevent.threadpool import ThreadPool
from gevent.greenlet import Greenlet
from .IntentHandling import IntentHandler


class IntentTransportPlugin(Plugin):
    def _init(self):
        if self.config.get("enable_intent"):
            self.api.register_transport_client(("intent", "intent"), self.send_request_indication)
        
        self._initialized()

    def send_request_indication(self, request_indication):

        with Promise() as p:
            from .client import XIXIntentClient
            fullpath = request_indication.path
            parsed = urlparse(fullpath)
            request_indication = copy(request_indication)
            request_indication.path = urlunparse(ParseResult("", "", *parsed[2:]))
            client = XIXIntentClient(parsed.netloc, self.config["Issuer"], self.logger, self.config["listenActions"])
            p.fulfill(client.send_request_indication(request_indication))
        return p

    def _start(self):

        try:
            max_queue_size = self.config["queue_max_size"]
        except:
            max_queue_size = 1000

        self.gevent_queue = Queue(max_queue_size)
        
        self.intent_handler = IntentHandler(self.logger, self.config)
        self.greenlet = Greenlet.spawn(self.intent_handler.executeQueuedRequests, self.gevent_queue, self.api.handle_request_indication)
        self.logger.info("started greenlet")
        
        
            
        if self.config.get("enable_intent"):
            self.logger.info("starting intent server")
            from server import IntentServer
            self.intent_server = IntentServer(self.api.handle_request_indication, self.gevent_queue,
                                                  self.config, self.logger)
            self.gevent_threadpool = ThreadPool(1)
            self.gevent_threadpool_worker = self.gevent_threadpool.spawn(self.intent_server.start)
            #self.intent_server.start()
            from .activate import PA_Activation
            pa_activation = PA_Activation(self.config, self.logger)
            pa_activation.start()
        
        for endpoint in self.config["endpoints"]:
            self.api.register_endpoint(endpoint["personality"], "%s://%s" % ("intent",endpoint["interface"]))

        if self.config.get("enable_test"):
            from .test import  test_read_params, test_create_app, test_create_app_property, test_subscribe_pushed_data, test_push_data, test_destroy_app, test_subscribe_apps_with_search_str
            from .test import test_create_app_with_search_str, test_discover_apps_with_search_str, test_get_app, test_get_all_properties, test_get_latest_data_of_property
            contact = "intent://intent_test/m2m"
            from .test_retarget import test_retarget

            test_retarget(self.api.handle_request_indication, self.logger, self.config, "retrieve", "/m2m")
#            contact = "http://localhost:8080" 
            test_read_params(self.api.handle_request_indication, self.logger, self.config)
            self.logger.info("============================================================")
            
#           test_create_app(self.api.handle_request_indication, self.logger, self.config, "myApp")
            self.logger.info("============================================================")
            
#           test_create_app_property(self.api.handle_request_indication, self.logger, self.config, "myApp", "myProperty")
            self.logger.info("============================================================")
            
#           test_subscribe_pushed_data(self.api.handle_request_indication, self.logger, self.config, "myApp", "myProperty", contact)
            self.logger.info("============================================================")
            
#            test_push_data(self.api.handle_request_indication, self.logger, self.config, "myApp", "myProperty")
            self.logger.info("============================================================")
            
#            test_get_all_properties(self.api.handle_request_indication, self.logger, self.config, "myApp")
            self.logger.info("============================================================")
            
#            test_get_latest_data_of_property(self.api.handle_request_indication, self.logger, self.config, "myApp", "myProperty")
            self.logger.info("============================================================")
            
#            test_destroy_app(self.api.handle_request_indication, self.logger, self.config, "myApp")
            self.logger.info("============================================================")
            
#            test_subscribe_apps_with_search_str(self.api.handle_request_indication, self.logger, self.config, "healthDevice", contact)
            test_subscribe_apps_with_search_str(self.api.handle_request_indication, self.logger, self.config, None, contact)
            self.logger.info("============================================================")
            
#            test_create_app_with_search_str(self.api.handle_request_indication, self.logger, self.config, "myApp", "healthDevice")
#            test_create_app_with_search_str(self.api.handle_request_indication, self.logger, self.config, "myApp", None)
            self.logger.info("============================================================")
            
#            test_discover_apps_with_search_str(self.api.handle_request_indication, self.logger, self.config, "healthDevice", "intent://test_action")
            self.logger.info("============================================================")
            
#            test_get_app(self.api.handle_request_indication, self.logger, self.config, "myApp", "intent://test_action")
            self.logger.info("============================================================")
            
#            test_destroy_app(self.api.handle_request_indication, self.logger, self.config, "myApp")
            self.logger.info("============================================================")



        self._started()

    def _stop(self):
        #self.__rack.stop()
        if self.gevent_threadpool_worker:
            self.gevent_threadpool_worker.kill()
        if self.greenlet:
            self.greenlet.kill()
        self._stopped()

from android.broadcast import BroadcastReceiver
from jnius import autoclass
from .android_service.list_iter import PythonListIterator
from .android_service.m2m_service_binder import M2MServiceCallbackImpl

from futile.logging import LoggerMixin
from .IntentHandling import IntentHandler

#from .client import IntentClient
#from openmtc.response import SuccessResponseConfirmation, ErrorResponseConfirmation
#from openmtc_scl.plugins.transport_gevent_http import import

Intent = autoclass('android.content.Intent')
String = autoclass('java.lang.String')
#M2MService = autoclass('org.openmtc.m2mservice.M2MService')
M2MServiceBinder = autoclass('org.renpy.android.m2mservice.M2MServiceBinder')
PythonService = autoclass('org.renpy.android.PythonService')
PythonActivity = autoclass('org.renpy.android.PythonActivity')

class IntentServer(LoggerMixin):

    def __init__(self, request_handler, gevent_queue, config, logger):

        self.config = config
        self.request_handler = request_handler
        self.action = self.config["listenActions"]
        self.logger = logger
        self.logger.info("!!!listening on action "+self.action)
        self.issuer = self.config["Issuer"],
        self.logger.info("!!!listening on action "+self.action)
        self.allowedIssuers = self.config["Issuer"].split(',')
        self.logger.info("!!!listening on action "+self.action)
        if gevent_queue is not None:
            self.gevent_queue = gevent_queue
        else:
            self.gevent_queue = None
        self.logger.info("starting the broadcast receiver")
        self.br = BroadcastReceiver(self._handle_intent_request, actions=[self.action])
        self.list_iter = PythonListIterator()
        self.m2m_service_callback =  M2MServiceCallbackImpl(None)
        self.m2mservice_binder = M2MServiceBinder()

        self.logger.info("created the callback")
        M2MServiceBinder.setCallback(self.m2m_service_callback)
	PythonService.setBinder(self.m2mservice_binder)

        context = PythonService.mService
      #  service = M2MService()
      #  service.onCreate()
      #  service.onStartCommand(None, 0, 0)
      #  service.setContext(context)

        serviceIntent = Intent()
        #serviceIntent.setClassName("org.openmtc.m2mservice", "org.openmtc.m2mservice.M2MService");
        serviceIntent.setClassName("org.renpy.android", "org.renpy.android.PythonService");
        #serviceIntent.setClassName("com.example.test_bind_service_server2", "com.example.test_bind_service_server2.DemoService");
        #context = PythonActivity.mActivity

        ok = context.bindService(serviceIntent)
        if ok is False:
            print("python could not start m2mservice")
        else:
            print("python starting component "+ok)

        self.logger.info("set the callback")
        #self.br.start()

    def start(self):
        self.br.start()

    def _handle_intent_request(self, context, intent_request):

        self.logger.info("received an intent request: "+str(intent_request))
        try:
            extras = intent_request.getExtras()

            issuer = extras.get('Issuer')

        except Exception as e:
            print("error while processing intent "+e)
            return
        intentHandler = IntentHandler(self.logger, self.config)
        request_dict = intentHandler.intent_extras_to_dict(intent_request)
        parsedRequest = intentHandler.parseRequest(issuer, request_dict, context)
        #intentHandler.handleParsedRequest(parsedRequest, self.request_handler, self.gevent_queue)
        intentHandler.handleParsedRequest(parsedRequest, None, self.gevent_queue)

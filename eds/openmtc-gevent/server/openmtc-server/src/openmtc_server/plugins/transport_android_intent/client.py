import json
import time

from openmtc.response import RetrieveResponseConfirmation, CreateResponseConfirmation, \
    DeleteResponseConfirmation, ErrorResponseConfirmation, \
    UpdateResponseConfirmation
from openmtc_scl.serializer import JsonSerializer

from aplus import Promise

try:
    from jnius import autoclass
    from android.broadcast import BroadcastReceiver

    Intent = autoclass('android.content.Intent')
    String = autoclass('java.lang.String')
    PythonService = autoclass('org.renpy.android.PythonService')
except:
    pass


class IntentClient():
    serializer = JsonSerializer()
    context = None

    def __init__(self, issuer, action, logger, replyAction=None):

        self.logger = logger
        self.intent = Intent()
        self.logger.info("creating intent client")
        self.context = PythonService.mService

        self.logger.info("intent action is "+str(action))
        self.intent.setAction(String(action))
        self.logger.info("intent issuer is "+str(issuer))
        self.intent.putExtra("Issuer", str(issuer))
        if replyAction:
            self.intent.putExtra("replyAction", str(replyAction))

        self.intent.putExtra("Issuer", str(issuer))
        self.logger.info("created intent client")
        #self.intent.setPackage(issuer)

    def send_IntentResponse(self, context, request, response):
        self.logger.info("send_intent_response called")
        if response is None:
            self.logger.info("response is None, ignore")
            return
        if isinstance(response, DeleteResponseConfirmation):
            self.logger.info("delete resp confirmation")
            self.intent.putExtra('status', String("200 OK"))

        if response.statusCode is not None:
            self.logger.info("response status code is "+str(response.statusCode))
            self.logger.info("response status is " + response.status)
            status = String(str(response.statusCode) + " " + str(response.status))
            self.logger.info("setting response status in the intent, action is  "+self.intent.getAction())
            self.intent.putExtra('status', status)
        else:
            self.logger.info("response status code is None")

        if isinstance(response, RetrieveResponseConfirmation):
                if response.resource is not None:
                    content = self.serializer.encode(response.resource)
                    self.logger.info("response content is "+content)
                    self.intent.putExtra("content", String(content))
                else:
                    self.logger.info("response content is None")

        if isinstance(response, CreateResponseConfirmation):
                if response.resourceURI is not None:
                    self.logger.info("resourceURI is "+response.resourceURI)
                    self.intent.putExtra("location", String(response.resourceURI))
        if request.intentRequestId is not None:
            self.logger.info("request id is "+request.intentRequestId)
            self.intent.putExtra('requestId', String(str(request.intentRequestId)))
        context.sendBroadcast(self.intent)
        self.logger.info("sent the reply to action "+str(request.replyAction))
        #if request.issuer:
         #   self.intent.setPackage(request.issuer)

    def send_IntentError(self, context, request, response):
        if response.statusCode is not None:
            self.intent.putExtra('status', String("500 Error"))
        if response.errorInfo is not None:
            self.intent.putExtra('content', String(str(response.errorInfo)))
        if request.intentRequestId is not None:
            self.logger.info("request id is "+request.intentRequestId)
            self.intent.putExtra('requestId', String(str(request.intentRequestId)))
        context.sendBroadcast(self.intent)
        return

    def send_create(self, path, data, replyAction, correlationID=None):
        self.logger.info("send_create path is "+path+" data is "+str(data))
        self.intent.putExtra("path", String(path))
        try:
            if data is not None:
                self.intent.putExtra("content", String(str(data)))
        except:
            self.logger.info("error on checking data")
        self.intent.putExtra("method", String("create"))
        # Add correlation id if present
        if correlationID:
            self.intent.putExtra("requestId", String(correlationID))
        else:
            self.intent.putExtra("requestId", String(str(int(time.time()))))
        if replyAction is not None:
            self.intent.putExtra("replyAction", String(replyAction))
        if self.context:
            self.logger.info("context is not none")
            self.context.sendBroadcast(self.intent)
        else:
            self.logger.info("context is none")
        #intent.putExtra('result', String('foobar123'))

    def send_update(self, path, data, replyAction):
        self.logger.info("calling client send_update")
        if replyAction is not None:
            self.intent.putExtra("replyAction", String(replyAction))
        if self.context:
            self.logger.info("context is not none")
            self.intent.putExtra("content", data)
            self.intent.putExtra("method", 'update')
            self.context.sendBroadcast(self.intent)
        else:
            self.logger.info("context is none")

    def send_read(self, path, data):
        if self.context:
            if data is not None:
                    self.intent.putExtra("content", data)
            self.intent.putExtra("method", 'retrieve')
            self.intent.putExtra("path", path)
            self.context.sendBroadcast(self.intent)

    def send_delete(self, path):
        if self.context:
            self.intent.putExtra("path", path)
            self.context.sendBroadcast(self.intent)


class XIXIntentClient():
    def __init__(self, action, issuer, logger, replyAction=None, *args, **kw):
        self.logger = logger
        self.client = IntentClient(issuer, action, logger, replyAction)
        self.__serializer = JsonSerializer()
        self.replyAction = replyAction
#        self.__unserializer = JsonUnserializer()
        self.methodmappers = {
            "create": self._send_create,
            "update": self._send_update,
            "delete": self._send_delete,
            "retrieve": self._send_retrieve,
            "notify": self._send_notify
        }

    def send_request_indication(self, request_indication):
        try:
            self.logger.info("sending req indication for path %s and method %s" %
                             (str(request_indication.path), str(request_indication.method)))
            self.path = request_indication.path
            return self.methodmappers[request_indication.method](request_indication)
        except:
            with Promise() as p:
                p.fulfill(ErrorResponseConfirmation(500, "unknown", "Invalid request_indication").__dict__)
                return p

    def _handle_create(self, resp):
        promise = Promise()
        promise.fulfill(self.serialize(CreateResponseConfirmation(self.path), "create"))
        return promise

    def _send_create(self, request_indication):
        try:
            data = self.__serializer(request_indication.typename, request_indication.resource)
            path, headers = self._get_pathinfo(request_indication)
            p = self.client.send_create(path, data, args=headers)
            return p.then(self._handle_create)
        except:
            with Promise() as p:
                p.fulfill(ErrorResponseConfirmation(500, "create", "Error while sending request").__dict__)
                return p

    def _handle_notify(self, resp):
        promise = Promise()
        return promise
#	promise.fulfill()
#        promise.fulfill(self.__serializer(NotifyResponseConfirmation(self.path), "notify")

    def _send_notify(self, request_indication):
        self.logger.info("sending notify "+str(request_indication)+" client is "+str(self.client))
        try:
#	        data = self.__serializer(request_indication.typename, request_indication.resource)
                #path, headers = self._get_pathinfo(request_indication)
                self.logger.info("path is "+str(request_indication.path)+" data is "+str(request_indication.resource))
                data = json.dumps(request_indication.resource, separators=(',', ':'))
                self.logger.info("path is "+str(request_indication.path)+" data is "+data)
                p = self.client.send_create(request_indication.path, data, self.replyAction, request_indication.correlationID)
                self.logger.info("called send notify")
                return p.then(self._handle_notify)
        except:
            with Promise() as p:
                p.fulfill(ErrorResponseConfirmation(500, "create", "Error while sending request").__dict__)

    def _handle_update(self, resp):
        promise = Promise()
        promise.fulfill(self.serialize(UpdateResponseConfirmation(self.path), "update"))
        return promise

    def _send_update(self, request_indication):
        self.logger.info("sending update "+str(request_indication)+" client is "+str(self.client))
  #      try:
        self.client.send_update(request_indication.path, request_indication.resource, self.replyAction)
        self.logger.info("called send update ")
#           return p.then(self._handle_update)
            #data = self.__serializer(request_indication.typename, request_indication.resource)
 #       except:
#	    self.logger.info("error on sending the update")
#            with Promise() as p:
 #               p.fulfill(ErrorResponseConfirmation(500,"update","Error while sending request").__dict__)
 #               return p

    def _handle_retrieve(self, resp):
        promise = Promise()
        promise.fulfill(self.serialize(RetrieveResponseConfirmation(resp.payload), "retrieve"))
        return promise

    def _send_retrieve(self, request_indication):
        try:
            p = self.client.send_read(self.path, request_indication.resource)
            return p.then(self._handle_retrieve)
        except:
            with Promise() as p:
                p.fulfill(ErrorResponseConfirmation(500, "retrieve", "Error while sending request").__dict__)
                return p

    def _send_delete(self, request_indication):
        try:
            promise = Promise()
            p = self.client.send_delete(self.path)
            p.then(promise.fulfill(DeleteResponseConfirmation()))
            return promise
        except:
            with Promise() as p:
                p.fulfill(ErrorResponseConfirmation(500, "delete", "Error while sending request").__dict__)
                return p

'''
    def create(self, path, resource):
        self.path=path
        return self._send_create(CreateRequestIndication(path, resource))

    def update(self, resource, fields = ()):
        self.path=resource.path
        return self._send_update(UpdateRequestIndication(resource.path, resource, fields = fields))

    def retrieve(self, path):
        self.path=path
        return self._send_retrieve(RetrieveRequestIndication(path))

    def delete(self, path):
        self.path=path
        return self._send_delete(DeleteRequestIndication(path))
'''

from base64 import b64decode
from json import loads

from openmtc_etsi.model import ContentInstance
from openmtc_etsi.scl import CreateRequestIndication, DeleteRequestIndication
from openmtc_server.Plugin import Plugin


# curl request for creating ContentInstance

# curl -X POST -H "Content-Type:application/json"
#              -d '{"test1":{"a":1, "b":5}}'
#         localhost:14000/m2m/applications/ScalableDynamicApp/containers/mycontainer/subcontainers/emulated_device_nb_4/subcontainers/measurements/contentInstances

class SampleBackEndAppPlugin(Plugin):
    def _init(self):
        self.config_parameters()
        self._initialized()

    def config_parameters(self, ):
        self.app_name = self.config.get("app_name", "ScalableDynamicApp");
        self.container_name_list = self.config["container_name_list"]

    def create_container(self, result):

        self.logger.info("registering application [%s] containers %s" % (self.app_name, self.container_name_list))
        path = result.resourceURI + "/containers"

        container = self.container_name_list[0]
        req_indication = CreateRequestIndication(path=path,
                                                 resource="{\"container\":{\"id\":\""+container+"\"}}",
                                                 content_type="application/json")
        promise = self.api.handle_request_indication(req_indication)

    def register_app(self):
        self.logger.info("registering application [%s]" % (self.app_name))
        path = "/m2m/applications/"
        self.app_path = path+self.app_name

        req_indication = CreateRequestIndication(path=path,
                                             resource="{\"application\":{\"appId\":\""+self.app_name+"\"}}",
                                             content_type="application/json")
        promise = self.api.handle_request_indication(req_indication)
        promise.then(self.create_container)

    def _handle_contentInstances_created(self, instance, request_indication):
        self.logger.debug("Content Instance Created function is called\n")

        try:
            content_dict = loads(b64decode(request_indication.resource["content"]["$t"]))
        except KeyError:
            content_dict = loads(b64decode(request_indication.resource["content"]["binaryContent"]))

        self.logger.info("The ContentInstance is " + str(content_dict))

    def deregister_app(self):
        try:
            req_indication = DeleteRequestIndication(path = self.app_path)
            promise = self.api.handle_request_indication(req_indication)
        except:
            pass

    def _start(self):
        self.register_app()
        self.events.resource_created.register_handler(self._handle_contentInstances_created, ContentInstance)
        self._started()

    def _stop(self):
        self.deregister_app()
        self._stopped()

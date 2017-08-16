import xml.etree.ElementTree as ETree
from base64 import b64encode
from gevent.server import DatagramServer
from json import dumps

from openmtc_etsi.model import Application, Container
from openmtc_etsi.response import ErrorResponseConfirmation
from openmtc_etsi.scl import CreateRequestIndication
from openmtc_server.Plugin import Plugin


class ABSUDPServer(DatagramServer):
    def __init__(self, address, gip, *args, **kwargs):
        DatagramServer.__init__(self, listener=address, *args, **kwargs)
        self.gip = gip

    def handle(self, data, address):
        print ("New Connection from: ", address)
        self.gip._handle_data(data)
        self.socket.sendto("Got it!", address)


class ABS_GIP(Plugin):
    def _init(self, ):
        self.configuration_params()
        self._initialized()
        self.containers = {}

    def run_udp_server(self, ):
        self.logger.debug("Starting UDP Server")
        address = (self.ip_address, self.port)
        abs_udp_server = ABSUDPServer(gip=self, address=address)
        abs_udp_server.serve_forever()

    def _start(self, ):
        self.create_application() \
            .then(self.create_container("/m2m/applications/" + self.app_name + "/containers", self.container_name))
        self.api.run_task(self.run_udp_server)
        self._started()

    def _stop(self, ):
        self._stopped()

    def configuration_params(self, ):
        self.app_name = self.config["app_name"]
        self.container_name = self.config["container_name"]
        self.ip_address = self.config["listening_ip"]
        self.port = self.config["port"]
        self.max_nr_of_instances = self.config["max_nr_of_instances"]

    def create_application(self, ):
        path = "/m2m/applications"
        app_object = Application(appId=self.app_name)
        request = CreateRequestIndication(path=path, resource=app_object)
        response = self.api.handle_request_indication(request)
        return response

    def create_container(self, path, container_id):
        if not path.endswith("/containers"):
            path += "/containers"
        container_object = Container(id=container_id, maxNrOfInstances=self.max_nr_of_instances)
        request = CreateRequestIndication(path=path, resource=container_object)
        response = self.api.handle_request_indication(request)
        return response

    def get_manipulated_serial_id(self, id):
        return id.replace(":", "_")

    def create_device_container(self, id):
        container_path = "/m2m/applications/" + self.app_name + "/containers/" + self.container_name + "/subcontainers"
        container = Container(id=id,
                              searchStrings=[';rt="thing"'],
                              maxNrOfInstances=self.max_nr_of_instances)
        request = CreateRequestIndication(path=container_path, resource=container)
        response = self.api.handle_request_indication(request)
        return response

    def create_device_tree(self, device_path, device_id):
        self.logger.debug("Creating device tree for device '%s' in path '%s'", device_id, device_path)

        response = self.create_device_subcontainer(path=device_path + "/subcontainers",
                                                   id="id") \
            .then(lambda response:
                  self.create_device_subcontainer(path=getattr(response, "resourceURI") + "/subcontainers",
                                                  id="unique",
                                                  searchStrings=[';rt="unique-text"'])) \
            .then(self.create_device_subcontainer(path=device_path + "/subcontainers",
                                                  id="Parameters",
                                                  searchStrings=[';rt="observe env-param";obs;ct=41'])
                  .then(lambda response, device_id=device_id:
                        self.add_parameters_container(device_id, getattr(response, "resourceURI"))))
        return response

    def add_parameters_container(self, device_id, path):
        self.logger.debug("Adding '%s' for device_id '%s'...", path, device_id)
        self.containers[device_id] = path

    def create_device_subcontainer(self, path=None, id=None, searchStrings=[]):
        container = Container(id=id, searchStrings=searchStrings, maxNrOfInstances=self.max_nr_of_instances)
        request = CreateRequestIndication(path=path, resource=container)
        response = self.api.handle_request_indication(request)
        return response

    def _handle_data(self, XML_Message):
        print("XML message:", XML_Message)

        root = ETree.fromstring(XML_Message)
        serial_id = root.find('Serial').text.replace(":", "_")

        if serial_id not in self.containers:
            self.create_device_container(serial_id) \
                .then(lambda response, device_id=serial_id: self.create_device_tree(getattr(response, "resourceURI"),
                                                                                    device_id))

        ci = dumps({
            "contentInstance": {
                "content": {
                    "$t": b64encode(XML_Message),
                    "contentType": "application/xml"
                }
            }
        })

        path = self.containers[serial_id]

        self.logger.debug("Pushing ABS data '%s' to path '%s'...", ci, path)

        self._push_content_instance(path, ci) \
            .then(self._handle_ci_push,
                  lambda error, ci=ci, device_id=serial_id: self._handle_ci_push_error(error, ci, device_id))

    def _push_content_instance(self, path, ci):
        if not path.endswith("/contentInstances"):
            path += "/contentInstances"

        request_indication = CreateRequestIndication(path=path,
                                                     resource=ci,
                                                     content_type="application/json")
        response = self.api.handle_request_indication(request_indication)
        return response

    def _handle_ci_push(self, response):
        self.logger.debug("XML data pushed successfully: %s", response)

    def _handle_ci_push_error(self, error, ci, device_id):
        if isinstance(error, ErrorResponseConfirmation):
            status_code = error.status
            if status_code == 'STATUS_NOT_FOUND':
                self.logger.error("Error '%s' while pushing xml data to path: %s", status_code, error.errorInfo)
                self.create_device_container(device_id) \
                    .then(lambda response, device_id=device_id: self.create_device_tree(
                    getattr(response, "resourceURI"), device_id)) \
                    .then(self._push_content_instance(self.containers[device_id], ci)) \
                    .then(lambda x: self.logger.debug("XML data pushed."),
                          lambda x: self.logger.error("Error pushing xml data."))

            if error.status == 'STATUS_CONFLICT':
                self.logger.error("Error '%s' while pushing xml data to path: %s", status_code, error.errorInfo)
        else:
            self.logger.error("Error pushing xml data: %s", error)

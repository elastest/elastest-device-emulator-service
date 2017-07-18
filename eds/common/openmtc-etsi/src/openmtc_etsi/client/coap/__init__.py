#XiXCoap
from openmtc_etsi.serializer.json import JsonSerializer
from openmtc_etsi.scl import CreateRequestIndication, RetrieveRequestIndication, \
    DeleteRequestIndication, UpdateRequestIndication
from openmtc_etsi.response import RetrieveResponseConfirmation, \
    CreateResponseConfirmation, DeleteResponseConfirmation, \
    ErrorResponseConfirmation, \
    NotifyResponseConfirmation, UpdateResponseConfirmation
from coap import CoapClient
from futile.logging import LoggerMixin
import openmtc_etsi.exc
from coap.coapy.coapy.constants import BAD_REQUEST, NOT_FOUND,\
    METHOD_NOT_ALLOWED, UNSUPPORTED_CONTENT_FORMAT, INTERNAL_SERVER_ERROR,\
    BAD_GATEWAY, GATEWAY_TIMEOUT, VALID
from openmtc.model.exc import ModelTypeError
from openmtc_etsi.client.util import decode_result


_coap2etsi = {
    BAD_REQUEST: openmtc_etsi.exc.STATUS_BAD_REQUEST,
    NOT_FOUND: openmtc_etsi.exc.STATUS_NOT_FOUND,
    METHOD_NOT_ALLOWED: openmtc_etsi.exc.STATUS_METHOD_NOT_ALLOWED,
    UNSUPPORTED_CONTENT_FORMAT: openmtc_etsi.exc.STATUS_BAD_REQUEST,
    INTERNAL_SERVER_ERROR: openmtc_etsi.exc.STATUS_INTERNAL_SERVER_ERROR,
    162: openmtc_etsi.exc.STATUS_BAD_GATEWAY,
    BAD_GATEWAY: openmtc_etsi.exc.STATUS_BAD_GATEWAY,
    GATEWAY_TIMEOUT: openmtc_etsi.exc.STATUS_GATEWAY_TIMEOUT
}

# TODO: set Accept option to JSON or XML
class XIXCoap(LoggerMixin):
    """XIXCoap serializes RequestIndications to CoAP messages and sends them using a CoapClient"""
    def __init__(self, uri, client_port=None, scl_base=None,
                 use_xml=False,
                 keyfile=None, certfile=None, block_size_exponent=10,
                 *args, **kw):
        """Initializes XIXCoap and its underlying CoapClient
        
        :param uri:URI referencing the server this clients is trying to reach. Can contain SCHEME://IP:PORT
        :param client_port: Port used by the client when sending requests
        :param scl_base: Default basename to prefix an SCL resource path
        :param use_xml: Binary parameter swapping between content types of xml and json
        """
        self.client = CoapClient(uri, client_port or 25682, keyfile=keyfile, certfile=certfile, block_size_exponent=block_size_exponent)
        self.scl_base = scl_base
        self.logger.debug("CoapClient created with uri %s", uri)
        if use_xml:
            from openmtc_etsi.serializer.xml import XMLSerializer as Serializer
            self.content_type = "application/xml"
        else:
            from openmtc_etsi.serializer.json import JsonSerializer as Serializer
            self.content_type = "application/json"
        self.__serializer = Serializer()
        self.methodmappers = {
            "create": self._send_create,
            "notify": self._send_notify,
            "update": self._send_update,
            "delete": self._send_delete,
            "retrieve": self._send_retrieve
        }

    def send_request_indication(self, request_indication):
        """Serializes a RequestIndication to a CoAP message and sends it using a CoapClient
        
        :param request_indication: RequestIndication to be processed
        :return: Corresponding ResponseConfirmation
        """
        if self.scl_base is not None and \
                not request_indication.path.startswith(self.scl_base) and \
                "://" not in request_indication.path:
            request_indication.path = self.scl_base + request_indication.path

        path = request_indication.path
        if path.startswith('/'):
            path = path[1:]

        mapper = self.methodmappers[request_indication.method]
        return mapper(request_indication, path)

    def _raise_error(self, method, response):
        """Handles reponses containing an error status code. Generates an ErrorResponseConfirmation.
        
        :param method: Request method, can be "create", "notify", "update", "delete" or "retrieve"
        :param response: CoAP response
        """
        try:
            status_code = _coap2etsi[response.code]
        except KeyError:
            self.logger.warning("Failed to map coap response code: %s", response.code)
            status_code = openmtc_etsi.exc.STATUS_INTERNAL_SERVER_ERROR
        except AttributeError:
            self.logger.warning("No response for %s", method)
            status_code = openmtc_etsi.exc.STATUS_INTERNAL_SERVER_ERROR

        if response and hasattr(response, "payload"):
            raise ErrorResponseConfirmation(
                statusCode=status_code,
                primitiveType=method,
                errorInfo=response.payload or "<no further information available>"
            )
        else:
            raise ErrorResponseConfirmation(
                statusCode=status_code,
                primitiveType=method,
                errorInfo=response or "<no further information available>"
            )

    def _send_create(self, request_indication, path):
        """Serializes a CreateRequestIndication to a CoAP POST message and sends it using a CoapClient
        
        :param request_indication: CreateRequestIndication to be processed
        :param path: Resource path
        :return: Corresponding CreateResponseConfirmation
        """
        if request_indication.content_type:
            data = request_indication.resource
        else:
            data = self.__serializer.encode_values(request_indication.typename, request_indication.resource)

        def handle_response(resp):
            if resp.code >= 100:
                self._raise_error("create", resp)
            location = resp.findOption(8)
            if location:
                return CreateResponseConfirmation(location[0].value, resp.payload)
            else:
                return CreateResponseConfirmation(resp.payload)

        return self.client.post(path, data, content_type=self.content_type).then(handle_response)

    def _send_notify(self, request_indication, path):
        """Serializes a NotifyRequestIndication to a CoAP POST message and sends it using a CoapClient
        
        :param request_indication: NotifyRequestIndication to be processed
        :param path: Resource path
        :return: Corresponding NotifyResponseConfirmation
        """
        if request_indication.content_type:
            data = request_indication.resource
        else:
            data = self.__serializer.encode_values(request_indication.typename, request_indication.resource)

        def handle_response(resp):
            if resp.code >= 100:
                self._raise_error("notify", resp)
            return NotifyResponseConfirmation()

        return self.client.post(path, data, content_type=self.content_type).then(handle_response)

    def _send_update(self, request_indication, path):
        """Serializes a UpdateRequestIndication to a CoAP POST message and sends it using a CoapClient
        
        :param request_indication: UpdateRequestIndication to be processed
        :param path: Resource path
        :return: Corresponding UpdateResponseConfirmation
        """
        if request_indication.content_type:
            data = request_indication.resource
        else:
            data = self.__serializer.encode_values(request_indication.typename, request_indication.resource)

        def handle_response(resp):
            if resp.code >= 100:
                self._raise_error("update", resp)
            return UpdateResponseConfirmation()

        return self.client.put(path, data, content_type=self.content_type).then(handle_response)

    def _send_retrieve(self, request_indication, path):
        """Serializes a RetrieveRequestIndication to a CoAP GET message and sends it using a CoapClient
        
        :param request_indication: RetrieveRequestIndication to be processed
        :param path: Resource path
        :return: Corresponding RetrieveResponseConfirmation
        """
        # TODO: Accept must be set dynamically
        self.logger.debug("send retrieve path %s"%path)

        def handle_response(resp):
            if resp.code >= 100:
                self._raise_error("retrieve", resp)
            if resp.code == VALID:
                return RetrieveResponseConfirmation(None)
            else:
                d, ct = decode_result(request_indication.path, resp.payload,
                                      resp.content_format)
            return RetrieveResponseConfirmation(resource=d, content_type=ct)

        return self.client.get(path, accept=50).then(handle_response)

    def _send_delete(self, request_indication, path):
        """Serializes a DeleteRequestIndication to a CoAP DELETE message and sends it using a CoapClient
        
        :param request_indication: DeleteRequestIndication to be processed
        :param path: Resource path
        :return: Corresponding DeleteResponseConfirmation
        """

        def handle_response(resp):
            if not resp or resp.code >= 100:
                self._raise_error("delete", resp)
            else:
                return DeleteResponseConfirmation()

        return self.client.delete(path).then(handle_response)

    def create(self, path, resource):
        """Creates and serializes a CreateRequestIndication to a CoAP POST message and sends it using a CoapClient

        :param path: Resource path
        :param resource: Request payload
        :return: Corresponding CreateResponseConfirmation
        """
        return self.send_request_indication(CreateRequestIndication(path, resource))

    def update(self, resource, fields=()):
        """Creates and serializes a UpdateRequestIndication to a CoAP PUT message and sends it using a CoapClient

        :param path: Resource path
        :return: Corresponding UpdateResponseConfirmation
        """
        return self.send_request_indication(UpdateRequestIndication(resource.path, resource, fields=fields))

    def retrieve(self, path):
        """Creates and serializes a RetrieveRequestIndication to a CoAP GET message and sends it using a CoapClient

        :param path: Resource path
        :return: Corresponding RetrieveResponseConfirmation
        """
        return self.send_request_indication(RetrieveRequestIndication(path))

    def delete(self, path):
        """Creates and serializes a DeleteRequestIndication to a CoAP DELETE message and sends it using a CoapClient

        :param path: Resource path
        :return: Corresponding DeleteResponseConfirmation
        """
        return self.send_request_indication(DeleteRequestIndication(path))

if __name__ == "__main__":
    from openmtc_etsi.model import Application, Subscription, Container
    coap_client = XIXCoap("coap://localhost:4000/m2m", scl_base="/m2m")

    def do_stuff():
        """Test function"""
        print(coap_client.create("/m2m/applications",
                                 Application(appId="myApp")).get())
        print(coap_client.create("/m2m/applications/myApp/subscriptions",
                                 Subscription(contact="http://localhost:9999")
                                 ).get())
        print(coap_client.create("/m2m/applications/myApp/containers",
                                 Container(id="container1")).get())
        print(coap_client.create("/m2m/applications/myApp/containers",
                                 Container(id="container2")).get())
        print(coap_client.create("/m2m/applications/myApp/containers",
                                 Container(id="container3")).get())
        print(coap_client.create("/m2m/applications/myApp/containers",
                                 Container(id="container4")).get())
        print(coap_client.delete("/m2m/applications/myApp").get())

    do_stuff()

from openmtc.client.util import decode_result
from openmtc.response import CreateResponseConfirmation, \
    DeleteResponseConfirmation, \
    ErrorResponseConfirmation, \
    NotifyResponseConfirmation, UpdateResponseConfirmation
from openmtc.scl import CreateRequestIndication, RetrieveRequestIndication, \
    DeleteRequestIndication, UpdateRequestIndication
from openmtc_scl.serializer import JsonSerializer

import openmtc.exc
from coap import CoapClient
from coap.coapy.coapy.constants import BAD_REQUEST, NOT_FOUND,\
    METHOD_NOT_ALLOWED, UNSUPPORTED_CONTENT_FORMAT, INTERNAL_SERVER_ERROR,\
    BAD_GATEWAY, GATEWAY_TIMEOUT
from futile.logging import LoggerMixin

_coap2etsi = {
       BAD_REQUEST: openmtc.exc.STATUS_BAD_REQUEST,
       NOT_FOUND: openmtc.exc.STATUS_NOT_FOUND,
       METHOD_NOT_ALLOWED: openmtc.exc.STATUS_METHOD_NOT_ALLOWED,
       UNSUPPORTED_CONTENT_FORMAT: openmtc.exc.STATUS_BAD_REQUEST,
       INTERNAL_SERVER_ERROR: openmtc.exc.STATUS_INTERNAL_SERVER_ERROR,
       162: openmtc.exc.STATUS_BAD_GATEWAY,
       BAD_GATEWAY: openmtc.exc.STATUS_BAD_GATEWAY,
       GATEWAY_TIMEOUT: openmtc.exc.STATUS_GATEWAY_TIMEOUT
}


class XIXCoap(LoggerMixin):
    def __init__(self, uri, client_port=None, *args, **kw):
        self.client = CoapClient(uri, client_port)
        self.logger.debug("CoapClient created with uri %s", uri)
        self.__serializer = JsonSerializer()
        self.methodmappers = {
            "create": self._send_create,
            "notify": self._send_notify,
            "update": self._send_update,
            "delete": self._send_delete,
            "retrieve": self._send_retrieve
        }

    def send_request_indication(self, request_indication):
        path = request_indication.path
        if path.startswith('/'):
            path = path[1:]

        mapper = self.methodmappers[request_indication.method]
        return mapper(request_indication, path)

    def _raise_error(self, method, response):
        try:
            status_code = _coap2etsi[response.code]
        except KeyError:
            self.logger.warning("Failed to map coap response code: %s", response.code)
            status_code = openmtc.exc.STATUS_INTERNAL_SERVER_ERROR

        raise ErrorResponseConfirmation(
            statusCode=status_code,
            primitiveType=method,
            errorInfo=response.payload or "<no further information available>"
        )

    def _send_create(self, request_indication, path):
        data = self.__serializer.encode_values(request_indication.typename, request_indication.resource)
        resp = self.client.post(path, data, content_type="application/json")
        if resp.code >= 100:
            self._raise_error("create", resp)
        return CreateResponseConfirmation(resp.payload)

    def _send_notify(self, request_indication, path):
        data = self.__serializer.encode_values(request_indication.typename, request_indication.resource)
        resp = self.client.post(path, data, content_type="application/json")
        if resp.code >= 100:
            self._raise_error("notify", resp)
        return NotifyResponseConfirmation()

    def _send_update(self, request_indication, path):
        data = self.__serializer.encode_values(request_indication.typename, request_indication.resource)
        resp = self.client.put(path, data, content_type="application/json")
        if resp.code >= 100:
            self._raise_error("create", resp)
        return UpdateResponseConfirmation()

    def _send_retrieve(self, request_indication, path):
        resp = self.client.get(path)
        if resp.code >= 100:
            self._raise_error("create", resp)

        return decode_result(request_indication.path, resp.payload,
                             resp.content_format)

    def _send_delete(self, request_indication, path):
        resp = self.client.delete(path)
        if resp.code >= 100:
            self._raise_error("create", resp)
        return DeleteResponseConfirmation()

    def create(self, path, resource):
        return self.send_request_indication(CreateRequestIndication(path, resource))

    def update(self, resource, fields = ()):
        return self.send_request_indication(UpdateRequestIndication(resource.path, resource, fields = fields))

    def retrieve(self, path):
        return self.send_request_indication(RetrieveRequestIndication(path))

    def delete(self, path):
        return self.send_request_indication(DeleteRequestIndication(path))

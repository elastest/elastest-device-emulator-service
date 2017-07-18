from base64 import b64encode
from urlparse import urlparse

from futile.logging import LoggerMixin, DEBUG
from futile.net.http.client.RestClient import RestClient
from futile.net.http.exc import NetworkError, HTTPError
from openmtc.exc import OpenMTCNetworkError
from openmtc_etsi.client.util import decode_result
from openmtc_etsi.exc import SCLError, get_error_class
from openmtc_etsi.response import DeleteResponseConfirmation,\
    UpdateResponseConfirmation, CreateResponseConfirmation,\
    NotifyResponseConfirmation, RetrieveResponseConfirmation
from openmtc_etsi.scl import CreateRequestIndication, RetrieveRequestIndication, \
    DeleteRequestIndication, UpdateRequestIndication, NotifyRequestIndication


def _request_wrapper(f):
    def wrapper(self, request_indication):
        if self.scl_base is not None and \
                not request_indication.path.startswith(self.scl_base) and \
                "://" not in request_indication.path:
            request_indication.path = self.scl_base + request_indication.path
        try:
            return f(self, request_indication)
        except HTTPError as e:
            if self.logger.isEnabledFor(DEBUG):
                self.logger.exception(e)
            error_class = get_error_class(e.status)
            raise error_class(e.message, e)
        except NetworkError as e:
            raise OpenMTCNetworkError(e)
    return wrapper


class XIXClient(LoggerMixin):
    def __init__(self, uri, scl_base="/m2m", use_xml=False, etsi_v2=True,
                 etsi_v1_compatibility=True, *args, **kw):
        self.scl_base = scl_base

        if use_xml:
            from openmtc_etsi.serializer.xml import XMLSerializer as Serializer
            content_type = "application/xml"
        else:
            from openmtc_etsi.serializer.json import JsonSerializer as Serializer
            content_type = "application/json"

        self.etsi_v2 = etsi_v2
        self.etsi_v1_compatibility = etsi_v2 or etsi_v1_compatibility

        self.__serializer = Serializer()
        headers = {"Accept": content_type}

        self.__rest = RestClient(uri=uri, headers=headers,
                                 content_type=content_type)

    def set_requesting_entity(self, requesting_entity, password=""):
        self.__rest.set_authinfo(requesting_entity, password)

    def send_request_indication(self, request_indication):
        handler = getattr(self, "_send_" + request_indication.type)
        return handler(request_indication)

    def _get_pathinfo(self, request_indication):
        headers = {}
        path = request_indication.path
        parsed = urlparse(path)

        if parsed.netloc:
            # path = urlunparse(ParseResult('', '', *parsed[2:]))
            headers = {"Host": parsed.netloc}

        # TODO: do this for the other transport plugins as well
        requesting_entity = request_indication.requestingEntity
        if requesting_entity:
            self.logger.debug("Setting requesting entity: %s",
                              requesting_entity)
            if self.etsi_v2:
                headers["From"] = requesting_entity
            if self.etsi_v1_compatibility:
                auth = "Basic %s" % (b64encode("%s:" %
                                               (requesting_entity, )), )
                headers["Authorization"] = auth
        else:
            self.logger.debug("Sending without requesting entity")

        via = request_indication.via
        if via:
            headers["Via"] = ', '.join(map("1.1 ".__add__, via))

        return (path, headers)

    @_request_wrapper
    def _send_create(self, request_indication):
        path, headers = self._get_pathinfo(request_indication)

        if request_indication.content_type:
            headers["Content-Type"] = request_indication.content_type
            data = request_indication.resource
        else:
            data = self.__serializer.encode_values(request_indication.typename,
                                                   request_indication.resource,
                                                   filter_none=True)

        with self.__rest.add(path=path, headers=headers,
                             data=data) as response:
            location = response.getheader("Location") or \
                response.getheader("Content-Location")
            self.logger.debug("Resource created at %s", location)
            try:
                urlparse(location)
            except:
                raise SCLError("SCL transmitted an invalid location for "
                               "created resource: %s" % (location, ))
        return CreateResponseConfirmation(location)

    @_request_wrapper
    def _send_notify(self, request_indication):
        path, headers = self._get_pathinfo(request_indication)

        if request_indication.content_type:
            headers["Content-Type"] = request_indication.content_type
            data = request_indication.resource
        else:
            data = self.__serializer.encode_values(request_indication.typename,
                                                   request_indication.resource,
                                                   filter_none=True)

        self.__rest.post(path=path, headers=headers, data=data).close()
        return NotifyResponseConfirmation()

    @_request_wrapper
    def _send_retrieve(self, request_indication):
        path, headers = self._get_pathinfo(request_indication)

        with self.__rest.get(path,
                             headers=headers) as response:
            if response.status == 204:
                return RetrieveResponseConfirmation(None)
            content_type = response.getheader("Content-Type",
                                              "application/octet-stream")
            rawdata = response.read()
            d, ct = decode_result(request_indication.path, rawdata,
                                  content_type)
            return RetrieveResponseConfirmation(resource=d, content_type=ct)

    @_request_wrapper
    def _send_delete(self, request_indication):
        path, headers = self._get_pathinfo(request_indication)

        self.__rest.delete(path, headers=headers).close()
        return DeleteResponseConfirmation()

    @_request_wrapper
    def _send_update(self, request_indication):
        path, headers = self._get_pathinfo(request_indication)
        if request_indication.content_type:
            headers["Content-Type"] = request_indication.content_type
            data = request_indication.resource
        else:
            data = self.__serializer.encode_values(request_indication.typename,
                                                   request_indication.resource)

        via = request_indication.via
        if via:
            headers["Via"] = ', '.join(map("1.1 ".__add__, via))

        with self.__rest.put(path, data, headers=headers) as response:
            location = response.getheader("Location") or \
                response.getheader("Content-Location")
            self.logger.debug("resource updated at %s", location)
        return UpdateResponseConfirmation()

    def create(self, path, resource):
        return self._send_create(CreateRequestIndication(path, resource))

    def notify(self, path, resource):
        return self._send_notify(NotifyRequestIndication(path, resource))

    def update(self, resource, fields=()):
        return self._send_update(UpdateRequestIndication(resource.path,
                                                         resource,
                                                         fields=fields))

    def retrieve(self, path):
        return self._send_retrieve(RetrieveRequestIndication(path))

    def delete(self, path):
        return self._send_delete(DeleteRequestIndication(path))

DIAClient = MIDClient = XIXClient

from urlparse import urlparse

from futile.collections import OrderedDict
from openmtc.mapper import BasicMapper, MapperError
from openmtc_etsi.model import (get_etsi_type as get_resource_type,
                                ContentInstance)
from openmtc_etsi.scl import (RetrieveRequestIndication,
                              CreateRequestIndication, UpdateRequestIndication,
                              DeleteRequestIndication)


def _is_persistent(instance):
    return bool(instance.path)


class ETSIMapper(BasicMapper):
    def __init__(self, scl, *args, **kw):
        super(ETSIMapper, self).__init__(*args, **kw)

        if not callable(scl):
            try:
                scl = scl.send_requestindication
                self.client = scl
            except AttributeError:
                parsed = urlparse(scl)
                if parsed.scheme.lower() in ("", "https", "http"):
                    from openmtc_etsi.client.http import XIXClient
                    scl = XIXClient(scl, scl_base="/m2m")
                elif parsed.scheme.lower() == "coap":
                    from openmtc_etsi.client.coap import XIXCoap
                    scl = XIXCoap(scl, scl_base="/m2m")
                else:
                    raise ValueError(
                        "Unsupported URL scheme: %s" % (parsed.scheme,))
                self.client = scl
                scl = scl.send_request_indication

        self._send_request = scl

    def set_requesting_entity(self, requesting_entity):
        self.scl.set_requesting_entity(requesting_entity)

    def create(self, path, instance):
        request_indication = CreateRequestIndication(path, instance)
        instance.path = self._send_request(
            request_indication).resourceURI
        self.logger.debug("Set instance path: %s", instance.path)
        instance._synced = False
        #        self._attach_instance(instance)
        return instance

    def update(self, instance, fields=None):
        if not _is_persistent(instance):
            raise MapperError("Instance is not yet stored")

        self._do_update(instance, fields)

    def _do_update(self, instance, fields):
        request_indication = UpdateRequestIndication(instance.path, instance,
                                                     fields=fields)

        self._send_request(request_indication)

    def get(self, path):
        response_confirmation = self._get_data(path)
        self.logger.debug("Received response: %s",
                          response_confirmation.resource)
        return response_confirmation.resource

    def delete(self, instance):
        request_indication = DeleteRequestIndication(
            getattr(instance, "path", instance))
        self._send_request(request_indication)

    def send_request(self, request_indication):
        self._send_request(request_indication)

    def _get_data(self, path):
        return self._send_request(RetrieveRequestIndication(path))

    def _map(self, path, typename, data):
        type = get_resource_type(typename)
        return self._fill_resource(type(path=path), data)

    def _fill_resource(self, res, data):
        for c in res.subresources:
            try:
                link = data.pop(c.name + "Reference")
            except KeyError:
                data[c.name] = None
                continue

            data[c.name] = self._make_subresource(c.type, link, res)

        for c in res.collections:
            try:
                collection = data[c.name]
            except KeyError:
                data[c.name] = None
                continue

            ct = c.content_type
            if c.name == "contentInstanceCollection":
                # hack taken from openmtc_scl.serializer.parse_representation
                content_instances = OrderedDict()
                for ci_values in collection["contentInstance"]:
                    ci = ContentInstance(ci_values["href"], **ci_values)
                    content_instances[ci_values["href"]] = ci
                data[c.name] = content_instances.values()

                if content_instances:
                    data["latest"] = content_instances[data["latest"]["$t"]]
                    data["oldest"] = content_instances[data["oldest"]["$t"]]
            else:
                data[c.name] = [self._make_subresource(ct, r["$t"], res) for r
                                in collection["namedReference"]]

        res.set_values(data)

        res._synced = True
        # self._attach_instance(res)

        return res

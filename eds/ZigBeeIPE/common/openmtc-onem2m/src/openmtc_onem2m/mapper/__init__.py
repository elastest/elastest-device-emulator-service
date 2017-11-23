try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from openmtc.mapper import BasicMapper, MapperError
from openmtc_onem2m import OneM2MRequest
from openmtc_onem2m.transport import OneM2MOperation


def _is_persistent(instance):
    return bool(instance.path)


class OneM2MMapper(BasicMapper):
    def __init__(self, cse, originator=None, *args, **kw):
        super(OneM2MMapper, self).__init__(*args, **kw)

        scheme = urlparse(cse).scheme.lower()
        if scheme in ("", "https", "http"):
            from openmtc_onem2m.client.http import get_client
            self._send_request = get_client(cse, use_xml=False).send_onem2m_request
        elif scheme in ("mqtt", "mqtts", "secure-mqtt"):
            from openmtc_onem2m.client.mqtt import get_client
            self._send_request = get_client(cse, use_xml=False, client_id=originator).send_onem2m_request
        elif scheme == "coap":
            raise NotImplementedError
        else:
            raise ValueError(
                "Unsupported URL scheme: %s" % (scheme,)
            )
        self.originator = originator

    def create(self, path, instance):
        for a in [a.name for a in type(instance).attributes if a.accesstype == a.RO]:
            try:
                setattr(instance, a, None)
            except AttributeError:
                pass

        # TODO(rst): add resource_type
        response = self._send_request(OneM2MRequest(
            OneM2MOperation.create,
            path,
            self.originator,
            ty=type(instance),
            pc=instance
        )).get()

        if response.content:
            for k, v in response.content.values.items():
                try:
                    setattr(instance, k, v)
                except AttributeError:
                    pass
            instance.path = '/'.join([path, response.content.resourceName])
        else:
            instance.path = path

        self.logger.debug("Set instance path: %s" % (instance.path, ))
        instance._synced = False
        return instance

    def update(self, instance, fields=None):
        if not _is_persistent(instance):
            raise MapperError("Instance is not yet stored")
        return self._do_update(instance, fields)

    def _do_update(self, instance, fields=None):
        if fields:
            for a in [a.name for a in type(instance).attributes if a.name not in fields]:
                try:
                    setattr(instance, a, None)
                except AttributeError:
                    pass
            instance.childResource = []

        # remove NP attributes
        for a in [a.name for a in type(instance).attributes if a.accesstype in (a.WO, a.RO)]:
            try:
                setattr(instance, a, None)
            except AttributeError:
                pass

        response = self._send_request(OneM2MRequest(
            OneM2MOperation.update,
            instance.path,
            self.originator,
            pc=instance
        )).get()
        try:
            response.content.path = instance.path
        except AttributeError:
            pass
        return response.content

    def get(self, path):
        response = self._get_data(path)
        response.content.path = path
        self.logger.debug("Received response: %s", response.content)
        return response.content

    def delete(self, instance):
        """ DUNNO, somethings gets deleted

        :param instance: instance/object or a string representing its path
        """
        self._send_request(OneM2MRequest(
            OneM2MOperation.delete,
            getattr(instance, "path", instance),
            self.originator
        ))

    def _get_data(self, path):
        return self._send_request(OneM2MRequest(
            OneM2MOperation.retrieve,
            path,
            self.originator
        )).get()

    # TODO(rst): check if this can be removed in parent class
    @classmethod
    def _patch_model(cls):
        pass

    def _fill_resource(self, res, data):
        pass

    def _map(self, path, typename, data):
        pass

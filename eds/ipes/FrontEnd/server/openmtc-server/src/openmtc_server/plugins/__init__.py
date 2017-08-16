from abc import ABCMeta, abstractmethod
from openmtc_server.Plugin import Plugin


class TransportPlugin(Plugin):
    __metaclass__ = ABCMeta

    @abstractmethod
    def send_request(self, request):
        """
        :param openmtc_server.transportdomain.Request request:
        :return Promise:
        """
        raise NotImplementedError

from openmtc_server.Plugin import Plugin
from aplus import Promise
from .ConnectivityMgm import ConnectivityMgm

class ConnectivityManagementM2MGWPlugin(Plugin):
    def _init(self):
        self.conn_mgm = ConnectivityMgm(self.config, self.logger, self.api)
        self.api.register_connectivity_handler(self.conn_mgm.process_connectivity_request)
        self.conn_mgm.create_lwm2m_mgm_resources()
        self.conn_mgm.start()
        self._initialized()

    def _start(self):
        self._started()

    def _stop(self):
        self._stopped()

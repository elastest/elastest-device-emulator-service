from urlparse import urlparse
from re import compile as re_compile
from netifaces import AF_INET, AF_INET6

from aplus import Promise
from openmtc.exc import OpenMTCNetworkError
from openmtc_onem2m.model import RemoteCSE, AE
from futile.collections import get_iterable
from openmtc_onem2m.transport import OneM2MErrorResponse
from openmtc_server import Component
from openmtc_onem2m.exc import CSETargetNotReachable, CSENotImplemented
from openmtc_server.util import get_regex_path_component

PATH_COMPONENT = get_regex_path_component()


class OneM2MTransportDomain(Component):
    def __init__(self, config, *args, **kw):
        super(OneM2MTransportDomain, self).__init__(*args, **kw)

        self._api = None
        self.events = None

        self.config = config

        self.sp_id = self.config.get("onem2m", {}).get("sp_id", "")

        self._addresses = {}

        self._poa_templates = []

        self._endpoints = []

        self._poa_lists = {}

        self._get_clients = {}

        ae_id = r'(C%s)' % PATH_COMPONENT
        sp_id = r'//(%s)' % PATH_COMPONENT
        cse_id = r'/(%s)' % PATH_COMPONENT
        path_suffix = r'(?:/' + PATH_COMPONENT + r')*'
        self.cse_ae_id_matcher = re_compile(r'^' + ae_id +
                                            r'(%s)' % path_suffix)
        self.sp_cse_id_matcher = re_compile(r'^' + cse_id + path_suffix)
        self.abs_cse_id_matcher = re_compile(r'^' + sp_id + cse_id +
                                             path_suffix)

    def initialize(self, api):
        self._api = api
        self.events = api.events

        # addresses
        self._api.events.interface_created.register_handler(
            self._handle_interface_created)
        self._api.events.interface_removed.register_handler(
            self._handle_interface_removed)
        self._api.events.address_created.register_handler(
            self._handle_address_created)
        self._api.events.address_removed.register_handler(
            self._handle_address_removed)

        # remote CSEs
        self.events.resource_created.register_handler(
            self._handle_cse_created, RemoteCSE)
        self.events.resource_updated.register_handler(
            self._handle_cse_updated, RemoteCSE)
        self.events.resource_deleted.register_handler(
            self._handle_cse_deleted, RemoteCSE)

        # AEs
        self.events.resource_created.register_handler(
            self._handle_ae_created, AE)
        self.events.resource_updated.register_handler(
            self._handle_ae_updated, AE)
        self.events.resource_deleted.register_handler(
            self._handle_ae_deleted, AE)

        interfaces = self._api.network_manager.get_interfaces().get()
        self._addresses = {i.name: filter(self._filter_out_link_local,
                                          i.addresses)
                           for i in interfaces}

    @staticmethod
    def _filter_out_link_local(address):
        return not address.address.startswith("fe80:")

    def _get_address_list(self):
        return [i for s in self._addresses.values() for i in s]

    def _create_endpoints(self):
        self._endpoints = []

        for poa_t in self._poa_templates:
            def map_func(address):
                if address.family == AF_INET6:
                    a = '[' + address.address + ']'
                else:
                    a = address.address
                return poa_t.scheme + '://' + a + ':' + str(poa_t.port)

            if poa_t.server_address == "::":
                def filter_func(x):
                    return x
            elif poa_t.server_address in ("", "0.0.0.0"):
                def filter_func(x):
                    return x.family == AF_INET
            else:
                def filter_func(x):
                    return x.address == poa_t.server_address

            self._endpoints += map(map_func, filter(filter_func,
                                                    self._get_address_list()))

    def _handle_interface_created(self, interface):
        self._addresses[interface.name] = filter(self._filter_out_link_local,
                                                 interface.addresses)
        self._create_endpoints()

    def _handle_interface_removed(self, interface):
        del self._addresses[interface.name]
        self._create_endpoints()

    def _handle_address_created(self, interface_name, address):
        if self._filter_out_link_local(address):
            self._addresses[interface_name].append(address)
            self._create_endpoints()

    def _handle_address_removed(self, interface_name, address):
        if self._filter_out_link_local(address):
            self._addresses[interface_name].remove(address)
            self._create_endpoints()

    # TODO(rst): find out if IDs starting with slash or not
    def _handle_cse_created(self, instance, req=None):
        self.logger.debug("_handle_cse_created(instance=%s, req=%s)",
                          instance, req)
        self.add_poa_list(instance.CSE_ID[1:], instance.pointOfAccess)

    def _handle_cse_updated(self, instance, req=None):
        self.logger.debug("_handle_cse_updated(instance=%s, req=%s)",
                          instance, req)
        # self._remove_poas(req_ind.path)
        # self.add_poa_list(instance.pointOfAccess, instance.path)

    def _handle_cse_deleted(self, instance, req):
        self.logger.debug("_handle_cse_deleted(req_ind=%s)", req)
        # self._remove_poas(req.path)

    def _handle_ae_created(self, instance, req=None):
        self.logger.debug("_handle_ae_created(instance=%s, req_ind=%s)",
                          instance, req)
        self.add_poa_list(instance.AE_ID, instance.pointOfAccess)

    def _handle_ae_updated(self, instance, req=None):
        self.logger.debug("_handle_ae_created(instance=%s, req_ind=%s)",
                          instance, req)
        # self._remove_poas(req.path)
        self.add_poa_list(instance.AE_ID, instance.pointOfAccess)

    def _handle_ae_deleted(self, instance, req):
        self.logger.debug("_handle_ae_created(instance=%s, req_ind=%s)",
                          instance, req)
        # self._remove_poas(req.path)

    def register_client(self, schemes, client):
        """Registers a specific client for the given schemes."""
        schemes = set(map(str.lower, get_iterable(schemes)))

        for scheme in schemes:
            self._get_clients[scheme] = client

    def register_point_of_access(self, poa):
        """Registers a point of access."""
        self._poa_templates.append(poa)
        self._create_endpoints()

    def send_onem2m_request(self, onem2m_request):
        # TODO: handle here multiple access points and intelligent decisions
        # TODO(rst): handle notify re-targeting correctly
        with Promise() as p:

            path = onem2m_request.to

            if self.cse_ae_id_matcher.match(path):  # local AE
                ae_id, path = self.cse_ae_id_matcher.findall(path).pop()
                poa_list = self._poa_lists.get(ae_id, [])
                onem2m_request.to = path.lstrip('/')
            elif self.sp_cse_id_matcher.match(path):  # other sp-relative CSE
                cse_id = self.sp_cse_id_matcher.findall(path).pop()
                poa_list = self._poa_lists.get(cse_id, [])
            elif self.abs_cse_id_matcher.match(path):  # other absolute CSE
                sp_id, cse_id = self.abs_cse_id_matcher.findall(path).pop()
                if self.sp_id == sp_id:
                    poa_list = self._poa_lists.get(cse_id, [])
                else:
                    # contact to other M2M Service provider not implemented yet
                    raise CSENotImplemented()
            else:
                poa_list = []

            if not poa_list:
                p.reject(CSETargetNotReachable())

            for poa in poa_list:
                use_xml = False  # TODO(rst): check how this needs to be handled
                client = self._get_clients[urlparse(poa).scheme](poa, use_xml) # TODO(hve): add scheme test.
                try:
                    response = client.send_onem2m_request(onem2m_request).get()
                    p.fulfill(response)
                except OpenMTCNetworkError:
                    continue
                except OneM2MErrorResponse as error_response:
                    p.reject(error_response)

            if p.isPending():
                p.reject(CSETargetNotReachable())
        return p

    # TODO(rst): add here more options to retrieve only non-local addresses etc.
    def get_endpoints(self):
        return self._endpoints

    def add_poa_list(self, identifier, poa_list):
        self._poa_lists[identifier] = poa_list

from openmtc_cse.transport.mappingfunction import openmtc_server

from openmtc_etsi.scl import RetrieveRequestIndication, NotifyRequestIndication
from openmtc_onem2m.model import RemoteCSE
from openmtc_onem2m.serializer import get_onem2m_decoder
from openmtc_server.Plugin import Plugin
from openmtc_etsi.model import M2mPoc, Scl
from openmtc_scl.mappingfunction import map_request_to_request_indication, \
    map_response_confirmation_to_response, \
    map_error_response_confirmation_to_response
import openmtc_scl.api

NOTIFY_ROUTE = "/notify-coap-etsi"

_notify_path = NOTIFY_ROUTE + "/"

class CoAPRetargetingHandler(Plugin):
    def _init(self):
        self._known_uris = {}

        self.scl_id = openmtc_scl.api.config["etsi"]["scl_id"]
        self.cse_base = openmtc_server.api.config["onem2m"]["cse_base"]

        # TODO: limit this to non-mId interfaces
        connectors = self.api.get_connectors(None,
                                             self._handle_connector_created)
        map(self._handle_connector_created, connectors)

        # etsi handlers
        self.events.resource_created.register_handler(
            self._handle_m2mpoc_created, M2mPoc)
        self.events.resource_deleted.register_handler(
            self._handle_m2mpoc_deleted, M2mPoc)
        self.events.resource_updated.register_handler(
            self._handle_m2mpoc_updated, M2mPoc)

        self.events.resource_created.register_handler(
            self._handle_scl_created, Scl)
        self.events.resource_deleted.register_handler(
            self._handle_scl_deleted, Scl)
        self.events.resource_updated.register_handler(
            self._handle_scl_updated, Scl)

        # onem2m handlers
        self.events.resource_created.register_handler(
            self._handle_cse_created, RemoteCSE)
        self.events.resource_deleted.register_handler(
            self._handle_cse_deleted, RemoteCSE)
        self.events.resource_updated.register_handler(
            self._handle_cse_updated, RemoteCSE)

        self._initialized()

    def _start(self):
        req = RetrieveRequestIndication("/m2m/scls")

        def handle_scls(result):
            # get scls
            for scl in result.resource.sclCollection:
                path = scl.path
                link = scl.link
                # add scl
                self._add_link(link, path)

        self.api.handle_request_indication(req).then(handle_scls)
        self._started()

    def _handle_connector_created(self, connector):
        connector.register_route(NOTIFY_ROUTE, self._handle_notify)

    def _handle_m2mpoc_created(self, instance, req_ind=None):
        self._add_link(instance.contactInfo, instance.path)

    def _handle_m2mpoc_deleted(self, instance, req_ind):
        self._remove_link(req_ind.path)
        pass

    def _handle_m2mpoc_updated(self, instance, req_ind=None):
        self._add_link(instance.contactInfo, instance.path)
        pass

    def _handle_scl_created(self, instance, req_ind=None):
        self._add_link(instance.link, instance.path)

    def _handle_scl_deleted(self, instance, req_ind):
        self._remove_link(req_ind.path)
        pass

    def _handle_scl_updated(self, instance, req_ind=None):
        self._remove_link(req_ind.path)
        self._add_link(instance.link, instance.path)
        pass

    def _handle_cse_created(self, instance, req_ind=None):
        self.logger.debug("_handle_cse_created(instance=%s, req_ind=%s)", instance, req_ind)
        self._add_link(instance.pointOfAccess, instance.path, is_etsi=False)

    def _handle_cse_deleted(self, instance, req_ind):
        self.logger.debug("_handle_cse_deleted(req_ind=%s)", req_ind)
        self._remove_link(req_ind.path)
        pass

    def _handle_cse_updated(self, instance, req_ind=None):
        self.logger.debug("_handle_cse_updated(instance=%s, req_ind=%s)", instance, req_ind)
        self._remove_link(req_ind.path)
        self._add_link(instance.pointOfAccess, instance.path, is_etsi=False)
        pass

    def _handle_notify(self, request):
        request_indication = map_request_to_request_indication(request)
        try:
            data = request_indication.resource.read()
        except AttributeError:
            data = request_indication.resource

        notify = NotifyRequestIndication(
            path=request_indication.path[len(_notify_path):],
            resource=data,
            content_type=request_indication.content_type
        )

        return self.api.send_request_indication(notify) \
            .then(lambda r: map_response_confirmation_to_response(request, r),
                  lambda e: map_error_response_confirmation_to_response(request,
                                                                        e))

    def _handle_etsi_retargeting(self, request):
        result = self.api.send_request(request)
        return result

    def _handle_onem2m_retargeting(self, request):
        return self.api.send_request(request)

    def _add_link(self, link, path, is_etsi=True):
        """
        Adds the link to the list of known URIs, and registers a retargeting
        handler.

        :param link: link to other scl
        :type link: str
        """

        def handle_link(link):
            link = self.__link_to_coap(link)

            if path in self._known_uris:
                if self._known_uris[path] == link:
                    self.logger.debug("SCL link of %s (%s) is already known", path,
                                      link)
                else:
                    # same path, different link. remove old link, add new one
                    self.logger.debug("Updating link of %s: %s -> %s", path,
                                      self._known_uris[path], link)
                    self._remove_link(path)
                    self._add_link(link, path)
            elif link in self._known_uris.values():
                # same link, different path, let's find which path occupies it
                for key, value in self._known_uris.iteritems():
                    if value == link:
                        self.logger.debug(
                            "SCL link of %s (%s) is already used by %s", path, link,
                            key)
                        break
            else:
                self.logger.debug("Adding link of %s (%s)", path, link)
                self._known_uris[path] = link
                if is_etsi:
                    self.api.register_retargeting_handler(link, self._handle_etsi_retargeting)
                else:
                    self.api.register_retargeting_handler(link, self._handle_onem2m_retargeting)

        # if list, iterate through all members
        if isinstance(link, list):
            for l in link:
                handle_link(l)
        else:
            handle_link(link)

    def _remove_link(self, path):
        """
        Remove the link of a given path, and unregisters the retargeting
        handler.

        :param path: path that link belongs to
        :type path: str
        """
        if path in self._known_uris:
            rlink = self._known_uris[path]
            self.api.unregister_retargeting_handler(rlink,
                                                    self._handle_etsi_retargeting)
            self.logger.debug("Removed link of %s (%s)", path, rlink)
            del self._known_uris[path]
        else:
            self.logger.debug(
                "Unable to remove link of '%s': path not found in known uris",
                path)

    def __link_to_coap(self, link):
        try:
            return "coap://" + link.split("://")[1]
        except:
            self.logger.warn("unable to update link for coap: %s", link)
            return link

    # copied from OneM2MMethodDomain
    def _decode_content(self, request):
        try:
            request.content = request.content.read()
        except AttributeError:
            pass

        serializer = get_onem2m_decoder(request.content_type)
        # TODO: kca: properly handle encodings
        return serializer.decode_resource_values(request.content)

from aplus import Promise
from openmtc_etsi.exc import STATUS_OK
from openmtc_etsi.model import M2mPoc
from openmtc_etsi.scl import UpdateRequestIndication
from openmtc_server.Plugin import Plugin
from openmtc_server.util.async import async_all


class NSCLm2mPocHandler(Plugin):
    pocs_info = {}
    """
    format:
        pocs_info = {
            scl_path1: {
                poc1_path: {
                    onlineStatus: "online"
                },
                poc2_path: {
                    onlineStatus: "offline"
                }
                onlineStatus: online
            },
        }
    """

    def _init(self):
        self.events.resource_created.register_handler(self._handle_created, M2mPoc)
        self.events.resource_deleted.register_handler(self._handle_deleted, M2mPoc)
        self.events.resource_updated.register_handler(self._handle_updated, M2mPoc)

        self.shelve = self.get_shelve("resources")
        self._load_resources(self.shelve) \
            .then(self._initialized, self._error)

    def _load_resources(self, shelve):
        """
            @type shelve: GEventSQLShelve
        """
        self.logger.debug("_load_resources: %s", shelve)

        def handle_items(items):
            if not items:
                p = Promise()
                return p.fulfill(None)
            promises = []
            for path, pocs in items:
                promises.append(self._do_handle_pocs(path, pocs, shelve))
            return async_all(promises, fulfill_with_none=True)

        pocs_info = self.shelve.get("pocs_info")
        return handle_items(pocs_info) \
            .then(shelve.commit, shelve.rollback)

    def _do_handle_pocs(self, scl_path, scl_info, shelve):
        """
        :param scl_path:    str
        :param scl_info:    dict of [str, str]
        :param shelve:      Shelve
        :return:            Promise
        """
        self.logger.debug("_do_handle_pocs: %s", scl_path)

        p = Promise()
        return p.fulfill(True)


    def _update_online_status(self, status):
        """ Checks if any known poc is listed as onlineStatus
        """

        self.logger.debug("_update_online_status: status: %s %s ", status, type(status))

        promise = Promise()

        if status.statusCode == STATUS_OK:
            return promise.fulfill(status)
        else:
            return promise.reject(status)

    def _update_scl(self, scl_path, scl):
        """
        :param scl_path:    str
        :param scl:
        :return:            Promise
        """
        p = Promise()

        def go(shelve):
            return self._do_update_scl(scl_path, scl, shelve) \
                .then(shelve.commit, shelve.rollback)

        resources = self.shelve.get("resources")
        if resources is not None:
            return go(resources)
        else:
            return p.fulfill(None)

    def _do_update_scl(self, scl_path, scl, shelve):
        """
        :param scl_path:        str
        :param scl
        :param shelve:          GEventSQLShelve
        :return:                Promise
        """
        p = Promise()

        if shelve is not None:
            shelve.setitem(scl_path, scl)
            return p.fulfill(shelve)
        return p.reject(None)


    def _handle_created(self, instance, req_ind):
        """
        #example:
        instance:M2mPoc(path='/m2m/scls/gscl/m2mPocs/m2mPocnRIjsAAZmqm1U49j', name='m2mPocnRIjsAAZmqm1U49j')
        req_ind:RequestIndication: {
            path: /m2m/scls/gscl/m2mPocs,
            method: create,
            typename: m2mPoc,
            resource: {
                'creationTime': datetime.datetime(2014, 7, 11, 13, 37, 40, 385438,
                    tzinfo=<openmtc.util.Utc object at 0x7f4d9bf68e50>),
                'expirationTime': datetime.datetime(2014, 7, 11, 13, 43, 40,
                    tzinfo=<FixedOffset '+00:00'>),
                'onlineStatus': 'ONLINE',
                'contactInfo': 'http://[2001:638:806:65:f4bf:ccb0:cad5:a203]:5000',
                'lastModifiedTime': datetime.datetime(2014, 7, 11, 13, 37, 40, 385438,
                    tzinfo=<openmtc.util.Utc object at 0x7f4d9bf68e50>)
            }
        }
        """

        self.logger.debug("_handle_created: instance:%s req_ind:%s", instance, req_ind)

        resource = req_ind.resource
        poc_path = instance.path
        scl_path = req_ind.path[:-8]
        online_status = resource['onlineStatus']

        if self.pocs_info.get(scl_path) is None:

            self.pocs_info[scl_path] = {
                'onlineStatus': online_status
            }
            self.pocs_info[scl_path][poc_path] = {
                'onlineStatus': online_status
            }
        else:
            self.pocs_info[scl_path][poc_path] = { 'onlineStatus': online_status }
            has_offline = False
            has_online = False
            for key, value in self.pocs_info.get(scl_path).items():
                if key != 'onlineStatus':
                    if value['onlineStatus'] == 'ONLINE':
                        has_online = True
                    elif value['onlineStatus'] == 'OFFLINE':
                        has_offline = True
            if has_online:
                self.pocs_info[scl_path]['onlineStatus'] = "ONLINE"
            elif has_offline:
                self.pocs_info[scl_path]['onlineStatus'] = "OFFLINE"
            else:
                self.pocs_info[scl_path]['onlineStatus'] = "NOT_REACHABLE"

        self.logger.debug("_handle_created: self.pocs_info: %s", self.pocs_info)

        onlinestatus_path = scl_path + "/onlineStatus"
        online_status = {"onlineStatus": self.pocs_info[scl_path]['onlineStatus']}
        rq = UpdateRequestIndication(onlinestatus_path, resource=online_status, typename="scl")
        rq.internal = True

        serverCapability_path = scl_path + "/serverCapability"
        serverCapability = {"serverCapability": True}
        rq2 = UpdateRequestIndication(serverCapability_path, resource=serverCapability, typename="scl")
        rq2.internal = True

        promises = [self._update_scl(scl_path, self.pocs_info[scl_path]), self.api.handle_request_indication(rq), \
            self.api.handle_request_indication(rq2)]
        return async_all(promises, fulfill_with_none=True)

    def _handle_deleted(self, instance, req_ind):

        poc_path = instance.path
        scl_path = poc_path.rpartition('/')[0].rpartition('/')[0]

        self.logger.debug("_handle_deleted: instance: %s %s", poc_path, scl_path)

        promises = []

        del(self.pocs_info[scl_path][poc_path])     #delete m2mpoc from list
        if len(self.pocs_info[scl_path]) <= 1:      #check if the scl has more pocs
            del(self.pocs_info[scl_path])           #delete scl from the list

            onlinestatus_path = scl_path + "/onlineStatus"
            online_status = {"onlineStatus": "OFFLINE"}
            rq = UpdateRequestIndication(onlinestatus_path, resource=online_status, typename="scl")
            rq.internal = True

            serverCapability_path = scl_path + "/serverCapability"
            serverCapability = {"serverCapability": "FALSE"}
            rq2 = UpdateRequestIndication(serverCapability_path, resource=serverCapability, typename="scl")
            rq2.internal = True
            promises = [self.api.handle_request_indication(rq), self.api.handle_request_indication(rq2)]

        promises.append(self._update_scl(scl_path, self.pocs_info[scl_path]))

        return async_all(promises, fulfill_with_none=True)




    def _handle_updated(self, instance, req_ind):
        """
        #example:
        instance:M2mPoc(path='/m2m/scls/gscl/m2mPocs/m2mPoc1qvr4rUOGJAKEPFK', name='m2mPoc1qvr4rUOGJAKEPFK')
        req_ind:RequestIndication: {
            path: /m2m/scls/gscl/m2mPocs/m2mPoc1qvr4rUOGJAKEPFK,
            method: update,
            typename: m2mPoc,
            resource: {
                'expirationTime': '2014-07-11T17:05:09.004744+00:00',
                'contactInfo': 'https://[2001:638:806:65:f4bf:ccb0:cad5:a203]:6000',
                'onlineStatus': 'ONLINE'
            }
        }
        """
        self.logger.debug("_handle_updated: instance:%s req_ind:%s", instance, req_ind)

        resource = req_ind.resource
        poc_path = instance.path
        scl_path = poc_path.rpartition('/')[0].rpartition('/')[0]

        online_status = resource['onlineStatus']
        self.logger.debug("_handle_updated: pocs_info:%s", self.pocs_info)

        self.pocs_info[scl_path][poc_path] = { 'onlineStatus': online_status }
        has_offline = False
        has_online = False
        for key, value in self.pocs_info.get(scl_path).items():
            if key != 'onlineStatus':
                if value['onlineStatus'] == 'ONLINE':
                    has_online = True
                elif value['onlineStatus'] == 'OFFLINE':
                    has_offline = True
        if has_online:
            self.pocs_info[scl_path]['onlineStatus'] = "ONLINE"
        elif has_offline:
            self.pocs_info[scl_path]['onlineStatus'] = "OFFLINE"
        else:
            self.pocs_info[scl_path]['onlineStatus'] = "NOT_REACHABLE"

        onlinestatus_path = scl_path + "/onlineStatus"
        online_status = {"onlineStatus": self.pocs_info[scl_path]['onlineStatus']}

        rq = UpdateRequestIndication(onlinestatus_path, resource=online_status, typename="scl")
        rq.internal = True
        promises = [self._update_scl(scl_path, self.pocs_info[scl_path]), self.api.handle_request_indication(rq)]
        return async_all(promises, fulfill_with_none=True)

        #return self.api.handle_request_indication(rq) \
        #    .then(self._update_online_status)



from urlparse import urlparse

from aplus import Promise
from openmtc_etsi.exc import SCLMethodNotAllowed
from openmtc.response import NotifyResponseConfirmation
from openmtc.scl import NotifyRequestIndication
from openmtc.serializer import get_serializer
from openmtc_server.Plugin import Plugin
from openmtc_scl.methoddomain import aggregate_data


class NotifyAggregator(Plugin):
    """This plugin catches notifies that are supposed to be aggregated.
    The plugin will collect those notifies and then send them together as a NotifyCollection."""

    def __init__(self, api, config, *args, **kw):
        super(NotifyAggregator, self).__init__(api, config, *args, **kw)

        # register on "aggregate:///*"
        self.api.register_transport_client(("aggregate", ),
                                           self.handle_aggregation)

    def handle_aggregation(self, request_indication):
        """Handles aggregation for request_indications where path starts with aggregate:///"""

        p = Promise()

        # check if really notify
        if request_indication.method != "notify":
            return p.reject(SCLMethodNotAllowed(request_indication.method))

        path = urlparse(request_indication.path).path[1:]

        self.logger.debug("aggregating for path: %s", path)

        # missing content_type signals me unparsed resource, so parse it
        ct = request_indication.content_type
        if ct:
            serializer = get_serializer(ct)

            typename, resource = serializer.decode(request_indication.resource)
            self.logger.debug("decoded resource: %s - %s", resource, typename)

            data = resource
            data["requestingEntity"] = request_indication.requestingEntity

        else:
            data = request_indication.resource
            data["requestingEntity"] = request_indication.requestingEntity

        self.logger.debug("Set requestingEntity to %s", request_indication.requestingEntity)

        # TODO: use dict.get()
        # check if there's a running aggregation for the path already
        # if so, just add the notify and promise to the maps
        if path in aggregate_data.ncolmap and len(aggregate_data.ncolmap[path]) > 0:
            aggregate_data.ncolmap[path].append(data)
            aggregate_data.ncolpromises[path].append(p)
            self.logger.debug("added notification to database, size: %s",
                              len(aggregate_data.ncolmap[path]))

        # otherwise, start a timer and create ney keys in the maps
        else:
            self.logger.debug("no pending notifies for %s", path)
            aggregate_data.ncolmap[path] = [data]
            aggregate_data.ncolpromises[path] = [p]
            try:
                dtol = aggregate_data.ncoldelaytolerance[path]
            except KeyError:
                # FIXME (ren) put default delay tolerance somewhere
                dtol = 10

            # to be fired after delaytolerance timer is over
            def dtol_handler():
                self.logger.debug("dtol_handler FIRING")

                payload = list(aggregate_data.ncolmap[path])

                promises = list(aggregate_data.ncolpromises[path])

                # remove path from maps
                aggregate_data.ncolmap.pop(path, None)
                aggregate_data.ncolpromises.pop(path, None)

                # FIXME (ren): from log: "Specifying typename is deprecated"
                notify_req_ind = NotifyRequestIndication(path,
                                                         {"notify": payload},
                                                         typename="notifyCollection")

                self.logger.debug("dtol_handler sends collection: %s", payload)

                def finished(response):
                    # fulfill each pending promise of the original notifies
                    result = NotifyResponseConfirmation()
                    for pending_p in promises:
                        pending_p.fulfill(result)

                    self.logger.debug("confirmed %s notifications for: %s", len(promises), path)

                return self.api.send_request_indication(notify_req_ind).then(finished)

            self.logger.debug("starting dtol_handler, countdown: %s seconds", dtol)
            self.api.set_timer(dtol, dtol_handler)

        return p

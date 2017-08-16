from collections import namedtuple
from urlparse import urlparse
from aplus import Promise
from openmtc_etsi.scl import (RetrieveRequestIndication,
                              NotifyRequestIndication, DeleteRequestIndication)
from openmtc_server.Plugin import Plugin
from openmtc_etsi.model import (SubscribableResource, Notify, Subscription,
                                FilterCriteria)
from openmtc_etsi.response import ErrorResponseConfirmation, get_status_message
from openmtc_etsi.exc import (STATUS_NOT_FOUND, STATUS_PERMISSION_DENIED,
                              STATUS_DELETED, STATUS_EXPIRED,
                              STATUS_BAD_GATEWAY)
from copy import copy

SubscriptionTuple = namedtuple('SubscriptionTuple', ['path', 'owner',
                                                     'contact', 'active',
                                                     'filterCriteria'])


class NotificationHandler(Plugin):
    # serializer

    def __init__(self, api, config, *args, **kw):
        super(NotificationHandler, self).__init__(api=api, config=config,
                                                  *args, **kw)
        # subscriptions info like owner and timestamp
        self._subscriptions = {}
        # TODO : move to shelve usage!
        self._last_sent = {}
        self._next_last_sent = {}
        self._timers = {}
        self._pending_operations = {}

    def _get_subscriptions_shelve(self):
        return self.get_shelve("subscriptions")

    def _get_last_sent_shelve(self):
        return self.get_shelve("last_sent")

    def _init(self):
        # subscribable resource updated
        self.events.resource_updated.register_handler(
            self._handle_subscribable_resource_updated, SubscribableResource)
        # subscription created
        self.events.resource_created.register_handler(
            self._handle_subscription_created, Subscription)
        # subscription deleted
        self.events.resource_deleted.register_handler(
            self._handle_subscription_deleted, Subscription)

        self._initialized()

    def _stop(self):
        for t in self._timers.values():
            self.api.cancel_timer(t)
        self._stopped()

    def _push_op(self, op, sub_path):

        def wait_for_same_resource(path):
            p = Promise()
            try:
                self._pending_operations[path].append(p)
            except KeyError:
                self._pending_operations[path] = [p]
                p.fulfill(path)
            return p

        def unwait_for_same_resource(path):
            self._pending_operations[path].pop(0)
            try:
                self._pending_operations[path][0].fulfill(path)
            except IndexError:
                del self._pending_operations[path]

        wait_for_same_resource(sub_path).then(
            lambda x: op(sub_path)).then(
            lambda x: unwait_for_same_resource(sub_path))

    def _handle_subscribable_resource_updated(self, resource, req_ind):
        self.logger.debug("_handle_subscribable_resource_updated for %s",
                          req_ind.path)

        self._notify(resource.path, resource.lastModifiedTime)

    def _handle_subscription_created(self, subscription, req_ind):
        self._subscriptions[subscription.path] = SubscriptionTuple(
            path=subscription.path,
            owner=req_ind.requestingEntity,
            contact=subscription.contact,
            active=True,
            filterCriteria=subscription.filterCriteria
        )

        self._initial_notify(subscription)

    def _cancel_timer(self, subscription_path):
        try:
            self.api.cancel_timer(self._timers.pop(subscription_path))
        except KeyError:
            pass

    def _handle_subscription_deleted(self, subscription, req_ind):
        self.logger.debug("_handle_subscription_deleted")

        sub = self._subscriptions.pop(req_ind.path)
        self._last_sent.pop(req_ind.path, None)
        self._next_last_sent.pop(req_ind.path, None)

        self._cancel_timer(req_ind.path)
        self._error_notify(req_ind, sub)

    def _error_notify(self, req_ind, sub):

        if req_ind.cascading:
            error_notify = _get_error_notify(_DELETED, sub.path)
        elif req_ind.expired:
            error_notify = _get_error_notify(_EXPIRED, sub.path)
        elif req_ind.read_access_lost:
            error_notify = _get_error_notify(_PERMISSION_DENIED, sub.path)
        else:
            return

        op = lambda x: self._send_notify(sub.contact, error_notify)
        self._push_op(op, sub.path)

    def _initial_notify(self, subscription):
        res_path = subscription.parent_path.rpartition("/")[0]
        self.logger.debug("Handling initial notify for %s (%s)", res_path,
                          subscription.parent_path)
        self._last_sent[subscription.path] = None
        self._next_last_sent[subscription.path] = subscription.lastModifiedTime

        op = lambda x: self._handle_subscription(subscription, res_path, True)
        self._push_op(op, subscription.path)

    def _handle_error(self, error):
        self.logger.error("Error occurred: %s", error)

    def _notify(self, res_path, res_last_mod_time):
        """
        @rtype : None
        @param res_path:
        @return:
        """

        subs_path = res_path + "/subscriptions"

        subs = filter(lambda x: x.path.startswith(subs_path) and
                      self._subscriptions[x.path].active,
                      self._subscriptions.values())

        for sub in subs:
            self._next_last_sent[sub.path] = res_last_mod_time
            op = lambda x: self._handle_subscription(sub, res_path)
            self._push_op(op, sub.path)

    def _handle_subscription(self, subscription, res_path, initial=False):
        """
        @rtype : None
        @param subscription:
        @param res_path:
        @return:
        """

        sub_path = subscription.path

        self.logger.debug("handling subscription: %s -> %s", sub_path,
                          subscription.contact)

        self._cancel_timer(sub_path)

        def create_notify(res_con):
            self._last_sent[sub_path] = self._next_last_sent[sub_path]
            self._next_last_sent[sub_path] = None
            notify = Notify(statusCode=res_con.status,
                            representation={},
                            subscriptionReference=sub_path)

            # raise Exception(notify.statusCode, res_con.status,
            #                 res_con.statusCode)

            try:
                result = res_con.resource
            except AttributeError:
                pass
            else:
                try:
                    if not result.contentInstanceCollection:
                        self.logger.debug("contentInstanceCollection is empty,"
                                          " not sending notify.")
                        # Don't send empty notifications
                        return
                    self.logger.debug("contentInstanceCollection is not empty,"
                                      " sending notify.")
                except AttributeError:
                    self.logger.debug("not a contentInstances object, sending "
                                      "notify.")

                if res_con.content_type:
                    notify.representation = {
                        "$t": result, "contentType": res_con.content_type
                    }
                else:
                    notify.representation = {"$t": result}

            def handle_error(error):
                self.logger.error("Failed to deliver notification to %s: %s",
                                  subscription.contact, error)
                if (isinstance(error, ErrorResponseConfirmation) and
                        error.statusCode == STATUS_BAD_GATEWAY):
                    self.logger.debug("Scheduling retry in 30s.")

                    def re_do():
                        self._handle_subscription(subscription, res_path)

                    self._timers[sub_path] = self.api.set_timer(30, re_do)
                else:
                    raise error

            return self._send_notify(subscription.contact, notify).then(
                None, handle_error)

        def handle_retrieve_error(error):
            self._next_last_sent[sub_path] = None
            assert isinstance(error, ErrorResponseConfirmation)
            try:
                if error.statusCode not in (
                        STATUS_NOT_FOUND, STATUS_PERMISSION_DENIED):
                    raise error
            except AttributeError:
                raise error

            # TS 102.921 10.39.6 last paragraph:
            # If at the time of subscription, a partial retrieve with the same
            # filterCriteria would result in an error response because of any of
            # the specific errors mentioned in clause 10.39.3, the creation of
            # the subscription shall be accepted, but the subscription is
            # immediately terminated, and a notify containing the error
            # response indicated in the partial retrieve(clause 10.39.3) is
            # returned in the notify. Similar, if in the subscribed-to resource
            # is modified in such a way that a partial retrieve with the
            # attributeAccessor as specified in the filterCriteria would return
            # an error, a final notify is send as specified in clause 10.25.7.3
            # and the subscription is terminated.
            try:
                self._subscriptions[sub_path] = self._subscriptions[
                    sub_path]._replace(active=False)
            except KeyError:
                return
            if initial:
                del_req_ind = DeleteRequestIndication(sub_path)
                self.api.handle_request_indication(del_req_ind)
                return self._send_notify(subscription.contact,
                                         _get_error_notify(error,
                                                           subscription.path))

            # delete the subscription
            del_req_ind = DeleteRequestIndication(sub_path,
                                                  reason="read_access_lost")
            return self.api.handle_request_indication(del_req_ind)

        try:
            req_ent = self._subscriptions[sub_path].owner
        except KeyError:
            req_ent = None

        fc = subscription.filterCriteria or FilterCriteria()

        if res_path.endswith("/contentInstances"):
            try:
                last_sent = self._last_sent[sub_path]
            except KeyError:
                pass
            else:
                try:
                    created_after = fc.createdAfter
                except AttributeError:
                    created_after = fc.get("createdAfter")

                if not created_after:
                    created_after = last_sent
                else:
                    self.logger.debug("Comparing %s <-> %s", created_after,
                                      last_sent)
                    if created_after < last_sent:
                        created_after = last_sent

                fc = copy(fc)
                fc.createdAfter = created_after

        req_ind = RetrieveRequestIndication(res_path, filterCriteria=fc,
                                            requestingEntity=req_ent)
        return self.api.handle_request_indication(req_ind) \
            .then(create_notify, handle_retrieve_error) \
            .then(None, self._handle_error)

    def _send_notify(self, contact, notify):
        req_ind = NotifyRequestIndication(
            path=contact,
            resource=notify
        )

        if urlparse(contact).scheme:
            self.logger.debug("Sending notify requestIndication")
            return self.api.send_request_indication(req_ind)
        else:
            self.logger.debug("Handling notify requestIndication")
            return self.api.handle_request_indication(req_ind)

NotifyError = namedtuple('NotifyError', ['statusCode', 'errorInfo'])
_DELETED = NotifyError(STATUS_DELETED, 'Resource was deleted.')
_PERMISSION_DENIED = NotifyError(STATUS_PERMISSION_DENIED,
                                 'Read Access is lost.')
_EXPIRED = NotifyError(STATUS_EXPIRED, 'Subscription has expired.')


def _get_error_notify(error, sub_path):
    status = get_status_message(error.statusCode)

    error_info = ErrorResponseConfirmation(error.statusCode, "notify",
                                           error.errorInfo)

    return Notify(statusCode=status,
                  representation={'$t': error_info},
                  subscriptionReference=sub_path)

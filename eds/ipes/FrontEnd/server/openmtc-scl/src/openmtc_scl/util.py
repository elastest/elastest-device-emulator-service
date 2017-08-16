# this is currently a copy of the util.py file from the openmtc directory.
# needs to be rewritten

import time

from futile.logging import LoggerMixin
from openmtc.util import datetime_the_future


class ExpTimeUpdater(LoggerMixin):
    """ Utility class to update mtc resources' expirationTime periodically.
    """

    def __init__(self, api, send_update, interval=None, offset=None,
                 *args, **kw):
        """
            @param api: the api
            @param send_update: send_update function for update requests
            @param interval: refresh interval in seconds
            @param offset: additional offset for expirationTime in seconds
        """
        super(ExpTimeUpdater, self).__init__(*args, **kw)
        self.__interval = interval or 60 * 60
        self.__offset = offset or 60 * 60
        self.__timers = {}
        self.api = api
        self.send_update = send_update
        self.__shutdown = None
        self.logger.debug("creating ExpTimeUpdater with interval: %s",
                          interval)

    # taken from openmtc_app
    def start(self, instance, fields=None):
        """ Starts a Timer chain,
            to repeatedly update a resource instances's expirationTime.

            @param instance: resource instance
        """
        self.logger.debug("starting expTimeUpdater: %s %s" % (instance, fields))
        self.__shutdown = False
        interval = (time.mktime(instance.expirationTime.timetuple()) -
                    (time.time() + time.timezone))
        if interval > self.__offset:
            interval = interval - self.__offset
        else:
            interval -= interval / 10

        # t = Timer(interval, self.__updateExpTime,
        #           kwargs = { "instance": instance, "fields": fields})
        # t.start()
        t = self.api.set_timer(interval,
                               lambda: self.__updateExpTime(instance,
                                                            fields=fields))

        self.__timers[instance.path] = t

    def __updateExpTime(self, instance, future=None, fields=[]):
        """ Updates a resource instance's expirationTime to future.

            @note: Starts a new Timer.
            @param instance: resource instance to update
            @param future: new expirationTime value (optional)
        """
        self.logger.debug("__updateExpTime: %s" % instance)
        if self.__shutdown:
            return

        interval = self.__interval
        offset = self.__offset
        if not future:
            future = datetime_the_future(interval + offset)
        fields.append("expirationTime")
        instance.expirationTime = future
        self.send_update(instance, fields)
        # NOTE: expirationTime might have been changed by SCL at this point.
        # update could/should return the updated instance in this case,
        #   but does it?
        # => additional GET to confirm expirationTime ?

        # t = Timer(interval, self.__updateExpTime,
        #           kwargs = { "instance": instance, "fields": fields})
        # t.start()
        t = self.api.set_timer(interval,
                               lambda: self.__updateExpTime(instance,
                                                            fields=fields))
        del self.__timers[instance.path]
        self.__timers[instance.path] = t
        # hopefully, GC will delete the old timer

    def stop(self):
        self.__shutdown = True
        self.logger.debug("Killing timers: %s", self.__timers)
        for t in self.__timers.values():
            self.api.cancel_timer(t)
            # t.cancel()

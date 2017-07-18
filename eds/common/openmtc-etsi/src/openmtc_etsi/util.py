from futile.logging import LoggerMixin
from threading import Timer
import time
from openmtc.util import datetime_the_future
from openmtc_etsi.exc import SCLNotFound


class ExpTimeUpdater(LoggerMixin):
    """ Utility class to update mtc resources' expirationTime periodically.
        Based on python Timers.
    """

    def __init__(self, send_update, interval=None, offset=None, *args, **kw):
        """
            @param send_update: send_update function for update requests
            @param interval: refresh interval in seconds
            @param offset: additional offset for expirationTime in seconds
        """
        super(ExpTimeUpdater, self).__init__(*args, **kw)
        self.__interval = interval or 60 * 60
        self.__offset = offset or 60 * 60
        self.__timers = {}
        self.send_update = send_update

# taken from openmtc_app
    def start(self, instance, fields=None, restore=None):
        """ Starts a threading.Timer chain,
            to repeatedly update a resource instances's expirationTime.

            @param instance: resource instance
            @param fields: additional fields mandatory during update
            @param restore: function that will restore the instance, if it has expired accidentally. Has to restart the refresher.
        """
        self.logger.debug("starting expTimeUpdater: %s %s" % (instance,
                                                              fields))
        self.__shutdown = False
        interval = time.mktime(instance.expirationTime.timetuple()) -(time.time() + time.timezone)
        if interval > self.__offset:
            interval = interval - self.__offset
        else:
            interval = interval - (interval/10)
        kwargs = {"instance": instance, "fields": fields, "restore": restore}
        t = Timer(interval, self.__updateExpTime, kwargs=kwargs)
        t.start()
        self.__timers[instance.path] = t

    def __updateExpTime(self, instance, future=None, fields=[], restore=None):
        """ Updates a resource instance's expirationTime to future.

            @note: Starts a new Timer.
            @param instance: resource instance to update
            @param future: new expirationTime value (optional)
            @param fields: additional fields mandatory during update
            @param restore: function that will restore the instance, if it has expired accidentally. Has to restart the refresher.
        """
        self.logger.debug("__updateExpTime: %s" %(instance))
        if self.__shutdown:
            return

        interval = self.__interval
        offset = self.__offset
        if not future:
            future = datetime_the_future(interval + offset)
        fields.append("expirationTime")
        instance.expirationTime = future
        try:
            self.mapper.update(instance, fields)
        except SCLNotFound as e:
            self.logger.warn("ExpirationTime update failed: %s", e)
            # subscription disappeared?
            # missed the expirationTime?
            # mb sync issue?; mb congestion?
            if restore:
                restore(instance)
                return
            else:
                raise
        # NOTE: expirationTime might have been changed by SCL at this point.
        # update could/should return the updated instance in this case, but does it?
        # => additional GET to confirm expirationTime ?
        kwargs = {"instance": instance, "fields": fields, "restore": restore}
        t = Timer(interval, self.__updateExpTime, kwargs=kwargs)
        t.start()
        self.__timers[instance.path] = t
        # hopefully, GC will delete the old timer

    def stop(self):
        self.__shutdown = True
        self.logger.debug("Killing timers: %s", self.__timers)
        for t in self.__timers.values():
            t.cancel()

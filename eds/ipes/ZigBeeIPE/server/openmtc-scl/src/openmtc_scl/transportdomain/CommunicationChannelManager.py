from datetime import datetime

import openmtc_scl.api
from futile.logging import LoggerMixin
from openmtc_etsi.model import safPolicySet, m2mSpPolicy, anpPolicy, \
    rcatParamList, MgmtObj
from .util import match_now_cron


class CommunicationChannelManager(LoggerMixin):
    """This class handles different Communication Channels used by the Store and Forward functionnality"""
    # This is a temporary function, it should be set somewhere else (DM ? Config ?)
    # TODO: Note that it will be needed to create them in the ressource tree
    def load_policies(self, config):
        """Function loading policies from the configuration file"""
        self._etsiSclMo = MgmtObj()
        self._etsiSclMo.safPolicySetCollection = []

        for __safPolicySet in config["etsiSclMo"]["safPolicySetCollection"]:
            _safPolicySet = safPolicySet(__safPolicySet["policyScope"][0])
            _safPolicySet.policyScope = __safPolicySet["policyScope"]
            _safPolicySet.anpPolicyCollection = []

            _safPolicySet.m2mSpPolicy = m2mSpPolicy()
            _safPolicySet.m2mSpPolicy.defaultRcatValue = __safPolicySet["m2mSpPolicy"]["defaultRcatValue"]
            _safPolicySet.m2mSpPolicy.rcatParamListCollection = []

            self._etsiSclMo.safPolicySetCollection.append(_safPolicySet)

            for __rcatParamList in __safPolicySet["m2mSpPolicy"]["rcatParamListCollection"]:
                _rcatParamList = rcatParamList(str(__rcatParamList["rcatValue"]))
                _rcatParamList.rcatValue = __rcatParamList["rcatValue"]
                _rcatParamList.anSelList = __rcatParamList["anSelList"]
                _rcatParamList.maxPendReq = __rcatParamList["maxPendReq"]
                _rcatParamList.maxPendData = __rcatParamList["maxPendData"]
                _safPolicySet.m2mSpPolicy.rcatParamListCollection.append(_rcatParamList)

    def __init__(self, *args, **kw):
        super(CommunicationChannelManager, self).__init__(*args, **kw)
        try:
            self.load_policies(openmtc_scl.api.config)
            self.logger.debug("SAF policies loaded")
        except Exception as e:
            self.logger.warn("Failed to load SAF policies: %s", e)
        self.listeners = {}
        self.current_channel = None

    def get_rcatParamList(self, rcat):
        """Return the policies list for a specific rcat.

        This includes default rcat Value, preferred network list, maximum pending requests and data.

        :param rcat: Tested rcat
        :type rcat: int
        :return: Rcat policy list
        :rtype: rcatParamList
        """
        return self._get_safPolicySet().m2mSpPolicy.rcatParamListCollection[rcat]

    def _get_safPolicySet(self):
        """Returns the policy set currently used.

        :return: Default policy set
        :rtype: safPolicySet
        """
        for _safPolicySet in self._etsiSclMo.safPolicySetCollection:
            for scope in _safPolicySet.policyScope:
                # TODO: add check for APP-id in combinaison to "default" (Scope can be set to a specific app)
                if scope == "default":
                    return _safPolicySet

    def _get_current_rcat(self, channel):
        """Provides the supported rcat for a channel, depending on the current datetime.

        :param channel: Tested channel
        :type channel: anpPolicy
        :return: rcat value from 0 to 8 (no supported rcat)
        :rtype: int
        """
        if not channel:
            return 8
        for cron in channel.rcatSchedule.keys():
            if match_now_cron(cron):
                return channel.rcatSchedule[cron]
        # Channel is not usable at this time
        return 8

    def get_channel(self, rcat, trpdt, send_pending_requests):
        """Retrives an existing channel corresponding to the request Category.

        If the request has to be handled urgently, try to establish a connection.

        :param rcat: Required request category
        :param trpdt: Tolerable Request Processing Delay Time, used to estimate the urgency of a request
        :param send_pending_requests: Callback function used to send requests when a channel gets ready
        :type rcat: int
        :type trpdt: float or datetime
        :type send_pending_requests: function
        :return: Available channel or None
        :rtype: anpPolicy or None
        """
        self.logger.debug("Get channel")
        if self._get_current_rcat(self.current_channel) <= rcat:
            return self.current_channel

        # The current channel isn't suitable, sets up a callback for when a new channel will be ready
        self.add_listener(send_pending_requests, rcat)

        _safPolicySet = self._get_safPolicySet()
        if rcat is None:
            rcat = _safPolicySet.m2mSpPolicy.defaultRcatValue

        # TODO: Make some checks with anSelList to find if we can use a preferred network
        for channel in _safPolicySet.anpPolicyCollection:
            c_rcat = self._get_current_rcat(channel)
            if c_rcat <= rcat:
                # We should re-establish a connection to the ssid channel.anName
                self.add_listener(send_pending_requests, rcat)
                self.establish_connection(rcat, channel.anName)
                return None

        if trpdt == 0.0 or type(trpdt) is datetime and trpdt <= datetime.now():
            self.establish_connection(rcat)
        return None

    def add_listener(self, cb, rcat):
        """Adds a call back function to be notified when a new channel corresponding to a Category is created.

        :param cb: Callback function used to send requests when a channel gets ready
        :param rcat: Required request category
        :type cb: function
        :type rcat: int
        """
        self.logger.debug("Adding a listener on rcat %d" % rcat)
        self.listeners[rcat] = cb

    def register_connectivity_handler(self, process_connectivity_request):
        """Allows connectivity services to register a callback when a connection needs to be established.

        :param process_connectivity_request: Callback function registered
        :type process_connectivity_request: function
        """
        self.process_connectivity_request = process_connectivity_request

    def create_channel(self, name, rcat_schedule):
        """Creates a new channel with name and supported category over time.

        Adds the channel to the list of available channels, and notifies the interested parties.

        :param name: Name of the created channel
        :param rcat_schedule: Supported category over time, formated as {crontab: rcat} or \
        int, in case a single rcat is handled all the time
        :type name: str
        :type rcat_schedule: dict or int
        :return: Created channel
        :rtype: anpPolicy
        """
        self.logger.debug("Creating channel %s with rcat %s" % (name, rcat_schedule))

        if type(rcat_schedule) is int:
            rcat_schedule = {'* * * * *': rcat_schedule}

        channel = anpPolicy(anName=name, rcatSchedule=rcat_schedule)
        _safPolicySet = self._get_safPolicySet()

        if channel not in _safPolicySet.anpPolicyCollection:
            _safPolicySet.anpPolicyCollection.append(channel)
        self.current_channel = channel
        self.notify_all(self._get_current_rcat(channel), channel)

        return channel

    def delete_channel(self, name):
        """Remove a channel corresponding to a specific name.

        :param name: Name of the channel
        :type name: str
        :return: True if removal was a success, False otherwise
        :rtype: bool
        """
        _safPolicySet = self._get_safPolicySet()
        for channel in _safPolicySet.anpPolicyCollection:
            if channel.anName == name:
                del channel
                return True
        return False

    def notify_all(self, rcat, channel):
        """Notifies every interested party about the creation of a new channel.

        :param rcat: Supported request category
        :param channel: Newly created channel
        :type rcat: int
        :type channel: anpPolicy
        """
        for i in range(8, rcat, -1):
            i = i - 1
            if i in self.listeners:
                callback = self.listeners[i]
                del self.listeners[i]
                callback(channel, i)

    def notify_failure(self, rcat):
        """Notifies the connection triggerer that no channel could be established.

        This is only triggered when a trpdt has reached 0, thus the requests need to be removed from buffers.

        :param rcat: Request category
        :type rcat: int
        """
        if rcat in self.listeners:
            cb = self.listeners[rcat]
            cb(None, rcat)

    def establish_connection(self, rcat, ssid=None):
        """Interfaces with connectivity services in establishing a new connection to a specfic device.

        :param rcat: Required request category
        :param ssid: Explicit targeted ssid
        :type rcat: int
        :type ssid: str
        """
        # Check connectivity service
        self.logger.debug("Establishing connect")
        # Second argument could be a channel name
        p = self.process_connectivity_request(rcat)

        def connection_success(t=("default", 0)):
            """Connection is a success, we create a new channel.

            :param t: Tuple containing channel name and Supported category over time, formated as {crontab: rcat} or \
            int, in case a single rcat is handled all the time
            :type t: tuple
            """
            self.logger.debug("Connec success")
            if type(t[0]) is str:
                name = t[0]
            else:
                # Netlink provides the channel using Interface namedtuple
                name = t[0].name
            rcat_schedule = t[1]
            self.create_channel(name, rcat_schedule)

        def connection_failure(*args):
            self.notify_failure(rcat)
        p.then(connection_success, connection_failure)
        #Tests:
        """
        from time import sleep
        sleep(3)
        connection_success()
        """

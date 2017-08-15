__author__ = 'ren'

import netifaces
import Queue
import json
from collections import namedtuple
from select import select

from pyroute2 import IPRSocket

from openmtc_server.Plugin import Plugin
from aplus import Promise

from openmtc_server.exc import InterfaceNotFoundException

Interface = namedtuple("Interface", ("name", "addresses", "hwaddress"))
Address = namedtuple("Address", ("address", "family"))


class NetLinkListener(Plugin):
    """This plugin reads kernel messages and is able to react to certain network events"""
    states = {"UP": True, "DOWN": False}

    def __init__(self, api, config, *args, **kw):

        super(NetLinkListener, self).__init__(api, config, *args, **kw)
        self.listen = True
        self.socket = IPRSocket()

    def _init(self, *args, **kw):
        # super(NetLinkListener, self).__init__(*args, **kw)
        self.queue = Queue.Queue()
        self.listen = False

        # add handlers here
        self.event_handlers = {
            "RTM_NEWLINK": self.rtm_newlink_handler,
            "RTM_NEWADDR": self.rtm_newaddr_handler,
            "RTM_DELADDR": self.rtm_deladdr_handler
        }

        self.api.register_connectivity_handler(self.connectivity_request)
        self.logger.debug("Connectivity request handler registered")

        self._initialized()

    def _start(self):
        self.api.run_task(self.start_listening)
        self.api.run_task(self.start_queue_handler)

        self._started()

    def _stop(self):
        self.stop_listening()
        self._stopped()

    def start_listening(self):

        if self.socket is None:
            self.socket = IPRSocket()

        self.socket.bind()

        self.logger.info("Starting listener...")
        self.listen = True
        while self.listen:
            r, _, _ = select((self.socket, ), (), (), 0.5)
            if r:
                msg_array = self.socket.get()
                for event_msg in msg_array:
                    try:
                        self.queue.put(event_msg)
                    except Queue.Full:
                        self.logger.warn("Message queue is full! it has %s elements", self.queue.qsize())

        # stop after listening
        self.socket.close()
        self.logger.debug("Socket closed")

    def start_queue_handler(self):
        """Start reading the queue in a while loop until plugin stops listening to kernel messages"""

        self.logger.debug("Starting queue handler...")
        while self.listen or not self.queue.empty():
            try:
                self.handle_event(self.queue.get(timeout=0.5))
            except Queue.Empty:
                pass
        self.logger.debug("Queue handler finished")

    def stop_listening(self):
        """Stop listening to kernel messages -> shuts down queue handler"""
        self.logger.info("Stopping listener...")
        self.listen = False

    def handle_event(self, event_msg):
        """Find the handler matching the message event and run the handler with the message

        :param event_msg: event message from kernel message (kernel message is usually an array with 1 event message
        """
        event = event_msg["event"]
        # self.logger.debug("new event:\r\n%s", json.dumps(event_msg, indent=2, sort_keys=True))
        # self.logger.debug("new event: %s", event)

        handler = self.event_handlers.get(event)
        if handler is not None:
            self.logger.info("Handling event: %s", event)
            handler(event_msg)
        else:
            # self.logger.debug("No handler for event: %s", event)
            pass

    def rtm_newlink_handler(self, msg):
        """Handler parsing RTM_NEWLINK event messages

        :param msg: RTM_NEWLINK event message
        """
        name = str()
        state = str()
        for attr in msg["attrs"]:
            if attr[0] == "IFLA_IFNAME":
                name = attr[1]
            elif attr[0] == "IFLA_OPERSTATE":
                state = attr[1]

        if name == str():
            self.logger.debug("No IFLA_IFNAME attribute found. Using index to assume interface")
            name = self.get_interface_name_from_index(msg)

        if name != str() and state != str():
            try:
                interface = self.get_interface(name)
                if self.states[state]:
                    self.api.events.interface_created.fire(interface)
                else:
                    self.api.events.interface_removed.fire(interface)
            except InterfaceNotFoundException:
                self.logger.error(
                    "RTM_NEWLINK: Unable to fire event for interface state change: %s is an unknown interface", name)
                self.logger.debug("Debug print of skipped message:\r\n%s", json.dumps(msg, indent=2, sort_keys=True))
        else:
            self.logger.warn("RTM_NEWLINK: interface not found or unknown state in msg!")
            self.logger.debug("Debug print of skipped message:\r\n%s", json.dumps(msg, indent=2, sort_keys=True))

    def rtm_newaddr_handler(self, msg):
        """Handler parsing RTM_NEWADDR event messages

        :param msg: RTM_NEWADDR event message
        """
        interface = str()
        address = str()
        for attr in msg["attrs"]:
            if attr[0] == "IFA_LABEL":
                interface = attr[1]
            elif attr[0] == "IFA_ADDRESS":
                address = attr[1]

        if interface == str():
            self.logger.debug("No IFA_LABEL attribute found. Using index to assume interface")
            interface = self.get_interface_name_from_index(msg)

        if interface != str() and address != str():
            try:
                self.api.events.address_created.fire(self.get_interface(interface),
                                                     Address(address=address, family=msg["family"]))
            except InterfaceNotFoundException:
                self.logger.error("RTM_NEWADDR: Unable to fire address_created event: %s is an unknown interface",
                                  interface)
                self.logger.debug("Debug print of skipped message:\r\n%s", json.dumps(msg, indent=2, sort_keys=True))
        else:
            self.logger.warn("RTM_NEWADDR: interface and/or address not found in msg!")
            self.logger.debug("Debug print of skipped message:\r\n%s", json.dumps(msg, indent=2, sort_keys=True))

    def rtm_deladdr_handler(self, msg):
        """Handler parsing RTM_DELADDR event messages

        :param msg: RTM_DELADDR event message
        """
        interface = str()
        address = str()
        for attr in msg["attrs"]:
            if attr[0] == "IFA_LABEL":
                interface = attr[1]
            elif attr[0] == "IFA_ADDRESS":
                address = attr[1]

        if interface == str():
            self.logger.debug("No IFA_LABEL attribute found. Using index to assume interface")
            interface = self.get_interface_name_from_index(msg)

        if interface != str() and address != str():
            try:
                self.api.events.address_removed.fire(self.get_interface(interface),
                                                     Address(address=address, family=msg["family"]))
            except InterfaceNotFoundException:
                self.logger.error("RTM_DELADDR: Unable to fire address_removed event: %s is an unknown interface",
                                  interface)
                self.logger.debug("Debug print of skipped message:\r\n%s", json.dumps(msg, indent=2, sort_keys=True))
        else:
            self.logger.warn("RTM_DELADDR: interface and/or address not found in msg!")
            self.logger.debug("Debug print of skipped message:\r\n%s", json.dumps(msg, indent=2, sort_keys=True))

    def get_addresses(self, interface):
        """Get addresses of a given interface

        :param interface: name of interface
        :return: list of addresses
        """
        n_addresses = netifaces.ifaddresses(interface)
        addresses = []
        for family in n_addresses:
            for addr in n_addresses[family]:
                addresses.append(Address(address=addr["addr"], family=family))

        return addresses

    def get_interface(self, name):
        """Returns an Interface object identified by name

        :param name: name of interface
        :return Interface: interface
        :raise UnknownInterface: if interface was not found
        """
        if name not in netifaces.interfaces():
            raise InterfaceNotFoundException("%s was not found" % name)
        else:
            addresses = self.get_addresses(name)
            hwaddress = [addr for addr in addresses if addr[1] == netifaces.AF_LINK][0]
            return Interface(name=name,
                             addresses=addresses,
                             hwaddress=hwaddress)

    def get_interface_name_from_index(self, msg):
        """Parse event message and try to assume interface from index attribute

        :param msg: event message
        :return: interface name corresponding to index value, or empty string if unsuccessful
        """
        interface = str()
        try:
            interface = netifaces.interfaces()[msg["index"] - 1]
            self.logger.debug("Index: %s -> %s", msg["index"], interface)
        except IndexError:
            self.logger.debug("Unable to get interface from index")
        finally:
            return interface

    def connectivity_request(self, rcat=0):
        """Handles connectivity requests"""
        with Promise() as p:
            blacklist = ['lo']
            interfaces = netifaces.interfaces()

            interface = next((x for x in interfaces if (x not in blacklist)), None)

            if interface is None:
                p.reject(InterfaceNotFoundException("No interfaces found matching request"))
            else:
                p.fulfill((self.get_interface(interface), 0))

        return p
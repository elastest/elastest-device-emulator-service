__author__ = 'ren'

import netifaces
from collections import namedtuple

from openmtc_server.Plugin import Plugin
from aplus import Promise
import time

from openmtc_server.exc import InterfaceNotFoundException

Interface = namedtuple("Interface", ("name", "addresses", "hwaddress"))
Address = namedtuple("Address", ("address", "family"))


class NetworkManager(Plugin):
    """This plugin reads out the netifaces python plugin every couple of
    seconds and reacts to changes"""
    states = {"UP": True, "DOWN": False}

    def __init__(self, api, config, *args, **kw):

        super(NetworkManager, self).__init__(api, config, *args, **kw)
        self.polling = True

    def _init(self, *args, **kw):

        self.api.register_connectivity_handler(self.connectivity_request)
        self.logger.debug("Connectivity request handler registered")

        self._initialized()

    def _start(self):
        self.api.run_task(self.start_polling)
        self._started()
        self.logger.debug("networkmanager loaded")

    def _stop(self):
        self.polling = False
        self.logger.debug("removed polling flag")
        self._stopped()

    def get_addresses(self, interface):
        """Get addresses of a given interface

        :param interface: name of interface
        :return: list of addresses
        """
        n_addresses = netifaces.ifaddresses(interface)
        addresses = []
        for family in n_addresses:
            for addr in n_addresses[family]:
                if family == 10:
                    addr["addr"] = self.remove_ipv6_special_stuff(addr["addr"])

                addresses.append(Address(address=addr["addr"], family=family))

        return addresses

    def get_addresses_from_ifaddresses(self, interface, ifaddresses):
        """Get addresses of a given interface

        :param interface: name of interface
        :return: list of addresses
        """
        addresses = []
        for family in ifaddresses:
            for addr in ifaddresses[family]:
                if family == 10:
                    addr["addr"] = self.remove_ipv6_special_stuff(addr["addr"])

                addresses.append(Address(address=addr["addr"], family=family))

        return addresses

    def create_interface(self, name, ifaddresses):
        """Create Interface tuple based on given interfaces addresses. (function independent of netifaces)

        :param name:
        :param ifaddresses:
        :return:
        """
        addresses = self.get_addresses_from_ifaddresses(name, ifaddresses)
        try:
            hwaddress = [addr for addr in addresses
                         if addr[1] == netifaces.AF_LINK][0]

        except IndexError:
            self.logger.warn("No hardware address found for %s!", name)
            hwaddress = None

        return Interface(name=name,
                         addresses=addresses,
                         hwaddress=hwaddress)

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
            hwaddress = [addr for addr in addresses
                         if addr[1] == netifaces.AF_LINK][0]
            return Interface(name=name,
                             addresses=addresses,
                             hwaddress=hwaddress)

    def connectivity_request(self, rcat=0):
        """Handles connectivity requests"""
        with Promise() as p:
            blacklist = ['lo']
            interfaces = netifaces.interfaces()

            interface = next((x for x in interfaces
                              if (x not in blacklist)), None)

            if interface is None:
                p.reject(InterfaceNotFoundException("No interfaces found"
                                                    "matching request"))
            else:
                p.fulfill((self.get_interface(interface), 0))

        return p

    def start_polling(self, timeout=1):
        """Poll netifaces information and check for differences, for as long as self.polling == True.

        :param timeout: Amount of time to wait between polling
        """
        last_interfaces = netifaces.interfaces()
        last_ifaddresses = {}
        for iface in last_interfaces:
            last_ifaddresses[iface] = netifaces.ifaddresses(iface)

        self.logger.debug("polling started")
        while self.polling:
            try:
                cur_interfaces = netifaces.interfaces()
                intersection = set(last_interfaces) ^ set(cur_interfaces)
                if len(intersection) > 0:
                    for isetface in intersection:
                        if isetface in cur_interfaces:
                            # new interface
                            self.logger.debug("Firing %s event for %s", "interface_created", isetface)
                            self.api.events.interface_created.fire(
                                self.create_interface(isetface, netifaces.ifaddresses(isetface)))
                        else:
                            # removed interface
                            self.logger.debug("Firing %s event for %s", "interface_removed", isetface)
                            self.api.events.interface_removed.fire(
                                self.create_interface(isetface, last_ifaddresses[isetface]))

                for iface in cur_interfaces:
                    cur_ifaddresses = netifaces.ifaddresses(iface)
                    if iface in last_ifaddresses and last_ifaddresses[iface] != cur_ifaddresses:
                        self.check_ifaddresses_diff(last_ifaddresses[iface], cur_ifaddresses, iface)

                    last_ifaddresses[iface] = cur_ifaddresses

                # updating last stuff to current stuff
                last_interfaces = cur_interfaces
                time.sleep(timeout)
            except Exception as e:
                self.logger.warning("Something went wrong during polling: %s",
                                    e)

        self.logger.debug("polling done")

    def check_ifaddresses_diff(self, lifaddr, cifaddr, iface):
        """parses last and current interface addresses of a given interface and
        fires events for discovered differences

        :param lifaddr: dict of family:addresses (last addresses)
        :param cifaddr: dict of family:addresses (curr addresses)
        :param iface: str name of interface (needed only to create interface for event firing)
        """
        self.logger.debug("checking difference of \r\n%s vs \r\n%s", lifaddr, cifaddr)

        intersection = set(lifaddr.keys()) ^ set(cifaddr.keys())
        if len(intersection) > 0:
            self.logger.debug("Sensing a change in address families of interface %s", iface)
            # first check if new address family
            for isectkey in intersection:
                if isectkey in cifaddr.keys():
                    for addr_list in cifaddr.get(isectkey):
                        for addr in addr_list:
                            self.logger.debug("Firing %s event for %s of %s", "address_created", addr, iface)
                            self.api.events.address_created.fire(self.create_interface(iface, cifaddr),
                                                                 Address(address=addr["addr"], family=isectkey))
                elif isectkey in lifaddr.keys():
                    for addr_list in cifaddr.get(isectkey):
                        for addr in addr_list:
                            self.logger.debug("Firing %s event for %s of %s", "address_removed", addr, iface)
                            self.api.events.address_removed.fire(self.create_interface(iface, lifaddr),
                                                                 Address(address=addr["addr"], family=isectkey))

        else:
            for key in lifaddr.keys():
                # check for removed addresses (contained only in lifaddr)
                removed_addr = []
                for laddr in lifaddr.get(key):
                    for caddr in cifaddr.get(key):
                        d = DictDiffer(caddr, laddr)

                        if len(d.changed()) == 0:
                            # this means both addresses are the same -> remove from removed_addr list
                            if laddr in removed_addr:
                                removed_addr.remove(laddr)
                            break

                        else:
                            # else add address to unknown/removed addresses
                            if laddr not in removed_addr:
                                removed_addr.append(laddr)

                if len(removed_addr) > 0:
                    self.logger.debug("removed addresses found: %s", removed_addr)
                    for raddr in removed_addr:
                        self.logger.debug("Firing %s event for %s of %s", "address_removed", raddr, iface)
                        self.api.events.address_removed.fire(self.create_interface(iface, lifaddr),
                                                             Address(address=raddr["addr"], family=key))

                # now check for added addresses (contained only in cifaddr)
                added_addr = []
                for caddr in cifaddr.get(key):
                    for laddr in lifaddr.get(key):
                        d = DictDiffer(caddr, laddr)

                        if len(d.changed()) == 0:
                            # this means both addresses are the same -> remove from added_addr list
                            if caddr in added_addr:
                                added_addr.remove(caddr)
                            break

                        else:
                            # else add address to unknown/added addresses
                            if caddr not in added_addr:
                                added_addr.append(caddr)

                if len(added_addr) > 0:
                    self.logger.debug("added addresses found: %s", added_addr)
                    for aaddr in added_addr:
                        self.logger.debug("Firing %s event for %s of %s", "address_created", aaddr, iface)
                        self.api.events.address_created.fire(self.create_interface(iface, lifaddr),

                                                             Address(address=aaddr["addr"], family=key))
    def remove_ipv6_special_stuff(self, address):
        return address.split("%")


class DictDiffer(object):
    """
    Calculate the difference between two dictionaries as:
    (1) items added
    (2) items removed
    (3) keys same in both but changed values
    (4) keys same in both and unchanged values
    """

    def __init__(self, current_dict, past_dict):
        self.current_dict, self.past_dict = current_dict, past_dict
        self.set_current, self.set_past = set(current_dict.keys()), set(past_dict.keys())
        self.intersect = self.set_current.intersection(self.set_past)

    def added(self):
        return self.set_current - self.intersect

    def removed(self):
        return self.set_past - self.intersect

    def changed(self):
        return set(o for o in self.intersect if self.past_dict[o] != self.current_dict[o])

    def unchanged(self):
        return set(o for o in self.intersect if self.past_dict[o] == self.current_dict[o])
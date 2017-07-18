# Demonstration local server.

import sys
import connection
import options
import link
import time
import constants




class StoreService (link.LinkValue):
    __storage = ""

    def process (self, rx_record):
        msg=rx_record.message
        if constants.PUT == msg.code or constants.POST == msg.code:
            self.__storage = msg.payload
            print 'Storing value: %s' % (self.__storage,)
            msg = connection.Message(connection.Message.ACK, code=constants.CHANGED, payload='Storing value: %s' % (self.__storage,))
        elif constants.DELETE == msg.code:
            self.__storage = ""
            print 'Deleting value: %s' % (self.__storage,)
            msg = connection.Message(connection.Message.ACK, code=constants.DELETED, payload='Deleting value: %s' % (self.__storage,))
        elif constants.GET == msg.code:
            print 'Stored value: %s' % (self.__storage,)
            msg = connection.Message(connection.Message.ACK, code=constants.CONTENT, payload='Stored value: %s' % (self.__storage,))
        rx_record.ack(msg)

class CounterService (link.LinkValue):
    __counter = 0

    def process (self, rx_record):
        ctr = self.__counter
        self.__counter += 1
        msg = connection.Message(connection.Message.ACK, code=constants.CONTENT, payload='%d' % (ctr,))
        rx_record.ack(msg)

class UptimeService (link.LinkValue):
    __started = time.time()

    def process (self, rx_record):
        uptime = time.time() - self.__started
        msg = connection.Message(connection.Message.ACK, code=constants.CONTENT, payload='%g' % (uptime,))
        rx_record.ack(msg)

class ResourceService (link.LinkValue):

    __services = None

    def __init__ (self, *args, **kw):
        super(ResourceService, self).__init__('.well-known/core', ct=[constants.media_types_rev.get('application/link-format')])
        self.__services = { self.uri : self }

    def add_service (self, service):
        self.__services[service.uri] = service
        
    def lookup (self, uri):
        return self.__services.get(uri)

    def process (self, rx_record):
        msg = connection.Message(connection.Message.ACK, code=constants.CONTENT, content_type='application/link-format')
        msg.payload = ",".join([ _s.encode() for _s in self.__services.itervalues() ])
        rx_record.ack(msg)


ep = connection.EndPoint()
ep.socket.bind(('', 12345))#constants.COAP_PORT))

services = ResourceService()
services.add_service(CounterService('counter'))
services.add_service(UptimeService('uptime'))
services.add_service(StoreService('store'))



while True:
    print "Server launched"
    rxr = ep.process(10000)
    if rxr is None:
        print 'No activity'
        continue
    print rxr
    msg = rxr.message
    #remove leading "/"
    uri=msg.uri[1:]
    print "Uri is %s"%uri
    if uri is None:
        continue
    service = services.lookup(uri)
    print 'Lookup %s got %s' % (uri, service)
    if service is None:
        rxr.reset()
        continue
    service.process(rxr)

# Demonstration local server.

import json
import time

import connection
import constants
import link
import options

ep = connection.EndPoint()
ep.socket.bind(('', 5684))  # constants.COAP_PORT))


class parseAll(object):
    def __init__(self):
        pass

    def parsePayload(self, msgpayload, payloadType):

        mpayload = {}
        self.msgpayload = msgpayload
        self.payloadType = payloadType
        if self.msgpayload.find(
                ',') != -1:  # in case of payload '1/1', '2/3/2', '3/4/1': separate based on comma(,)
            self.payloadType = True
            self.msgpayload = str(msgpayload).split(",")
            for i in range(0, len(self.msgpayload)):
                mpayload[i] = str(self.msgpayload[i]).split("/")

                self.msgpayload[i] = mpayload[i]

        else:
            self.msgpayload = str(msgpayload).split("/")

    def returnParseUriQuery(self):
        return self.devParameters

    def returnParsePayload(self):
        return self.msgpayload
        pass

    def returnPayloadType(self):
        return self.payloadType


class storeInformation(object):
    # TODO :: Control mechanism required to see if the same resource object is being POST again.
    def createResource(self, devParams, devPayload, payloadType):  # CREATE

        self.devParams = devParams
        self.devPayload = devPayload
        self.payloadType = payloadType
        print "PRINT PAYLOAD TYPE %s" % self.payloadType

        self.nameTemp = ["objectID", "objectInstID", "resourceID"]
        self.totalFormat = {}

        # check for comma(,) separated payload
        if self.payloadType is True:
            print "ENTER HERE with COMMA"
            for j in range(0, len(self.devPayload)):
                for k in range(0, len(self.devPayload[j])):
                    self.totalFormat[self.nameTemp[k]] = self.devPayload[j][k]

                for p in range(0, len(self.devParams)):
                    testStr = str(self.devParams[p]).split("=")
                    # if p == 0:
                    testStr[0] = str(str(testStr[0]).split(":")[1]).strip()

                    self.totalFormat[testStr[0]] = testStr[1]
                print "TOTAL FORMAT ........ %s" % self.totalFormat

                testStorage.append(self.totalFormat)
                self.totalFormat = {}

            self.payloadType = False

            # else:
            # For No Comma; only 1 payload

            # k=0
            # for charac in self.devPayload:
            #   self.totalFormat[self.nameTemp[k]] = charac
            #  k+=1

        for i in range(0, len(self.devPayload)):
            self.totalFormat[self.nameTemp[i]] = self.devPayload[i]

            for i in range(0, len(self.devParams)):
                testStr = str(self.devParams[i]).split("=")

                # if i==0:
                testStr[0] = str(str(testStr[0]).split(":")[1]).strip()

                self.totalFormat[testStr[0]] = testStr[1]

        print "TOTAL FORMAT ........ %s" % self.totalFormat

        testStorage.append(self.totalFormat)


def getResource(self, devParams,
                devPayload=None):  # READ #for now, payload is NONE

    self.devParams = devParams
    self.devPayload = devPayload
    self.storeAllData = {}
    # print "ENTERING GET %s" %len(self.devParams)

    # for i in range(0, len(self.devParams)):
    testStr = str(self.devParams).split("=")

    # Checks with the Node name to get all the information; needs more details
    # if i==0:
    testStr[0] = str(str(testStr[0]).split(":")[1]).strip()

    for i in range(0, len(testStorage)):

        if testStorage[i]["ep"] == testStr[1]:
            print "TEST STORAGE ..... %s" % testStorage[i]["ep"]
            print "TOTAL CONTENT ....... %s" % testStorage[i]
            self.storeAllData[i] = testStorage[i]


            # print "TEST STORAGE ..... %s" %testStorage[0]["ep"]
            # print "TEST STORAGE ..... %s" %testStorage[1]["ep"]


def returnGetResource(self):
    return self.storeAllData


class StoreService(link.LinkValue):
    __storage = ""

    def process(self, rx_record, uri):
        self.uriQuery_ = uri
        print "TESTING STORE SERVICE......"
        print "URI QUERY ................ %s" % self.uriQuery_
        payloadtype = False

        msg = rx_record.message
        if constants.PUT == msg.code or constants.POST == msg.code:
            self.__storage = msg.payload

            pars.parsePayload(str(self.__storage), payloadtype)
            strInfo.createResource(self.uriQuery_, pars.returnParsePayload(),
                                   pars.returnPayloadType())

            print 'Storing value: %s' % (self.__storage,)
            msg = connection.Message(connection.Message.ACK,
                                     code=constants.CHANGED,
                                     payload='Storing value: %s' % (
                                     self.__storage,))
        elif constants.DELETE == msg.code:
            self.__storage = ""
            print 'Deleting value: %s' % (self.__storage,)
            msg = connection.Message(connection.Message.ACK,
                                     code=constants.DELETED,
                                     payload='Deleting value: %s' % (
                                     self.__storage,))
        elif constants.GET == msg.code:
            print 'Stored value: %s' % (self.__storage,)

            pars.parsePayload(str(self.__storage), payloadtype)

            # print "URI QUERY FROM GET %s" %len(self.uriQuery_)

            strInfo.getResource(self.uriQuery_, pars.returnParsePayload())

            msg = connection.Message(connection.Message.ACK,
                                     code=constants.CONTENT, payload=json.dumps(
                    strInfo.returnGetResource()))  # 'Stored value: %s' % (self.__storage,))
        rx_record.ack(msg)


class CounterService(link.LinkValue):
    __counter = 0

    def process(self, rx_record):
        ctr = self.__counter
        self.__counter += 1
        msg = connection.Message(connection.Message.ACK, code=constants.CONTENT,
                                 payload='%d' % (ctr,))
        rx_record.ack(msg)


class UptimeService(link.LinkValue):
    __started = time.time()

    def process(self, rx_record):
        uptime = time.time() - self.__started
        msg = connection.Message(connection.Message.ACK, code=constants.CONTENT,
                                 payload='%g' % (uptime,))
        rx_record.ack(msg)


class ResourceService(link.LinkValue):
    __services = None

    def __init__(self, *args, **kw):
        super(ResourceService, self).__init__('.well-known/core', ct=[
            constants.media_types_rev.get('application/link-format')])
        self.__services = {self.uri: self}

    def add_service(self, service):
        self.__services[service.uri] = service

    def lookup(self, uri):
        return self.__services.get(uri)

    def process(self, rx_record):
        msg = connection.Message(connection.Message.ACK, code=constants.CONTENT,
                                 content_type='application/link-format')
        msg.payload = ",".join(
            [_s.encode() for _s in self.__services.itervalues()])
        rx_record.ack(msg)


services = ResourceService()
services.add_service(CounterService('counter'))
services.add_service(UptimeService('uptime'))
services.add_service(StoreService('rd'))

pars = parseAll()
strInfo = storeInformation()
testStorage = []

while True:
    print "Server launched"
    rxr = ep.process(10000)
    if rxr is None:
        print 'No activity'
        continue
    print rxr
    msg = rxr.message
    # if constants.GET != msg.code and constants.PUT != msg.code:
    #    continue
    uri = msg.findOption(options.UriPath)
    uriQuery1 = msg.findOption(options.UriQuery)
    print "URI and URI Query .................. %s and %s" % (uri, uriQuery1)
    if uri is None:
        continue
    service = services.lookup(uri.value)
    print 'Lookup %s got %s' % (uri, service)
    if service is None:
        rxr.reset()
        continue
    service.process(rxr, uriQuery1)

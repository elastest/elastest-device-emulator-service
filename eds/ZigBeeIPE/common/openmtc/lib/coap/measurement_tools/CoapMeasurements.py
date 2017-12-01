#PYTHONPATH=../:../../:../../../src:../../../../futile/src python CoapMeasurements.py
from coap import CoapClient
from coapy.coapy import options
from time import sleep
from timeit import timeit, repeat
from random import randrange
import threading


"""Config Constants"""
#SERVER_HOST = "coap://10.147.65.150"
SERVER_HOST = "coap://localhost"
SERVER_PORT = 5000
IP = "%s:%s" % (SERVER_HOST, SERVER_PORT)


def reset(filename="data"):
    """Clear the file content"""
    f = open(filename, 'w')
    f.write('')
    f.close()

    """Delete the old application and create a new one"""
    client = CoapClient(IP)
    client.delete('m2m/applications/apptest')
    client.post('m2m/applications', '{"application": {"appId":"apptest"}}', content_type='application/json')
    client.post('m2m/applications/apptest/containers', '{"container": {"id":"cont1"}}', content_type='application/json')


def run(start_port=10000, reqPerS=100, filename="data"):
    """Config Constants"""
    # Number of requests to be sent
    NUM_REQ = 500  # int(10/(1.0/reqPerS))

    # Used method (POST or GET)
    METHOD = "GET"

    # Path to retrieve in case of GET
    GET_PATH = 'm2m'

    # Size of the randomly generated payload for post requests (in bytes)
    POST_PAYLOAD_SIZE = 200

    # If CONCURRENCY is set to True, a new thread sending a request is created every CONCURRENCY_INTERVAL seconds
    # If CONCURRENCY is set to False, requests wait for a reply before sending a new one (optimal)
    CONCURRENCY = False
    CONCURRENCY_INTERVAL = 1.0/reqPerS

    """Initialization"""
    if METHOD == "POST":
        print "Started, sending %s %s requests on %s\n" % (NUM_REQ, METHOD, IP)
        print "Post Payload is %s" % POST_PAYLOAD_SIZE
    else:
        print "Started, sending %s %s requests on %s/%s\n" % (NUM_REQ, METHOD, IP, GET_PATH)

    if CONCURRENCY:
        print "Concurrency interval %s\n" % CONCURRENCY_INTERVAL
    else:
        print "Concurrency is Off\n"
    client = CoapClient(IP)

    if METHOD == "POST":
        val = "".join([str(randrange(10)) for n in range(POST_PAYLOAD_SIZE - 12)])

    def repeat_post(client):
        client.post('m2m/applications/apptest/containers/cont1/contentInstances', '{"value":"' + val + '"}',
                    content_type='application/json', block1={"size_exponent": 6})

    def repeat_get(client):
        client.get(GET_PATH)

    """Concurrent Measurement loops"""
    def measure_post(i):
        if (i+1) % 50 == 0:
            print "%s requests processed" % (i+1)
        client = CoapClient(IP, client_port=i+start_port)
        t = timeit(lambda: repeat_post(client), number=1)
        t_list.append(t)
        avg = 0
        for tt in t_list:
            avg += tt
        avg = avg / len(t_list)
        f = open(filename, 'a')
        f.write('%s %s\n' % (str(t), avg))
        f.close()

    def measure_get(i):
        if (i+1) % 50 == 0:
            print "%s requests processed" % (i+1)
        client = CoapClient(IP, client_port=i+10000)
        t = timeit(lambda: repeat_get(client), number=1)
        t_list.append(t)
        avg = 0
        for tt in t_list:
            avg += tt
        avg = avg/len(t_list)
        f = open(filename, 'a')
        f.write('%s %s\n' % (str(t), avg))
        f.close()

    """Method differentiation"""
    if METHOD == "POST":
        if CONCURRENCY:
            t_list = []
            for i in range(NUM_REQ):
                t = threading.Thread(target=lambda: measure_post(i))
                t.start()
                sleep(CONCURRENCY_INTERVAL)
            sleep(10)
        else:
            t_list = repeat(lambda: repeat_post(client), number=1, repeat=NUM_REQ)
            strin = "\n".join(map(str, t_list))
            f = open(filename, 'a')
            f.write('%s' % strin)
            f.close()

    elif METHOD == "GET":
        if CONCURRENCY:
            t_list = []
            for i in range(NUM_REQ):
                thr = threading.Thread(target=lambda: measure_get(i))
                thr.start()
                sleep(CONCURRENCY_INTERVAL)
            sleep(2)
        else:
            t_list = repeat(lambda: repeat_get(client), number=1, repeat=NUM_REQ)
            strin = "\n".join(map(str, t_list))
            f = open(filename, 'a')
            f.write('%s' % strin)
            f.close()

    """Overall output"""
    t = 0
    for time in t_list:
        t = time + t
    total_req = len(t_list)

    print "Total experiment time: %ss" % t
    print "Number of req sent: %s" % NUM_REQ
    print "Number of req recv: %s" % total_req
    print "Req rate: %f req/s , %.3f req/ms" % (total_req/t, total_req/(t*1000))
    print "Average RTT: %fms" % ((t/float(total_req))*1000.0)

reset()

thr1 = threading.Thread(target=lambda: run())
thr1.start()

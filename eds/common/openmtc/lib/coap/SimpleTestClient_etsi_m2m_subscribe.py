#Coap Client example
#PYTHONPATH=../:../../src:../../../futile/src python SimpleTestClient.py
from coap import CoapClient
from coapy.coapy import options
from openmtc_scl.plugins.transport_gevent_coap import CoapServer

import logging

logging.basicConfig(level=logging.DEBUG)


certpath = '/opt/OpenMTC/openmtc-python/openmtc-gevent/certs/'

#for dtls and ca certificate usage
keyfile = certpath+'CA_and_certs/pydtls/client/client-keycert.pem'
certfile = certpath+'CA_and_certs/pydtls/client/client-cert.pem'
cacertfile = certpath+'CA_and_certs/pydtls/ca/ca-cert.pem'

#keyfile = '/opt/OpenMTC/openmtc-python/openmtc/lib/ocsp/test/certs/validprivkey.pem'
#certfile = '/opt/OpenMTC/openmtc-python/openmtc/lib/ocsp/test/certs/validcert.pem'
"""
Create a client instance with the server IP and port
Note that coap:// is mandatory here
"""
#client = CoapClient("coap://vs0.inf.ethz.ch:5685/")

#client = CoapClient("coap://localhost:5000", client_port=9876)
# client = CoapClient("coaps://localhost:6000", keyfile=keyfile, certfile=certfile, cacertfile=cacertfile)
#client = CoapClient("coap://130.149.247.214:8089")
#client = CoapClient("coap://coap.me:5683")


def resultPrinter(result):
    print "got result:"
    print result

def errorPrinter(error):
    print "got error:"
    print error

"""
Some example of requests, the return is a response or None
1st param: ressource path
2nd param: payload
Optional params: 'content_type', 'max_age', 'etag', 'uri_host', 'uri_port', 'location', 'if_match',
                 'if_none_match', 'block1', 'block2, 'accept', 'observe'
"""
"""Simple get"""
# client.get("m2m", accept='application/json').then(resultPrinter, errorPrinter)

"""Observe"""
#print client.get("/m2m", observe=0)

"""Create an app"""
#client.post('m2m/applications?x-etsi-correlationID=220&x-etsi-trpdt=2&x-etsi-rcat=0&x-etsi-contactURI=coap://localhost:9000', '{"application": {"appId":"MyApp"}}', content_type='application/json',
#                  uri_host="coap://localhost:15000").then(resultPrinter, errorPrinter)

"""Create container"""
#client.post('m2m/applications/MyApp/containers?x-etsi-correlationID=221&x-etsi-trpdt=4&x-etsi-rcat=0', '{"container": {"id":"MyCon"}}', content_type='application/json',
#                  uri_host="coap://localhost:15000").then(resultPrinter, errorPrinter)

"""Create contentInstance"""


#client.post('m2m/applications/MyApp/containers/MyCon/contentInstances?x-etsi-correlationID=222&x-etsi-trpdt=6&x-etsi-rcat=0', '{"contentInstance": {"id":"MyIns", "content":{"textContent":"world"}}}', content_type='application/json',
#                  uri_host="coap://localhost:15000").then(resultPrinter, errorPrinter)

"""Subscribe"""
#print client.post('m2m/applications/subscriptions','{"subscription": {"id":"A_S", "contact": "coap://localhost:12345"}}')

"""Delete"""
#client.delete("ressource_name")

"""Retargeting"""
#print client.get("/m2m", uri_host="coaps://localhost:16000", accept='application/json')

"""Store and forward"""
#print client.get("m2m/applications?x-etsi-correlationID=2", uri_host="coap://localhost:15000", accept='application/json')
# print client.get("m2m/applications?x-etsi-correlationID=223&x-etsi-trpdt=0&x-etsi-rcat=0", uri_host="coap://localhost:15000")

#client.delete("m2m/applications/MyApp/containers/MyCon/contentInstances/MyIns?x-etsi-correlationID=224&x-etsi-trpdt=0&x-etsi-rcat=0", uri_host="coap://localhost:15000").then(
#    resultPrinter, errorPrinter)
#client.delete("m2m/applications/MyApp/containers/MyCon?x-etsi-correlationID=225&x-etsi-trpdt=00&x-etsi-rcat=0", uri_host="coap://localhost:15000").then(resultPrinter, errorPrinter)
#client.delete("m2m/applications/MyApp?x-etsi-correlationID=226&x-etsi-trpdt=0&x-etsi-rcat=0", uri_host="coap://localhost:15000").then(resultPrinter, errorPrinter)

"""Block1"""
# client.post('m2m/applications', '{"application": {"appId":"myapp"}}', content_type='application/json', block1={"size_exponent":4}).then(resultPrinter, errorPrinter)

"""Block2"""
# print client.get("/m2m", block2={"size_exponent":5})

"""Block2 and retargeting"""
#print client.get("/m2m", block2={"size_exponent":5}, uri_host="coap://localhost:15000")

"""Accept"""
#print client.get("/m2m", accept=50)
#print client.get("/m2m", accept='application/xml')

"""
Generic request format
Supported methods: GET POST PUT DELETE
"""
#client.request("GET","path")
#client.request("PUT","path","data")

#client = CoapClient("coap://130.149.247.213:8090", client_port=9876)
'''
client = CoapClient("coap://10.0.0.79:8090", client_port=9876)

client.delete("onem2m/MyOwnApp")
client.post("onem2m?rt=AE&nm=MyOwnApp", '{"AE":{}}', content_type='application/json')
client.post("onem2m/MyOwnApp?nm=myContainer", '{"container":{}}', content_type='application/json')
client.post("onem2m/MyOwnApp/myContainer?nm=mySubContainer", '{"container":{}}', content_type='application/json')
client.post("onem2m/MyOwnApp/myContainer/mySubContainer?nm=myContentInstance", '{"contentInstance":{"content":"myContent", "encoding":1}}', content_type='application/json')
#client.post("onem2m/MyOwnApp/myContainer?rt=subscription&nm=mySubscription", '{"subscription":{"notificationURI":["coap://10.252.55.54:8090"]}}', content_type='application/json')
'''

#client = CoapClient("coap://10.0.0.230:8090", client_port=9876)
#client.post("/m2m/applications/EUPilot/containers/Devices/subcontainers/Device_1/subcontainers/Settings/contentInstances/subscriptions",'{"subscription":{"contact":"coap://10.252.55.54:8090","filterCriteria":{"attributeAccessor":"latest/content"}}}', content_type='application/json')



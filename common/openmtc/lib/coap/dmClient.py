#Coap Client example
#PYTHONPATH=../:../../src:../../../futile/src python SimpleTestClient.py
from coap import CoapClient
import ast
import json

"""
Create a client instance with the server IP and port
Note that coap:// is mandatory here
"""
#client = CoapClient("coap://ns.tzi.org:61616")
client = CoapClient("coap://localhost:5684")

"""
Some example of requests, the return is always a promise object
1st param: ressource path
2nd param: payload
Optional params: 'content_type', 'max_age', 'uri_scheme', 'etag', 'uri_authority', 'location'
"""
#p=client.post("sink","data")
#p=client.put("rd?ep=test","data")
#p=client.delete("ressource_name")
p=client.post("rd?ep=node1&lt=4500&version=1&binding=U","3/1/1, 4/1/2")
#p=client.post("rd?ep=node2&lt=9000&version=5&binding=UP","3/2/2")
p=client.get("rd?ep=node1")
#&lt=4500&version=1&binding=U"
#, content_type='JSON'

#This fails:
#p=client.get("mes")
#This works:
#p=client.get("res")

"""
Generic request format
Supported methods: GET POST PUT DELETE
"""
#p=client.request("GET","path")
#p=client.request("PUT","path","data")

"""
Processing of the Promise with a simple handler


# converting the string payload into Dictionary/JSON format:
#import ast
#ast.literal_eval("string")

"""
def handl(x):
    print "Handling %s \n %s"%(x,x.payload)
    print "PAYLOAD 0 %s" %json.loads(x.payload)['0']["ep"]
    #print "PAYLOAD with json " %eval(x.payload)
   # xr = ast.literal_eval(x.payload)[1]
   # print "PRINTING resourceID ..... %s" % xr["resourceID"]
p.then(handl)

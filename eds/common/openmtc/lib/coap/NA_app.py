#Coap Client example
#PYTHONPATH=../:../../src:../../../futile/src python SimpleTestClient.py
from coap import CoapClient
from lwm2m import lwm2m_ClientRegIntf

"""
Create a client instance with the server IP and port
Note that coap:// is mandatory here
"""

#client = CoapClient("coap://localhost:5688")

server_ip = "localhost"
server_port = 5684
server_ip_port = server_ip + ":" + str(server_port)

client_port = 5900 #5900

client = lwm2m_ClientRegIntf()

#query = "rd/AMYNNKP49F/3"
client.observeResource(server_ip_port, path = "rd/B4HCMFE0GG/3", client_port = client_port)

##
#path = "rd/XFHCW5B0QL/3"
#client.cancelSubscription(server_ip_port, path = path, client_port=client_port)



#client.discoverResource(server_ip_port, path = ".well-known/core", client_port = client_port)
#client.discoverResource(server_ip_port, path = "rd/B4HCMFE0GG/3/0", client_port = client_port)
##Discovery
##
#query = "discover"
#client.discoverResource(server_ip_port, query, 3, client_port= client_port)


#Write Attributes
##
#query = "pmax=33&pmin=7"
#client.writeAttributes(server_ip_port, query, path = "rd/B4HCMFE0GG/3", client_port = client_port)



#Observation

#query = "observe"
#client.observeResource(server_ip_port, query,  3, client_port = client_port)


#
##Cancel Observation
#







"""
Some example of requests, the return is a response or None
1st param: ressource path
2nd param: payload
Optional params: 'content_type', 'max_age', 'etag', 'uri_host', 'uri_port', 'location', 'if_match', 'if_none_match'
"""

#print client.put("rd?manu=myclients", "3/0")


"""
Generic request format
Supported methods: GET POST PUT DELETE
"""
#client.request("GET","path")
#client.request("PUT","path","data")



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
server_port = 5688
server_ip_port = server_ip + ":" + str(server_port)

client_port = 5902

client = lwm2m_ClientRegIntf()

#Updates
query = "lt=5005"
path = "rd?"
payload = "3/1"

#client.clientRegistration(server_ip_port, path, query, payload, client_port = client_port)
client.clientUpdate(server_ip_port, path, query, payload, client_port= client_port)

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



import sys
from gevent import socket

address = ('127.0.0.1', 8022)
    
xml_file = open('iq100.xml','r')
xml_message = xml_file.read()

sock = socket.socket(type=socket.SOCK_DGRAM)
sock.connect(address)

print 'Sending %s bytes to %s:%s' % ((len(xml_message), ) + address)
sock.sendall(xml_message)
confirmation_mesage = sock.recvfrom(8022)
print confirmation_mesage


xml_file = open('iq200.xml','r')
xml_message = xml_file.read()

sock = socket.socket(type=socket.SOCK_DGRAM)
sock.connect(address)

print 'Sending %s bytes to %s:%s' % ((len(xml_message), ) + address)
sock.sendall(xml_message)
confirmation_mesage = sock.recvfrom(8022)
print confirmation_mesage


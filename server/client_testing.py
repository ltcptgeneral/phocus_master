#from socket import *
import sys
import zmq
import random

port = "4445"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)
    
context = zmq.Context()
print "Connecting to server..."
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)
if len(sys.argv) > 2:
    socket.connect ("tcp://localhost:%s" % port1)
    
#  Do 10 requests, waiting each time for a response
print "Sending request "
socket.send (str(random.randint(-100, 100)))
#  Get the reply.
message = socket.recv()
print "Received: ", "[", message, "]"

"""
def get_constants(prefix):
    #Create a dictionary mapping socket module constants to their names.
    return dict( (getattr(socket, n), n)
                 for n in dir(socket)
                 if n.startswith(prefix)
                 )

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

# Create a TCP/IP socket

sock = create_connection(("143.195.117.237", 4445))

print >>sys.stderr, 'Family  :', families[sock.family]
print >>sys.stderr, 'Type    :', types[sock.type]
print >>sys.stderr, 'Protocol:', protocols[sock.proto]
print >>sys.stderr

try:
    
    # Send data
    message = 'This is the message.  It will be repeated.'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()


"""

#import socket
import sys
import time
import zmq

port = '4445'
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)
print("binded to port %s" % port)

while True:
    #  Wait for next request from client
    message = socket.recv()
    print "Received: ", message
    time.sleep (1)  
    socket.send("ack %s" % port)

    
""" Below is Socket implementation, obsolete
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Find correct IP socket
socket_address = socket.gethostbyname(socket.gethostname())

# Bind the socket to the port
server_address = (socket_address, 4445)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
# Listen for incoming connections
sock.listen(5)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(64)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
    #except socket.error:
 
    finally:
        # Clean up the connection
        connection.close()

"""

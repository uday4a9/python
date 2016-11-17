#! /usr/bin/env /usr/bin/python

from socket import *
import sys

def server():
    sock = create_connection(('pypi.python.org', 80))
    sock.send('GET pypi.python.org/pypi/requests/json')
    print sock.recv(100)

if __name__ == '__main__':
    #assert(len(sys.argv) == 3)
    server()

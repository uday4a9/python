#! /usr/bin/env /usr/bin/python

from socket import *
import sys
LFCR = "\r\n\r\n"
import urllib2
import time

def starter(*args):
    sock = socket(AF_INET, SOCK_STREAM, 0)
    sock.connect(("www.python.org", 80))
    ip = ("GET {0} HTTP/1.0".format(''.join(*args)))
    print(ip)
    sock.send("GET {0} HTTP/1.0".format(args[0]) + LFCR)
    while True:
        line = sock.recv(200)
        if not line:
            break
        print(line)

def urlreader(link):
    ufd = urllib2.urlopen(link)
    start = time.time()
    #print(ufd.read())
    print("Took {0}sec".format(time.time() - start))

if __name__ == '__main__':
    #starter(sys.argv[1:])
    for i in range(1):
        urlreader(sys.argv[1])

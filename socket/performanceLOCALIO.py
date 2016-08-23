#! /usr/bin/env /usr/bin/python

"""
    This program demonstrates how threading, processing and sequential call works for
I/O bound tasks.

Ex:
    python performanceLOCALIO.py threading 15 localhost 25000
    python performanceLOCALIO.py sequential 15 localhost 25000
    python performanceLOCALIO.py processing 15 localhost 25000
--------------------
Before running this program needs to run server program : "perfserver.py"
"""

import urllib2
import time
import sys
import threading
import multiprocessing
from socket import *

def opener(*args):
    conn = create_connection(('localhost', 25000))
    while True:
        buf = conn.recv(40)
        if not buf:
            break
        sys.stdout.write(buf)



if __name__ == '__main__':

    if sys.argv[1] == "sequential":
        start = time.time()
        for i in range(int(sys.argv[2])):
            opener(sys.argv[3:])
        print("sequential took {0} sec".format(time.time()-start))
    elif sys.argv[1] == "threading":
        threads = []

        for i in range(int(sys.argv[2])):
            threads.append(threading.Thread(target=opener, args=(sys.argv[3:],)))

        start = time.time()
        for trd in threads:
            trd.start()

        for trd in threads:
            trd.join()
        print("threading took {0} sec".format(time.time()-start))
    elif sys.argv[1] == "processing":
        procs = []

        for i in range(int(sys.argv[2])):
            procs.append(multiprocessing.Process(target=opener, args=(sys.argv[3:],)))

        start = time.time()
        for proc in procs:
            proc.start()

        for proc in procs:
            proc.join()
        print("multiprocessing took {0} sec".format(time.time()-start))

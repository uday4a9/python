#! /usr/bin/env /usr/bin/python

"""
    This program demonstrates how threading, processing and sequential call works for
I/O bound tasks.

Ex:
    ./performancIO.py sequentital requests requests 
    ./performanceIO.py threading requests requests
    ./performanceIO.py processing requests requests
"""

import urllib2
import time
import sys
import threading
import multiprocessing

def opener(module):
    #start = time.time()
    opener = urllib2.urlopen("https://pypi.python.org/pypi/{0}/json".format(module))
    end = time.time()
    #print("{0} took : {1} secs".format(module, end-start))


if __name__ == '__main__':

    if sys.argv[1] == "sequential":
        start = time.time()
        for mod in sys.argv[2:]:
            opener(mod)
        print("sequential took {0} sec".format(time.time()-start))
    elif sys.argv[1] == "threading":
        threads = []

        for mod in sys.argv[2:]:
            threads.append(threading.Thread(target=opener, args=(mod,)))

        start = time.time()
        for trd in threads:
            trd.start()

        for trd in threads:
            trd.join()
        print("threading took {0} sec".format(time.time()-start))
    elif sys.argv[1] == "processing":
        procs = []

        for mod in sys.argv[2:]:
            procs.append(multiprocessing.Process(target=opener, args=(mod,)))

        start = time.time()
        for proc in procs:
            proc.start()

        for proc in procs:
            proc.join()
        print("multiprocessing took {0} sec".format(time.time()-start))

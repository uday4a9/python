#! /usr/bin/env /usr/bin/python

"""
    This program demonstrates how threading and sequential call works for
CPU bound tasks.
"""

import urllib2
import time
import sys
import threading
import multiprocessing

def fib(number):
    if number < 2:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)

if __name__ == '__main__':

    if sys.argv[1] == "sequential":
        start = time.time()
        for mod in sys.argv[2:]:
            fib(int(mod))
        print("sequential took {0} sec".format(time.time()-start))
    elif sys.argv[1] == "threading":
        threads = []

        for mod in sys.argv[2:]:
            threads.append(threading.Thread(target=fib, args=(int(mod),)))

        start = time.time()
        for trd in threads:
            trd.start()

        for trd in threads:
            trd.join()
        print("threading took {0} sec".format(time.time()-start))
    elif sys.argv[1] == "processing":
        procs = []

        for mod in sys.argv[2:]:
            procs.append(multiprocessing.Process(target=fib, args=(int(mod),)))

        start = time.time()
        for proc in procs:
            proc.start()

        for proc in procs:
            proc.join()
        print("multiprocessing took {0} sec".format(time.time()-start))

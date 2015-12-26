#! /usr/bin/env /usr/bin/python

import threading
import sys
import threading
import time
import signal

def handler(signo, frame):
    print "Got the:", signo
    return

signal.signal(signal.SIGINT, handler)


def thread():
    myname = threading.current_thread().getName()
    print "Just started", myname, "thread"
    try:
        raw_input()
    except EOFError, emsg:
        print emsg
        return

def main():
    print main.__name__, "function invoked"
    threadnames = ["sender", "receiver"]
    threads = []

    for i in range(len(threadnames)):
        thrd = threading.Thread(target=thread, name=threadnames[i])
        threads.append(thrd)

    for i in range(len(threadnames)):
        threads[i].start()

    for i in range(len(threadnames)):
        threads[i].join()

if __name__ == '__main__':
    main()

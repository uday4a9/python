#! /usr/bin/env /usr/bin/python

import threading
import sys
import threading
import time

status = True

def thread1 ():
    i = 0
    while status:
        time.sleep(1)
        print str(i), ":", threading.current_thread().getName(), "In Action"
#        if i == 2:
#            print "THREAD1 coming out"
#            break
        i += 1

def thread2 ():
    i = 0
    while status:
        time.sleep(2)
        print str(i), ":", threading.current_thread().getName(), "In Action"
#        if i == 2:
#            print "THREAD2 coming out"
#            break
        i += 1

def killer():
    global status
    status = False
    print threading.current_thread().getName(), "thread invoked for change status"

if __name__ == '__main__':
    print "Time :", time.time()
    thrd = threading.Timer(9.0, killer)
    thrd.start()

    threads  = []
    threads.append(threading.Thread(target=thread1, name="THREAD1"))
    threads.append(threading.Thread(target=thread2, name="THREAD2"))

    for thread in threads:
        thread.setDaemon(True)
        thread.start()

    for thread in threads:
        thread.join()

    if thrd.isAlive():
        print "Still thread is alive"
        thrd.cancel()
        thrd.join()

    print "Thread status :", thrd.isAlive()
    print "Time :", time.time()

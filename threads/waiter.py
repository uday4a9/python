#! /usr/bin/env /usr/bin/python

""" 
    This program to demomnstrate one function excution waits
till other thread started execution
"""

import threading
import time


def fun(val, cond):
    cond.acquire()
    print("waiting on fun")
    cond.wait()
    print("After releasing lock in fun")
    time.sleep(val)
    print("End of the execution of fun")
    cond.notify()
    cond.release()

def foo(val, cond):
    cond.acquire()
    print("waiting on foo")
    #cond.wait()
    print("After releasing lock in foo")
    time.sleep(val)
    print("End of the execution of foo")
    cond.notify()
    cond.release()


if __name__ == '__main__':
    lock = threading.Lock()
    cond = threading.Condition(lock)
    trds = []

    trd1 = threading.Thread(target=fun, args=(3, cond,))
    trd2 = threading.Thread(target=foo, args=(4, cond,))
    trd1.start()
    trd2.start()

    trd1.join()
    trd2.join()

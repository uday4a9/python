#! /usr/bin/env /usr/bin/python

import threading
import time
import Queue

queue = Queue.Queue()


def goo():
    for i in range(10):
        if i == 2:
            queue.put(KeyError)
            raise KeyError
        time.sleep(.5)
        print("Running time in goo : {}".format(i + 1))

def foo():
    gtrd = threading.Thread(target=goo, name="goo")
    try:
        gtrd.start()
    except Exception:
        print("Caught the exception")

    for i in range(10):
        try:
            exc = queue.get(block=False)
        except Queue.Empty:
            pass
        else:
#            exc_type, exc_obj, exc_trace = exc
            print("TYPE::::", exc)
            raise exc 
#            break

        time.sleep(2)
        print("Running time in foo: {}".format(i + 1))

    print("STATUS :", gtrd.isAlive())
    if gtrd.isAlive():
        gtrd.join()

def checker():
    ftrd = threading.Thread(target=foo, name="foo")

    ftrd.start()

    print("BEFORE FTRD STATUS :", ftrd.isAlive())
    if ftrd.isAlive():
        ftrd.join()
    print("AFTER FTRD STATUS :", ftrd.isAlive())

if __name__ == '__main__':
    checker()

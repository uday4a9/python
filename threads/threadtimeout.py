#! /usr/bin/env /usr/bin/python

import threading
import time

def foo(sec):
    print("Begining of foo : {0} ".format(time.time()))
    time.sleep(sec)
    print("Done with foo : {0} ".format(time.time()))

if __name__ == '__main__':
    trd = threading.Thread(target=foo, args=(3,))
    trd.start()
    trd.join(4)
    print("STATUS : {0}".format(trd.isAlive()))

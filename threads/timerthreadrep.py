#! /usr/bin/env /usr/bin/python

import threading
import time


starttime = None
timer = None

def fun():
    global starttime, timer
    print("Invoked @ {0}".format(time.time()-starttime))
    timer = threading.Timer(3, fun)
    timer.start()
    starttime = time.time()


def main():
    global starttime, timer
    starttime = time.time()
    timer = threading.Timer(3, fun)
    timer.start()
    time.sleep(11.5)
    timer.cancel()


if __name__ == '__main__':
    main()

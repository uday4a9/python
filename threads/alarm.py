#! /usr/bin/env /usr/bin/python

import threading
import time

i = 0

def thread_target(hello, hi):
    while True:
        print hello, hi
        global i
        time.sleep(.5)
        print i, threading.current_thread().getName()
        if i == 5:
            return
        i += 1

def main():
    print "Main thread invoked"


if __name__ == '__main__':
    main()
    args = ["sdfasdfsadfdsaF", "Hello"]
    thrd = threading.Thread(target=thread_target, name="THREAD_TARGET", args=("sdfasdfsadfdsaF", "Hello"))
    thrd.setDaemon(True)
    thrd.start()
    thrd.join()

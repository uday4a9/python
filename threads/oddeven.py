#! /usr/bin/env /usr/bin/python

import threading

val = 0
mval = 20

lock = threading.RLock()
cond = threading.Condition(lock)

def eventhread():
    global val
    while 1:
        cond.acquire()
        if val % 2 == 1:
            cond.wait()
        if val > mval:
            cond.notify(1)
            cond.release()
            break
        #print("EVEN :", val)
        print(threading.currentThread().getName(), val)
        val += 1
        cond.notify(1)
        cond.release()

def oddthread():
    global val
    while 1:
        cond.acquire()
        if val % 2 == 0:
            cond.wait()
        if val > mval:
            cond.notify(1)
            cond.release()
            break
        #print("ODD:", val)
        print(threading.currentThread().getName(), val)
        val += 1
        cond.notify(1)
        cond.release()

if __name__ == '__main__':
    threads = []
    targets = [eventhread, oddthread]
    targets_name = ["eventhread", "oddthread"]

    i = 0
    for tar in targets:
        threads.append(threading.Thread(target=tar, name=targets_name[i]))
        i += 1

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

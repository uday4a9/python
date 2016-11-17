#! /usr/bin/env /usr/bin/python

import threading

class MyTimer(object):
    def  __init__(self):
        self.timer  = threading.Timer(3, self.foo)

    def foo(self):
        print("Foo method invoked")
        self.timer  = threading.Timer(3, self.foo)
        self.timer.start()

    def start(self):
        self.timer.start()
    
    def cancel(self):
        self.timer.cancel()

ev = threading.Event()
ev.clear()

def wait():
    print ev.isSet()
    s = ev.wait(5)
    if not s:
        print "TIMEOUT"
    print("Waiting OVER")

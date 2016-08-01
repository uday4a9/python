#! /usr/bin/env /usr/bin/python

import time
from contextlib import contextmanager 

def timethis(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print func.__name__, "executed for :", str(time.time() - start)+"sec"
    return inner

#@timethis
def fun(val):
    time.sleep(val)
fun = timethis(fun)
# Above works like a decorator method and time the function

@contextmanager
def timethisto(label):
    start = time.time()
    try:
        yield
    finally:
        print("%s : %0.3f"%(label, time.time()-start))

def foo(val):
    with timethisto('waiting'):
        time.sleep(val)
#Above code works like ocntext managering the code and time the function

@contextmanager
def fgen(val):
    try:
        yield val
    finally:
        print "close with val"
        
def boo(val):
    with fgen('waiting'):
        time.sleep(val)

if __name__ == '__main__':
    print "hello"
    fun(1.8)
    foo(2.9)
    boo(2)

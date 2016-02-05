#! /usr/bin/env /usr/bin/python3

import sys
from collections import namedtuple

Result = namedtuple('Result', 'count average')

class MyException(Exception):
    """
    While deriving the new Exceptions, __init__ should not return 
    other than None
    """
    pass

def demo():
    print("-> coroutine started")
    while True:
        try:
            x = yield
        except MyException:
            print("Caught with MyException, and breaking from here")
            sys.exit(1)
        else:
            print("got : {}".format(x))

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)

def yfrom():
    yield from "ABC"
    yield from [1, 2, 3]
print("Usage of yield from :", list(yfrom()))

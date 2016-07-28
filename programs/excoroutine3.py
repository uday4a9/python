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
    """ By sending the None at last it'll returns the value
    in namedtuple by raising StopIteration"""
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

def grouper(results, key):
    while True:
        results[key] = yield from averager()


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format( result.count,
            group, result.average, unit))

def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)
    report(results)

data = {
        'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5], 
        'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
        'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
        'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
     }

def yfrom():
    yield from "ABC"
    yield from [1, 2, 3]
#print("Usage of yield from :", list(yfrom()))

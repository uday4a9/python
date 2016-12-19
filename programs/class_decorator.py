#! /usr/bin/env /usr/bin/python3.5

import sys
import pdb
from functools import wraps
from pprint import pprint

debug = False 


def debugger(method):
    def inner_method(*args, **kwargs):
        if debug:
            print("method Debugger started")
            pdb.set_trace()

        print(method.__name__, "Invoked => ", *args, **kwargs)
        return method(*args, **kwargs)
    return inner_method

def clsdebugger(cls):
    def inner_method(*args, **kwargs):
        if debug:
            print("class Debugger started")
            pdb.set_trace()
        pprint(list(cls.__dict__.items()))
        try:
            mobj = cls(*args, **kwargs)
        except TypeError:
            mobj = cls()
        for key, val in cls.__dict__.items():
            if callable(val) and val.__name__.startswith('get_'):
                print("method :", val.__qualname__)
                cls.__dict__[val.__name__](mobj)
                #setattr(mobj, 'c', 1)
        return mobj
    return inner_method

@clsdebugger
class Mine:
    #    def __init__(self, *args, **kwargs):
    #        print("Mine object created :", *args, **kwargs)

    def function(self):
        print("Function call made")

    def get_a(self):
        print("get_a method invoked")

    def get_b(self):
        print("get_b method invoked")

if __name__ == '__main__':
    m = Mine("hello", "hi", {'s' : 34})

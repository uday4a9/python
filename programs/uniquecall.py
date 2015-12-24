#! /usr/bin/env /usr/bin/python

import os, sys


def call_once(func):
    def wrap(*args, **kwargs):
        if not wrap._called:
            try:
                return func(*args, **kwargs)
            finally:
                wrap._called = True
    wrap._called = False
    return wrap


class Main(object):
    """
     Here make sure that class method should call only once 
    irrespective of any number of objects.
    """
    def __init__(self, val):
        """
         Here it invokes the class initializer with needed elements
        """
        self.val = val

    def show(self):
        print "Got the value :", self.val
    
    def call_once(func):
        def wrap(*args, **kwargs):
            if not wrap._called:
                try:
                    return func(*args, **kwargs)
                finally:
                    wrap._called = True
        wrap._called = False

    @self.call_once
    def call_once(self):
        print "This function invoke only once"


if __name__ == '__main__':
    obj1 = Main(12)
    obj2 = Main(13)
    obj3 = Main(14)
    obj4 = Main(15)

    obj1.show()
    obj2.show()
    obj3.show()
    obj4.show()

    obj1.call_once()
    obj2.call_once()
    obj3.call_once()
    obj4.call_once()

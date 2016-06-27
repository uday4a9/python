#! /usr/bin/env /usr/bin/python

import os
import sys


class Simple(object):
    """
    simple class to demonstrate the usage of __call__
    """

    def __init__(self):
        print "Object Created"

    def __call__(self):
        print "Object invoked"


if __name__ == '__main__':
    obj1 = Simple()
    obj1()
    obj1.new = "Value"

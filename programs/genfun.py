#! /usr/bin/env /usr/bin/python

import sys
import os

sys.path.append(os.getcwd())

total = 2

def final():
    print "Called final after :", total

def gen():
    while True:
        if total == 2:
            one = yield
            print "Got one of two :", one
            two = yield
            print "Got two of two :", two
        if total == 1:
            one = yield
            print "Got one of one :", one
        final()

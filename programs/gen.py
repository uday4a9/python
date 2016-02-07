#! /usr/bin/env /usr/bin/python

import os
import sys

def fun(val):
    a = []
    for i in range(val):
        a.append(i)
    return a

def gen(val):
    for i in range(val):
        yield i

l = fun(10)
g = gen(10)

print "LIST1"
for i in l:
    print i
print "LIST2"
for i in l:
    print i

print "GEN1"
for i in g:
    print i
print "GEN2"
for i in g:
    print i

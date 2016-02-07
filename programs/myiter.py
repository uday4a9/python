#! /usr/bin/env /usr/bin/python

import os
import sys
import time



def main():
    print "In Main function"


class Iter(object):
    def __init__(self):
        print "Just an object created"
        self.lst = []
        self._len = 0

    def append(self, _val):
        #self.lst.append(_val)
        self.lst.insert(self._len, _val)
        self._len += 1

    def __iter__(self):
        print "Just iterator invoked"
        return iter(self.lst)

    def __str__(self):
        return str(self.lst)

    def __len__(self):
        return self._len
        #return len(self.lst)

if __name__ == '__main__':
    print "Invokes my iterator module"
    it = Iter()

    prv = time.time()
    for i in range(10000000):
        it.append(i)
    print "Time taken : ", (time.time() - prv)

#    print it

#    for i in it:
#        print i

    prv = time.time()
    print "prv :", prv
    print "Length : ", len(it)
    print "Time taken : ", (time.time() - prv)
    print time.time()

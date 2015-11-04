#! /usr/bin/env /usr/bin/python

import sys
import mydebug
sys.settrace(mydebug.tracer)

def main(*args):
    print "Got the args:", args
    print "Length:", len(*args)
    print 1 / 0
    open('a.txt', 'r')

if __name__ == '__main__':
#    sys.settrace(mydebug.tracer)
    main(sys.argv[1:])

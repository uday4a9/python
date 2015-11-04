#! /usr/bin/env /usr/bin/python

import sys

def main(*args):
    print "Got the args:", args
    print "Length:", len(*args)

if __name__ == '__main__':
    main(sys.argv[1:])

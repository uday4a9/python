#! /usr/bin/env /usr/bin/python3

import sys

class File(object):
    def __init__(self, fil):
        self.__fil = fil
#        print("Context object created")

    def __enter__(self):
        print('=' * 10 + "\nexecuted the enter part")

    def __exit__(self, exc_type, exc_value, traceback):
        print("executed the exit part\n" + '=' * 10)

if __name__ == '__main__':
    assert (len(sys.argv) == 2)
    f = File(sys.argv[1])

    with f as fp:
        print("Inside the context operation")

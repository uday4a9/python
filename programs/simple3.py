#! /usr/bin/env /usr/bin/python3

import os
import sys


class Klass(object):

    def __init__(self):
        self._val = []
        self.__values = []

    def __len__(self):
        return len(self._val)

    def append(self, item):
        self._val.append(item)

def main():
    print("In main Function")

if __name__ == '__main__':
    main()

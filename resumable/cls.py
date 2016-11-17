#! /usr/bin/env /usr/bin/python

class Main(object):
    def __init__(self):
        print ("INIT")
        self.res = None

    def result(self, res):
        self.res = res
        self.res[1] = "1233"

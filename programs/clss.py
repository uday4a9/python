#! /usr/bin/env /usr/bin/python

class Main(object):
    """
    Created a simple class to check how the
    variables can be accessed
    """
    val = 34
    def __init__(self):
        print("Just created an object")

    def show(self):
        print("In show method {0}".format(self.val))

if __name__ == '__main__':
    m = Main()
    m.show()

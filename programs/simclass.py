#! /usr/bin/env /usr/bin/python

import sys

class Base(object):
    def __init__(self, val):
        #print "Object created"
        self.val = val

    def display(self):
        print "Value is :", self.val

    def change(self, new):
        self.val = new


bobj = Base(5)
#bobj.display()

class derived(object):
    def __init__(self):
        self.base = bobj
	print "self.base.val :", self.base.val

    def display(self):
        print "In derived display method"
        self.base.display()

    def change(self, new):
        self.base.change(new)
        

objs = [derived(), derived()]

print "Displaying items"
for item in objs:
    item.display()

objs[0].change(40)

print "After changing items"
for item in objs:
    item.display()

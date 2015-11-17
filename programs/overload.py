#! /usr/bin/env /usr/bin/python
'''
Simple module to show how overload works.
1. overloading the print(__str__) method for the
   Class.
2. overloading the +(__add__) method to perform 
   addtion operation. This method just adds the 
   given number and returns the resultant value.
Observations:
1. Able to inherit the overloaded print and 
   add methods to the base class.
2. If there is a scenario, Need to create base 
   class attributes to the derived class, Then 
   simple invoke bsae class dict and run it as
   exec statements.
   EXAMPLE:
    In derived class Two @ __init__ method add below
    statements upon successful running on the dictionary.
	   print " BASE DICT", One().__dict__
	   exec('self.' + 'val' + '= 12')
3. To use all variables in base to derived class use
   below way invoke super method.
   EXAMPLE:
        One.__init__(self, val)
'''

import os
import sys


class One:
    def __init__(self, val=0):
	""" initializer for class One """
        self.val = val
	self.no = None

    def __str__(self):
        """ Over loading and printing the object 
	directly"""
	return "val : %d" %(self.val)

    def __add__(self, add):
        """ add the given value to the instance
	"""
	#print "in overloaded add method"
	self.val += add
	return self

    def __iadd__(self, add):
        """ inplace addtion to acheive the result
	"""
	self.val += add

    def display(self):
        """ print in display method """
	print "In display method"

class Two(One):
    def __init__(self, val=0):
        print "IN DERIVED INIT"
        #One(val).__init__(val)
        One.__init__(self, val)
        #One(val)
	#self.val = val
	#print " BASE DICT", One().__dict__
	#exec('self.' + 'val' + '= 12')
	#print "TWO", One(val).__dict__['val']

if __name__ == '__main__':
    instance = One(12)
    #instance()
    print (instance)
    print (instance + 3)
    instance += 3 * 3
    print (instance)
    in2 = Two(-3)
    print (in2)
    #print dir(in2)
    print (in2 + 5)

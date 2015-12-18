#! /usr/bin/env /usr/bin/python


class Klass(object):
    """
     Class which gives the class related operations
    """
    # variables definfing in this section are called as class variables
    # or class attributes. These are similar to STATIC varibales in c++.
    
    value = "CLASS VARIABLE"

    def __init__(self, val=-1):
        # Here the declared vaiables are called as instance attributes
	# or variables.
        print "Object created"
	self._val = val

    @classmethod
    def method(cls, item):
        # Here first argument is class name, So, we are able to access
	# Class attribute here
        print "Got the item to class method :", item
	print "VALUE : ", cls.value

    def chng(self, item):
        self._val = item
        print "Got the items to chng method :", item

    @staticmethod
    def smethod():
        # this is self less method. This can be accessed using
	# both instances and class.
	# Need to access only, Class variables only.
        print "In static method"
	print "VALUE :", Klass.value

    def __str__(self):
        return "object value: {0}".format(self._val)


if __name__ == '__main__':
    obj1 = Klass()

    # Below is invoking the method using object
    print obj1
    obj1.chng(40)
    print obj1
    # Below is the internal implementation of the above call
    Klass.chng(obj1, 20)
    print obj1

    # Below code demonstrates the classmethod
    obj2 = Klass(30)
    obj2.method("got it")
    Klass.method("Hello")
    # Above calls are same, but instead of having the call from instance
    # Need to invoke with class. So, Here we shouldn't execute values with
    # self argument. So, Avoid using self argument in class methods. This 
    # class method needed mainly when we need to access class attributes rather
    # than instance attributes.


    # Below code demonstrates the staticmetod
    obj3 = Klass(10)
    Klass.smethod()

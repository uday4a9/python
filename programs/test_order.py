from unittest.loader import TestLoader
import unittest
import collections

"""
	THis program demonstrates, How to execute the unittest cases in given order.
    Metaclass helps to build the data in given order.
    Last method name should be using only test_cleanup only
"""

def getOrderedTestCaseNames(self, testCaseClass):
    """Return a sorted sequence of method names found within testCaseClass
    """
    def isTestMethod(attrname, testCaseClass=testCaseClass,
                     prefix=self.testMethodPrefix):
        return attrname.startswith(prefix) and \
            callable(getattr(testCaseClass, attrname))
    testFnNames = list(filter(isTestMethod, testCaseClass._ordered))

    if testFnNames[-1] != "test_cleanup":
        raise AttributeError("last method of {0} should be `test_cleanup`".format(testCaseClass))
    return testFnNames

setattr(TestLoader, "getTestCaseNames", getOrderedTestCaseNames)

class MyMeta(type):
    def __new__(klass, name, base, klassdict):
#        print(klass, name, base, klassdict)
        klassobj = super().__new__(klass, name, base, klassdict)
        klassobj._ordered = klassdict
        return klassobj

    @classmethod
    def __prepare__(klass, name, bases):
#        print("Invoked __prepare__ for klass", klass, name, bases)
        return collections.OrderedDict()


class Test(unittest.TestCase, metaclass=MyMeta):
    def setUp(self):
        print("IN setup")

    def testc(self):
        print("testc")

    def testb(self):
        print("testb")

    def testa(self):
        print("testa")

    def test_cleanup(self):
	    pass	

    def tearDown(self):
        print("In teardown")

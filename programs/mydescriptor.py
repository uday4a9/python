#! /usr/bin/env /usr/bin/python3


class Descriptor:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, cls):
        print("Get", self.name)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print("Set", self.name, value)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print("Delete", self.name)
        del instance.__dict__[self.name]

class Student:
    """
    Need to create a class which should accept 3 args
    """
    _fields = ["name", "age", "sid"]
    def __init__(self, *args):
        assert len(args) == len(Student._fields), "Pass atleast 3 arguments"
        for key, value in zip(Student._fields, args):
            setattr(self, key, value)

    def __str__(self):
        for key in Student._fields:
            print("{0} : {1}".format(key, self.__dict__[key]), end=", ")
        return ""


class Structure:
    _fields = ['name', 'share', 'price']

    def __init__(self, *args):
        print("Structure init", args)
        for key, value in zip(Structure._fields, args):
            setattr(self, key, value)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']

    # redefining the meaning of .shares attribute in this class
    shares = Descriptor('shares')   # <==> Descriptor.__init__(shares, name='shares')
    # When we created an object for Stock class
    # s = Stock()
    # s.shares      <==> Descriptor.__get__(shares, s, Stock)
    # s.shares = 50 <==> Descriptor.__set__(shares, s, 50)
    # del s.share   <==> Descriptor.__delete__(shares, s)


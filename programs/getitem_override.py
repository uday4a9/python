#! /usr/bin/env /usr/bin/python

class A(object):
    def __init__(self, name="Hello", age=5):
        self.name = name
        self.age = age

    def __getitem__(self, key): 
        print (key)
        key1, key2 = key
        print(key1, key2)
        #return self.__dict__[key]


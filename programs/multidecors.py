#! /usr/bin/env /usr/bin/python3.5

def fun():
    print("IN fun method")

def fun(func):
    def inner(*args, **kwargs):
        print("inner from fun function")
        func(*args, **kwargs)
        print("Done with inner fun function")
    return inner

def foo(func):
    def inner(*args, **kwargs):
        print("inner from foo function")
        func(*args, **kwargs)
        print("Done with inner foo function")
    return inner

@foo
@fun
def goo():
    print("In goo method")

goo()

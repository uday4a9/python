#! /usr/bin/env /usr/bin/python3

# Always try to see things in interactive mode.
# Which gives clear desc about how they works.

# python3 -i YYYYY.py

def simplecoroutine():
    print("Corutine started")
    x = yield
    if x is None:
        print("Please pass a value to me, using send method")
        return
    x = x * x
    print("After yielding", x ,"and stops execution of coroutine")

def croutine(a):
    print("Value of a : ",a)
    b = yield a
    print("Values of a and b : ", a, b)
    c = yield a + b
    print("Values of a, b and c : ", a, b, c)

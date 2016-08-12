#! /usr/bin/env /usr/bin/python3

def fib():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y

def gfib():
    yield from fib() 

def rfib(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x

# run rfib(40)
# run
# 

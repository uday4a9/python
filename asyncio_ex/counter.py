#! /usr/bin/env /usr/bin/python

def countdown(val):
    while val > 0:
        yield val
        val -= 1

c = countdown(5)

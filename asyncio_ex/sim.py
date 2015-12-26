#! /usr/bin/env /usr/bin/python3

from time import sleep

def compute(x, y):
    print("Compute %s + %s ..." %(x, y))
    sleep(1.0)
    return x + y


def print_sum(x, y):
    result = compute(x, y)
    print("%s + %s = %s" %(x, y, result))

print_sum(1, 2)

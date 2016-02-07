#! /usr/bin/env /usr/bin/python3

import time

def interval(func):
    def inner_calc(*args):
        before = time.time()
        res = func(*args)
        diff = "%.08f"%(time.time() - before)
        name = func.__name__
        print(name + "(" + str(*args) + ") =", res, "took :", diff, "secs")
        return res
    return inner_calc

@interval
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

def main():
    print("In main program..")

if __name__ == '__main__':
    main()
    #print("Res : ", factorial(5))
    factorial(5)

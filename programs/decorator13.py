#! /usr/bin/env /usr/bin/python3

register = []

def decorate(fun):
    print("Running decorator")
    def inner():
        register.append(fun.__name__)
        print("Under inner decorator, invoked from :", fun.__name__)
        fun()
    return inner 

@decorate
def foo():
    print("In foo function\n")
#main = decorate(main)

@decorate
def goo():
    print("In goo function\n")

def status():
    print("Invoked by:", register, "functions")


def average():
    vals = []
    def inner_avg(val):
        vals.append(val)
        return sum(vals) / len(vals)
    return inner_avg

class Average(object):
    def __init__(self):
        self._values = []

    def __call__(self, val):
        self._values.append(val)
        return sum(self._values) / len(self._values)

if __name__ == '__main__':
    foo()
    goo()
    status()

    # Here Both average function and Average callases does the same job
    print("")
    avg = average()
    print("Callable func:", avg(10))
    print("Callable func:", avg(11))
    print("Callable func:", avg(12))

    print("")
    cavg = Average()
    print("Callable obj:", cavg(10))
    print("Callable obj:", cavg(11))
    print("Callable obj:", cavg(12))

    print("\nTypes :")
    print("type(avg)  :", type(avg), avg)
    print("type(cavg) :", type(cavg), cavg)

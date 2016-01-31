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
    # Here, values is a mutable type, so we can easily extend the
    # way of using in below inner function.
    # If we are trying to use immutable variables like numbers, strings
    # This type of code will not work.
    # This mutable type values can be change dby using
    # <average objecta>.__closure__[0].cell_contents
    # can be modified... This can cause for changing the variables
    vals = []
    def inner_avg(val):
        vals.append(val)
        return sum(vals) / len(vals)
    return inner_avg

def nlaverage():
    # Here update the total directly instead of saving in a list
    # This depicts the usage of nonlocal keyword in python
    count = 0
    total = 0

    def inner_avg(val):
        nonlocal count, total
        count += 1
        total += val
        return total / count
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


    print("")
    navg = nlaverage()
    print("non local Callable obj:", navg(10))
    print("non local Callable obj:", navg(11))
    print("non local Callable obj:", navg(12))

    print("\nTypes :")
    print("type(avg)  :", type(avg), avg)
    print("type(cavg) :", type(cavg), cavg)
    print("type(navg) :", type(navg), navg)

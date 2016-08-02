#! /usr/bin/env /usr/bin/python

def decor(func):
    print("Global DECOR")
    def _inner(*args, **kwargs):
        print(args, kwargs, func.__name__)
        func(*args, **kwargs)
    return _inner

class Klass:
    def __init__(self, a=12, b=23):
        self.a = a
        self.b = b
        self.dpc = True

    def dekor(func):
        print("in method dekor")
        def inner(*args, **kwargs):
            if not args[0].dpc:
                print("DPC TRUE retruning func")
                func(*args, **kwargs)
                return
            else:
                print("In klass decor method, process the results here")
                #print(args, kwargs, func.__name__)
                func(*args, **kwargs)
        return inner

    @dekor
    def display(self):
        print("In display method of klass")
    


if __name__ == '__main__':
    obj = Klass()
    obj.display()

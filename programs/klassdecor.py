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

    def dekor(self):
        print("in method dekor")
        def inner(*args, **kwargs):
            if not args[0].dpc:
                print("DPC TRUE retruning func")
                self(*args, **kwargs)
            else:
                print("In klass decor method, process the results here")
                #print(args, kwargs, func.__name__)
                self(*args, **kwargs)
        return inner

    @dekor
    def display(self, _val1, _val2):
        print("In display method of klass", _val1, _val2)
    


if __name__ == '__main__':
    obj = Klass()
    obj.display(-12, -32)

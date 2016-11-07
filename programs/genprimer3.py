#! /usr/bin/env /usr/bin/python

"""
This whole module details the usage of yield with generators.
"""

from functools import wraps
import inspect

def genprimer(function):
    """
    1.  
        This decorator always tries to create the object for generator function
        and simply applies the next on the particular genrator object. 
        So, that when any funciton makes use of this funciton as decorator,
        corresponding calls directly can make(as .send, with out sending None or
        advancing the position by one)
    2. 
        We've used the @wraps function below, not to loose the documentaion string
        on the object invoker (or) whomever used this genprimer as decorator for that.

    """
    @wraps(function)
    def dispatcher(*args, **kwargs):
        genobj = function(*args, **kwargs)
        if not inspect.isgenerator(genobj):
            raise Exception("Please pass only Generator objects, to advance the operation")
        next(genobj)
        return genobj
    return dispatcher


@genprimer
def consumer():
    """
    1.  
        This is a consumer function, and it is ready to accept/consume the values.
    2.  
        If we're not using the @genprimer decorator, Need to advance the object created
        for this consumer. otherwise it leads to an error by saying expected to send a 
        None value for first time created a generator object.
        Ex:
            c = consumer()
            next(c)
    """
    while True:
        value =  yield
        print("Got value:", value)

def fun():
    pass

def producer(gen):
    """
    1.
        This is a produer, whic to produce the values.
    """
    for i in range(5):
        gen.send(i)

if __name__ == '__main__':
    fun()
    cgen = consumer()
    producer(cgen)

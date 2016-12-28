#! /usr/bin/env /usr/bin/python3.5

import sys
from collections import abc
import doctest

class FlattenJson:
    """
    This will flatten only one level of json 
#    >>> print(d)
#    <FlattenJson : {'h23': [12, 'hell'], 'hi': 'Newly entered', 12: 'hello', 'yes': {'val': 12, 'new': 34}}>
    >>> d.h23
    [12, 'hell']
    >>> d.h23[0]
    12
    >>> d.h23[1]
    'hell'
    >>> d.yes
    {'val': 12, 'new': 34}
    >>> d.yes.val
    Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
    AttributeError: 'dict' object has no attribute 'val'

    """
    def __init__(self, hashmap):
        self._data = dict(hashmap)

    def __repr__(self):
        return "<{0} : {1}>".format(self.__class__.__qualname__, hex(id(self)))

    def __str__(self):
        return "<{0} : {1}>".format(self.__class__.__qualname__, self._data)

    def __getattr__(self, node):
        #print(hasattr(self._data, node))
        #print(self._data[node])
        if hasattr(self._data, node):
            return getattr(self._data, node)
        else:
            try:
                return FlattenJson.build(self._data[node])
            except KeyError:
                return None

    @classmethod
    def build(cls, node):
        if isinstance(node, abc.Mapping):
            return node
        elif isinstance(node, abc.MutableSequence):
            #print([cls.build(item) for item in node])
            return [cls.build(item) for item in node]
        else:
            return node 

if __name__ == '__main__':
    fjson = {12 : "hello",
             'h23' : [12, "hell"],
             "hi" : "Newly entered",
             "yes" : {
                        "val" : 12,
                        "new" : 34
                     }
             }
    d = FlattenJson(fjson)
    doctest.testmod()


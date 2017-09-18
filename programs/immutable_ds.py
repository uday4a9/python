
from functools import wraps

def is_immutable(self, *args, **kwargs):
    raise TypeError('%r objects are immutable' % self.__class__.__name__)

def immutables_to_typeerror(*arguments):
    def decor(klass):
        for method in arguments:
            setattr(klass, method, is_immutable)
    
        @wraps(klass)
        def inner(*args, **kwargs):
            return klass(*args, **kwargs)
        return inner
    return decor

@immutables_to_typeerror("update", "__setitem__", "__delitem__",
                         "pop", "popitem", "setdefault", "copy")
class ImmutableDict(dict):
    """
        This is immutable dict type. So in place changes are not allowed.
    """
    def __init__(self, obj):
        if not isinstance(obj, dict):
            raise ValueError("Pass only dict type object")
        super().update(obj)

    def __repr__(self):
        return '%s(%s)' % (
            self.__class__.__name__,
            dict.__repr__(self),
        )

@immutables_to_typeerror("__setitem__", "__delitem__", "sort",
                         "append", "clear", "copy", "extend", 
                         "pop", "insert", "remove", "reverse")
class ImmutableList(list):
    """
        This is immutable list type. So in place changes are not allowed.
    """    
    def __init__(self, obj):
        if not isinstance(obj, list):
            raise ValueError("Pass only list type object")
        super().__init__(obj)
        
    def __repr__(self):
        return '%s(%s)' % (
            self.__class__.__name__,
            list.__repr__(self),
        )        

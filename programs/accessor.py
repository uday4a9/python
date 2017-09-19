import collections 

class Accessor:
    def __init__(self, obj):
#        if not isinstance(obj, dict):
#            raise ValueError("pass dict object only")
        self.__dict = obj

    def __getattr__(self, key):
        try:
            type_ = self._Accessor__dict[key]
        except KeyError:
           raise
        
        if isinstance(type_, collections.MutableSequence):
            return (self._Accessor__dict[key])
            #try:
            #    index = int(key)
            #    return Accessor(self._Accessor__dict[key])
            #except Exception:
            #    raise
        elif isinstance(type_, collections.MutableMapping):
            return Accessor(self._Accessor__dict[key])
        else:
            return self._Accessor__dict[key]


if __name__ == '__main__':
    ac = Accessor({"hello" : 12, 
                   "hi" : 32,
                   "ad" : {"qwerty": 321,
                           "asdf" : 213
                    },
                   "ip" : [12, 23, 34]
                 })

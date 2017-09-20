import collections 

class Accessor:
    def __init__(self, obj):
        self.__iobj = obj
    
    def __repr__(self):
        return "<{0}: {1}>".format(self.__class__.__name__,
                                   hex(id(self)))

    def __len__(self):
        return len(self.__iobj)

    def as_raw(self):
        return self.__iobj

    def __getitem__(self, ind):
        return (self._Accessor__iobj[int(ind)])

    def __getattr__(self, key):
        try:
            type_ = self._Accessor__iobj[key]
        except KeyError:
           raise
        
        if isinstance(type_, collections.MutableSequence):
            return Accessor([Accessor(item) 
                             for item in self._Accessor__iobj[key]])
        return Accessor(self._Accessor__iobj[key])


if __name__ == '__main__':
    ac = Accessor({"hello" : 12, 
                   "hi" : 32,
                   "ad" : {"qwerty": 321,
                           "asdf" : 213
                    },
                   "ip" : [12, 23, 34],
                   "num" : [{"one": 1},
                            {"two": 2},
                            {"three": {
                                "four":4
                                }
                            }
                    ],
                   "yes": "it is here"
                 })

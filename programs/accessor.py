import collections 

class Accessor:
    def __init__(self, obj):
        self.__iobj = obj
    
    def __repr__(self):
        return "<{0}: {1}>".format(self.__class__.__name__,
                                   hex(id(self)))

    def __iter__(self):
        return iter(self.__iobj)

    def __len__(self):
        return len(self.__iobj)

    def __getitem__(self, ind):
        return (self.__iobj[int(ind)])

    def __getattr__(self, key):
        try:
            type_ = self.__iobj[key]
        except KeyError:
            raise
        
        if isinstance(type_, collections.MutableSequence):
            return Accessor([Accessor(item) 
                             for item in self.__iobj[key]])
        return Accessor(self.__iobj[key])
    
    @classmethod
    def raw_obj_traverser(cls, _obj, path="obj"):
        if not path.startswith("obj"):
            raise Exception("please start it with `obj`")
        obj = cls(_obj)
        return eval(path)
    
    @staticmethod
    def klass_obj_traverser(klsobj, path="obj"):
        if not isinstance(klsobj, Accessor):
            raise ValueError("First argument should be of `Accessor` instance type")
        
        if not path.startswith("obj"):
            raise Exception("please start it with `obj`")
        obj = klsobj
        return eval(path)

    def as_raw(self):
        if isinstance(self.__iobj, collections.MutableSequence):
            return [item.as_raw() for item in self.__iobj]
        return self.__iobj
    
    @staticmethod
    def list_traverser(klsobj, first_path="obj"):
        if not isinstance(klsobj, Accessor):
            raise ValueError("First argument should be of `Accessor` instance type")
        
        if not first_path.startswith("obj"):
            raise Exception("first_path should be started with `obj`")

        res = []
        for item in klsobj:
            obj = item
            res.append(eval(first_path))           
        return Accessor(res)


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
    print(ac.hello)
    print(ac.hello.as_raw())
    print(ac.num)
    print(ac.num.as_raw())
    print(ac.num[-1].three.four)
    print(ac.num[-1].three.four.as_raw())

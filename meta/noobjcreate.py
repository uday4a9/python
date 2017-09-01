
class NoInstanceClass(type):
    def __new__(klass, name, bases, klassdict):
        print(4, "IN __new__ of", klass)
        print(klass, name, bases, klassdict, sep="<=>")
        return super().__new__(klass, name, bases, klassdict)

#    def __init__(self, name, bases, klassdict):
#        print("IN BASE __init__")
#        print(self, name, bases, klassdict, sep="\n")
#
#    def __call__(self):
#        raise ValueError

    def value(self):
        print(self, "VAL... val...")

class NewMeta(NoInstanceClass):
    def __new__(klass, name, bases, klassdict):
        print(20, "IN __new__ of", klass)
        return super().__new__(klass, name, bases, klassdict)

    def value(self):
        print(self, "IN NEW VALUE.. VAL")
        super().value()

print("%%" * 15)
class Main(metaclass=NewMeta):
    """
        This class contains only one static method. So inorder to use that,
    No need to create an object and invoke it.
    """
    @staticmethod
    def smethod():
        print("In static method of class")

if __name__ == '__main__':
    print(dir(Main))
    m = Main()
    #m()
    #Main.smethod()
    pass

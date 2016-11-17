#! /usr/bin/env /usr/bin/python

class Base(object):
    _fields = ["Bhello", "Bhi"]
    def __init__(self):
        self.data = "Hello"
        print("Base")

    def disp(self):
        print("In base disp method")


class Der1(Base):
    _fields = ["DHello", "Dhi"]
    def __init__(self):
        super(Der1, self).__init__()
        #Base.__init__(self)
        print("Der1")

    def disp(self):
        print("In der disp")
        Base.disp(self)

if __name__ == '__main__':
    pass
    #b = Base()
    #d = Der1()

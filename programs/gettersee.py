class Dummy:
    def __init__(self, val):
        self.val = val

d = Dummy(123)
#print("Val:", d.val)

# This instance attribute not available
#print(d.a) # This line caused for AttributeError


###################################################
class Dummy1:
    def __init__(self, val):
        self.val = val

    def __getattr__(self, key):
        """If any instance attribute is missing,
        then attribute access will leads here."""
        return self.__dict__.get(key)

d1 = Dummy1(123)
#print("Val:", d1.val)
#print("instance attribute:", d1.a)

####################################################
# for all instance attribute access call directly 
# goes to __getattribute__. if the instance attribute
# not exists then it dipatches call to __getattr__
####################################################
class Dummy2:
    def __init__(self, val):
        self.val = val

    def __getattribute__(self, key):
        print("All Here")
        return super().__getattribute__(key)
    
    def __getattr__(self, key):
        print("missed instance attributes here")
        self.__dict__[key] = -123123
        return -123123

d2 = Dummy2(1234)
#print("Val:", d2.val)
print("Val:", d2.v)

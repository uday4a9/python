#! /usr/bin/env /usr/bin/python3

def foo():
    for _ in range(10):
        i = yield
        print("Value :", i)

if __name__ == '__main__':
    f = foo()
    next(f)
    # For above foo generator always send included
    # None value also.
    # None, 0 to 9 will be correct(total = 10)
    # but here, range(10) means we'll send 11 values
        
    for i in range(10):
        try:
            f.send(i)
        except StopIteration:
            break

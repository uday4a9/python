#! /usr/bin/env /usr/bin/python


def coroutine(fun):
    def start(*args, **kwargs):
        cr = fun(*args, **kwargs)
        cr.next()
        return cr
    return start

@coroutine
def grep(pattern):
    # If below line enabled then no need to send the None value to this gen
    #   g.send(None)
    #      (or)
    #   g.next();  for first time
    print "Looking for : ", pattern
    try:
        while True:
            line = yield
            if line and pattern in line:
                print line,
    except GeneratorExit:   # To handle g.close()
        print "Bye, Stopping from the program"


g = grep("python")
# But sending an argument is always we can't remeber
# So, write a decorator to send None
# g.send(None)

# To close the generator pass g.close()

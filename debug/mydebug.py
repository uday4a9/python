#! /usr/bin/env /usr/bin/python

import sys

def tracer1(frame, event, args):
    #print dir(frame)
    #print help(frame)
    #raw_input("Enter some thing")
    #pprint (frame.f_code)
    #print frame.f_locals
    #print frame.f_globals
    #print "%d: %s"%(frame.f_lineno, event)
    #print "ARGS:", args
    #pprint (frame)
    return trace_exceptions

def tracer(frame, event, args):
    #print dir(frame)
    #print help(frame)
    #raw_input("Enter some thing")
    #print frame.f_locals
    #print frame.f_globals
    #print "%d: %s"%(frame.f_lineno, event)
    #print "ARGS:", args
    #pprint (frame)
    return trace_exceptions

def trace_exceptions(frame, event, arg):
    if event != 'exception':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    exc_type, exc_value, exc_traceback = arg
    print 'Exception : %s occured in %s file at line no %s' % \
        (exc_type.__name__, filename, line_no)
#    print 'Tracing exception: %s "%s" on line %s of %s' % \
#        (exc_type.__name__, exc_value, line_no, func_name)
    sys.exit(1)

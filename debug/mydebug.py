#! /usr/bin/env /usr/bin/python

import sys
import os

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
    #print os.getcwd()
    #print filename, os.path.realpath(filename)
    #print os.path.dirname(filename)
    if os.getcwd() not in os.path.realpath(filename):
        # if the file is in current directory then only,
	#handle the exception otherwise never touch any
	# THis can be avoiding if there is any exceptio hnadling in
	# default file in python
        return
    print 'Exception : %s occured in %s file at line no %s' % \
        (exc_type.__name__, filename, line_no)
#    print 'Tracing exception: %s "%s" on line %s of %s' % \
#        (exc_type.__name__, exc_value, line_no, func_name)
    sys.exit(1)

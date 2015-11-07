#! /usr/bin/python

import filecmp
import difflib
import sys
import time
import os
from pprint import pprint
import argparse
import sqlite3
import getpass


def configdiffer(fromfile, tofile, db):
#    lines1 = open(sys.argv[1], 'r').readlines()
#    lines2 = open(sys.argv[2], 'r').readlines()
    fromdate = time.ctime(os.stat(fromfile).st_mtime)
    todate = time.ctime(os.stat(tofile).st_mtime)
    fromlines = open(fromfile, 'U').readlines()
    tolines = open(tofile, 'U').readlines()

    #print lines1, lines2
    #pprint(lines1)
    #pprint(lines2)

    # all diff_lib.* functions are generators
    #for line in difflib.context_diff(fromlines, tolines, fromfile, tofile):
    #        print line.rstrip('\n')
    #        ischanged = True

    diff = list(difflib.context_diff(fromlines, tolines, fromfile, tofile))

    user = getpass.getuser()
    site = fromfile.split('/')[2] 
    ischanged = 1 if len(diff) else 0 
    
    if not ischanged:
        print "No new changes in:", tofile
	stamp = ''
	diff = ''
    else:
	stamp = time.strftime("%d %b %Y %H:%M:%S")
	diff = ''.join(diff)
	os.system('cp %s .'%(tofile))
	print "Local config file replaceed with rmeote svn config file"

    # Create DB if not avaiable
    if not os.path.isfile(db):
        print "db creating for first time"
	con = sqlite3.connect(db)
	cursor = con.cursor()
	cursor.execute('''
	    CREATE TABLE diffs(id TEXT, datacenter TEXT,
	    ischange INTEGER, date TEXT, diff TEXT)
	    ''')
        cursor.execute('''INSERT INTO diffs(id, datacenter, ischange, date, diff)
                  VALUES(?,?,?,?,?)''', (user, site, ischanged, stamp, diff))
	con.commit()
    else:
        con = sqlite3.connect(db)
        cursor = con.cursor()
        cursor.execute('''INSERT INTO diffs(id, datacenter, ischange, date, diff)
                  VALUES(?,?,?,?,?)''', (user, site, ischanged, stamp, diff))
        con.commit()
        

    #diff = difflib.ndiff(lines1, lines2)
    #diff = list(diff)
    #print ''.join(difflib.restore(diff, 1))

    #for i in difflib.ndiff(lines1, lines2):
    #    if i[:1] == '-':
    #        print i.rstrip('\n')

def parser():
    """
       Parsing the data given from command line.
    """
    parse = argparse.ArgumentParser(prog=sys.argv[0])
    parse.add_argument('site_config', nargs=1, metavar=('site_config.ini'),
                     help="pass the local config.ini file path")
    parse.add_argument('remote_config', nargs=1, metavar=('svn_config.ini'),
                     help="pass the svn config.ini file path")
    parse.add_argument('-db','--database', nargs=1, required=False, 
                     metavar=('exmpale.db'), default=["datacenter.db"],
                     help="""pass the databse name to store the table if needed. 
		     else, data will be written to datacenter.db""")
    args = parse.parse_args()
    Dict = vars(args)
    configdiffer(Dict['site_config'][0], Dict['remote_config'][0], Dict['database'][0])

if __name__ == '__main__':
    parser()

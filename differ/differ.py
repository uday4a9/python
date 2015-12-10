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
import subprocess

import mydebug
sys.settrace(mydebug.tracer)


svnremote = "svn export http://tblubttrs01apdvg.tdc.vzwcorp.com:1080/svn/EnvironmentSpecificConfigs/branches/%s/Prod/%s/config.ini"
svnlocal = "/usagebrkr/%s/mz/config.ini"


def configdiffer(Dict):
#    lines1 = open(sys.argv[1], 'r').readlines()
#    lines2 = open(sys.argv[2], 'r').readlines()
    fromfile = svnlocal%(Dict['datacenter'])
    tofile = pull(Dict)
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
	subprocess.call('cp %s %s'%(tofile, fromfile), shell=True)
	print "Local config file replaced with remote svn config file"

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

def pull(Dict):
    """ pulling config.ini file form remote server for future comaprison """
    command = svnremote%(Dict['datacenter'], Dict['release'])
    print command
    subprocess.check_output(command, shell=True)
    #subprocess.check_output(svnremote%(Dict['datacenter'], Dict['release']), shell=True)
    return os.path.join(os.getcwd(), 'config.ini')

def parser():
    """
       Parsing the data given from command line.
    """
    parse = argparse.ArgumentParser(prog=sys.argv[0], 
                                   description = """ This program needs pasword authentication.
				   so, please be attentive.""")
    parse.add_argument('-rel', '--release', nargs=1, metavar=('release'), required=True,
                     help="pass the release name to fetch the exact svn repo")
    parse.add_argument('-dc', '--datacenter', nargs=1, metavar=('Data_center'), required=True,
                     help="Pass the datacenter name, To fetch the svn config.ini")
    parse.add_argument('-db','--database', nargs=1, required=True, metavar=('exmpale.db'),
                     help='pass the databse name to store the diff table')
    args = parse.parse_args()
    Dict = vars(args)
    for key in Dict:
        Dict[key] = Dict[key][0]
    configdiffer(Dict)

if __name__ == '__main__':
    parser()

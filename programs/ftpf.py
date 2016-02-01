#! /usr/bin/env /usr/bin/python

import sys
import ftplib
import argparse
import time
import os

total = 0
def checker(block):
    # blocksize in bytes
    global  total
    total += 8192


def process(param):
    # Create ftp connection
    global total
    try:
        ftp = ftplib.FTP(param['address'])
    except Exception, emsg:
        print("Exception while connecting: " + str(emsg[0]))
        sys.exit(1)

    try:
        ftp.login(param['username'], param['passwd'])
    except Exception, emsg:
        print("Exception while login : " + str(emsg[0]))
        sys.exit(1)
    print("LOGIN successful")

    filename = param['file']

    if param['sub'] == 'DL':
        try:
            ftp.cwd(param['directory'])
            print("changing directory succesfully")
            before = time.time()
            #ftp.retrbinary('RETR ' + filename, checker, 8192)
            ftp.retrbinary('RETR ' + filename, open(filename, 'wb').write)
            after= time.time()
        except Exception, emsg:
            print("Exception caught while downloading : " + str(emsg[0]))
            sys.exit(1)
        print("file download succesful")
        total = os.path.getsize(filename)
    elif param['sub'] == 'UL':
        try:
            ftp.cwd(param['directory'])
            print("changing directory succesfully")
            before = time.time()
            ftp.storbinary('STOR ' + filename, open(filename, 'rb'), 8192, checker)
            after= time.time()
        except Exception, emsg:
            print("Exception caught while uploading : " + str(emsg[0]))
            sys.exit(1)
        print("file upload successful")

    diff  = after - before
    print("%d bytes transfer successful in %0.8fs; Throughput : %0.4fKBps"%(total, diff, (total) / (round(diff, 5) * 1000)))
    ftp.quit()


def parser():
    parse = argparse.ArgumentParser(description="FTP")
    parse.add_argument('address', nargs=1,
            help="Pass the ip/target domain name to specify")
    parse.add_argument('-u', '--username', nargs=1, required=True,
            help="Pass the username")
    parse.add_argument('-p', '--passwd', nargs=1, required=True,
            help="Pass the password")
    parse.add_argument('-f', '--file', nargs=1, required=True,
            help="Pass the filename")
    parse.add_argument('-d', '--directory', nargs=1, default=["."],
            help="Need to pass this, When need of changing dir")

    subparser = parse.add_subparsers(dest="sub", help="Adding the subparsers")

    download = subparser.add_parser('DL', help="choose download")
    upload = subparser.add_parser('UL', help="choose upload")

    args = parse.parse_args()
    param = vars(args)

    for key in param:
        if key != "sub":
            param[key] = param[key][0]
    #print(param)
    process(param)

if __name__ == '__main__':
    parser()

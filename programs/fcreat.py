#! /usr/bin/env /usr/bin/python

"""
This file helps to create a file wiht given size the same name.
Ex:
    python ./fcreat.py 10M
    python ./fcreat.py 10M --out ~/Desktop
"""
import argparse
import os
import re

sizemapper = {  'B' : 1,
                'K' : 1024,
                'M' : 1024 * 1024,
                'G' : 1024 * 1024 * 1024
             }

def createfile(sz, pth):
    print("{0} size file created with name {1}".format(sz, pth))
    fil = open(pth, 'w')
    fil.seek(sz - 1) # seek the file pointer to last but one pos
    fil.write('a')   # Write one random character  
    fil.close()      # flush the opened buffers

def create_file(fd):
    size = fd['fsize'].upper()
    opdir = fd['out']
    try:
        sizeargs = list(re.findall(r'(\d+)(\w){1}$', size)[0])
    except IndexError:
        print("Invalid args for fsize: " + size)
        return -1

    #convert first argument to int
    sizeargs[0] = int(sizeargs[0])
    #print(sizeargs)

    createfile(sizeargs[0] * sizemapper[sizeargs[1]],
               os.path.join(opdir, size))

def parsee():
    parser = argparse.ArgumentParser(description="File creator",
            epilog=""" This program creates a file, with needed
            size.
            1b -> 1byte size file
            1k -> 1kilobyte size file
            1M -> 1MegaByte size file
            """)
    parser.add_argument('fsize', metavar='fsize', type=str,
            default='1b', nargs='?',
            help="create files size : B, K, M, G.\
            These are not case insensitive.")
    parser.add_argument('-o', '--out', nargs='?', default='.',
            help="Need to pass the filename, else create in current\
                  directory. with fsize argument")
    args = parser.parse_args()
    create_file(vars(args))

if __name__ == '__main__':
    parsee()

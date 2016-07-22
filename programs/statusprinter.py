#! /usr/bin/env /usr/bin/python

import sys
import time

def main():
    i = 0
    sys.stdout.write('[')
    while i < 5:
        i += 1
        sys.stdout.write('%]')
        sys.stdout.write('\b')
        sys.stdout.flush()
        time.sleep(.5)
    print("")


def man():
    sys.stdout.write('[  ')
    while True:
        for i in "-\|/-":
            sys.stdout.write(i)
            sys.stdout.write('\b')
            sys.stdout.flush()
            time.sleep(.03)

if __name__ == '__main__':
    man()

#! /usr/bin/env /usr/bin/python

import sys
import time

def main():
    i = 0
    sys.stdout.write('[')
    while i < 255:
        i += 1
        sys.stdout.write('%]')
        sys.stdout.write('\b')
        sys.stdout.flush()
        time.sleep(.3)
    print("")


if __name__ == '__main__':
    main()

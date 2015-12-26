#! /usr/bin/env /usr/bin/python

import sys

status = (int(str(sys.version_info.major) + str(sys.version_info.minor)) >= 34)

#print(status)

try:
    assert status, "Upgrade the version to 3.4 or more"
except AssertionError as emsg:
    print(emsg)
    sys.exit(1)

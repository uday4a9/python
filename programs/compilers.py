#! /usr/bin/env /usr/bin/python3

import re
from collections import namedtuple

tokens = [
        r'(?P<NUMBER>\d+)',
        r'(?P<PLUS>\+)',
        r'(?P<MINUS>-)',
        r'(?P<TIMES>\*)',
        r'(?P<DIVIDE>/)',
        r'(?P<WS>\s+)'
         ]

master_re = re.compile('|'.join(tokens))

#print(master_re)

text = "2 + 3 * 4 - 5"
#text = "1 % 2 + 3 * 4 - 5"

# Python RE.scanner method
# this scanner method process one token at a time from above tikenizer list.
s = master_re.scanner(text)

#for _ in range(len(text)):
#    if s.match != " ":
#        print("Token : ", s.match())


match = master_re.match(text)
Token = namedtuple('Token', ['type', 'value'])
def tokenize(text):
    scan = master_re.scanner(text)
    return (Token(m.lastgroup, m.group()) for m in iter(scan.match, None) if m.lastgroup != 'WS')

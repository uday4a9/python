import re
from collections import namedtuple

tokens = [
        r'(?P<NUMBER>\d+)',
        r'(?P<PLUS>\+)',
        r'(?P<MINUS>-)',
        r'(?P<TIMES>\*)',
        r'(?P<DIVIDE>/)',
        r'(?P<WS>\s+)',
        r'(?P<POW>\^)',
        r'(?P<LP>\()',
        r'(?P<RP>\))'
         ]

master_re = re.compile('|'.join(tokens))

#print(master_re)

text = "2 + 3 * 4 - 5"
#text = "1 % 2 + 3 * 4 - 5"

# Python RE.scanner method
# this scanner method process one token at a time from above tokenizer list.
s = master_re.scanner(text)

#for _ in range(len(text)):
#    if s.match != " ":
#        print("Token : ", s.match())


match = master_re.match(text)
Token = namedtuple('Token', ['type', 'value'])
def tokenize(text):
    scan = master_re.scanner(text)
    return (Token(m.lastgroup, m.group()) for m in iter(scan.match, None) if m.lastgroup != 'WS')

inp = '36+6-6*412-9+26-9110/10*654+8*855'
inp = '2^(3^2)*(8+2*(3+1-2*(8+20)/4))/4-1'
inp = '(2^3)^2'
print(list(tokenize(inp)))

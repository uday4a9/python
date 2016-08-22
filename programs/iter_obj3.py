#! /usr/bin/env /usr/bin/python3

"""
python follows two types of iterators
1.  for i in S:
        print(i)
2.  S[0], S[1]
"""

import re

RE_WORD = re.compile(r'\w+')

class Sentence:
    def __init__(self, line):
        self.words = RE_WORD.findall(line)
        self._len = len(self.words)
        self._cnt = 0

# Below teo methods are to create generators only

    def __iter__(self):         # converting to iter
        for word in self.words:
            yield word

    def __getitem__(self, ind): # Support for indexing
        return self.words[ind]
    
    def __next__(self):
        if self._cnt >= self._len:
            raise StopIteration
        self._cnt += 1
        return self.words[self._cnt - 1]

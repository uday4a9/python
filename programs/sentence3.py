#! /usr/bin/env /usr/bin/python3

import reprlib
import re

RE_WORD = re.compile('\w+')

class Sentence(object):
    def __init__(self, sentence):
        self.__sentence = sentence
        self.__words = RE_WORD.findall(sentence)

    def __repr__(self):
        return ('Sentence : %s'%(reprlib.repr(self.__sentence)))

    def __getitem__(self, index):
        return self.__words[index]

    def __len__(self):
        return len(self.__words)

if __name__ =='__main__':
    s = Sentence("Hi, How are you ???")
    print(len(s))
    for i in s:
        print(i)

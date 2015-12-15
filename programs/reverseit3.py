#! /usr/bin/env /usr/bin/python3

class NewIter(object):
    '''
     This class creates new iterator which have reverse iteration protocol.
    Here we overloaded with newly declared __reverse__ operator.
    '''

    def __init__(self, start):
        print("Created a new iterator")
        self.start = start

    def __iter__(self):
        ''' Forward iterator'''
        print("Forward Iterator")
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        ''' Reversed iterator '''
        print("Reverse Iterator")
        n = 1
        while n <= self.start:
            yield n
            n += 1

if __name__ == '__main__':
    l = NewIter(5)

    for element in l:
        print(element)

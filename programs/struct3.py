#! /usr/bin/env /usr/bin/python3


class Node():
    def __init__(self, value):
        print ("Node created successfully..")
        self._value = value
        self._child = []

    def __repr__(self):
        return "Node : {!r}".format(self._value)



if __name__ == '__main__':
    root = Node(0)
    left = Node(1)
    right = Node(2)
    print (root)
    print (left)
    print (right)

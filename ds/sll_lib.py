from functools import wraps
import sys

def read_value():
    a = input("Enter a value to insert in list: ")
    return a

class Node:
    _value = 123123
    __v2 = 321
    def __init__(self, val):
        self._data = val
        self._next = None
        self.__v3 = 123

    def get_value(self):
        return self._data

    def get_next(self):
        return self._next

    def set_next(self, new):
        self._next = new

class LinkedList:
    """
        All methods which are going to exposed to user under this class,
    should use the prefix as `sll_`.
    """
    def __init__(self, front=None):
        self.front = front

    def sll_insert_at_begin(self):
        node = Node(read_value())
        node.set_next(self.front)
        self.front = node
        self.sll_display()

    def sll_insert_at_end(self):
        node = Node(read_value())
        if not self.front:
            self.front = node
        else:
            temp = self.front
            while temp.get_next():
                temp = temp.get_next()
            temp.set_next(node)
        self.sll_display()

    def sll_insert_at_end_rec(self):
        pass

    def empty_check(self):
        @wraps
        def inner(*args, **kwargs):
            print("inner", self, args, kwargs)
        return inner

    def sll_display(self):
        if not self.front:
            print("List empty, Nothing to display")
            return
        temp = self.front
        while temp:
            print(temp.get_value(), end="->")
            temp = temp.get_next()
        print("NULL")

    def sll_delete_at_begin(self):
        if not self.front:
            print("List empty, Nothing to delete")
            return
        node = self.front
        self.front = node.get_next()
        node.set_next(None)
        del node
        self.sll_display()

    def sll_delete_at_end(self):
        if not self.front:
            print("List empty, Nothing to delete")
            return

        prv = self.front
        nxt = prv.get_next()

        if not nxt:
            del self.front
            self.front=None
            self.sll_display()
            return

        while nxt and nxt.get_next():
            prv = nxt
            nxt = nxt.get_next()
        prv.set_next(None)
        del nxt
        self.sll_display()

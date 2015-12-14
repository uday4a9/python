#! /usr/bin/env /usr/bin/python3


class Node(object):
    def __init__(self, value):
        #print ("Node created successfully..")
        self._value = value
        self._child = []
        self._len = 0

    def __repr__(self):
        return "Node : {!r}".format(self._value)

    def add_child(self, child):
        self._len += 1
        self._child.append(child)

    def __iter__(self):
        '''
         To create iterator object on top of the child list
	'''
        return iter(self._child)

    def __len__(self):
        '''
         Which returns always how amny no.of child nodes it contains.
	'''
        return self._len 

    def depth_first(self):
        yield self
        for entry in self:
            #print("DEPTH_FIRST", entry)
            yield from entry.depth_first()


if __name__ == '__main__':
    root = Node(0)
    left = Node(1)
    right = Node(2)
    #print (root)
    #print (left)
    #print (right)

    root.add_child(left)
    root.add_child(right)

    left.add_child(Node(3))
    left.add_child(Node(4))
    right.add_child(Node(5))

    print(root, "Contains :", len(root), "childs")
    # Here iterator protocol invokes and convert it to be handled
    # by for loop.
    for node in root:
        print(node, "contains :", len(node), "childs")

    for child in root.depth_first():
        print(child) 

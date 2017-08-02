import builtins
import ast

RULE_INT = (
        ("__eq__", "Action: Both are Equal"),
        ("__lt__", "Action: obj1 < obj2"),
        ("__gt__", "Action: obj1 > obj2" )
)


RULE_STR = (
        ("__eq__", "Action: Both are Equal"),
        ("__ne__", "Action: Both are Equal"),
        ("__contains__", "Action: obj1 in obj2"),
)

Rule = type("Rule", (), {})

class Node:
    def __init__(self, val):
        self._data = val
        self._next = None

    def get_value(self):
        return self._data

    def get_next(self):
        return self._next

    def set_next(self, new):
        self._next = new

    def node_eval(self, obj1, obj2, dtype):
        if builtins.isinstance(obj1, dtype) and\
           builtins.isinstance(obj2, dtype):
            return Exception("Both are not same types to compare")

class LinkedList:
    def __init__(self, front=None):
        self.front = front

    def sll_insert_at_end(self):
        node = Node(read_value())
        if not self.front:
            self.front = node
        else:
            temp = self.front
            while temp.get_next():
                temp = temp.get_next()
            temp.set_next(node)

def create_new_rule(iterable):
    sll = LinkedList()
    for item in iterable:
       sll.sll_insert_at_end(item) 
    return sll

if __name__ == '__main__':
    rule_int = Rule()

    ips = [(1, 1), ("Hello", "Hi"),
           ("i am uday", "am")]
    
    i = 0
    for rules in (RULE_INT, RULE_STR, RULE_STR):
        for subrule in rules:
            operator, action = subrule
            matcher = getattr(ips[i][0], operator)
            print(ips[i][0], matcher.__name__ , ips[i][1], ", Result:", matcher(ips[i][1]))
        i += 1 

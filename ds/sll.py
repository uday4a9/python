import builtins
import collections
import sys
import os

from sll_lib import LinkedList

#>>> [item[4:] for item in LinkedList.__dict__ if builtins.callable(LinkedList.__dict__[item]) and item.startswith("sll_")]


def form_dict_from_sll_lib():
    methods = [LinkedList.__dict__[method] for method in LinkedList.__dict__
                if method.startswith('sll_')]
    methods.insert(0, sys.exit)
    return {ind: method for ind, method in enumerate(sorted(methods, key=lambda s:s.__name__))}

resd = form_dict_from_sll_lib()

def print_choices():
    for key, val in resd.items():
        print(key, ":", val.__name__[4:] if val.__name__.startswith('sll_') else val.__name__)

def main():
    start = LinkedList() 
    while True:
        print_choices()
        try:
            choice = int(input("Enter an input choice from above options: "))
        except ValueError:
            print("Enter proper option")
            continue
        os.system("clear")
        try:
            resd[choice](start)
        except KeyError:
            print("Choose options from available only")

if __name__ == '__main__':
    main()

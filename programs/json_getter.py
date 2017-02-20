#! /usr/bin/env /usr/bin/python3.4

from collections import abc
import json
from pprint import pprint

def get_targetnode_in_json(d, node, path):
    if not isinstance(d, abc.Mapping):
        return
    if node in d:
        path.append(node)
        print('.'.join(path), d[node], sep=" => ")
        path.pop()
    for key in d:
        path.append(key)
        if isinstance(d[key], abc.Mapping):
            get_targetnode_in_json(d[key], node, path)
        path.pop()




def main(target_node=None):
    d = json.load(open('sim2.json'))
    pprint(d)
    print('=*=' * 25)
    for key in d:
        get_targetnode_in_json(d[key], target_node, [key])

if __name__ == '__main__':
    #main(target_node="name")
    main(target_node="badges")


#! /usr/bin/env /usr/bin/python3.5

import re
from collections import abc

WORDS = re.compile(r'\w+')

def traversejson(json = None, path=None):
    """
        This function which extracts the value and returns the extracted value
    """
    if not path:
        return json
    if json:
        """
        print(json)
        print(WORDS.findall(path))
        nodes = [node.isdigit() for node in WORDS.findall(path)]
        print(nodes)
        """
        for node in WORDS.findall(path):
            if node.isdigit():
                node = int(node)

            try:
                json = json[node]
            except (TypeError, IndexError):
                return None
            """
            if isinstance(json, abc.Mapping):
                try:
                    json = json[node]
                except IndexError or TypeError:
                    return None
                print(1, type(json), node, json)
            elif isinstance(json, abc.MutableSequence):
                try:
                    json = json[node]
                except IndexError or TypeError:
                    return None
                print(2, type(json), node, json)
            else:
                try:
                    json = json[node]
                except IndexError or TypeError:
                    return None
                print(3, type(json), node, json)
            """
        return json



if __name__ == '__main__':
    d = {
            "hello" : [ {"world" : 
                                { "how" : "are"}
                      }
                    ],
            "hi" : "new" 
        }
    d1 = traversejson(d, "hello.0.world.how.are")
    print("Returned value :", d1)
    d2 = traversejson(d, "hi")
    print("Returned value :", d2)

# -*- coding=utf-8 -*-
"""
:author alex
:date 2018/3/9 

"""


def flatten(source):
    for sub in source:
        if isinstance(sub, list):
            yield from flatten(sub)
        else:
            yield sub


source_list = [1, 'alex', ['hello', 'world', ['inner', 'data']], 2, [3, 4]]

for obj in flatten(source_list):
    print(obj)


#!/usr/bin/python3
def uniq_add(my_list=[]):
    us = 0
    y = set()
    for x in my_list:
        if x not in y:
            us += x
            y.add(x)
            return us

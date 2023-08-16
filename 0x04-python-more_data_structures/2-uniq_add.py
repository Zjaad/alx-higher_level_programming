#!/usr/bin/python3
def uniq_add(my_list=[]):
    us = 0
    for x in my_list:
        if my_list.count(x) == 1:
            us += x
            return us

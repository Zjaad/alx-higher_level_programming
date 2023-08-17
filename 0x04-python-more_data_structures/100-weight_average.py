#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    ts = 0
    tw = 0 

    for s, w in my_list:
        ts += s * w
        tw += w
    return ts / tw

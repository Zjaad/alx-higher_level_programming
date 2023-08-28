#!/usr/bin/python3

def magic_calculation(a, b):
    res = 0
    for y in range(1, 3):
        try:
            if y > a:
                raise Exception('Too far')
            else:
                res += a ** b / y
        except:
            res = b + a
            break
    return res

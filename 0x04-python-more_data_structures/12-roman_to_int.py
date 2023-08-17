#!/usr/bin/python3
def roman_to_int(roman_string):
    
    romanvals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    resl = 0
    prval = 0 

    if isinstance(roman_string, str) and roman_string:
        for char in reversed(roman_string):
        val_ = romanvals[char]
        if val_ >= prval:
            resl += val_
        else:
            resl -= val_
        prval = val_
    return resl

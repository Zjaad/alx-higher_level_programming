#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    romanvals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    resl = 0
    prval = 0 

    for char in reversed(roman_string):
        val = romanvals[char]
        if val < prval:
            resl -= val
        else:
            resl += val
            prval = val
    return result

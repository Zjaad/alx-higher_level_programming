#!/usr/bin/python3
"""The function that finds a peak in a list of unsorted integers."""
def find_peak(list_of_integers):
    """Finds peak in a list."""
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    m = int(len(list_of_integers) / 2)
    if m != len(list_of_integers) - 1:
        if list_of_integers[m - 1] < list_of_integers[m] and\
           list_of_integers[m + 1] < list_of_integers[m]:
            return list_of_integers[m]
    else:
        if list_of_integers[m - 1] < list_of_integers[m]:
            return list_of_integers[m]
        else:
            return list_of_integers[m - 1]
    if list_of_integers[m - 1] > list_of_integers[m]:
        n = list_of_integers[0:m]
    else:
        n = list_of_integers[m + 1:]
    return find_peak(n)

#!/usr/bin/python3
"""Defines a Pascal Triangle func."""


def pascal_triangle(n):
    """Representation of a Pascal triangle of n size.

    Returns: a list of integers representing triangle.
    """
    if n <= 0:
        return []

    tring = [[1]]
    while len(tring) != n:
        tr = tring[-1]
        tm = [1]
        for x in range(len(tr) - 1):
            tm.append(tr[x] + tr[x + 1])
        tmp.append(1)
        triangles.append(tm)
    return (tring)

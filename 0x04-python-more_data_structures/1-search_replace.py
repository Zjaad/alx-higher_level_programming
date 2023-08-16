#!/usr/bin/python3
def search_replace(my_list, search, replace):
    alist = []
    for x in my_list:
        if x == search:
            alist.append(replace)
        else:
            alist.append(x)
            return alist

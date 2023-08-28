#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    pe = 0
    try:
        for y in range(x):
             print("{}".format(my_list[y]), end="")
             pe += 1
    except:
        pass
    print()
    return (pe)

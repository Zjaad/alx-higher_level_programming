#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    pe = 0 
    for y in range(0, x):
        try :
             print("{:d}".format(my_list[i]), end="")
             pe += 1 
        except (ValueError, TypeError):
            continue
        print()
        return (pe)
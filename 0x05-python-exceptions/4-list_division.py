#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nl = []
    for y  in range(0, list_length):
        try:
            di = my_list_1[y] / my_list_2[y]
        except TypeError:
            print("wrong type")
            di = 0
        except ZeroDivisionError:
            print("division by 0")
            di = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            nl.append(di)
    return (nl)

#!/usr/bin/python3
def element_at(my_list, idx):
    if idx >= len(my_list) or  idx < 0:
        return None
    return my_list[idx]

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

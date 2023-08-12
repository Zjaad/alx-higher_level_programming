#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_arg = len(argv) - 1

    if num_arg == 0:
        print("0 arguments.")
    elif num_arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_arg))

    for x in range(1, num_arg + 1):
        print("{}: {}".format(x, argv[x]))

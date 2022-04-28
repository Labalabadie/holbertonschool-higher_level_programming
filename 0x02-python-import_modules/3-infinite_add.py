#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from add_0 import add
    a = 0
    if len(argv) != 1:
        for i in range(len(argv) - 1):
            a = add(a, int(argv[i + 1]))
        print(a)
    else:
        print("0")

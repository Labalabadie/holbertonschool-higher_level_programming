#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = 1
    for elem in my_list:
        print(my_list[(len(my_list) - a)])
        a += 1

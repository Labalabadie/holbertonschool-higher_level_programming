#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i, elem in enumerate(my_list):
        if elem != search:
            new_list[i] = my_list[i]
        else:
            new_list[i] = replace
    return new_list

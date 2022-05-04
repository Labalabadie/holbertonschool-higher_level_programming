#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_3 = []
    for elem in set_1:
        for elements in set_2:
            if elem == elements:
                set_3.append(elem)
    return set_3

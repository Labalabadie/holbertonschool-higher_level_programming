#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = []
    for elem in set_1:
        flag = 0
        for elements in set_2:
            if elem == elements:
                flag = 1
        if flag == 0:
            set_3.append(elem)
    for elements in set_2:
        flag = 0
        for elem in set_1:
            if elem == elements:
                flag = 1
        if flag == 0:
            set_3.append(elements)
    return set_3

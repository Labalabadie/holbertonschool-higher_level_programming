#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for i, elem in enumerate(my_list):
        flag = 0
        for j, element in enumerate(new_list):
            if my_list[i] == new_list[j]:
                flag = 1
        if flag == 0:
            new_list.append(my_list[i])
    return sum(new_list)

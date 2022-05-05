#!/usr/bin/python3
def best_score(a_dictionary):
    b_dictionary = [0, 0]
    if a_dictionary is not None:
        for key, value in a_dictionary.items():
            if value > b_dictionary[1]:
                b_dictionary = key, value
        return b_dictionary[0]

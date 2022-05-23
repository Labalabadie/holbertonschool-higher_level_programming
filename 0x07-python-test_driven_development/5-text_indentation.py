#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    for letter in text:
        if letter == "?":
            print("\n")
        elif letter == ".":
            print("\n")
        elif letter == ":":
            print("\n")
        else:
            print(letter, end="")

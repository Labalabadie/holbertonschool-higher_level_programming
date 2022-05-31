#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, mode='a', encoding='utf-8') as c_file:
        return (c_file.write(text))

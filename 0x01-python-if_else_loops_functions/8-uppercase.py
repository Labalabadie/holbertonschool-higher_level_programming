#!/usr/bin/python3
def uppercase(str):
    strm = ""
    a = 0
    for letter in str:
        if ord(str[a]) > 96 and ord(str[a]) < 123:
            strm = chr(ord(str[a]) - 32)
        else:
            strm = chr(ord(str[a]))
        a = a + 1
        print(strm, end='')
    print()

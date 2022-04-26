#!/usr/bin/python3
flag = 0
for i in range(122, 96, -1):
    if flag == 1:
        i = i - 32
    print(chr(i), end='')
    if flag == 1:
        i = i + 32
        flag = 0
        continue
    flag = 1

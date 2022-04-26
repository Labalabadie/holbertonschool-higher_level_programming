#!/usr/bin/python3
a = 0
b = 1
for a in range(0, 9):
    b = a + 1
    for b in range(int(b), 10):
        print(a, b,sep='', end=', ')
print("89")

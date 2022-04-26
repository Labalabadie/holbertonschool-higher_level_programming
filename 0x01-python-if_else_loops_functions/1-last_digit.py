#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    numero = -number
else:
    numero = number

if (numero % 10) > 5:
    print("Last digit of", number, "is", (numero % 10), "and is greater than 5")
elif (numero % 10) == 0:
    print("Last digit of", number, "is 0 and is 0")
elif (numero % 10) < 6:
    print("Last digit of", number, "is", numero % 10, "and is less than 6")

#!/usr/bin/python3
import random
from math import fmod
number = random.randint(-10000, 10000)

if fmod(number, 10) > 5:
    print("Last digit of", number, "is", int(fmod(number, 10)), end='')
    print(" and is greater than 5")
elif fmod(number, 10) == 0:
    print("Last digit of", number, "is 0 and is 0")
elif fmod(number, 10) < 6:
    print("Last digit of", number, "is", int(fmod(number, 10)), end='')
    print(" and is less than 6 and not 0")

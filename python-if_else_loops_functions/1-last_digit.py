#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    equi = number % 10
else:
    equi = abs(number) % 10 * -1
if equi > 5:
    print(F"Last digit of {number} is {equi} and is greater than 5")
elif equi == 0:
    print(F"Last digit of {number} is {equi} and is 0")
elif equi < 6 and equi != 0:
    print(F"Last digit of {number} is {equi} and is less than 6 and not 0")

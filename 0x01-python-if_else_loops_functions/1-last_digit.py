#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
las_digit = abs(number) % 10
if number < 0:
    las_digit = -las_digit
print("Last digit of {} is {} and is ".format(number, las_digit), end="")
if las_digit > 5:
    print("greater than 5")
elif las_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")

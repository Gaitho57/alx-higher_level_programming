#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
otpt = f"Last digit of {number} is {last_digit}"

if last_digit > 5:
    otpt += " and is greater than 5"
elif last_digit == 0:
    otpt += " and is 0"
else:
    otpt += " and is less than 6 and not 0"

print(otpt)



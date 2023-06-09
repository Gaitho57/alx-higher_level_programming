#!/usr/bin/python3

# Print numbers from 0 to 89 with leading zeros
number = 0
while number <= 89:
    if number % 10 == 0:
        number += 1 + number // 10
    print("{:02d}".format(number), end='\n' if number == 89 else ", ")
    number += 1

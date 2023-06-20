#!/usr/bin/python3

# This program prints decimal and hexadecimal representations of numbers from 0 to 98
for num in range(0, 99):
    print("{:d} = 0x{:x}".format(num, num))

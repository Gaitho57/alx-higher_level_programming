#!/usr/bin/python3

# Print all lowercase letters from 'a' to 'z', excluding 'e' and 'q'
for char in range(97, 123):
    if char != 101 and char != 113:
        print("{:c}".format(char), end='')

#!/usr/bin/python3
#gives the following output abcdfghijklmnoprstuvwxyz
for letter in range(97, 123):
    if chr(letter) is not ['q', 'e']:
        print("{}".format(chr(letter)), end="")

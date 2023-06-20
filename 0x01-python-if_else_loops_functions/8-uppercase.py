#!/usr/bin/python3

def to_upper(character):
    # Converts lowercase character to uppercase
    if ord(character) >= ord('a') and ord(character) <= ord('z'):
        return chr(ord(character) - 32)
    else:
        return character


def uppercase(string):
    # Converts characters in string to uppercase
    new_string = ""
    for character in string:
        new_string += to_upper(character)
    print("{:s}".format(new_string))

#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    # Check if the input is a list
    if isinstance(my_list, list):
        # Reverse the list in-place
        my_list.reverse()

        # Iterate through the reversed list and print each element as an integer
        for i in my_list:
            print("{:d}".format(i))


#!/usr/bin/python3

def print_list_integer(my_list=[]):
    # Iterate through each element in the list
    for i in range(len(my_list)):
        # Print the element as an integer
        print("{:d}".format(my_list[i]))

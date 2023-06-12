#!/usr/bin/python3

def no_c(my_string):
    # Create a new list by filtering out characters 'c' and 'C' from the original string
    copy = [x for x in my_string if x != 'c' and x != 'C']

    # Join the filtered characters from the list to form a new string
    new_string = "".join(copy)

    # Return the new string with 'c' and 'C' removed
    return new_string


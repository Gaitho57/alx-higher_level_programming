#!/usr/bin/python3

def max_integer(my_list=[]):
    # Check if the list is empty
    if len(my_list) == 0:
        # If the list is empty, return None
        return None

    # Initialize the variable 'big' with the first element of the list
    big = my_list[0]

    # Iterate through the elements of the list
    for i in range(len(my_list)):
        # Compare each element with the current maximum value ('big')
        if my_list[i] > big:
            # If an element is greater than 'big', update 'big' with the new maximum value
            big = my_list[i]

    # Return the maximum value found in the list
    return big


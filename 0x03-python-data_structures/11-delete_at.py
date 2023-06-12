#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Check if the given index is within the valid range for the list
    if idx >= 0 and idx < len(my_list):
        # If the index is valid, delete the element at the specified index using the 'del' statement
        del my_list[idx]

    # Return the modified list
    return my_list


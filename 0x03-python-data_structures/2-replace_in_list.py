#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    # Check if the index is within the bounds of the list
    if idx >= 0 and idx < len(my_list):
        # Replace the element at the specified index with the new element
        my_list[idx] = element

    # Return the modified list
    return my_list


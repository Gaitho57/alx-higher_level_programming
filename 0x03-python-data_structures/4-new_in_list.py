#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # Check if the index is out of bounds
    if idx < 0 or idx > (len(my_list) - 1):
        # Return the original list if the index is invalid
        return my_list

    # Create a copy of the original list
    copy = [x for x in my_list]

    # Replace the element at the specified index with the new element in the copied list
    copy[idx] = element

    # Return the modified copy of the list
    return copy


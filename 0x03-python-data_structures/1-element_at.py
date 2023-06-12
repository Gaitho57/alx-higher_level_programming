#!/usr/bin/python3
# 1-element_at.py
def element_at(my_list, idx):
    # Check if the index is out of bounds
    if idx < 0 or idx >= len(my_list):
        # Return None if the index is invalid
        return None

    # Return the element at the specified index
    return my_list[idx]


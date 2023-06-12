#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Check the length of tuple_a
    if len(tuple_a) < 2:
        # If tuple_a has less than 2 elements
        if len(tuple_a) == 0:
            # If tuple_a is empty, assign it a default value of (0, 0)
            tuple_a = 0, 0
        else:
            # If tuple_a has only one element, assign the second element as 0
            tuple_a = tuple_a[0], 0

    # Check the length of tuple_b
    if len(tuple_b) < 2:
        # If tuple_b has less than 2 elements
        if len(tuple_b) == 0:
            # If tuple_b is empty, assign it a default value of (0, 0)
            tuple_b = 0, 0
        else:
            # If tuple_b has only one element, assign the second element as 0
            tuple_b = tuple_b[0], 0

    # Return a new tuple with the sum of corresponding elements from tuple_a and tuple_b
    return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]


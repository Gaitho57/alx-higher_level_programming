#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Create an empty list to store the results
    multiples = []

    # Iterate through each element in the list
    for i in range(len(my_list)):
        # Check if the element is divisible by 2
        if my_list[i] % 2 == 0:
            # If divisible by 2, append True to the multiples list
            multiples.append(True)
        else:
            # If not divisible by 2, append False to the multiples list
            multiples.append(False)

    # Return the list of multiples
    return multiples


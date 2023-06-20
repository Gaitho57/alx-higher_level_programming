#!/usr/bin/python3

def print_last_digit(number):
    # Get absolute value of number
    abs_number = abs(number)

    # Calculate last digit
    last_digit = abs_number % 10

    # Prints last digit without newline
    print("{:d}".format(last_digit), end='')

    return last_digit

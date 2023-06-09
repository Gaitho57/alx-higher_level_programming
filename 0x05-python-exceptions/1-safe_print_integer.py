#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))  # Print the value as an integer
        return True
    except (ValueError, TypeError):
        return False

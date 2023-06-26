#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for index in range(x):
            if isinstance(my_list[index], int):
                print("{:d}".format(my_list[index]), end=' ')  # Print the integer element
                count += 1
    except (IndexError, ValueError, TypeError):
        pass
    finally:
        print()
        return count

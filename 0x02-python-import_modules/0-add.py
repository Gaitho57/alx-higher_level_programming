#!/usr/bin/python3

if __name__ == "__main__":
    # Imports function definition and applies it
    a = 1
    b = 2

    from add_0 import add

    print("{} + {} = {}".format(a, b, add(a, b)))

#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    list_ord = list(a_dictionary.keys())
    list_ord.sort()

    for in_dex in list_ord:
        print("{}: {}".format(in_dex, a_dictionary.get(in_dex)))

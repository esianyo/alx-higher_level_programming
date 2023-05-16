#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for el in reversed(my_list):
        if isinstance(el, int):
            print("{:d}".format(el))

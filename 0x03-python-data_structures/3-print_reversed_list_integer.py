#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for el in my_list:
        if isinstance(el, int):
            print("{:d}".format(el))

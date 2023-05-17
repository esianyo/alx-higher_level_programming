#!/usr/bin/python3

def no_c(my_string):
    mine = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            mine = mine + i
    return mine

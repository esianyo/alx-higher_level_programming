#!/usr/bin/python3
def print_last_digit(number):
    last = abs(number) % 10
    if number < 0:
        last = last * -1
    return last

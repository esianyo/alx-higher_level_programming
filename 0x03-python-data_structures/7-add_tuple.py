#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    ans = tuple(first + second for first, second in zip(tuple_a, tuple_b))
    return ans

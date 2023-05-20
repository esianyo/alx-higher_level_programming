#!/usr/bin/python3

def uniq_add(my_list):
  uniq_integers = set(my_list)
  sum_of_uniq_integers = 0
  for uniq_integer in uniq_integers:
    sum_of_uniq_integers += uniq_integer

  return sum_of_uniq_integers

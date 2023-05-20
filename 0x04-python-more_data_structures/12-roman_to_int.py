#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_numerals = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
    }

    result = 0
    for i in range(len(roman_string)):
        current_value = roman_numerals[roman_string[i]]
        next_value = roman_numerals[roman_string[i + 1]] if i + 1 < len(roman_string) else 0

        if current_value < next_value:
            result -= current_value
        else:
            result += current_value

    return result

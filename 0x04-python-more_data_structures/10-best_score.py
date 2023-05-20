#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best_score = None
    best_key = None
    for key, value in a_dictionary.items():
        if best_score is None or value > best_score:
            best_score = value
            best_key = key

    return best_key

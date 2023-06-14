#!/usr/bin/python3
"""Returns an object represented by a JSON string"""
import json



def from_json_string(my_str):
    """"Main function for the magic"""
    return json.loads(my_str)

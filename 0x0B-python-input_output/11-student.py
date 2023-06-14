#!/usr/bin/python3
"""Student to disk reload"""


class Student:
    """Represents a student  """


    def __init__(self, first_name, last_name, age):
        """Initialize a Student object."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    
    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student object."""

        if attrs is None:
            attrs = []

            json_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)

        return json_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""

        for attr, value in json.items():
            if hasattr(self, attr):
                setattr(self, attr, value)

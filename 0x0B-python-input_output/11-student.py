#!/usr/bin/python3
"""Student to disk reload"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attribute.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__

        return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
                }

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): Dictionary containing attribute names and values.

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)

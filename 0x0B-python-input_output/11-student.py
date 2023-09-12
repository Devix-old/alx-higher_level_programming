#!/usr/bin/python3
"""10-student module"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        json_dict = {}
        for key in attrs:
            if (hasattr(self, key)):
                json_dict[key] = getattr(self, key)
        return json_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)

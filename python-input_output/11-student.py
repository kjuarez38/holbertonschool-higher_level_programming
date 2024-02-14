#!/usr/bin/python3
"""class Student v.3"""


class Student:
    """class Student v.3"""
    def __init__(self, first_name, last_name, age):
        """class Student v.3"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """class Student v.3"""
        return self.__dict__

    def to_json(self, attrs=None):
        """class Student v.3"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict

    def reload_from_json(self, json):
        """class Student v.3"""
        for key in json:
            self.__dict__[key] = json[key]

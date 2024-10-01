#!/usr/bin/python3

"""
class Studen with three public instances
returns a dictionary representation of a Student instance
"""


class Student():

    """
    public instance attributes for Student
    returns dictionary representation
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return (self.__dict__)

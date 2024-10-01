#!/usr/bin/python3

"""
a class Student with three public instance attributes
method that retrieves a dictionary representation of a Student
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

    def to_json(self, attrs=None):
        if attrs is None:
            return (self.__dict__)
        else:
            return ({
                key: value for key, value in self.__dict__.items()
                if key in attrs
                    })

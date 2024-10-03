#!/usr/bin/python3

"""
a custom Python class named CustomObject
"""
import pickle


class CustomObject():
    """
    three attributes, name, age and is_student
    two methods within the class and a class method
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, "wb") as my_file:
                pickle.dump(self, my_file)
        except Exception as error:
            print(f"Error while serializing: {error}")

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as my_file:
                return (pickle.load(my_file))
        except (FileNotFoundError, pickle.UnpicklingError) as error:
            print(f"Error while deserializing: {error}")
            return (None)

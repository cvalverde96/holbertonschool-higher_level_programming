#!/usr/bin/python3


from abc import ABC, abstractmethod


"""
clase abstracta con metodo abstracto sound
"""


class Animal(ABC):

    """
    clase con metodo abstracto sound
    dos clases que heredan de Animal
    implementando el metodo de sound
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return ("Bark")


class Cat(Animal):
    def sound(self):
        return ("Meow")

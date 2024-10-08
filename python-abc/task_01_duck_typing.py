#!/usr/bin/python3

from abc import ABC, abstractmethod
import math

"""
clase abstracte de nombre Shape que hereda de ABC
dos clases concretas que heredan de Shape
funcion que imprime info de shape
"""


class Shape(ABC):

    """
    clase Shape abstracta
    clase Cricle que define area y perimeter
    clase Rectangle que define area y perimeter
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return (math.pi * self.__radius ** 2)

    def perimeter(self):
        return (2 * math.pi * abs(self.__radius))


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        return (2 * (self.__width + self.__height))


def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

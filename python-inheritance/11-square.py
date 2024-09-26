#!/usr/bin/python3

"""
clase que hereda de rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    clase square que hereda de rectangulo
    tiene constructor que inicializa un cuadrado con size
    tiene un metodo de area y override de string
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")

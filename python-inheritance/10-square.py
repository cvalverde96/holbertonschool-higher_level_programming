#!/usr/bin/python3

"""
clase que define un square heredado de rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    inicializa el square con size, que width y height
    size es validado por integer validator
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

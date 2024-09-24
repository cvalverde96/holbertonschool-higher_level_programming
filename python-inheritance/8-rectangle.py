#!/usr/bin/python3

"""
clase Rectangle que hereda de clase BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    inicializando Rectangulo con width y height
    usamos integer validator, para validar que sean
    integers y que sea mayor a 0

    Args:
        width (int): width del rectangle
        height (int): height del rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

#!/usr/bin/python3

"""
este modulo define una clase square
con validacion de tamaño y computa el area
"""


class Square:
    """
    definiendo clase square con atributo privado de size
    """
    def __init__(self, size=0):
        """
        inicializa un square con un tamaño opcional
        tamañano debe ser integer y mayor a 0
        """
        self.__size = size

    @property
    def size(self):
        """
        getter para el atributo de size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        setter para el atributo de size con validacion
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        retorna el area
        """
        return (self.__size * self.__size)

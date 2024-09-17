#!/usr/bin/python3

"""
este module define un cuadrado con
validacion de tamano
y tiene area
"""


class Square:
    """
    declaracion de clase Square, con instancia privada
    inicializa el square con tamano 0, y luego valida
    si es integer o si es mayor a 0
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """
    definimos un metodo que retorna el area
    """
    def area(self):
        return (self.__size * self.__size)

#!/usr/bin/python3

"""
este modulo define una clase square con validacion
de tamaño
"""


class Square:

    """
    una clase llamada Square que representa un cuadrado
    con una instancia privada de atributo
    dos if statements para validar si son integers
    y si es mayor a 0
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

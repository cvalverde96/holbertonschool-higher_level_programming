#!/usr/bin/python3

"""
imprime un cuadrado con el character '#'
"""


def print_square(size):
    """
    Args:
        size: el tamano del square
    Raises:
        TypeError: si el tamano no es un integer
        ValueError: si el tamano es menor que 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)

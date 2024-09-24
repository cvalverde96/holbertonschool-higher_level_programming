#!/usr/bin/python3

"""
module que define una clase BaseGeometry
contiene metodo que alza Exception
y metodo para validar integer
"""


class BaseGeometry():
    """
    Methods:
    area(self):
        alza exception que el area no ha sido implementado

    integer_validator(self, name, value):
        valida que el valor sea integer y mayor a zero
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

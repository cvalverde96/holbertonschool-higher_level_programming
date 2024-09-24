#!/usr/bin/python3

"""
modulo con clase BaseGeometry con public instance method
que alza una excepcion con mensaje
"""


class BaseGeometry():
    """
    Methods:
        - area(self): raise Exception con mensaje que area
        no ha sido implementado
    """
    def area(self):
        raise Exception("area() is not implemented")

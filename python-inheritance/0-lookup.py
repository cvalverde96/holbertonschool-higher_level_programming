#!/usr/bin/python3


"""
modulo que define una funcion que retorna
una lista de los atributos y metodos disponibles
a ese objeto
"""


def lookup(obj):
    """
    Retorna la lista de los atributos y metodos disponibles
    a ese objeto

    Args:
        obj: el objeto, a cual le vamos a retornar
        los atributos y metodos disponibles

    Returns:
        retorna una lista de los atr y obj disponibles
    """
    return (dir(obj))

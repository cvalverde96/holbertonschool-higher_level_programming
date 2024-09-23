#!/usr/bin/python3


"""
modulo con funcion que valida si objeto es
igual a la clase especificada
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: el objeto a checck

    Returns:
        True si es igual, False si no
    """
    if type(obj) == a_class:
        return (True)
    else:
        return (False)

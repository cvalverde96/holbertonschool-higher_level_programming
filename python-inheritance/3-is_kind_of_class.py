#!/usr/bin/python3

"""
este modulo define una funcion que chequea si el objeto
es una instancia de donde heredo la clase
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: el objeto a validar
        a_class: la clase a validar

    Returns:
        True si es una instance de la clase
        false si no
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)

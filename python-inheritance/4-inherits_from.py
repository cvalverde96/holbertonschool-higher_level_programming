#!/usr/bin/python3

"""
modulo contiene funcion que chequea si objeto es instancia
de una clase que heredo de una clase
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: objeto a ser validado
        a_class: clase a validar herencia

    Returns:
        True: cierto si objeto es instancia de una clase
        que heredo de a_class
        False: falso si no
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return (True)
    else:
        return (False)

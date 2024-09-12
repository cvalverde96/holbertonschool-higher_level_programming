#!/usr/bin/python3
def add_integer(a, b=98):
    """
    anade dos integers o floats
    tenemos isinstance para validar que en efecto sea in o float
    de no ser asi, va raise el error correcto con su mensaje adecuado

    Args:
        a: primer numero
        b: segundo numero, le pusimos default 98

    Returns:
        retorna resultado de suma

    Raises:
        TypeError: si a o b no son integers o float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)

#!/usr/bin/python3

"""
imprime 'My name is <primer nomber> <apellido>'
"""

def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name: nombre, deber ser un string
        last_name: apellido, debe ser un string
    Raises:
        TypeError: 
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")

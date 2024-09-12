#!/usr/bin/python3

"""
divide todos los elementos en una matriz por division,
redondeado a dos espacios decimales
"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix: una lista de lista de integers o floats
    Returns:
        un matrix nuevo con sus elementos divididos
    Raises:
        TypeError: si la lista no es de integers o floats
                o si los rows no son del mismo tamaño
                o si la division no es un numero
        ZeroDivisionError:
            si la division es por 0
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([[round(num / div, 2) for num in row] for row in matrix])

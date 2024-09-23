#!/usr/bin/python3

"""
modulo que define una clase MyList que hereda
de list, tiene metodo para imprimir la lista en
orden ascendente
"""


class MyList(list):
    """
    mi clase MyList que hereda the el built-in list classs
    """
    def print_sorted(self):
        """
        metodo que imprime lista en orden ascendente
        """
        print(sorted(self))

#!/usr/bin/python3

"""
tres clases, SwimMixin, FlyMixin, Dragon
"""


class SwimMixin():
    """
    metodo swim que imprime mensaje
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin():
    """
    metodo fly que imprime mensaje
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    metodo roar que imprime mensaje
    """
    def roar(self):
        print("The dragon roars!")

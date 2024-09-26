#!/user/bin/python3

"""
definiendo tres clases Fish, Bird, FlyingFish
la clase FlyingFish hereda de Bird y Firsh
"""


class Fish:
    """
    dos metodos swim imprime y habitat imprime
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
    dos metodos fly y habitat imprime
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("he bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    tres metodos, fly, swim, y habitat imprime
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

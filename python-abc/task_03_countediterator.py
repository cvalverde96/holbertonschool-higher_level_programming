#!/usr/bin/python3

"""
clase CountedIterator que trabaja con un iterable
trackea la cantidad de veces que un item fue iterado
"""


class CountedIterator():

    """
    constructor que inicializa dos atributos, iterator y count
    metodo __next__ que esta overriting para tener comportamiento custom
    metodo get_count para retornar el count de items iterados
    metodo __iter__ que estamos overriding
    """
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):

        try:
            item = next(self.iterator)
            self.count += 1
            return (item)

        except StopIteration:
            raise (StopIteration)

    def get_count(self):
        return (self.count)

    def __iter__(self):
        return (self)

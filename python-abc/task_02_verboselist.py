#!/usr/bin/python3

"""
Clase VerboseList que extiende el built in list class
imprime un tipo de mensaje de notificacion cada vez
que uno de los metodos se ejecutan
"""


class VerboseList(list):

    """
    append, extend, remove y pop definidos con mensaje
    de notificacion
    """
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return (super().pop(index))

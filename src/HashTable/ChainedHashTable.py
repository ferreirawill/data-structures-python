import random

import numpy


class ChainedHashTable:
    dimension = 1
    length = 0
    integer_bits = 32

    def __init__(self):
        self.table = numpy.empty(self.dimension, object)
        self.random_odd_int = random.randrange(1, 2 ** self.integer_bits) | 1
        self.average_of_stored_elements = 0

    def add(self, item):
        if self.find(item) is not None:
            return False
        if self.average_of_stored_elements + 1 > len(self.table):
            self.__resize()

        self.table[hash(item)].append(item)

        self.average_of_stored_elements += 1
        return True

    def remove(self, item):
        raise NotImplementedError

    def find(self, item):
        raise NotImplementedError

    def __resize(self):
        raise NotImplementedError

    def __hash(self, item):
        return ((self.random_odd_int * item) % 2 ** self.integer_bits) // 2**(self.integer_bits-self.dimension)

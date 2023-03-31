import random

import numpy


class ChainedHashTable:
    dimension = 8
    integer_bits = 32

    def __init__(self):
        self.table = numpy.empty(self.dimension, object)
        self.random_odd_int = random.randrange(1, 2 ** self.integer_bits) | 1
        self.average_of_stored_elements = 0

    def add(self, item: int):
        if self.find(item) is not None:
            return False
        if self.average_of_stored_elements + 1 > len(self.table):
            self.__resize()

        self.table[hash(item)].append(item)

        self.average_of_stored_elements += 1
        return True

    def remove(self, item: int):
        itemList: list = self.table[self.__hash(item)]
        for value in itemList:
            if value == item:
                itemList.remove(value)
                self.average_of_stored_elements -= 1

                if 3 * self.average_of_stored_elements < len(self.table):
                    self.__resize()
                return value

        return None

    def find(self, item: int):
        for value in self.table[self.__hash(item)]:
            if value == item:
                return value
        return None

    def __resize(self):
        self.dimension = 1
        while (2 ** self.dimension < 3 * self.average_of_stored_elements):
            self.dimension += 1
            old_table = self.table
            self.table = numpy.empty(2 ** self.dimension)
            for value in old_table:
                if value is not None:
                    value_hash = self.__hash(value)
                    while self.table[value_hash] is not None:
                        value_hash = (value_hash + 1) % len(self.table)
                    self.table[value_hash] = value
    def __hash(self, item: int):
        return ((self.random_odd_int * item) % 2 ** self.integer_bits) // 2 ** (self.integer_bits - self.dimension)

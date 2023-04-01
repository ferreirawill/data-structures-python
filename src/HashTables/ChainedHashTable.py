import random

import numpy


class ChainedHashTable:
    integer_bits = 32

    def __init__(self):
        self.dimension = 1
        self.table = self.__alloc_table(self.dimension)
        self.random_odd_int = random.randrange(1, 2 ** self.integer_bits) | 1
        self.stored_elements = 0

    def add(self, item: int):
        if self.find(item) is not None:
            return False
        if self.stored_elements + 1 > len(self.table):
            self.__resize()

        self.table[self.__hash(item)].append(item)

        self.stored_elements += 1
        return True

    def remove(self, item: int):
        itemList = self.table[self.__hash(item)]
        for value in itemList:
            if value == item:
                itemList.remove(value)
                self.stored_elements -= 1
                if self.stored_elements == 1:
                    pass

                if 3 * self.stored_elements < len(self.table):
                    self.__resize()
                return value

        return None

    def find(self, item: int):
        position_hash = self.table[self.__hash(item)]
        for value in position_hash:
            if value == item:
                return value
        return None

    def __resize(self):
        self.dimension = 1
        while (1 << self.dimension) <= 3*self.stored_elements:
            self.dimension += 1
        old_table = self.table
        self.table = self.__alloc_table(self.dimension)
        for old_table_index in range(len(old_table)):
            for value in old_table[old_table_index]:
                self.add(value)


    def __alloc_table(self, dimension):
        return [[] for _ in range(1<<dimension)]

    def __hash(self, item: int):
        return ((self.random_odd_int * hash(item)) % (1 << self.integer_bits)) >> (self.integer_bits - self.dimension)

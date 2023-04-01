import numpy


class LinearHashTable:
    integer_bits = 32
    tabulation_array = numpy.random.randint(0, high=0xFFFFFFFF, size=(256, 4))

    def __init__(self):
        self.void = object
        self.dimension = 1
        self.table = numpy.empty(1 << self.dimension, object)
        self.voids_number = 0
        self.stored_elements = 0

    def find(self, item: int):
        index = self.__hash(item)
        while self.table[index] is not None:
            if self.table[index] != self.void and item == self.table[index]:
                return self.table[index]
            index = (index + 1) % len(self.table)

    def add(self, item: int):
        if self.find(item) is not None:
            return False
        if 2 * (self.voids_number + 1) > len(self.table):
            self.__resize()
        index = self.__hash(item)

        while self.table[index] is not None and self.table[index] != self.void:
            index = (index + 1) % len(self.table)

        if self.table[index] is None:
            self.voids_number += 1

        self.stored_elements += 1
        self.table[index] = item
        return True

    def remove(self, item: int):
        index = self.__hash(item)

        while self.table[index] is not None:
            removed = self.table[index]
            if removed != self.void and item == removed:
                self.table[index] = self.void
                self.stored_elements -= 1

                if 8 * self.stored_elements < len(self.table):
                    self.__resize()
                return removed

            index = (index + 1) % len(self.table)
        return None

    def __hash(self, item: int):
        hash_code = hash(item)
        return (self.tabulation_array[hash_code & 0xFF][0] ^ self.tabulation_array[(hash_code >> 8) & 0xFF][1]
                ^ self.tabulation_array[(hash_code >> 16) & 0xFF][2]
                ^ self.tabulation_array[(hash_code >> 24) & 0xFF][3]) >> (self.integer_bits - self.dimension)

    def __resize(self):
        self.dimension = 1

        while (1 << self.dimension) < 3 * self.stored_elements:
            self.dimension += 1

        old_table = self.table
        self.table = numpy.empty(1 << self.dimension, object)
        self.voids_number = self.stored_elements

        for value in old_table:
            if value is not None and value != self.void:
                index = self.__hash(value)

                while self.table[index] is not None:
                    index = (index + 1) % len(self.table)
                self.table[index] = value

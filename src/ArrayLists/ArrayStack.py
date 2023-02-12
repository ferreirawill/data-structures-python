import numpy

from Interfaces.Stack import Stack


class ArrayStack(Stack):
    length = 0

    def __init__(self):
        self.__backing_array = numpy.empty(1, object)

    def get(self, position):
        return self.__backing_array[position]

    def set(self, position, value):
        old_value = self.__backing_array[position]
        self.__backing_array[position] = value
        return old_value

    def add(self, position, value):
        if self.length == self.__backing_array.size:
            self.__resize()

        self.__backing_array[position + 1:self.length] = self.__backing_array[position:self.length]
        self.__backing_array[position] = value
        self.length += 1

    def remove(self, position):
        old_value = self.__backing_array[position]

        self.__backing_array[position:self.length - 1] = self.__backing_array[position + 1:self.length]

        if 3 * self.__backing_array.size >= self.length:
            self.__resize()

        return old_value

    def __resize(self):
        new_array = numpy.empty(2 * self.length, object)
        new_array[0:self.length] = self.__backing_array[0:self.length]
        self.__backing_array = new_array

import numpy

from src.Interfaces.List import List


class ArrayStack(List):
    length = 0

    def __init__(self):
        self.backing_array = numpy.empty(1, object)

    def size(self):
        return self.length

    def get(self, position):
        return self.backing_array[position]

    def set(self, position, value):
        old_value = self.backing_array[position]
        self.backing_array[position] = value
        return old_value

    def add(self, position, value):
        if self.length == self.backing_array.size:
            self.__resize()

        self.backing_array[position + 1:self.length] = self.backing_array[position:self.length]
        self.backing_array[position] = value
        self.length += 1

    def remove(self, position):
        old_value = self.backing_array[position]

        self.backing_array[position:self.length - 1] = self.backing_array[position + 1:self.length]

        self.length -=1

        if 3 * self.backing_array.size >= self.length:
            self.__resize()


        return old_value

    def __resize(self):
        new_array = numpy.empty(2 * self.length, object)
        new_array[0:self.length] = self.backing_array[0:self.length]
        self.backing_array = new_array

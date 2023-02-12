import numpy

from src.Interfaces.Queue import Queue


class ArrayQueue(Queue):
    lenght = 0
    next_remove = 0

    def __init__(self):
        self.backing_array = numpy.empty(1, object)

    def add(self, value):
        if self.lenght + 1 > self.backing_array.size:
            self.__resize()

        self.backing_array[(self.lenght + self.next_remove) % self.backing_array.size] = value

        self.lenght += 1
        return True

    def remove(self):
        value_to_remove = self.backing_array[self.next_remove]

        self.next_remove = (self.next_remove + 1) % self.backing_array.size

        self.lenght -= 1
        if self.backing_array.size >= 3 * self.lenght:
            self.__resize()

        return value_to_remove

    def __resize(self):
        new_array = numpy.empty(2*self.lenght,object)

        for i in range(0,self.lenght,1):
            new_array[i] = self.backing_array[(self.next_remove + i) % self.backing_array.size]

        self.backing_array = new_array
        self.next_remove = 0


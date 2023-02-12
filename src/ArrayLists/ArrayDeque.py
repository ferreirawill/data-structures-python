import numpy

from src.Interfaces.List import List


class ArrayDeque(List):
    length = 0
    next_remove = 0

    def __init__(self):
        self.backing_array = numpy.empty(1, object)

    def size(self):
        return self.length

    def get(self, position):
        return self.backing_array[(position + self.next_remove) % self.backing_array.size]

    def set(self, position, value):
        old_value = self.backing_array[(position + self.next_remove) % self.backing_array.size]
        self.backing_array[(position + self.next_remove) % self.backing_array.size] = value
        return old_value

    def add(self, position, value):
        if self.length + 1 > self.backing_array.size:
            self.__resize()

        if position < self.length / 2:
            for idx in range(position):
                self.backing_array[(self.next_remove + idx)
                                   % self.backing_array.size] = self.backing_array[(self.next_remove + idx + 1)
                                                                                   % self.backing_array.size]
        else:
            for idx in range(self.length, position, -1):
                self.backing_array[(self.next_remove + idx)
                                   % self.backing_array.size] = self.backing_array[(self.next_remove + idx - 1)
                                                                                   % self.backing_array.size]

        self.backing_array[(position + self.next_remove) % self.backing_array.size] = value

        self.length += 1

    def remove(self, position):
        removed_value = self.backing_array[(position+self.next_remove)% self.backing_array.size]

        if position < self.length/2:
            for idx in range(position):
                self.backing_array[(self.next_remove + idx)
                                   % self.backing_array.size] = self.backing_array[(self.next_remove + idx - 1)
                                                                                   % self.backing_array.size]
            self.next_remove = (self.next_remove+1) % self.backing_array.size
        else:
            for idx in range(position,self.length-1,1):
                self.backing_array[(self.next_remove + idx)
                                   % self.backing_array.size] = self.backing_array[(self.next_remove + idx + 1)
                                                                                   % self.backing_array.size]
        self.length -= 1
        if self.backing_array.size >= 3* self.length:
            self.__resize()

        return removed_value


    def __resize(self):
        new_array = numpy.empty(2*self.length,object)

        for i in range(0,self.length,1):
            new_array[i] = self.backing_array[(self.next_remove + i) % self.backing_array.size]

        self.backing_array = new_array
        self.next_remove = 0





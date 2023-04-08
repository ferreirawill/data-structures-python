import random
import numpy
from src.Interfaces.SSet import SSet


class SkiplistSSet(SSet):
    integer_size = 32

    class Node:
        next = None
        label = None

        def __init__(self, label, height):
            self.next = numpy.empty(height + 1, object)
            self.label = label

        def height(self):
            return len(self.next) - 1

    def __init__(self):
        self.height = 0
        self.length = 0
        self.sentinel = SkiplistSSet.Node(None, height=self.integer_size)
        self.stack = numpy.empty(self.sentinel.height() + 1, object)

    def size(self):
        pass

    def find(self, value):
        node = self.__find_pred_node(value)
        if node.next[0] is None:
            return None

        return node.next[0].label

    def add(self, value):
        node = self.sentinel
        row = self.height
        while row >= 0:
            while node.next[row] is not None and node.next[row].label < value:
                node = node.next[row]
            if node.next[row] is not None and node.next[row].label == value:
                return False

            self.stack[row] = node
            row -= 1

        new_sentinel = SkiplistSSet.Node(value, self.__pick_height())
        while self.height < new_sentinel.height():
            self.height += 1
            self.stack[self.height] = self.sentinel

        for i in range(len(new_sentinel.next)):
            new_sentinel.next[i] = self.stack[i].next[i]
            self.stack[i].next[i] = new_sentinel
        self.length += 1

        return True

    def remove(self, value):
        removed = False
        node = self.sentinel
        row = self.height

        while row >= 0:
            while node.next[row] is not None and node.next[row].label < value:
                node = node.next[row]

            if node.next[row] is not None and node.next[row].label == value:
                removed = True
                node.next[row] = node.next[row].next[row]
                if node == self.sentinel and node.next[row] is None:
                    self.height -= 1
            row -= 1

        if removed:
            self.length -= 1

        return removed

    def __find_pred_node(self, value) -> Node:
        node = self.sentinel
        row = self.height
        while row >= 0:
            while node.next[row] is not None and node.next[row].label < value:
                node = node.next[row]
            row -= 1

        return node

    def __pick_height(self):
        random_int = random.getrandbits(self.integer_size)
        height = 0
        while random_int & 1:
            height += 1
            random_int = random_int // 2
        return height

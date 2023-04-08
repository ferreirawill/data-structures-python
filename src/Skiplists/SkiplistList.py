import random

import numpy

from src.Interfaces.List import List


class SkiplistList(List):
    integer_size = 32

    class Node:
        next = None
        label = None

        def __init__(self, label, height):
            self.next = numpy.empty(height + 1, object)
            self.label = label
            self.length = numpy.ones(height + 1, int)

        def height(self):
            return len(self.next) - 1

    def __init__(self):
        self.height = 0
        self.sentinel = SkiplistList.Node(None, self.integer_size)
        self.size = 0

    def size(self):
        return self.size

    def get(self, position):
        return self.__find_pred(position).next[0].label

    def set(self, position, value):
        node = self.__find_pred(position).next[0]
        label = node.label
        node.label = value
        return label

    def add(self, position, value):
        new_node = SkiplistList.Node(label=value, height=self.__pick_height())
        if new_node.height() > self.height:
            self.height = new_node.height()

        self.__add_node(position, new_node)

    def remove(self, position):
        node = self.sentinel
        row = self.height
        node_position = -1
        old_label = None
        while row >= 0:
            while node.next[row] is not None and node_position + node.length[row] < position:
                node_position = node_position + node.length[row]
                node = node.next[row]

            node.length[row] -= 1
            if node_position + node.length[row] + 1 == position and node.next[row] is not None:
                old_label = node.next[row].label
                node.length[row] += node.next[row].length[row]
                node.next[row] = node.next[row].next[row]

                if node == self.sentinel and node.next[row] is None:
                    self.height -= 1

            row -= 1

        self.size += 1

        return old_label

    def __find_pred(self, position) -> Node:
        node = self.sentinel
        row = self.height
        node_position = -1
        while row >= 0:
            while node.next[row] is not None and node_position + node.length[row] < position:
                node_position = node_position + node.length[row]
                node = node.next[row]

            row -= 1
        return node

    def __pick_height(self) -> int:
        random_int = random.getrandbits(self.integer_size)
        height = 0
        while random_int & 1:
            height += 1
            random_int = random_int // 2
        return height

    def __add_node(self, position, new_node):
        node = self.sentinel
        new_node_height = new_node.height()
        row = self.height
        node_position = -1
        while row >= 0:
            while node.next[row] is not None and node_position + node.length[row] < position:
                node_position = node_position + node.length[row]
                node = node.next[row]
            node.length[row] += 1

            if row <= new_node_height:
                new_node.next[row] = node.next[row]
                node.next[row] = new_node
                new_node.length[row] = node.length[row] - (position - node_position)
                node.length[row] = position - node_position

            row -= 1
        self.size += 1
        return node



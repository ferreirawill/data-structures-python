from src.Interfaces.List import List


class DoublyLinkedList(List):
    class Node:
        label = None
        previous = None
        next = None

        def __init__(self, label):
            self.label = label

    def __init__(self):
        self.length = 0
        self.dummy = self.Node(None)
        self.dummy.next = self.dummy
        self.dummy.previous = self.dummy

    def size(self):
        return self.length

    def get(self, position: int):
        ''''Get node value by position'''
        return self.__get_node(position).label

    def get_node_info(self, position: int):
        ''''Get position previous, label and next'''
        info = self.__get_node(position)
        return info.previous.label, info.label, info.next.label

    def set(self, position: int, label):
        '''set node value by position'''
        if 0 > position or position > self.length:
            raise IndexError("Invalid possition to set")

        node = self.__get_node(position)
        node_label = node.label
        node.label = label
        return node_label

    def add(self, position, label):
        '''Add node in a given position'''
        self.__add_before(self.__get_node(position), label)

    def remove(self, position):
        '''Remove a node in a given position'''
        self.__remove_node(self.__get_node(position))

    def __get_node(self, position: int):
        '''Get node position'''
        if position < self.length / 2:
            node = self.dummy.next
            for x in range(position):
                node = node.next
        else:
            node = self.dummy
            for x in range(self.length, position, -1):
                node = node.previous

        return node

    def __add_before(self, node: Node, label):
        '''add node before a given node'''
        new_node = self.Node(label)
        new_node.previous = node.previous
        new_node.next = node
        new_node.next.previous = new_node
        new_node.previous.next = new_node

        self.length += 1
        return new_node

    def __remove_node(self, node: Node):
        ''' Remove a given node'''
        node.previous.next = node.next
        node.next.previous = node.previous
        self.length -= 1

'''SLL implements a List interface and the operations get(i), set(i,x),add(i,x),remove(i) run in 0(1+min{i,n-i}) time per operation'''

class Node:
    label = None
    previous = None
    next = None

    def __init__(self, label):
        self.label = label


class DoublyLinkedList:
    length = 0
    dummy = Node(None)

    def __init__(self):
        self.dummy.next = self.dummy
        self.dummy.previous = self.dummy

    def __get_node(self, position:int):
        '''Get node position'''
        if position < self.length / 2:
            node = self.dummy.next
            for x in range(position):
                node = node.next
        else:
            node = self.dummy
            for x in range(self.length,position,-1):
                node = node.previous

        return node

    def get(self,position:int):
        ''''Get node value by position'''
        return self.__get_node(position).label

    def get_node_info(self, position: int):
        ''''Get position previous, label and next'''
        info = self.__get_node(position)
        return (info.previous.label,info.label,info.next.label)

    def set(self,position:int,label):
        '''set node value by position'''
        if  0 > position or position > self.length:
            raise IndexError("Invalid possition to set")

        node = self.__get_node(position)
        node_label = node.label
        node.label = label
        return node_label


    def __add_before(self,node:Node,label):
        '''add node before a given node'''
        new_node = Node(label)
        new_node.previous = node.previous
        new_node.next = node
        new_node.next.previous = new_node
        new_node.previous.next = new_node

        self.length+=1
        return new_node


    def add(self,position,label):
        '''Add node in a given position'''
        self.__add_before(self.__get_node(position),label)

    def __remove_node(self,node:Node):
        ''' Remove a given node'''
        node.previous.next = node.next
        node.next.previous = node.previous
        self.length -=1

    def remove(self,position):
        '''Remove a node in a given position'''
        self.__remove_node(self.__get_node(position))

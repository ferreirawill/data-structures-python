'''SLL implements Stack and Queue interfaces and the operations push(x), pop(),add(x),remove() has O(1) complexity'''
from Interfaces.Queue import Queue
from Interfaces.Stack import Stack


class Node:
    label = None
    next = None

    def __init__(self,label):
        self.label = label


class LinkedList(Stack,Queue):
    head = None
    tail = None
    length = 0

    def push(self,label):
        '''Add elements at head'''
        new_node = Node(label)
        new_node.next = self.head
        self.head = new_node

        if self.length == 0:
            self.tail = new_node

        self.length += 1
        return new_node.label

    def pop(self):
        '''Remove elements from head'''
        if self.length == 0: return None

        label = self.head.label
        self.head = self.head.next
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return label

    def remove(self):
        '''Redirect to pop, it is just a queue interface implementation'''
        return self.pop()

    def add(self,label):
        '''Add elements at tail'''
        new_node = Node(label)

        if self.length ==0:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.length +=1
        return new_node.label

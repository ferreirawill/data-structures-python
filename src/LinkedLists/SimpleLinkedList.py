'''SLL implements Stack and Queue interfaces and the operations push(x), pop(),add(x),remove() has O(1) complexity'''
from src.Interfaces.Queue import Queue
from src.Interfaces.Stack import Stack




class SimpleLinkedList(Stack, Queue):
    class Node:
        label = None
        next = None

        def __init__(self, label):
            self.label = label

    def __init__(self):
        self.head: SimpleLinkedList.Node = None
        self.tail: SimpleLinkedList.Node = None
        self.length = 0

    def push(self,label):
        '''Add elements at head'''
        new_node = self.Node(label)
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
        new_node = self.Node(label)

        if self.length ==0:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.length +=1
        return new_node.label

    def find(self,value):
        node = self.head
        list_length = self.length

        while list_length >= 0:
            if value == node.label:
                return node.label
            node = node.next

            list_length -=1

        return None

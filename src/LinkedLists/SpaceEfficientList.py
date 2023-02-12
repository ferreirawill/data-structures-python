class Node:
    next = None
    prev = None
    blockDeque= None

    def __init__(self,label):
        self.label = label

class SpaceEfficientList:
    dummy = Node(None)
    lenght = 0

    def __init__(self):
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def get_location(self,position):

        if position < self.lenght/2:
            node = self.dummy.next

        raise NotImplementedError("Essa lista depende de ArrayLists")
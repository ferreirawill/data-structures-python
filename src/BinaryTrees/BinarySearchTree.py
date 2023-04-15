from src.BinaryTrees.BinaryTree import BinaryTree


class BinarySearchTree(BinaryTree):
    class Node(BinaryTree.Node):
        def __init__(self, value):
            super().__init__(parent=None, left=None, right=None)
            self.value = value

    def __init__(self):
        super().__init__()
        self.root = None
        self.size = 0

    def find_equal(self, value):
        """Find a node with the given value"""
        node = self.root
        while node is not None:
            if value == node.value:
                return node
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return None

    def find(self, value):
        """Find a node or the nearest node with the given value"""
        node = self.root
        found = None
        while node is not None:
            if value < node.value:
                node = node.left
                found = node
            elif value > node.value:
                node = node.right
            else:
                return node.value

        if found is None:
            return None

        return found

    def find_last(self, value):
        node = self.root
        previous = None

        while node is not None:
            previous = node
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return node
        return previous

    def add(self, value):
        """Add a node with the given value"""
        previous = self.find_last(value)
        return self.__add_child(previous, self.Node(value))

    def __add_child(self, previous, new_node):

        if previous is None:
            self.root = new_node

        else:
            if new_node.value < previous.value:
                previous.left = new_node
            elif new_node.value > previous.value:
                previous.right = new_node
            else:  # node.value is already in the tree
                return False

            new_node.parent = previous

        self.size += 1
        return True

    def splice(self, node):
        if node.left is not None:
            child = node.left
        else:
            child = node.right

        if node is self.root:
            self.root = child
            parent = None
        else:
            parent = node.parent
            if parent.left is node:
                parent.left = child
            else:
                parent.right = child

        if child is not None:
            child.parent = parent

        self.size -= 1
        return node.value

    def remove_node(self,node):
        if node.left is None or node.right is None:
            return self.splice(node)
        else:
            successor = node.right
            while successor.left is not None:
                successor = successor.left
            node.value = successor.value
            return self.splice(successor)
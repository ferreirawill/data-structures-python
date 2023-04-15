from src.ArrayLists.ArrayQueue import ArrayQueue


class BinaryTree:
    class Node:
        def __init__(self, parent, left, right):
            self.parent = parent
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def depth(self, node):
        depth = 0
        while node != self.root:
            node = node.parent
            depth += 1
        return depth

    def recursive_size(self, node):
        if node is None:
            return 0
        return 1 + self.recursive_size(node.left) + self.recursive_size(node.right)

    def recursive_height(self, node):
        if node is None:
            return -1
        return 1 + max(self.recursive_height(node.left), self.recursive_height(node.right))

    def recursive_traverse(self, node):
        if node is None:
            return
        self.recursive_traverse(node.left)
        self.recursive_traverse(node.right)

    def traverse(self):
        node = self.root
        previous = None

        while node is not None:
            if previous == node.parent:
                if node.left is not None:
                    next = node.left
                else:
                    next = node.right if node.right is not None else node.parent
            elif previous == node.left:
                next = node.right if node.right is not None else node.parent
            else:
                next = node.parent

            previous = node
            node = next

    def size(self):
        node = self.root
        previous = None
        size = 0
        while node is not None:
            if previous == node.parent:
                size += 1
                if node.left is not None:
                    next = node.left
                else:
                    next = node.right if node.right is not None else node.parent
            elif previous == node.left:
                next = node.right if node.right is not None else node.parent
            else:
                next = node.parent

            previous = node
            node = next

        return size

    def breadth_first_traverse(self):
        queue = ArrayQueue()
        if self.root is not None:
            queue.add(self.root)

        while queue.lenght() > 0:
            node = queue.remove()
            if node.left is not None:
                queue.add(node.left)
            if node.right is not None:
                queue.add(node.right)

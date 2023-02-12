import string
import unittest

from src.ArrayLists.ArrayDeque import ArrayDeque
from src.ArrayLists.ArrayQueue import ArrayQueue
from src.ArrayLists.ArrayStack import ArrayStack


class ArraysStackTests(unittest.TestCase):

    def testArrayStack(self):
        values = [string.ascii_uppercase[i] for i in range(26)]
        ars = ArrayStack()
        for idx, value in enumerate(values):
            ars.add(idx, value)
            print(f"ADDING StackSize: {ars.size()} backing_array: {ars.backing_array}\n")

        print("\n\n\n---------------------------\n\n\n")

        for idx in range(ars.size(), 0, -1):
            ars.remove(idx)
            print(f"REMOVING StackSize: {ars.size()}  backing_array: {ars.backing_array}\n")

class ArrayQueueTests(unittest.TestCase):

    def testArrayQueue(self):
        values = [string.ascii_uppercase[i] for i in range(26)]
        arq = ArrayQueue()
        for i in values:
            arq.add(i)
            # print(f"ADDING StackSize: {arq.lenght} backing_array: {arq.backing_array}\n")

        print("\n\n\n---------------------------\n\n\n")

        for _ in range(arq.lenght):
            removed = arq.remove()
            print(f"REMOVING StackSize: {arq.lenght} - Removed: {removed}\nbacking_array: {arq.backing_array}\n")

class ArrayDequeTests(unittest.TestCase):

    def testArrayQueue(self):
        values = [string.ascii_uppercase[i] for i in range(26)]
        ard = ArrayDeque()
        for idx, value in enumerate(values):
            ard.add(idx,value)
            print(f"ADDING StackSize: {ard.length} backing_array: {ard.backing_array}\n")

        print("\n\n\n---------------------------\n\n\n")

        for idx in range(ard.size()):
            removed = ard.remove(0)
            print(f"REMOVING StackSize: {ard.size()} - Removed: {removed}\nbacking_array: {ard.backing_array}\n")
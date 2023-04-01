import math
import random
import unittest

from src.HashTables.ChainedHashTable import ChainedHashTable


class ChainedHashTableTests(unittest.TestCase):

    def testHandlingElements(self):
        cht = ChainedHashTable()
        number_of_items = 10**6
        for value in range(number_of_items):
            cht.add(value)

        for _ in range((math.floor(number_of_items*0.1))):
            value_to_find = random.randrange(0, number_of_items, 1)
            self.assertEqual(value_to_find,cht.find(value_to_find),f"Value To Find: {value_to_find} | Found Value: {cht.find(value_to_find)}")

        for value in range(number_of_items):
            cht.remove(value)



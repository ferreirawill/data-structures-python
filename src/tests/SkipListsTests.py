import random
import unittest

from src.Skiplists.SkiplistList import SkiplistList
from src.Skiplists.SkiplistSSet import SkiplistSSet


class SkipListSSetTest(unittest.TestCase):

    def testCreateSkipList(self):
        skls = SkiplistSSet()
        self.assertIsInstance(skls, SkiplistSSet)
        self.assertIsInstance(skls.sentinel, SkiplistSSet.Node)
        self.assertEqual(skls.sentinel.label, None)

    def testAddAndRemoveItems(self):
        skls = SkiplistSSet()
        number_of_itens = 100
        for i in range(number_of_itens):
            skls.add(i)

        for i in range(number_of_itens):
            value_to_find = random.randrange(0, number_of_itens)
            self.assertEqual(value_to_find, skls.find(value_to_find))

        for i in reversed(range(number_of_itens)):
            skls.remove(i)

        for i in range(100):
            value_to_find = random.randrange(0, number_of_itens)
            self.assertFalse(skls.find(value_to_find))


class SkiplistListTest(unittest.TestCase):
    def testCreateSkipList(self):
        skll = SkiplistList()
        self.assertIsInstance(skll, SkiplistList)
        self.assertIsInstance(skll.sentinel, SkiplistList.Node)
        self.assertEqual(skll.sentinel.label, None)

    def testAddAndRemoveItems(self):
        skll = SkiplistList()
        number_of_items = 100
        random_list = [random.randrange(0, number_of_items) for _ in range(number_of_items)]
        for i in range(number_of_items):
            skll.add(i, i)

        print("\n---------GETTING AFTER ADD ------------\n")
        for i in random_list:
            print(skll.get(i))

        for i in reversed(range(number_of_items)):
            skll.remove(i)

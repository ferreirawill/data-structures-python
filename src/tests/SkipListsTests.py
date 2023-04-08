import random
import unittest

from src.Skiplists.SkiplistSSet import SkiplistSSet


class SkipListSSetTest(unittest.TestCase):

    def testCreateSkipList(self):
        skls = SkiplistSSet()
        print(skls)
        print(skls.sentinel)
        print(skls.sentinel.label)
        print(skls.sentinel.next)

    def testAddAndRemoveItems(self):
        skls = SkiplistSSet()
        for i in range(100):
            skls.add(i)

        for i in range(100):
            value_to_find = random.randrange(0, 100)
            self.assertEqual(value_to_find, skls.find(value_to_find))

        for i in reversed(range(100)):
            skls.remove(i)

        for i in range(100):
            value_to_find = random.randrange(0, 100)
            self.assertFalse(skls.find(value_to_find))

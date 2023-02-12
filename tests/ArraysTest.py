import string
import unittest

from ArrayLists.ArrayStack import ArrayStack


class ArraysTests(unittest.TestCase):

    def testArrayStack(self):
        values = [string.ascii_uppercase[i] for i in range(26)]
        ars = ArrayStack()
        for value in values:
            ars.add(0,value)
            print(f"Adicionado:{ars.get(0)}")

        for i in ars.length:
            print(f"Índice: {i} | Valor: {ars.get(i)}")


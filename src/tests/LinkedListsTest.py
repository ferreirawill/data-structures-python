import string
import unittest
import random

from src.LinkedLists.DoublyLinkedList import DoublyLinkedList
from src.LinkedLists.SimpleLinkedList import SimpleLinkedList


class SimpleLinkedListTest(unittest.TestCase):

    def testAddAndPush(self):
        labels = [string.ascii_uppercase[i] for i in range(26)]
        pushSll = SimpleLinkedList()
        print("------------- PUSHING ------------------\n")
        for label in labels:
            a = pushSll.push(label)
            print(f"Adicionado:{a} | Head.label: {pushSll.head.label} | "
                  f"Head.next: {pushSll.head.next.label if pushSll.head.next is not None else 'None'} | "
                  f"Tail.label: {pushSll.tail.label} | Tail.label.next: {pushSll.tail.next.label if pushSll.tail.next is not None else 'None'}")

        print("\n\n------------- ADDING ------------------\n")

        addSll = SimpleLinkedList()
        for label in labels:
            a = addSll.add(label)
            print(f"Adicionado:{a} | Head.label: {addSll.head.label} | "
                  f"Head.next: {addSll.head.next.label if addSll.head.next is not None else 'None'} | "
                  f"Tail.label: {addSll.tail.label} | Tail.label.next: {addSll.tail.next.label if addSll.tail.next is not None else 'None'}")


    def testPushandPop(self):
        labels = [string.ascii_uppercase[i] for i in range(26)]
        sll = SimpleLinkedList()
        print("------------- ADICIONANDO ------------------\n")
        for label in labels:
            a = sll.push(label)
            print(f"Adicionado:{a} | Head.label: {sll.head.label} | "
                  f"Head.next: {sll.head.next.label if sll.head.next is not None else 'None'} | "
                  f"Tail.label: {sll.tail.label} | Tail.label.next: {sll.tail.next.label if sll.tail.next is not None else 'None'}")

        print(f'*****TAMANHO: {sll.length}')

        print("\n\n\n------------- REMOVENDO ------------------\n")
        for i in reversed(range(sll.length)):
            a = sll.pop()

            if i == 0:
                print(f"Removido:{a} | Head: {sll.head} | Tail: {sll.tail} ")
                continue

            print(f"Removido:{a} | Head.label: {sll.head.label} | "
                  f"Head.next: {sll.head.next.label if sll.head.next is not None else 'None'} | "
                  f"Tail.label: {sll.tail.label}")

        print(f'*****TAMANHO: {sll.length}')

    def testAddAndRemove(self):
        labels = [string.ascii_uppercase[i] for i in range(26)]
        sll = SimpleLinkedList()
        print("------------- ADICIONANDO ------------------\n")
        for label in labels:
            a = sll.add(label)
            print(f"Adicionado:{a} | Head.label: {sll.head.label} | "
                  f"Head.next: {sll.head.next.label if sll.head.next is not None else 'None'} | "
                  f"Tail.label: {sll.tail.label} | Tail.label.next: {sll.tail.next.label if sll.tail.next is not None else 'None'}")
        print(f'*****TAMANHO: {sll.length}')

        print("\n\n\n------------- REMOVENDO ------------------\n")
        for i in reversed(range(sll.length)):
            a = sll.remove()

            if i == 0:
                print(f"Removido:{a} | Head: {sll.head} | Tail: {sll.tail} ")
                continue

            print(f"Removido:{a} | Head.label: {sll.head.label} | "
                  f"Head.next: {sll.head.next.label if sll.head.next is not None else 'None'} | "
                  f"Tail.label: {sll.tail.label}")

        print(f'*****TAMANHO: {sll.length}')


class DoublyLinkedListTest(unittest.TestCase):

    def testOperations(self):
        labels = [string.ascii_uppercase[i] for i in range(26)]
        dll = DoublyLinkedList()

        for label in reversed(labels):
            dll.add(0, label)

        print(" ---------------- LISTA MONTADA --------------\n")
        for i in range(dll.length):
            node_info = dll.get_node_info(i)
            print(f"Previous: {node_info[0]} |Label: {node_info[1]} | Next: {node_info[2]}")

        print(f'*****TAMANHO: {dll.length}********')
        print("\n\n\n ---------------- LISTA ALTERADA --------------\n")

        dll.set(4, "1")
        dll.set(8, "2")
        dll.set(12, "3")
        dll.set(16, "4")
        for i in range(dll.length):
            node_info = dll.get_node_info(i)
            print(f"Previous: {node_info[0]} |Label: {node_info[1]} | Next: {node_info[2]}")

        print(f'*****TAMANHO: {dll.length}********')
        print("\n\n\n ---------------- NOVOS DADOS --------------\n")

        dll.add(3, "5")
        dll.add(9, "7")
        dll.add(15, "8")
        for i in range(dll.length):
            node_info = dll.get_node_info(i)
            print(f"Previous: {node_info[0]} |Label: {node_info[1]} | Next: {node_info[2]}")

        print(f'*****TAMANHO: {dll.length}********')

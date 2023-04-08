import timeit
import concurrent.futures
import matplotlib.pyplot as plt

from src.LinkedLists.SimpleLinkedList import LinkedList
from src.Skiplists.SkiplistSSet import SkiplistSSet

sizes = [10, 100, 1000, 10000]
skiplist_add_times = []
linked_list_add_times = []
skiplist_find_times = []
linked_list_find_times = []


def add_items_in_LinkedList(size):
    linkedList = LinkedList()
    for i in range(size):
        linkedList.add(i)
    return linkedList


def add_items_in_SkiplistSSet(size):
    skiplistSSet = SkiplistSSet()
    for i in range(size):
        skiplistSSet.add(i)

    return skiplistSSet

def add_items_in_LinearHashTable():
    pass


def find_items_in_LinkedList(linkedList: LinkedList):
    for i in range(linkedList.length):
        linkedList.find(i)


def find_items_in_SkiplistSSet(skls: SkiplistSSet):
    for i in range(skls.size):
        skls.find(i)


def find_items_in_LinearHashTable():
    pass


for size in sizes:
    sll = add_items_in_LinkedList(size)
    skls = add_items_in_SkiplistSSet(size)

    linked_list_add_times.append(timeit.timeit(lambda: add_items_in_LinkedList(size), number=10))
    skiplist_add_times.append(timeit.timeit(lambda: add_items_in_SkiplistSSet(size), number=10))

    linked_list_find_times.append(timeit.timeit(lambda: find_items_in_LinkedList(sll), number=10))
    skiplist_find_times.append(timeit.timeit(lambda: find_items_in_SkiplistSSet(skls), number=10))

plt.plot(sizes, linked_list_add_times, label='Linkedlist')
plt.plot(sizes, skiplist_add_times, label='SkilList add')
plt.legend()
plt.xlabel('Input size')
plt.ylabel('Time (seconds)')
plt.title('Comparison of LinkedList e and SkipList for add operation')
plt.show()

plt.plot(sizes, linked_list_find_times, label='Linkedlist Find')
plt.plot(sizes, skiplist_find_times, label='Skiplist Find')
plt.legend()
plt.xlabel('Input size')
plt.ylabel('Time (seconds)')
plt.title('Comparison of LinkedList and SkipList for find operation')
plt.show()

from src.HashTables.ChainedHashTable import ChainedHashTable
from src.HashTables.LinearHashTable import LinearHashTable
from src.LinkedLists.DoublyLinkedList import DoublyLinkedList
from src.LinkedLists.SimpleLinkedList import SimpleLinkedList
from src.Skiplists.SkiplistList import SkiplistList
from src.Skiplists.SkiplistSSet import SkiplistSSet


class DataHandler:
    def __init__(self):
        self.simple_linkedlist = SimpleLinkedList()
        self.doubly_linkedlist = DoublyLinkedList()
        self.skiplist_list = SkiplistList()
        self.skiplist_sset = SkiplistSSet()
        self.chained_hashtable = ChainedHashTable()
        self.linear_hashtable = LinearHashTable()

    def add_items_to_simple_linkedlist(self, number_of_items):
        for i in range(number_of_items):
            self.simple_linkedlist.add(i)

    def add_items_to_doubly_linkedlist(self, number_of_items):
        for i in range(number_of_items):
            self.doubly_linkedlist.add(i, i)

    def add_items_to_skiplist_list(self, number_of_items):
        for i in range(number_of_items):
            self.skiplist_list.add(i, i)

    def add_items_to_skiplist_sset(self, number_of_items):
        for i in range(number_of_items):
            self.skiplist_sset.add(i)

    def add_items_to_chained_hashtable(self, number_of_items):
        for i in range(number_of_items):
            self.chained_hashtable.add(i)

    def add_items_to_linear_hashtable(self, number_of_items):
        for i in range(number_of_items):
            self.linear_hashtable.add(i)

    def find_items_in_simple_linkedlist(self, number_of_items):
        for i in range(number_of_items):
            self.simple_linkedlist.find(i)

    def find_items_in_doubly_linkedlist(self, number_of_items):
        for i in range(number_of_items):
            self.doubly_linkedlist.get(i)

    def find_items_in_skiplist_list(self, number_of_items):
        for i in range(number_of_items):
            self.skiplist_list.get(i)

    def find_items_in_skiplist_sset(self, number_of_items):
        for i in range(number_of_items):
            self.skiplist_sset.find(i)

    def find_items_in_chained_hashtable(self, number_of_items):
        for i in range(number_of_items):
            self.chained_hashtable.find(i)

    def find_items_in_linear_hashtable(self, number_of_items):
        for i in range(number_of_items):
            self.linear_hashtable.find(i)

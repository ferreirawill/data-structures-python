import math
import timeit
import matplotlib.pyplot as plt
from src.DataHandler import DataHandler

data_handler = DataHandler()
sizes = []
skiplist_add_times = []
linked_list_add_times = []
hashtable_add_times = []
hashtable_find_times = []
skiplist_find_times = []
linked_list_find_times = []
ideal_curve_values = []

for size in range(10, 10000, 100):
    sizes.append(size)
    ideal_curve_values.append(math.log10(size))

    skiplist_add_times.append(timeit.timeit(lambda: data_handler.add_items_to_skiplist_sset(size), number=10))
    skiplist_find_times.append(timeit.timeit(lambda: data_handler.find_items_in_skiplist_sset(size),number=10))

#plt.plot(sizes, linked_list_add_times, label='Linkedlist add')
plt.plot(sizes, ideal_curve_values, label='Ideal')
plt.plot(sizes, skiplist_add_times, label='Skiplist add')
#plt.plot(sizes, hashtable_add_times, label='Hashtable add')
plt.legend()
plt.xlabel('Input size')
plt.ylabel('Time (seconds)')
plt.title('Comparison of SimpleLinkedList, SkipList and ChainedHashTable for add operation')
plt.show()

#plt.plot(sizes, linked_list_find_times, label='Linkedlist Find')
plt.plot(sizes, ideal_curve_values, label='Ideal')
plt.plot(sizes, skiplist_find_times, label='Skiplist Find')
#plt.plot(sizes, hashtable_add_times, label='Hashtable Find')
plt.legend()
plt.xlabel('Input size')
plt.ylabel('Time (seconds)')
plt.title('Comparison of SimpleLinkedList, SkipList and ChainedHashTable for find operation')
plt.show()

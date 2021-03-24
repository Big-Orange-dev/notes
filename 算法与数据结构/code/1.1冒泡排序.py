import time


def bubble_sort(items, comp=lambda x, y: x > y):

    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
                swapped = True
        if not swapped:
            break
    return items

import random
my_list = list(set(range(50)))
random.shuffle(my_list)
print(my_list)
result = bubble_sort(my_list)
print(result)

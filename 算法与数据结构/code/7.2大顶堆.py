import random


def heapify(items, i):
    left = 2*i+1
    right = 2*i+2
    largest = i

    if left < len(items)-1 and items[left] > items[largest]:
        largest = left
    if right < len(items)-1 and items[right] > items[largest]:
        largest = right
    if largest != i:
        swap(items, i, largest)
        heapify(items, largest)
    return items


def swap(items, i, j):
    items[i], items[j] = items[j], items[i]


my_list = list(range(9))
random.shuffle(my_list)
print(my_list)
result = heapify(my_list)
print(result)

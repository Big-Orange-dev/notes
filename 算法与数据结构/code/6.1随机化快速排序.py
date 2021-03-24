import profile
import random


def quickSort(items, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(items)-1 if not isinstance(right, (int, float)) else right
    if left < right:
        partitionIndex = partition(items, left, right)
        quickSort(items, left, partitionIndex-1)
        quickSort(items, partitionIndex+1, right)
    return items


def partition(items, left, right):
    pivot = left
    index = pivot+1
    i = index
    while i <= right:
        if items[i] < items[pivot]:
            swap(items, i, index)
            index += 1
        i += 1
    swap(items, pivot, index-1)
    return index-1


def swap(items, i, j):
    items[i], items[j] = items[j], items[i]


my_list = list(range(100))
random.shuffle(my_list)
print(my_list)
result = quickSort(my_list)
print(result)
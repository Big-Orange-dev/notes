import random


def quickSort2way(items, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(items)-1 if not isinstance(right, (int, float)) else right
    if left < right:
        partitionIndex = partition(items, left, right)
        quickSort2way(items, left, partitionIndex-1)
        quickSort2way(items, partitionIndex+1, right)
    return items


def partition(items, left, right):
    i = left + 1
    j = right
    while True:
        while i <= right and items[i] < items[left]:
            i += 1
        while j >= left + 1 and items[j] > items[left]:
            j -= 1
        if i > j:
            break
        else:
            swap(items, i, j)   
            i += 1
            j -= 1
    swap(items, left, j)
    return j


def swap(items, i, j):
    items[i], items[j] = items[j], items[i]


my_list = list(range(10))
random.shuffle(my_list)
print(my_list)
result = quickSort2way(my_list)
print(result)

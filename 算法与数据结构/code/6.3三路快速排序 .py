import random


def quickSort3way(items, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(items)-1 if not isinstance(right, (int, float)) else right
    if left < right:
        partitionIndex, partitionIndey = partition(items, left, right)
        quickSort3way(items, left, partitionIndex-1)
        quickSort3way(items, partitionIndey, right)
    return items


def partition(items, left, right):
    if left < right:
        lt = left
        gt = right+1
        i = left + 1
        while i < gt:
            if items[i] < items[left]:
                swap(items, i, lt+1)
                lt += 1
                i += 1
            elif items[i] > items[left]:
                swap(items, i, gt-1)
                gt -= 1
            else:
                i += 1
    swap(items, left, lt)
    return i, gt


def swap(items, i, j):
    items[i], items[j] = items[j], items[i]


my_list = list(range(10))
random.shuffle(my_list)
print(my_list)
result = quickSort3way(my_list)
print(result)

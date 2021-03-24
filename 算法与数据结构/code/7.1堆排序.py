def buildMaxHeap(items):
    import math
    # math.floor() 向下取整
    for i in range(math.floor(len(items)/2),-1,-1):
        heapify(items,i)

def heapify(items, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < itemsLen and items[left] > items[largest]:
        largest = left
    if right < itemsLen and items[right] > items[largest]:
        largest = right

    if largest != i:
        swap(items, i, largest)
        heapify(items, largest)

def swap(items, i, j):
    items[i], items[j] = items[j], items[i]

def heapSort(items):
    global itemsLen
    itemsLen = len(items)
    buildMaxHeap(items)
    for i in range(len(items)-1,0,-1):
        swap(items,0,i)
        itemsLen -=1
        heapify(items, 0)
    return items


import random
my_list = list(range(50))
random.shuffle(my_list)
print(my_list)
result = heapSort(my_list)
print(result)

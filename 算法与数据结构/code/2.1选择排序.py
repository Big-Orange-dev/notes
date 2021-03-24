def selectionSort(items):
    for i in range(len(items) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(items)):
            if items[j] < items[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            items[i], items[minIndex] = items[minIndex], items[i]
    return items

import random
my_list = list(set(range(50)))
random.shuffle(my_list)
print(my_list)
result = selectionSort(my_list)
print(result)

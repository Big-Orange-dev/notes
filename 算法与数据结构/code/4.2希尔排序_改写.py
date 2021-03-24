def shell_sort(items,comp=lambda x,y:x>y):
    n = len(items)
    # gap = 1 时就是一个插入排序
    # gap > 1时优化算法，将小的数移到前面
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            for j in range(i,-1,-gap):
                if j-gap>=0 and comp(items[j-gap],items[j]):
                    items[j],items[j-gap] = items[j-gap],items[j]
        gap = gap // 2
    return items

import random
my_list = list(set(range(50)))
random.shuffle(my_list)
print(my_list)
result = shell_sort(my_list)
print(result)

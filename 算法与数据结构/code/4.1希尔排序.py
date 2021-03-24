'''

    希尔排序，目的是优化插入排序
        1.让小数去到左边
    适用于中等大小规模
    又称 --> 减少增量排序

'''


def shell_sort(items):
    n = len(items)
    # gap = 1 时就是一个插入排序
    # gap > 1时优化算法，将小的数移到前面
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            tmp = items[i]
            j = i
            while j >= 0 and j-gap >= 0 and items[j-gap] > tmp:
                items[j] = items[j-gap]
                j -= gap
            items[j] = tmp
        gap = gap // 2
    return items


my_list = [5, 1145, 2452, 645, 678, 4678, 365, 256, 5675367, 567,
           7589, 3, 1, 6, 4, 9, 8, 7, 2, 542, 36, 4678, 7858, 2542, ]

result = shell_sort(my_list)
print(result)

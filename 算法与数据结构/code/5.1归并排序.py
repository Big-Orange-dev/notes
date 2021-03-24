import random


def merge_sort(items, comp=lambda x, y: x <= y):
    ''' 并归排序，适用于数据量大的场景 '''

    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    result = []
    while left and right:
        if comp(left[0], right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result


my_list = list(set(range(50)))
random.shuffle(my_list)
print(my_list)
result = merge_sort(my_list)
print(result)

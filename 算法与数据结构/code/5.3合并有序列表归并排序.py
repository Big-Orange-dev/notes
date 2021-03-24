def merge(items1, items2, comp=lambda x, y: x < y):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items

def merge_sort(items):
    """
    归并排序
    将数列拆分为只有一个元素的数列再利用merge()函数合并
    """
    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)

mylist1 = [1, 3, 5, 7, 9,345,25,56,2,85,345,68,2546,67598,4125,6735,24,23]

print(merge_sort(mylist1))

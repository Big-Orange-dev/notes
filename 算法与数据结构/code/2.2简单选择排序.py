def select_sort(items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i+1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


mylist = [34, 64, 12, 6, 456, 41, 5, 56, 26, 7, 27, 2356, 23]
a = select_sort(mylist)
print(a)

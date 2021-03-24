

def merge(items1, items2, comp=lambda x, y: x < y):
    '''合并两个有序列表为一个有序列表'''
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

mylist1 = [1, 3, 5, 7, 9]
mylist2 = [2, 4, 6, 8, 10]
print(merge(mylist1, mylist2))

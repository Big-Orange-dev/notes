my_list = [88, 6, 9, 1, 4, 6, 7, 2, 5687, 2,
           5, 23, 43, 462, 254, 2451, 145, 51, 0, 578]


def insert_sort(items, comp=lambda x, y: x < y):
    for i in range(len(my_list)-1):
        if comp(items[i], items[i+1]):
            continue
        else:
            items[i], items[i+1] = items[i+1], items[i]
            for j in range(i, 0, -1):
                if comp(items[j], items[j-1]):
                    items[j], items[j-1] = items[j-1], items[j]

    return items


print(insert_sort(my_list))

def seq_search(items,key):
    '''顺序找查'''

    for index,item in enumerate(items):
        if item == key:
            return index
    return -1

mylist = [3,45,36,26,12,587,36,567,3,6,2,5465,45]
print(seq_search(mylist,45))
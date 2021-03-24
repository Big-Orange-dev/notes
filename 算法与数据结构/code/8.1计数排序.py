def countingSort(arr, maxValue):
    bucketLen = maxValue+1
    
    bucket = [0]*bucketLen
    sortedIndex =0
    arrLen = len(arr)
    for i in range(arrLen):
        if not bucket[arr[i]]:
            bucket[arr[i]]=0
        bucket[arr[i]]+=1
    for j in range(bucketLen):
        while bucket[j]>0:
            arr[sortedIndex] = j
            sortedIndex+=1
            bucket[j]-=1
    return arr


import random
my_list = [1,1,1,2,2,2,4,4,2,1,2,3,2,3,3,2,2,3,4,4,6,3,2]
random.shuffle(my_list)
print(my_list)
result = countingSort(my_list,6)
print(result)

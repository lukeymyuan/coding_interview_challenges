#!/usr/bin/python3

def countPairsWithSum(arr, sum):
    count = 0
    freq = {}
    for x in arr:
        if x not in freq:
            freq[x] = 1
        else:
            freq[x]+=1
    for x in arr:
        if (sum-x) in freq:
            count += freq[sum-x]
        if sum-x == x:
            count -=1
    return int(count/2)

arr = [ 1, 5, 7, -1 ]
sum = 6
print (countPairsWithSum(arr, sum))
arr = [ 1, 1, 1, 1 ]
sum = 2
print (countPairsWithSum(arr, sum))

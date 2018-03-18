#!/bin/python3

import sys

# O(n^2) time
def longestIncreasingSubsequence(arr):
    lis = [1]*len(arr)
    for i in range (1, len(arr)):
        for j in range (0, i):
             if arr[j]<arr[i]:
                    lis[i] = max(lis[i], lis[j]+1)
    return max(lis)
                    
    

if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(n):
       arr_t = int(input().strip())
       arr.append(arr_t)
    result = longestIncreasingSubsequence(arr)
    print(result)

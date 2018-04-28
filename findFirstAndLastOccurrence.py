#!/usr/bin/python3
# Given a sorted array with possibly duplicate elements, 
# the task is to find indexes of first and last occurrences of an element x in the given array.
# https://www.geeksforgeeks.org/find-first-and-last-positions-of-an-element-in-a-sorted-array/

def first(arr,x):
    low, high = 0, len(arr)
    result = -1
    while low<=high:
        mid = low +(high-low)//2 # avoid overflow
        if arr[mid]==x:
            result = mid
            high = mid-1
        elif arr[mid]<x:
            low = mid+1
        elif arr[mid]>x:
            high = mid-1
    return result


def last(arr,x):
    low, high = 0, len(arr)
    result = -1
    while low<=high:
        mid = low +(high-low)//2 # avoid overflow
        if arr[mid]==x:
            result = mid
            low = mid+1
        elif arr[mid]<x:
            low = mid+1
        elif arr[mid]>x:
            high = mid-1
    return result

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print("First Occurrence = ", first(arr,x))
print("Last Occurrence = ", last(arr,x))

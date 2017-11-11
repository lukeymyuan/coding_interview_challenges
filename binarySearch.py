#!//usr/bin/python2

def iterativeBinarySearch(arr, l, r, x):
    while l<=r:
        mid = (l+r)/2
        if(arr[mid] ==x ):
            return mid
        elif(mid<x):
            l = mid+1
        else:
            r =mid-1
    return -1

def recursiveBinarySearch(arr, l, r, x):
    if(l>r):
        return -1
    mid = (l+r)/2
    if(arr[mid] ==x ):
        return mid
    elif(mid<x):
        return recursiveBinarySearch(arr, l+1, r, x)
    else:
        return recursiveBinarySearch(arr, l, r-1, x)


# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

method = raw_input('iterative or recursive?\n')
if method == "iterative":
    print "implemeting iterative method..."
    result = iterativeBinarySearch(arr, 0, len(arr)-1, x)
elif method == "recursive":
    print "implemeting recurssive method..."
    result = recursiveBinarySearch(arr, 0, len(arr)-1, x)
else:
    print "please enter either iterative or recursive"
    quit()


if result != -1:
    print "Element is present at index %d" % result
else:
    print "Element is not present in array"

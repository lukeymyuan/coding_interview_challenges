# https://www.geeksforgeeks.org/shuffle-a-given-array/

import random
def shuffleArray(arr):
    for i in range(len(arr)):
        j = random.randint(0,i)
        arr[i],arr[j]=arr[j],arr[i]
    return arr
    

print(shuffleArray([1,2,3,4,5]))

def longestConsecutiveCharacters(string):
    prev=None
    maxCount=0
    count=1
    maxChar=None
    for curr in string:
        if curr == prev:
            count+=1
        else:
            count = 1
        if count>maxCount:
            maxCount=count
            maxChar=curr
        prev=curr
    return {maxChar:maxCount}

string = "AABCDDDDBBBBBEA"
print(longestConsecutiveCharacters(string))

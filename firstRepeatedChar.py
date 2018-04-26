#!/usr/bin/python3
def firstRepeatedChar(str):
    seen=[]
    for ch in str:
        if ch in seen:
            return ch
        else:
            seen.append(ch)
    return "no char is repeated"

print(firstRepeatedChar("Luke"))
print(firstRepeatedChar("Luke Yuan"))   #output u

# https://www.geeksforgeeks.org/square-root-of-an-integer/

def squareRoot(input):
    i=1
    result =1
    while result<input:
        i+=1
        result =i*i
    return i-1

print(squareRoot(0))
print(squareRoot(16))
print(squareRoot(50))

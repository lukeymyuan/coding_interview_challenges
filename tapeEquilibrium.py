def solution(A):
    min, sumL, sumR = 2000, 0, sum(A)
    for counter in range(1,len(A)):
        sumL += A[counter-1]
        sumR -= A[counter-1]
        diff = abs(sumL-sumR)
        if diff < min:
            min = diff
return min

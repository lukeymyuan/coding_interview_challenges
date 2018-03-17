def solution(A):
    if(len(A)<3):
        return 0
    A.sort()
		
    for i in range (0, len(A)-2):
        # check adjacent values as they provide the highest value
				if A[i] + A[i+1] > A[i+2]:
            return 1
    return 0

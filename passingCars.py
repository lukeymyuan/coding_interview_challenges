def solution(A):
    # record the east car, when west is encountered, increment east
    east, pairs = 0, 0
    for counter in range (0,len(A)):
        if A[counter] == 0:
            east += 1
        elif A[counter] == 1:
            pairs += east
    if pairs > 1000000000:
        return -1
    else:
        return pairs

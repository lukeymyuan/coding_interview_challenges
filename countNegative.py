# Count Negative Numbers in a Column-Wise and Row-Wise Sorted Matrix
# https://www.geeksforgeeks.org/count-negative-numbers-in-a-column-wise-row-wise-sorted-matrix/

def countNegative(M,r,c):
	count = 0
	# start at top right corner
	i = 0
	j = c-1
	while i<r and j>=0:
		if M[i][j]>=0:
			j-=1
		else:
			count += j+1
			i+=1
	return count

M = [ 
      [-3, -2, -1,  1],
      [-2,  2,  3,  4],
      [4,   5,  7,  8]
    ]
print(countNegative(M, 3, 4))

# Python program for the above approach

import math
m = 10**9 + 7

# Function to find the value of x ^ y
def power(x, y):

	# Stores the value of x ^ y
	res = 1
	
	# Iterate until y is positive
	while y > 0:
	
		# If y is odd
		if (y & 1) != 0:
			res = (res * x) % m
			
		# Divide y by 2
		y = y >> 1
		
		x = (x * x) % m
		
	# Return the value of x ^ y
	return res

# Function to find the number of N-digit
# integers satisfying the given criteria
def countNDigitNumber(n: int) -> None:
	
	# Count of even positions
	ne = N // 2 + N % 2
	
	# Count of odd positions
	no = N // 2
	
	# Return the resultant count
	return power(4, ne) * power(5, no)

# Driver Code
if __name__ == '__main__':
	
	N = 5
	print(countNDigitNumber(N) % m)

import sys

# The solution to the problem is as follows:
#       1. find the greatest divisor for a number
#       2. subtract that greatest divisor from the number
#       3. ++count
#       4. if the new number is > 1 , go back to step 1,
#           else if number == 1, ++count

# greatestdivisor(int )
# returns the greatest divisor other than the parameter itself
# input: an integer N
# output: greatest divisor for N other than N itself
def greatestdivisor(N) :
	D = N - 1
	while (N % D != 0) :
		D -= 1
	return D


N = int(sys.stdin.readline())
count = 0
while (N > 0) :
	if N > 1 :
		N -= greatestdivisor(N)
	elif N == 1 :
		N -= 1
	count += 1
print(count)

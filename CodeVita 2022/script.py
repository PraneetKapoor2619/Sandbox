import re
import sys
# Main body of the code
C, N = sys.stdin.readline().split()
C = int(C)
N = int(N)

S = re.findall("[0-9]+", sys.stdin.readline())
data = [re.findall("[0-9.]+", sys.stdin.readline()) for i in range(N)]

S = list(map(lambda x:int(x), S))
data = sorted(data, key = lambda x:(-float(x[1]),int(x[0])))

for i in range(N):
	for choice in data[i][2:]:
		if(S[int(choice) - 1] > 0):
			S[int(choice) - 1] -= 1
			print("Student-" + data[i][0] + " C-" + choice)
			break

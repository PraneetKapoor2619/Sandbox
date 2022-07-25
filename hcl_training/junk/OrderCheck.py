def countStudents(heights):
	sorted_heights = sorted(heights)
	diffs = [1 if (heights[i] != sorted_heights[i]) else 0 for i in range(len(heights))]
	return sum(diffs)


if __name__ == "__main__" :
	import os
	os.environ["OUTPUT_PATH"] = "input.txt"
	fptr = open(os.environ["OUTPUT_PATH"], 'r')
	height_count = int(input().strip())
	height = []

	for _ in range(height_count) :
		height.append(int(input()))
	print(countStudents(height))
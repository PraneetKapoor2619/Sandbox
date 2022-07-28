import random
import time


if __name__ == "__main__" :
	array = sorted([random.randint(0, 100) for _ in range(100)])

	time_array = []
	for _ in range(1000) :
		element = random.randint(0, 100)
		index = None
		left_limit = 0
		right_limit = len(array) - 1

		start_time = time.time()
		while left_limit <= right_limit :
			m = (left_limit + right_limit) // 2
			if (array[m] == element) :
				index = m
				break
			elif (array[m] < element) :
				left_limit = m + 1
			elif (array[m] > element) :
				right_limit = m - 1
		end_time = time.time()
		print(element, "found at index", index, "in", end_time - start_time, "seconds")
		time_array.append(end_time - start_time)
	print("Average time required to find an element using binary search is",\
	sum(time_array)/len(time_array), "seconds")

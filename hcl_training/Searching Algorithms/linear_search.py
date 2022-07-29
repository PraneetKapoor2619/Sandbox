import random
import time


if __name__ == "__main__" :
	array = sorted([random.randint(0, 100) for i in range(100)])

	time_array = []
	for _ in range(1000) :
		element = random.randint(0, 100)
		index = None
		
		start_time = time.time()
		for i in range(len(array)):
			if (array[i] == element) :
				index = i
				break
		end_time = time.time()
		print(element, "found at index", index, "in", end_time - start_time, "seconds")
		time_array.append(end_time - start_time)

	print("Average time required in finding an element using linear search:",\
	sum(time_array) / len(time_array))
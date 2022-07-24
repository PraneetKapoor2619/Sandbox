import time
import threading


def function1():

	for i in range(100000) :
		print("1", end = " ")


def function2():

	for i in range(100000) :
		print("2", end = " ")


if __name__ == "__main__" :

	thread1 = threading.Thread(target = function1)
	thread2 = threading.Thread(target = function2)

	start_time = time.time()

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

	end_time = time.time()

	print("Execution completed in", end_time - start_time, "seconds.")
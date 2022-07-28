import threading


def function1(iterations, lock):
	lock.acquire()
	for i in range(iterations) :
		print("1", end = " ")
	lock.release()


def function2(iterations, lock):
	lock.acquire()
	for i in range(iterations) :
		print("2", end = " ")
	lock.release()


if __name__ == "__main__" :
	iterations = 100000
	lock = threading.Lock()

	thread1 = threading.Thread(target = function1, args = (iterations, lock))
	thread2 = threading.Thread(target = function2, args = (iterations, lock))

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

	print()
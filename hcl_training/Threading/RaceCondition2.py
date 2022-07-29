import time
import threading


resource = 0


def function1(num):
	global resource
	for i in range(100000000) :
		resource += num


if __name__ == "__main__" :
	thread1 = threading.Thread(target = function1, args = (1, ))
	thread2 = threading.Thread(target = function1, args = (-1, ))

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

	print(resource)
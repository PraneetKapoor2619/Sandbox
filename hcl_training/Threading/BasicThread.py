import threading
import time


def greeting_1():
	
	for i in range(6) :
		time.sleep(0.5)
		print("Hello")


def greeting_2():

	for i in range(6) :
		time.sleep(0.5)
		print("World")


if __name__ == "__main__" :

	# function invokation without any threading
	start_time = time.time()
	
	greeting_1()
	greeting_2()

	end_time = time.time()

	print("Total time for execution: ", end_time - start_time)

	# function invokation with threading

	start_time = time.time()

	thread1 = threading.Thread(target = greeting_1)
	thread2 = threading.Thread(target = greeting_2)

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

	end_time = time.time()

	print("Total time for execution: ", end_time - start_time)
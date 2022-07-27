def natural(limit):
	if (limit <= 0) : raise ValueError("Limit cannot be less than 1")
	elif (type(limit) is not int): raise TypeError("Limit should be of int type") 

	n = 1
	while (n <= limit) :
		yield n
		n += 1


if __name__ == "__main__" :
	nn_generator = natural(10)

	while True :
		print(next(nn_generator))
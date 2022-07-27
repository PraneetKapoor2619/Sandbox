def fibonacci(terms):
	if (terms <= 0) : raise ValueError("No. of terms cannot be less than 1")
	elif (type(terms) is not int) : raise TypeError("No. of terms should be an integer")

	previous = 0
	current = 1
	i = 1
	while (i <= terms) : 
		yield previous
		previous, current = current, previous + current
		i += 1


if __name__ == "__main__" :
	fib10 = fibonacci(10)
	for term in fib10 :
		print(term)
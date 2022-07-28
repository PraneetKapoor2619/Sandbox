def decorator_factory(argument):
	def decorator(function):
		def wrapper(arg1):
			if (argument == 1) :
				if (arg1 < 0) :
					print("Argument should not be less than zero.")
					return None
				return function(arg1)
			elif (argument == 2) :
				if (type(arg1) is not list) :
					print("Argument should be a list")
					return None
				return function(arg1)
		return wrapper
	return decorator


@decorator_factory(1)
def factorial(number) :
	if (number == 0) :
		return 1
	
	result = number * factorial(number - 1)
	return result


@decorator_factory(2)
def squared(list1):
	print([x ** 2 for x in list1])


def cubed(list1):
	print([x ** 3 for x in list1])


if __name__ == "__main__" :
	print("Factorial of 5 is:", factorial(5))
	print("Factorial of -5 is:", factorial(-5))

	squared(list(range(10)))
	squared(12)
	
	dec_ref = decorator_factory(2)
	wrap_ref = dec_ref(cubed)
	wrap_ref(list(range(10)))
	wrap_ref(15)
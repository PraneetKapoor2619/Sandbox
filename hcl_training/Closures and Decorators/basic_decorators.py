def decorator(func):
	def closure(args):
		nonlocal func
		if (type(args) is not int) :
			#raise TypeError("Argument should be an int")
			print("Argument should be an int")
			return None
		return func(args)
	return closure


def function1(number):
	print("Square of", number, "is:", number ** 2)


@decorator
def function2(number):
	print("Square of", number, "is:", number ** 2)


if __name__ == "__main__" :
	print("Using a decorator manually")
	func_ref1 = decorator(function1)
	func_ref1(11)
	func_ref1([1, 2, 3])

	print("Using a decorator using @ syntax")
	function2(9)
	function2({'a': 1, 'b': 2, 'c': 3})
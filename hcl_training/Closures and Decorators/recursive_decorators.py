def isNegative(func):
	def check(number):
		nonlocal func
		if (number < 0) : 
			raise ValueError("Value cannot be negative")
		print(number)
		return func(number)
	return check


@isNegative
def factorial(number):
	if (number == 0) : 
		return 1 
	result = number * factorial(number - 1)
	return result


if __name__ == "__main__" :
	number = int(input("Enter a number: "))
	print("Factorial of", number, "=", factorial(number))
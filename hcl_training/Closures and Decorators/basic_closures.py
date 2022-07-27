def outer_function():
	const1 = 0

	def inner_function():
		nonlocal const1
		const1 += 1
		print("S:", const1)
	
	return inner_function


if __name__ == "__main__" :
	ref_inner_function1 = outer_function()
	ref_inner_function2 = outer_function()
	for i in range(5) :
		ref_inner_function1()
	
	del(outer_function)

	try :
		ref_inner_function_3 = outer_function()
	
	except (BaseException, ZeroDivisionError) as exception :
		print(exception)
	
	try :
		ref_inner_function1()
		ref_inner_function2()
		print("Inner function still lives on. It contains a free variable")
	
	except (BaseException, ZeroDivisionError) as exception :
		print(exception)

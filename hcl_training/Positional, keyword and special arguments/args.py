def func1(*args):
	for argument in args :
		print(argument, end = " ")
	print("")


def func2(args):
	for argument in args :
		print(argument, end = " ")
	print("")


def func3(**kwargs):
	for k, v in kwargs.items() :
		print(k, v)

list1 = list(range(5))
func1(list1)
func1(*list1)
func2(list1)
func3(**{"Name": "Praneet Kapoor", "Job": "Developer"})
func3(**{"Name": "R2D2", "Job": "Nothing"})
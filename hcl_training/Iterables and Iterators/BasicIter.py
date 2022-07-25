list1 = [i for i in range(10)]

"""
A list is an iterable but it is not itself an iterator. Only an iterator object can go through a 
list or any other iterable object and fetch its contituents.
"""

try :
	next(iter)
except (BaseException) as e :
	print(e)

"""
To generate an iterator for a list, use iter() method. Then pass this object as an argument to 
the next() built-in function.
"""

iterable_object = iter(list1)
print(type(iterable_object))

while True :
	print(next(iterable_object))
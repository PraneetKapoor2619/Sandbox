"""
Write a python program to create a lambda function that returns
a square value of a given number.
"""

square = lambda x: x ** 2

num = int(input())
print("The square of {:d} is {:d}".format(num, square(num)))
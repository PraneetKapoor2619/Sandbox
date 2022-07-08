"""
Write a function decorator to calculate factorial, when it’s get applied on a given function.
"""

import math

def factorial(func):
        result = 1
        def __factorial__(number):
                nonlocal result
                if (number < 0) : 
                        raise ValueError("Factorial of a negative integer cannot be computed!")
                elif (number == 1 or number == 0) :
                        return result
                else :
                        tmp = number
                        while (tmp > 0) :
                                result *= tmp
                                tmp -= 1
                print("Factorial of the number passed is:", result)
                return func(number)
        return __factorial__

@factorial
def area_of_circle(r):
        print("Area of circle with radius {:d} units is {:.2f} sq. units"\
        .format(r, math.pi * r * r))

if __name__ == "__main__" :
        radius = int(input("Enter a positive integer: "))
        area_of_circle(radius)
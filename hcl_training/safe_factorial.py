def ispositive(func):

        def check(number):
                if number < 0:
                        raise ValueError("Factorial of a negative number cannot be computed")
                else:
                        return func(number)

        return check

@ispositive
def factorial(n):

        if (n == 0):
                return 1

        return n * factorial(n - 1)

print(factorial(5))
print(factorial(4))
print(factorial(-2))
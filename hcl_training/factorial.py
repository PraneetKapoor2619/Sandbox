import sys

def factorial(num):

        if num < 0:
                print("Factorial doesn't exist for negative numbers")
                return float("nan")

        if num == 0:
                return 1
        
        fact = num * factorial(num - 1)
        return fact

print(factorial(int(sys.argv[1])))
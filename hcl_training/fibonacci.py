import sys

def fibonacci(a, b, i, terms):

        if i >= terms:
                return 0
        
        print(a + b, end = " ")
        fibonacci(b, a + b, i + 1, terms)
        return 0

fibonacci(-1, 1, 0, int(sys.argv[1]))
print("")
import sys

def fibonacci(a, b, i, terms):

        if i >= terms:
                return

        fib_series.append(a + b)
        fibonacci(b, a + b, i + 1, terms)
        return

fib_series = []
fibonacci(-1, 1, len(fib_series), int(sys.argv[1]))
print(fib_series)
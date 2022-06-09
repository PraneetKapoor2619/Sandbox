cube = lambda x: x ** 3 

def fibonacci(n):
        fib_series = []
        for i in range(n):
                if (i == 0): 
                        fib_series.append(0)
                elif (i == 1):
                        fib_series.append(1)
                else:
                        last = len(fib_series) - 1
                        fib_series.append(fib_series[last - 1] + fib_series[last])
        return fib_series

if __name__ == '__main__':
        n = int(input())
        print(list(map(cube, fibonacci(n))))
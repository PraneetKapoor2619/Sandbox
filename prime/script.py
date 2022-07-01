import numpy as np
import matplotlib.pyplot as plt


def isprime(N):
    for n in range(2, int(N / 2) + 1):
        if (N % n == 0):
            return 1
    return 0

list_main = []
for N in range(2, 100):
    if(isprime(N) == 0):
        list_main.append(N)
list1 = [round(0.1 * p, 1) for p in list_main]
list_main += list1
list_main.sort()
print(list_main)
pi_func = []
pi = 0
x = np.arange(1, 100, 0.1)
x = [round(n, 1) for n in x]
for n in x:
    if(n in list_main):
        print("Here")
        pi += 1
    pi_func.append(pi)
plt.plot(x, pi_func, 'r*')
plt.show()
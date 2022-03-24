import numpy as np
import matplotlib.pyplot as plt

size = [2, 5, 10, 25, 75, 100]
python3 = [8.57E+05, 7.92E+05, 7.16E+05, 4.20E+05, 4.60E+03, 2.72E+03]
matlab2021 = [1.92e+06, 1.73e+06, 1.21e+06, 6.98e+05, 8.10e+04, 4.57e+04]
gpp11 = [2.75e+07, 2.40e+06, 2.16e+04, 1.83e+04, 3.75e+02, 1.50e+02]

plt.xlabel("Dimension of square matrix")
plt.ylabel("No. of matrices multiplied per second")
plt.plot(size, python3, 'r', label = 'python3')
plt.plot(size, matlab2021, 'b', label = 'matlab2021')
plt.plot(size, gpp11, 'g', label = 'gpp11')
plt.legend(loc = "upper right")
plt.show()
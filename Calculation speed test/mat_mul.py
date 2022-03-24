import numpy as np
import random
import time


if __name__ == "__main__":
	c = 100
	lim = 1.0
	m = np.zeros((c, c))
	r = np.arange(0, 1, 0.01)
	for i in range(0, c):
		for j in range(0, c):
			m[i][j] = random.choice(r)
	
	print("Starting computations...")
	count = 0
	start = time.time()
	while((time.time() - start) < lim):
		np.matmul(m, m)
		count += 1
	print("Total matrix multiplications performed =", f"{count:.2E}",
		"\nCalculations per second performed =", f"{count/lim:.2E}")

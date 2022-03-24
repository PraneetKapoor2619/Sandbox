#include <iostream>
#include <random>
#include <stdint.h>
#include <ctime>

int main(int argc, char **argv)
{
	int c = 100;
	double m[c][c], result[c][c];
	
	std::random_device dev;
	std::mt19937 rng(dev());
	std::uniform_int_distribution<std::mt19937::result_type> distribution(1, 100);
	
	for (int i = 0; i < c; ++i) {
		for (int j = 0; j < c; ++j) {
			m[i][j] = distribution(rng) / 100.0;
			std::cout << m[i][j] << " ";
			result[i][j] = 0;
		}
		std::cout << std::endl;
	}
	
	//now we will perform matrix multiplication using a simple algorithm
	//c[i][j] = \summation (k = 0, lim) a[i][k] * b[k][j]
	std::cout << "Starting computations..." << std::endl;
	long double count = 0;
	time_t start = time(NULL);
	while((time(NULL) - start) < 1) {
		for (int i = 0; i < c; ++i) {
			for (int j = 0; j < c; ++j) {
				result[i][j] = 0;
				for (int k = 0; k < c; ++k) {
					result[i][j] += (m[i][k] * m[k][j]);
				}
			}
		}
		++count;
	}
	
	for (int i = 0; i < c; ++i) {
		for (int j = 0; j < c; ++j) {
			std::cout << result[i][j] << " ";
		}
		std::cout << std::endl;
	}
	std::cout.precision(2);
	std::cout << std::scientific;
	std::cout << "Total matrix multiplications performed = " << count 
		<< "\nComputations per second = " << (count / 1.0) << std::endl;
	return 0;
}
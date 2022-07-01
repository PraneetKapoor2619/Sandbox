#include <stdio.h>
#include <stdlib.h>

int main(int argc, char ** argv)
{
	int n = 2, N = 0;
	fscanf(stdin, "%d", &N);
	for (; n <= N / 2; ++ n) {
		if (N % n == 0) {
			fprintf(stdout, "N is not a prime number\n");
			exit(0);
		}
	}
	fprintf(stdout, "N is a prime number\n");
	return 0;
}

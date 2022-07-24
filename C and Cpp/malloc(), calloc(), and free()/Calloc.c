#include <stdio.h>
#include <stdlib.h>


#define ENDL printf("\n")


int main(int argc, char **argv)
{
	int N = 10;
	int *ptr = (int *) calloc(10, sizeof(int));
	printf("ptr -> %p\n", ptr);

	for (int i = 0; i < N; ++i) {
		printf("%d ", *(ptr + i));
		ptr[i] = i + 1;
	}
	ENDL;

	for (int i = 0; i < N; ++i) {
		printf("%d ", *(ptr + i));
	}
	ENDL;

	free(ptr);
	for (int i = 0; i < N; ++i) {
		printf("%d ", *(ptr + i));
	}
	ENDL;
	return 0;
}
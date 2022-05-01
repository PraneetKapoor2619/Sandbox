#include <stdio.h>

void main(void)
{
	printf("char: %d\n"
		"int: %d\n"
		"short int: %d\n"
		"unsigned char: %d\n"
		"unsigned int: %d\n"
		"unsigned short int: %d\n",
		sizeof(char), sizeof(int), sizeof(short int), sizeof(unsigned char),
		sizeof(unsigned int), sizeof(unsigned short int));
	int x = 3333234;
	int copy, q;
	copy = x;
	int flag = 0;
	char ch = '0';
	for (int i = 1e+09; i >= 1; i /= 10) {
		q = copy / i;
		copy %= i;
		if (q > 0 && flag == 0) {
			flag = 1;
		}
		if (flag == 1) {
			printf("%c", ch + q);
		}
	}
	printf("\n");
}

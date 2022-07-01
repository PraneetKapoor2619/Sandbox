#include <stdio.h>

int main(void)
{
	int c;

	c = getchar();
	while (c != EOF) {
		c = getchar();
		printf("%02x", c);
	}
	return 0;
}

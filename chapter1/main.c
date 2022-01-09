#include<stdio.h>

int main(int argc, char **argv)
{
	int c;
	c = getchar();
	while(c != EOF){		/*EOF -> Unix Ctrl + D, Windows Ctrl + Z*/
		putchar(c);
		c = getchar();
	}
	return 0;
}
#include<stdio.h>

int main(int argc, char **argv)
{
	int c;
	
	while((c = getchar()) != EOF){		/*EOF -> Unix Ctrl + D, Windows Ctrl + Z*/
		putchar(c);
	}
	return 0;
}
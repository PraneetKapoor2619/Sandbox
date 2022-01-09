#include<stdio.h>

/* print input one word per line*/
int main(int argc, char **argv)
{
	int c;
	while((c = getchar()) != EOF){
		if(((c >= 'A') && (c <= 'Z')) ||
			((c >= 'a') && (c <= 'z'))){
			putchar(c);
		}
		else{
			putchar('\n');
		}
	}
	return 0;
}
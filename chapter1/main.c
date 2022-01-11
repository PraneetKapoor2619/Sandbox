#include<stdio.h>

#define MAXLENGTH 1024		/* Maximum Length of input allowed */

int readline(char [], int);

int main(int argc, char **argv)
{
	int l, max;
	char line[MAXLENGTH];
	
	while((l = readline(line, MAXLENGTH)) > 0)
		if(l > 80)
			printf("(%d) %s", l, line);
	return 0;
}

int readline(char line[], int N)
{
	int i, c;
	
	for(i = 0; (i < N) && (c = getchar()) != EOF && (c != '\n'); ++i)
		line[i] = c;
	
	if(c == '\n'){
		line[i] = c;
		++i;
	}
	line[i] = '\0';
	return i;
}
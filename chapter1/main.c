#include<stdio.h>

#define MAXLENGTH 1024		/* Maximum Length of input allowed */

int readline(char [], int);
void reverse(char [], int);

int main(int argc, char **argv)
{
	int n;
	char line[MAXLENGTH];
	
	while((n = readline(line, MAXLENGTH)) > 0){
		printf("Old string:\n%s", line);
		reverse(line, n);
		printf("Reversed string:%s\n", line);
	}
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

void reverse(char s[], int N)
{
	int c, i;
	
	for(i = 0; i < N / 2; ++i){
		c = s[i];
		s[i] = s[N - 1 - i];
		s[N - 1 - i] = c;
	}
}
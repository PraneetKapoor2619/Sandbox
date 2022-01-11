#include<stdio.h>

#define MAXLENGTH 80		/* Maximum Length of input allowed */

int readline(char [], int);
void copy(char [], char []);

int main(int argc, char **argv)
{
	int l, max;
	char current_line[MAXLENGTH], longest_line[MAXLENGTH];
	
	for(max = 0; (l = readline(current_line, MAXLENGTH)) > 0; ){
		if(l > max){
			copy(current_line, longest_line);
			max = l;
		}
	}
	
	printf("The longest line is:\n%s\nit has %d characters.\n", longest_line, max);
	return 0;
}

int readline(char line[], int N)
{
	int i, c;
	
	for(i = 0; (c = getchar()) != EOF && (c != '\n'); ++i)
		if(i < N)
			line[i] = c;
	
	if(c == '\n' && i < N){
		line[i] = c;
		++i;
		line[i] = '\0';
	}
	else
		line[N - 1] = '\0';

	return i;
}

void copy(char from[], char to[])
{
	int i;
	
	i = 0;
	while((to[i] = from[i]) != '\0')
		++i;
}
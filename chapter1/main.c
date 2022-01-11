#include<stdio.h>

#define MAXLENGTH 1024		/* Maximum Length of input allowed */

int readline(char [], int);
void store(char [], char []);

int main(int argc, char **argv)
{
	char line[MAXLENGTH], longest[MAXLENGTH];
	int current_length, max_length;
	
	max_length = 0;
	while((current_length = readline(line, MAXLENGTH)) > 0){
		if(current_length > max_length){
			store(line, longest);
			max_length = current_length;
		}
	}
	printf("Longest line is:\n%sIt has %d characters.\n", longest, max_length);
	return 0;
}

int readline(char line[], int N)
{
	int i, c;
	
	i = 0;
	while(	(i < N) &&
			((c = getchar()) != EOF) &&
			(c != '\n')){
		line[i] = c;
		++i;
	}
	if(c == '\n'){
		line[i] = c;
		++i;
	}
	line[i] = '\0';
	return i;
}

void store(char from[], char to[])
{
	int i;
	i = 0;
	while((to[i] = from[i]) != '\0')
		++i;
}
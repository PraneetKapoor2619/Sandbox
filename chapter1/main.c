#include<stdio.h>

#define MAXLENGTH 1024		/* Maximum Length of input allowed */

int readline(char [], int);
void reverse(char []);

int main(int argc, char **argv)
{
	int n;
	char line[MAXLENGTH];
	
	while((n = readline(line, MAXLENGTH)) > 0){
		reverse(line);
		printf("\nReversed string:\n%s", line);
	}
	return 0;
}

int readline(char line[], int N)
{
	int i, c;
	
	i = 0;
	while((c = getchar()) != EOF){
		line[i] = c;
		++i;
	}
	line[i] = '\0';
	return i;
}

void reverse(char s[])
{
	int begin, end;
	int c, i, N;
	
	begin = 0;
	while(s[begin] != '\0'){
		end = begin;
		while(s[end] != '\n')
			++end;
		N = (end - 1) - begin;
		for(i = begin; i <= begin + (N / 2); ++i){
			c = s[i];
			s[i] = s[(begin + N) - (i - begin)];
			s[(begin + N) - (i - begin)] = c;
		}
		begin = end + 1;
	}
}
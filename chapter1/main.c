#include<stdio.h>

#define MAXLENGTH 1024		/* Maximum Length of input allowed */

int readline(char [], int);
int strip(char [], int);

int main(int argc, char **argv)
{
	int l1, l2;
	char line[MAXLENGTH];
	
	while((l1 = readline(line, MAXLENGTH)) > 0){
		l2 = strip(line, l1);
		printf("\nOld length: %d"
				"\nNew length: %d"
				"\nLine:\n%s", l1, l2, line);
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

int strip(char line[], int N)
{
	int i;
	if(N == 1){
		--N;
		line[N] = '\0';
	}
	else{
		for(i = N - 2; i >= 0 && (line[i] == ' ' || line[i] == '\t'); --i){
			line[i] = '\n';
			line[i + 1] = '\0';
		}
		N = i + 2;
	}

	return N;
}
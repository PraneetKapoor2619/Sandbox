#include<stdio.h>

#define MAXLENGTH 1024		/* Maximum Length of input allowed */
#define TABS 4				/* length of a single tab in spaces */

void detab(char [], int);

int main(int argc, char **argv)
{
	char line[MAXLENGTH];
	
	detab(line, MAXLENGTH);
	printf("\n%s\n", line);
	return 0;
}

void detab(char line[], int N)
{
	int c, i, s;
	
	for (i = 0; i < N && (c = getchar()) != EOF; ++i)
		if (c == '\t') {
			for (s = i; (i - s) < TABS; ++i)
				line[i] = ' ';
			--i;
		}
		else
			line[i] = c;
	line[i] = '\0';
}
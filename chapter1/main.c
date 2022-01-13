#include<stdio.h>

#define MAXLENGTH 1024		/* Maximum Length of input allowed */

int main(int argc, char **argv)
{
	int c, i, cflag;
	char line[MAXLENGTH];
	
	i = cflag = 0;
	while ((c = getchar()) != EOF) {
		if (c == '/' && cflag == 0) {
			if ((c = getchar()) == '*')
				cflag = 1;
			else {
				cflag = 0;
				line[i] = '/';
				++i;
				line[i] = c;
			}
		}
		else if (c == '*' && cflag == 1) {
			if ((c = getchar()) == '/')
				cflag = 0;
		}
		else if (cflag == 0) {
			line[i] = c;
			++i;
		}
	}
	line[i] = '\0';
	
	printf("\n%s\n", line);
	return 0;
}
#include<stdio.h>

#define MAXLENGTH 1024
int lower(char);

int main(int argc, char **argv)
{
	int i, c;
	char line[MAXLENGTH];
	
	for (i = 0; i < MAXLENGTH && (c = getchar()) != EOF; ++i)
		line[i] = lower(c);
	line[i] = '\0';
	printf("%s\n", line);
	return 0;
}

/* lower: converts c to lower case; ASCII only */
int lower(char c)
{
	if (c >= 'A' && c <= 'Z')
		return c - 'A' + 'a';
	else
		return c;
}
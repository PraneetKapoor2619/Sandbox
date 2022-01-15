#include<stdio.h>

#define MAXLENGTH 1024

int htoi(char []);

int main(int argc, char **argv)
{
	int i, c, n;
	char line[MAXLENGTH];
	
	for (i = 0; i < MAXLENGTH && (c = getchar()) != EOF; ++i)
		line[i] = c;
	line[i] = '\0';
	n = htoi(line);
	printf("\n%s = %d\n", line, n);
	return 0;
}

/* htoi: converts a hexadecimal string to its decimal equivalent number */
int htoi(char s[])
{
	int i, n, val;
	
	n = i = 0;
	if (s[i] == '0' && (s[i + 1] == 'x' || s[i + 1] == 'X'))
		i = 2;
	for (; s[i] != '\0' && ((s[i] >= '0' && s[i] <= '9') ||
							(s[i] >= 'A' && s[i] <= 'F') ||
							(s[i] >= 'a' && s[i] <= 'f'))
							; ++i) {
		if (s[i] >= '0' && s[i] <= '9')
			val = s[i] - '0';
		else if (s[i] >= 'A' && s[i] <= 'F')
			val = s[i] - 'A' + 10;
		else if (s[i] >= 'a' && s[i] <= 'f')
			val = s[i] - 'a' + 10;
		n = (n * 16) + val;
	}
	return n;
}
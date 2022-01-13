#include<stdio.h>

#define MAXLENGTH 1024		/* Maximum Length of input allowed */

int main(int argc, char **argv)
{
	int c, i;
	int flag[6];
	char line[MAXLENGTH];
	
	for (i = 0; i < 6; ++i)
		flag[i] = 0;
	
	for (i = 0; i < MAXLENGTH && (c = getchar()) != EOF; ++i) {
		line[i] = c;
		if (c == '(')
			++flag[0];
		else if (c == ')')
			--flag[0];
		if (c == '[')
			++flag[1];
		else if (c == ']')
			++flag[1];
		if (c == '{')
			++flag[2];
		else if (c == '}')
			++flag[2];
		if (c == '\'')
			++flag[3];
		if (c == '\"')
			++flag[4];
		if (c == '/')
			flag[5] = 1;
		if (c == '*' && flag[5] == 1 && line[i - 1] == '/')
			flag[5] = 2;
		if (flag[5] == 2 && c == '*')
			flag[5] = 1;
		if (flag[5] == 1 && c == '/')
			flag[5] = 0;
	}
	
	if (flag[0] != 0)
		printf("Unbalanced parenthesis!\n");
	if (flag[1] != 0)
		printf("Unbalanced brackets!\n");
	if (flag[2] != 0)
		printf("Unbalanced braces!\n");
	if (flag[3] % 2 != 0)
		printf("Unbalanced single quotes!\n");
	if (flag[4] % 2 != 0)
		printf("Unbalanced double quotes!\n");
	if (flag[5] != 0)
		printf(" Unbalanced comments!\n");
	return 0;
}
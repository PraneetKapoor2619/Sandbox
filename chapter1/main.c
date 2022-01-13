#include<stdio.h>

#define MAXLENGTH 1024		/* Maximum Length of input allowed */
#define MAXCOLUMNS 80		/* maximum number of columns */

void insertnl(char [], int, int, int);

int main(int argc, char **argv)
{
	int i, cnt, c, wlength;
	char line[MAXLENGTH];
	
	i = cnt = wlength = 0;
	while ((c = getchar()) != EOF) {
		if (c != ' ' && c != '\n')
			++wlength;
		else
			wlength = 0;
		line[i] = c; 
		++cnt; 
		++i;
		
		if (cnt == (MAXCOLUMNS + 1)) {
			insertnl(line, i - wlength, i, '\n');
			++i;
			cnt = wlength;
		}
	}
	line[i] = '\0';
	
	printf("\n");
	for (i = 0; i < MAXCOLUMNS; ++i)
		printf("-");
	printf("\n%s\n", line);
	return 0;
}

void insertnl(char line[], int si, int ei, int tmp)
{
	line[ei] = ' ';
	while (si <= ei) {
		line[si] = line[si] + tmp;
		tmp = line[si] - tmp;
		line[si] = line[si] - tmp;
		++si;
	}
}
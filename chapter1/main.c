#include<stdio.h>

#define MAXLENGTH 1024		/* Maximum Length of input allowed */
#define TABS 4				/* length of a single tab in spaces */
#define IN 1				/* inside a 'space' chain */
#define OUT 0				/* outside of a 'space' chain */

void detab(char [], int);
void entab(char [], int);
int replace(char [], int, int, char);

int main(int argc, char **argv)
{
	char line[MAXLENGTH];
	
	entab(line, MAXLENGTH);
	printf("\n%s\n", line);
	return 0;
}

void detab(char line[], int N)
{
	int c, i, s;
	
	for (i = 0; i < N && (c = getchar()) != EOF; ++i)
		if (c == '\t')
			i = replace(line, i, i + TABS, ' '); 
		else
			line[i] = c;
	line[i] = '\0';
}

void entab(char line[], int N)
{
	int c, cnt, i, ns, nt, state;
	
	state = OUT;
	for (i = 0; i < N && (c = getchar()) != EOF; ++i)
		if (c == ' ') {
			if (state == OUT) {
				state = IN;
				cnt = 0;
			}
			++cnt;
		}
		else {
			if (state == IN) {
				state = OUT;
				nt = cnt / TABS;			/* gives number of tabs */
				ns = cnt - (nt * TABS);		/* gives number of spaces */
				i = i - cnt;
				i = replace(line, i, i + nt, '\t');
				i = replace(line, i, i + ns, ' ');
				++i;
			}
			line[i] = c;
		}
	line[i] = '\0';
}

int replace(char line[], int i, int end, char c)
{
	if (i != end) {
		while (i < end) {
			line[i] = c;
			++i;
		}
		return (i - 1);
	}
	else
		return i;
}

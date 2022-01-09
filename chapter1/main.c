#include<stdio.h>

/*count blanks, tabs, newlines in input*/
int main(int argc, char **argv)
{
	int c, nb, nt, nl;
	nb = 0;
	nt = 0;
	nl = 0;
	
	while((c = getchar()) != EOF){
		if(c == ' ')
			++nb;
		if(c == '\t')
			++nt;
		if(c == '\n')
			++nl;
	}
	printf("No. of blanks = %d\n"
			"No. of tabs = %d\n"
			"No. of newlines = %d\n"
			, nb, nt, nl);
	return 0;
}
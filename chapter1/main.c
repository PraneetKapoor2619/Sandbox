#include<stdio.h>

#define IN 1	/*inside a word*/
#define OUT 0	/*inside a word*/

/*count lines, words, and characters in input*/
int main(int argc, char **argv)
{
	int c, nl, nw, nc, state;
	
	state = OUT;
	nl = nw = nc = 0;
	while((c = getchar()) != EOF){
		++nc;
		if(c == ' ' || c == '\t' || c == '\n'){
			state = OUT;
			if(c == '\n')
				++nl;
		}
		else if(state == OUT){
			state = IN;
			++nw;
		}
	}
	printf("No. of lines = %d\n"
			"No. of words = %d\n"
			"No. of characters = %d\n"
			, nl, nw, nc);
	return 0;
}
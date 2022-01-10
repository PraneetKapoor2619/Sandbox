#include<stdio.h>

#define RANGE 128		/* length of character set supported */
						/* In this case, ASCII, (128) */

/* print histogram of the frequencies of different characters in the input*/
int main(int argc, char **argv)
{
	int c;
	int freq[RANGE];
	
	for(int i = 0; i < RANGE; ++i)
		freq[i] = 0;
	
	while((c = getchar()) != EOF)
		++freq[c];
	
	/* Now print the histogram */
	for(int i = 0; i < RANGE; ++i){
		if(freq[i] > 0){
			if(i == 0)
				printf("NULL");
			else if(i == '\n')
				printf("%6s ", "\\n");
			else if(i == '\t')
				printf("%6s ", "\\t");
			else if(i == '\r')
				printf("%6s ", "\\r");
			else if(i == ' ')
				printf("%6s ", "SPACE");
			else
				printf("%6c ", i);
			for(int j = 0; j < freq[i]; ++j)
				printf("|");
			printf("%d\n", freq[i]);
		}
	}
	return 0;
}
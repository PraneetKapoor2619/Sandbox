#include<stdio.h>

#define IN 1				/* inside a word */
#define OUT 0				/* outside a word */
#define MAX_WLENGTH	16		/* maximum length of words supported */
/* print histogram of length of words in the input*/
int main(int argc, char **argv)
{
	int c, state, current_length;
	int wlength[MAX_WLENGTH];
	
	current_length = 0;
	state = OUT;
	for(int i = 0; i < MAX_WLENGTH; ++i)
		wlength[i] = 0;
	
	while((c = getchar()) != EOF){
		if(((c >= 'A') && (c <= 'Z')) ||
			((c >= 'a') && (c <= 'z'))){
			if(state == OUT)
				state = IN;
			++current_length;
		}
		else{
			if(state == IN){
				state = OUT;
				++wlength[current_length - 1];
				current_length = 0;
			}
		}
	}
	
	/* Now print the histogram */
	for(int i = 0; i < MAX_WLENGTH; ++i){
		if(wlength[i] > 0){
			printf("%4d ", i + 1);
			for(int j = 0; j < wlength[i]; ++j)
				printf("|");
			printf("%d\n", wlength[i]);
		}
	}
	return 0;
}
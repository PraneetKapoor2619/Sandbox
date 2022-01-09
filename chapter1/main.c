#include<stdio.h>

#define LOWER 0 /*lower limit of table*/
#define UPPER 300 /*upper limit of table*/
#define STEP 20 /*step size*/

/*
fahrenheit to celsius converter
*/
int main(int argc, char **argv)
{
	int fahr;
	
	for(fahr = LOWER; fahr <= UPPER; fahr += STEP)
		printf("%3d\t%6.1f\n",
				fahr, (5.0 / 9.0) * (fahr - 32));
	return 0;
}
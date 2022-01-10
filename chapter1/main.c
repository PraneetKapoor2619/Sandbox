#include<stdio.h>

#define LOWER 0		/*lower limit of temp*/
#define UPPER 300	/*upper limit of temp*/
#define STEP 20		/*step size*/

float F_to_C(int);

/* given temperature in fahrenheit, calculate temperature in celsius */
int main(int argc, char **argv)
{
	int fahr;
	
	for(fahr = LOWER; fahr <= UPPER; fahr = fahr + STEP)
		printf("%3d\t%6.1f\n", fahr, F_to_C(fahr));
	return 0;
}

/* 
Name:	float F_to_C(int)
Input:	temp in fahrenheit (integer)
Output:	temp in celsius (float)
*/
float F_to_C(int fahr)
{
	return (5.0 / 9.0) * (fahr - 32);
}
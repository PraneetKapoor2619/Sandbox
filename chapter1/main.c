#include<stdio.h>

/*
fahrenheit to celsius converter
*/
int main(int argc, char **argv)
{
	int fahr, celsius;
	int lower, upper, step;
	lower = 0;
	upper = 300;
	step = 20;
	fahr = lower;
	while(fahr <= upper){
		celsius = (5 / 9)* (fahr - 32);
		printf("%d\t%d\n", fahr, celsius);
		fahr += step;
	}
	return 0;
}
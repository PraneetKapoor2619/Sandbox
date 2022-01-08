#include<stdio.h>

/*
celsius to fahrenheit converter
*/
int main(int argc, char **argv)
{
	float fahr, celsius;
	int lower, upper, step;
	lower = -100;
	upper = 100;
	step = 20;
	celsius = lower;
	printf("%3c\t%6c\n", 'C', 'F');
	while(celsius <= upper){
		fahr = (9.0 / 5.0) * celsius;
		fahr += 32;
		printf("%3.0f\t%6.1f\n", celsius, fahr);
		celsius += step;
	}
	return 0;
}
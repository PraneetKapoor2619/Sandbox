#include<stdio.h>
#include<limits.h>
#include<float.h>

int main(int argc, char **argv)
{
	printf("\nRange of char"
			"\nSigned char: %d to %d"
			"\nUnsigned char: %d to %d\n",
			SCHAR_MIN, SCHAR_MAX, 0, UCHAR_MAX);
			
	printf("\nRange of int"
			"\nSigned int: %d to %d"
			"\nUnsigned int: %d to %ld\n",
			INT_MIN, INT_MAX, 0, UINT_MAX);
			
	printf("\nRange of short"
			"\nSigned short: %d to %d"
			"\nUnsigned short: %d to %d\n",
			SHRT_MIN, SHRT_MAX, 0, USHRT_MAX);
	
	printf("\nRange of long"
			"\nSigned long: %ld to %ld"
			"\nUnsigned long: %ld to %lu\n",
			LONG_MIN, LONG_MAX, 0, ULONG_MAX);
	
	printf("\nRange of float"
			"\nFloat: %f to %f\n",
			FLT_MIN, FLT_MAX);
	
	return 0;
}
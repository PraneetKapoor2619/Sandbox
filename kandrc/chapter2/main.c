#include<stdio.h>

int main(int argc, char **argv)
{
	char c;
	int i;
	short int si;
	long int li;
	float f;
	
	int nc, ni, nsi, nli, nf;
	
	c = i = si = li = f = 2;
	nc = ni = nsi = nli = nf = 1;
	
	while (c != 0 || i != 0 || si != 0 || li != 0 || f != 0) {
		if (c != 0) {
			c = c * 2;
			++nc;
		}
		if (i != 0) {
			i = i * 2;
			++ni;
		}
		if (si != 0) {
			si = si * 2;
			++nsi;
		}
		if (li != 0) {
			li = li * 2;
			++nli;
		}/*
		if (f != 0) {
			f = f * 2.0;
			++nf;
		}*/
		
	}
	
	printf("\nSize of char: %d", nc / 8);
	printf("\nSize of int: %d", ni / 8);
	printf("\nSize of short int: %d", nsi / 8);
	printf("\nSize of longt int: %d", nli / 8);
	//printf("\nSize of float: %d", nf / 8);
	
	return 0;
}
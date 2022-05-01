#include <stdio.h>


typedef char * a_list;
#define a_start(ap,x) ((void)(ap = (a_list)&x + sizeof(x)))
#define a_arg(ap,type) (*((type *)ap++))
#define a_end(ap) ((void)(ap = 0))



void __cdecl clerk (char *, int,...);

void main(void)
{
	printf("char: %d\n"
		"int: %d\n"
		"short int: %d\n"
		"unsigned char: %d\n"
		"unsigned int: %d\n"
		"unsigned short int: %d\n",
		sizeof(char), sizeof(int), sizeof(short int), sizeof(unsigned char),
		sizeof(unsigned int), sizeof(unsigned short int));
	clerk("Hello jicky", 2, 5, 'P');
}

void clerk(char *buf, int count,...)
{
	a_list ptr;
	a_start(ptr, count);		/* last parameter to be passed to va_start */
	printf("%s", buf);
	for (int i = 1; i <= count; ++i) {
		printf("%d ", a_arg(ptr, int));
	}
	a_end(ptr);
}

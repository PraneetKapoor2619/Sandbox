#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char **argv)
{
	FILE *fp, *tmp;
	fp = fopen("junk.bin", "rb");
	
	uint8_t byte = 0; 
	fprintf(stdout, "%d -> %c\n", ftell(fp), byte);
	while (fread(&byte, 1, 1, fp) == 1) {
		fprintf(stdout, "%d -> %c\n", ftell(fp), byte);
	}
	fseek(fp, 2, SEEK_SET);
	fread(&byte, 1, 1, fp);
	fprintf(stdout, "%d : %d -> %c", SEEK_SET, ftell(fp), byte);
	fseek(fp, -4, SEEK_END);
	fread(&byte, 1, 1, fp);
	fprintf(stdout, "%d : %d -> %c", SEEK_END, ftell(fp), byte);
	return 0;
}

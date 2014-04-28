#include "stdio.h"
#include "stdint.h"
#include "hamrtty.h"

int main(int argc, char *argv[])
{
	unsigned char lastchar, outchar[4], c[4];
	unsigned char unhamming_lut[0x80];
        FILE *fin = stdin;
        FILE *fout = stdout;

	int i, j;
	for (i=0; i<0x10; i++)
		for (j=0; j<8; j++)
			unhamming_lut[0x7f & (hamrtty_lut[i] ^(1<<j))] = i;

	lastchar = 0xff;
	while ( fread(c, 1, 1, fin) > 0 ) {
		c[1] = unhamming_lut[c[0] & 0x7f]; 
		if ( c[1]>=8 ){
			// 8 low digits are sent as nibbles, with high bit set
			outchar[0] = 48 + c[1] - 8;
			fwrite(outchar, 1, 1, fout);
			lastchar = 0xff;
		} else {
			if (lastchar == 0xff) {
				lastchar = c[1] & 0x7;
				continue;
			}
			// 8 x 8 other chars are sent as two nibbles
			c[2] = lastchar + 8 * (0x7 & c[1]);
			lastchar = 0xff;
			c[2] += 32;
			if (c[2]==48) c[2] = 10;
			if (c[2]==48+3) c[2] = 13;
			outchar[0] = c[2];
			fwrite(outchar, 1, 1, fout);
		}
	}

	return 0;
}

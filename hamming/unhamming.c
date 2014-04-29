/*
Public domain reference (c) 2014 John Greb
*/

#include "stdio.h"
#include "stdint.h"
#include "hamrtty.h"

int main(int argc, char *argv[])
{
	unsigned char lastchar, temp, c[4];
	unsigned char unhamming_lut[0x80];
        FILE *fin = stdin;
        FILE *fout = stdout;

	int i, j;
	for (i=0; i<0x10; i++)
		for (j=0; j<8; j++)
			unhamming_lut[0x7f & (hamrtty_lut[i] ^(1<<j))] = i;

	lastchar = 0xff;
	while ( fread(c, 1, 1, fin) > 0 ) {
		temp = unhamming_lut[c[0] & 0x7f];
		if ( temp >= 4 && lastchar == 0xff ){
			// ".,01234567890" are sent as nibbles
			if (temp == 5) // ASCII 47 swapped with ASCII 44
				temp = 2;
			c[0] = 46 + temp - 4;
			fwrite(c, 1, 1, fout);
		} else if (lastchar == 0xff) {
			lastchar = temp;
		} else {
			// 4 x 16 other chars are sent as two nibbles
			temp = lastchar + 4 * temp;
			lastchar = 0xff;
			temp += 32;
			if (temp == 44) temp = 10;
			if (temp == 46) temp = 13;
			c[0] = temp;
			fwrite(c, 1, 1, fout);
		}
	}

	return 0;
}

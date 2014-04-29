/*
Public domain reference (c) 2014 John Greb
*/

#include "stdio.h"
#include "stdint.h"
#include "hamrtty.h"

int main(int argc, char *argv[])
{
	unsigned char temp, c[4];
        FILE *fin = stdin;
        FILE *fout = stdout;

	while ( fread(c, 1, 1, fin) > 0 ) {
		temp = c[0];
		if (temp == 44 || temp == 47 )
			 temp = 47 + 44 - temp;
		if ( temp>=46 && temp<=(48 + 9) ){
			// ",.01234567890" are single nibbles
			c[0] = hamrtty_lut[4 + temp - 46];
			fwrite(c, 1, 1, fout);
		} else {
			// 4 x 16 other chars are sent as two nibbles
			if (temp==44) temp = 47;
			if (temp==10) temp = 44;
			if (temp==13) temp = 46;
			temp -= 32;
			if (temp>=64) temp -= 32;
			c[0] = hamrtty_lut[0x3 & temp];
			temp >>= 2;
			c[1] = hamrtty_lut[0xf & temp];
			fwrite(c, 1, 2, fout);
		}
	}

	return 0;
}

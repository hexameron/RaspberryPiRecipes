#include "stdio.h"
#include "stdint.h"
#include "hamrtty.h"

int main(int argc, char *argv[])
{
	unsigned char outchar[4], c[4];
        FILE *fin = stdin;
        FILE *fout = stdout;

	while ( fread(c, 1, 1, fin) > 0 ) {
		if ( c[0]>=48 && c[0]<=(48+7) ){
			// 8 low digits are sent as nibbles, with high bit set
			outchar[0] = hamrtty_lut[8 + c[0] - 48];
			fwrite(outchar, 1, 1, fout);
		} else {
			// 8 x 8 other chars are sent as two nibbles
			if (c[0]==10) c[0] = 48;
			if (c[0]==13) c[0] = 48+3;
			c[0] -= 32;
			if (c[0]>=64) c[0] -= 32;
			outchar[0] = hamrtty_lut[0x7 & c[0]];
			c[0] >>= 3;
			outchar[1] = hamrtty_lut[0x7 & c[0]];
			fwrite(outchar, 1, 2, fout);
		}
	}

	return 0;
}

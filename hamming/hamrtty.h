/*

hamrtty.h Public Domain header (c) John Greb 2014

Hamming enhanced rtty: Single Error Correction
- corrects single errors in each 7 bit char, but not early/late start bits


1) Use standard 7 bit rtty for broadcast, 4 bits of data and three parity bits.
2) Start bits can be inferred by timing if parity is good: needs improved decoder.
3) 4 bit data allows DominoEx-like charset, maintaining datarate.

12 primary characters: "0123456789,."; (for text use DominoEx mapping)

4x16 secondary chars, ASCII 32-95
 .. lowercase mapped onto uppercase, for ASCII 96 to 127 subtract 32

Upto 12 extended chars, mapped onto ASCII "0123456789,.", but only CR and LF are used
 .. for ASCII 10 & 13 add (48 - 10), discard all other chars below " "( ASCII 32).


Nibble to Hamming map:
ODD Parity, big endian
  ODD Parity   |  Bit - swapped
X xxx.pxpp  OUT xxx.xppp OUT
0 000.0001   01 000.0001  01
1 000.1110   0e 000.1110  0e
2 001.1000   18 001.0100  14  
3 001.0111   17 001.1011  1b
4 010.1011   2b 010.0111  27
5 010.0100   24 010.1000  28
6 011.0010   32 011.0010  32
7 011.1101   3d 011.1101  3d
8 100.0010   42 100.0010  42
9 100.1101   4d 100.1101  4d
a 101.1011   5b 101.0111  57
b 101.0100   54 101.1000  58
c 110.1000   68 110.0100  64
d 110.0111   67 110.1011  6b
e 111.0001   71 111.0001  71
f 111.1110   7e 111.1110  7e

Even parity is too symetric, odd parity flips the lsb
Best not send "$" (ascii 0x24), so swap (bit 2) with (bit 3)
*/

// Odd Parity, with swapped bits:
const unsigned char hamrtty_lut[] = {0x01,0x0e,0x14,0x1b,0x27,0x28,0x32,0x3d,0x42,0x4d,0x57,0x58,0x64,0x6b,0x71,0x7e};

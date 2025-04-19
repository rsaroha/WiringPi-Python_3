import wiringpi
import sys

def printf(format, *args):
   sys.stdout.write(format % args)


printf("\nI2CDetect Python implementation using WiringPi-Python\n\n")

printf("     0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F\n")

for i in range(0, 128, 16):
    printf("%02x: ", i)
    for j in range(0,16,1):
        if(wiringpi.wiringPiI2CSetup(i+j) != -1):
            printf("%2x ", i + j)
        else:
            printf("-- ")

    printf("\n")

printf("\n")
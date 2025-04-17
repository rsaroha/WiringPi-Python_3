"""

Demo implementation of gpio in python. This file is equivalent to calling
gpio allreadall

"""
import wiringpi
import sys

def printf(format, *args):
   sys.stdout.write(format % args)

physToWpi = [   -1, 
                -1, -1,   # 1, 2
                 8, -1,   # 3, 4
                 9, -1,
                 7, 15,
                -1, 16,
                 0,  1,
                 2, -1,
                 3,  4,
                -1,  5,
                12, -1,
                13,  6,
                14, 10,
                -1, 11,   # 25, 26
                30, 31,	# Actually also I2C, but not used
                21, -1,
                22, 26,
                23, -1,
                24, 27,
                25, 28,
                -1, 29,
                -1, -1,
                -1, -1,
                -1, -1,
                -1, -1,
                -1, -1,
                17, 18,
                19, 20,
                -1, -1, -1, -1, -1, -1, -1, -1, -1
            ]

physNames = [    "",
                "   3.3v", "5v     ",
                "  SDA.1", "5v     ",
                "  SCL.1", "0v     ",
                "GPIO. 7", "TxD    ",
                "     0v", "RxD    ",
                "GPIO. 0", "GPIO. 1",
                "GPIO. 2", "0v     ",
                "GPIO. 3", "GPIO. 4",
                "   3.3v", "GPIO. 5",
                "   MOSI", "0v     ",
                "   MISO", "GPIO. 6",
                "   SCLK", "CE0    ",
                "     0v", "CE1    ",
                "  SDA.0", "SCL.0  ",
                "GPIO.21", "0v     ",
                "GPIO.22", "GPIO.26",
                "GPIO.23", "0v     ",
                "GPIO.24", "GPIO.27",
                "GPIO.25", "GPIO.28",
                "     0v", "GPIO.29",
                    "", "",
                    "", "",
                    "", "",
                    "", "",
                    "", "",
                "GPIO.17", "GPIO.18",
                "GPIO.19", "GPIO.20",
                "","","","","","","","",""
            ]



altNames = ["IN", "OUT", "ALT5", "ALT4", "ALT0", "ALT1", "ALT2", "ALT3", "ALT6", "ALT7", "ALT8", "ALT9"]

piModelNames = [  
                        "---Pi A---",	
                        "---Pi B---",	
                        "---Pi A+--",	
                        "---Pi B+--",	
                        "---Pi 2---",	
                        "---Alpha--",	
                        "----CM----",	
                        "",
                        "---Pi 3B--",	
                        "-Pi Zero--",	
                        "---CM3----",	
                        "",	
                        "-Pi ZeroW-",	
                        "---Pi 3B+-",	
                        "---Pi 3A+-",	
                        "",	
                        "---CM3+---",	
                        "---Pi 4B--",	
                        "Pi Zero 2W",	
                        "--Pi 400--",	
                        "---CM4----",	
                        "---CM4S---",	
                        "",	
                        "---Pi 5---",	
                        "---CM5----",	
                        "--Pi 500--",	
                        "---CM5L---"
                    ]

piVersionsNames = [ "PI_VERSION_1", "PI_VERSION_1_1", "PI_VERSION_1_2", "PI_VERSION_2"]

piMemNames = ["256 Mb", "512 Mb", "1024 Mb", "2048 Mb", "4096 Mb", "8192 Mb", "16384 Mb","0 Mb"]
piMakerNames = ["PI_MAKER_SONY", "PI_MAKER_EGOMAN", "PI_MAKER_EMBEST", "PI_MAKER_UNKNOWN"]

MAX_ALTS = 11


def GetAltString(alt):
    if ( alt>=0 and alt<=MAX_ALTS):
        return altNames[alt]
    else:
        return " - "
    
def readallPhys(physPin):
    if (wiringpi.physPinToGpio (physPin) == -1):
        printf (" |     |    ") 
    else:
        printf (" | %3d | %3d", wiringpi.physPinToGpio (physPin), physToWpi [physPin])

    printf (" | %s", (physNames [physPin]))

    if (physToWpi [physPin] == -1):
        printf (" |      |  ") 
    else:
        printf (" | %4s", GetAltString( wiringpi.getAlt(physPin)))
        printf (" | %d", wiringpi.digitalRead (physPin))
        

    #  Pin numbers:

    printf (" | %2d", physPin)
    physPin = physPin+1
    printf (" || %-2d", physPin)

    # Same, reversed

    if (physToWpi [physPin] == -1):
        printf (" |   |     ")
    else:
        printf (" | %d", wiringpi.digitalRead (physPin))
        printf (" | %-4s", GetAltString(wiringpi.getAlt (physPin)))


    printf (" | %-5s", physNames [physPin])

    if (physToWpi[physPin] == -1):
        printf (" |     |    ")
    else:
        printf (" | %-3d | %-3d", physToWpi [physPin], wiringpi.physPinToGpio (physPin))
    printf (" |\n")



def allReadall():
    wiringpi.wiringPiSetupGpio()

    printf ("+-----+------+-------+      +-----+------+-------+\n")
    printf ("| Pin | Mode | Value |      | Pin | Mode | Value |\n")
    printf ("+-----+------+-------+      +-----+------+-------+\n")

    for pin in range (1, 27, 1):
        printf ("| %3d ", pin)
        printf ("| %-4s ", GetAltString(wiringpi.getAlt (pin)))
        if wiringpi.digitalRead (pin) == 1 :
            printf("| HIGH  ")
        else:
            printf("| LOW   ")
                    
        printf ("|      ")
        printf ("| %3d ", pin + 27)
        printf ("| %-4s ", GetAltString(wiringpi.getAlt (pin + 27)))
        if wiringpi.digitalRead (pin+27) == 1 :
            printf("| HIGH  ")
        else:
            printf("| LOW   ")
        printf ("|\n")
    printf ("+-----+------+-------+      +-----+------+-------+\n") 


def plus2header(model):
    if(model < wiringpi.PI_MODELS_MAX and piModelNames[model]!= ""):
        printf(" +-----+-----+---------+------+---+%s+---+------+---------+-----+-----+\n", piModelNames[model])
    else:
        printf (" +-----+-----+---------+------+---+---- ? ---+---+------+---------+-----+-----+\n")    

def piPlusReadall():
    wiringpi.wiringPiSetupPhys()

    printf (" +-----+-----+---------+------+---+----------+---+------+---------+-----+-----+\n")
    plus2header(wiringpi.intp_value(model))
    printf (" |     |     |         |      |   |          |   |      |         |     |     |\n")
    printf (" | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |\n")
    printf (" |     |     |         |      |   |          |   |      |         |     |     |\n") 
    printf (" +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+\n")

    for pin in range(1, 40, 2) :
        readallPhys(pin)

    printf (" +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+\n")
    printf (" |     |     |         |      |   |          |   |      |         |     |     |\n")
    printf (" | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |\n")
    printf (" |     |     |         |      |   |          |   |      |         |     |     |\n")
    plus2header(wiringpi.intp_value(model))
    printf (" +-----+-----+---------+------+---+----------+---+------+---------+-----+-----+\n")

def abReadall(model, rev):
    if(model == wiringpi.PI_MODEL_A):
        type = " A"
    else:
        if(rev == wiringpi.PI_VERSION_2):
            type = "B2"
        else:
            type = "B1"

    printf (" +-----+-----+---------+------+---+-Model %s-+---+------+---------+-----+-----+\n", type)
    printf (" | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |\n")
    printf (" +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+\n")
    for pin in range(1, 27, 2):
        readallPhys (pin)

    # B version 2
    if (rev == wiringpi.PI_VERSION_2) :
        printf (" +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+\n")
        for pin in range( 51, 55, 2):
            readallPhys (pin) 
    

    printf (" +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+\n")
    printf (" | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |\n")
    printf (" +-----+-----+---------+------+---+-Model %s-+---+------+---------+-----+-----+\n", type)




model = wiringpi.new_intp()
rev = wiringpi.new_intp()
mem = wiringpi.new_intp()
maker = wiringpi.new_intp()
overVolted = wiringpi.new_intp()

wiringpi.piBoardId ( model, rev, mem, maker, overVolted) ;

print("")
print("model = ", piModelNames[wiringpi.intp_value(model)])
print("rev   = ", piVersionsNames[wiringpi.intp_value(rev)])
print("mem   = ", piMemNames[wiringpi.intp_value(mem)])
print("maker = ", piMakerNames[wiringpi.intp_value(maker)])
print("")


piPlusReadall();

allReadall()


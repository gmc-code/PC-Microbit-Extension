# buzzer tests for BitBotXL module

from microbit import *
import neopixel
import BitBotXL


__I2CADDR1 = 0x1c  # address of PCA9557
I2CADDR = 0x1c # address of PCA9557

fireleds = neopixel.NeoPixel(pin13, 12)

'''
28 0x1c
r	114	01110010
s	115	01110011

x << y
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros).
This is the same as multiplying x by 2**y.

x & y
Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.

    value_left = i2c.read(__I2CADDR1, 1)[0]
    value_right = i2c.read(__I2CADDR2, 1)[1]
    print(value1, value2)  # , (value0 & 2), (value0 & 1))
    # print(1 << 1, 1 << 0)  #, 2, 1
    sleep(1000

'''



def getLine(bitval):
    mask = 1 << bitval
    value = 0
    try:
        if bitval == 0:
            value = i2c.read(I2CADDR, 1)[0]
        elif bitval == 1:
            value = i2c.read(I2CADDR, 2)[1]
    except OSError:
        pass
    if (value & mask) > 0:
        return 1
    else:
        return 0


while True:
    if getLine(0) == 0:
        fireleds[5] = (0, 0, 20)
    else:
        fireleds[5] = (0, 20, 0)
    if getLine(1) == 0:
        fireleds[11] = (, 0, 20)
    else:
        fireleds[11] = (0, 20, 0)
    fireleds.show()
    sleep(200)

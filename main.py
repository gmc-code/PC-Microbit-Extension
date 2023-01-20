# buzzer tests for BitBotXL module

from microbit import *
import neopixel
import BitBotXL


fireleds = neopixel.NeoPixel(pin13, 12)


while True:
    rightVal = pin1.read_analog()
    leftVal = pin2.read_analog()
    print(rightVal, leftVal)  
    if leftVal < 200:
        fireleds[5] = (20, 0, 0)
    else:
        fireleds[5] = (0, 20, 0)
    if rightVal < 200:
        fireleds[11] = (20, 0, 0)
    else:
        fireleds[11] = (0, 20, 0)
    fireleds.show()
    sleep(200)
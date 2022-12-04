# maqueen lights
from microbit import *
import music
import maqueen


leds = maqueen.MaqueenNeoPixels()
# front=(20, 20, 20), indicator=(35, 25, 0), rear=(20, 0, 0)
def testmain():
    leds.front_lights()
    sleep(500)
    leds.left_indicator()
    sleep(500)
    leds.right_indicator()
    sleep(500)
    leds.both_indicators()
    sleep(500)

while True:
#     leds.set_front((0, 0, 255))
#     leds.set_indicator((255, 255, 0))
#     leds.set_rear((255, 0, 0))
#     testmain()
#     leds.set_front()
#     leds.set_indicator()
#     leds.set_rear()
#     testmain()

    leds.set_leds((0, 15, 15))
    sleep(500)
    for i in range(4):
        leds.set_led(i)
        sleep(900)
    leds.set_leds((15, 0, 15))
    sleep(500)
    leds.set_leds()
    sleep(900)

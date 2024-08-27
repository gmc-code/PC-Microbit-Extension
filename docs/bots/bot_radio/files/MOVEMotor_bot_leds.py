# MOVEMotor bot code, change radio group to match bot number
# MOVEMotor_v31 200 + bot number
# MOVEMotor v2 150 + bot number

from microbit import *
import radio
import MOVEMotor
import neopixel

# set speeds
fast, medium, slow = 10, 3, 1

radio.config(group=151)  # 0-255
radio.on()


np = neopixel.NeoPixel(pin8, 4)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
orange = (255, 94, 5)
green = (0, 128, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
magenta = (255, 0, 255)
# led position numbers
lf, lb, rf, rb = 0, 3, 1, 2



# Function to adjust brightness
def adjust_brightness(color, brightness):
    return tuple(int(brightness * x) for x in color)

def np_stopped(lvl=1.0):
    for led_num in range(4):
        np[led_num] = adjust_brightness(red, lvl)
    np.show()

def np_forwards(lvl=1.0):
    for led_num in range(4):
        np[led_num] = adjust_brightness(green, lvl)
    np.show()

def np_backwards(lvl=1.0):
    for led_num in range(4):
        np[led_num] = adjust_brightness(magenta, lvl)
    np.show()
    
def np_right(lvl=1.0):
    for led_num in [rf, rb]:
        np[led_num] = adjust_brightness(yellow, lvl)
    np.show()

def np_spinright(lvl=1.0):
    for led_num in [rf, rb]:
        np[led_num] = adjust_brightness(orange, lvl)
    np.show()
    
def np_left(lvl=1.0):
    for led_num in [lf, lb]:
        np[led_num] = adjust_brightness(cyan, lvl)
    np.show()

def np_spinleft(lvl=1.0):
    for led_num in [lf, lb]:
        np[led_num] = adjust_brightness(blue, lvl)
    np.show()
    
def leds0ff():
    np.clear()


buggy = MOVEMotor.MOVEMotorMotors()
dec_left = 0
dec_right = 0
biaslist =['decleft', 'resetbias', 'decright']


while True:
    sleep(50)
    msg = radio.receive()
    if msg is not None:
        if msg in biaslist:
            display.show(biaslist.index(msg))
        else:
            display.show(msg)
            
        if msg == "decleft":
            dec_left +=20
        elif msg == "decright":
            dec_right +=20
        elif msg == "resetbias":
            dec_left = 0
            dec_right = 0        
        elif msg == "B":
            buggy.backwards(speed=slow, decrease_left=dec_left, decrease_right=dec_right)
            np_backwards(0.2)
        elif msg == "C":
            buggy.backwards(speed=medium, decrease_left=dec_left, decrease_right=dec_right)
            np_backwards(0.5)
        elif msg == "D":
            buggy.backwards(speed=fast, decrease_left=dec_left, decrease_right=dec_right)
            np_backwards()
        elif msg == "F":
            buggy.forwards(speed=slow, decrease_left=dec_left, decrease_right=dec_right)
            np_forwards(0.2)
        elif msg == "G":
            buggy.forwards(speed=medium, decrease_left=dec_left, decrease_right=dec_right)
            np_forwards(0.5)
        elif msg == "H":
            buggy.forwards(speed=fast, decrease_left=dec_left, decrease_right=dec_right)
            np_forwards()
        elif msg == "X":
            buggy.stop()
            np_stopped(0.1)
        elif msg == "L":
            buggy.left(speed=slow, radius=5)
            np_left()
        elif msg == "M":
            buggy.left(speed=medium, radius=20)
            np_left(0.5)
        elif msg == "N":
            buggy.left(speed=fast, radius=100)
            np_left(0.2)
        elif msg == "R":
            buggy.right(speed=slow, radius=5)
            np_right()
        elif msg == "S":
            buggy.right(speed=medium, radius=20)
            np_right(0.5)
        elif msg == "T":
            buggy.right(speed=fast, radius=100)
            np_right(0.2)
        elif msg == "sL":
            buggy.spin_left(speed=slow)
            np_spinleft()
        elif msg == "sR":
            buggy.spin_right(speed=slow)
            np_spinright()
            

# line follow with lights and buzzer
from microbit import *
import music
from neopixel import NeoPixel as leds
import docs.bots.MoveMotor.files.MOVEMotor_v31 as MOVEMotor_v31


buggy = MOVEMotor_v31.MOVEMotorMotors()
buggy.stop()
line_sensor = MOVEMotor_v31.MOVEMotorLineSensors()
line_sensor.line_sensor_calibrate()
left_sensor_start = line_sensor.line_sensor_read('left')
right_sensor_start = line_sensor.line_sensor_read('right')
distance_sensor = MOVEMotor_v31.MOVEMotorDistanceSensors()

thin_line_follow_flag = True
CHANGETHRESHOLD = 40
MAXSPEED = 1
MINTURN = -1
MAXTURN = 1
MOTORTIME = 20
SPINTIME = 800
# Setup the Neopixels on pin8 with a length of 4 pixels
LED_PIN = pin8
NUM_PIXELS = 4
lights = leds(LED_PIN, NUM_PIXELS)
DULL_WHITE = (20, 20, 20)
DULL_YELLOW = (35, 25, 0)
DULL_RED = (20, 0, 0)

def rear_lights():
    lights[2] = DULL_RED
    lights[3] = DULL_RED

def front_lights(left, right):
    lights[0] = left
    lights[1] = right
    rear_lights()
    lights.show()

def head_lights():
    front_lights(DULL_WHITE, DULL_WHITE)

def left_indicator():
    front_lights(DULL_YELLOW, DULL_WHITE)

def right_indicator():
    front_lights(DULL_WHITE, DULL_YELLOW)

def both_indicators():
    front_lights(DULL_YELLOW, DULL_YELLOW)

def police_siren():
    for i in range(3):
        for freq in range(1500, 1760, 16):
            music.pitch(freq, 30, wait=False)
            sleep(20)
        for freq in range(1760, 1500, -16):
            music.pitch(freq, 30, wait=False)
            sleep(20)

def follow_thin_line(drive_time=20):
    left_sensor = line_sensor.line_sensor_read('left')
    right_sensor = line_sensor.line_sensor_read('right')
    black_left = left_sensor + CHANGETHRESHOLD < left_sensor_start
    black_right = right_sensor + CHANGETHRESHOLD < right_sensor_start
    if not(black_left) and not(black_right):
        display.show(Image.ARROW_N)
        head_lights()
        buggy.left_motor(MAXSPEED)
        buggy.right_motor(MAXSPEED)
    elif black_left and not(black_right):
        display.show(Image.ARROW_W)
        left_indicator()
        buggy.left_motor(MINTURN)
        buggy.right_motor(MAXTURN)
    elif black_right and not(black_left):
        display.show(Image.ARROW_E)
        right_indicator()
        buggy.left_motor(MAXTURN)
        buggy.right_motor(MINTURN)
    else:
        display.show(' ')
        both_indicators()
        buggy.left_motor(MAXTURN)
        buggy.right_motor(-MAXTURN)
    sleep(drive_time)

def follow_thick_line(drive_time=20):
    left_sensor = line_sensor.line_sensor_read('left')
    right_sensor = line_sensor.line_sensor_read('right')
    black_left = left_sensor + CHANGETHRESHOLD < left_sensor_start
    black_right = right_sensor + CHANGETHRESHOLD < right_sensor_start
    if not(black_left) and not(black_right):
        display.show(' ')
        both_indicators()
        buggy.left_motor(-MAXTURN)
        buggy.right_motor(-MAXTURN)
    elif black_left and not(black_right):
        display.show(Image.ARROW_W)
        left_indicator()
        buggy.left_motor(MINTURN)
        buggy.right_motor(MAXTURN)
    elif black_right and not(black_left):
        display.show(Image.ARROW_E)
        right_indicator()
        buggy.left_motor(MAXTURN)
        buggy.right_motor(MINTURN)
    else:
        display.show(Image.ARROW_N)
        head_lights()
        buggy.left_motor(MAXSPEED)
        buggy.right_motor(MAXSPEED)
    sleep(drive_time)

def spin_from_obstacle(spin_time=800):
    display.show(' ')
    both_indicators()
    buggy.left_motor(MAXTURN)
    buggy.right_motor(-MAXTURN)
    sleep(spin_time)

def start_buggy():
    left_sensor = line_sensor.line_sensor_read('left')
    right_sensor = line_sensor.line_sensor_read('right')
    display.scroll('L' + str(left_sensor), delay=60)
    display.scroll('R' + str(right_sensor), delay=60)
    head_lights()
    police_siren()
    both_indicators()

start_buggy()
while True:
    if button_a.is_pressed() and not button_b.is_pressed():
        display.scroll('A', delay=100)
        thin_line_follow_flag = True
    elif button_b.is_pressed() and not button_a.is_pressed():
        display.scroll('B', delay=100)
        thin_line_follow_flag = False
    if thin_line_follow_flag:
        follow_thin_line(MOTORTIME)
    else:
        follow_thick_line(MOTORTIME)
    # check for obstacle and spin and go back
    if distance_sensor.distance() < 10:
        spin_from_obstacle(SPINTIME)
    buggy.stop()
    sleep(10)

# line follow with lights and buzzer
from microbit import *
import music
from neopixel import NeoPixel as leds
import MOVEMotor

# setup buggy
buggy = MOVEMotor.MOVEMotorMotors()

# setup distance_sensor
distance_sensor = MOVEMotor.MOVEMotorDistanceSensors()


MAXTURN = 1
SPINTIME = 800


def police_siren():
    for i in range(3):
        for freq in range(1500, 1760, 16):
            music.pitch(freq, 30, wait=False)
            sleep(20)
        for freq in range(1760, 1500, -16):
            music.pitch(freq, 30, wait=False)
            sleep(20)


while True:
    buggy.forwards()
    if distance_sensor.distance() < 50:
        buggy.spin(speed=1, direction='left', duration=1000)
        police_siren()
    sleep(200)

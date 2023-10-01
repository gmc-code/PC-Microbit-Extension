# thin_line_follow_with_distance
from microbit import *
import docs.bots.MoveMotor.files.MOVEMotor_v31 as MOVEMotor_v31


buggy = MOVEMotor_v31.MOVEMotorMotors()
buggy.stop()
line_sensor = MOVEMotor_v31.MOVEMotorLineSensors()
line_sensor.line_sensor_calibrate()
left_sensor_start = line_sensor.line_sensor_read('left')
right_sensor_start = line_sensor.line_sensor_read('right')
distance_sensor = MOVEMotor_v31.MOVEMotorDistanceSensors()

CHANGETHRESHOLD = 40
MAXSPEED = 1
MINTURN = -1
MAXTURN = 1
MOTORTIME = 20
SPINTIME = 800

def follow_thin_line(drive_time=20):
    left_sensor = line_sensor.line_sensor_read('left')
    right_sensor = line_sensor.line_sensor_read('right')
    black_left = left_sensor + CHANGETHRESHOLD < left_sensor_start
    black_right = right_sensor + CHANGETHRESHOLD < right_sensor_start
    if not(black_left) and not(black_right):
        buggy.left_motor(MAXSPEED)
        buggy.right_motor(MAXSPEED)
    elif black_left and not(black_right):
        buggy.left_motor(MINTURN)
        buggy.right_motor(MAXTURN)
    elif black_right and not(black_left):
        buggy.left_motor(MAXTURN)
        buggy.right_motor(MINTURN)
    else:
        buggy.left_motor(MAXTURN)
        buggy.right_motor(-MAXTURN)
    sleep(drive_time)

def spin_from_obstacle(spin_time=800):
    buggy.left_motor(MAXTURN)
    buggy.right_motor(-MAXTURN)
    sleep(spin_time)

while True:
    follow_thin_line(MOTORTIME)
    # check for obstacle and spin and go back
    if distance_sensor.distance() < 10:
        spin_from_obstacle(SPINTIME)
    buggy.stop()
    sleep(10)

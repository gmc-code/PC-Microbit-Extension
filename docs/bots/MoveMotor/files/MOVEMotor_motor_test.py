# Motor tests for MOVEMotor module

from microbit import *
import docs.bots.MoveMotor.files.MOVEMotor_v31 as MOVEMotor_v31


# setup buggy
buggy = MOVEMotor_v31.MOVEMotorMotors()
buggy.stop()
sleep(500)
# gap between tests
SLEEPGAP = 1000


def forward_backward_test():
    # forwards(speed=1, duration=None, decrease_left=0, decrease_right=0)
    # backwards(speed=1, duration=None, decrease_left=0, decrease_right=0)
    for i in range(2, 11, 1):
        buggy.forwards(i, 250)
    buggy.stop()
    for i in range(2, 11, 1):
        buggy.backwards(i, 250)
    buggy.stop()
    sleep(SLEEPGAP)


def straight_line_test():
    # forwards(speed=1, duration=None, decrease_left=0, decrease_right=0)
    # backwards(speed=1, duration=None, decrease_left=0, decrease_right=0)
    delta = 5
    buggy.forwards(2, 200, delta, 0)
    buggy.forwards(5, 200, delta, 0)
    buggy.forwards(9, 1000, delta, 0)
    buggy.forwards(5, 200, delta, 0)
    buggy.forwards(2, 200, delta, 0)
    buggy.stop()
    buggy.backwards(2, 200, delta, 0)
    buggy.backwards(5, 200, delta, 0)
    buggy.backwards(9, 1000, delta, 0)
    buggy.backwards(5, 200, delta, 0)
    buggy.backwards(2, 200, delta, 0)
    buggy.stop()
    sleep(SLEEPGAP)


def individual_motors_test():
    # left_motor(speed=1, duration=None)
    # right_motor(speed=1, duration=None)
    for i in range(-10, 11, 2):
        buggy.left_motor(i, 300)
    buggy.stop()
    for i in range(10, -11, -2):
        buggy.right_motor(i, 300)
    buggy.stop()
    sleep(SLEEPGAP)


def spin_test():
    # spin(speed=1, duration=None)
    for i in range(2, 11, 2):
        buggy.spin_left(i, 500)
    buggy.stop()
    for i in range(2, 11, 2):
        buggy.spin_right(i, 500)
    buggy.stop()
    sleep(SLEEPGAP)


def turn_test():
    # left(speed=1, radius=25, duration=None)
    # right(speed=1, radius=25, duration=None)
    for i in range(2, 11, 2):
        buggy.left(i, 25, 400)
    buggy.stop()
    for i in range(2, 11, 2):
        buggy.right(i, 25, 400)
    buggy.stop()
    sleep(SLEEPGAP)


def zigzag_test(slow_speed=2, fast_speed=4, zigzag_count=5, zigzag_time=1000):
    for i in range(zigzag_count):
        buggy.left_motor(fast_speed)
        buggy.right_motor(slow_speed)
        sleep(zigzag_time)
        buggy.left_motor(slow_speed)
        buggy.right_motor(fast_speed)
        sleep(zigzag_time)
    for i in range(zigzag_count):
        buggy.left_motor(-slow_speed)
        buggy.right_motor(-fast_speed)
        sleep(zigzag_time)
        buggy.left_motor(-fast_speed)
        buggy.right_motor(-slow_speed)
        sleep(zigzag_time)
    buggy.stop()
    sleep(SLEEPGAP)


def polygon_test(spin_duration=240, sides=20):
    for i in range(sides):
        buggy.forwards(3, 800)
        buggy.spin_left(1, spin_duration)
    buggy.stop()
    sleep(SLEEPGAP)


def spiral_test():
    for i in [10, 20, 40, 60, 80, 100]:
        buggy.left(3, i, duration=1000)
    buggy.stop()
    sleep(SLEEPGAP)


def oval_test():
    radii = [20, 40, 60, 80, 60, 40]
    durations = [500, 600, 1000, 1000, 1000, 600]
    for i in range(6):
        for r, d in zip(radii, durations):
            buggy.left(3, r, d)
    buggy.stop()
    sleep(SLEEPGAP)


def loops_test():
    radii = [10, 30, 80, 30]
    durations = [2000, 400, 1200, 400]
    for i in range(4):
        for r, d in zip(radii, durations):
            buggy.left(3, r, d)
    buggy.stop()
    sleep(SLEEPGAP)


def buggy_stop_test():
    # only for verison 3.1 movemotor
    for brightness in range(0, 255, 10):
        buggy.stop(brightness)
        sleep(100)
    buggy.stop()


def buggy_test():
    forward_backward_test()
    straight_line_test()
    individual_motors_test()
    spin_test()
    turn_test()
    # zigzag_test()
    # polygon_test()
    # spiral_test()
    # oval_test()
    # loops_test()


while True:
    if button_a.is_pressed():
        buggy_test()
    else:
        buggy_stop_test()

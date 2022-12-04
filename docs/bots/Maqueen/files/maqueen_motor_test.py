# Motor tests for Maqueen module

from microbit import *
import maqueen


# setup buggy
buggy = maqueen.MaqueenMotors()
buggy.stop()
sleep(500)


def individual_motors_test():
    # individual motors
    for spd in range(-5, 5, 1):
        display.scroll(spd)
        buggy.left_motor(spd, 1000)
    buggy.stop()
    for spd in range(5, -5, -1):
        display.scroll(spd)
        buggy.right_motor(spd, 1000)
    buggy.stop()
    sleep(2000)


def spin_test():
    # speed=1, direction='left', duration=None)
    display.scroll('spin')
    buggy.spin_left(duration=1000)
    buggy.spin_left(duration=1000)
    buggy.spin_left(5, duration=1000)
    buggy.spin_left(2, duration=1000)
    buggy.spin_right(2, duration=1000)
    buggy.spin_right(5, 1000)
    buggy.stop()
    sleep(2000)

def forward_backward_test():
    display.scroll('fb')
    buggy.forwards(duration=1000)
    buggy.backwards(duration=1000)
    buggy.forwards(5, 1000)
    buggy.backwards(5, 1000)
    buggy.stop()
    sleep(2000)

def forward_backward_speed_test():
    display.scroll('fb+')
    for spd in range(1, 5, 1):
        display.scroll(spd)
        buggy.forwards(spd, duration=1000)
        buggy.stop()
        buggy.backwards(spd, duration=1000)
        buggy.stop()
    sleep(2000)

def turn_test():
    display.scroll('turn')
    buggy.left(duration=1000)
    buggy.left(3, duration=1000)
    buggy.left(tightness=2, duration=1000)
    buggy.left(1, 1000)
    buggy.stop()
    buggy.right(1, 1000)
    buggy.right(2, duration=1000)
    buggy.right(tightness=3, duration=1000)
    buggy.right(duration=1000)
    buggy.stop()
    sleep(2000)


def zigzag_test(slow_speed=1, fast_speed=5, zigzag_count=5, zigzag_time=1000):
    display.scroll('zz')
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

def spiral_test():
    display.scroll('spiral')
    for i in [5, 4, 3, 2, 1]:
        buggy.left(i, duration=1000)
    buggy.stop()
    sleep(2000)

def polygon_test():
    display.scroll('polygon')
    for i in range(13):
        buggy.forwards(5, 800)
        buggy.spin_left(5, 280)
    buggy.stop()
    sleep(2000)

def oval_test():
    display.scroll('oval')
    dist = [3, 2, 1, 2]
    tdist = [50, 100, 4000, 100]
    for i in range(4):
        for d, t in zip(dist, tdist):
            buggy.left(d, t)
    buggy.stop()
    sleep(2000)

def loops_test():
    display.scroll('loops')
    dist = [4, 3, 1, 3]
    tdist = [3000, 400, 1200, 400]
    for i in range(4):
        for d, t in zip(dist, tdist):
            buggy.left(d, t)
    buggy.stop()
    sleep(2000)

while True:
    individual_motors_test()
    spin_test()
    forward_backward_test()
    forward_backward_speed_test()
    turn_test()
    zigzag_test()
    spiral_test()
    polygon_test()
    oval_test()
    loops_test()


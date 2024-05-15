# maqueen module for motors, line following and distance sensing
# requires microbit v2
# GMC-code; 2022
# The MIT License (MIT)
# motor uses i2c
# motor speeds from 0,1,2,3,4,5
# turn tightness from 5,4,3,2,1
# 5 being tightest without spinning by reversing other wheel

from microbit import *
import machine
import utime
from neopixel import NeoPixel as leds


CHIP_ADDR = 0x10
LEFT_MOTOR = 0x00
RIGHT_MOTOR = 0x02
forwards = 0x00
backwards= 0x01
SERVO_ONE = 0x14
SERVO_TWO = 0x15

TRIGGER_PIN = pin1
ECHO_PIN = pin2
LEFT_HEADLIGHT_PIN = pin8
RIGHT_HEADLIGHT_PIN = pin12
LEFT_LINE_SENSOR_PIN = pin13
RIGHT_LINE_SENSOR_PIN = pin14	
IR_PIN = pin16

MOTOR_SPEEDS = [0, 20, 25, 30, 60, 255]
MPC = len(MOTOR_SPEEDS) - 1  # Motor speed count used for tightness of turns


class MaqueenMotors:

    def stop_left(self):
        buffer = bytearray(3)
        buffer[0] = LEFT_MOTOR
        buffer[1] = FORWARD
        buffer[2] = 0
        i2c.write(CHIP_ADDR, buffer, False)

    def stop_right(self):
        buffer = bytearray(3)
        buffer[0] = RIGHT_MOTOR
        buffer[1] = FORWARD
        buffer[2] = 0
        i2c.write(CHIP_ADDR, buffer, False)

    def stop(self):
        self.stop_left()
        self.stop_right()

    @staticmethod
    def _analog_speed(self, speed):
        if speed < -MPC:
            return -MOTOR_SPEEDS[MPC]
        elif speed < 0 and speed >= -MPC:
            return -MOTOR_SPEEDS[abs(int(speed))]
        elif speed > 0 and speed <= MPC:
            return MOTOR_SPEEDS[int(speed)]
        elif speed > MPC:
            return MOTOR_SPEEDS[MPC]
        else:
            return 0

    def left_motor(self, speed=1, duration=None):
        buffer = bytearray(3)
        buffer[0] = LEFT_MOTOR
        if (speed > 0):
            buffer[1] = FORWARD
        else:
            buffer[1] = BACKWARD
        buffer[2] = abs(self._analog_speed(self, speed))
        i2c.write(CHIP_ADDR, buffer, False)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop_left()

    def right_motor(self, speed=1, duration=None):
        buffer = bytearray(3)
        buffer[0] = RIGHT_MOTOR
        if (speed > 0):
            buffer[1] = FORWARD
        else:
            buffer[1] = BACKWARD
        buffer[2] = abs(self._analog_speed(self, speed))
        i2c.write(CHIP_ADDR, buffer, False)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop_right()

    def backwards(self, speed=1, duration=None):
        analog_speed = abs(self._analog_speed(self, speed))
        buffer = bytearray(3)
        buffer[0] = LEFT_MOTOR
        buffer[1] = BACKWARD
        buffer[2] = analog_speed
        i2c.write(CHIP_ADDR, buffer, False)
        buffer = bytearray(3)
        buffer[0] = RIGHT_MOTOR
        buffer[1] = BACKWARD
        buffer[2] = analog_speed
        i2c.write(CHIP_ADDR, buffer, False)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    def forwards(self, speed=1, duration=None):
        analog_speed = abs(self._analog_speed(self, speed))
        buffer = bytearray(3)
        buffer[0] = LEFT_MOTOR
        buffer[1] = FORWARD
        buffer[2] = analog_speed
        i2c.write(CHIP_ADDR, buffer, False)
        buffer = bytearray(3)
        buffer[0] = RIGHT_MOTOR
        buffer[1] = FORWARD
        buffer[2] = analog_speed
        i2c.write(CHIP_ADDR, buffer, False)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    @staticmethod
    def _inner_turn_speed(self, tightness=MPC):
        return MOTOR_SPEEDS[MPC - tightness]

    def left(self, tightness=MPC, duration=None):
        # right motor faster than left
        inner_turn_speed = self._inner_turn_speed(self, tightness)
        buffer = bytearray(3)
        buffer[0] = LEFT_MOTOR
        buffer[1] = FORWARD
        buffer[2] = inner_turn_speed
        i2c.write(CHIP_ADDR, buffer, False)
        utime.sleep_ms(2)
        buffer = bytearray(3)
        buffer[0] = RIGHT_MOTOR
        buffer[1] = FORWARD
        buffer[2] = 255
        i2c.write(CHIP_ADDR, buffer, False)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    def right(self, tightness=MPC, duration=None):
        # left motor faster than right
        inner_turn_speed = self._inner_turn_speed(self, tightness)
        buffer = bytearray(3)
        buffer[0] = LEFT_MOTOR
        buffer[1] = FORWARD
        buffer[2] = 255
        i2c.write(CHIP_ADDR, buffer, False)
        utime.sleep_ms(2)
        buffer = bytearray(3)
        buffer[0] = RIGHT_MOTOR
        buffer[1] = FORWARD
        buffer[2] = inner_turn_speed
        i2c.write(CHIP_ADDR, buffer, False)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    def spin_left(self, speed=1, duration=None):
        analog_speed = abs(self._analog_speed(self, speed))
        buffer = bytearray(3)
        buffer[0] = LEFT_MOTOR
        buffer[1] = BACKWARD
        buffer[2] = analog_speed
        i2c.write(CHIP_ADDR, buffer, False)
        buffer[0] = RIGHT_MOTOR
        buffer[1] = FORWARD
        buffer[2] = analog_speed
        i2c.write(CHIP_ADDR, buffer, False)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    def spin_right(self, speed=1, duration=None):
        analog_speed = abs(self._analog_speed(self, speed))
        buffer = bytearray(3)
        buffer[0] = LEFT_MOTOR
        buffer[1] = FORWARD
        buffer[2] = analog_speed
        i2c.write(CHIP_ADDR, buffer, False)
        buffer[0] = RIGHT_MOTOR
        buffer[1] = BACKWARD
        buffer[2] = analog_speed
        i2c.write(CHIP_ADDR, buffer, False)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    # angle: {0-180}
    def servo_one(self, angle=0):
        buffer = bytearray(2)
        buffer[0] = SERVO_ONE
        buffer[1] = angle
        i2c.write(CHIP_ADDR, buffer, False)

    # angle: {0-180}
    def servo_two(self, angle=0):
        buffer = bytearray(2)
        buffer[0] = SERVO_TWO
        buffer[1] = angle
        i2c.write(CHIP_ADDR, buffer, False)


class MaqueenLineSensors:

    def line_sensor_read(self, sensor):
        if sensor == 'left':
            return LEFT_LINE_SENSOR_PIN.read_digital()
        elif sensor == 'right':
            return RIGHT_LINE_SENSOR_PIN.read_digital()


class MaqueenDistanceSensor:

    def distance(self):
        ECHO_PIN.set_pull(ECHO_PIN.NO_PULL)
        TRIGGER_PIN.write_digital(0)
        utime.sleep_us(2)
        TRIGGER_PIN.write_digital(1)
        utime.sleep_us(10)
        TRIGGER_PIN.write_digital(0)
        distance = machine.time_pulse_us(ECHO_PIN, 1, 1160000)
        if distance > 0:
            # distance in cm
            return round(distance/58)
        else:
            return 0


class MaqueenIR:

    def get_IR(self):
        IR_PIN.set_pull(IR_PIN.PullUp)


class MaqueenHeadLights:

    def set_headlight(self, headlight='left', on=1):
        # value = 1 for on and 0 for off
        if headlight == 'left':
            if on == 1:
                LEFT_HEADLIGHT_PIN.write_digital(1)
            else:
                LEFT_HEADLIGHT_PIN.write_digital(0)
        elif headlight == 'right':
            if on == 1:
                RIGHT_HEADLIGHT_PIN .write_digital(1)
            else:
                RIGHT_HEADLIGHT_PIN .write_digital(0)

    def set_headlights(self, left=1, right=1):
        # value = 1 for on and 0 for off
        LEFT_HEADLIGHT_PIN.write_digital(left)
        RIGHT_HEADLIGHT_PIN .write_digital(right)


class MaqueenNeoPixels:

    def __init__(self, front=(20, 20, 20), indicator=(35, 25, 0), rear=(20, 0, 0)):
        self.np = leds(pin15, 4)
        self.front = front
        self.indicator = indicator
        self.rear = rear

    # rgb: (red: {0-255}, green: {0-255}, blue: {0-255})
    # front left = 0; rear left = 1; rear right = 2; front right = 3

    def set_front(self, rgb=(20, 20, 20)):
        self.front = rgb

    def set_indicator(self, rgb=(35, 25, 0)):
        self.indicator = rgb

    def set_rear(self, rgb=(20, 0, 0)):
        self.rear = rgb

    def set_led(self, led_number, rgb=(20, 20, 20)):
        self.np[led_number] = rgb
        self.np.show()

    def set_leds(self, rgb=(20, 20, 20)):
        for led_number in range(4):
            self.np[led_number] = rgb
        self.np.show()

    def rear_lights(self):
        self.np[1] = self.rear
        self.np[2] = self.rear

    def all_lights(self, left, right):
        self.np[0] = left
        self.np[3] = right
        self.rear_lights()
        self.np.show()

    def front_lights(self):
        self.all_lights(self.front, self.front)

    def left_indicator(self):
        self.all_lights(self.indicator, self.front)

    def right_indicator(self):
        self.all_lights(self.front, self.indicator)

    def both_indicators(self):
        self.all_lights(self.indicator, self.indicator)


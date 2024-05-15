# micropython module for the Kitronik :MOVE Motor buggy v3.1
# for microbit v2
# MOVEMotor module for motors, line following and distance sensing
# GMC-code 2024
# The MIT License (MIT)
# Depending on board version, motors are driven in different ways:
# V1 and 2 - PCA9632, motor uses i2c
# V3.1 - WS2811
# The jerk message gives the motor a 'shove' at full power to aid starting on lower pwm ratios

# motor uses pin12 on v3.1:MOVE Motor; WS2811 ICs, each with RGB (RG = Motor, B = Brake light)
# right motor is WS2811[0] and backwards, forwards is the RG order
# left motor is WS2811[1] and forwards, backwards is the RG order

# A bytearray is a mutable sequence of bytes with integer values in the range 0 <= x < 256.
# in motorGo mg[0] and in motorJump mj[0] = 255, it’s stored as a byte in the bytearray; when retrieved it’s still a byte.
# direct calls using integers seem to work as in: self.ws2811[1] = (0, 0, brightness)

# see https://github.com/KitronikLtd/micropython-microbit-kitronik-MOVE-motor
# see Kitronic MakeCode module: https://github.com/KitronikLtd/pxt-kitronik-move-motor/blob/master/main.ts
# for quick lookups of hex values
# see https://www.prepressure.com/library/technology/ascii-binary-hex
# See datasheet: https://www.nxp.com/docs/en/data-sheet/PCA9632.pdf
# pin15, pin16, are for servo
# for v3.1 of movemotor; motor uses pin12 as a neopixel
# pin 8 for LEDS

from microbit import i2c, pin1, pin2, pin8, pin12, pin13, pin14, display, sleep

import machine
import utime
from neopixel import NeoPixel


# constants
# LEDS_NUMBER = 4
RIGHT_LINE_SENSOR_PIN = pin1
LEFT_LINE_SENSOR_PIN = pin2
TRIGGER_PIN = pin14
ECHO_PIN = pin13

# for testing if version v2 prior to v3.1
CHIP_ADDR = 0x62
MODE_1_REG_ADDR = 0x00
MODE_1_REG_VALUE = 0x00


class MOVEMotorMotors:
    def __init__(self):

        try:
            # Attempting to write/read a register on the PCA9632 IC will identify
            # whether the IC is there or not (no PCA9632 on V3.1)
            # Note: This check relies on the micro:bit not throwing an error
            # when an I2C address is used which isn't present on the I2C bus
            buffer = bytearray(2)
            buffer[0] = MODE_1_REG_ADDR
            buffer[1] = MODE_1_REG_VALUE
            i2c.write(CHIP_ADDR, buffer, False)
            readBuffer = i2c.read(CHIP_ADDR, 1, False)
            if readBuffer[0] == MODE_1_REG_VALUE:
                self.moveMotorVersion = 10  # not 31
                display.scroll("Change library: not v3.1")
        except OSError:
            self.moveMotorVersion = 31
            # display.scroll(self.moveMotorVersion, delay=60)
            # ws2811[0] is right motor, [1] is left motor
            self.ws2811 = NeoPixel(pin12, 2)

    def stop_left(self, brightness=255):
        # Left motor
        self.ws2811[1] = (0, 0, brightness)
        self.ws2811.show()

    def stop_right(self, brightness=255):
        # Right motor
        self.ws2811[0] = (0, 0, brightness)
        self.ws2811.show()

    def stop(self, brightness=255):
        self.ws2811[0] = (0, 0, brightness)
        self.ws2811[1] = (0, 0, brightness)
        self.ws2811.show()

    @staticmethod
    def _analog_speed(speed):
        # input speed = -10 to 0 to 10
        # output = 60 to 255
        if speed < 0 and speed >= -10:
            return int((speed * -21) + 45)
        elif speed > 0 and speed <= 10:
            return int((speed * 21) + 45)
        else:
            return 0

    def left_motor(self, speed=1, duration=None):
        mg = bytearray([0, 0, 0])
        mj = bytearray([0, 0, 0])
        motor_speed = self._analog_speed(speed)
        # Left motor
        wsIndex = 1
        if speed > 0:
            # Going forwards
            mg[0] = motor_speed
            mj[0] = 255
        else:
            # Going backwards
            mg[1] = motor_speed
            mj[1] = 255
        self.ws2811[wsIndex] = (mj[0], mj[1], mj[2])
        self.ws2811.show()
        sleep(1)  # 1 ms to allow for motor processing
        self.ws2811[wsIndex] = (mg[0], mg[1], mg[2])
        self.ws2811.show()
        #
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop_left()

    def right_motor(self, speed=1, duration=None):
        # speed values are integers or floats (decimals) from -10 to 10.
        mg = bytearray([0, 0, 0])
        mj = bytearray([0, 0, 0])
        motor_speed = self._analog_speed(speed)
        # Right  motor
        wsIndex = 0
        if speed > 0:
            # Going forwards
            mg[1] = motor_speed
            mj[1] = 255
        else:
            # Going backwards
            mg[0] = motor_speed
            mj[0] = 255
        self.ws2811[wsIndex] = (mj[0], mj[1], mj[2])
        self.ws2811.show()
        sleep(1)  # 1 ms
        self.ws2811[wsIndex] = (mg[0], mg[1], mg[2])
        self.ws2811.show()
        #
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop_right()

    @staticmethod
    def _straight_line_adjustment(analog_speed, adjustment):
        # limit adjustment to 0 to 20
        # make percentage adjustment (adjustment/max analog) to _analog_speed
        if adjustment < 0:
            adjustment = 0
        elif adjustment > 20:
            adjustment = 20
        return int(analog_speed * (255 - adjustment) / 255)

    def backwards(self, speed=1, duration=None, decrease_left=0, decrease_right=0):
        # speed 0 to 10
        analog_speed = abs(self._analog_speed(speed))
        mg = bytearray([0, 0, 0])
        mj = bytearray([0, 0, 0])
        ##
        right_speed = self._straight_line_adjustment(analog_speed, decrease_right)
        left_speed = self._straight_line_adjustment(analog_speed, decrease_left)
        # Jump motor to get it going for 1 millisec at full power
        # Going backwards
        # Right  motor
        mj[0] = 255
        # right motor is WS2811[0] and backwards, forwards is the RG order
        self.ws2811[0] = (mj[0], mj[1], mj[2])
        # left  motor
        mj[0] = 0
        mj[1] = 255
        # left motor is WS2811[1] and forwards, backwards is the RG order
        self.ws2811[1] = (mj[0], mj[1], mj[2])
        self.ws2811.show()
        sleep(1)  # 1 ms
        # Going backwards
        # Right  motor
        mg[0] = right_speed
        # right motor is WS2811[0] and backwards, forwards is the RG order
        self.ws2811[0] = (mg[0], mg[1], mg[2])
        # left  motor
        mg[0] = 0
        mg[1] = left_speed
        # left motor is WS2811[1] and forwards, backwards is the RG order
        self.ws2811[1] = (mg[0], mg[1], mg[2])
        self.ws2811.show()
        #
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    def forwards(self, speed=1, duration=None, decrease_left=0, decrease_right=0):
        # speed 0 to 10
        analog_speed = abs(self._analog_speed(speed))
        mg = bytearray([0, 0, 0])
        mj = bytearray([0, 0, 0])
        ##
        right_speed = self._straight_line_adjustment(analog_speed, decrease_right)
        left_speed = self._straight_line_adjustment(analog_speed, decrease_left)
        # Jump motor to get it going for 1 millisec at full power
        # Right motor
        mj[1] = 255
        # right motor is WS2811[0] and backwards, forwards is the RG order
        self.ws2811[0] = (mj[0], mj[1], mj[2])
        # left motor
        mj[0] = 255
        mj[1] = 0
        # left motor is WS2811[1] and forwards, backwards is the RG order
        self.ws2811[1] = (mj[0], mj[1], mj[2])
        self.ws2811.show()
        #
        sleep(1)  # 1 ms
        # Going backwards
        # Right  motor
        mg[1] = right_speed
        # right motor is WS2811[0] and backwards, forwards is the RG order
        self.ws2811[0] = (mg[0], mg[1], mg[2])
        # left  motor
        mg[0] = left_speed
        mg[1] = 0
        # left motor is WS2811[1] and forwards, backwards is the RG order
        self.ws2811[1] = (mg[0], mg[1], mg[2])
        self.ws2811.show()
        #
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    @staticmethod
    def _turn_radius_factor(radius=25):
        # limit radius (in cm) of inner wheel to 4 to 800 cm
        # calculate the relative speed factor of the inner to outer wheel
        # uses approximate distance between buggy wheels of 8.5 cm
        if radius < 4:
            radius = 4
        elif radius > 800:
            radius = 800
        return (radius + 8.5) / radius

    def left(self, speed=1, radius=25, duration=None):
        # right motor faster than left
        # speed values are integers or floats (decimals) from -10 to 10.
        # speed values above 0 drive the buggy forwards to the left.
        # speedvalues below 0 drive the buggy backwards to the left.
        motor_speed = self._analog_speed(speed)
        turn_radius_factor = self._turn_radius_factor(radius)
        motor_speed_inner = int(motor_speed / turn_radius_factor)
        #
        right_mg = bytearray([0, 0, 0])
        right_mj = bytearray([0, 0, 0])
        left_mg = bytearray([0, 0, 0])
        left_mj = bytearray([0, 0, 0])
        if speed > 0:
            # Going forwards
            # right motor is WS2811[0]; 0 backwards, 1 forwards is the RG order
            right_mg[1] = motor_speed
            right_mj[1] = 255
            # left motor is WS2811[1]; 0 forwards, 1 backwards is the RG order
            left_mg[0] = motor_speed_inner
            left_mj[0] = 255
        else:
            # Going backwards
            # right motor is WS2811[0]; 0 backwards, 1 forwards is the RG order
            right_mg[0] = motor_speed
            right_mj[0] = 255
            # left motor is WS2811[1]; 0 forwards, 1 backwards is the RG order
            left_mg[1] = motor_speed_inner
            left_mj[1] = 255
        # right
        self.ws2811[0] = (right_mj[0], right_mj[1], right_mj[2])
        # left
        self.ws2811[1] = (left_mj[0], left_mj[1], left_mj[2])
        self.ws2811.show()
        sleep(1)  # 1 ms
        # right
        self.ws2811[0] = (right_mg[0], right_mg[1], right_mg[2])
        # left
        self.ws2811[1] = (left_mg[0], left_mg[1], left_mg[2])
        self.ws2811.show()
        #
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    def right(self, speed=1, radius=25, duration=None):
        # left motor faster than right
        # speed values are integers or floats (decimals) from -10 to 10.
        # speed values above 0 drive the buggy forwards to the left.
        # speedvalues below 0 drive the buggy backwards to the left.
        motor_speed = self._analog_speed(speed)
        turn_radius_factor = self._turn_radius_factor(radius)
        motor_speed_inner = int(motor_speed / turn_radius_factor)
        #
        right_mg = bytearray([0, 0, 0])
        right_mj = bytearray([0, 0, 0])
        left_mg = bytearray([0, 0, 0])
        left_mj = bytearray([0, 0, 0])
        if speed > 0:
            # Going forwards
            # right motor is WS2811[0]; 0 backwards, 1 forwards is the RG order
            right_mg[1] = motor_speed_inner
            right_mj[1] = 255
            # left motor is WS2811[1]; 0 forwards, 1 backwards is the RG order
            left_mg[0] = motor_speed
            left_mj[0] = 255
        else:
            # Going backwards
            # right motor is WS2811[0]; 0 backwards, 1 forwards is the RG order
            right_mg[0] = motor_speed_inner
            right_mj[0] = 255
            # left motor is WS2811[1]; 0 forwards, 1 backwards is the RG order
            left_mg[1] = motor_speed
            left_mj[1] = 255
        # right
        self.ws2811[0] = (right_mj[0], right_mj[1], right_mj[2])
        # left
        self.ws2811[1] = (left_mj[0], left_mj[1], left_mj[2])
        self.ws2811.show()
        sleep(1)  # 1 ms
        # right
        self.ws2811[0] = (right_mg[0], right_mg[1], right_mg[2])
        # left
        self.ws2811[1] = (left_mg[0], left_mg[1], left_mg[2])
        self.ws2811.show()
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    def spin_left(self, speed=1, duration=None):
        # speed values are integers or floats (decimals) from 0 to 10.
        analog_speed = abs(self._analog_speed(speed))
        #
        right_mg = bytearray([0, 0, 0])
        right_mj = bytearray([0, 0, 0])
        left_mg = bytearray([0, 0, 0])
        left_mj = bytearray([0, 0, 0])
        # left back and right fwd
        # right motor is WS2811[0]; 0 backwards, 1 forwards is the RG order
        right_mg[1] = analog_speed
        right_mj[1] = 255
        # left motor is WS2811[1]; 0 forwards, 1 backwards is the RG order
        left_mg[1] = analog_speed
        left_mj[1] = 255
        # right
        self.ws2811[0] = (right_mj[0], right_mj[1], right_mj[2])
        # left
        self.ws2811[1] = (left_mj[0], left_mj[1], left_mj[2])
        self.ws2811.show()
        sleep(1)  # 1 ms
        # right
        self.ws2811[0] = (right_mg[0], right_mg[1], right_mg[2])
        # left
        self.ws2811[1] = (left_mg[0], left_mg[1], left_mg[2])
        self.ws2811.show()
        #
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    def spin_right(self, speed=1, duration=None):
        # speed values are integers or floats (decimals) from 0 to 10.
        analog_speed = abs(self._analog_speed(speed))
        #
        right_mg = bytearray([0, 0, 0])
        right_mj = bytearray([0, 0, 0])
        left_mg = bytearray([0, 0, 0])
        left_mj = bytearray([0, 0, 0])
        # left fws and right back
        # right motor is WS2811[0]; 0 backwards, 1 forwards is the RG order
        right_mg[0] = analog_speed
        right_mj[0] = 255
        # left motor is WS2811[1]; 0 forwards, 1 backwards is the RG order
        left_mg[0] = analog_speed
        left_mj[0] = 255
        # right
        self.ws2811[0] = (right_mj[0], right_mj[1], right_mj[2])
        # left
        self.ws2811[1] = (left_mj[0], left_mj[1], left_mj[2])
        self.ws2811.show()
        sleep(1)  # 1 ms
        # right
        self.ws2811[0] = (right_mg[0], right_mg[1], right_mg[2])
        # left
        self.ws2811[1] = (left_mg[0], left_mg[1], left_mg[2])
        self.ws2811.show()
        #
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()


class MOVEMotorLineSensors:
    def __init__(self):
        self.left_offset = 0
        self.right_offset = 0

    def line_sensor_calibrate(self):
        rightLineSensor = RIGHT_LINE_SENSOR_PIN.read_analog()
        leftLineSensor = LEFT_LINE_SENSOR_PIN.read_analog()
        offset = int(abs(rightLineSensor - leftLineSensor) / 2)
        if leftLineSensor > rightLineSensor:
            self.left_offset = -offset
            self.right_offset = offset
        else:
            self.left_offset = offset
            self.right_offset = -offset

    def line_sensor_read(self, sensor):
        if sensor == "left":
            return LEFT_LINE_SENSOR_PIN.read_analog() + self.left_offset
        elif sensor == "right":
            return RIGHT_LINE_SENSOR_PIN.read_analog() + self.right_offset


class MOVEMotorDistanceSensors:
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
            return round(distance / 58)
        else:
            return 0

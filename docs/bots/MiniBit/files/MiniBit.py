# MiniBit module for motors, and distance sensing
# requires microbit v2
# GMC-code; 2022
# The MIT License (MIT)

# A microbit v2 micropython module
# speed from -10 to 10


from microbit import *
import utime

# constants
LMF = pin12
LMB = pin8
RMF = pin16
RMB = pin14
DSP = pin15
                   
class MiniBitMotors:

    def __init__(self):
        # no need to do anything
        pass

    def stop(self):
        LMF.write_digital(0)
        LMB.write_digital(0)
        RMF.write_digital(0)
        RMB.write_digital(0)

    @staticmethod
    def scale(from_value, from_min, from_max, to_min, to_max):
        return int(((from_value - from_min) / (from_max - from_min)) * (to_max - to_min) + to_min)

    @staticmethod
    def speed_scaled(speed):
        return __class__.scale(speed, 0, 10, 0, 1023)
        
    def forwards(self, speed=2, duration=None):
        analog_speed = self.speed_scaled(speed)
        LMF.write_analog(analog_speed)
        LMB.write_digital(0)
        RMF.write_analog(analog_speed)
        RMB.write_digital(0)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    def backwards(self, speed=2, duration=None):
        analog_speed = self.speed_scaled(speed)
        LMF.write_digital(0)
        LMB.write_analog(analog_speed)
        RMF.write_digital(0)
        RMB.write_analog(analog_speed)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    @staticmethod
    def inner_turn_speed(speed, tightness=2):
        if tightness == 0:
            return 0
        else:
            return int(speed / tightness)


    def left(self, speed=2, tightness=2, duration=None):
        outer_speed = speed_scaled(speed)
        inner_speed = inner_turn_speed(outer_speed, tightness)
        if speed > 0:
            LMF.write_analog(inner_speed)
            LMB.write_digital(0)
            RMF.write_analog(outer_speed)
            RMB.write_digital(0)
        else:
            LMF.write_digital(0)
            LMB.write_analog(-inner_speed)
            RMF.write_digital(0)
            RMB.write_analog(-outer_speed)
        if duration is not None:
            utime.sleep_ms(duration)
            stop()


    def right(self, speed=2, tightness=2, duration=None):
        outer_speed = self.speed_scaled(speed)
        inner_speed = self.inner_turn_speed(outer_speed, tightness)
        if speed > 0:
            LMF.write_analog(outer_speed)
            LMB.write_digital(0)
            RMF.write_analog(inner_speed)
            RMB.write_digital(0)
        else:
            LMF.write_digital(0)
            LMB.write_analog(-outer_speed)
            RMF.write_digital(0)
            RMB.write_analog(-inner_speed)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    def spin_left(self, speed=2, duration=None):
        analog_speed = self.speed_scaled(speed)
        LMF.write_digital(0)
        LMB.write_analog(analog_speed)
        RMF.write_analog(analog_speed)
        RMB.write_digital(0)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()

    def spin_right(self, speed=2, duration=None):
        analog_speed = self.speed_scaled(speed)
        LMF.write_analog(analog_speed)
        LMB.write_digital(0)
        RMF.write_digital(0)
        RMB.write_analog(analog_speed)
        if duration is not None:
            utime.sleep_ms(duration)
            self.stop()


class MiniBitDistanceSensor():

    def distance(self):
        DSP.write_digital(1)
        utime.sleep_us(10)
        DSP.write_digital(0)

        while DSP.read_digital() == 0:
            pulse_start = utime.ticks_us()
        while DSP.read_digital() == 1:
            pulse_end = utime.ticks_us()

        try:
            pulse_duration = pulse_end - pulse_start
        except ValueError:
            pulse_duration = 0
        else:
            pulse_duration = 0

        distance = int(0.01715 * pulse_duration)
        return distance


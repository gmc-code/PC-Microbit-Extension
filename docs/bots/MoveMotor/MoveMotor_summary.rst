====================================================
MOVEMotor summary
====================================================

| A summary of the MoveMotor methods is below.
| General speed values are integers or floats (decimals) from -10 to 10.
| Spin speed values are integers or floats (decimals) from 0 to 10.
| Turn radius values are from 4 to 800 (in cm)

.. code-block:: python

    from microbit import *
    import MOVEMotor
    import neopixel


    buggy = MOVEMotor.MOVEMotorMotors()
    buggy.left_motor(speed=1, duration=1000)
    buggy.stop_left()
    buggy.right_motor(speed=4, duration=3000)
    buggy.stop_right()
    buggy.forwards(speed=6, duration=5000, decrease_left=6, decrease_right=0)
    buggy.backwards(speed=4, duration=5000, decrease_left=0, decrease_right=3)
    buggy.left(speed=3, radius=20, duration=4000)
    buggy.right(speed=2, radius=40, duration=3000)
    buggy.spin_left(speed=1, duration=2000)
    buggy.spin_right(speed=2, duration=1000)
    buggy.stop()

    distance_sensor = MOVEMotor.MOVEMotorDistanceSensors()
    dist = distance_sensor.distance()

    line_sensor = MOVEMotor.MOVEMotorLineSensors()
    line_sensor.line_sensor_calibrate()
    left_reading = line_sensor.line_sensor_read('left')
    right_reading = line_sensor.line_sensor_read('right')

    lights = neopixel.NeoPixel(pin8, 4)
    lights[0] = (0, 255, 255)
    lights.show()
    sleep(2000)
    lights.clear()





====================================================
BitBotXL summary
====================================================


| A summary of the BitBotXL methods:

.. code-block:: python

    from microbit import *
    import MOVEMotor
    import neopixel


    buggy = BitBotXL.BitBotXLMotors()
    buggy.stop_left()
    buggy.stop_right()
    buggy.stop()

    buggy.left_motor(speed=1, duration=None)
    buggy.right_motor(speed=1, duration=None)
    
    buggy.forwards(speed=6, duration=None, decrease_left=0, decrease_right=0)
    buggy.backwards(speed=4, duration=None, decrease_left=0, decrease_right=0)

    buggy.left(speed=1, tightness=2, duration=None)
    buggy.right(speed=1, tightness=2, duration=None)

    buggy.spin_left(speed=1, duration=None)
    buggy.spin_right(speed=1, duration=None)
    

    distance_sensor = BitBotXL.BitBotXLDistanceSensor()
    dist = distance_sensor.distance()

    buggyLights = neopixel.NeoPixel(pin13, 12)
    buggyLights[0] = (0, 255, 255)
    buggyLights.show()
    sleep(2000)
    buggyLights.clear()





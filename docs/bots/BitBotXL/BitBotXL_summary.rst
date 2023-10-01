====================================================
BitBotXL summary
====================================================


| A summary of the BitBotXL methods is below.
| Speeds values are 0 to 10 for forwards and backwards and spin_left and spin_right.
| Speeds values are -10 to 10 for left_motor and right_motor and left and right.
| Suggested tightness values are from 1 to 10.


.. code-block:: python

    from microbit import *
    import BitBotXL
    import neopixel


    buggy = BitBotXL.BitBotXLMotors()
    buggy.stop_left()
    buggy.stop_right()
    buggy.stop()

    buggy.left_motor(speed=2, duration=None)
    buggy.right_motor(speed=2, duration=None)
    
    buggy.forwards(speed=2, duration=None)
    buggy.backwards(speed=2, duration=None)

    buggy.left(speed=2, tightness=2, duration=None)
    buggy.right(speed=2, tightness=2, duration=None)

    buggy.spin_left(speed=2, duration=None)
    buggy.spin_right(speed=2, duration=None)
    

    distance_sensor = BitBotXL.BitBotXLDistanceSensor()
    dist = distance_sensor.distance()

    linesensors = BitBotXL.BitBotXLLineSensor()
    linesensors.linesensor(direction)

    buzzer = BitBotXL.BitBotXLBuzzer()
    buzzer.buzz(duration=500)

    buggyLights = neopixel.NeoPixel(pin13, 12)
    buggyLights[0] = (0, 255, 255)
    buggyLights.show()
    sleep(2000)
    buggyLights.clear()





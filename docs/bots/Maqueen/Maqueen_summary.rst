====================================================
Maqueen summary
====================================================


| A summary of the Maqueen methods is below.
| Speeds values are 0,1,2,3,4,5
| Turn tightness from tighest 5,4,3,2,1 to least tight.
| The line sensor value: over white is 1, while over black is 0.
| Headlights use 1 for on and 0 for off.


.. code-block:: python

    from microbit import *
    import machine
    import utime
    from neopixel import NeoPixel as leds


    buggy = maqueen.MaqueenMotors()
    buggy.stop_left()
    buggy.stop_right()
    buggy.stop()

    buggy.left_motor(speed=1, duration=None)
    buggy.right_motor(speed=1, duration=None)
    
    buggy.forwards(speed=1, duration=None)
    buggy.backwards(speed=1, duration=None)

    buggy.left(tightness=5, duration=None)
    buggy.right(tightness=5, duration=None)

    buggy.spin_left(speed=1, duration=None)
    buggy.spin_right(speed=1, duration=None)
    

    distance_sensor = maqueen.MaqueenDistanceSensor()
    dist = distance_sensor.distance()


    line_sensor = maqueen.MaqueenLineSensors()
    left_reading = line_sensor.line_sensor_read('left')
    right_reading = line_sensor.line_sensor_read('right')


    headlights = maqueen.MaqueenHeadLights()
    headlights.set_headlight(headlight='left', on=1)
    headlights.set_headlights(left=1, right=1)


    lights = maqueen.MaqueenNeoPixels(front=(20, 20, 20), indicator=(35, 25, 0), rear=(20, 0, 0))
    lights.set_front(rgb=(20, 20, 20))
    lights.set_indicator(rgb=(35, 25, 0))
    lights.set_rear(rgb=(20, 0, 0))
    lights.set_led(led_number, rgb=(20, 20, 20))
    lights.set_leds(rgb=(20, 20, 20))
    lights.all_lights()
    lights.front_lights()
    lights.rear_lights()
    lights.left_indicator()    
    lights.right_indicator()
    lights.both_indicators()

    
====================================================
BitBotXL module design
====================================================

This is a tutorial in which a module for the BitBotXL will be written.

| The module will broken into sections based on functionality. 
| Each section of code in the module will be in a class code block with all the relevant functions and methods for that functionality within that class:

* a class for **motors** using pin16, pin8, pin14, pin12
* a class for **ultrasonic sensor** using pin15
* a class for **line sensors** using I2C
* a class for the **LEDS** using pin13
* a class for the **buzzer** using pin0
* a class for **light sensors** using pin1 and pin2


----

| The module will be named ``BitBotXL.py``.
| Code using the module will typically begin with:

.. code-block:: python

    from microbit import *
    import BitBotXL

| Each class will be named systematically, using **BitBotXL** in their names.
| Objects for each class will be created when setting up the BitBotXL.

.. code-block:: python

    from microbit import *
    import BitBotXL
    

    buggy = BitBotXL.BitBotXLMotors()
    distance_sensor = BitBotXL.BitBotXLDistanceSensor()
    line_sensor = BitBotXL.BitBotXLLineSensor()
    leds = BitBotXL.BitBotXLNeoPixels()
    buzzer = BitBotXL.BitBotXLBuzzer()
    light_sensors = BitBotXL.BitBotXLLightSensors()



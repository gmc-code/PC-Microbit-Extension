====================================================
LEDs
====================================================

| The examples below assume a device, such as a buggy, has 4 RGB LEDs (WS2812) on pin8.
| The neopixel module is used to drive these RGB LEDs.
| In RGB, R stands for red, G stands for green, and B stands for blue.
| Each RGB LED can produce a full spectrum of colours independent to all of the other RGB LEDs. 
| Each ZIP LED has a Red, Green and Blue element within the LED, and each of these can have brightness set from 0 to 255.

NeoPixel module
-----------------

| The neopixel module allows use of multiple RGB LEDs connected to one pin so that each can have their own colour and brightness set.
| First, import the neopixel library with ``import neopixel``.

.. code-block:: python

    from microbit import *
    import neopixel

----

Set up LEDs
-------------

.. py:method:: neopixel.NeoPixel(pin, n)

    | Initialise a strip of RGB LEDs 
    | ``pin`` is the pin that they are connected by.
    | ``n`` is the number of LEDs

| The code below sets up 4 LEDs connected to pin8 via: ``lights = neopixel.NeoPixel(pin8, 4)``.
| The variable, lights, is the neopixel object that is used to control the LEDs.

.. code-block:: python

    from microbit import *
    import neopixel


    lights = neopixel.NeoPixel(pin8, 4)

----

Set LED colour and brightness
------------------------------

.. py:method:: lights[n] = (red, green, blue)

    Set the red, green and blue brightness from 0 to 255 for a RGB LED at position n.

| Each LED is set by indexing it (like with a Python list, starting from 0). 
| e.g the LED in position 0 is ``lights[0]``. 
| Neopixels are given RGB (red, green, blue) values between 0-255 as a tuple.
| A value of 0 is off, while 255 is full brightness. 
| When red, green and blue are all full brightness, ``(255, 255, 255)``, the colour is white.


| The code below sets the RGB values to (255, 255, 255) for the LED in position 0.

.. code-block:: python

    from microbit import *
    import neopixel


    lights = neopixel.NeoPixel(pin8, 4)
    lights[0] = (255, 255, 255)

| The code below sets the colours of the 4 LEDs: lights[0] is white, lights[1] is red, lights[2] is green and lights[3] is blue, with all at full brightness.

.. code-block:: python

    from microbit import *
    import neopixel


    lights = neopixel.NeoPixel(pin8, 4)
    lights[0] = (255, 255, 255)
    lights[1] = (255, 0, 0)
    lights[2] = (0, 255, 0)    
    lights[3] = (0, 0, 255)

----

.. admonition:: Tasks

    | For quick RGB values for common colours, see https://www.rapidtables.com/web/color/RGB_Color.html

    #. Write code to set the last LEDS at position 1, 2 and 3 to yellow, cyan and magenta.

----

Show LEDs 
----------

| Setting the colours for LEDs doesn't change the displayed colour of the LEDs until ``show()`` is used on the neopixel object that was set up. e.g. ``lights.show()``

.. py:method:: show()

    Show the LEDs using their colour settings. This must be called for any updates to the LEDs to become visible.

| The code below displays the set colours for the neopixel LEDS using ``lights.show()``

.. code-block:: python

    from microbit import *
    import neopixel


    lights = neopixel.NeoPixel(pin8, 4)
    lights[0] = (255, 255, 255)
    lights.show()


Clear LEDs
------------

.. py:method:: clear()

    Clear all the LEDs so that they have no colours set and turns off the LEDs.

| The code below uses the variable ``lights`` for the neopixel settings.
| The front lights are at position 0 and 1. They are set to dull blue.
| The rear lights are at position 2 and 3. They are set to dull red.
| The lights are turned on for 2 seconds then turned off using ``clear()``.

.. code-block:: python

    from microbit import *
    import neopixel


    lights = NeoPixel(pin8, 4)
    dull_blue = [20, 20, 25]
    dull_red = [25, 0, 0]
    lights[0] = dull_blue
    lights[1] = dull_blue
    lights[2] = dull_red
    lights[3] = dull_red
    lights.show()
    sleep(2000)
    lights.clear()

----

.. admonition:: Tasks

    | For quick RGB values for common colours, see https://www.rapidtables.com/web/color/RGB_Color.html

    #. | Modify the colours used in the code by changing the variable names and their values. | Use yellow and purple instead of red and blue.

----

LED values
-------------------

To read the colour of a specific pixel just reference it.


.. py:method:: lights[n]

    Return the red, green and blue value for the RGB LED at position n.

| The code below sets the LED to a sandy brown colour. 
| The ``for`` loop displays each value in the tuple ``(255, 0, 0)``.

.. code-block:: python

    from microbit import *
    import neopixel


    lights = neopixel.NeoPixel(pin8, 4)
    lights[0] = (255, 0, 0)
    for i in lights[0]:
        display.scroll(i)


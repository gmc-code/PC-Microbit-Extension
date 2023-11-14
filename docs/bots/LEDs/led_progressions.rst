====================================================
led progressions
====================================================

Colour lists
-------------------

| A list of colours can be used to create a colourful display.
| Two for-loops are used, one nested inside the other.
| ``for c in colour_list:`` loops through the colours.
| ``for i in range(4):`` loops through each LED to set the colour for it.
| This example requires a strip of 4 Neopixels (WS2812) connected to pin8.

.. code-block:: python

    from microbit import *
    import neopixel


    white = (255, 255, 255)
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    green = (0, 128, 0)
    cyan = (0, 255, 255)
    blue = (0, 0, 255)
    magenta = (255, 0, 255)

    colour_list = [white, red, yellow, green, cyan, blue, magenta, ]

    lights = neopixel.NeoPixel(pin8, 4)
    for c in colour_list:
        for i in range(4):
            lights[i]=c
        lights.show()
        sleep(200)


----

.. admonition:: Tasks


    See https://www.indezine.com/products/powerpoint/learn/color/color-rgb.html

    #. Modify the code to use a shorter list of colours, with just the primary colours.
    #. Modify the code to use a shorter list of colours, with just the secondary colours.


----

Random brightness
-----------------

| Repeatedly display random colours on the LED strip.
| This example requires a strip of 4 Neopixels (WS2812) connected to pin8.

.. code-block:: python

    from microbit import *
    import neopixel
    from random import randint

    # Setup the Neopixel strip on pin8 with a length of 4 pixels
    lights = neopixel.NeoPixel(pin8, 4)

    while True:
        #Iterate over each LED in the strip

        for pixel_id in range(0, len(lights)):
            red = randint(0, 60)
            green = randint(0, 60)
            blue = randint(0, 60)

            # Assign the current LED a random red, green and blue value between 0 and 60
            lights[pixel_id] = (red, green, blue)

            # Display the current pixel data on the Neopixel strip
            lights.show()
            sleep(100)

----

Random colours
-----------------

| Repeatedly display random colours on the 4 LEDs connected to pin8.

.. code-block:: python

    from microbit import *
    import neopixel
    import random


    # Setup the Neopixel strip on pin8 with a length of 4 pixels
    lights = neopixel.NeoPixel(pin8, 4)

    def same_random_pixels():
        # Iterate over each LED in the strip
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        for pixel_id in range(NUM_PIXELS):
            # Assign the current LED a random red, green and blue value between 0 and 60
            lights[pixel_id] = (red, green, blue)
        # Display the current pixel data on the Neopixel strip
        lights.show()


    while True:
        same_random_pixels()
        sleep(400)

----

Front and rear lights
------------------------------

| Display front and rear lights.

.. code-block:: python

    from microbit import *
    import neopixel
    import random


    # Setup the Neopixel strip on pin8 with a length of 4 pixels
    lights = neopixel.NeoPixel(pin8, 4)

    def front_lights():
        # LED 0 and 1; red, green and blue value between 0 and 255
        lights[0] = (0, 255, 0)
        lights[1] = (0, 255, 0)
        # Display the current pixel data on the Neopixel strip
        lights.show()

    def rear_lights():
        # LED 2 and 3; red, green and blue value between 0 and 255
        lights[2] = (255, 0, 0)
        lights[3] = (255, 0, 0)
        # Display the current pixel data on the Neopixel strip
        lights.show()


    front_lights()
    rear_lights()

----

Button control
------------------------------

| Use def blocks wiht button pressing.

.. code-block:: python

    from microbit import *
    import neopixel
    import random


    # Setup the Neopixel strip on pin8 with a length of 4 pixels
    lights = neopixel.NeoPixel(pin8, 4)

    def same_random_pixels():
        # Iterate over each LED in the strip
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        for pixel_id in range(NUM_PIXELS):
            # Assign the current LED a random red, green and blue value between 0 and 60
            lights[pixel_id] = (red, green, blue)
        # Display the current pixel data on the Neopixel strip
        lights.show()

    def front_lights():
        # LED 0 and 1; red, green and blue value between 0 and 255
        lights[0] = (0, 255, 0)
        lights[1] = (0, 255, 0)
        # Display the current pixel data on the Neopixel strip
        lights.show()

    def rear_lights():
        # LED 2 and 3; red, green and blue value between 0 and 255
        lights[2] = (255, 0, 0)
        lights[3] = (255, 0, 0)
        # Display the current pixel data on the Neopixel strip
        lights.show()

    while True:
        if button_a.is_presssed():
            front_lights()
            rear_lights()
        elif button_b.is_presssed():
            same_random_pixels()
        sleep(400)


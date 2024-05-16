====================================================
LED progressions
====================================================

color lists
-------------------

| A list of colors can be used to create a colorful display.
| Two for-loops are used, one nested inside the other.
| ``for c in color_list:`` loops through the colors.
| ``for i in range(4):`` loops through each LED to set the color for it.
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

    color_list = [white, red, yellow, green, cyan, blue, magenta, ]

    lights = neopixel.NeoPixel(pin8, 4)
    for c in color_list:
        for i in range(4):
            lights[i]=c
        lights.show()
        sleep(200)


----

.. admonition:: Tasks


    See https://www.indezine.com/products/powerpoint/learn/color/color-rgb.html

    #. Modify the code to use a shorter list of colors, with just the primary colors.
    #. Modify the code to use a shorter list of colors, with just the secondary colors.


----

Random brightness
-----------------

| Repeatedly display random colors on the LED strip.
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

Random colors
-----------------

| Repeatedly display random colors on the 4 LEDs connected to pin8.
| This example requires a strip of 4 Neopixels (WS2812) connected to pin8.

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
        for pixel_id in range(4):
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

| Display front lights as green and rear lights as red.
| This example requires a strip of 4 Neopixels (WS2812) connected to pin8.

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

| Use def blocks with button pressing to display random light colors.
| This example requires a strip of 4 Neopixels (WS2812) connected to pin8.

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
        for pixel_id in range(4):
            # Assign the current LED a random red, green and blue value between 0 and 60
            lights[pixel_id] = (red, green, blue)
        # Display the current pixel data on the Neopixel strip
        lights.show()

    def diff_random_pixels():
        # Iterate over each LED in the strip
        for pixel_id in range(4):
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
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
        if button_a.is_pressed():
            diff_random_pixels()
        elif button_b.is_pressed():
            same_random_pixels()
        else:
            front_lights()
            rear_lights()
        sleep(400)

----

color wheel
----------------

| This code is used to create a rainbow color effect on a Neopixel strip. 
| The wheel function generates a color based on an input position, transitioning from red to green to blue and back to red. The rainbow function applies this color effect to each pixel in the Neopixel strip. 
| The color of each pixel is determined by its position in the strip, creating a rainbow effect. 
| The Neopixel strip is then updated to display the new colors.
| This example requires a strip of 12 Neopixels connected to pin13.

.. code-block:: python

    from microbit import *
    import neopixel

    # Setup the Neopixel strip on pin13 with a length of 12 pixels
    np = neopixel.NeoPixel(pin13, 12)

    def wheel(pos):
        """
        Generate color based on the input position, transitioning from red to green to blue and back to red. The rainbow function applies this color effect to each pixel in the Neopixel strip. 

        Parameters:
        pos (int): Position value ranging from 0 to 255.

        Returns:
        tuple: Returns a color value as a tuple (R, G, B).
        """
        # Input a value 0 to 255 to get a color value.
        # The colors are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            return (255,255,255)
        if pos < 85:
            return (255 - pos * 3, pos * 3, 0)
        if pos < 170:
            pos -= 85
            return (0, 255 - pos * 3, pos * 3)
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)

    def rainbow(np):
        """
        Generate a rainbow color effect on the Neopixel strip.

        Parameters:
        np (NeoPixel): The Neopixel strip object.

        Returns:
        None
        """
        # Loop through each pixel in the strip.
        for i in range(len(np)):
            # Calculate the color index for the current pixel.
            rc_index = (i * 256 // len(np)) % 256
            # Set the color of the current pixel.
            np[i] = wheel(rc_index)
        # Update the Neopixel strip to display the colors.
        np.show()

    # Call the rainbow function to display the effect on the Neopixel strip.
    rainbow(np)

----

color wheel with brightness control
---------------------------------------

| This code is used to create a rainbow color effect on a Neopixel strip. 
| The wheel function uses a brightness_factor from 0 to 1 to dim the LEDs.
| This example requires a strip of 12 Neopixels connected to pin13.

.. code-block:: python


    from microbit import *
    import neopixel

    # Setup the Neopixel strip on pin13 with a length of 12 pixels
    np = neopixel.NeoPixel(pin13, 12)

    def wheel(pos, brightness_factor=1):
        """
        Generate color based on the input position and brightness factor.

        Parameters:
        pos (int): Position value ranging from 0 to 255.
        brightness_factor (float): Brightness scaling factor ranging from 0.1 to 1.0.

        Returns:
        tuple: Returns a color value as a tuple (r, g, b).
        """
        # Input a value 0 to 255 to get a color value.
        # The colors are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            return (0, 0, 0)
        if pos < 85:
            return (int((255 - pos * 3) * brightness_factor), int((pos * 3) * brightness_factor), 0)  # scale down the brightness
        if pos < 170:
            pos -= 85
            return (0, int((255 - pos * 3) * brightness_factor), int((pos * 3) * brightness_factor))  # scale down the brightness
        pos -= 170
        return (int((pos * 3) * brightness_factor), 0, int((255 - pos * 3) * brightness_factor))  # scale down the brightness

    def rainbow(np, brightness_factor):
        """
        Generate a rainbow color effect on the Neopixel strip.

        Parameters:
        np (NeoPixel): The Neopixel strip object.

        Returns:
        None
        """
        # Loop through each pixel in the strip.
        for i in range(len(np)):
            # Calculate the color index for the current pixel.
            rc_index = (i * 256 // len(np)) % 256
            # Set the color of the current pixel.
            np[i] = wheel(rc_index, brightness_factor)
        # Update the Neopixel strip to display the colors.
        np.show()

    # Call the rainbow function to display the effect on the Neopixel strip.
    rainbow(np, 0.01)

----

Rainbow cycle
----------------

| This code is used to create a rainbow color effect on a Neopixel strip. 
| The wheel function generates a color based on the input position, and the rainbow_cycle function applies this color to each pixel in the Neopixel strip, creating a beautiful rainbow effect. 
| The effect continuously loops due to the while True loop at the end of the script.
| This example requires a strip of 12 Neopixels connected to pin13.

.. code-block:: python

    from microbit import *
    import neopixel

    # Setup the Neopixel strip on pin13 with a length of 12 pixels
    np = neopixel.NeoPixel(pin13, 12)

    def wheel(pos, brightness_factor=1):
        """
        Generate color based on the input position and brightness factor.

        Parameters:
        pos (int): Position value ranging from 0 to 255.
        brightness_factor (float): Brightness scaling factor ranging from 0.1 to 1.0.

        Returns:
        tuple: Returns a color value as a tuple (r, g, b).
        """
        # Input a value 0 to 255 to get a color value.
        # The colors are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            return (0, 0, 0)
        if pos < 85:
            return (int((255 - pos * 3) * brightness_factor), int((pos * 3) * brightness_factor), 0)  # scale down the brightness
        if pos < 170:
            pos -= 85
            return (0, int((255 - pos * 3) * brightness_factor), int((pos * 3) * brightness_factor))  # scale down the brightness
        pos -= 170
        return (int((pos * 3) * brightness_factor), 0, int((255 - pos * 3) * brightness_factor))  # scale down the brightness

    def rainbow_cycle(np, wait, brightness_factor):
        """
        Create a rainbow cycle effect on the Neopixel strip.

        Parameters:
        np (neopixel.NeoPixel): The Neopixel strip.
        wait (int): The delay time in milliseconds.
        brightness_factor (float): Brightness scaling factor ranging from 0.1 to 1.0.
        """
        for j in range(0, 256, 12):
            for i in range(len(np)):
                rc_index = (i * 256 // len(np) + j) % 255
                np[i] = wheel(rc_index, brightness_factor)
            np.show()
            sleep(wait)

    brightness_factor = 0.5  # Set your desired brightness factor here

    while True:
        # Continuously display the rainbow cycle effect
        rainbow_cycle(np, 100, 0.02)





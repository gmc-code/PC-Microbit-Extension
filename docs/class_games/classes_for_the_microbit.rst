==========================
Classes for the microbit
==========================

| See: https://www.w3schools.com/python/python_classes.asp

| Practical examples of using classes in coding on the microbit are included below.

----

Pixel Classes
-------------------

| The code below blinks a pixel which moves as the microbit is tilted.
| The ``acc_x_change()`` and ``acc_y_change()`` functions return the change in x and y as the microbit is tilted.
| These are passed to the ``move`` method of the BlinkPixel object as in ``mypix.move(acc_x_change(), acc_y_change())``
| The ``move`` method uses ``min`` amd ``max`` to prevent the x or y values going outside the range 0 to 4, as seen in ``self.x_position = min(4, max(0, self.x_position + x_delta))``

.. code-block:: python

    # BlinkPixel class with accelerometer
    from microbit import *


    class BlinkPixel:
        def __init__(self, x_position=2, y_position=2):
            self.x_position = x_position
            self.y_position = y_position

        def move(self, x_delta, y_delta):
            self.x_position = min(4, max(0, self.x_position + x_delta))
            self.y_position = min(4, max(0, self.y_position + y_delta))

        def blink(self):
            display.set_pixel(self.x_position, self.y_position, 5)
            sleep(50)
            display.set_pixel(self.x_position, self.y_position, 2)

    def acc_x_change():
        sensitivity = 100
        accx = accelerometer.get_x()
        if accx < -sensitivity:
            xd = -1
        elif accx > sensitivity:
            xd = 1
        else:
            xd = 0
        return xd

    def acc_y_change():
        sensitivity = 300
        accy = accelerometer.get_y()
        if accy < sensitivity:
            yd = -1
        elif accy > sensitivity:
            yd = 1
        else:
            yd = 0
        return yd

    # Create an instance of a BlinkPixel object
    mypix = BlinkPixel()

    mypix.blink()
    while True:
        mypix.move(acc_x_change(), acc_y_change())
        mypix.blink()
        sleep(200)

----

.. admonition:: Tasks

    #. Modify the code above to allow a button press to clear the display.
    #. Modify the code above to just show the current pixel position and leave a trail.

----

Pixel animation using classes
--------------------------------

| The Class ``Pixel`` is used to create several Pixel objects used in the animation.
| The definitions within the class allows easy use of methods to control the microbit LED brightness. 

.. code-block:: python

    # Pixel class with animation
    from microbit import *


    class Pixel():
        def __init__(self, x=2, y=2):
            self.x = x
            self.y = y

        def intensity(self, brightness=9):
            display.set_pixel(self.x, self.y, brightness)

        def on(self, brightness=9):
            display.set_pixel(self.x, self.y, brightness)

        def off(self):
            display.set_pixel(self.x, self.y, 0)

    pixel0 = Pixel(0, 2)
    pixel1 = Pixel(1, 2)
    pixel2 = Pixel(2, 2)
    pixel3 = Pixel(3, 2)
    pixel4 = Pixel(4, 2)

    pixel2.on()
    sleep(500)
    pixel2.off()
    sleep(500)

    pixel_list = [pixel0, pixel1, pixel2, pixel3, pixel4]
    pixel_list_rev = pixel_list.copy()
    pixel_list_rev.reverse()

    while True:
        for i in range(1, 10, 2):
            for pixelxy in pixel_list:
                pixelxy.intensity(i)
                sleep(40)
                pixelxy.off()
                sleep(10)
            for pixelxy in pixel_list_rev:
                pixelxy.intensity(i)
                sleep(40)
                pixelxy.off()
                sleep(10)
        for i in range(7, 0, -2):
            for pixelxy in pixel_list:
                pixelxy.intensity(i)
                sleep(40)
                pixelxy.off()
                sleep(10)
            for pixelxy in pixel_list_rev:
                pixelxy.intensity(i)
                sleep(40)
                pixelxy.off()
                sleep(10)

----

.. admonition:: Tasks

    #. Modify the code so that after the brightness increases from 1 to 9, it decreases smoothly back down to 1 before repeating.
    #. Modify the code to use the middle column instead of the middle row.

----

Potentiometer Classes
----------------------------

| A potentiometer can be connected to a microbit using a breadboard.
| Create a class for the Potentiometer to make it easy to get its analog reading, 
keep track of the last reading, be able to tell if it has changed and to convert the reading to a particular range like 0 to 10.
| The code below first checks to see if the value of the potentiometer has changed, 
and then if it has, displays the value as a scaled value in the range 0 to 10.
| The ``Potentiometer()`` class will use the default pin: ``pin0``.
| This is coded via: ``def __init__(self, io_pin=pin0)``


.. code-block:: python

    # potentiometer using class
    from microbit import *


    class Potentiometer:
        def __init__(self, io_pin=pin0):
            self.io_pin = io_pin
            self.last_val = -1

        def get_val(self):
            return self.io_pin.read_analog()

        def was_changed(self):
            curr_val = self.get_val()
            if self.last_val != curr_val:
                self.last_val = curr_val
                return True
            else:
                return False

        def get_range(self, rng):
            analog_read = self.get_val()
            scaled = rng * (analog_read / 1023)
            return int(scaled)

    # this defaults to pin0
    # to use pinl1 instead use pot = Potentiometer(pin1)
    pot = Potentiometer()
    while True:
        if pot.was_changed():
            display.show(pot.get_range(10))


----

.. admonition:: Tasks

    #. Modify the code so there is a short sleep between potentiometer readings.
    #. Modify the code so that the potentiometer only displays values from 0 to 5.


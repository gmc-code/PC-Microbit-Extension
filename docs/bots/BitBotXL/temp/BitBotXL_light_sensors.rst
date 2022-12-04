====================================================
BitBotXL light sensors
====================================================

Using the buzzer
------------------------------

| The buzzer is connected to pin0.
| Turn it on using: ``pin0.write_digital(1)``.
| Turn it off using: ``pin0.write_digital(0)``.

To turn on the buzzer for a specific time, put in a sleep between turning it on and turning it off. The code below has a sleep of 1000ms, so that the buzzer is on for 1 sec.

.. code-block:: python

    from microbit import *

    pin0.write_digital(1)
    sleep(1000)
    pin0.write_digital(0)

----

.. admonition:: Tasks

    #. Write code to turn on the buzzer for half a second.
    #. Write code, using a for loop, to make 3 half second buzzer sounds with 1 second between each of them.

----   

Refactoring into a class
------------------------------

| The class, ``class BitBotXLBuzzer()``, is used to group the code related to the buzzer.
| The code to drive the buzzer is placed in a function, ``buzz``.
| The function will have a parameter, ``duration``,  which sets the duration of the buzzer.
| This should also simplify the buzzer use. e.g. ``buzz(1000)``.

| Firstly, the code above is placed inside a function.
| The sleep value is replaced with the ``duration`` variable.
| The ``duration`` parameter is added to the definition line: ``def buzz(duration):``.
| The ``self`` parameter must be included first for a regular method in a class.
| Instead of ``def buzz(duration):``, ``def buzz(self, duration):`` is required.

.. code-block:: python

    class BitBotXLBuzzer():

        def buzz(self, duration):
            """Sound a buzz for duration milliseconds."""
            pin0.write_digital(1)
            sleep(duration)
            pin0.write_digital(0)


----

Using the class
----------------------------------------

.. py:class:: BitBotXLBuzzer() 

    | Set up the buggy's buzzer for use.
    | Use ``buzzer = BitBotXL.BitBotXLBuzzer()`` to use the buggy's buzzer.

| The code below imports the BitBotXL module and sets up the buzzer.

.. code-block:: python

    from microbit import *
    import BitBotXL


    # setup the buzzer
    buzzer = BitBotXL.BitBotXLBuzzer()


----

Using the buzz method
----------------------------------------

.. py:method:: buzz(duration)

    Activates the buzzer for the specified duration in milliseconds.


| The code below, uses ``buzzer.buzz(duration)`` to make a buzz.

.. code-block:: python

    from microbit import *
    import BitBotXL


    # setup the buzzer
    buzzer = BitBotXL.BitBotXLBuzzer()

    buzzer.buzz(1000)


----

.. admonition:: Tasks

    #. Write code using a while True loop to make a 500ms buzz every 2 seconds.
    #. Write code using a for loop to make buzz sounds of 100, 200, 300 and 400ms separated by a 500ms sleep.


'''
    28 0x1c
    r	114	01110010
    s	115	01110011

    x << y
    Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros).
    This is the same as multiplying x by 2**y.

    x & y
    Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.

        value_left = i2c.read(__I2CADDR1, 1)[0]
        value_right = i2c.read(__I2CADDR2, 1)[1]
        print(value1, value2)  # , (value0 & 2), (value0 & 1))
        # print(1 << 1, 1 << 0)  #, 2, 1
        sleep(1000

'''

def getLine(bitval):
    mask = 1 << bitval
    value = 0
    try:
        print(i2c.read(I2CADDR, 1))
        if bitval == 0:
            value = i2c.read(I2CADDR, 1)[0]
            print(0, value, mask, (value & mask))
        elif bitval == 1:
            value = i2c.read(I2CADDR, 2)[1]
            print(1, value, mask, (value & mask))
    except OSError:
        pass
    if (value & mask) > 0:
        return 1
    else:
        return 0
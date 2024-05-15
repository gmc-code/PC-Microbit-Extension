====================================================
Maqueen line sensors
====================================================

Set up the line sensors
----------------------------------------

.. py:class:: MaqueenLineSensors() 

    | Set up the buggy's line sensors for use.
    | Use ``line_sensor = maqueen.MaqueenLineSensors()`` to use the buggy's line sensors.

| The code below imports the maqueen module and sets up the line sensors.

.. code-block:: python

    from microbit import *
    import maqueen


    # set up line sensor
    line_sensor = maqueen.MaqueenLineSensors()

----

Read values from the line sensors
----------------------------------------

.. py:method:: line_sensor_read(sensor)

    | Return the line sensor value.
    | The value over white is 1, while over black is 0, since it uses a digital read (not analog).
    | ``sensor`` is 'left' or 'right'

.. code-block:: python

    from microbit import *
    import maqueen


    # set up line sensor
    line_sensor = maqueen.MaqueenLineSensors()
    
    left_reading = line_sensor.line_sensor_read('left')
    display.scroll(left_reading)

----

.. admonition:: Tasks

    #. Write code to read the right line sensor and display its value.
    #. Write code to read both the left and the right line sensor and display their values with 'L' before the left reading and 'R' before the right reading.


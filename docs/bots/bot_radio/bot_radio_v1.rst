====================================================
Bot radio v1
====================================================

| This is a simple starter approach for using the radio to steer the bots.

----

Unique groups
----------------------

| Use ``radio.config(group=8)`` to set unique groups in the room.
| Make sure all microbits using a bot have the same group number (0-255).
| Edit the code below to set the group.
| The buggy **speeds** and **durations** can also be edited for different responses.

----

Radio for controller
----------------------

| The code below gives messages based on forwards - backwards tilting and sideways tilting.
| The code displays the message on the microbit for testing purposes.
| For the forwards and backwards tilting, make sure not to tilt the microbit sideways.
| If the microbit is level, ``-200 <= y_reading <= 200 and -200 <= x_reading <= 200`` send an "X", to stop.

.. code-block:: python

    from microbit import *
    import radio


    radio.config(group=8)  # 0-255
    radio.on()

    while True:
        y_reading = accelerometer.get_y()
        x_reading = accelerometer.get_x()
        # flat
        if -200 <= y_reading <= 200 and -200 <= x_reading <= 200:
            msg = "X"
        # level sideways
        elif -200 <= x_reading <= 200:
            # forwards and back tilting
            if y_reading > 200:
                msg = "B"
            elif y_reading < -200:
                msg = "F"
            else:
                msg = "X"
        else:
            # sideways tilting
            if x_reading > 200:
                msg = "R"
            elif x_reading < -200:
                msg = "L"
            else:
                msg = "X"      
        radio.send(msg)
        display.show(msg)

----

Radio for microbit on MiniBit
--------------------------------------

| The code below moves the MiniBit at maximum speed, since its top speed is relatively slow.
| The tightness of 5 gives a tight turn.

.. code-block:: python

    import MiniBit


    radio.config(group=8)  # 0-255
    radio.on()

    buggy = MiniBit.MiniBitMotors()

    while True:
        sleep(50)
        msg = radio.receive()
        if msg is not None:
            display.show(msg)
            if msg == "X":
                buggy.stop()
            elif msg == "B":
                buggy.backwards(speed=10)
            elif msg == "F":
                buggy.forwards(speed=10)
            elif msg == "R":
                buggy.right(speed=10, tightness=5)
            elif msg == "L":
                buggy.left(speed=10, tightness=5)

----

Radio for microbit on BitBotXL
--------------------------------------

| The code below moves the BitBotXL at maximum speed, since its top speed is relatively slow.
| The tightness of 5 gives a tight turn.

.. code-block:: python


    from microbit import *
    import radio
    import BitBotXL


    radio.config(group=8)  # 0-255
    radio.on()
    
    buggy = BitBotXL.BitBotXLMotors()
    

    while True:
        msg = radio.receive()
        if msg is not None:
            display.show(msg)
            if msg == "X":
                buggy.stop()
            elif msg == "B":
                buggy.backwards(speed=10)
            elif msg == "F":
                buggy.forwards(speed=10)
            elif msg == "R":
                buggy.right(speed=10, tightness=5)
            elif msg == "L":
                buggy.left(speed=10, tightness=5)

----

Radio for microbit on MOVEMotor
--------------------------------

| The code below moves the MOVEMotor at medium speed, since its top speed is relatively fast.
| The radius of 5 gives a tight turn.


.. code-block:: python

    from microbit import *
    import radio
    import MOVEMotor


    radio.config(group=8)  # 0-255
    radio.on()

    buggy = MOVEMotor.MOVEMotorMotors()


    while True:
        sleep(100)
        msg = radio.receive()
        if msg is not None:
            display.show(msg)
            if msg == "X":
                buggy.stop()
            elif msg == "B":
                buggy.backwards(speed=5)
            elif msg == "F":
                buggy.forwards(speed=5)
            elif msg == "R":
                buggy.right(speed=2, radius=5)
            elif msg == "L":
                buggy.left(speed=2, radius=5)

----

Radio Racing
----------------------------

.. admonition:: Tasks

    #. Create an obstacle course and race another bot using radio controls.
    #. Modify the speed settings to suit the obstacle course.
    #. Add a variable to keep track of the last msg sent and only send a new msg if it is different to the last msg.



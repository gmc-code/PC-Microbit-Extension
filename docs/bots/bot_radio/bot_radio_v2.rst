====================================================
Bot radio v2
====================================================

| This uses more settings for the motor control by tilting to different degrees.
| Three speed settings are used below.

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

| If the microbit is level, ``-200 <= y_reading <= 200 and -200 <= x_reading <= 200``, send an "X", to stop.

| For increasing speed forward, send: F, G, H. 
| Tilt forwards a bit, F is sent, and a slow speed results.
| Tilt forwards a bit more, G is sent, and a medium speed results.
| Tilt forwards a lot, H is sent, and a fast speed results.

| For increasing speed backward, send: B, C, D
| Tilt backwards more and more.

| For increasing tightness of turn left, send: L, M, N
| Tilt left more and more.

| For increasing tightness of turn right, send: R, S, T
| Tilt right more and more.

| To force a stop, hold down the A button.
| To force a short spin to left, hold down the B button.


.. code-block:: python

    from microbit import *
    import radio

    radio.config(group=8)  # 0-255
    radio.on()


    while True:
        sleep(50)
        if button_a.is_pressed():
            # stop
            msg = "X"
        elif button_b.is_pressed():
            # spin left
            msg = "W"
        else:
            y_reading = accelerometer.get_y()
            x_reading = accelerometer.get_x()
            # level sideways only
            if -200 <= y_reading <= 200 and -200 <= x_reading <= 200:
                msg = "X"
            # level sideways only
            elif -200 <= x_reading <= 200:
                if y_reading > 700:
                    msg = "D"
                elif y_reading > 500:
                    msg = "C"
                elif y_reading > 200:
                    msg = "B"
                elif y_reading < -700:
                    msg = "H"
                elif y_reading < -500:
                    msg = "G"
                elif y_reading < -200:
                    msg = "F"
            else:
                if x_reading > 700:
                    msg = "T"
                elif x_reading > 500:
                    msg = "S"
                elif x_reading > 200:
                    msg = "R"
                elif x_reading < -700:
                    msg = "N"
                elif x_reading < -500:
                    msg = "M"
                elif x_reading < -200:
                    msg = "L"
        radio.send(msg)
        display.show(msg)

----

Radio for microbit on MiniBit
--------------------------------------

| The code below moves the MiniBit at maximum speed, since its top speed is relatively slow.
| The tightness of 5 gives a tight turn.
| High turning speed settings are used below for best control based on testing.

.. code-block:: python

    from microbit import *
    import radio
    import MiniBit

    radio.config(group=8)  # 0-255
    radio.on()

    buggy = MiniBit.MiniBitMotors()

    while True:
        sleep(50)
        msg = radio.receive()
        if msg is not None:
            display.show(msg)
            if msg == "B":
                buggy.backwards(speed=5)
            elif msg == "C":
                buggy.backwards(speed=8)
            elif msg == "D":
                buggy.backwards(speed=10)
            elif msg == "F":
                buggy.forwards(speed=5)
            elif msg == "G":
                buggy.forwards(speed=8)
            elif msg == "H":
                buggy.forwards(speed=10)
            elif msg == "X":
                buggy.stop()
            elif msg == "L":
                buggy.left(speed=10, tightness=2)
            elif msg == "M":
                buggy.left(speed=10, tightness=3)
            elif msg == "N":
                buggy.left(speed=10, tightness=5)
            elif msg == "R":
                buggy.right(speed=10, tightness=2)
            elif msg == "S":
                buggy.right(speed=10, tightness=3)
            elif msg == "T":
                buggy.right(speed=10, tightness=5)
            elif msg == "W":
                buggy.spin_left(speed=1) 

----

Radio for microbit on BitBotXL
--------------------------------------

| The code below moves the BitBotXL at maximum speed, since its top speed is relatively slow.
| The tightness of 5 gives a tight turn.
| High turning speed settings are used below for best control based on testing.

.. code-block:: python

    from microbit import *
    import radio
    import BitBotXL


    radio.config(group=8)  # 0-255
    radio.on()

    buggy = BitBotXL.BitBotXLMotors()


    while True:
        sleep(50)
        msg = radio.receive()
        if msg is not None:
            display.show(msg)
            if msg == "B":
                buggy.backwards(speed=5)
            elif msg == "C":
                buggy.backwards(speed=8)
            elif msg == "D":
                buggy.backwards(speed=10)
            elif msg == "F":
                buggy.forwards(speed=5)
            elif msg == "G":
                buggy.forwards(speed=8)
            elif msg == "H":
                buggy.forwards(speed=10)
            elif msg == "X":
                buggy.stop()
            elif msg == "L":
                buggy.left(speed=10, tightness=2)
            elif msg == "M":
                buggy.left(speed=10, tightness=3)
            elif msg == "N":
                buggy.left(speed=10, tightness=5)
            elif msg == "R":
                buggy.right(speed=10, tightness=2)
            elif msg == "S":
                buggy.right(speed=10, tightness=3)
            elif msg == "T":
                buggy.right(speed=10, tightness=5)
            elif msg == "W":
                buggy.spin_left(speed=1) 

----

Radio for microbit on MOVEMotor
--------------------------------

| The code below moves the MOVEMotor at varying speed.
| The radius of 5 gives a tight turn.


.. code-block:: python

    from microbit import *
    import radio
    import MOVEMotor

    radio.config(group=8)  # 0-255
    radio.on()

    buggy = MOVEMotor.MOVEMotorMotors()

    while True:
        sleep(50)
        msg = radio.receive()
        if msg is not None:
            display.show(msg)
            if msg == "B":
                buggy.backwards(speed=5)
            elif msg == "C":
                buggy.backwards(speed=8)
            elif msg == "D":
                buggy.backwards(speed=10)
            elif msg == "F":
                buggy.forwards(speed=5)
            elif msg == "G":
                buggy.forwards(speed=8)
            elif msg == "H":
                buggy.forwards(speed=10)
            elif msg == "X":
                buggy.stop()
            elif msg == "L":
                buggy.left(speed=5, radius=100)
            elif msg == "M":
                buggy.left(speed=3, radius=50)
            elif msg == "N":
                buggy.left(speed=1, radius=5)
            elif msg == "R":
                buggy.right(speed=5, radius=100)
            elif msg == "S":
                buggy.right(speed=3, radius=50)
            elif msg == "T":
                buggy.right(speed=1, radius=5)
            elif msg == "W":
                buggy.spin_left(speed=1) 

----

Radio for microbit on Maqueen
--------------------------------------

| The code below moves the Maqueen.

.. code-block:: python

    from microbit import *
    import radio
    import maqueen


    radio.config(group=8)  # 0-255
    radio.on()

    buggy = maqueen.MaqueenMotors()

 
    while True:
        sleep(50)
        msg = radio.receive()
        if msg is not None:
            display.show(msg)
            if msg == "B":
                buggy.backwards(speed=1)
            elif msg == "C":
                buggy.backwards(speed=3)
            elif msg == "D":
                buggy.backwards(speed=5)
            elif msg == "F":
                buggy.forwards(speed=1)
            elif msg == "G":
                buggy.forwards(speed=3)
            elif msg == "H":
                buggy.forwards(speed=5)
            elif msg == "X":
                buggy.stop()
            elif msg == "L":
                buggy.left(tightness=1)
            elif msg == "M":
                buggy.left(tightness=3)
            elif msg == "N":
                buggy.left(tightness=5)
            elif msg == "R":
                buggy.right(tightness=1)
            elif msg == "S":
                buggy.right(tightness=3)
            elif msg == "T":
                buggy.right(tightness=5)
            elif msg == "W":
                buggy.spin_left(speed=1)             

----

Radio Racing
----------------------------

.. admonition:: Tasks

    #. Create an obstacle course and race another bot using radio controls.
    #. Modify the speed settings to suit the obstacle course.
    #. Nodify the B button pressing to allow backwards movement while turning.
    #. Add a variable to keep track of the last msg sent and only send a new msg if it is different to the last msg.




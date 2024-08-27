====================================================
Bot radio v4 - KitronikGameController
====================================================

Unique groups
----------------------

| Change the group number in ``radio.config(group=8)`` to set unique groups in the room.
| Make sure all microbits using a bot have the same group number (0-255).
| Edit the code below to set the group.
|  
| # MOVEMotor bot code, change radio group to match bot number
| # MOVEMotor_v31 200 + bot number
| # MOVEMotor v2 150 + bot number

----

MOVEMotor v3.1 radio v4 files:
-----------------------------------

| Hex Files for the MOVEMotor v3.1 can be loaded via the project:open button at: https://python.microbit.org/v/3
| Hex file for the bot :download:`MOVEMotor bot_v3 hex file <files/MM_bot_v3.hex>`.
| Hex file for the hand held controller  :download:`MOVEMotor controller_v4 hex file <files/MM_radio_controller_v4.hex>`.

----

Using Kitronik Game Controller for variable speeds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Radio for controller
----------------------


| The code below requires button pressing for motor control.
| No durations are set, so the motors will continue running with the last instruction they receive.

| To spin, press the microbit A or B button.
| Use this instead of stopping, since there is no code to send an "X".

| For increasing speed forward, send: F, G, H. 
| Press the joypad UP button, F is sent, and a slow speed results.
| Hold down the FIRE SW 1 button, and press the joypad UP button, G is sent, and a medium speed results.
|  Hold down the FIRE SW 2 button, and press the joypad UP button, H is sent, and a fast speed results.

| For increasing speed backward, send: B, C, D
| Press the joypad DOWN button.

| For increasing speed left, send: L, M, N
| Press the joypad LEFT button.

| For increasing speed right, send: R, S, T
| Press the joypad LEFT button.


.. code-block:: python

    # MoverMotor bot code, change radio group to match bot number in 200s
    # MOVEMotor_v31  200 + number
    # MM v2 150 + number

    from microbit import *
    import music
    import radio

    radio.config(group=151)  # 0-255
    radio.on()


    # Class to drive Kitronik :GAME Controller
    class KitronikGameController:

        # This function will be called when a class instance is created
        def __init__(self):
            self.musicPin = pin2
            self.Up = pin8
            self.Down = pin14
            self.Left = pin12
            self.Right = pin13
            self.Fire_1 = pin15
            self.Fire_2 = pin16

        # Determines whether a particular button has been pressed
        #  (returns True or False)
        def onButtonPress(self, button):
            if button.read_digital() == 0:
                return True
            else:
                return False

    controller = KitronikGameController()
    msg=""

    while True:
        msg=""

        if button_a.is_pressed():
            # spin
            msg = "sL"
        elif button_b.is_pressed():
            # spin
            msg = "sR"
        elif controller.onButtonPress(controller.Fire_2) is True:
            if controller.onButtonPress(controller.Up) is True:
                msg = "H"
            elif controller.onButtonPress(controller.Down) is True:
                msg = "D"
            elif controller.onButtonPress(controller.Left) is True:
                msg = "N"
            elif controller.onButtonPress(controller.Right) is True:
                msg = "T"
        elif controller.onButtonPress(controller.Fire_1) is True:
            if controller.onButtonPress(controller.Up) is True:
                msg = "G"
            elif controller.onButtonPress(controller.Down) is True:
                msg = "C"
            elif controller.onButtonPress(controller.Left) is True:
                msg = "M"
            elif controller.onButtonPress(controller.Right) is True:
                msg = "S"
        else:
            if controller.onButtonPress(controller.Up) is True:
                msg = "F"
            elif controller.onButtonPress(controller.Down) is True:
                msg = "B"
            elif controller.onButtonPress(controller.Left) is True:
                msg = "L"
            elif controller.onButtonPress(controller.Right) is True:
                msg = "R"
        radio.send(msg)
        display.show(msg)



----

Radio for microbit on MOVEMotor
---------------------------------

| There are 3 speed settings.
| When turning, the slowest speed has a tighter turn; the fastest speed has a less tight turning circle.


.. code-block:: python

    from microbit import *
    import radio
    import MOVEMotor


    radio.config(group=8)  # 0-255
    radio.on()

    # setup buggy
    buggy = MOVEMotor.MOVEMotorMotors()

            
    while True:
        msg = radio.receive()
        if msg is not None:
            if msg == "B":
                buggy.backwards(speed=2)
            elif msg == "C":
                buggy.forwards(speed=5)
            elif msg == "D":
                buggy.forwards(speed=10)
            elif msg == "F":
                buggy.forwards(speed=2)
            elif msg == "G":
                buggy.forwards(speed=5)
            elif msg == "H":
                buggy.forwards(speed=10)
            elif msg == "X":
                buggy.stop()
            elif msg == "L":
                buggy.left(speed=2, radius=25)
            elif msg == "M":
                buggy.left(speed=3, radius=15)
            elif msg == "N":
                buggy.left(speed=4, radius=5)
            elif msg == "R":
                buggy.right(speed=2, radius=25)
            elif msg == "S":
                buggy.right(speed=3, radius=15)
            elif msg == "T":
                buggy.right(speed=4, radius=5)


----

Turning backwards
----------------------------

.. admonition:: Tasks

    #. Add B button pressing to allow backwards movement while turning.


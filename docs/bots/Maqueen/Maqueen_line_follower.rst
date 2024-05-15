====================================================
Maqueen line follower
====================================================

| The maqueen buggy is best suited to following a thick track.

Set up buggy and sensors
----------------------------------------

| Import the maqueen module and set up the buggy and line sensor.

.. code-block:: python

    from microbit import *
    import maqueen


    buggy = maqueen.MaqueenMotors()
    buggy.stop()
    line_sensor = maqueen.MaqueenLineSensors()

Set constants
----------------------------------------

| Set constants to be used in line following.

.. code-block:: python

    MAXSPEED = 3
    MINTURN = 0
    MAXTURN = 3
    MOTORTIME = 20
    SPINTIME = 530


Thick line following
----------------------------------------

| Define ``follow_thick_line`` to follow a thick black line and use it in a ``while True`` loop.

.. code-block:: python

    from microbit import *
    import music
    import maqueen


    buggy = maqueen.MaqueenMotors()
    buggy.stop()
    line_sensor = maqueen.MaqueenLineSensors()

    MAXSPEED = 3
    MINTURN = 0
    MAXTURN = 3
    MOTORTIME = 20

    def follow_thick_line(drive_time=20):
        # stay on black track; turn away from white
        left_sensor = line_sensor.line_sensor_read('left')
        right_sensor = line_sensor.line_sensor_read('right')
        black_left = (left_sensor == 0)
        black_right = (right_sensor == 0)
        if not(black_left) and not(black_right):
            buggy.left_motor(-MAXTURN)
            buggy.right_motor(-MAXTURN)
        elif black_left and not(black_right):
            buggy.left_motor(MINTURN)
            buggy.right_motor(MAXTURN)
        elif black_right and not(black_left):
            buggy.left_motor(MAXTURN)
            buggy.right_motor(MINTURN)
        else:
            buggy.left_motor(MAXSPEED)
            buggy.right_motor(MAXSPEED)
        sleep(drive_time)

    while True:
        follow_thick_line(MOTORTIME)
        buggy.stop()
        sleep(10)

----

.. admonition:: Tasks

    #. Add headlights and LEDs.
    #. Add obstacle avoidance using the distance sensor so that the buggy spins if an object is on the track. 



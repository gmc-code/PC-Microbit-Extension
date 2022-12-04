====================================================
Maqueen motors
====================================================


Set up the buggy
----------------------------------------

.. py:class:: MaqueenMotors() 

    | Set up the buggy's motors for use.
    | Use ``buggy = maqueen.MaqueenMotors()`` to use the motor on the buggy.

| The code below imports the maqueen module and sets up the motors.

.. code-block:: python

    from microbit import *
    import maqueen


    # setup buggy
    buggy = maqueen.MaqueenMotors()

----

Duration parameter
----------------------------------------

| The Buggy methods that drive the motors have a duration parameter. 
| The duration parameter specifies how long the motor runs for.
| The default duration is ``None``. If the duration is ``None`` or is not specified the motor will run continuously until another command is sent to it.
| e.g. using the duration parameter: ``buggy.forwards(1, duration=5000)``  the buggy stops after 5 sec.
| e.g. not using the duration parameter: ``buggy.forwards(1)`` the buggy runs forwards continuously.

----

Independent motor control
----------------------------------------

| The left and right motors can be controlled independently using the four methods below:
| ``left_motor(speed=1, duration=None)`` runs the left motor.
| ``right_motor(speed=1, duration=None)`` runs the right motor.
| ``stop_left()`` stops the left motor.
| ``stop_right()`` stops the right motor.

----

left_motor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: left_motor(speed=1, duration=None)

    | Make the left motor run. 
    | ``speed`` values are **integers** from -5 to 5.
    | Default ``speed`` is 1.
    | If speed < 0 the motor turns the wheel backwards.
    | ``duration`` values are **integers** above 0.
    | Default ``duration`` is None.
    | The motor will stop after a given duration in milliseconds.
    | If the duration is None, the motor runs without stopping.

| ``left_motor()`` and ``left_motor(1)`` and ``left_motor(speed=1)`` all set the speed to 1.
| ``left_motor(2, 3000)`` and ``left_motor(2, duration=3000)`` and ``left_motor(speed=2, duration=3000)`` all run the left motor at speed 2 for 3 sec.

| The code below, using ``left_motor(5)``,  runs the left motor at full speed.

.. code-block:: python

    from microbit import *
    import maqueen


    # setup buggy
    buggy = maqueen.MaqueenMotors()

    buggy.left_motor(5)

| The code below, using ``left_motor(2, 5000)``,  runs the left motor at speed 2 for 5 sec.

.. code-block:: python

    from microbit import *
    import maqueen


    # setup buggy
    buggy = maqueen.MaqueenMotors()

    buggy.left_motor(2, 5000)

----

right_motor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: right_motor(speed=1, duration=None)

    | Make the left motor run. 
    | ``speed`` values are **integers** from -5 to 5.
    | Default ``speed`` is 1.
    | If speed < 0 the motor turns the wheel backwards.
    | ``duration`` values are **integers** above 0.
    | Default ``duration`` is None.
    | The motor will stop after a given duration in milliseconds.
    | If the duration is None, the motor runs without stopping.

| ``right_motor()`` and ``right_motor(1)`` and ``right_motor(speed=1)`` all set the speed to 1.
| ``right_motor(2, 4000)`` and ``right_motor(2, duration=4000)`` and ``right_motor(speed=2, duration=4000)`` all run the right motor at speed 2 for 4sec.

| The code below, using ``right_motor(speed=4, duration=3000)``, runs the right motor at speed 4 for 3 sec.

.. code-block:: python

    from microbit import *
    import maqueen


    # setup buggy
    buggy = maqueen.MaqueenMotors()

    buggy.right_motor(speed=4, duration=3000)

| The code below, using ``right_motor(-5)``, runs the right motor backwards at full speed.

.. code-block:: python

    from microbit import *
    import maqueen


    # setup buggy
    buggy = maqueen.MaqueenMotors()

    buggy.right_motor(-5)


----

stop_left
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: stop_left()

    | Stop the left motor.


| The code below runs the left motor continuously during the sleep of 2 sec then stops it.

.. code-block:: python

    from microbit import *
    import maqueen


    # setup buggy
    buggy = maqueen.MaqueenMotors()

    buggy.left_motor()
    sleep(2000)
    buggy.stop_left()


----

stop_right
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: stop_right()

    | Stop the right motor.


| The code below runs the right motor continuously during the sleep then stops it.

.. code-block:: python

    from microbit import *
    import maqueen


    # setup buggy
    buggy = maqueen.MaqueenMotors()

    buggy.right_motor(4)
    sleep(2000)
    buggy.stop_right()

----

Stop both motors
----------------------------------------

.. py:method:: stop()

    | Stop both motors.


| The code below runs the left motor at speed 5 and the right motor at speed 2, then after 1500ms stops them both.

.. code-block:: python

    from microbit import *
    import maqueen


    # setup buggy
    buggy = maqueen.MaqueenMotors()
    
    buggy.left_motor(5)
    buggy.right_motor(2)
    sleep(1500)
    buggy.stop()


----

.. admonition:: Tasks

    #. Write code to drive the left motor at speed 2 for 1 second, stop it, run the right motor at speed 2 for 1 sec then stop it.
    #. Write code to drive the right motor at speed 3 while the left motor runs at speed 2 for 3 sec then stop it.
    #. Write code to drive the left motor at speed 3 while the right motor runs at speed 2 for 3 sec then stop it.
    #. Write code that drives the left side faster than the right side then the right side faster the left side so that it zig zags for 5 sec then stop it.
    #. Write code so that the buggy repetitively zig zags forwards for 5 zigs and zags then forwards forwards for 5 zigs and zags.
    #. Modify the zig zag code so that it uses variables for the 2 motor speeds, the number of zig zags forwards and backward, and the time for each zig and zag.

----

forwards and backwards
----------------------------------------

| The left and right motors can be run so that the buggy moves forwards or backwards in a straight line:
| ``forwards(speed=1, duration=None)``
| ``backwards(speed=1, duration=None)``

forwards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: forwards(speed=1, duration=None)

    | Drive the buggy forward.
    | ``speed`` values are integers from 0 to 5.
    | Default ``speed`` is 1.
    | ``duration`` values are integers above 0.
    | Default ``duration`` is None.
    | The motor will stop after a given duration in milliseconds.


| The code below, drives the buggy forwards at speed 5 for 4 secs.

.. code-block:: python

    from microbit import *
    import maqueen


    # setup buggy
    buggy = maqueen.MaqueenMotors()

    buggy.forwards(speed=5, duration=4000)


----

backwards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: backwards(speed=1, duration=None)

    | Drive the buggy backwards.
    | ``speed`` values are integers from 0 to 5.
    | Default ``speed`` is 1.
    | ``duration`` values are integers above 0.
    | Default ``duration`` is None.
    | The motor will stop after a given duration in milliseconds.
    | If the duration is None, the motor runs without stopping.

| The code below drives the buggy backwards at speed 5 for 3 secs.

.. code-block:: python

    from microbit import *
    import maqueen


    # setup buggy
    buggy = maqueen.MaqueenMotors()

    buggy.backwards(5, 3000)


----

.. admonition:: Tasks

    #. Write code to drive the buggy forwards at speed 3 for 3 seconds.
    #. Write code to drive the buggy backwards at speed 1 for 2 seconds.
    #. Write code to drive the buggy forwards at speed 1 for 3 seconds then backwards at speed 1 for 3 seconds.

----

Turning
----------------------------------------

| The left and right motors are adjusted to turn the buggy with a given turn tightness:
| ``left(tightness=5, duration=None)``
| ``right(tightness=5, duration=None)``
| When turning left, the left wheel is slowed based on the tightness value.
| When turning right, the right wheel is slowed based on the tightness value.
| The turning tightness is greatest with a value of 5.

----

left
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: left(tightness=5, duration=None)

    | Drive the buggy to the left.
    | ``tightness`` values are integers from 1 to 5
    | Default ``tightness`` is 5 (a tight turn).
    | ``duration`` values are integers above 0.
    | Default ``duration`` is None.
    | The motor will stop after a given duration in milliseconds.
    | If the duration is None, the motor runs without stopping, until another command is sent to the motor.

| The code below, ``left(tightness=5, duration=4000)``, turns the buggy left through a tight turn for 4 secs.

.. code-block:: python

    from microbit import *
    import maqueen


    # setup buggy
    buggy = maqueen.MaqueenMotors()

    buggy.left(tightness=5, duration=4000)


----

.. admonition:: Tasks

    #. Write code to drive the buggy to the left at tightness 3 for 5 seconds.
    #. Write code to drive the buggy to the left at tightness 1 for 5 seconds.
    #. Write code to drive the buggy to the left at increasing tightness. Use a for loop to change the tightness from 1 to 5, with each turn lasting for 2 seconds.

----

right
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: right(tightness=5, duration=None)

    | Drive the buggy to the right.
    | ``tightness`` values are integers from 1 to 5
    | Default ``tightness`` is 5 (a tight turn).
    | ``duration`` values are integers above 0.
    | Default ``duration`` is None.
    | The motor will stop after a given duration in milliseconds.
    | If the duration is None, the motor runs without stopping, until another command is sent to the motor.

| The code below, ``right(5, 4000)``, turns the buggy right through a tight turn for 4 secs.

.. code-block:: python

    from microbit import *
    import maqueen


    # setup buggy
    buggy = maqueen.MaqueenMotors()

    buggy.right(5, 4000)

----

.. admonition:: Tasks

    #. Write code to drive the buggy to the right at tightness 4 for 2 seconds.
    #. Write code to drive the buggy to the right at tightness 1 for 2 seconds.
    #. Write code to drive the buggy to the right at decreasing tightness. Use a for loop to change the tightness from 5 to 1, with each turn lasting for 2 seconds.

----

Spinning
----------------------------------------

| Spin the buggy to the left or right at the chosen speed using:
| ``spin_left(speed=1, duration=None)``
| ``spin_right(speed=1, duration=None)``
| When spining left, the left wheel goes forwards while the right wheel goes forward.
| When spining right, the right wheel goes forwards while the left wheel goes forward.

----

spin left
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: spin_left(speed=1, duration=None)

    | Spin the buggy on the spot.
    | ``speed`` values are integers from 0 to 5.
    | Default ``speed`` is 1.
    | ``duration`` values are integers above 0.
    | Default ``duration`` is None.
    | The motor will stop after a given duration in milliseconds.
    | If the duration is None, the motor runs without stopping, until another command is sent to the motor.

| ``spin_left()`` and ``spin_left(1)`` and ``spin_left(speed=1)`` all spin the buggy to the left at speed 1.
| ``spin_left(3, 2000)`` and ``spin_left(3, duration=2000)`` and ``spin_left(speed=3, duration=2000)`` all spin the buggy to the left at speed 3 for 2 secs.

----

spin right
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: spin_right(speed=1, duration=None)

    | Spin the buggy on the spot.
    | ``speed`` values are integers from 0 to 5.
    | Default ``speed`` is 1.
    | ``duration`` values are integers above 0.
    | Default ``duration`` is None.
    | The motor will stop after a given duration in milliseconds.
    | If the duration is None, the motor runs without stopping, until another command is sent to the motor.

| The code below, ``spin_right(2, 4000)``, spins the buggy to the right at speed 2 for 4 secs.

.. code-block:: python

    from microbit import *
    import maqueen


    # setup buggy
    buggy = maqueen.MaqueenMotors()

    buggy.spin(2, 'right', 4000)

----

.. admonition:: Tasks

    #. Write code to spin the buggy to the left at speed 4 for 5 seconds.
    #. Write code to spin the buggy to the right at speed 2 for 3 seconds.
    #. Write code to spin the buggy to the left for 3 seconds then to right for 3 seconds at speed 4.
    #. Write code to drive the buggy in a polygonal path (many straight sides) by combining short drives forwards with short spins.

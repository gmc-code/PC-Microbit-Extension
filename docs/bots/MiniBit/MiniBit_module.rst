====================================================
MiniBit module
====================================================

Pins for the motors are below.

=======  ===========================
 Pin     Purpose
=======  ===========================
 pin12   Left Motor
 pin8    Left Motor Backwards

 pin14   Right Motor
 pin16   Right Motor Backwards

 pin15   Ultrasonic
=======  ===========================

| Write a module for the MiniBit that uses classes.

* a class for **motors** using pin12, pin8, pin14, pin16
* a class for **ultrasonic sensor** using pin15

| The module will be named ``MiniBit.py``.
| Code using the module will typically begin with:

.. code-block:: python

    from microbit import *
    import MiniBit

| Each class will be named systematically, using **MiniBit** in their names.
| Objects for each class will be created when setting up the MiniBit.

.. code-block:: python

    from microbit import *
    import MiniBit
    
    buggy = MiniBit.MiniBitMotors()
    distance_sensor = MiniBit.MiniBitDistanceSensor()


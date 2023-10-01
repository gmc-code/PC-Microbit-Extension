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

----

Install module
------------------

| The ``MiniBit`` module is required to control the MiniBit buggy.
| Download the python file :download:`MiniBit.py module <files/MiniBit.py>`.
| Place it in the mu_code folder: C:\\Users\\username\\mu_code
| The file needs to be copied onto the microbit.
| In Mu editor, with the microbit attached by USB, click the Files icon.
| Files on the microbit are shown on the left.
| Files in the mu_code folder are listed on the right.
| Click and drag the maqueen.py file from the right window to the left window to copy it to the microbit.

| The images below are for the maqueen, but illustrate the idea.
| Before copying:

.. image:: images/Mu_files.png
    :scale: 50 %

After copying:

.. image:: images/Mu_files_copied.png
    :scale: 50 %


----

Module code
----------------------------------------

| The module is shown below.

.. literalinclude:: files/MiniBit.py
   :linenos:


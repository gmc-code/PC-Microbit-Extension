====================================================
MOVEMotor module
====================================================


| The MOVEMotor module is required to control the **MOVEmotor buggy v3.1**.
| Download the python file :download:`MOVEMotor.py module <files/MOVEMotor.py>`.
| Place it in the mu_code folder: C:\\Users\\username\\mu_code
| The file needs to be copied onto the microbit.
| In Mu editor, with the microbit attached by USB, click the Files icon.
| Files on the microbit are shown on the left.
| Files in the mu_code folder are listed on the right.
| Click and drag the MOVEMotor.py file from the right window to the left window to copy it to the microbit.

Before copying:

.. image:: images/Mu_files.png
    :scale: 50 %

After copying:

.. image:: images/Mu_files_copied.png
    :scale: 50 %


----

Use MOVEMotor library
----------------------------------------

| To use the MOVEMotor module, import it via: ``import MOVEMotor``.

.. code-block:: python

    from microbit import *
    import MOVEMotor

----

MOVEmotor buggy versions 1 and 2
----------------------------------------


| The MOVEMotor_v2 module is required to control the MOVEmotor buggy versions 1 and 2.
| Download the python file :download:`MOVEMotor_v2.py module <files/MOVEMotor_v2.py>`.


| To use the MOVEMotor_v2 module, import it via: ``import MOVEMotor_v2 as MOVEMotor``.
| This will allow the sample code in these docs to be used without a need to change all other references to ``MOVEMotor``.

.. code-block:: python

    from microbit import *
    import MOVEMotor_v2 as MOVEMotor


----

MOVEMotor code v31
----------------------------------------

| The full version of the MOVEMotor module is shown below.


.. literalinclude:: files/MOVEMotor_v31.py
   :linenos:

----

MOVEMotor code
----------------------------------------

| The simplified version of the MOVEMotor module is shown below.
| It has comments removed to reduce the file size.

.. literalinclude:: files/MOVEMotor.py
   :linenos:

----

MOVEMotor code v2
----------------------------------------

| The MOVEMotor module that supports v2 of the MOVEMotor, using i2c to control the motors, is shown below.

.. literalinclude:: files/MOVEMotor_v2.py
   :linenos:


====================================================
Maqueen headlights
====================================================

| The maqueen buggy has two red headlights.

Set up buggy headlights
----------------------------------------

.. py:class:: MaqueenHeadLights() 

    | Set up the buggy's headlights for use.
    | Use ``headlights = maqueen.MaqueenHeadLights()`` to use the buggy's headlights.

| The code below imports the maqueen module and sets up the headlights.

.. code-block:: python

    from microbit import *
    import maqueen


    headlights = maqueen.MaqueenHeadLights()


----

set_headlight
----------------------------------------

.. py:method:: set_headlight(headlight='left', on=1)

    | Turn the red headlights on or off individually.
    | ``headlight`` is 'left' or 'right'. Default is 'left'.
    | ``on`` is 1 to turn on the headlight or 0 to turn off the headlight. Default is 1.

| The code below turns on the left headlight.

.. code-block:: python

    from microbit import *
    import maqueen


    headlights = maqueen.MaqueenHeadLights()

    headlights.set_headlight(headlight='left', on=1)

----

.. admonition:: Tasks

    #. Write code to turn on the left headlight, then after a sleep of 1 sec, turn it off.
    #. Write code to turn on the right headlight, then after a sleep of 2 secs, turn it off.

----

set_headlights
----------------------------------------

.. py:method:: set_headlights(left=1, right=1)

    | Turn the red headlights on or off.
    | ``left`` is 1 to turn on the headlight or 0 to turn off the headlight. Default is 1.
    | ``right`` is 1 to turn on the headlight or 0 to turn off the headlight. Default is 1.

| The code below turns on both headlights.

.. code-block:: python

    from microbit import *
    import maqueen


    headlights = maqueen.MaqueenHeadLights()
    
    headlights.set_headlights(left=1, right=1)

----

.. admonition:: Tasks

    #. Write code to turn on the left headlight while turning off the right headlight.
    #. Write code to turn on both headlights, then after a sleep of 1 sec, turn them both off.


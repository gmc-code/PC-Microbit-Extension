====================================================
Games introduction
====================================================

| Some of the games in this section use python classes where convenient.

----

All time records
----------------

.. list-table::
    :widths: 60 20 60
    :header-rows: 1

    *   - **Game** 
        - **High score**  
        - **Player**
    *   - Asteroids
        - 4207    
        - Lachlan
    *   - Falling Blocks
        - 154    
        - Sai
    *   - Space Invaders    
        - 365    
        - Snehath
    *   - Snake    
        - 140 
        - Jaskirat


----

Modifying the game code for official records
----------------------------------------------

| All records have to be witnessed.
| One way to enable this is to add a for-loop to display the final game score many times so it can be sighted by a witness.

.. code-block:: python
        
    display.scroll(str(score))


While keeping the original indenting level, the code above can be changed to:

.. code-block:: python
        
    for i in range(10):
        display.scroll(str(score))

The ``display`` line is indented as part of the for-loop.

----

Game loop for replays
-----------------------

| There are convenient ways to show to the user that the game can be played and played again.
| In the code below, an arrow pointing to the A button suggests to the user that they should press the A button.

.. code-block:: python
    
    
    from microbit import *


    while True:
        display.show(Image.ARROW_W)
        if button_a.is_pressed():
            PlayGame()
        sleep(1000)


----

| In the code below, when the game ends, "A or B" is scrolled across the screen and the user has 2 seconds to hold down the A or B buttons to play the game again, otherwise the ``while True`` loop is exited and the game can no longer be played.

.. code-block:: python
    
    
    from microbit import *


    while True:
        PlayGame()
        display.scroll("A or B", delay=80)
        sleep(2000)
        if button_a.is_pressed() or button_b.is_pressed():
            continue
        else:
            break


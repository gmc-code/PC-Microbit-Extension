====================================================
Press It game
====================================================

Game design
--------------------

| Press It is a game to press the A or B button after 'A' or 'B' is shown.
| A class is used to run the game.

#. Set up the game object
    a. Assign values to the LEVEL_SPEED dictionary.
    b. Assign values to the LEVELUP tuple.
    c. Set the score to 0.
    d. Set the level to 1.
#. Run the game:
    a. Show 'A' or 'B'.
    b. If the correct button is pressed within the time limit then:
        #. Display a tick (Image.YES).
        #. Add one to the score.
        #. Level up if the next level has been reached.
    c. If the wrong button is pressed or no button is pressed within the time limit then:
        #. Display an X (Image.NO).
        #. Scroll the score.

| The code uses the class, ``PressIt()``, for the game object.
| Only the ``run_game`` method is used outside the class itself.

| The code below omits the PressIt class for simplicity, but shows the rest of the game code.
| The while True loop repeats the game if both buttons have been pressed.

.. code-block:: python

    from microbit import *
    import random

    game = PressIt()
    game.run_game()
    while True:
        if button_a.was_pressed() and button_b.was_pressed():
            game = PressIt()
            game.run_game()
        else:
            sleep(2000)


----

The PressIt class
------------------------

| Use a class for the game object.

.. py:class:: PressIt()

    | Set up the game object to control the game, including the LEVEL_SPEED dictionary, the LEVELUP tuple, the initial level and score.

| The code below imports the random module and creates the game object by creating an instance of the PressIt class.

.. code-block:: python

    from microbit import *
    import random


    game = PressIt()

----

The PressIt class methods
-------------------------------

| The PressIt class methods are described below.

#. ``show_a()`` shows 'A'.
#. ``show_b()`` shows 'B'.
#. ``show_yes()`` shows a tick, Image.YES.
#. ``show_no()`` shows a cross, Image.NO.
#. ``show_start`` shows 'A or B' and the level.
#. ``show_levelup()`` shows an up arrow, Image.ARROW_N, and scrolls the level.
#. ``show_score`` shows the score.
#. ``is_correct_button()`` picks A or B to show then waits according to the duration for the level, and returns True if the correct button has been pressed, otherwise False.
#. ``continue_game()`` calls show_yes() and updates the score and level.
#. ``end_game()`` calls show_no() and show_score() methods
#. ``run_game()`` calls several methods as it checks the correct button is pressed within the time limit and either continues or ends the game.

----

The PressIt constructor
---------------------------------

.. py:method:: __init__()

    | The __init__() method is the constructor called when the game object is created.
    | ``score`` is set to 0.
    | ``level`` is set to 1.

| The __init__ method is given below.

.. code-block:: python

    class TiltPixels:

        def __init__(self):
            self.score = 0
            self.level = 1

----

The PressIt class constants
---------------------------------

| The class constants are in capitals: LEVEL_SPEED and LEVELUP.
| LEVEL_SPEED is a dictionary with the level number as the key and the duration in milliseconds. The duration specifies the time the player has to press a button. e.g for ``1: 1200``, the key is 1 and the duration is 1200.
| LEVELUP is a tuple of numbers for when the level is increased. e.g. after 3 correct button presses the level goes up 1. There are only 8 numbers even though there are 9 levels, since there can only be 8 level ups from level 1 to level 9.

.. code-block:: python

    class TiltPixels:

        LEVEL_SPEED = {1: 1200, 2: 1000, 3: 800, 4: 700, 5: 600, 6: 550, 7: 500, 8: 450, 9: 400}
        LEVELUP = (3, 6, 9, 12, 15, 18, 21, 24)

----

Game code
---------------------------------

| The game code is below.

.. code-block:: python

    """PressIt_game: Press the A or B button when the text is shown"""

    from microbit import *
    import random


    class PressIt():
        
        LEVEL_SPEED = {1: 1200, 2: 1000, 3: 800, 4: 700, 5: 600, 6: 550, 7: 500, 8: 450, 9: 400}
        LEVELUP = (3, 6, 9, 12, 15, 18, 21, 24)
        
        def __init__(self):
            self.score = 0
            self.level = 1

        def show_a(self):
            display.show("A")

        def show_b(self):
            display.show("B")

        def show_yes(self):
            display.show(Image.YES)
            sleep(500)

        def show_no(self):
            display.show(Image.NO)
            sleep(500)

        def show_levelup(self):
            display.show(Image.ARROW_N)
            display.scroll('level ' + str(self.level), delay=60)
            sleep(500)

        def is_correct_button(self):
            button_number = random.randint(0, 1)
            if button_number == 0:
                self.show_a()
            elif button_number == 1:
                self.show_b()
            a_pressed = False
            b_pressed = False
            start_time = running_time()
            now = running_time()
            while now - start_time < self.LEVEL_SPEED[self.level]:
                if button_a.is_pressed():
                    a_pressed = True
                if button_b.is_pressed():
                    b_pressed = True
                now = running_time()
            if button_number == 0:
                if a_pressed is True and b_pressed is False:
                    return True
                else:
                    return False
            elif button_number == 1:
                if a_pressed is False and b_pressed is True:
                    return True
                else:
                    return False

        def continue_game(self):
            self.show_yes()
            self.score += 1
            if self.score in self.LEVELUP:
                self.level += 1
                self.show_levelup()
                
        def end_game(self):
            self.show_no()
            self.show_score()
                
        def run_game(self):
            self.show_start()
            game_over = False
            while game_over is False:
                if self.is_correct_button():
                    self.continue_game()
                else:
                    game_over = True
                    self.end_game()

    game = PressIt()
    game.run_game()
    while True:
        if button_a.was_pressed() and button_b.was_pressed():
            game = PressIt()
            game.run_game()
        else:
            sleep(2000)


----

.. admonition:: Tasks

    #. Modify the code to display left and right arrows instead of 'A' and 'B'.
    #. Add a rapid animation of 3 to 6 built in image shapes to be shown when the level reaches level 5.
    #. Replace the level scrolled text with an animation in which the number of images in the animation is equal to the level number.
    #. Add code to store all the game scores and display the average score after each game.
    #. Add code to store the best game score after each game and display the best score after exiting by pressing both buttons.




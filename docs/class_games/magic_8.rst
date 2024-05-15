====================================================
Magic 8-ball
====================================================

Game design
--------------------

| The user asks a yes-no question then shakes the microbit to receive an answer.
| The standard responses are in the list **responses**.
| A random choice from the list is obtained using ``random.choice(responses)``.

Specific Syntax
--------------------

.. py:function::  import random

    Import the random number module.

.. py:function::  random.choice(sequence)

    Return a random element from a sequence such as a list.

| e.g. Randomly choose from the list **responses** and scroll the choice.
| ``display.scroll(random.choice(responses), delay=120)``

.. py:function::  accelerometer.was_gesture(gesture)

    Return True or False to indicate if the named gesture was active since the last call.

| e.g. Decide what to do if the microbit was shaken.
| ``if accelerometer.was_gesture("shake"):``

----

Game code without classes
---------------------------------

| The version of the game code, using functions, without classes, is below.

.. code-block:: python


    """Magic_8 simulation see responses at https://en.wikipedia.org/wiki/Magic_8-Ball"""

    from microbit import *
    import random


    responses = [
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes, definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
        "Reply hazy try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful",
    ]

    while True:
        display.show("8")
        if accelerometer.was_gesture("shake"):
            display.clear()
            sleep(1000)
            display.scroll(random.choice(responses), delay=120)

----

.. admonition:: Tasks

    #. Modify the code to only respond with positive responses.
    #. Modify the code to require a tilt to the left or right instead of a shake.
    #. Modify the code to require a button press instead of a shake.
    #. Divide up the responses into positive responses and negative responses. Display a positive response when the A button is pressed and a negative response when the B button is pressed.
    #. Divide up the responses into positive responses and negative responses. Display a negative response when the microbit is tilted to the left and a positive response when the microbit is tilted to the right.

----

Converting to using a class
---------------------------------

| The class version of the game code is below.
| ``game = Magic8()`` instantiates the class by creating an object from the class, called an instance, which inherits all the class attributes and methods.
| The ``__init__`` method has the **responses** list as well as an attribute for the text, **magic_text**, to display between responses.
| The ``run_game`` method has the game code that was previously within the body of the while loop.
| ``game.run_game()`` calls the ``run_game`` method on the game object to run the game.

.. code-block:: python


    from microbit import *
    import random


    class Magic8:
        """Magic_8 game using a class"""
        def __init__(self, magic_text=8):
            self.magic_text = magic_text
            self.responses = [
                "It is certain",
                "It is decidedly so",
                "Without a doubt",
                "Yes, definitely",
                "You may rely on it",
                "As I see it, yes",
                "Most likely",
                "Outlook good",
                "Yes",
                "Signs point to yes",
                "Reply hazy try again",
                "Ask again later",
                "Better not tell you now",
                "Cannot predict now",
                "Concentrate and ask again",
                "Don't count on it",
                "My reply is no",
                "My sources say no",
                "Outlook not so good",
                "Very doubtful",
            ]
            
        def run_game(self):
            display.show(self.magic_text)
            sleep(1000)
            if accelerometer.was_gesture("shake"):
                display.clear()
                sleep(100)
                display.scroll(random.choice(self.responses), delay=120)

    game = Magic8()
    while True:
        game.run_game()

.. admonition:: Tip
    
    In the code ``game = Magic8()``, the class is ``Magic8`` and the instantiated object is ``game``.
    The ``__init__`` method is used to initialize (assign values) to the data variables of the class when the class object is created. It also can contain statements (i.e. instructions) that are executed at time of object creation. The ``__init__`` method is run as soon as the class object is instantiated. 

----

Modifying classes
---------------------------------

| Below are some examples of how game variations can be achieved by modifying the classes.
| To keep the code shorter, the standard game responses are replaced with the 4 below:
| ``responses = ["For sure", "Yes", "No", "No way"]``

----

Pass arguments to the class
---------------------------------

.. admonition:: Tasks

    #. Use '?' as an argument for ``Magic8()`` to show '?' instead of '8'.

| When no argument is passed when instantiating the game object, **magic_text** defaults to 8.
| ``game = Magic8('?')`` replaces the default value of 8 with '?'. 
| ``'?'`` is passed to the __init__ method in place of the ``magic_text`` parameter.
| ``self`` is automatically passed to the instance methods.

.. code-block:: python

    from microbit import *
    import random


    class Magic8:
        def __init__(self, magic_text=8):
            self.magic_text = magic_text
            self.responses = ["For sure", "Yes", "No", "No way"]

        def run_game(self):
            display.show(self.magic_text)
            sleep(1000)
            if accelerometer.was_gesture("shake"):
                display.clear()
                sleep(100)
                display.scroll(random.choice(self.responses), delay=120)

    game = Magic8('?')
    while True:
        game.run_game()
    
----

Modify the __init__ method in a child class
------------------------------------------------------

.. admonition:: Tasks

    #. Modify the code to only respond with positive responses.

| The Magic8 class can be used as the parent class.
| A child class, ``Magic8Pos``, can inherit from the ``Magic8`` class by passing ``Magic8`` as an argument when declaring ``Magic8Pos``, as in: ``class Magic8Pos(Magic8):``
| Use ``super().__init__(magic_text=8)`` to inherit attributes from the ``__init__`` method in the ``Magic8`` class.
| Modify the ``self.responses`` attribute in the child class, ``Magic8Pos``, to just use positive responses.
| There is no need to include a **run_game** method in the child class since it is inherited.

.. code-block:: python

    from microbit import *
    import random


    class Magic8:
        def __init__(self, magic_text=8):
            self.magic_text = magic_text
            self.responses = ["For sure", "Yes", "No", "No way"]

        def run_game(self):
            display.show(self.magic_text)
            sleep(1000)
            if accelerometer.was_gesture("shake"):
                display.clear()
                sleep(100)
                display.scroll(random.choice(self.responses), delay=120)


    class Magic8Pos(Magic8):
        """modifies responses to just positive ones"""
        def __init__(self, magic_text=8):
            super().__init__(magic_text=8)
            self.responses = ["It is certain", "Yes"]

    game = Magic8Pos(Magic8)
    while True:
        game.run_game()

----

Use tilting in the run_game method in a child class
----------------------------------------------------------

.. admonition:: Tasks

    #. Modify the code to require a tilt to the left or right instead of a shake.

| The Magic8 class can be used as the parent class.
| A child class, ``Magic8Tilt``, can inherit from the ``Magic8`` class by passing it as an argument when declaring it, as in: ``class Magic8Tilt(Magic8):``
| Use ``super().__init__(magic_text=8)`` to inherit attributes from the ``__init__`` method in the ``Magic8`` class.
| Modify the ``run_game`` method in the child class, ``Magic8Tilt``, to use tilting.

.. code-block:: python

    from microbit import *
    import random


    class Magic8:
        def __init__(self, magic_text=8):
            self.magic_text = magic_text
            self.responses = ["For sure", "Yes", "No", "No way"]

        def run_game(self):
            display.show(self.magic_text)
            sleep(1000)
            if accelerometer.was_gesture("shake"):
                display.clear()
                sleep(100)
                display.scroll(random.choice(self.responses), delay=120)


    class Magic8Tilt(Magic8):
        """modifies run_game to use tilts"""
        def __init__(self, magic_text=8):
            super().__init__(magic_text=8)
                
        def run_game(self):
            display.show(self.magic_text)
            sleep(1000)
            if accelerometer.was_gesture("left") or accelerometer.was_gesture("right"):
                display.clear()
                sleep(100)
                display.scroll(random.choice(self.responses), delay=120)

                    
    game = Magic8Tilt()
    while True:
        game.run_game()

----

Use button pressing in the run_game method in a child class
-----------------------------------------------------------------------

.. admonition:: Tasks

    #. Modify the code to require a button press instead of a shake.

| The Magic8 class can be used as the parent class.
| A child class, ``Magic8Button``, can inherit from the ``Magic8`` class by passing it as an argument when declaring it, as in: ``class Magic8Button(Magic8):``
| Use ``super().__init__(magic_text=8)`` to inherit attributes from the ``__init__`` method in the ``Magic8`` class.
| Modify the ``run_game`` method in the child class, ``Magic8Button``, to use button pressing.


.. code-block:: python

    from microbit import *
    import random


    class Magic8:
        def __init__(self, magic_text=8):
            self.magic_text = magic_text
            self.responses = ["For sure", "Yes", "No", "No way"]

        def run_game(self):
            display.show(self.magic_text)
            sleep(1000)
            if accelerometer.was_gesture("shake"):
                display.clear()
                sleep(100)
                display.scroll(random.choice(self.responses), delay=120)


    class Magic8Button(Magic8):
        """modifies run_game to use button pressing"""
        def __init__(self, magic_text=8):
            super().__init__(magic_text=8)
                
        def run_game(self):
            display.show(self.magic_text)
            sleep(1000)
            if button_a.is_pressed() or button_b.is_pressed():
                display.clear()
                sleep(100)
                display.scroll(random.choice(self.responses), delay=120)

    game = Magic8Button()
    while True:
        game.run_game()


----

Modify the __init__ and run_game methods in a new class
-----------------------------------------------------------------------

.. admonition:: Tasks

    #. Divide up the responses into positive responses and negative responses. Display a negative response when the A button is pressed and a positive response when the B button is pressed.

| Rewrite the Magic8 class since both methods need changing.
| In the ``__init__`` method, use **responses_neg** and **responses_pos** instead of just **responses**.
| In the ``run_game`` method, use button pressing to set the **responses_choice** which is then picked from for display.

.. code-block:: python

    from microbit import *
    import random


    class Magic8NegPos:
        def __init__(self, magic_text=8):
            self.magic_text = magic_text
            self.responses_pos = ["For sure", "Yes"]
            self.responses_neg = ["No", "No way"]

        def run_game(self):
            display.show(self.magic_text)
            sleep(1000)
            if button_a.is_pressed():
                responses_choice = self.responses_neg
            elif button_b.is_pressed():
                responses_choice = self.responses_pos
            else:    
                responses_choice = ""
            if responses_choice != "":
                display.clear()
                sleep(100)
                display.scroll(random.choice(responses_choice), delay=120)

    game = Magic8NegPos()
    while True:
        game.run_game()

----

.. admonition:: Tasks

    #. Use a subclass of ``Magic8NegPos`` to display a negative response when the microbit is tilted to the left and a positive response when the microbit is tilted to the right.
    #. Use a subclass of ``Magic8NegPos`` to display a negative response when pin0 of the microbit is touched and a positive response when pin2 of the microbit is touched.

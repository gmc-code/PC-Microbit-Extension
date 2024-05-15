====================================================
Instance Methods
====================================================

| When you define a function inside a class, and call the function via an instance of a class, the function is a method. e.g ``game.level_up()`` below.
| The method, ``def level_up(self)``, has the first argument, ``(self)``.
| Python automatically passes the object to the method as the first argument. 

----

Regular Methods without parameters
----------------------------------------

| In the code below, ``game.level_up()`` calls the method ``level_up``.
| ``self.game_level += 1`` adds 1 to ``self.game_level``.
| When calling the method on the game object, ``game.level_up()``, self is not written in the parentheses since it is automatically passed.
| The first print statement outputs 1, since the game object is instantiated with a game_level of 1 via ``game = LevelGame(game_level=1)``.
| Then, after the ``level_up()`` method has been called via ``game.level_up()``, the second print statement outputs 2.

| In the code below

.. code-block:: python

    class LevelGame:
        def __init__(self, game_level):
            self.game_level = game_level

        def level_up(self):
            self.game_level += 1

    game = LevelGame(game_level=1)
    print(game.game_level)

    game.level_up()
    print(game.game_level)


.. admonition:: Tasks

    #. Check that print output above is 1, then 2.
    #. Modify the level_up function in the previous example so that the level can't go above 10. Hint: use the max function.
    #. Modify the code so that the LevelGame.game_level starts at 10 then goes down by 1 when a level_down function is called.
    #. Modify the level_down function in the previous example so that the level can't go below 0. Hint: use the min function.

----

Regular Methods with parameters
-------------------------------------

| In the code below, ``game.set_speed(5)`` calls the method ``set_speed`` to set the variable ``self.game_speed`` to 5.
| ``game = SpeedGame(1)`` initializes the game speed to 1.
| The print statement outputs 1.
| ``game.set_speed(5)`` sets the game speed to 5.
| The print statement outputs 5.

.. code-block:: python

    class SpeedGame:
        def __init__(self, game_speed):
            self.game_speed = game_speed

        def set_speed(self, game_speed):
            self.game_speed = game_speed

    game = SpeedGame(1)
    print(game.game_speed)

    game.set_speed(5)
    print(game.game_speed)


.. admonition:: Tasks

    #. Modify the set_speed function so that any speed values passed in are limited to a maximum speed of 10. Hint: use the max function.
    #. Modify the set_speed function so the speed must be between 0 and 10. Hint: use the min and max functions.


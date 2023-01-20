====================================================
The init function
====================================================

The __init__() function
--------------------------

| The ``__init__()`` function is a built-in-function that is used to assign values to object attributes, and to do other operations that are necessary when the object is created.
| The ``__init__()`` function is called automatically every time the class is called when creating a new object.
| The first parameter in the ``__init__()`` function is self, referring to the object itself.
| Other parameters can follow self. e.g. ``__init__(self, level)``
| These other parameters, such as ``level``, are passed in as arguments when the class is called.
| e.g. ``game = LevelGame(level=1)`` passes in ``level=1`` to the ``__init__()`` function.
|  ``game = LevelGame(1)`` and ``game = LevelGame(level=1)`` do the same thing.
| e.g. ``game = LevelGame(level=1, lives=3)`` passes in ``level=1`` and ``lives=3`` to the ``__init__()`` function.

| In the sample code, two instance variables, game_level and player_lives, are created.

.. code-block:: python

    class LevelGame:
        def __init__(self, game_level, player_lives):
            self.game_level = game_level
            self.player_lives = player_lives

    game = LevelGame(game_level=1, player_lives=3)


.. admonition:: Tasks

    #. Modify the code so that the game level starts at level 0 with 5 lives.
    #. Modify the code so the parameters and the instance variables have matching names.
    #. Modify the code by adding a third instance variable using a parameter called level_score and initialize it to 0.

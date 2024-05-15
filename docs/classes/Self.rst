====================================================
Self
====================================================


Self in variables
----------------------

| The **self** parameter is used to access variables that belong to the class as instance variables.
| The dot, '.', operator is then used to access the object variable.
| e.g. ``self.game_level``

----

Self in methods
----------------------

| Class functions use the **self** parameter (first parameter) to reference the current instance of the class.

.. code-block:: python

    class LevelGame:
        def __init__(self, game_level):
            self.game_level = game_level


| It does not have to be named **self**, but it makes it easier for others if it is used, since that is common practice.
| The code below uses "game" instead of "self".
| Since this is not expected, it makes it harder for another programmer to read it fluently.

.. code-block:: python

    class LevelGame:
        def __init__(game, game_level):
            game.game_level = game_level


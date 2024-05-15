====================================================
Instance variables
====================================================

Variables unique to the instance
--------------------------------------

| Instance variables are variables, created in a class, that are unique to the instance.
| The __init__() function assigns values to instance variables when the object is created. 
| e.g. ``self.game_level = 1``
| ``self.game_level`` is an instance variable. It is referenced using the self keyword.

.. code-block:: python

    class LevelGame:
        def __init__(self):
            self.game_level = 1

    game = LevelGame()
    print(game.game_level)

----

Instantiating a class instance with arguments
---------------------------------------------------

| Parameters can be used in the ``__init__`` definition so that arguments can be passed when the object is instantiated.
| e.g. the ``level`` parameter has been used in ``__init__(self, level)``.
| When game is instantiated using ``game = LevelGame(1)``, a value of 1 is passed in as the argument, so that ``level`` = 1.

.. code-block:: python

    class LevelGame:
        def __init__(self, level):
            self.game_level = level

    game = LevelGame(1)
    print(game.game_level)

----

Customary variable names
---------------------------------------------------

| Is it customary to use the same name for the parameters as for the instance variables.
| e.g. ``self.game_level = game_level``
| In the code above, a different variable name, ``level``, has been used instead of ``game_level`` to help see what is happening with the variables.
| The code below follows the custom.

.. code-block:: python

    class LevelGame:
        def __init__(self, game_level):
            self.game_level = game_level

    game = LevelGame(1)
    print(game.game_level)

----

.. admonition:: Tasks

    #. Run the code above and check the print output is 1.
    #. Modify the code to use ``game = LevelGame(2)`` and check the print output.

----

Default paramaters
---------------------------------------------------

| A default value for a pareter can be set.
| e.g. the ``level`` parameter can be set to a value of 1 by default in ``__init__(self, level=1)``.
| When game is instantiated using ``game = LevelGame()``, ``level`` = 1 by default.

.. code-block:: python

    class LevelGame:
        def __init__(self, level=1):
            self.game_level = level

    game = LevelGame()
    print(game.game_level)

----

Changing Instance variables in an instance
----------------------------------------------

| An instance variable can be altered for a particular instance.
| ``game.game_level = 2`` changes the value of the variable within the instance.

.. code-block:: python

    class LevelGame:
        def __init__(self, game_level):
            self.game_level = game_level

    game = LevelGame(1)
    game.game_level = 2
    print(game.game_level)

.. admonition:: Tasks

    #. Check the print output to verify that the instance has a different value to that set when the instance was created.
    #. Add code after the instance value is changed so that the ``game.game_level`` is set to 3, then check the value for the instance to see if it is affected.

----

.. admonition:: Tip

    #. Direct access to instance variables outside of the class code can be prevented by using double underscores.
    #. ``self.game_level`` could be changed to ``self.__game_level`` so that ``game.__game_level`` would be blocked.
    #. However, ``game._LevelGame__game_level`` still enables access to the attribute.
    #. Setters (a method to set self.__game_level) and getters (a method to return self.__game_level) are methods used along with this approach, known as encapsulation.

    .. code-block:: python

        class LevelGame:
            def __init__(self, game_level):
                self.__game_level = game_level
                
            def set_game_level(self, game_level):
                self.__game_level = game_level
                
            def get_game_level(self):
                return self.__game_level 

        game = LevelGame(3)
        print(game._LevelGame__game_level)
        print(game.get_game_level())


 
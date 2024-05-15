====================================================
Class variables
====================================================

Class variables common to instances
------------------------------------------

| A class variable is shared by all instances of a class.
| In the code below, ``game_level`` is a class variable.
| In the code below, both ``game1.game_level`` and ``game2.game_level`` have the same value.

.. code-block:: python

    class LevelGame:
        game_level = 1

    game1 = LevelGame()
    print(game1.game_level)

    game2 = LevelGame()
    print(game2.game_level)

.. admonition:: Tasks

    #. Check that the print output is the same for each print statement above.
    #. Modify the code so that the class definition has a game_level of 0, then check its value for both instances.

----

Changing Class variables for all instances
----------------------------------------------

| A class variable can be altered in the class.
| In the code below, ``LevelGame.game_level = 3``, the class variable is changed to 3.
| The change in the class variable results in the same change for the instance values of ``game1.game_level`` and ``game2.game_level``.

.. code-block:: python

    class LevelGame:
        game_level = 1

    game1 = LevelGame()
    game2 = LevelGame()

    LevelGame.game_level = 3
    print(game1.game_level)
    print(game2.game_level)

.. admonition:: Tasks

    #. Check that print output is the same for each statement above.
    #. Modify the code so that the LevelGame.game_level is set to 5, then check its value for both instances.

----

Changing Class variables in an instance
----------------------------------------------

| A class variable can be altered for a particular instance.
| ``game.game_level = 2`` changes the value of the variable within the instance.
| ``LevelGame.game_level`` is not altered.

.. code-block:: python

    class LevelGame:
        game_level = 1

    game = LevelGame()
    game.game_level = 2
    print(game.game_level)
    print(LevelGame.game_level)

.. admonition:: Tasks

    #. Check the print output to verify that the instance has a different value to the class.
    #. Add code after the instance value is changed so that the ``LevelGame.game_level`` is set to 5, then check the value for the instance to see if it is affected.


.. admonition:: Tip

    #. Use Class variables when the same value is needed in all instances. 
    #. Avoid changing class variables in instances since it can lead to confusion.
    #. Use Instance variables instead of class variables when different values are needed in each instance.

----

Modifying Class variables during instantiation
-------------------------------------------------

| In the code below, ``game_number`` is a class variable.
| ``LevelGame.game_number += 1`` is used to increment the game number by 1 each time a new LevelGame is instantiated.
| Since ``game_number`` is a class variable, it is accessed via ``LevelGame.game_number`` within the __init__ function. The **class name**,  ``LevelGame`` is used instead of **self**.


.. code-block:: python

    class LevelGame:
        game_number = 0
        
        def __init__(self, game_level):
            self.game_level = game_level
            LevelGame.game_number += 1

    game = LevelGame(1)
    print(game.game_number)

    game2 = LevelGame(2)
    print(game.game_number)
    print(game2.game_number)

.. admonition:: Tasks

    #. Check that print output shows that the class variable is the same for both instances.
    #. Add a third instance, game3, then check the class variable value for all three instances.


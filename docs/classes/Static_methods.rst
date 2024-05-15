====================================================
Static methods
====================================================

| Static methods behave like regular functions and are included in the class since they have some logical connection with it.
| Choose to use static methods when there are no references to instance variables or class variables within it.
| In practice, use static methods to define utility methods or group functions that have some logical relationships in a class.

| Static methods do not pass anything automatically (such as self or cls).
| Static methods cannot access and modify an object's attributes.
| In comparison, instance methods pass **self** automatically.
| In comparison, class methods pass the **cls** automatically.

| Static methods do not require a class instance to be created first.
| The simplified code below illustrates this:

.. code-block:: python

    class LevelGame:
        
        @staticmethod        
        def get_required_level_score(game_level):
            return game_level * 10

    score = LevelGame.get_required_level_score(game_level=3)
    print(score)


| In the code below, when the game is instantiated at a particular game level, ``game = LevelGame(game_level=1)``, it will use the static method, ``get_required_level_score``, and then print the value for it.

| ``def get_required_level_score(level):`` does not pass in **self** to the function. 
| The decorator, ``@staticmethod``, is needed to make it so that the function does not require **self** to be passed in.

.. code-block:: python

    class LevelGame:
        game_lives = 5
        
        def __init__(self, game_level):
            self.game_level = game_level
            print(self.get_required_level_score(self.game_level))
            
        @staticmethod        
        def get_required_level_score(level):
            return level * 10

    game = LevelGame(game_level=1)


.. admonition:: Tasks

    #. Test out the static method and show that it is working for 2 different game levels.
    #. Write a static method that calculates a level bonus score using the formula: ``bonus = level * 5.`` 


.. admonition:: Note

    | If a static method needs to call another static method, since self is not avalailable to the method, a reference to the class is needed.
    | The class itself can be used or the special method, __class__, can be used.
    | e.g return MyClass.staticmethod2()
    | e.g return __class__.staticmethod2()


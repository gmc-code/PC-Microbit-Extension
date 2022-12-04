====================================================
Class methods
====================================================

| A class method isn't bound to any specific instance. It's bound to the class only.
| The class methods can access and modify the class state.

| To define a class method:
| First place the ``@classmethod`` decorator above the method definition. 
| The ``@classmethod`` decorator will change an instance method to a class method.
| Second, rename the ``self`` parameter to ``cls``. 
| The ``cls`` means class. Since ``class`` is a keyword, it can't be used as a parameter.

----

@classmethod and cls parameter
-------------------------------------------------

| Class methods use the ``cls`` parameter as the first parameter for passing the class.
| In the code below, ``game_number`` is a class variable.
| The ``set_game_number`` function takes ``cls`` as the first parameter, and has ``game_number`` as a second parameter.
| The class variable, ``cls.game_number``, is set to the value of ``game_number``.
| The function is preceded by the decorator, ``@classmethod``, which is required to make the function work as a class method, so the function acts on the class rather than an instance of the class.
| The class method is called on the class using ``LevelGame.set_game_number(1)`` which sets the class variable, ``game_number``, to 1. 

| The class method, ``set_game_number``,  can also be called on an instance, ``game``,  such as, ``game.set_game_number(1)``. 
| While this works like calling on the class, it makes more sense to call it on the class itself.


.. code-block:: python

    class LevelGame:
        game_number = 0
        
        def __init__(self, game_level):
            self.game_level = game_level
            
        @classmethod        
        def set_game_number(cls, game_number):
            cls.game_number = game_number

    game = LevelGame(1)
    LevelGame.set_game_number(1)
    print(game.game_number)

.. admonition:: Tasks

    #. Modify the code so that the ``game_number`` is set to 5, then check its value for the instance, ``game``.

----

Using a Class method in the __init__ function
-------------------------------------------------

| In the code below, the class method ``increase_lives`` is called by the __init__ function.
| It increases the class variable, ``lives``,  by 1.

.. code-block:: python

    class LevelGame:
        lives = 3
        
        def __init__(self, game_level):
            self.game_level = game_level
            self.increase_lives()
            
        @classmethod        
        def increase_lives(cls):
            cls.lives += 1
            
    game1 = LevelGame(1)
    print(game1.lives)

    game2 = LevelGame(2)
    print(game2.lives)

.. admonition:: Tasks

    #. Modify the code so that the ``lives`` starts at 1 for the first time that ``LevelGame`` is called, then ``increase_lives`` increases lives by 2 each time it is called.

----

Class methods as alternative constructors
-------------------------------------------------

| In the code below, the class method ``make_game`` provides an alternate constructor to that of just calling the class to create a new instance.
| ``game1 = LevelGame(game_level=1)`` results in game_level = 1 and game_lives = 5
| ``game2 = LevelGame.make_game(game_level=1, game_lives=3)`` results in game_level = 1 and game_lives = 3
| The last line of code, ``return cls(game_level)``, calls the __init__ function to create the new instance.

.. code-block:: python

    class LevelGame:
        game_lives = 5
        
        def __init__(self, game_level):
            self.game_level = game_level
            
        @classmethod        
        def set_game_lives(cls, game_lives):
            cls.game_lives = game_lives
            
        @classmethod
        def make_game(cls, game_level, game_lives):
            cls.set_game_lives(game_lives)
            return cls(game_level)
            
            
    game1 = LevelGame(game_level=1)   
    print(game1.game_level, game1.game_lives)

    game2 = LevelGame.make_game(game_level=1, game_lives=3)
    print(game2.game_level, game2.game_lives)

.. admonition:: Tasks

    #. Write code to create a game at level 10 with 2 lives.


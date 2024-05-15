====================================================
RPS classes
====================================================

Python Game design
--------------------

| This version of the game code uses classes: a Player class and a Game class.

----

Player class
--------------------

| Each player will be set up using the Player class.
| e.g.  ``computer = Player('Computer')``.
| The Player class will take the name of the player as the argument.
| The ``__init__`` method has the name parameter.

.. code-block:: python

    class Player:
        def __init__(self, name):
            self.name = name

| The name of the player can be obtained using an instance property.
| e.g. ``computer.name``

| The Player class has a ``set_move`` method to set the player move.
| e.g. ``computer.set_move(random.choice(['scissors', 'paper', 'rock']))``

.. code-block:: python

    class Player:

        def set_move(self, move):
            self.move = move

| The player move can be obtained using the instance property. e.g. ``computer.move``

| It is good practice to initialise all the attributes in the ``__init__`` method 
so the ``move`` attribute is initialised to ``None`` 
before it is set to one of the possible moves.

| Full code for the Player class is below.

.. code-block:: python

    class Player:
        def __init__(self, name):
            self.name = name
            self.move = None

        def set_move(self, move):
            self.move = move


| Test the Player class for the computer Player.

.. code-block:: python

    import random


    class Player:
        def __init__(self, name):
            self.name = name
            self.move = None

        def set_move(self, move):
            self.move = move
            
    computer = Player('Computer')
    computer.set_move(random.choice(['scissors', 'paper', 'rock']))
    print(computer.name, 'played:', computer.move)

----

Game class
--------------------

| Each game will be set up using the Game class. e.g.  ``game = Game(human, computer)``.
| The Game class will take the the two players (instances of the Player class) as the arguments.
| The ``__init__`` method has the the two players as parameters.

.. code-block:: python


    class Game:

        def __init__(self, player1, player2):
            self.player1 = player1
            self.player2 = player2


| Each game will be set up using the Game class. e.g.  ``game = Game(human, computer)``.
| The Game class will take the the two players (instances of the Player class) as the arguments.
| The ``__init__`` method has the the two players as parameters.

.. code-block:: python


    class Game:

        def __init__(self, player1, player2):
            self.player1 = player1
            self.player2 = player2





----

Full code
--------------------


.. code-block:: python

    import random


    number_matches = int(input('How many matches would you like to play? '))


    class Player:
        def __init__(self, name):
            self.name = name
            self.move = None

        def set_move(self, move):
            self.move = move


    class Game:
        win_moves = {'paper': 'rock', 'scissors': 'paper', 'rock': 'scissors'}

        def __init__(self, player1, player2):
            self.player1 = player1
            self.player2 = player2

        def get_match_winner(self):
            if self.player1.move == self.player2.move:
                return None
            if Game.win_moves[self.player1.move] == self.player2.move:
                return self.player1
            else:
                return self.player2


    human = Player('Human')
    computer = Player('Computer')
    for i in range(number_matches):
        computer.set_move(random.choice(['scissors', 'paper', 'rock']))
        human.set_move(input('Type your move: rock, paper or scissors. \n'))
        print(computer.name, 'played:', computer.move)
        print(human.name, 'played:', human.move)

        game = Game(human, computer)
        winner = game.get_match_winner()
        if not winner:
            print('Tie!')
        else:
            print(winner.name, 'won')
    print('GAME OVER!')


----

.. admonition:: Tasks

    #. Modify the python code to use R, P or S instead of rock, paper or scissors throughout the code.
    #. Add counters so that the total wins, losses and draws is printed after each game in python.
    #. Modify the code to ask for a valid move from the use by placing the human move in a while loop and test to see if the move is a list or tuple of valid moves.

----

Microbit version
---------------------------------

| The Microbit version of the game code, using classes, is below.


.. code-block:: python

    from microbit import *
    import random


    class Player:
        def __init__(self, name):
            self.name = name
            # self.move = None

        def set_move(self, move):
            self.move = move


    class Game:
        win_moves = {'P': 'R', 'S': 'P', 'R': 'S'}

        def __init__(self, player1, player2):
            self.player1 = player1
            self.player2 = player2

        def get_match_winner(self):
            if self.player1.move == self.player2.move:
                return None
            if Game.win_moves[self.player1.move] == self.player2.move:
                return self.player1.name
            else:
                return self.player2.name

    human = Player('human')
    microbit = Player('microbit')

    display.scroll('A for R, B for P, AB for S', delay=80)
    while True:
        microbit.set_move(random.choice(['R', 'P', 'S']))
        while True:
            # short pause to allow time to hold down 2 buttons
            sleep(300)
            if button_a.is_pressed() and button_b.is_pressed():
                human.set_move('S')
                break
            elif button_a.is_pressed():
                human.set_move('R')
                break
            elif button_b.is_pressed():
                human.set_move('P')
                break

        display.scroll(human.move + ' v ' + microbit.move, delay=60)
        game = Game(human, microbit)
        winner = game.get_match_winner()

        if winner == None:
            display.show('=')
        elif winner == 'human':
            display.show(Image.YES)
        elif winner == 'microbit':
            display.show(Image.NO)
        sleep(500)
        display.clear()


----

.. admonition:: Tasks

    #. Modify the microbit code so that after the first game, arrows to the A button and B button are shown to prompt the user to play another game.
    #. Add counters so that the total wins, losses and ties is scrolled after each game. e.g. 'W3 L2 T4'
    #. Use if-else after each game to ask to continue playing by pressing the A button or to exit by pressing the B button.
    #. Modify the display of the R, P or S to use custom images instead.
   

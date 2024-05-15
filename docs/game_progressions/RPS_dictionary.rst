====================================================
RPS dictionary
====================================================

Python Game design
--------------------

| This version of the game code uses a dictionary for the results.
| Each item in the dictionary has a key.
| Each key in the dictionary is a 2-tuple with the user choice first followed by the computer choice.
| There is a key for all nine possible combinations.
| Each item has a value indicating the winner or a tie.
| To look up the results dictionary use: ``winner = results.get(combo, 'invalid entry')``. This is able to handle the use of a key that does not exist.
| This is better than ``winner = results[combo]`` since if the user entry is not a proper choice, an error results.

.. code-block:: python

    import random

    results = {
        ('rock', 'rock'): 'tie',
        ('rock', 'paper'): 'computer',
        ('rock', 'scissors'): 'human',
        ('paper', 'rock'): 'human',
        ('paper', 'paper'): 'tie',
        ('paper', 'scissors'): 'computer',
        ('scissors', 'rock'): 'computer',
        ('scissors', 'paper'): 'human',
        ('scissors', 'scissors'): 'tie',
    }


    num_games = int(input('How many games would you like to play? '))

    for i in range(num_games):
        computer_move = random.choice(['scissors', 'paper', 'rock'])
        human_move = input('Type your move: rock, paper or scissors. ')
        results_key = (human_move, computer_move)

        print('Computer Played: ' + computer_move)
        print('Human Played: ' + human_move)
        # winner = results[combo]
        winner = results.get(results_key, 'invalid entry')
        if winner == 'invalid entry':
            print('invalid entry')
        elif winner == 'tie':
            print('Tie!')
        else:
            print(winner + ' wins')


----

.. admonition:: Tasks

    #. Modify the python code to use R, P or S instead of rock, paper or scissors throughout the code.
    #. Add counters so that the total wins, losses and draws is printed after each game in python.
    #. Modify the code to ask for a valid move from the use by placing the human move in a while loop and test to see if the move is a list or tuple of valid moves.
    
----

Microbit version
---------------------------------

| The Microbit version of the game code, using a dictionary for the results, is below.


.. code-block:: python

    from microbit import *
    import random


    results = {
        ('R', 'R'): 'tie',
        ('R', 'P'): 'computer',
        ('R', 'S'): 'human',
        ('P', 'R'): 'human',
        ('P', 'P'): 'tie',
        ('P', 'S'): 'computer',
        ('S', 'R'): 'computer',
        ('S', 'P'): 'human',
        ('S', 'S'): 'tie',
    }

    display.scroll('A for R   B for P   A&B for S', delay=80)

    while True:
        microbit_move = random.choice(['R', 'P', 'S'])
        while True:
            # short pause to allow time to hold down 2 buttons
            sleep(300)
            if button_a.is_pressed() and button_b.is_pressed():
                human_move = 'S'
                break
            elif button_a.is_pressed():
                human_move = 'R'
                break
            elif button_b.is_pressed():
                human_move = 'P'
                break

        display.scroll(human_move + ' v ' + microbit_move, delay=60)

        results_key = (human_move, microbit_move)
        winner = results.get(results_key, 'invalid entry')

        if winner == 'invalid entry':
            display.show(Image.MEH)
        if winner == 'tie': 
            display.show('=')
        elif winner == 'human':
            display.show(Image.YES)
        elif winner == 'computer':
            display.show(Image.NO)

        sleep(500)
        display.clear()

----

.. admonition:: Tasks

    #. Modify the microbit code so that after the first game, arrows to the A button and B button are shown to prompt the user to play another game.
    #. Add counters so that the total wins, losses and ties is scrolled after each game. e.g. 'W3 L2 T4'
    #. Use if-else after each game to ask to continue playing by pressing the A button or to exit by pressing the B button.
    #. Modify the display of the R, P or S to use custom images instead.


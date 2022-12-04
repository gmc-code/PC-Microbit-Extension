====================================================
Class Composition
====================================================

| See: https://www.geeksforgeeks.org/inheritance-and-composition-in-python/
| See: https://medium.com/swlh/the-best-way-to-understand-composition-in-python-5-case-studies-and-solution-4b23a6a2cc38

----

Composition
-----------------

| Composition models a has-a-relationship.
| Use composition to create components that can be reused by multiple classes.
| A composite class can be assigned to an instance variable.

----

Board Asteroid
-----------------

| In the code below, the composite class, Asteroid, is accessed via the self.asteroid1 and self.asteroid2 attribute of the Board class.

.. code-block:: python
        
    import random

    class Asteroid:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def move(self):
            self.y = self.y + 1
            if self.y == 5:
                self.y = 0
                self.x = random.randint(0, 4)

    class Board:
        def __init__(self):
            self.score = 0
            self.ship = Ship(2, 4)
            self.asteroid1 = Asteroid(random.randint(0, 4), 0)
            self.asteroid2 = Asteroid(random.randint(0, 4), 1)

        def get_board(self):
            self.board = []
            self.board.append((self.ship.x, self.ship.y))
            self.board.append((self.asteroid1.x, self.asteroid1.y))
            self.board.append((self.asteroid2.x, self.asteroid2.y))
            return self.board


    game_board = Board()
    print(game_board.get_board())


----

Board Asteroid Ship
---------------------

| In the code below, the composite class, Ship has been added so that it is accessed via the self.ship attribute of the Board class.

.. code-block:: python
        
    import random

    class Asteroid:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def move(self):
            self.y = self.y + 1
            if self.y == 5:
                self.y = 0
                self.x = random.randint(0, 4)

    class Ship:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def move(self):
            if button_a.was_pressed() and self.x != 0:
                self.x = self.x - 1
            elif button_b.was_pressed() and self.x != 4:
                self.x = self.x + 1

    class Board:
        def __init__(self):
            self.score = 0
            self.ship = Ship(2, 4)
            self.asteroid1 = Asteroid(random.randint(0, 4), 0)
            self.asteroid2 = Asteroid(random.randint(0, 4), 1)

        def get_board(self):
            self.board = []
            self.board.append((self.ship.x, self.ship.y))
            self.board.append((self.asteroid1.x, self.asteroid1.y))
            self.board.append((self.asteroid2.x, self.asteroid2.y))
            return self.board


    game_board = Board()
    print(game_board.get_board())


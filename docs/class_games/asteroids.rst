====================================================
Asteroids
====================================================


| Asteroids; based on http://www.multiwingspan.co.uk/micro.php?page=charlie2
| The game involves moving a ship, shown on the bottom row of the screen. 
| The other pixels represents an asteroid that is falling towards the ship. 
| The player moves the ship left or right by pressing the A & B buttons to avoid contact with an asteroid.

.. code-block:: python

    from microbit import *
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

        def draw_board(self):
            self.board = Image("00000:" * 5)
            self.board.set_pixel(self.ship.x, self.ship.y, 9)
            self.board.set_pixel(self.asteroid1.x, self.asteroid1.y, 5)
            self.board.set_pixel(self.asteroid2.x, self.asteroid2.y, 5)
            display.show(self.board)

        def update_board(self, asteroid_bool):
            self.ship.move()
            if asteroid_bool:
                self.asteroid1.move()
                self.asteroid2.move()
                
        def check_not_hit(self):
            if self.asteroid1.y == 4 and self.ship.x == self.asteroid1.x:
                return False
            if self.asteroid2.y == 4 and self.ship.x == self.asteroid2.x:
                return False
            return True
            
        def update_score(self, scoreup=1):
            self.score += scoreup

        def get_score(self):
            return self.score

    def PlayGame():
        game_board = Board()
        game_board.draw_board()
        
        playing = True
        game_speed = 200
        while playing:
            # move ship only
            for i in range(3):
                sleep(game_speed)
                game_board.update_board(False)
                game_board.draw_board()
            # move ship and asteroids
            sleep(game_speed)
            game_board.update_board(True)
            game_board.draw_board()
            playing = game_board.check_not_hit()
            if playing:
            game_board.update_score() 
            
        display.scroll(game_board.get_score())    



    while True:
        display.show(Image.ARROW_W)
        if button_a.was_pressed():
            PlayGame()
        sleep(500)


----

.. admonition:: Tasks

    #. Add sounds.
    #. Add a flashy start and end animation.
    #. Modify the code to speed up the game as the score increases.
    #. Modify the code to use more asteroids as the score increases.
    #. Modify the code to use levels with a screen indicating the new level.

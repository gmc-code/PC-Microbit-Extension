====================================================
Red Rain game
====================================================

Game
--------------------

.. code-block:: python

    from microbit import *

    # adapted from Red Rain by Matt Land, June 2016
    # A micro:bit game where the player blocks raindrops with an 'umbrella' paddle.
    # Move the paddle using buttons A and B. Block drops to score, miss five to lose!

    from microbit import *
    import random

    # Paddle sprites
    paddle_sprites = [
        "66000",  # Leftmost
        "06600",  # Center-left
        "00660",  # Center-right
        "00066",  # Rightmost
    ]
    paddle_position = 0  # Start paddle at the left

    def run_paddle():
        """Update paddle position based on button input."""
        global paddle_position
        if button_a.is_pressed() and paddle_position > 0:
            paddle_position -= 1
        if button_b.is_pressed() and paddle_position < 3:
            paddle_position += 1

    # Ball sprites
    ball_sprites = [
        "90000:",  # Left
        "09000:",  # Left-center
        "00900:",  # Center
        "00090:",  # Right-center
        "00009:",  # Right
    ]

    class ScoreState:
        """Handles scoring and level progression."""
        def __init__(self):
            self._hits = 0
            self._misses = 0
            self._level = 1
            self.time = 200  # Time delay for ball movement
            self.score = 0
            self._streak = 0

        def hit(self):
            """Register a hit and increase the score."""
            self._hits += 1
            self._streak += 1
            self.score += self._streak * self._level * 10
            display.show(Image.SQUARE)
            sleep(25)

        def miss(self):
            """Register a miss and reset the streak."""
            self._misses += 1
            self._streak = 0
            display.show(Image.NO)
            sleep(250)

        def level_complete(self):
            """Advance to the next level if the current one is complete."""
            if self._hits < 10:
                return
            display.show(Image.YES)
            sleep(300)
            display.clear()
            sleep(500)
            display.show(Image("00000:00000:00000:00000:00000"))  # Blank screen
            sleep(600)
            self._level += 1
            self.time = max(50, self.time - 2)  # Reduce time, with a minimum limit
            self._hits = self._misses = 0  # Reset for the new level
            display.scroll("Level {} Score {}".format(self._level, self.score), delay=75)

        def game_is_over(self):
            """Check if the game is over."""
            return self._misses >= 5

    class BallState:
        """Manages ball behavior and collisions."""
        def __init__(self, score):
            self._spawned = False
            self._direction = False
            self._column = 0
            self._row = 0
            self.score = score  # Assign the score object during initialization

        def _spawn(self):
            """Spawn a new ball at a random column."""
            if not self._spawned:
                self._column = random.randint(0, 4)
                self._row = -1  # Start above the display
                self._spawned = True
                self._direction = False  # Ball starts falling

        def _move(self):
            """Move the ball down or up based on its direction."""
            if not self._direction and self._row < 4:
                self._row += 1  # Move down
            elif self._direction and self._row >= 0:
                self._row -= 1  # Move up
            sleep(100)  # Add sleep to slow down each ball movement

        def _test_collision(self):
            """Check for collisions with the paddle."""
            if self._row == 4:  # Ball reaches the paddle row
                if self._column in [paddle_position, paddle_position + 1]:
                    self._hit()
                else:
                    self._miss()

        def _despawn(self):
            """Remove the ball if it leaves the screen."""
            if (not self._direction and self._row == 4) or (self._direction and self._row == -1):
                self._spawned = False

        def _hit(self):
            """Handle a successful hit."""
            self._direction = True  # Change direction to rising
            self.score.hit()

        def _miss(self):
            """Handle a missed ball."""
            self._despawn()
            self.score.miss()

        def run(self):
            """Main ball logic for movement and collision checks."""
            self._spawn()
            self._move()
            self._test_collision()
            self._despawn()

        def draw_field(self, row):
            """Draw the current row of the field."""
            if not self._spawned or row != self._row:
                return "00000:"
            return ball_sprites[self._column]

    # Initialize game state
    my_score = ScoreState()
    my_ball = BallState(my_score)  # Link the ball state with the score state

    # Main game loop
    while True:
        run_paddle()
        my_ball.run()
        field = [my_ball.draw_field(n) for n in range(4)]  # Create field rows
        field = "".join(field) + paddle_sprites[paddle_position]  # Add paddle
        image = Image(field)  # Generate image from the field
        display.show(image)
        my_score.level_complete()  # Check for level completion
        if my_score.game_is_over():  # End game if over
            break
        sleep(my_score.time)  # Adjust game speed
        # sleep(my_score.time + 50)  # Add an extra delay to slow things further

    # Display final score
    display.scroll("Game Over Score {}".format(my_score.score), loop=True, delay=100)

----

Red Rain Game Explanation
------------------------------

This is a game for the microbit where the player moves an 'umbrella' paddle at the bottom of the LED matrix using the A and B buttons. Raindrops fall from the top of the LED matrix and can be blocked by the paddle. The game increases in speed after each level. The player must block ten raindrops to complete a level and avoid missing five drops, which ends the game. Scoring is based on successful blocks, with points awarded for streaks of consecutive blocks.

Imports and Initialization
--------------------------

.. code-block:: python

    from microbit import *
    import random

----

Paddle Sprites and Position
---------------------------

.. code-block:: python

    paddle_sprites = [
        "66000",  # Leftmost
        "06600",  # Center-left
        "00660",  # Center-right
        "00066",  # Rightmost
    ]
    paddle_position = 0  # Start paddle at the left

- **Paddle Sprites**: Defines the visual representation of the paddle in different positions.
- **Paddle Position**: Initializes the paddle's starting position.

----

Paddle Movement Function
------------------------

.. code-block:: python

    def run_paddle():
        """Update paddle position based on button input."""
        global paddle_position
        if button_a.is_pressed() and paddle_position > 0:
            paddle_position -= 1
        if button_b.is_pressed() and paddle_position < 3:
            paddle_position += 1

- **run_paddle**: Updates the paddle's position based on button A and B inputs.

----

Ball Sprites
------------
.. code-block:: python

    ball_sprites = [
        "90000:",  # Left
        "09000:",  # Left-center
        "00900:",  # Center
        "00090:",  # Right-center
        "00009:",  # Right
    ]

- **Ball Sprites**: Defines the visual representation of the ball in different columns.

----

ScoreState Class
----------------

.. code-block:: python

    class ScoreState:
        """Handles scoring and level progression."""
        def __init__(self):
            self._hits = 0
            self._misses = 0
            self._level = 1
            self.time = 200  # Time delay for ball movement
            self.score = 0
            self._streak = 0

        def hit(self):
            """Register a hit and increase the score."""
            self._hits += 1
            self._streak += 1
            self.score += self._streak * self._level * 10
            display.show(Image.SQUARE)
            sleep(25)

        def miss(self):
            """Register a miss and reset the streak."""
            self._misses += 1
            self._streak = 0
            display.show(Image.NO)
            sleep(250)

        def level_complete(self):
            """Advance to the next level if the current one is complete."""
            if self._hits < 10:
                return
            display.show(Image.YES)
            sleep(300)
            display.clear()
            sleep(500)
            display.show(Image("00000:00000:00000:00000:00000"))  # Blank screen
            sleep(600)
            self._level += 1
            self.time = max(50, self.time - 2)  # Reduce time, with a minimum limit
            self._hits = self._misses = 0  # Reset for the new level
            display.scroll("Level {} Score {}".format(self._level, self.score), delay=75)

        def game_is_over(self):
            """Check if the game is over."""
            return self._misses >= 5

- **ScoreState**: Manages the game's scoring, level progression, and game-over conditions.
  - **hit**: Increments hits and score.
  - **miss**: Increments misses and resets the streak.
  - **level_complete**: Advances to the next level if the player has enough hits.
  - **game_is_over**: Checks if the game should end based on the number of misses.

----

BallState Class
---------------

.. code-block:: python

    class BallState:
        """Manages ball behavior and collisions."""
        def __init__(self, score):
            self._spawned = False
            self._direction = False
            self._column = 0
            self._row = 0
            self.score = score  # Assign the score object during initialization

        def _spawn(self):
            """Spawn a new ball at a random column."""
            if not self._spawned:
                self._column = random.randint(0, 4)
                self._row = -1  # Start above the display
                self._spawned = True
                self._direction = False  # Ball starts falling

        def _move(self):
            """Move the ball down or up based on its direction."""
            if not self._direction and self._row < 4:
                self._row += 1  # Move down
            elif self._direction and self._row >= 0:
                self._row -= 1  # Move up
            sleep(100)  # Add sleep to slow down each ball movement

        def _test_collision(self):
            """Check for collisions with the paddle."""
            if self._row == 4:  # Ball reaches the paddle row
                if self._column in [paddle_position, paddle_position + 1]:
                    self._hit()
                else:
                    self._miss()

        def _despawn(self):
            """Remove the ball if it leaves the screen."""
            if (not self._direction and self._row == 4) or (self._direction and self._row == -1):
                self._spawned = False

        def _hit(self):
            """Handle a successful hit."""
            self._direction = True  # Change direction to rising
            self.score.hit()

        def _miss(self):
            """Handle a missed ball."""
            self._despawn()
            self.score.miss()

        def run(self):
            """Main ball logic for movement and collision checks."""
            self._spawn()
            self._move()
            self._test_collision()
            self._despawn()

        def draw_field(self, row):
            """Draw the current row of the field."""
            if not self._spawned or row != self._row:
                return "00000:"
            return ball_sprites[self._column]

- **BallState**: Manages the ball's spawning, movement, collision detection, and despawning.
  - **_spawn**: Spawns a new ball at a random column.
  - **_move**: Moves the ball down or up based on its direction.
  - **_test_collision**: Checks if the ball collides with the paddle.
  - **_despawn**: Removes the ball if it leaves the screen.
  - **_hit**: Handles a successful hit.
  - **_miss**: Handles a missed ball.
  - **run**: Executes the main ball logic.
  - **draw_field**: Draws the current row of the field.

----

Game Initialization and Main Loop
---------------------------------

.. code-block:: python

    # Initialize game state
    my_score = ScoreState()
    my_ball = BallState(my_score)  # Link the ball state with the score state

    # Main game loop
    while True:
        run_paddle()
        my_ball.run()
        field = [my_ball.draw_field(n) for n in range(4)]  # Create field rows
        field = "".join(field) + paddle_sprites[paddle_position]  # Add paddle
        image = Image(field)  # Generate image from the field
        display.show(image)
        my_score.level_complete()  # Check for level completion
        if my_score.game_is_over():  # End game if over
            break
        sleep(my_score.time)  # Adjust game speed
        # sleep(my_score.time + 50)  # Add an extra delay to slow things further

    # Display final score
    display.scroll("Game Over Score {}".format(my_score.score), loop=True, delay=100)


- **Initialization**: Creates instances of `ScoreState` and `BallState`, linking them together.
- **Main Loop**: Runs the game loop, updating the paddle position, ball state, and display. Checks for level completion and game-over conditions, adjusting the game speed accordingly.
- **Final Score Display**: Displays the final score when the game ends.


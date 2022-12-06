====================================================
Lights Out
====================================================

| Lights Out; See http://www.multiwingspan.co.uk/micro.php?page=lights

| The game below is an easier version of the the original.

----

Bitwise operations to reverse 0 and 1
-------------------------------------------------

| The on/off lights are stored as a 2D list of 1s and 0s. 
| In order to make the moves, the XOR operator, ^, is used. 
| The bitwise xor operator returns 1 if the bits are different; 0 if the same.
| Note, bitwise operations on integers convert the integers to binary, carry out the bitwise operation, convert the binary number back to an integer and retrun the integer.

| The code below shows the different possible results from using the bitwise XOR, ^, and the assignment operator, ^=, for 0s and 1s.

.. code-block:: python

    print(0 ^ 0)  # 0
    print(0 ^ 1)  # 1
    print(1 ^ 0)  # 1
    print(1 ^ 1)  # 0

    x = 0
    x ^= 0
    print(x)  # 0
    x = 0
    x ^= 1
    print(x)  # 1
    x = 1
    x ^= 0
    print(x)  # 1
    x = 1
    x ^= 1
    print(x)  # 0

----

Grid referencing
-------------------

| A grid, where each pixel is referenced using the x and y coordinates, makes it easy to change the pixels relative to the player pixel, (x, y).
| In the grid code below, each pixel is referenced by ``grid[x][y]``.
| In the grid array below, the first column in grid[0].

.. code-block:: python

    grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]


----

Lights Out Outline
-------------------

.. admonition:: Tasks

    #. Here is the outline to the Lights Out code. The game loop has been provided. See if you can write code for each method in the classes to get the game working. SOme of the key code has been kept. Comments guide you to the rest of what is needed.


.. code-block:: python

    from microbit import *
    import random


    class LightsOut:
        def __init__(self, tilt_sensitivity=300, tilt_delay=400, x=2, y=2)
            # initialize the parameters
            # set the brightness and the grid

        def ToggleX(self, tx=None, ty=None):
            """toggle all in same row"""
            if tx is None:
                tx = self.x
            if ty is None:
                ty = self.y
            # toggle the pixles in the row

        def ToggleY(self, tx=None, ty=None):
            """toggle all in same column"""
            if tx is None:
                tx = self.x
            if ty is None:
                ty = self.y
            # toggle the pixels in the column

        def ToggleXY(self, tx=None, ty=None):
            """toggle all in same row and all in same column"""
            if tx is None:
                tx = self.x
            if ty is None:
                ty = self.y
            # toggle the pixles in the row
            # toggle the pixels in the column

        def RandomGrid(self):
            #staring with random x and random y pixels use ToggleXY a random number of times from 4 to 30


        def DrawGame(self):
            """Add pixels from grid one at a time at brightness, gb, of 3
            b is 0 or 9, player pixel will be 0 or 9 if pixel not in grid, or 7 or 9 is in self.grid.
            """
            gb = 3
            img = Image("00000:" * 5)
            # set pixels brightenss in img from grid
            # add player pixel depending on whetehr b is 0 or 9, player pixel will be 0 or 9 if pixel not in grid, or 7 or 9 is in self.grid
            # display image and sleep for tilt_delay

        def CheckWin(self):
            """Return True if all points in grid are 0"""
            tot = 0
            # add grid values
            # Return True if all points in grid are 0; or False if not

        def MovePlayer(self):
            '''alternate between 0 and 9 for brightness'''
            self.brightness = 9 - self.brightness
            dx = accelerometer.get_x()
            dy = accelerometer.get_y()
            # move based on dx and dy
            # keep on grid



    game = LightsOut(tilt_sensitivity=300, tilt_delay=400, x=2, y=2)
    game.RandomGrid()

    playing = True
    while playing:
        game.MovePlayer()
        game.DrawGame()
        if button_a.was_pressed():
            game.ToggleX()
            game.DrawGame()
        elif button_b.was_pressed():
            game.ToggleY()
            game.DrawGame()
        if game.CheckWin():
            playing = False
            sleep(500)
            for w in range(0, 3):
                display.show(Image.HAPPY)
                sleep(300)
                display.clear()
                sleep(300)


----


Working code
-------------------------------

| The working code is below.

.. code-block:: python

    from microbit import *
    import random


    class LightsOut:
        def __init__(self):
            self.tilt_sensitivity = 300
            self.tilt_delay = 400
            self.x = 2
            self.y = 2
            self.brightness = 0
            """grid[tx][ty]; the grid array has the first column in grid[0]"""
            self.grid = [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]

        def Toggle5(self, tx=None, ty=None):
            """For original game only; toggle all 5 points, if they exist, above, below and to the sides of a point"""
            if tx is None:
                tx = self.x
            if ty is None:
                ty = self.y
            self.grid[tx][ty] ^= 1
            if tx > 0:
                self.grid[tx - 1][ty] ^= 1
            if tx < 4:
                self.grid[tx + 1][ty] ^= 1
            if ty > 0:
                self.grid[tx][ty - 1] ^= 1
            if ty < 4:
                self.grid[tx][ty + 1] ^= 1

        def ToggleX(self, tx=None, ty=None):
            """toggle all in same row"""
            if tx is None:
                tx = self.x
            if ty is None:
                ty = self.y
            for x in range(5):
                self.grid[x][ty] ^= 1

        def ToggleY(self, tx=None, ty=None):
            """toggle all in same column"""
            if tx is None:
                tx = self.x
            if ty is None:
                ty = self.y
            for y in range(5):
                self.grid[tx][y] ^= 1

        def ToggleXY(self, tx=None, ty=None):
            """toggle all in same row and all in same column"""
            if tx is None:
                tx = self.x
            if ty is None:
                ty = self.y
            for x in range(5):
                self.grid[x][ty] ^= 1
            for y in range(5):
                self.grid[tx][y] ^= 1

        def RandomGrid(self):
            """use ToggleXY a random number of times from 4 to 30"""
            # use ToggleXY at random pixels 4 to 30 times

        def DrawGame(self):
            """Add pixels from grid one at a time at brightness, gb, of 3.
            b is 0 or 9, player pixel will be 0 or 9 if pixel not in grid, or 7 or 9 is in self.grid.
            """
            gb = 3
            img = Image("00000:" * 5)
            for cy in range(0, 5):
                for cx in range(0, 5):
                    img.set_pixel(cx, cy, self.grid[cx][cy] * gb)
            # add player pixel
            if img.get_pixel(self.x, self.y) == gb:
                if self.brightness == 0:
                    img.set_pixel(self.x, self.y, 7)
                else:
                    img.set_pixel(self.x, self.y, self.brightness)
            else:
                img.set_pixel(self.x, self.y, self.brightness)
            # return img
            display.show(img)
            sleep(self.tilt_delay)

        def CheckWin(self):
            """Return True if all all points in grid are 0.
            Also can do: print(sum([sum(i) for i in grid]))
            """
            tot = 0
            for cy in range(0, 5):
                for cx in range(0, 5):
                    tot += self.grid[cx][cy]
            if tot == 0:
                return True
            else:
                return False

        def MovePlayer(self):
            '''alternate between 0 and 9 for brightness'''
            self.brightness = 9 - self.brightness
            dx = accelerometer.get_x()
            dy = accelerometer.get_y()
            if dx > self.tilt_sensitivity:
                self.x += 1
            if dx < -self.tilt_sensitivity:
                self.x -= 1
            if dy > self.tilt_sensitivity:
                self.y += 1
            if dy < -self.tilt_sensitivity:
                self.y -= 1
            # keep on grid
            self.x = max(0, min(self.x, 4))
            self.y = max(0, min(self.y, 4))


    game = LightsOut()
    game.RandomGrid()

    playing = True
    while playing:
        game.MovePlayer()
        game.DrawGame()
        if button_a.was_pressed():
            game.ToggleX()
            game.DrawGame()
        elif button_b.was_pressed():
            game.ToggleY()
            game.DrawGame()
        if game.CheckWin():
            playing = False
            sleep(500)
            for w in range(0, 3):
                display.show(Image.HAPPY)
                sleep(300)
                display.clear()
                sleep(300)


----


How To Beat The Original Game
-------------------------------

| The original game is a puzzle game that takes many moves to solve.
| The original code used toggling of the 5 pixels in a cross shape and is included below for reference.

.. code-block:: python

    from microbit import *
    import random

    def Toggle5(self, tx=None, ty=None):
        """For original game only; toggle all 5 points, if they exist, above, below and to the sides of a point"""
        if tx is None:
            tx = self.x
        if ty is None:
            ty = self.y
        self.grid[tx][ty] ^= 1
        if tx > 0:
            self.grid[tx - 1][ty] ^= 1
        if tx < 4:
            self.grid[tx + 1][ty] ^= 1
        if ty > 0:
            self.grid[tx][ty - 1] ^= 1
        if ty < 4:
            self.grid[tx][ty + 1] ^= 1

| Jaap Scherphuis explained the solution on his site at http://www.jaapsch.net/puzzles/lights.htm.

| Stage 1 - Chase The Lights
| Start at the top row. For every light that is on, select the light beneath it. Do this with the next 4 rows. If you are really lucky, this will solve the puzzle. If not, there will be a couple of lights on the bottom row and stage 2 and 3 will need to be done.

| Stage 2 - Set Up For The Win
| Look at the first 3 LEDs on the bottom row.
| If LED(0, 4) is on, press LED(3, 0) and LED(4, 0). These are the 4th and 5th lights of the top row.
| If LED(1, 4) is on, press LED(1, 0) and LED(4, 0). These are the 2nd and 5th lights of the top row.
| If LED(2, 4) is on, press LED(3, 0). This is the 4th light on the top row.

| Stage 3 - Chase The Lights Again
| Repeat the chase the lights process again with the lights that are now on. By the time you get to the bottom row, the lights should all be out and you win.

====================================================
Lights Out
====================================================

| Lights Out; see http://www.multiwingspan.co.uk/micro.php?page=lights

| The on/off lights are stored as a 2D list of 1s and 0s. 
| In order to make the moves, the XOR operator is used. 
| Bitwise xor operator: Returns 1 if the bits are different; 0 if the same.
| If we do XOR with 1, this will make a 1 into a 0.
| If we do XOR with 1, this will make a 0 into a 1.

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

| A grid, where each pixel is referenced using the x and y coordinates, makes it each to change the pixels around another pixel, (x, y).

----

How To Beat The Game
--------------------------

Jaap Scherphuis explained the solution on his site at http://www.jaapsch.net/puzzles/lights.htm.

Stage 1 - Chase The Lights
Satrt at the top row. For every light that is on, select the light beneath it. Do this with the next 4 rows. If you are really lucky, this will solve the puzzle. If not, there will be a couple of lights on the bottom row and stage 2 and 3 will need to be done.

Stage 2 - Set Up For The Win
Look at the first 3 LEDs on the bottom row.
If LED(0,4) is on, press LED(3,0) and LED(4,0). These are the 4th and 5th lights of the top row.
If LED(1,4) is on, press LED(1,0) and LED(4,0). These are the 2nd and 5th lights of the top row.
If LED(2,4) is on, press LED(3,0). This is the 4th light on the top row.

Stage 3 - Chase The Lights Again
Repeat the chase the lights process again with the lights that are now on. By the time you get to the bottom row, the lights should all be out and you win.


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

        def Toggle(self, tx=None, ty=None):
            """toggle all 4 points, if they exist, above, below and to the sides of a point"""
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

        def RandomGrid(self):
            """toggle 50 random points"""
            for r in range(0, 50):
                cx = random.randint(0, 4)
                cy = random.randint(0, 4)
                self.Toggle(cx, cy)

        def DrawGame(self):
            """Add pixels from grid one at a time at brightness, gb,  of 4
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
            """Return True if all all points in grid are 0"""
            tot = 0
            for cy in range(0, 5):
                for cx in range(0, 5):
                    tot += self.grid[cx][cy]
            if tot == 0:
                return True
            else:
                return False

        def MovePlayer(self):
            # alternate between 0 and 9 for brightness
            self.brightness = 9 - self.brightness
            # check for movement
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
    # set the board up for a game
    game.RandomGrid()

    playing = True
    while playing:
        game.MovePlayer()
        # update screen
        game.DrawGame()
        # check for button press
        if button_a.was_pressed() or button_b.was_pressed():
            game.Toggle()
            sleep(200)
            # update screen
            game.DrawGame()
        # check for win
        if game.CheckWin():
            playing = False
            sleep(1000)
            for w in range(0, 6):
                display.show(Image.HAPPY)
                sleep(500)
                display.clear()
                sleep(500)

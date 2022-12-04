====================================================
Lights Out
====================================================


| Lights Out; see http://www.multiwingspan.co.uk/micro.php?page=lights

In order to make the moves, the XOR operator is used. The on/off lights are stored as a 2D list of 1s and 0s. If we do XOR with 1, this will make a 1 into a 0 and a 0 into a 1.

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

    x = 2
    y = 2
    tick = -1

    grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    # A 'move' in Lights Out
    def Toggle(tx, ty):
        grid[tx][ty] ^= 1
        if tx > 0:
            grid[tx - 1][ty] ^= 1
        if tx < 4:
            grid[tx + 1][ty] ^= 1
        if ty > 0:
            grid[tx][ty - 1] ^= 1
        if ty < 4:
            grid[tx][ty + 1] ^= 1


    def RandomGrid():
        for r in range(0, 50):
            cx = random.randint(0, 4)
            cy = random.randint(0, 4)
            Toggle(cx, cy)


    def DrawGame(t):
        img = Image("00000:" * 5)
        for cy in range(0, 5):
            for cx in range(0, 5):
                img.set_pixel(cx, cy, grid[cx][cy] * 5)
        img.set_pixel(x, y, (t % 2) * 9)
        return img


    def CheckWin():
        tot = 0
        for cy in range(0, 5):
            for cx in range(0, 5):
                tot += grid[cx][cy]
        if tot == 0:
            return True
        else:
            return False


    # set the board up for a game
    RandomGrid()
    tilt_sensitivity = 300
    tilt_delay = 500
    while True:
        tick += 1
        if tick == 4:
            tick = 0
        # check for movement
        dx = accelerometer.get_x()
        dy = accelerometer.get_y()
        if dx > tilt_sensitivity:
            x += 1
            sleep(tilt_delay)
        if dx < -tilt_sensitivity:
            x -= 1
            sleep(tilt_delay)
        if dy > tilt_sensitivity:
            y += 1
            sleep(tilt_delay)
        if dy < -tilt_sensitivity:
            y -= 1
            sleep(tilt_delay)
        # keep on grid
        x = max(0, min(x, 4))
        y = max(0, min(y, 4))
        sleep(50)
        # check for button press
        if button_a.was_pressed():
            Toggle(x, y)
            sleep(200)
        # update screen
        i = DrawGame(tick)
        display.show(i)
        if CheckWin():
            sleep(1000)
            for w in range(0, 6):
                display.show(Image.HAPPY)
                sleep(500)
                display.clear()
                sleep(500)
            RandomGrid()
            x = 2
            y = 2
            i = DrawGame(tick)
        sleep(400)

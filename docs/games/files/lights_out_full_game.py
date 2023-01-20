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
        """toggle 50 random points"""
        for r in range(0, random.randint(4, 30)):
            cx = random.randint(0, 4)
            cy = random.randint(0, 4)
            self.ToggleXY(cx, cy)

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
    if button_a.was_pressed():
        game.ToggleX()
        sleep(200)
        # update screen
        game.DrawGame()
    elif button_b.was_pressed():
        game.ToggleY()
        sleep(200)
        # update screen
        game.DrawGame()
    # check for win
    if game.CheckWin():
        playing = False
        sleep(500)
        for w in range(0, 3):
            display.show(Image.HAPPY)
            sleep(300)
            display.clear()
            sleep(300)

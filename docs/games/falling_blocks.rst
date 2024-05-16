====================================================
Falling blocks
====================================================


| Falling blocks based on https://www.101computing.net/bbc-microbit-tetris-game/
| For V2 microbit
| Move left and right with A and B buttons
| Rotate with A and B together


.. code-block:: python

    from microbit import *
    from random import choice
    import music


    class TetrisGrid:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.grid = self.create_grid(self.width, self.height)

        @staticmethod
        def create_grid(width, height):
            # x -1 to width -1; y -2 to width -2;
            grid = {(x, y): 0 for y in range(-2, height - 2) for x in range(-1, width - 1)}
            # put 1 in sides
            grid_edge = {(x, y): 1 for y in range(-2, height - 2) for x in (-1, width - 2)}
            grid.update(grid_edge)
            # put 1 in bottom
            grid_edge = {(x, height - 3): 1 for x in range(-1, width - 1)}
            grid.update(grid_edge)
            return grid


    class TetrisBlock:
        bricks = [[9, 9, 9, 0], [9, 9, 0, 9], [9, 9, 9, 9], [9, 9, 0, 0]]

        def __init__(self, x=2, y=-2):
            # x is start pos of top left; 1 to 4 for width = 7
            self.x = x
            self.y = y

        def create_block(self):
            # top left of block at x, y; block row 1 then row 2 left to right
            brick = choice(self.bricks)
            block = {}
            index = 0
            for y0 in range(2):
                for x0 in range(2):
                    block[(x0 + self.x, y0 + self.y)] = brick[index]
                    index += 1
            return block


    class TetrisBoard:
        def __init__(self, width=7, height=8, block_score=1, line_score=5):
            self.do_start_game_message()
            self.width = width
            self.height = height
            self.block_score = block_score
            self.line_score = line_score
            tetris_grid = TetrisGrid(width, height)
            self.grid = tetris_grid.grid
            self.new_block()
            self.run_game()

        def do_start_game_message(self):
            display.scroll("go", delay=80)

        def new_block(self):
            self.block_top_x = 2
            self.block_left_y = -2
            tetris_block = TetrisBlock(self.block_top_x, self.block_left_y)
            self.block = tetris_block.create_block()
            self.new_block = {}
            self.show_block()

        def get_block_top_left(self):
            x_vals = {x for x, y in self.block.keys()}
            y_vals = {y for x, y in self.block.keys()}
            self.block_top_x = min(x_vals)
            self.block_left_y = min(y_vals)

        def show_block(self):
            # can't just display all 4 parts,
            # need to take into account previous blocks on grid
            for (x, y) in self.block.keys():
                if -1 < x < 5 and -1 < y < 5:
                    display.set_pixel(x, y, max(self.block[(x, y)], self.grid[(x, y)]))

        def hide_block(self):
            # keep previous blocks on grid
            for (x, y) in self.block.keys():
                if -1 < x < 5 and -1 < y < 5:
                    display.set_pixel(x, y, self.grid[(x, y)])

        # A function to rotate the 2x2 brick
        def get_rotate_block(self):
            # clockwise order
            k00 = self.block[(self.block_top_x, self.block_left_y)]
            k01 = self.block[(self.block_top_x + 1, self.block_left_y)]
            k11 = self.block[(self.block_top_x + 1, self.block_left_y + 1)]
            k10 = self.block[(self.block_top_x, self.block_left_y + 1)]
            self.new_block = {}
            self.new_block[(self.block_top_x, self.block_left_y)] = k10
            self.new_block[(self.block_top_x + 1, self.block_left_y)] = k00
            self.new_block[(self.block_top_x + 1, self.block_left_y + 1)] = k01
            self.new_block[(self.block_top_x, self.block_left_y + 1)] = k11

        def rotate_block(self):
            self.get_rotate_block()
            if self.can_move_block():
                self.do_block_move()

        def get_move_block(self, delta_x, delta_y):
            self.new_block = {}
            for (x, y) in self.block.keys():
                self.new_block[(x + delta_x, y + delta_y)] = self.block[(x, y)]

        def move_block(self, delta_x=0, delta_y=0):
            self.get_move_block(delta_x, delta_y)
            if self.can_move_block():
                self.do_block_move()

        def do_block_move(self):
            self.hide_block()
            self.block = {k: v for k, v in self.new_block.items()}
            self.show_block()
            self.get_block_top_left()

        def can_move_block(self):
            for k, v in self.new_block.items():
                if self.new_block[k] > 0 and self.grid[k] > 0:
                    return False
            return True

        def drop_block(self, delta_y=1):
            self.get_move_block(0, delta_y)
            can_move_block = self.can_move_block()
            if can_move_block:
                self.do_block_move()
            else:
                self.add_block_to_grid()
                self.score += self.block_score
                if self.is_game_over():
                    self.do_game_over()
                else:
                    music.play(["C4:1"])
                    self.clear_lines_of_grid()
                    self.new_block()

        def add_block_to_grid(self):
            # can only each if value is 9
            dict_to_include = {k: v for k, v in self.block.items() if v == 9}
            self.grid.update(dict_to_include)

        def is_game_over(self):
            if self.block_left_y < 0:
                self.gameOn = False
                return True
            else:
                return False

        def do_game_over(self):
            # End of Game
            sleep(1000)
            display.scroll("Game Over: Score: " + str(self.score), delay=80)

        def clear_lines_of_grid(self):
            # check each line one at a time from y=0 to y = 4
            for y in range(0, 5):
                removeLine = True
                for x in range(0, 5):
                    if self.grid[(x, y)] != 9:
                        removeLine = False
                if removeLine:
                    music.play(["E5:2"])
                    self.score += self.line_score
                    # Remove the line and make all lines above fall by 1:
                    for y2 in range(y, -1, -1):
                        for x in range(0, 5):
                            self.grid[(x, y2)] = self.grid[(x, y2 - 1)]
            # Refresh the LED screen
            for x in range(0, 5):
                for y in range(0, 5):
                    display.set_pixel(x, y, self.grid[(x, y)])

        def run_game(self):
            self.gameOn = True
            self.score = 0
            frame_time = 100  # 200
            frameCount = 0
            while self.gameOn:
                sleep(frame_time)
                frameCount += 1
                if button_a.is_pressed() and button_b.is_pressed():
                    self.rotate_block()
                elif button_a.is_pressed():
                    self.move_block(-1)
                elif button_b.is_pressed():
                    self.move_block(1)
                # Every 10 frames try to move the brick down
                if frameCount == 10:
                    frameCount = 0
                    self.drop_block(1)


    while True:
        game = TetrisBoard(block_score=1, line_score=5)
        sleep(2000)
        if button_a.is_pressed() or button_b.is_pressed():
            continue
        else:
            break




----

.. admonition:: Tasks

    #. Modify the code to set the frame_time parameter when the class is initialized.
    #. Use A and B button pressing to play 2 different versions of the game, using different frame_time parameters using code from in task 1. Have A play a slow game, and B a faster game.



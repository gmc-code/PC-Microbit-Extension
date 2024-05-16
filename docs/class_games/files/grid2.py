# Tetris grid2
import matplotlib.pyplot as plt
import numpy as np


class Grid:
    """grid to illustrate microbit coordinates for game"""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self.create_grid(self.width, self.height)

    @staticmethod
    def create_grid(width, height):
        # x -1 to width -1; y -2 to width -2;
        # put 0 in grid to start with, dictionary order maintained row by row
        grid = {(x, y): 0 for y in range(-2, height - 2) for x in range(-1, width - 1)}
        # put 1 in sides
        grid_edge = {(x, y): 1 for y in range(-2, height - 2) for x in (-1, width - 2)}
        grid.update(grid_edge)
        # put 1 in bottom
        grid_edge = {(x, height - 3): 1 for x in range(-1, width - 1)}
        grid.update(grid_edge)
        return grid


game = Grid(7, 8)
dict_items = game.grid
print(game.grid)


def getx(dict_items):
    x_vals = [k[0] for k in dict_items.keys()]
    return x_vals


x_vals = getx(dict_items)


def gety(dict_items):
    y_vals = [k[1] for k in dict_items.keys()]
    return y_vals


y_vals = gety(dict_items)


def get_points(dict_items):
    p_vals = [k for k in dict_items.keys()]
    return p_vals


p_vals = get_points(dict_items)


def getc(dict_items, width=7):
    c_vals = [[0, 1, 0] if k == 0 else [0, 0, 1] for k in dict_items.values()]
    # modify c_vals; x from 0 to 4, y <0
    # top middle red
    for y in range(2):
        for x in range(1, width - 1):
            c_vals[(y * width) + x] = [1, 0, 0]
    return c_vals


c_vals = getc(dict_items, width=7)

xa = np.array(x_vals)
ya = np.array(y_vals)
ca = np.array(c_vals)

plt.gca().invert_yaxis()
plt.gca().xaxis.tick_top()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.scatter(xa, ya, s=10, color=ca)
plt.title("Tetris grid", fontsize=18)
for x, y in zip(xa, ya):
    label = f"({x},{y})"
    plt.annotate(
        label,  # this is the text
        (x, y),  # these are the coordinates to position the label
        textcoords="offset points",  # how to position the text
        xytext=(0, -10),  # distance from text to points (x,y)
        ha="center",
    )  # horizontal alignment can be left, right or center

# plt.show()
plt.savefig("tetris_grid2.png", bbox_inches="tight")

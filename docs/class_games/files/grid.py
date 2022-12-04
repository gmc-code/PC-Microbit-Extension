# Tetris grid

import matplotlib.pyplot as plt
import numpy as np


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self.create_grid(self.width, self.height)

    @staticmethod
    def create_grid(width, height):
        # put 0 in grid to start with
        grid = {(x, y): 0 for x in range(width) for y in range(height)}
        # put 1 in sides
        gridedge = {(x, y): 1 for x in (0, width - 1) for y in range(height)}
        grid.update(gridedge)
        # put 1 in bottom
        gridedge = {(x, height-1): 1 for x in range(width)}
        grid.update(gridedge)
        return grid


game = Grid(7, 6)
dict_items = game.grid


def getx(dict_items):
    xvals = [k[0] for k in dict_items.keys()]
    return xvals


xvals = getx(dict_items)


def gety(dict_items):
    yvals = [k[1] for k in dict_items.keys()]
    return yvals


yvals = gety(dict_items)


def getpoints(dict_items):
    pvals = [k for k in dict_items.keys()]
    return pvals


pvals = getpoints(dict_items)


def getc(dict_items):
    cvals = [[1, 0, 0] if k == 0 else [0, 0, 1] for k in dict_items.values()]
    return cvals


cvals = getc(dict_items)

xa = np.array(xvals)
ya = np.array(yvals)
ca = np.array(cvals)

plt.gca().invert_yaxis()
plt.gca().xaxis.tick_top()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.scatter(xa, ya, s=10, color=ca)
plt.title("Tetris grid", fontsize=18)
for x, y in zip(xa, ya):
    label = f"({x},{y})"
    plt.annotate(label,  # this is the text
                 (x, y),  # these are the coordinates to position the label
                 textcoords="offset points",  # how to position the text
                 xytext=(0, -10),  # distance from text to points (x,y)
                 ha='center')  # horizontal alignment can be left, right or center

#plt.show()
plt.savefig('tetris_grid.png', bbox_inches='tight')

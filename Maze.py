import numpy as np
import random
from matplotlib import pyplot as plt


def random_square(maze):
    x, y = random.randint(1, maze.shape[0] - 2), random.randint(1, maze.shape[0] - 2)
    return [x, y]


def display_maze(maze):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    im = ax.pcolor(maze)
    plt.show(block=False)


class Maze:
    def __init__(self, size):
        self._generate_maze(size)
        self.exitPos = random_square(self.maze)
        self.maze[self.exitPos[0], self.exitPos[1]] = 2

    def value_at_point(self, position):
        return self.maze[position[0], position[1]]

    def set_value_at_point(self, position, value):
        self.maze[position[0], position[1]] = value

    def _generate_maze(self, size):
        base = np.zeros((size, size))
        base[:, 0] = 1
        base[0, :] = 1
        base[-1, :] = 1
        base[:, -1] = 1
        self.maze = base

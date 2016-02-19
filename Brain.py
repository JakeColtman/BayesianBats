import numpy as np


class Brain:
    def __init__(self, maze):
        self.maze = maze
        self.belief = np.zeros(maze.maze.shape)

    def accept_information(self, information):
        raise NotImplementedError()

    def determine_direction(self):
        raise NotImplementedError()

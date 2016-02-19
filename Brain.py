import numpy as np


class Brain:
    def __init__(self, maze):
        self.maze = maze
        self.belief = np.zeros(maze.maze.shape)
        self.informationCache = []

    def accept_information(self, information):
        self.informationCache.append(information)
        return True

    def determine_direction(self):
        raise NotImplementedError()

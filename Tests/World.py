from Brain import Brain
from Maze import Maze
from RoboBat import RoboBat


class World:
    def __init__(self, mazeSize):
        self.maze = Maze(mazeSize)
        self.brain = Brain(self.maze)
        self.robobat = RoboBat(self.maze, [1, 1], self.brain)

    def solve(self):
        while self.robobat.pos != self.maze.exitPos:
            self.robobat.move_in_direction(self.brain.determine_direction())

        print("solved")


world = World(5)
world.solve()

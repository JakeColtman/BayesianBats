import unittest
from Brain import Brain
from Maze import Maze


class TestBrainSetup(unittest.TestCase):
    def test_brain_starts_with_correct_representation(self):
        maze = Maze(3)
        brain = Brain(maze)
        self.assertEqual(brain.belief.shape, maze.maze.shape)

    def test_brain_adds_new_information(self):
        maze = Maze(3)
        brain = Brain(maze)
        prevLength = len(brain.informationCache)
        brain.accept_information([1,2,3,4])
        newLength = len(brain.informationCache)
        self.assertEqual(prevLength + 1, newLength)

if __name__ == '__main__':
    unittest.main()

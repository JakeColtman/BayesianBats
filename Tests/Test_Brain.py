import unittest
from Brain import Brain
from Maze import Maze


class TestBrainSetup(unittest.TestCase):
    def test_brain_starts_with_correct_representation(self):
        maze = Maze(3)
        brain = Brain(maze)
        self.assertEqual(brain.belief.shape, maze.maze.shape)


if __name__ == '__main__':
    unittest.main()

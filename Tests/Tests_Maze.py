import unittest
import random
from Maze import Maze


class MazeAssignmentAndGet(unittest.TestCase):
    def test_maze_assign_and_get(self):
        maze = Maze(5)
        new_val = random.randint(1, 6)
        maze.set_value_at_point([1, 3], new_val)
        self.assertEqual(new_val, maze.value_at_point([1, 3]))


if __name__ == '__main__':
    unittest.main()

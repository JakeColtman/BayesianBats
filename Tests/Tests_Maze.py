import unittest
import random
from Maze import Maze


class MazeAssignmentAndGet(unittest.TestCase):
    def test_maze_assign_and_get(self):
        maze = Maze(5)
        new_val = random.randint(1, 6)
        maze.set_value_at_point([1, 3], new_val)
        self.assertEqual(new_val, maze.value_at_point([1, 3]))

    def test_next_point_in_direction(self):
        maze = Maze(5)
        basePoint = [2, 2]
        leftPoint = maze.next_point_in_direction(basePoint, "left")
        rightPoint = maze.next_point_in_direction(basePoint, "right")
        upPoint = maze.next_point_in_direction(basePoint, "up")
        downPoint = maze.next_point_in_direction(basePoint, "down")

        self.assertEqual(downPoint, [2, 3])
        self.assertEqual(upPoint, [2, 1])
        self.assertEqual(leftPoint, [1, 2])
        self.assertEqual(rightPoint, [3, 2])


if __name__ == '__main__':
    unittest.main()

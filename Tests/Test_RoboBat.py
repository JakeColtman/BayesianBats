import unittest
from RoboBat import RoboBat
from Maze import Maze


class RobotCreationAndMove(unittest.TestCase):
    def test_hardcoded_creation(self):
        robotPos = [1, 4]
        maze = Maze(7)
        bat = RoboBat(maze, robotPos)
        self.assertEqual(3, maze.value_at_point(robotPos))

    def test_robot_move_updates_maze(self):
        maze = Maze(7)
        robotPos = [1, 4]
        bat = RoboBat(maze, robotPos)
        bat.move_in_direction("LEFT")
        self.assertFalse(maze.value_at_point(robotPos) == 3)
        self.assertTrue(maze.value_at_point(bat.pos) == 3)

    def test_robot_move_changes_robotpos(self):
        maze = Maze(7)
        robotPos = [1, 4]
        bat = RoboBat(maze, robotPos)
        bat.move_in_direction("LEFT")
        robotPos != bat.pos


if __name__ == '__main__':
    unittest.main()

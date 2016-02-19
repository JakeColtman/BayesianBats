import unittest
from RoboBat import RoboBat
from Maze import Maze


class RobotCreationAndMove(unittest.TestCase):
    def test_hardcoded_creation(self):
        robot_pos = [1, 4]
        maze = Maze(7)
        bat = RoboBat(maze, robot_pos)
        self.assertEqual(3, maze.value_at_point(robot_pos))

    def test_robot_move_updates_maze(self):
        maze = Maze(7)
        robot_pos = [1, 4]
        bat = RoboBat(maze, robot_pos)
        bat.move_in_direction("left")
        self.assertFalse(maze.value_at_point(robot_pos) == 3)
        self.assertTrue(maze.value_at_point(bat.pos) == 3)

    def test_robot_move_changes_robotpos(self):
        maze = Maze(7)
        robot_pos = [1, 4]
        bat = RoboBat(maze, robot_pos)
        bat.move_in_direction("left")
        self.assertNotEqual(robot_pos, bat.pos)

    def test_robot_moves_in_right_direction(self):
        maze = Maze(7)
        robot_pos = [3, 4]
        bat = RoboBat(maze, robot_pos)
        bat.move_in_direction("left")
        self.assertEqual(bat.pos, [2, 4])


if __name__ == '__main__':
    unittest.main()

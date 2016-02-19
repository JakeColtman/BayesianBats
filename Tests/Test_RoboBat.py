import unittest
from RoboBat import RoboBat
from Maze import Maze
from Brain import Brain

class RobotCreationAndMove(unittest.TestCase):
    def test_hardcoded_creation(self):
        robot_pos = [1, 4]
        maze = Maze(7)
        brain = Brain(maze)
        bat = RoboBat(maze, robot_pos, brain)
        self.assertEqual(3, maze.value_at_point(robot_pos))

    def test_robot_move_updates_maze(self):
        maze = Maze(7)
        brain = Brain(maze)
        robot_pos = [1, 4]
        bat = RoboBat(maze, robot_pos, brain)
        bat.move_in_direction("left")
        self.assertFalse(maze.value_at_point(robot_pos) == 3)
        self.assertTrue(maze.value_at_point(bat.pos) == 3)

    def test_robot_move_changes_robotpos(self):
        maze = Maze(7)
        brain = Brain(maze)
        robot_pos = [1, 4]
        bat = RoboBat(maze, robot_pos, brain)
        bat.move_in_direction("left")
        self.assertNotEqual(robot_pos, bat.pos)

    def test_robot_moves_in_right_direction(self):
        maze = Maze(7)
        brain = Brain(maze)
        robot_pos = [3, 4]
        bat = RoboBat(maze, robot_pos, brain)
        bat.move_in_direction("left")
        self.assertEqual(bat.pos, [2, 4])


class RobotLooking(unittest.TestCase):
    def test_next_to_wall_returns_zero(self):
        maze = Maze(3)
        brain = Brain(maze)
        robot_pos = [1, 1]
        bat = RoboBat(maze, robot_pos, brain)
        self.assertEqual(bat.submit_observation("left"), 0)
        self.assertEqual(bat.submit_observation("down"), 0)
        self.assertEqual(bat.submit_observation("up"), 0)
        self.assertEqual(bat.submit_observation("right"), 0)

    def test_1_space_all_directions(self):
        maze = Maze(5)
        brain = Brain(maze)
        robot_pos = [2, 2]
        bat = RoboBat(maze, robot_pos, brain)
        self.assertEqual(bat.submit_observation("left"), 1)
        self.assertEqual(bat.submit_observation("down"), 1)
        self.assertEqual(bat.submit_observation("up"), 1)
        self.assertEqual(bat.submit_observation("right"), 1)

    def test_2_space_all_directions(self):
        maze = Maze(7)
        brain = Brain(maze)
        robot_pos = [3, 3]
        bat = RoboBat(maze, robot_pos, brain)
        self.assertEqual(bat.submit_observation("left"), 2)
        self.assertEqual(bat.submit_observation("down"), 2)
        self.assertEqual(bat.submit_observation("up"), 2)
        self.assertEqual(bat.submit_observation("right"), 2)

        if __name__ == '__main__':
            unittest.main()

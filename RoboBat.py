from Observation import Observation

class RoboBat:
    def __init__(self, maze, pos, brain):
        self.pos = pos
        self.maze = maze
        self.brain = brain
        self.maze.set_value_at_point(self.pos, 3)
        self.isHome = False

    def move_in_direction(self, direction):
        new_pos = self.maze.next_point_in_direction(self.pos, direction)
        self.maze.set_value_at_point(self.pos, 0)
        self.maze.set_value_at_point(new_pos, 3)
        self.pos = new_pos

    def submit_observation(self, direction):
        totalDistanceSeen = 0
        next_pos = self.maze.next_point_in_direction(self.pos, direction)
        while self.maze.value_at_point(next_pos) == 0:
            next_pos = self.maze.next_point_in_direction(next_pos, direction)
            totalDistanceSeen += 1
        observation = Observation(self.pos, totalDistanceSeen, direction)
        self.brain.accept_information(observation)
        return totalDistanceSeen

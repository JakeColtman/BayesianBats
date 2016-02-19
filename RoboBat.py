class RoboBat:
    def __init__(self, maze, pos):
        self.pos = pos
        self.maze = maze
        self.maze.set_value_at_point(self.pos, 3)
        self.isHome = False

    def move_in_direction(self, direction):
        new_pos = self.maze.next_point_in_direction(self.pos, direction)
        self.maze.set_value_at_point(self.pos, 0)
        self.maze.set_value_at_point(new_pos, 3)
        self.pos = new_pos

    def distance_to_objection_in_direction(self, direction):
        raise NotImplementedError()

class RoboBat:
    def __init__(self, maze, pos):
        self.pos = pos
        self.maze = maze
        self.maze.set_value_at_point(self.pos, 3)
        self.isHome = False

    def move_in_direction(self, direction):
        raise NotImplementedError()

    def distance_to_objection_in_direction(self, direction):
        raise NotImplementedError()

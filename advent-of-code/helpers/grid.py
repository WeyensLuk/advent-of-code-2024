from helpers.coordinate import Coordinate

class Grid:
    def __init__(self, grid):
        self.grid = grid

    def __str__(self):
        grid = ""
        for cell, _ in self.visit_all():
            grid += cell
        
        return grid

    def visit_all(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                yield self.grid[i][j], Coordinate(j, i)

    def is_out_of_bounds(self, position):
        return position.x < 0 or position.y < 0 or \
            position.x >= len(self.grid) or position.y >= len(self.grid)

    def set_cell(self, coord, value):
        self.grid[coord.y][coord.x] = value

    def get_cell(self, coord):
        if self.is_out_of_bounds(coord): return None
        return self.grid[coord.y][coord.x]
    
    @property
    def current_position(self):
        return self._current_position

    @current_position.setter
    def current_position(self, value):
        self._current_position = value

    @property
    def current_cell(self):
        return self.get_cell(self._current_position)

    @current_cell.setter
    def current_cell(self, value):
        self.set_cell(self._current_position, value)

    def navigate(self, coord):
        self._current_position.x += coord.x
        self._current_position.y += coord.y
        if self.is_out_of_bounds(self._current_position):
            self._current_position.x -= coord.x
            self._current_position.y -= coord.y
            return False

        return True
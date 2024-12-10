class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if type(other) is Coordinate:
            return self.x == other.x and self.y == other.y
        if type(other) is tuple:
            return self.x == other[0] and self.y == other[1]
        
        return False

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)

    def inverse(self):
        return Coordinate(self.x * -1, self.y * -1)

    def rotate_90degrees_clockwise(self):
        if self == NORTH: return EAST
        if self == EAST: return SOUTH
        if self == SOUTH: return WEST
        if self == WEST: return NORTH

    def as_tuple(self):
        return (self.x, self.y)

NORTH = Coordinate(0, -1)
NORTH_EAST = Coordinate(1, -1)
EAST = Coordinate(1, 0)
SOUTH_EAST = Coordinate(1, 1)
SOUTH = Coordinate(0, 1)
SOUTH_WEST = Coordinate(-1, 1)
WEST = Coordinate(-1, 0)
NORTH_WEST = Coordinate(-1, -1)

ORTHOGONAL_DIRECTIONS = [NORTH, EAST, SOUTH, WEST]
ALL_DIRECTIONS = [NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST]